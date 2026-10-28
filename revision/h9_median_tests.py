"""
h9_median_tests.py  (revision, Action Tracker H9)

RQ1 asks about the median, but the one-sample Wilcoxon signed-rank test only
addresses the median when x - 0.85 is symmetric. This script, on the C0 scores
of results/full_per_row_metrics.csv:

  1. checks symmetry of x - 0.85: sample skewness with a 95% percentile
     bootstrap interval, quartile distances, mean versus median, and the
     Hodges-Lehmann pseudo-median (the location the Wilcoxon test addresses);
  2. runs the exact one-sided sign test (binomial test on files above versus
     below 0.85, ties dropped) and a 95% percentile bootstrap interval for the
     median (10,000 resamples, numpy default_rng(2026));
  3. keeps the pre-registered one-sided Wilcoxon test as a sensitivity analysis;
  4. repeats the sign test per project, for every reference point of the
     sensitivity table (0.80-0.90), and for C0, C1, C2 on the 255 common files
     (revision/h2/h2_cosine_per_file.csv).

Primary analysis N = 258 (exemplars 2, 102, 202 excluded); N = 261 alongside.

Usage (from the repository root):  python revision/h9_median_tests.py
"""
import os

import numpy as np
import pandas as pd
from scipy.stats import binomtest, skew, wilcoxon

T = 0.85
SEED = 2026
B = 10000
C0_EXEMPLARS = [2, 102, 202]
ALL_EXEMPLARS = [2, 102, 202, 86, 119, 203]


def boot(x, stat, seed=SEED):
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(B, len(x)))
    return np.percentile([stat(x[i]) for i in idx], [2.5, 97.5])


def sign_test(x, t=T, alternative="greater"):
    d = x - t
    above, below = int((d > 0).sum()), int((d < 0).sum())
    return above, below, binomtest(above, above + below, 0.5, alternative=alternative).pvalue


def hodges_lehmann(d):
    i, j = np.triu_indices(len(d))
    return np.median((d[i] + d[j]) / 2)


def rq1_row(name, x):
    d = x - T
    q1, med, q3 = np.quantile(x, [0.25, 0.5, 0.75])
    above, below, p_sign = sign_test(x)
    lo, hi = boot(x, np.median)
    s_lo, s_hi = boot(d, skew)
    return {"sample": name, "N": len(x), "median": med, "median_ci_low": lo, "median_ci_high": hi,
            "above": above, "below": below, "delta": (above - below) / len(x), "sign_p_greater": p_sign,
            "wilcoxon_W": wilcoxon(d, alternative="greater").statistic,
            "wilcoxon_p_greater": wilcoxon(d, alternative="greater").pvalue,
            "mean": x.mean(), "Q1": q1, "Q3": q3, "median_minus_Q1": med - q1, "Q3_minus_median": q3 - med,
            "skewness": skew(d), "skew_ci_low": s_lo, "skew_ci_high": s_hi,
            "hodges_lehmann": hodges_lehmann(d) + T}


def main(outdir="revision/results"):
    os.makedirs(outdir, exist_ok=True)
    df = pd.read_csv("results/full_per_row_metrics.csv").merge(
        pd.read_csv("data/full_user_stories.csv")[["id", "project_name"]], on="id", validate="one_to_one")
    prim = df[~df.id.isin(C0_EXEMPLARS)]

    rq1 = pd.DataFrame([rq1_row("C0 N=258", prim.skeleton_cosine.to_numpy(float)),
                        rq1_row("C0 N=261", df.skeleton_cosine.to_numpy(float))])
    rq1.to_csv(os.path.join(outdir, "h9_rq1_median_tests.csv"), index=False)

    rows = []
    for name, g in prim.groupby("project_name"):
        x = g.skeleton_cosine.to_numpy(float)
        a, b, pg = sign_test(x)
        rows.append({"table": "per project", "group": name, "N": len(x), "above": a, "below": b,
                     "sign_p_greater": pg, "sign_p_less": sign_test(x, alternative="less")[2],
                     "wilcoxon_p_greater": wilcoxon(x - T, alternative="greater").pvalue,
                     "wilcoxon_p_less": wilcoxon(x - T, alternative="less").pvalue, "skewness": skew(x - T)})
    x = prim.skeleton_cosine.to_numpy(float)
    for t in [0.80, 0.82, 0.84, 0.85, 0.86, 0.88, 0.90]:
        a, b, pg = sign_test(x, t)
        rows.append({"table": "reference point", "group": f"{t:.2f}", "N": len(x), "above": a, "below": b,
                     "sign_p_greater": pg, "wilcoxon_p_greater": wilcoxon(x - t, alternative="greater").pvalue})
    h2 = pd.read_csv("revision/h2/h2_cosine_per_file.csv")
    h2 = h2[~h2.id.isin(ALL_EXEMPLARS)]
    for c, g in h2.groupby("condition"):
        x = g.skeleton_cosine.to_numpy(float)
        a, b, pg = sign_test(x)
        lo, hi = boot(x, np.median)
        rows.append({"table": "ablation (255 common files)", "group": c, "N": len(x), "above": a, "below": b,
                     "sign_p_greater": pg, "wilcoxon_p_greater": wilcoxon(x - T, alternative="greater").pvalue,
                     "median": np.median(x), "median_ci_low": lo, "median_ci_high": hi})
    other = pd.DataFrame(rows)
    other.to_csv(os.path.join(outdir, "h9_sign_tests_other.csv"), index=False)

    rep = [rq1.T.to_string(header=False), "", other.round(4).to_string(index=False)]
    open(os.path.join(outdir, "h9_report.txt"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
