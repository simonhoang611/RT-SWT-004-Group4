"""
mutation_sbert_test.py  --  Quantitative evidence for B2 + H3: SBERT skeleton cosine is "blind" to business defects
=============================================================================================================
Idea (mutation testing of the METRIC, not of code):
  Take valid GT scenarios -> deliberately inject 1 business/order defect (mutant) -> compute the skeleton cosine
  between the original and the mutant with EXACTLY the paper's to_skeleton() function + all-MiniLM-L6-v2.
  If cosine(original, mutant) is still >= 0.85, the metric does NOT detect that defect.
  At the same time, run the h3 checker on the mutant to show that the rule-based check catches order defects.

Mutation operators (each operator is applied to 1 scenario):
  B2  M_NUM       change every number (x+1 / x*10)             -> the skeleton replaces numbers with <NUM>  => cosine = 1.0 by definition
  B2  M_PARAM     change the values in double quotes           -> the skeleton replaces them with <PARAM>   => cosine = 1.0 by definition
  B2  M_NEG       flip the negation in a Then step (should <-> should not, can <-> cannot, ...)
  B2  M_OP        flip the operator (more than <-> less than, at least <-> at most, increase <-> decrease, ...)
  B2  M_DROP_THEN delete 1 Then step (postcondition lost)
  H3  M_SWAP_WT   swap the keywords When <-> Then (action and result reversed)
  H3  M_THEN_FIRST move the Then block to the start of the scenario (result before cause)
  H3  M_DROP_GIVEN delete all Given steps of the scenario (precondition lost)

RUN ON GOOGLE COLAB (needs sentence-transformers + torch):
    !pip install sentence-transformers behave pandas scipy
    # in this repository the data are read from data/ at the repository root (default of --data)
    !python mutation_sbert_test.py --n-per-domain 40
Output:
    mutation_results.csv          -- 1 row / mutant: id, domain, operator, cosine, detected_by_h3
    mutation_summary.csv          -- per operator: N, median cosine, % of mutants still >= 0.85 (= % missed by SBERT)
    counterexamples/*.feature     -- a few original/mutant pairs for the paper (the "invalid counterexamples" part)
"""
import argparse
import random
import re
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent  # repository root (this script is in revision/audit/06_mutation_test_SBERT/)
sys.path.insert(0, str(HERE.parent / "03_H3_temporal_causal"))
sys.path.insert(0, str(HERE))
from h3_order_check import check_sequence, ERRORS  # noqa: E402

SEED = 2026
THRESH = 0.85
STEP_RE = re.compile(r"^(\s*)(Given|When|Then|And|But)\b(.*)$")


# ---------- identical to the paper's compute_metrics.py (NOT modified, to keep exactly the reported metric) ----------
def to_skeleton(gherkin_text):
    if not isinstance(gherkin_text, str):
        return ""
    text = gherkin_text.replace('\\n', '\n')
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'"[^"]*"', '<PARAM>', text)
    text = re.sub(r'\b\d+(\.\d+)?\b', '<NUM>', text)
    keywords = ['Feature', 'Scenario', 'Given', 'When', 'Then', 'And', 'But', 'Background']
    return '\n'.join(l.strip() for l in text.split('\n') if any(l.strip().startswith(k) for k in keywords))


# ---------- extract simple scenarios (not Outline) from a GT file ----------
def extract_scenarios(text):
    """Returns a list of (feature_header_lines, scenario_lines) for the ordinary scenarios with >=1 When and >=1 Then."""
    lines = text.replace("\\n", "\n").split("\n")
    header = []
    for l in lines:
        if l.strip().startswith(("Feature", "Background", "Scenario", "Rule")):
            if l.strip().startswith("Feature"):
                header = [l]
            if l.strip().startswith("Scenario"):
                break
    out, cur = [], None
    for l in lines:
        s = l.strip()
        if s.startswith("Scenario Outline") or s.startswith("Scenario Template"):
            if cur:
                out.append(cur)
            cur = None
            continue
        if s.startswith("Scenario"):
            if cur:
                out.append(cur)
            cur = [l]
        elif s.startswith(("Examples", "Rule", "Background", "@")) and cur:
            out.append(cur)
            cur = None
        elif cur is not None:
            cur.append(l)
    if cur:
        out.append(cur)
    good = []
    for sc in out:
        kws = [m.group(2) for m in (STEP_RE.match(x) for x in sc) if m]
        if "When" in kws and "Then" in kws and len(kws) <= 25:
            good.append((header, sc))
    return good


