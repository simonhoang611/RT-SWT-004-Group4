"""
h2_analysis.py  (revision, Action Tracker H2/M1)

Implements revision/h2/H2_ANALYSIS_PLAN.md (fixed 16 Oct 2026 before any
C1/C2 output existed, SHA-256 in H2_ANALYSIS_PLAN.sha256). Nothing here goes
beyond that plan.

Inputs (from the repository root):
  revision/h2/h2_cosine_per_file.csv          from h2_cosine_onnx.py
  revision/h2/h2_syntax_C0.csv, _C1, _C2      from revision/check_syntax.py
  revision/h2/h2_C1_api_log.jsonl, _C2        completion tokens
  results/full_api_log.jsonl                   completion tokens of C0
  data/full_user_stories.csv                   project of each id
Outputs: revision/h2/h2_results_table.csv, h2_results_by_project.csv, h2_report.txt

Usage:  python revision/h2/h2_analysis.py
"""
import json

import numpy as np
import pandas as pd
from scipy.stats import binom, binomtest, wilcoxon

EXCLUDE = {2, 102, 202, 86, 119, 203}
T = 0.85
D = "revision/h2/"


def holm(p):
    p = np.asarray(p, float)
    order = np.argsort(p)
    adj = np.empty_like(p)
    run = 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(p) - rank) * p[i]))
        adj[i] = run
    return adj


def mcnemar_exact(a, b):
    # a, b: boolean PASS vectors on the same files. Two-sided exact test on discordant pairs.
    n01 = int((a & ~b).sum())
    n10 = int((~a & b).sum())
    n = n01 + n10
    p = 1.0 if n == 0 else min(1.0, 2 * binom.cdf(min(n01, n10), n, 0.5))
    return n01, n10, p


def tokens(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        e = json.loads(line)
        if e.get("status", "OK") == "OK" and "completion_tokens" in e:
            out[int(e["id"])] = e["completion_tokens"]
    return out


def main():
    proj = pd.read_csv("data/full_user_stories.csv")[["id", "project_name"]]
    cos = pd.read_csv(D + "h2_cosine_per_file.csv")
    cos = cos[~cos.id.isin(EXCLUDE)].merge(proj, on="id")
    wide = cos.pivot(index="id", columns="condition", values="skeleton_cosine")
    ids = sorted(wide.index)
    assert len(ids) == 255 and not wide.isna().any().any()

    syn = {c: pd.read_csv(D + f"h2_syntax_{c}.csv").set_index("id").loc[ids, "parse_status"].eq("PASS").values
           for c in ["C0", "C1", "C2"]}
    tok = {"C0": tokens("results/full_api_log.jsonl"), "C1": tokens(D + "h2_C1_api_log.jsonl"),
           "C2": tokens(D + "h2_C2_api_log.jsonl")}

    rows, pw = [], []
    for c in ["C0", "C1", "C2"]:
        x = wide[c].values
        k = int((x >= T).sum())
        ci = binomtest(k, len(x)).proportion_ci(method="exact")
        npass = int(syn[c].sum())
        sci = binomtest(npass, len(x)).proportion_ci(method="exact")
        chars = cos[cos.condition == c].set_index("id").loc[ids, "gen_chars"]
        rows.append({"condition": c, "N": len(x), "median": np.median(x),
                     "Q1": np.percentile(x, 25), "Q3": np.percentile(x, 75),
                     "n_ge_0.85": k, "share_ge_0.85": k / len(x), "ci_low": ci.low, "ci_high": ci.high,
                     "wilcoxon_p_greater_0.85": wilcoxon(x - T, alternative="greater").pvalue,
                     "parse_pass": npass, "parse_rate": npass / len(x), "parse_ci_low": sci.low,
                     "parse_ci_high": sci.high, "parse_fail_ids": " ".join(str(i) for i, ok in zip(ids, syn[c]) if not ok),
                     "median_gen_chars": float(np.median(chars)),
                     "median_completion_tokens": float(np.median([tok[c][i] for i in ids]))})
    for c in ["C1", "C2"]:
        d = wide[c].values - wide["C0"].values
        w = wilcoxon(wide[c].values, wide["C0"].values, alternative="two-sided")
        n01, n10, pm = mcnemar_exact(syn["C0"], syn[c])
        pw.append({"comparison": f"{c} vs C0", "median_paired_diff": np.median(d), "n_higher": int((d > 0).sum()),
                   "n_lower": int((d < 0).sum()), "wilcoxon_W": w.statistic, "wilcoxon_p": w.pvalue,
                   "c0_pass_only": n01, "cond_pass_only": n10, "mcnemar_p": pm})
    pw = pd.DataFrame(pw)
    pw["wilcoxon_p_holm"] = holm(pw.wilcoxon_p)
    pw["mcnemar_p_holm"] = holm(pw.mcnemar_p)
    table = pd.DataFrame(rows)
    table.to_csv(D + "h2_results_table.csv", index=False)
    pw.to_csv(D + "h2_results_pairwise.csv", index=False)

    byp = []
    for (c, p), g in cos.groupby(["condition", "project_name"]):
        x = g.skeleton_cosine.values
        byp.append({"condition": c, "project": p, "N": len(x), "median": np.median(x),
                    "IQR": np.percentile(x, 75) - np.percentile(x, 25), "share_ge_0.85": (x >= T).mean()})
    byp = pd.DataFrame(byp)
    byp.to_csv(D + "h2_results_by_project.csv", index=False)

    rep = ["H2 results on 255 ids (exclusions: 2, 102, 202, 86, 119, 203)", "",
           table.round(4).to_string(index=False), "", pw.round(6).to_string(index=False), "",
           byp.pivot(index="project", columns="condition", values="median").round(4).to_string(), "",
           byp.pivot(index="project", columns="condition", values="share_ge_0.85").round(3).to_string()]
    open(D + "h2_report.txt", "w", encoding="utf-8").write("\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
