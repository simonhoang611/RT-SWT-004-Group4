"""
h12_kappa_ci.py  (revision, Action Tracker v1: H12)

95% percentile bootstrap intervals for the two Cohen's kappa values of the 15 doubly
labelled audit files (business logic and temporal/causal). The 2x2 tables are read from
revision/audit/independent_rater_15/kappa_result.json; files are resampled with
replacement (10,000 resamples, seed 2026, as elsewhere in the paper). Kappa itself is not
recomputed from new labels.

Usage (from the repository root):
  python revision/h12/h12_kappa_ci.py
Output: revision/h12/results/h12_kappa_ci.txt
"""
import json
import os

import numpy as np

SRC = "revision/audit/independent_rater_15/kappa_result.json"
OUT = "revision/h12/results/h12_kappa_ci.txt"
B, SEED = 10_000, 2026


def kappa(a, b):
    po = np.mean(a == b)
    pe = np.mean(a) * np.mean(b) + (1 - np.mean(a)) * (1 - np.mean(b))
    return np.nan if pe == 1 else (po - pe) / (1 - pe)


def main():
    res = json.load(open(SRC, encoding="utf-8"))
    lines = [f"source: {SRC}", f"bootstrap: {B} resamples of files, seed {SEED}, percentile 95% CI"]
    for facet, name in [("b2", "business logic"), ("h3", "temporal/causal")]:
        t = res[facet]["rows_An_cols_Hoang"]
        a, b = [], []
        for x in ("Y", "N"):
            for y in ("Y", "N"):
                n = t[x][y]
                a += [x == "Y"] * n
                b += [y == "Y"] * n
        a, b = np.array(a, float), np.array(b, float)
        k = kappa(a, b)
        assert abs(k - res[facet]["kappa"]) < 1e-12
        rng = np.random.default_rng(SEED)
        ks = np.array([kappa(a[i], b[i]) for i in (rng.integers(0, len(a), len(a)) for _ in range(B))])
        undefined = int(np.isnan(ks).sum())
        lo, hi = np.percentile(ks[~np.isnan(ks)], [2.5, 97.5])
        lines.append(f"{name}: n {len(a)}, kappa {k:.3f}, 95% CI {lo:.3f} to {hi:.3f} "
                     f"(undefined resamples {undefined})")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