def resolved_types(sc_lines):
    """Assigns the real type to And/But (inherited from the previous step)."""
    types, last = [], None
    for l in sc_lines:
        m = STEP_RE.match(l)
        if not m:
            types.append(None)
            continue
        kw = m.group(2)
        if kw in ("And", "But"):
            types.append(last)
        else:
            last = kw.lower()
            types.append(last)
    return types


# ---------- mutation operators ----------
NEG_PAIRS = [(r"\bshould not\b", "should"), (r"\bshould\b", "should not"), (r"\bcannot\b", "can"),
             (r"\bcan\b", "cannot"), (r"\bis not\b", "is"), (r"\bis\b", "is not"),
             (r"\bdoes not\b", "does"), (r"\bnot\b", ""), (r"\bno\b", "some")]
OP_PAIRS = [("more than", "less than"), ("less than", "more than"), ("at least", "at most"),
            ("at most", "at least"), ("greater", "smaller"), ("increase", "decrease"),
            ("decrease", "increase"), ("before", "after"), ("after", "before"), ("enabled", "disabled"),
            ("disabled", "enabled"), ("valid", "invalid"), ("added", "removed"), ("removed", "added"),
            ("paid", "unpaid"), ("visible", "hidden"), ("debit", "credit"), ("credit", "debit")]


def m_num(sc):
    return [re.sub(r"\b\d+(\.\d+)?\b", lambda m: str(float(m.group(0)) * 10 + 1).rstrip("0").rstrip("."), l)
            for l in sc]


def m_param(sc):
    return [re.sub(r'"([^"]*)"', lambda m: '"' + m.group(1)[::-1] + 'X"', l) for l in sc]


def _first_then_index(sc):
    t = resolved_types(sc)
    return [i for i, x in enumerate(t) if x == "then"]


def m_neg(sc):
    sc = list(sc)
    for i in _first_then_index(sc):
        for pat, rep in NEG_PAIRS:
            new = re.sub(pat, rep, sc[i], count=1)
            if new != sc[i]:
                sc[i] = re.sub(r"\s{2,}", " ", new) if rep == "" else new
                return sc
    return None


def m_op(sc):
    sc = list(sc)
    for i, l in enumerate(sc):
        if not STEP_RE.match(l):
            continue
        low = l.lower()
        for a, b in OP_PAIRS:
            if re.search(r"\b" + a + r"\b", low):
                sc[i] = re.sub(r"\b" + a + r"\b", b, l, count=1, flags=re.I)
                return sc
    return None


def m_drop_then(sc):
    idx = _first_then_index(sc)
    if len(idx) < 2:  # keep at least 1 Then so that the mutant stays syntactically "valid"
        return None
    i = idx[-1]
    return [l for j, l in enumerate(sc) if j != i]


def m_swap_wt(sc):
    out = []
    for l in sc:
        m = STEP_RE.match(l)
        if m and m.group(2) == "When":
            l = f"{m.group(1)}Then{m.group(3)}"
        elif m and m.group(2) == "Then":
            l = f"{m.group(1)}When{m.group(3)}"
        out.append(l)
    return out


def m_then_first(sc):
    t = resolved_types(sc)
    then_lines = [l for l, x in zip(sc, t) if x == "then"]
    rest = [l for l, x in zip(sc[1:], t[1:]) if x != "then"]
    if not then_lines:
        return None
    first = STEP_RE.match(then_lines[0])
    then_lines[0] = f"{first.group(1)}Then{first.group(3)}"
    return [sc[0]] + then_lines + rest


