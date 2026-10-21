"""
h2_run_prompts.py  (revision, Action Tracker H2/M1)

Runs the two new prompt conditions on all 261 user stories with the SAME model,
temperature, system messages, prompt wording and output clean-up as the
original run (scripts/run_experiment.ipynb, code cells 5, 7 and 9, counted from 0). Only the example part
of the prompt changes:

  C1  zero-shot: no example user story / Gherkin in the prompt.
  C2  one-shot with a different exemplar per domain, drawn once with
      numpy.random.default_rng(2026).choice over the sorted ids of each domain
      (domains in the order E-commerce, Finance/Banking, Social Network),
      excluding the original exemplars 2, 102, 202. Result: 86, 119, 203.
      These ids are fixed here BEFORE any C2 output exists.

As in the original run there is no max_tokens cap (see E15).
Analysis must exclude every id used as an exemplar in any condition:
2, 102, 202, 86, 119, 203 (C0, C1 and C2 on the same 255 ids).

Each call is logged with the model name the API returned (response.model),
UTC timestamp, finish_reason, usage (including cached prompt tokens when the
API reports them) and status. Failed calls are retried up to 5 times with
backoff; if all fail the row is written with status ERROR and an empty output,
never with invented text. Cost is NOT computed here; compute it later from the
logged usage and the verified price page.

Requirements: Python 3.9+, `pip install openai`. The API key is read from the
environment variable OPENAI_API_KEY; never paste it into this file.

Usage (from the repository root):
  python revision/h2/h2_run_prompts.py --condition C1
  python revision/h2/h2_run_prompts.py --condition C2
Pilot first on one story per domain:  --ids 1,101,201
Re-running the same command resumes: ids already written with status OK are skipped.

Comment-only fix on 16 Oct 2026 after the C1/C2 runs: cell numbers corrected.
The runs used the version with SHA-256 f634130978c4a7a4...67fef (code identical).
"""
import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone

MODEL = "gpt-5.4-mini-2026-03-17"
TEMPERATURE = 0
C0_EXEMPLARS = {"E-commerce": 2, "Finance/Banking": 102, "Social Network": 202}
C2_EXEMPLARS = {"E-commerce": 86, "Finance/Banking": 119, "Social Network": 203}

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
    # The one-shot wording with the example block and the reference to it removed.
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--condition", required=True, choices=["C1", "C2"])
    ap.add_argument("--stories", default="data/full_user_stories.csv")
    ap.add_argument("--gt", default="data/full_ground_truth.csv")
    ap.add_argument("--outdir", default="revision/h2")
    ap.add_argument("--limit", type=int, help="only the first N stories (for a pilot)")
    ap.add_argument("--ids", help="comma-separated ids to run (for a pilot)")
    x = ap.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("Set OPENAI_API_KEY in the environment first.")
    from openai import OpenAI
    client = OpenAI(api_key=key)

    stories = read_csv(x.stories)
    gt = {int(r["id"]): r["gherkin_content"] for r in read_csv(x.gt)}
    us = {int(r["id"]): r["user_story"] for r in stories}

    def example(i):  # same as get_sample() in cell 5
        return us[i], gt[i].replace("\\n", "\n")

    out_csv = os.path.join(x.outdir, f"h2_{x.condition}_output.csv")
    log_path = os.path.join(x.outdir, f"h2_{x.condition}_api_log.jsonl")
    os.makedirs(x.outdir, exist_ok=True)
    done = {}
    if os.path.exists(out_csv):
        done = {int(r["id"]): r for r in read_csv(out_csv)}
    config = {"condition": x.condition, "model_requested": MODEL, "temperature": TEMPERATURE, "max_tokens": None,
              "exemplars": C2_EXEMPLARS if x.condition == "C2" else None,
              "exclude_in_analysis": sorted(set(C0_EXEMPLARS.values()) | set(C2_EXEMPLARS.values())),
              "started_utc": datetime.now(timezone.utc).isoformat()}
    with open(os.path.join(x.outdir, f"h2_{x.condition}_config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, indent=1)

    todo = stories[: x.limit] if x.limit else stories
    if x.ids:
        keep = {int(v) for v in x.ids.split(",")}
        todo = [r for r in todo if int(r["id"]) in keep]
    for n, r in enumerate(todo, 1):
        i, domain = int(r["id"]), r["domain"]
        if i in done and done[i]["status"] == "OK":
            continue
        if x.condition == "C1":
            prompt = zero_shot_prompt(r["user_story"])
        else:
            ex_us, ex_gk = example(C2_EXEMPLARS.get(domain, C2_EXEMPLARS["Social Network"]))
            prompt = one_shot_prompt(ex_us, ex_gk, r["user_story"])
        entry, text = {"id": i, "condition": x.condition}, ""
        for attempt in range(1, 6):
            try:
                resp = client.chat.completions.create(
                    model=MODEL, temperature=TEMPERATURE,
                    messages=[{"role": "system", "content": sys_msg(domain)}, {"role": "user", "content": prompt}])
                text = clean(resp.choices[0].message.content)
                u = resp.usage
                details = getattr(u, "prompt_tokens_details", None)
                entry.update({"status": "OK" if text else "EMPTY", "attempt": attempt,
                              "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                              "response_model": resp.model, "response_id": resp.id,
                              "finish_reason": resp.choices[0].finish_reason,
                              "prompt_tokens": u.prompt_tokens, "completion_tokens": u.completion_tokens,
                              "cached_prompt_tokens": getattr(details, "cached_tokens", None) if details else None})
                break
            except Exception as e:  # noqa: BLE001  log and retry
                entry.update({"status": "ERROR", "attempt": attempt, "error": f"{type(e).__name__}: {e}"[:500],
                              "timestamp_utc": datetime.now(timezone.utc).isoformat()})
                time.sleep(min(60, 5 * 2 ** (attempt - 1)))
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        done[i] = {"id": i, "status": entry["status"], "generated_gherkin": text}
        with open(out_csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, ["id", "status", "generated_gherkin"])
            w.writeheader()
            w.writerows(done[k] for k in sorted(done))
        print(f"{n}/{len(todo)} id={i} {entry['status']}", flush=True)
        time.sleep(1)
    bad = [k for k, v in done.items() if v["status"] != "OK"]
    print(f"Finished. {len(done)} rows, not OK: {bad}")


if __name__ == "__main__":
    main()
