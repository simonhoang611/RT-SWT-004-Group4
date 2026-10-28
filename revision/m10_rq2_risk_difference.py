"""
m10_rq2_risk_difference.py  (revision, Action Tracker M10)

Effect size for RQ2: the risk difference between the observed parser-compliance
rate of condition C0 and the 0.80 reference rate of H0, with a 95% CI. The CI is
the exact Clopper-Pearson interval of the rate shifted by 0.80, the same interval
that Section 3.7 reports for the rate itself. No API calls.

Input : revision/results/syntax_parse_n261.csv (per-file behave parser result)
Output: revision/results/m10_rq2_risk_difference.txt

Usage (from the repository root):
  python revision/m10_rq2_risk_difference.py
"""
import csv
import os

from scipy.stats import beta, binomtest

P0 = 0.80
EXEMPLARS = {2, 102, 202}
IN = os.path.join("revision", "results", "syntax_parse_n261.csv")
OUT = os.path.join("revision", "results", "m10_rq2_risk_difference.txt")


def summary(rows, label):
    n = len(rows)
    k = sum(r["parse_status"] == "PASS" for r in rows)
    p = k / n
    lo = beta.ppf(0.025, k, n - k + 1)
    hi = beta.ppf(0.975, k + 1, n - k)
    pv = binomtest(k, n, P0, alternative="greater").pvalue
    return (f"{label}: {k}/{n} PASS, rate {p:.4f} (95% Clopper-Pearson CI {lo:.4f}-{hi:.4f}); "
            f"risk difference from {P0:.2f}: {p - P0:+.4f} (95% CI {lo - P0:+.4f} to {hi - P0:+.4f}); "
            f"one-sided exact binomial p = {pv:.3g}")


def main():
    rows = list(csv.DictReader(open(IN, encoding="utf-8")))
    lines = [summary([r for r in rows if int(r["id"]) not in EXEMPLARS], "N = 258 (primary)"),
             summary(rows, "N = 261")]
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
