"""
h3_make_annotation_sheet.py  --  Manual review sheet for H3 (pre/postconditions, causality)
==========================================================================================
REUSES the 60 ids sampled in B2 (same review_cards/) so that An reads each scenario only once and fills in 2 sheets.
Run after: b2_make_review_pack.py and h3_order_check.py
"""
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
b2 = pd.read_csv(HERE.parent / "02_B2_semantic_defects" / "b2_annotation_sheet.csv")
st = pd.read_csv(HERE / "h3_structure_per_file.csv")
st = st[st.source == "generated"][["id", "n_scenarios", "n_scen_with_error", "W1_NO_WHEN", "W3_MULTI_CYCLE"]]
sheet = b2[["id", "domain", "skeleton_cosine", "double_annotate"]].merge(st, on="id", how="left")
sheet = sheet.rename(columns={"n_scen_with_error": "auto_order_errors"})
for c in ["annotator",
          "n_AC_with_precondition",   # number of ACs in the US that have a precondition (initial state)
          "PRE_missing",              # number of REQUIRED preconditions that do not appear in Given/Background
          "ACTION_wrong",             # 0/1: the When step is not the triggering action that the AC describes
          "POST_missing",             # number of expected results (AC) with no Then step verifying them
          "CAUSAL_wrong",             # 0/1: Then is not a consequence of When, or an impossible state transition
          "ORDER_wrong",              # 0/1: the state sequence is in the wrong order (e.g. confirm order before add to cart)
          "has_temporal_causal_defect",  # Y/N
          "counterexample_quote",     # copy 2-4 Gherkin lines verbatim as an example
          "note"]:
    sheet[c] = ""
sheet.to_csv(HERE / "h3_annotation_sheet.csv", index=False, encoding="utf-8-sig")
print(f"Created h3_annotation_sheet.csv ({len(sheet)} rows)")
