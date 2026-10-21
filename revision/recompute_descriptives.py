"""
recompute_descriptives.py  (revision, plan items E2, E6, E8)

Recomputes every RQ1 number in Table 3 and Section 4 from the per-row metrics
file written by scripts/compute_metrics.py. It does not re-embed anything: the
skeleton_cosine values are taken as they are in results/full_per_row_metrics.csv.

Definitions used (state these in the paper):
  - Quartiles: linear interpolation between order statistics
    (numpy/pandas default, Hyndman-Fan type 7).
  - SD: sample standard deviation (ddof = 1).
  - Wilcoxon: one-sample signed-rank test on x - 0.85, alternative "greater",
    scipy.stats.wilcoxon defaults (zero differences dropped, "wilcox" method).
  - Cliff's delta (one-sample, against the threshold):
        delta = (#{x > 0.85} - #{x < 0.85}) / n
    i.e. P(X > 0.85) - P(X < 0.85).
  - Exemplars: ids 2, 102 and 202 were the one-shot examples in the prompt
    (scripts/run_experiment.ipynb). They are reported with and without them.

Usage (from the repository root):
    python revision/recompute_descriptives.py
"""
import argparse
import os

import numpy as np
import pandas as pd
from scipy.stats import kruskal, wilcoxon

THRESHOLD = 0.85
EXEMPLAR_IDS = [2, 102, 202]


def describe(x):
    x = np.asarray(x, dtype=float)
    n = len(x)
    w = wilcoxon(x - THRESHOLD, alternative="greater")
    above = int((x > THRESHOLD).sum())
    below = int((x < THRESHOLD).sum())
    q1, med, q3 = np.quantile(x, [0.25, 0.5, 0.75])
    return {
        "N": n,
        "min": x.min(),
        "Q1": q1,
        "median": med,
        "Q3": q3,
        "max": x.max(),
        "IQR": q3 - q1,
        "mean": x.mean(),
        "SD": x.std(ddof=1),
        "n_above_0.85": above,
        "n_below_0.85": below,
        "cliffs_delta_vs_0.85": (above - below) / n,
        "wilcoxon_W": w.statistic,
        "wilcoxon_p_one_sided": w.pvalue,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metrics", default="results/full_per_row_metrics.csv")
    ap.add_argument("--stories", default="data/full_user_stories.csv")
    ap.add_argument("--outdir", default="revision/results")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)

    m = pd.read_csv(a.metrics)
    s = pd.read_csv(a.stories)[["id", "project_name", "domain"]]
    df = m.merge(s, on="id", how="left", validate="one_to_one")
    assert len(df) == 261 and df["project_name"].notna().all()
    assert set(EXEMPLAR_IDS) <= set(df["id"])

    rows = []
    for label, sub in [("all_N261", df), ("no_exemplars_N258", df[~df["id"].isin(EXEMPLAR_IDS)])]:
        rows.append({"set": label, "group": "all", **describe(sub["skeleton_cosine"])})
        for proj, g in sub.groupby("project_name", sort=False):
            rows.append({"set": label, "group": proj, **describe(g["skeleton_cosine"])})
        groups = [g["skeleton_cosine"].values for _, g in sub.groupby("project_name", sort=False)]
        kw = kruskal(*groups)
        rows.append({"set": label, "group": "Kruskal-Wallis across projects",
                     "wilcoxon_W": np.nan, "kruskal_H": kw.statistic, "kruskal_p": kw.pvalue})
    out = pd.DataFrame(rows)
    path = os.path.join(a.outdir, "descriptives_skeleton_cosine.csv")
    out.to_csv(path, index=False)

    ex = df[df["id"].isin(EXEMPLAR_IDS)][["id", "project_name", "skeleton_cosine"]]
    ex.to_csv(os.path.join(a.outdir, "exemplar_scores.csv"), index=False)

    pd.set_option("display.width", 200)
    cols = ["set", "group", "N", "min", "Q1", "median", "Q3", "max", "IQR", "mean", "SD",
            "cliffs_delta_vs_0.85", "wilcoxon_p_one_sided"]
    print(out[out["group"] != "Kruskal-Wallis across projects"][cols].round(4).to_string(index=False))
    print(out[out["group"] == "Kruskal-Wallis across projects"][["set", "kruskal_H", "kruskal_p"]].to_string(index=False))
    print("\nExemplar scores:\n" + ex.round(4).to_string(index=False))
    print(f"\nSaved {path}")


if __name__ == "__main__":
    main()
