"""
m9_effect_size_ci.py  (revision, Action Tracker M9)

95% confidence intervals for the effect sizes of the C0 analysis:
- delta = P(x > 0.85) - P(x < 0.85) for N = 258 and N = 261: exact interval from the
  Clopper-Pearson interval of the share above 0.85 (no ties at 0.85), delta = 2p - 1;
  a percentile bootstrap interval is given for comparison.
- eta^2_H = (H - k + 1) / (n - k) of the Kruskal-Wallis test across the three projects
  (N = 258): percentile bootstrap, resampling within each project so that the group
  sizes stay 99, 99 and 60.
- Spearman's rho between story-reference trigram overlap and skeleton cosine, per
  project and pooled, N = 258 (revision/results/b1_overlap_per_file.csv): percentile bootstrap.
All bootstraps use 10,000 resamples and numpy.random.default_rng(2026), as the
median interval of Section 3.7.

Usage (from the repository root):  python revision/m9_effect_size_ci.py
Output: revision/results/m9_effect_size_ci.txt
"""
import os

import numpy as np
import pandas as pd
from scipy.stats import binomtest, kruskal, spearmanr

T = 0.85
B = 10_000
EXEMPLAR_IDS = [2, 102, 202]


def delta(x):
    return ((x > T).sum() - (x < T).sum()) / len(x)


def eta2_h(groups):
    H = kruskal(*groups).statistic
    n, k = sum(len(g) for g in groups), len(groups)
    return (H - k + 1) / (n - k)


def main(out="revision/results/m9_effect_size_ci.txt"):
    df = pd.read_csv("results/full_per_row_metrics.csv").merge(
        pd.read_csv("data/full_user_stories.csv")[["id", "project_name"]], on="id", validate="one_to_one")
    lines = []

    for label, d in [("N = 258", df[~df.id.isin(EXEMPLAR_IDS)]), ("N = 261", df)]:
        x = d.skeleton_cosine.to_numpy(float)
        above, below, n = int((x > T).sum()), int((x < T).sum()), len(x)
        assert above + below == n, "ties at 0.85"
        ci = binomtest(above, n).proportion_ci(method="exact")
        rng = np.random.default_rng(2026)
        boot = [delta(x[rng.integers(0, n, n)]) for _ in range(B)]
        lines.append(f"delta {label}: {delta(x):.4f} (above {above}, below {below}); "
                     f"exact 95% CI [{2 * ci.low - 1:.4f}, {2 * ci.high - 1:.4f}]; "
                     f"bootstrap 95% CI [{np.percentile(boot, 2.5):.4f}, {np.percentile(boot, 97.5):.4f}]")

    d = df[~df.id.isin(EXEMPLAR_IDS)]
    groups = [g.skeleton_cosine.to_numpy(float) for _, g in d.groupby("project_name")]
    rng = np.random.default_rng(2026)
    boot = [eta2_h([g[rng.integers(0, len(g), len(g))] for g in groups]) for _ in range(B)]
    lines.append(f"eta^2_H N = 258: {eta2_h(groups):.4f}; bootstrap 95% CI "
                 f"[{np.percentile(boot, 2.5):.4f}, {np.percentile(boot, 97.5):.4f}] "
                 f"(group sizes {[len(g) for g in groups]})")

    b1 = pd.read_csv("revision/results/b1_overlap_per_file.csv")
    b1 = b1[~b1.id.isin(EXEMPLAR_IDS)]  # as in revision/results/b1_spearman.csv
    for name, g in [("All", b1)] + list(b1.groupby("project")):
        a, c = g.story_gt_overlap.to_numpy(float), g.skeleton_cosine.to_numpy(float)
        rng = np.random.default_rng(2026)
        idx = [rng.integers(0, len(a), len(a)) for _ in range(B)]
        boot = [spearmanr(a[i], c[i]).statistic for i in idx]
        lines.append(f"Spearman rho story overlap vs cosine, {name} (n = {len(a)}): "
                     f"{spearmanr(a, c).statistic:.4f}; bootstrap 95% CI "
                     f"[{np.nanpercentile(boot, 2.5):.4f}, {np.nanpercentile(boot, 97.5):.4f}]")

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
