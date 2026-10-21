"""
b3_threshold_sensitivity.py  (revision, Action Tracker B3; post-hoc analysis)

Asks how the RQ1 conclusion depends on the 0.85 threshold and what the
available defect evidence says about that threshold. It re-embeds nothing:
skeleton_cosine is taken from results/full_per_row_metrics.csv.

Part 1, threshold sweep (t = 0.80, 0.81, ..., 0.90), overall and per project,
with exemplars 2, 102, 202 excluded (N = 258) and included (N = 261):
  - n and share of files with cosine >= t, exact (Clopper-Pearson) 95% CI;
  - median minus t;
  - one-sample Wilcoxon signed-rank on x - t, one-sided "greater"
    (scipy defaults, zero differences dropped).
Part 2, defect evidence (only if the files are given):
  - --audit: the 60-file B2 audit (all files have cosine >= 0.85 by design,
    so it cannot estimate how often files BELOW a threshold are defective);
    reports defect share by cosine band and a Mann-Whitney comparison of the
    cosine of defective vs non-defective files.
  - --mutation: the SBERT mutation test; for each threshold, the share of
    seeded-defect pairs whose cosine is still >= t (valid pairs only).

Usage (from the repository root):
  python revision/b3_threshold_sensitivity.py \
     [--audit <b2_annotation_An_CONFIRMED.csv>] [--mutation <mutation_results.csv>]
"""
import argparse
import os

import numpy as np
import pandas as pd
from scipy.stats import binomtest, mannwhitneyu, wilcoxon

EXEMPLAR_IDS = [2, 102, 202]
THRESHOLDS = [round(0.80 + 0.01 * k, 2) for k in range(11)]


def sweep(df):
    rows = []
    for excl in (True, False):
        d = df[~df.id.isin(EXEMPLAR_IDS)] if excl else df
        groups = [("All", d)] + list(d.groupby("project_name"))
        for name, g in groups:
            x = g.skeleton_cosine.to_numpy(float)
            for t in THRESHOLDS:
                k = int((x >= t).sum())
                ci = binomtest(k, len(x)).proportion_ci(method="exact")
                w = wilcoxon(x - t, alternative="greater")
                rows.append({"exemplars_excluded": excl, "group": name, "N": len(x), "threshold": t,
                             "n_ge_t": k, "share_ge_t": k / len(x), "ci_low": ci.low, "ci_high": ci.high,
                             "median_minus_t": float(np.median(x)) - t,
                             "wilcoxon_W": w.statistic, "wilcoxon_p_greater": w.pvalue})
    return pd.DataFrame(rows)


def audit_part(path):
    a = pd.read_csv(path)
    y = a.has_business_defect.astype(str).str.strip().str.upper().eq("Y")
    c = a.skeleton_cosine.astype(float)
    bands = pd.cut(c, [0.85, 0.875, 0.90, 0.95, 1.0001], right=False)
    out = a.assign(defect=y, band=bands).groupby("band", observed=True).agg(N=("defect", "size"), n_defect=("defect", "sum"))
    mw = mannwhitneyu(c[y], c[~y], alternative="two-sided")
    auc = mw.statistic / (y.sum() * (~y).sum())
    lines = [f"audit file: {os.path.basename(path)}  N={len(a)}  min cosine={c.min():.4f}",
             f"defective {int(y.sum())}/{len(a)}",
             out.to_string(),
             f"median cosine defective={c[y].median():.4f}  non-defective={c[~y].median():.4f}",
             f"Mann-Whitney U={mw.statistic:.1f} p={mw.pvalue:.4f}  AUC(cosine ranks defective higher)={auc:.3f}"]
    return "\n".join(lines)


def mutation_part(path):
    m = pd.read_csv(path)
    v = m[m.pair_parser_valid_baseline_no_hard_error.astype(str).eq("True")]
    rows = []
    for op, g in [("ALL", v)] + list(v.groupby("operator")):
        x = g.cosine_orig_vs_mutant.astype(float)
        r = {"operator": op, "N": len(x), "min_cosine": x.min()}
        for t in THRESHOLDS + [0.95, 0.99]:
            r[f"share_ge_{t:.2f}"] = (x >= t).mean()
        rows.append(r)
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metrics", default="results/full_per_row_metrics.csv")
    ap.add_argument("--stories", default="data/full_user_stories.csv")
    ap.add_argument("--audit")
    ap.add_argument("--mutation")
    ap.add_argument("--outdir", default="revision/results")
    x = ap.parse_args()
    os.makedirs(x.outdir, exist_ok=True)
    df = pd.read_csv(x.metrics).merge(pd.read_csv(x.stories)[["id", "project_name"]], on="id", validate="one_to_one")
    s = sweep(df)
    s.to_csv(os.path.join(x.outdir, "b3_threshold_sweep.csv"), index=False)
    view = s[s.exemplars_excluded].pivot(index="threshold", columns="group", values="share_ge_t").round(3)
    report = ["Share of files with skeleton cosine >= t (exemplars excluded, N = 258):", view.to_string(), ""]
    pv = s[s.exemplars_excluded & (s.group == "All")][["threshold", "n_ge_t", "share_ge_t", "ci_low", "ci_high", "median_minus_t", "wilcoxon_p_greater"]]
    report += ["All projects, N = 258:", pv.to_string(index=False), ""]
    if x.audit:
        report += ["Defect evidence, 60-file audit:", audit_part(x.audit), ""]
    if x.mutation:
        mt = mutation_part(x.mutation)
        mt.to_csv(os.path.join(x.outdir, "b3_mutation_by_threshold.csv"), index=False)
        report += ["Seeded-defect pairs still >= t (valid pairs):", mt.round(3).to_string(index=False), ""]
    open(os.path.join(x.outdir, "b3_report.txt"), "w", encoding="utf-8").write("\n".join(report))
    print("\n".join(report))


if __name__ == "__main__":
    main()
