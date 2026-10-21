"""
h1_domain_analysis.py  (revision, Action Tracker H1)

Per-project results for skeleton cosine, exemplars 2, 102, 202 excluded (N = 258):
median, IQR, mean, SD, share >= 0.85 with exact 95% CI, one-sample Wilcoxon on
x - 0.85 in both one-sided directions, Kruskal-Wallis across projects with
two effect sizes (eta^2_H = (H - k + 1) / (n - k), Tomczak & Tomczak 2014;
epsilon^2_R = H / (n - 1)), and pairwise two-sided Mann-Whitney tests with Holm correction.

Usage (from the repository root):  python revision/h1_domain_analysis.py
"""
import itertools
import os

import numpy as np
import pandas as pd
from scipy.stats import binomtest, kruskal, mannwhitneyu, wilcoxon

T = 0.85
EXEMPLAR_IDS = [2, 102, 202]


def holm(p):
    order = np.argsort(p)
    adj, run = np.empty(len(p)), 0.0
    for rank, i in enumerate(order):
        run = max(run, (len(p) - rank) * p[i])
        adj[i] = min(run, 1.0)
    return adj


def main(outdir="revision/results"):
    os.makedirs(outdir, exist_ok=True)
    df = pd.read_csv("results/full_per_row_metrics.csv").merge(
        pd.read_csv("data/full_user_stories.csv")[["id", "project_name"]], on="id", validate="one_to_one")
    df = df[~df.id.isin(EXEMPLAR_IDS)]
    rows, groups = [], {}
    for name, g in [("All", df)] + list(df.groupby("project_name")):
        x = g.skeleton_cosine.to_numpy(float)
        if name != "All":
            groups[name] = x
        q1, med, q3 = np.quantile(x, [0.25, 0.5, 0.75])
        k = int((x >= T).sum())
        ci = binomtest(k, len(x)).proportion_ci(method="exact")
        rows.append({"project": name, "N": len(x), "median": med, "Q1": q1, "Q3": q3, "IQR": q3 - q1,
                     "mean": x.mean(), "SD": x.std(ddof=1), "n_ge_0.85": k, "share_ge_0.85": k / len(x),
                     "ci_low": ci.low, "ci_high": ci.high,
                     "wilcoxon_p_greater": wilcoxon(x - T, alternative="greater").pvalue,
                     "wilcoxon_p_less": wilcoxon(x - T, alternative="less").pvalue})
    table = pd.DataFrame(rows)
    table.to_csv(os.path.join(outdir, "h1_domain_table.csv"), index=False)
    H, p = kruskal(*groups.values())
    n, k = sum(len(v) for v in groups.values()), len(groups)
    eta2_h = (H - k + 1) / (n - k)  # corrected 16/10: this formula is eta^2_H, not epsilon^2
    eps2 = H / (n - 1)
    pairs = list(itertools.combinations(groups, 2))
    raw = np.array([mannwhitneyu(groups[a], groups[b], alternative="two-sided").pvalue for a, b in pairs])
    pw = pd.DataFrame({"pair": [f"{a} vs {b}" for a, b in pairs], "p_raw": raw, "p_holm": holm(raw)})
    pw.to_csv(os.path.join(outdir, "h1_pairwise.csv"), index=False)
    rep = [table.round(4).to_string(index=False), "",
           f"Kruskal-Wallis H={H:.3f} df={k - 1} p={p:.3e} eta^2_H={eta2_h:.3f} epsilon^2_R={eps2:.3f}", "", pw.to_string(index=False)]
    open(os.path.join(outdir, "h1_report.txt"), "w", encoding="utf-8").write("\n".join(rep))
    print("\n".join(rep))


if __name__ == "__main__":
    main()