def m_drop_given(sc):
    t = resolved_types(sc)
    if "given" not in t:
        return None
    out = [l for l, x in zip(sc, t) if x != "given"]
    # the first remaining step may be "And ..." -> change it to the correct keyword
    return out


OPERATORS = {"M_NUM": m_num, "M_PARAM": m_param, "M_NEG": m_neg, "M_OP": m_op, "M_DROP_THEN": m_drop_then,
             "M_SWAP_WT": m_swap_wt, "M_THEN_FIRST": m_then_first, "M_DROP_GIVEN": m_drop_given}
FAMILY = {"M_NUM": "B2", "M_PARAM": "B2", "M_NEG": "B2", "M_OP": "B2", "M_DROP_THEN": "B2",
          "M_SWAP_WT": "H3", "M_THEN_FIRST": "H3", "M_DROP_GIVEN": "H3"}


def h3_detect(sc_lines):
    t = [x for x in resolved_types(sc_lines) if x]
    return bool(check_sequence(t, has_background_context=True) & set(ERRORS))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(REPO / "data"))
    ap.add_argument("--n-per-domain", type=int, default=40, help="number of GT scenarios taken per domain")
    ap.add_argument("--no-sbert", action="store_true", help="only check skeleton + H3 (torch not needed)")
    a = ap.parse_args()

    gt = pd.read_csv(Path(a.data) / "full_ground_truth.csv")
    gt = gt[~gt.id.isin([2, 102, 202])]
    rng = random.Random(SEED)
    pool = []
    for _, r in gt.iterrows():
        for header, sc in extract_scenarios(r.gherkin_content):
            pool.append((r.id, r.domain, header, sc))
    chosen = []
    for d in sorted({p[1] for p in pool}):
        cand = [p for p in pool if p[1] == d]
        rng.shuffle(cand)
        chosen += cand[: a.n_per_domain]

    model = None
    if not a.no_sbert:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")

    rows, ce_dir = [], HERE / "counterexamples"
    ce_dir.mkdir(exist_ok=True)
    saved = {}
    for sid, (fid, dom, header, sc) in enumerate(chosen):
        orig = "\n".join(header + sc)
        for op, fn in OPERATORS.items():
            mut_sc = fn(sc)
            if mut_sc is None or mut_sc == sc:
                continue
            mut = "\n".join(header + mut_sc)
            sk_o, sk_m = to_skeleton(orig), to_skeleton(mut)
            row = dict(sample=sid, id=fid, domain=dom, family=FAMILY[op], operator=op,
                       skeleton_identical=sk_o == sk_m, detected_by_h3=h3_detect(mut_sc),
                       orig_detected_by_h3=h3_detect(sc))
            if model is not None:
                e = model.encode([sk_o, sk_m], normalize_embeddings=True)
                row["cosine_orig_vs_mutant"] = float((e[0] * e[1]).sum())
            rows.append(row)
            if saved.get(op, 0) < 3:
                saved[op] = saved.get(op, 0) + 1
                (ce_dir / f"{op}_{saved[op]}_id{fid}.feature").write_text(
                    f"# ORIGINAL (expert GT id={fid}, {dom})\n{orig}\n\n# MUTANT ({op})\n{mut}\n", encoding="utf-8")
    res = pd.DataFrame(rows)
    res.to_csv(HERE / "mutation_results.csv", index=False)

    agg = {"N": ("operator", "size"), "skeleton_identical_%": ("skeleton_identical", "mean"),
           "detected_by_h3_%": ("detected_by_h3", "mean")}
    if model is not None:
        agg["median_cosine"] = ("cosine_orig_vs_mutant", "median")
        agg["missed_by_sbert_%(cos>=0.85)"] = ("cosine_orig_vs_mutant", lambda s: (s >= THRESH).mean())
    summ = res.groupby(["family", "operator"]).agg(**agg).round(4)
    summ.to_csv(HERE / "mutation_summary.csv")
    print(f"Original scenarios: {len(chosen)} | mutants: {len(res)}")
    print(summ.to_string())


if __name__ == "__main__":
    main()
