"""
rerun_analysis.py  (revision, Action Tracker v1: H2, H4, H11, M11, M7)

Analyses 1-6 of revision/rerun/RERUN_ANALYSIS_PLAN.md on the output of
revision/rerun/rerun_conditions.py. No API call.

Measures:
- skeleton cosine with to_skeleton() and the ONNX all-MiniLM-L6-v2 encoder of
  revision/h2/h2_cosine_onnx.py (imported unchanged); the original C0 outputs are
  scored again as a check against results/full_per_row_metrics.csv;
- parser outcome with check() of revision/check_syntax.py (behave 1.3.3 parser).

Before any analysis the script checks every job against the committed inputs: the
prompt is rebuilt from data/ with the functions of rerun_conditions.py and its SHA-256
must equal the prompt_sha256 logged for that job (jobs run before this field existed
are counted separately).

The bootstrap interval for the median paired differences of analysis 1 is not in the
plan; it is added for Action Tracker M9 and labelled as such in the report.

Usage (from the repository root):
  python revision/rerun/rerun_analysis.py --onnx-dir <folder with model.onnx and tokenizer.json>
Outputs in revision/rerun/results/: rerun_report.txt, rerun_per_job.csv, rerun_h11_per_file.csv
"""
import argparse
import csv
import hashlib
import json
import os
import sys
from collections import Counter

import numpy as np
import pandas as pd
from scipy.stats import binom, binomtest, f as f_dist, t as t_dist, wilcoxon

sys.path[:0] = ["revision/h2", "revision", "revision/rerun"]
from h2_cosine_onnx import Encoder, to_skeleton  # noqa: E402
from check_syntax import check  # noqa: E402
import rerun_conditions as rc  # noqa: E402

T = 0.85
B = 10_000
C0_EX = {2, 102, 202}
ALL_EX = C0_EX | {86, 119, 203}
PRICE_IN, PRICE_OUT = 0.75e-6, 4.50e-6  # Standard list price per token, as in Section 3.3


def holm(p):
    # same as revision/h2/h2_analysis.py
    p = np.asarray(p, float)
    order = np.argsort(p)
    adj = np.empty_like(p)
    run = 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(p) - rank) * p[i]))
        adj[i] = run
    return adj


def mcnemar_exact(a, b):
    # same as revision/h2/h2_analysis.py: two-sided exact test on discordant pairs
    n01 = int((a & ~b).sum())
    n10 = int((~a & b).sum())
    n = n01 + n10
    p = 1.0 if n == 0 else min(1.0, 2 * binom.cdf(min(n01, n10), n, 0.5))
    return n01, n10, p


def boot_ci(x, stat, seed=2026):
    rng = np.random.default_rng(seed)
    return np.percentile([stat(x[rng.integers(0, len(x), len(x))]) for _ in range(B)], [2.5, 97.5])


def cp(k, n):
    ci = binomtest(int(k), int(n)).proportion_ci(method="exact")
    return ci.low, ci.high


def q(x):
    return np.quantile(x, [0.25, 0.5, 0.75])


