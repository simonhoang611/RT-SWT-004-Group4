"""
h3_order_check.py  --  H3: Check of the order Given -> When -> Then (temporal / causal structure)
================================================================================================
Reviewer R2: skeleton cosine does NOT check the temporal/causal dependency between Given-When-Then.
This script uses behave's parser (which itself resolves And/But to the type of the previous step) and checks every Scenario:

  ERROR (structural violation):
    E1_NO_THEN            scenario has no Then step (no postcondition / verified result)
    E2_GIVEN_AFTER_ACTION a Given step appears AFTER When/Then (precondition placed after the action)
    E3_THEN_BEFORE_WHEN   the first Then step comes BEFORE the first When step (result before cause)
    E4_BG_NOT_GIVEN       Background contains When/Then (Background may only contain preconditions)
  WARNING (anti-pattern, may be a project convention):
    W1_NO_WHEN            no When step (no triggering action)
    W2_NO_CONTEXT         no Given and also no Background
    W3_MULTI_CYCLE        When appears again after Then (G-W-T-W-T...), several behaviours in 1 scenario

Run on BOTH generated and expert GT for comparison (GT = the project's real convention):
    pip install behave pandas
    python h3_order_check.py
Output:
    h3_structure_per_file.csv      -- 1 row / (source, id)
    h3_violations_detail.csv       -- 1 row / violating scenario (to take examples for the paper)
"""
from pathlib import Path

import pandas as pd
from behave.parser import parse_feature

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent  # repository root (this script is in revision/audit/03_H3_temporal_causal/)
ERRORS = ["E1_NO_THEN", "E2_GIVEN_AFTER_ACTION", "E3_THEN_BEFORE_WHEN", "E4_BG_NOT_GIVEN"]
WARNINGS = ["W1_NO_WHEN", "W2_NO_CONTEXT", "W3_MULTI_CYCLE"]


def check_sequence(types, has_background_context):
    """types: list of the step_types ('given'|'when'|'then') of 1 scenario. Returns the set of violation codes."""
    v = set()
    if "then" not in types:
        v.add("E1_NO_THEN")
    if "when" not in types:
        v.add("W1_NO_WHEN")
    if "given" not in types and not has_background_context:
        v.add("W2_NO_CONTEXT")
    seen_action = False
    seen_then = False
    for t in types:
        if t in ("when", "then"):
            if t == "when" and seen_then:
                v.add("W3_MULTI_CYCLE")
            seen_action = True
            seen_then = seen_then or t == "then"
        elif t == "given" and seen_action:
            v.add("E2_GIVEN_AFTER_ACTION")
    if "when" in types and "then" in types and types.index("then") < types.index("when"):
        v.add("E3_THEN_BEFORE_WHEN")
    return v


def analyse_text(text):
    """Returns (file_summary_dict, list_detail_dicts) or (None, None) if the text cannot be parsed."""
    if not isinstance(text, str) or not text.strip():
        return None, None
    try:
        feat = parse_feature(text.replace("\\n", "\n"))
    except Exception:
        return None, None
    if feat is None:
        return None, None
    bg = feat.background
    bg_types = [s.step_type for s in bg.steps] if bg else []
    bg_bad = any(t != "given" for t in bg_types)
    details, counts = [], {k: 0 for k in ERRORS + WARNINGS}
    scen = list(feat.walk_scenarios())
    for sc in scen:
        types = [s.step_type for s in sc.steps]
        v = check_sequence(types, has_background_context=bool(bg_types))
        if bg_bad:
            v.add("E4_BG_NOT_GIVEN")
        for k in v:
            counts[k] += 1
        if v:
            details.append(dict(scenario=sc.name, line=sc.line,
                                sequence="-".join(t[0].upper() for t in types),
                                violations="|".join(sorted(v))))
    n = len(scen)
    n_err = sum(1 for d in details if any(e in d["violations"] for e in ERRORS))
    summary = dict(n_scenarios=n, n_scen_with_error=n_err,
                   file_has_error=n_err > 0,
                   share_scen_error=round(n_err / n, 4) if n else None, **counts)
    return summary, details


def main():
    gen = pd.read_csv(REPO / "results" / "full_gpt54mini_output.csv")
    gt = pd.read_csv(REPO / "data" / "full_ground_truth.csv")
    meta = gt[["id", "domain", "project_name"]]
    rows, det = [], []
    for source, df, col in [("generated", gen, "generated_gherkin"), ("expert_GT", gt, "gherkin_content")]:
        for _, r in df.iterrows():
            s, d = analyse_text(r[col])
            if s is None:
                rows.append(dict(source=source, id=r.id, parse_ok=False))
                continue
            rows.append(dict(source=source, id=r.id, parse_ok=True, **s))
            det += [dict(source=source, id=r.id, **x) for x in d]
    out = pd.DataFrame(rows).merge(meta, on="id")
    out.to_csv(HERE / "h3_structure_per_file.csv", index=False, encoding="utf-8")
    pd.DataFrame(det).merge(meta, on="id").to_csv(HERE / "h3_violations_detail.csv", index=False, encoding="utf-8")

    ok = out[out.parse_ok]
    print("=== Share of FILES with at least 1 scenario violating an ERROR rule (E1-E4) ===")
    print(ok.groupby(["source", "domain"]).file_has_error.agg(["sum", "count", "mean"]).round(3).to_string())
    print("\n=== Total number of violating scenarios by code (generated vs GT) ===")
    print(ok.groupby("source")[ERRORS + WARNINGS + ["n_scenarios"]].sum().T.to_string())


if __name__ == "__main__":
    main()
