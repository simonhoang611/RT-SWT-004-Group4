"""
rerun_conditions.py  (revision, Action Tracker v1: H2, H4, H11, M11)

Runs C0, C1, C2 and the capped condition C0cap in one session, interleaved,
with one logging path, so that the prompt conditions are compared at the same
time (H2), run-to-run variation is measured (H4, H11) and the 1,500-token cap
planned in the research proposal is tried (M11). The analysis plan is
revision/rerun/RERUN_ANALYSIS_PLAN.md; it was fixed before any output existed.

Conditions (model, temperature, system messages, prompt wording and output
clean-up as in scripts/run_experiment.ipynb and revision/h2/h2_run_prompts.py):
  C0     same-project one-shot, exemplars 2, 102, 202 (the original condition)
  C1     zero-shot
  C2     same-project one-shot, exemplars 86, 119, 203
  C0cap  C0 with max_completion_tokens = 1500

Jobs:
  rep 1      all 261 stories, all four conditions
  reps 2-5   the 60-story stratified subset SUBSET (20 per project, drawn with
             numpy.random.default_rng(20261028).choice over the sorted ids of each
             project that are not an exemplar in C0 or C2), conditions C0, C1, C2
All jobs are shuffled once with random.Random(SEED) so that the conditions are
interleaved in time.

Failure policy (M7): each request has a 600 s timeout and the client's own
retries are switched off, so every attempt is counted here. A job is tried at
most 5 times; after a failed attempt (any exception, including rate limits and
timeouts, or an output that is empty after clean-up) the job waits 5, 10, 20 or
40 s. A job that fails 5 times is written with status ERROR or EMPTY and an
empty output, never with invented text. Re-running the same command retries
only the jobs that are not OK.

Requirements: Python 3.9+, `pip install openai`. The API key is read from the
environment variable OPENAI_API_KEY; never paste it into this file.

Usage (from the repository root):
  python revision/rerun/rerun_conditions.py --pilot     # 12 calls: ids 1, 101, 201, rep 1
  python revision/rerun/rerun_conditions.py             # everything else (1,752 calls)
"""
import argparse
import csv
import hashlib
import json
import os
import platform
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

MODEL = "gpt-5.4-mini-2026-03-17"
TEMPERATURE = 0
CAP = 1500
TIMEOUT_S = 600
ATTEMPTS = 5
WAITS_S = [5, 10, 20, 40]
SEED = 20261028
REPS = 5
CONDITIONS = ["C0", "C1", "C2", "C0cap"]
REPEATED = ["C0", "C1", "C2"]
EXEMPLARS = {
    "C0": {"E-commerce": 2, "Finance/Banking": 102, "Social Network": 202},
    "C2": {"E-commerce": 86, "Finance/Banking": 119, "Social Network": 203},
}
EXEMPLARS["C0cap"] = EXEMPLARS["C0"]
SUBSET = [3, 7, 9, 11, 15, 19, 21, 45, 51, 56, 61, 64, 77, 83, 88, 91, 92, 94, 97, 99,
          103, 104, 105, 107, 109, 118, 128, 129, 133, 135, 141, 154, 161, 163, 164, 172, 175, 178, 190, 198,
          206, 209, 212, 213, 214, 216, 220, 223, 227, 229, 233, 234, 239, 240, 243, 249, 251, 257, 258, 260]
PILOT_IDS = [1, 101, 201]

# System messages copied verbatim from scripts/run_experiment.ipynb, cell 7.
SYS = {
    "E-commerce": "You are an expert QA Engineer for Sylius, an E-commerce platform using the Behat framework. You write business-focused Gherkin tests. Focus on product variants, shopping carts, and UI interactions using business language.",
    "Finance/Banking": "You are an expert QA Engineer for Apache Fineract, a core banking system. Your signature style is using detailed Data Tables in the Background block to mock extensive financial data (e.g. LoanProduct, clients). Write highly technical, data-driven Gherkin.",
}
SYS_SOCIAL = "You are an expert QA Engineer for Diaspora, a Ruby on Rails social network using Capybara and Cucumber. Your signature style is writing concrete UI automation steps using CSS selectors (e.g. 'within \".class\"') and exact UI actions."


def sys_msg(domain):
    # The notebook uses an if / elif / else, so any other domain gets the Diaspora message.
    return SYS.get(domain, SYS_SOCIAL)


def one_shot_prompt(ex_us, ex_gk, user_story):
    # Copied verbatim from scripts/run_experiment.ipynb, cell 7.
    return f"""Generate a BDD Gherkin file for the following user story. 
Follow the exact style, wording, and conventions shown in the Example.

EXAMPLE USER STORY:
{ex_us}

EXAMPLE GHERKIN:
{ex_gk}

---
NOW GENERATE FOR THIS USER STORY:
{user_story}
"""


def zero_shot_prompt(user_story):
    # Same as revision/h2/h2_run_prompts.py.
    return f"""Generate a BDD Gherkin file for the following user story. 

---
NOW GENERATE FOR THIS USER STORY:
{user_story}
"""


def clean(text):
    # Same clean-up as scripts/run_experiment.ipynb, cell 9.
    t = (text or "").strip()
    if t.startswith("```gherkin"):
        t = t.replace("```gherkin", "", 1)
    if t.startswith("```"):
        t = t.replace("```", "", 1)
    if t.endswith("```"):
        t = t[:-3]
    return t.strip()