def load_calls(path):
    last = {}
    with open(path, "rb") as f:
        for line in f.read().decode("utf-8", errors="replace").splitlines():
            try:
                e = json.loads(line)
            except ValueError:
                continue
            last[(e["condition"], e["rep"], e["id"])] = e
    return last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--onnx-dir", required=True)
    ap.add_argument("--calls", default="revision/rerun/rerun_calls.jsonl")
    ap.add_argument("--outdir", default="revision/rerun/results")
    x = ap.parse_args()
    os.makedirs(x.outdir, exist_ok=True)
    rep = []

    def out(s=""):
        rep.append(s)

    # ---- inputs and the run itself (M7) ----
    stories = {int(r["id"]): r for r in rc.read_csv("data/full_user_stories.csv")}
    gt = {int(r["id"]): r["gherkin_content"] for r in rc.read_csv("data/full_ground_truth.csv")}
    project = {i: r["project_name"] for i, r in stories.items()}

    def prompt_for(cond, r):  # same as in rerun_conditions.main()
        if cond == "C1":
            return rc.zero_shot_prompt(r["user_story"])
        e = rc.EXEMPLARS[cond].get(r["domain"], rc.EXEMPLARS[cond]["Social Network"])
        return rc.one_shot_prompt(stories[e]["user_story"], gt[e].replace("\\n", "\n"), r["user_story"])

    calls = load_calls(x.calls)
    expected = set(rc.all_jobs())
    missing = expected - set(calls)
    ok_prompt = bad_prompt = no_hash = 0
    for (c, r, i), e in calls.items():
        if "prompt_sha256" not in e:
            no_hash += 1
        elif e["prompt_sha256"] == rc.sha256_text(prompt_for(c, stories[i])):
            ok_prompt += 1
        else:
            bad_prompt += 1
    out("== Run ==")
    out(f"input sha256 (LF): stories {rc.file_sha256_lf('data/full_user_stories.csv')}, "
        f"reference {rc.file_sha256_lf('data/full_ground_truth.csv')}")
    out(f"jobs expected {len(expected)}, logged {len(calls)}, missing {len(missing)}")
    out(f"prompt_sha256 equals the prompt rebuilt from data/: {ok_prompt}; differs: {bad_prompt}; "
        f"not logged (pilot run before the field existed): {no_hash}")
    allv = list(calls.values())
    out(f"final status: {dict(Counter(e['status'] for e in allv))}")
    out(f"attempts: {dict(Counter(e['attempt'] for e in allv))}; logged errors: "
        f"{sum(len(e.get('errors', [])) for e in allv)}")
    out(f"response_model: {dict(Counter(e.get('response_model') for e in allv))}")
    out(f"system_fingerprint: {dict(Counter(e.get('system_fingerprint') for e in allv))}")
    out(f"finish_reason by condition: {dict(Counter((e['condition'], e.get('finish_reason')) for e in allv))}")
    ts = sorted(e["timestamp_utc"] for e in allv)
    out(f"first and last call (UTC): {ts[0]} .. {ts[-1]}")
    pt = sum(e.get("prompt_tokens") or 0 for e in allv)
    ct = sum(e.get("completion_tokens") or 0 for e in allv)
    out(f"tokens: prompt {pt}, completion {ct}; estimated cost at the Standard list price "
        f"${pt * PRICE_IN + ct * PRICE_OUT:.2f} (no cache discount; not an invoice)")
    cached = sum(e.get("cached_prompt_tokens") or 0 for e in allv)
    out(f"cached prompt tokens reported by the API: {cached}")

    # ---- per-job measures ----
    enc = Encoder(x.onnx_dir)
    cache = {}

    def emb(t):
        if t not in cache:
            cache[t] = enc.encode(t)
        return cache[t]

    ref_emb = {i: emb(to_skeleton(gt[i])) for i in gt}
    rows = []
    for (c, r, i), e in sorted(calls.items()):
        g = e.get("generated_gherkin") or ""
        okj = e["status"] == "OK"
        rows.append({"condition": c, "rep": r, "id": i, "project": project[i], "status": e["status"],
                     "finish_reason": e.get("finish_reason"), "completion_tokens": e.get("completion_tokens"),
                     "skeleton_cosine": float(emb(to_skeleton(g)) @ ref_emb[i]) if okj else np.nan,
                     "parse_status": check(g)["parse_status"] if okj else "FAIL", "text_sha256": rc.sha256_text(g)})
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(x.outdir, "rerun_per_job.csv"), index=False)

    # original C0 run, scored the same way
    csv.field_size_limit(2**31 - 1)
    with open("results/full_gpt54mini_output.csv", encoding="utf-8-sig", newline="") as f:
        orig_txt = {int(r["id"]): r["generated_gherkin"] for r in csv.DictReader(f)}
    orig = pd.DataFrame([{"id": i, "skeleton_cosine": float(emb(to_skeleton(t)) @ ref_emb[i]),
                          "parse_status": check(t)["parse_status"], "text": t} for i, t in orig_txt.items()])
    st = pd.read_csv("results/full_per_row_metrics.csv")[["id", "skeleton_cosine"]]
    chk = orig.merge(st, on="id", suffixes=("", "_st"))
    out(f"check: original C0 rescored with ONNX vs results/full_per_row_metrics.csv, "
        f"max abs diff {(chk.skeleton_cosine - chk.skeleton_cosine_st).abs().max():.2e}")

    r1 = df[df.rep == 1]

    def wide(col, ids, conds):
        w = r1[r1.id.isin(ids)].pivot(index="id", columns="condition", values=col)
        return w[conds].loc[sorted(ids)]

    def describe(xv, passed, label):
        x_ = xv[~np.isnan(xv)]
        q1, med, q3 = q(x_)
        k = int((x_ >= T).sum())
        lo, hi = cp(k, len(xv))
        plo, phi = cp(passed, len(xv))
        return (f"{label}: n {len(xv)} (cosine n {len(x_)}), median {med:.4f}, IQR {q3 - q1:.4f} "
                f"[{q1:.4f}, {q3:.4f}], >= 0.85 {k} ({k / len(xv):.1%}, 95% CI {lo:.1%}-{hi:.1%}), "
                f"parser PASS {passed}/{len(xv)} ({passed / len(xv):.2%}, 95% CI {plo:.2%}-{phi:.2%})")

    # ---- analysis 1: same-time ablation (H2) ----
    ids255 = [i for i in range(1, 262) if i not in ALL_EX]
    out("")
    out("== 1. Same-time ablation, rep 1, 255 files (H2) ==")
    cos = wide("skeleton_cosine", ids255, ["C0", "C1", "C2"])
    par = wide("parse_status", ids255, ["C0", "C1", "C2"]) == "PASS"
    for c in ["C0", "C1", "C2"]:
        out(describe(cos[c].to_numpy(float), int(par[c].sum()), c))
    res = []
    for c in ["C1", "C2"]:
        m = cos[[c, "C0"]].dropna()
        d = (m[c] - m["C0"]).to_numpy()
        w = wilcoxon(m[c], m["C0"], alternative="two-sided")
        n01, n10, pm = mcnemar_exact(par["C0"].to_numpy(), par[c].to_numpy())
        lo, hi = boot_ci(d, np.median)
        res.append((c, len(d), int((d > 0).sum()), int((d < 0).sum()), np.median(d), lo, hi, w.statistic, w.pvalue,
                    n01, n10, pm))
    wh, mh = holm([r_[8] for r_ in res]), holm([r_[11] for r_ in res])
    for r_, a, b in zip(res, wh, mh):
        out(f"{r_[0]} vs C0: n {r_[1]}, higher {r_[2]}, lower {r_[3]}, median paired diff {r_[4]:+.4f} "
            f"(bootstrap 95% CI {r_[5]:+.4f} to {r_[6]:+.4f}; added for M9, not in the plan); "
            f"Wilcoxon W {r_[7]:.1f}, p {r_[8]:.3g}, Holm p {a:.3g}; McNemar C0-only {r_[9]}, "
            f"{r_[0]}-only {r_[10]}, p {r_[11]:.3g}, Holm p {b:.3g}")
    for pname in ["Sylius", "Apache Fineract", "Diaspora"]:
        sub = [i for i in ids255 if project[i] == pname]
        meds = {c: np.nanmedian(cos.loc[sub, c]) for c in ["C0", "C1", "C2"]}
        share = {c: (cos.loc[sub, c] >= T).mean() for c in ["C0", "C1", "C2"]}
        out(f"  {pname} (n {len(sub)}): median " + ", ".join(f"{c} {v:.4f}" for c, v in meds.items())
            + "; >= 0.85 " + ", ".join(f"{c} {v:.1%}" for c, v in share.items())
            + "; PASS " + ", ".join(f"{c} {int(par.loc[sub, c].sum())}" for c in ["C0", "C1", "C2"]))
    tok = r1[r1.id.isin(ids255)].groupby("condition").completion_tokens.median()
    out(f"median completion tokens: {tok.round(1).to_dict()}")

    # ---- analysis 2: RQ1 and RQ2 on the new C0 ----
    ids258 = [i for i in range(1, 262) if i not in C0_EX]
    out("")
    out("== 2. RQ1 and RQ2 on the new C0, rep 1, 258 files ==")
    c0 = r1[(r1.condition == "C0") & r1.id.isin(ids258)]
    xv = c0.skeleton_cosine.dropna().to_numpy(float)
    above, below = int((xv > T).sum()), int((xv < T).sum())
    sign_p = binomtest(above, above + below, 0.5, alternative="greater").pvalue
    lo, hi = boot_ci(xv, np.median)
    out(f"cosine n {len(xv)}, median {np.median(xv):.4f} (bootstrap 95% CI {lo:.4f}-{hi:.4f}), above {above}, "
        f"below {below}, exact sign test one-sided p {sign_p:.3g}, Wilcoxon one-sided p "
        f"{wilcoxon(xv - T, alternative='greater').pvalue:.3g}, delta {(above - below) / len(xv):.4f}")
    k, n = int((c0.parse_status == "PASS").sum()), len(c0)
    plo, phi = cp(k, n)
    out(f"parser PASS {k}/{n} ({k / n:.2%}, 95% CI {plo:.2%}-{phi:.2%}), exact binomial vs 0.80 one-sided p "
        f"{binomtest(k, n, 0.80, alternative='greater').pvalue:.3g}, risk difference {k / n - 0.8:+.4f} "
        f"(95% CI {plo - 0.8:+.4f} to {phi - 0.8:+.4f})")

    # ---- analysis 3: change over time ----
    out("")
    out("== 3. New C0 (rep 1) vs original C0, 258 files ==")
    m = c0[["id", "skeleton_cosine", "parse_status", "text_sha256"]].merge(
        orig[orig.id.isin(ids258)], on="id", suffixes=("_new", "_orig"))
    same = int((m.text_sha256 == m.text.map(rc.sha256_text)).sum())
    d = (m.skeleton_cosine_new - m.skeleton_cosine_orig).dropna().to_numpy()
    q1, med, q3 = q(d)
    out(f"byte-identical outputs {same}/{len(m)}; cosine diff new - original median {med:+.4f}, IQR "
        f"[{q1:+.4f}, {q3:+.4f}], mean abs {np.abs(d).mean():.4f}, paired Wilcoxon two-sided p "
        f"{wilcoxon(d).pvalue:.3g} (n {len(d)})")
    out(f"parser outcome differs {int((m.parse_status_new != m.parse_status_orig).sum())}; side of 0.85 differs "
        f"{int(((m.skeleton_cosine_new >= T) != (m.skeleton_cosine_orig >= T)).sum())}")

    # ---- analysis 4: run-to-run variation (H4) ----
    sub = df[df.id.isin(rc.SUBSET) & df.condition.isin(["C0", "C1", "C2"])]
    out("")
    out(f"== 4. Run-to-run variation, {len(rc.SUBSET)} files x {rc.REPS} reps (H4) ==")
    for c in ["C0", "C1", "C2"]:
        s = sub[sub.condition == c]
        nrep = s.groupby("id").size()
        g = s.dropna(subset=["skeleton_cosine"]).groupby("id")
        ident = int(s.groupby("id").text_sha256.nunique().eq(1).sum())
        sd = g.skeleton_cosine.std(ddof=1)
        within_sd = float(np.sqrt(g.skeleton_cosine.var(ddof=1).mean()))
        full = [i for i, v in g.size().items() if v == rc.REPS]
        Y = np.array([s[(s.id == i)].skeleton_cosine.to_numpy(float) for i in full])
        nf, kk = Y.shape
        msb = kk * ((Y.mean(1) - Y.mean()) ** 2).sum() / (nf - 1)
        msw = ((Y - Y.mean(1, keepdims=True)) ** 2).sum() / (nf * (kk - 1))
        icc = (msb - msw) / (msb + (kk - 1) * msw)
        F = msb / msw if msw > 0 else np.inf
        if np.isfinite(F):
            fl, fu = F / f_dist.ppf(0.975, nf - 1, nf * (kk - 1)), F * f_dist.ppf(0.975, nf * (kk - 1), nf - 1)
            icc_ci = f"[{(fl - 1) / (fl + kk - 1):.4f}, {(fu - 1) / (fu + kk - 1):.4f}]"
        else:
            icc_ci = "[not defined: no within-file variation]"
        pchange = int(s.groupby("id").parse_status.nunique().gt(1).sum())
        side = int(s.dropna(subset=["skeleton_cosine"]).assign(a=lambda z: z.skeleton_cosine >= T)
                   .groupby("id").a.nunique().gt(1).sum())
        out(f"{c}: files {len(nrep)} (all {rc.REPS} reps OK for {len(full)}); 5 identical outputs {ident}; "
            f"per-file SD median {sd.median():.4f} (max {sd.max():.4f}); pooled within-file SD {within_sd:.4f}; "
            f"ICC(1,1) {icc:.4f} 95% CI {icc_ci}; parser outcome changes {pchange}; side of 0.85 changes {side}")

    # ---- analysis 5: within- and between-prompt variation (H11) ----
    out("")
    out("== 5. Within- and between-prompt variation, C0 and C2 on the subset (H11) ==")
    fl_ids = [i for i in rc.SUBSET if all(
        sub[(sub.condition == c) & (sub.id == i)].skeleton_cosine.notna().sum() == rc.REPS for c in ["C0", "C2"])]
    Y = np.array([[sub[(sub.condition == c) & (sub.id == i)].skeleton_cosine.to_numpy(float) for c in ["C0", "C2"]]
                  for i in fl_ids])  # files x prompts x reps
    a, p_, r_ = Y.shape
    gm = Y.mean()
    mf, mp, mfp = Y.mean((1, 2)), Y.mean((0, 2)), Y.mean(2)
    ss_w = ((Y - mfp[:, :, None]) ** 2).sum()
    ss_int = r_ * ((mfp - mf[:, None] - mp[None, :] + gm) ** 2).sum()
    ss_f = p_ * r_ * ((mf - gm) ** 2).sum()
    ms_w = ss_w / (a * p_ * (r_ - 1))
    ms_int = ss_int / ((a - 1) * (p_ - 1))
    ms_f = ss_f / (a - 1)
    eff = mfp[:, 1] - mfp[:, 0]
    tcrit = t_dist.ppf(0.975, a - 1)
    se = eff.std(ddof=1) / np.sqrt(a)
    out(f"files with all reps in both prompts: {a}")
    out(f"within-prompt (residual) variance {ms_w:.6f} (SD {np.sqrt(ms_w):.4f}); file x prompt variance component "
        f"{max(0.0, (ms_int - ms_w) / r_):.6f}; file variance component {max(0.0, (ms_f - ms_int) / (p_ * r_)):.6f}")
    out(f"between-prompt effect (mean over files of C2 mean - C0 mean) {eff.mean():+.4f}, paired t 95% CI "
        f"{eff.mean() - tcrit * se:+.4f} to {eff.mean() + tcrit * se:+.4f}; F(prompt x file vs within) "
        f"{ms_int / ms_w if ms_w > 0 else float('inf'):.3f}")
    above0 = below0 = incl = 0
    per_file = []
    for i, y in zip(fl_ids, Y):
        d_ = y[1].mean() - y[0].mean()
        v0, v1 = y[0].var(ddof=1) / r_, y[1].var(ddof=1) / r_
        se_ = np.sqrt(v0 + v1)
        if se_ == 0:
            lo_, hi_ = d_, d_
        else:
            dfw = (v0 + v1) ** 2 / ((v0 ** 2 + v1 ** 2) / (r_ - 1)) if (v0 > 0 and v1 > 0) else r_ - 1
            h = t_dist.ppf(0.975, dfw) * se_
            lo_, hi_ = d_ - h, d_ + h
        above0 += lo_ > 0
        below0 += hi_ < 0
        incl += lo_ <= 0 <= hi_
        per_file.append({"id": i, "project": project[i], "diff_C2_minus_C0": d_, "ci_low": lo_, "ci_high": hi_})
    out(f"per-file Welch 95% CI of C2 - C0: wholly above 0 {above0}, wholly below 0 {below0}, include 0 {incl}")
    pf = pd.DataFrame(per_file)
    pf.to_csv(os.path.join(x.outdir, "rerun_h11_per_file.csv"), index=False)
    for pname, g in pf.groupby("project"):
        out(f"  {pname} (n {len(g)}): mean effect {g.diff_C2_minus_C0.mean():+.4f}; above 0 "
            f"{int((g.ci_low > 0).sum())}, below 0 {int((g.ci_high < 0).sum())}")

    # ---- analysis 6: capped condition (M11) ----
    out("")
    out("== 6. Capped condition C0cap vs new C0, rep 1, 258 files (M11) ==")
    cap = r1[(r1.condition == "C0cap") & r1.id.isin(ids258)]
    out(f"stopped by the cap (finish_reason = length): {int((cap.finish_reason == 'length').sum())}/{len(cap)}")
    kc = int((cap.parse_status == "PASS").sum())
    lo, hi = cp(kc, len(cap))
    out(f"parser PASS {kc}/{len(cap)} ({kc / len(cap):.2%}, 95% CI {lo:.2%}-{hi:.2%}); median cosine "
        f"{cap.skeleton_cosine.median():.4f}")
    cw = wide("skeleton_cosine", ids258, ["C0", "C0cap"])
    pw_ = wide("parse_status", ids258, ["C0", "C0cap"]) == "PASS"
    mm = cw.dropna()
    n01, n10, pm = mcnemar_exact(pw_["C0"].to_numpy(), pw_["C0cap"].to_numpy())
    out(f"C0cap vs C0: median paired diff {np.median(mm.C0cap - mm.C0):+.4f}, Wilcoxon two-sided p "
        f"{wilcoxon(mm.C0cap, mm.C0).pvalue:.3g} (n {len(mm)}); McNemar C0-only {n01}, C0cap-only {n10}, p {pm:.3g}")
    stopped = cap[cap.finish_reason == "length"].id
    out(f"among the files stopped by the cap: parser PASS {int((cap[cap.id.isin(stopped)].parse_status == 'PASS').sum())}"
        f"/{len(stopped)}")

    with open(os.path.join(x.outdir, "rerun_report.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
