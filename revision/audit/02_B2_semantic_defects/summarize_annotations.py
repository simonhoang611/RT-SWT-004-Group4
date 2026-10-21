"""
summarize_annotations.py  --  Summary of the B2/H3 sheets + Cohen's kappa (agreement between 2 annotators)
=====================================================================================================
Procedure:
  1. An fills in b2_annotation_sheet.csv (60 rows) -> saves it as  b2_annotation_An.csv
  2. Hoang INDEPENDENTLY fills in the 15 ids in double_annotation_ids.txt -> saves it as b2_annotation_Hoang.csv
     (Hoang does NOT look at An's sheet before finishing)
  3. python summarize_annotations.py --a b2_annotation_An.csv --b b2_annotation_Hoang.csv --label has_business_defect
     (H3: --a ../03_H3_temporal_causal/h3_annotation_An.csv --b ...Hoang.csv --label has_temporal_causal_defect)
Guide RBL-4: accepted only if kappa >= 0.7; < 0.7 -> discuss, clarify the guideline, annotate again.

Printed output: defect rate + 95% CI (Clopper-Pearson) by domain, frequency of each defect type, kappa,
                accuracy of the rule-based flags (precision of the script compared with the human).
"""
import argparse
from pathlib import Path
import math

import pandas as pd
from scipy.stats import binomtest


def kappa(a, b):
    a, b = list(a), list(b)
    if not a or len(a) != len(b):
        raise ValueError('Kappa needs nonempty equal-length paired labels')
    if any(x not in {'Y','N'} for x in a+b):
        raise ValueError('Blank/unknown labels cannot be treated as N')
    n = len(a)
    cats = sorted(set(a) | set(b))
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else math.nan


def validated(path, label):
    df = pd.read_csv(path)
    if not len(df) or not {'id', label}.issubset(df.columns):
        raise ValueError('Empty sheet or missing id/label column')
    ids = pd.to_numeric(df.id, errors='raise')
    if ids.isna().any() or (ids % 1 != 0).any() or ids.duplicated().any():
        raise ValueError('Missing/noninteger/duplicate ids')
    df['id'] = ids.astype(int)
    labels = df[label].astype('string').str.strip().str.upper()
    if labels.isna().any() or not labels.isin(['Y','N']).all():
        raise ValueError('Every label must be an explicit Y or N')
    df[label] = labels
    cols = [c for c in df.columns if c.startswith(('D_','PRE_','POST_','ACTION_','CAUSAL_','ORDER_'))]
    for c in cols:
        n = pd.to_numeric(df[c], errors='raise')
        if n.isna().any() or (n<0).any() or (n%1 != 0).any():
            raise ValueError(f'{c}: every count must be a nonnegative integer')
    if {'n_AC_total','n_AC_covered_correctly'}.issubset(df.columns):
        total = pd.to_numeric(df.n_AC_total, errors='raise')
        covered = pd.to_numeric(df.n_AC_covered_correctly, errors='raise')
        if total.isna().any() or covered.isna().any() or (covered>total).any():
            raise ValueError('AC coverage cannot be blank or exceed total')
    return df


def ci(k, n):
    c = binomtest(k, n).proportion_ci(method="exact")
    return f"{k}/{n} = {k / n:.1%} [95% CI {c.low:.1%}, {c.high:.1%}]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b")
    ap.add_argument("--label", default="has_business_defect")
    ap.add_argument('--expected-double-ids', default=str(Path(__file__).parent/'double_annotation_ids.txt'))
    x = ap.parse_args()
    A = validated(x.a, x.label)
    expected_a_path = (Path(__file__).parent.parent/'03_H3_temporal_causal/h3_annotation_sheet.csv'
        if x.label=='has_temporal_causal_defect' else Path(__file__).parent/'b2_annotation_sheet.csv')
    expected_a = set(pd.read_csv(expected_a_path).id)
    if set(A.id) != expected_a:
        raise ValueError('Annotator A must cover exactly the fixed 60 review ids; missing cases cannot disappear from the denominator')
    print(f"== {x.label} (annotator A, N={len(A)}) ==")
    print("Total:", ci(int((A[x.label] == 'Y').sum()), len(A)))
    for d, g in A.groupby("domain"):
        print(f"  {d}:", ci(int((g[x.label] == 'Y').sum()), len(g)))
    dcols = [c for c in A.columns if c.startswith(("D_", "PRE_", "POST_", "ACTION_", "CAUSAL_", "ORDER_"))]
    if dcols:
        print("\nNumber of scenarios with at least 1 defect of each type:")
        print((pd.to_numeric(A[dcols].stack(), errors="coerce").unstack().fillna(0) > 0).sum().to_string())
    if "rule_flag_confirmed" in A.columns:
        f = A[A["flags"].fillna("") != ""]
        conf = f["rule_flag_confirmed"].astype(str).str.upper()
        if len(f):
            if not conf.isin(['Y','N']).all():
                raise ValueError('Flag confirmation must be explicit Y/N')
            print(f"\nFile-level rule-flag confirmation: {(conf == 'Y').sum()}/{len(f)} (not per-flag precision)")
    if x.b:
        B = validated(x.b, x.label)
        expected = {int(v.strip()) for v in Path(x.expected_double_ids).read_text().replace(',', '\n').splitlines() if v.strip()}
        if set(B.id) != expected or not expected.issubset(set(A.id)):
            raise ValueError('Second sheet must contain exactly the fixed independent double-annotation ids')
        m = A[["id", x.label]].merge(B[["id", x.label]], on="id", suffixes=("_A", "_B"))
        value = kappa(m[x.label + '_A'], m[x.label + '_B'])
        print(f"\nCohen's kappa on {len(m)} ids: {value:.3f}" if not math.isnan(value) else '\nKappa undefined: expected agreement=1 (all paired labels constant)')
        dis = m[m[x.label + "_A"] != m[x.label + "_B"]]
        if len(dis):
            print("Disagreement on ids:", dis.id.tolist(), "-> discuss and record the consensus result in the note column")


if __name__ == "__main__":
    main()
