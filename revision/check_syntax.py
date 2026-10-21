"""
check_syntax.py  --  CORRECT Gherkin syntax check (replaces the old check_executable())
==========================================================================================
Reason: the check_executable() function in scripts/compute_metrics.py runs `behave --dry-run temp.feature`
in a directory that has NO steps/. behave stops immediately with "ConfigError: No steps directory" BEFORE parsing,
and the output does not contain the word "ParserError" => every file is counted as PASS (even text that is not Gherkin).

This script calls behave's parser directly (behave.parser.parse_feature), so it really parses each file.
Results on the 261 original outputs: 258 PASS / 3 FAIL (id 136, 148, 154).

How to run:
    pip install behave pandas
    python revision/check_syntax.py --input results/full_gpt54mini_output.csv --col generated_gherkin --out revision/results/syntax_parse_n261.csv
    # for the output files of the H2 conditions (zero-shot, 3-shot, ...):
    python check_syntax.py --input h2_zeroshot_output.csv --col generated_gherkin --out syntax_zeroshot.csv

Output: 1 row / id with the columns: id, parse_status (PASS/FAIL/EMPTY), error_type, error_msg,
        n_scenarios, n_steps, has_feature_kw, has_then.
"""
import argparse
import sys

import pandas as pd
from behave.parser import parse_feature


def strip_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else ""
    if t.endswith("```"):
        t = t[:-3]
    return t.strip()


def check(text):
    if not isinstance(text, str) or not text.strip():
        return dict(parse_status="EMPTY", error_type="", error_msg="", n_scenarios=0,
                    n_steps=0, has_feature_kw=False, has_then=False)
    text = strip_fence(text.replace("\\n", "\n"))
    try:
        feat = parse_feature(text)
    except Exception as e:  # ParserError, etc.
        return dict(parse_status="FAIL", error_type=type(e).__name__, error_msg=str(e)[:300],
                    n_scenarios=0, n_steps=0, has_feature_kw=False, has_then=False)
    if feat is None:
        return dict(parse_status="FAIL", error_type="NoFeature", error_msg="no Feature: keyword",
                    n_scenarios=0, n_steps=0, has_feature_kw=False, has_then=False)
    scen = list(feat.walk_scenarios())
    steps = [s for sc in scen for s in sc.steps]
    return dict(parse_status="PASS", error_type="", error_msg="", n_scenarios=len(scen),
                n_steps=len(steps), has_feature_kw=True,
                has_then=any(s.step_type == "then" for s in steps))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--col", default="generated_gherkin")
    ap.add_argument("--id-col", default="id")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    df = pd.read_csv(a.input)
    rows = [{"id": r[a.id_col], **check(r[a.col])} for _, r in df.iterrows()]
    out = pd.DataFrame(rows)
    out.to_csv(a.out, index=False, encoding="utf-8")
    n, k = len(out), (out.parse_status == "PASS").sum()
    print(f"PASS {k}/{n} = {k / n:.2%}")
    print(out.parse_status.value_counts().to_string())
    fails = out[out.parse_status != "PASS"]
    if len(fails):
        print("\nFAIL ids:", fails["id"].tolist())
    try:
        from scipy.stats import binomtest
        res = binomtest(int(k), int(n), p=0.80, alternative="greater")
        # The two-sided CI must come from the two-sided test (the one-sided test gives a one-sided CI, upper bound = 1)
        ci = binomtest(int(k), int(n)).proportion_ci(confidence_level=0.95, method="exact")
        print(f"Exact binomial vs 0.80: p = {res.pvalue:.3g}; 95% Clopper-Pearson CI [{ci.low:.4f}, {ci.high:.4f}]")
    except ImportError:
        print("(install scipy to get the p-value and CI)")


if __name__ == "__main__":
    sys.exit(main())