def read_csv(path):
    csv.field_size_limit(2**31 - 1)  # some GT files are longer than the default limit
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def all_jobs():
    jobs = [(c, 1, i) for c in CONDITIONS for i in range(1, 262)]
    jobs += [(c, r, i) for c in REPEATED for r in range(2, REPS + 1) for i in SUBSET]
    random.Random(SEED).shuffle(jobs)
    return jobs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", action="store_true", help="only ids 1, 101, 201 of rep 1")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--stories", default="data/full_user_stories.csv")
    ap.add_argument("--gt", default="data/full_ground_truth.csv")
    ap.add_argument("--outdir", default="revision/rerun")
    x = ap.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("Set OPENAI_API_KEY in the environment first.")
    import openai
    client = openai.OpenAI(api_key=key, timeout=TIMEOUT_S, max_retries=0)

    stories = {int(r["id"]): r for r in read_csv(x.stories)}
    gt = {int(r["id"]): r["gherkin_content"] for r in read_csv(x.gt)}
    if len(stories) != 261 or len(gt) != 261:
        sys.exit("Expected 261 stories and 261 reference files.")

    def prompt_for(cond, r):
        if cond == "C1":
            return zero_shot_prompt(r["user_story"])
        e = EXEMPLARS[cond].get(r["domain"], EXEMPLARS[cond]["Social Network"])
        # same as get_sample() in cell 5
        return one_shot_prompt(stories[e]["user_story"], gt[e].replace("\\n", "\n"), r["user_story"])

    os.makedirs(x.outdir, exist_ok=True)
    calls_path = os.path.join(x.outdir, "rerun_calls.jsonl")
    done = set()
    if os.path.exists(calls_path):
        with open(calls_path, "rb") as f:
            data = f.read()
        if data and not data.endswith(b"\n"):  # a run was stopped while writing a line
            with open(calls_path, "ab") as f:
                f.write(b"\n")
        broken = 0
        for line in data.decode("utf-8", errors="replace").splitlines():
            try:
                e = json.loads(line)
            except ValueError:
                broken += 1  # kept in the file, ignored here; the job runs again
                continue
            if e["status"] == "OK":
                done.add((e["condition"], e["rep"], e["id"]))
        if broken:
            print(f"{broken} incomplete line(s) in {calls_path} ignored", flush=True)

    with open(os.path.abspath(__file__), "rb") as f:
        script_sha = hashlib.sha256(f.read()).hexdigest()
    config = {"model_requested": MODEL, "temperature": TEMPERATURE, "cap_C0cap": CAP,
              "timeout_s": TIMEOUT_S, "client_max_retries": 0, "attempts": ATTEMPTS, "waits_s": WAITS_S,
              "seed": SEED, "reps": REPS, "subset": SUBSET, "exemplars": EXEMPLARS,
              "workers": x.workers, "pilot": x.pilot, "script_sha256": script_sha,
              "openai_version": openai.__version__, "python": platform.python_version(),
              "started_utc": datetime.now(timezone.utc).isoformat()}
    with open(os.path.join(x.outdir, "rerun_config.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(config) + "\n")

    jobs = all_jobs()
    if x.pilot:
        jobs = [j for j in jobs if j[1] == 1 and j[2] in PILOT_IDS]
    todo = [j for j in jobs if j not in done]
    print(f"{len(jobs)} jobs, {len(jobs) - len(todo)} already OK, {len(todo)} to run", flush=True)

    lock = threading.Lock()
    counter = {"n": 0, "bad": []}

    def run(job):
        cond, rep, i = job
        r = stories[i]
        kwargs = {"model": MODEL, "temperature": TEMPERATURE,
                  "messages": [{"role": "system", "content": sys_msg(r["domain"])},
                               {"role": "user", "content": prompt_for(cond, r)}]}
        if cond == "C0cap":
            kwargs["max_completion_tokens"] = CAP
        entry, text, errors = {"condition": cond, "rep": rep, "id": i}, "", []
        for attempt in range(1, ATTEMPTS + 1):
            t0 = time.time()
            try:
                resp = client.chat.completions.create(**kwargs)
                text = clean(resp.choices[0].message.content)
                u = resp.usage
                pd_ = getattr(u, "prompt_tokens_details", None)
                cd_ = getattr(u, "completion_tokens_details", None)
                entry.update({"status": "OK" if text else "EMPTY", "attempt": attempt,
                              "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                              "latency_s": round(time.time() - t0, 2),
                              "response_model": resp.model, "response_id": resp.id,
                              "system_fingerprint": getattr(resp, "system_fingerprint", None),
                              "service_tier": getattr(resp, "service_tier", None),
                              "finish_reason": resp.choices[0].finish_reason,
                              "prompt_tokens": u.prompt_tokens, "completion_tokens": u.completion_tokens,
                              "cached_prompt_tokens": getattr(pd_, "cached_tokens", None) if pd_ else None,
                              "reasoning_tokens": getattr(cd_, "reasoning_tokens", None) if cd_ else None})
            except Exception as e:  # noqa: BLE001  log and retry
                entry.update({"status": "ERROR", "attempt": attempt,
                              "timestamp_utc": datetime.now(timezone.utc).isoformat()})
                errors.append(f"{type(e).__name__}: {e}"[:300])
            if entry["status"] == "OK":
                break
            if entry["status"] == "EMPTY":
                errors.append("EMPTY output after clean-up")
            if attempt < ATTEMPTS:
                time.sleep(WAITS_S[attempt - 1])
        entry["errors"] = errors
        entry["generated_gherkin"] = text
        with lock:
            with open(calls_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            counter["n"] += 1
            if entry["status"] != "OK":
                counter["bad"].append(job)
            print(f"{counter['n']}/{len(todo)} {cond} rep={rep} id={i} {entry['status']}", flush=True)
        time.sleep(1)

    with ThreadPoolExecutor(max_workers=x.workers) as ex:
        list(ex.map(run, todo))
    print(f"Finished. {len(todo)} jobs run, not OK: {counter['bad']}")


if __name__ == "__main__":
    main()
