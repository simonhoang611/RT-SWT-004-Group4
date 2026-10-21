"""
b2_rule_check.py  --  B2: Rule-based critical-token check (numbers, operators, negation, conditions)
=============================================================================================
Goal (Reviewer R1, R3): SBERT skeleton cosine can give a high score even when a scenario gets the business
logic wrong in "small but critical" tokens (numbers, comparison operators, negation, conditional clauses).

This script does NOT conclude that there is a defect. It only flags candidates for An to check manually.
Main comparison:      generated Gherkin  <->  user story (the input the model received, with Acceptance Criteria).
Secondary comparison: generated Gherkin  <->  expert ground truth (GT).
  (The Fineract GT is very long and the Fineract user stories were created from the first 15,000 characters
   of the GT, so the comparison with the GT is for reference only.)

How to run (from the folder 02_B2_semantic_defects):
    pip install pandas
    python b2_rule_check.py
Output:
    b2_rule_flags_all.csv        -- 261 rows, one row per id, columns with token counts / missing tokens
    b2_candidates_highcos.csv    -- only the ids with skeleton_cosine >= 0.85 AND flagged, sorted by suspicion level
"""
import re
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent.parent.parent  # repository root (this script is in revision/audit/02_B2_semantic_defects/)
THRESH = 0.85
EXEMPLAR_IDS = {2, 102, 202}  # 3 few-shot examples -- they are in the test set, excluded from the analysis

# ---------- Dictionary of critical tokens ----------
NEGATION = [r"\bnot\b", r"\bno\b", r"\bnever\b", r"\bcannot\b", r"\bcan't\b", r"\bwon't\b",
            r"\bshouldn't\b", r"\bisn't\b", r"\baren't\b", r"\bdoesn't\b", r"\bdon't\b",
            r"\bwithout\b", r"\bunable\b", r"\bdisabled\b", r"\binvalid\b", r"\bfail(s|ed)?\b",
            r"\breject(s|ed)?\b", r"\bdenied\b", r"\bprevent(s|ed)?\b"]
OPERATORS = {  # group -> regex
    "GT":  r"\b(more than|greater than|above|exceed(s|ing)?|over)\b|>",
    "GTE": r"\b(at least|minimum|no less than|or more)\b|>=",
    "LT":  r"\b(less than|fewer than|below|under)\b|<(?!PARAM|NUM)",
    "LTE": r"\b(at most|maximum|no more than|up to|or less)\b|<=",
    "EQ":  r"\b(equal(s)? to|exactly)\b",
    "ARITH": r"\b(plus|minus|multipl(y|ied)|divid(e|ed)|percent|%|sum|total|subtract|add(ed)? to)\b",
}
CONDITIONAL = [r"\bif\b", r"\bunless\b", r"\bonly\b", r"\bonly if\b", r"\bwhen\b", r"\bafter\b",
               r"\bbefore\b", r"\bbecause\b", r"\bso that\b", r"\buntil\b", r"\bwhile\b", r"\bonce\b"]
NUM_RE = re.compile(r"(?<![\w.])\d{1,4}[-/]\d{1,2}[-/]\d{1,4}|(?<![\w.])\d+(?:[.,]\d+)?%?")
MONTHS = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
DATE_TXT_RE = re.compile(r"\b\d{1,2} " + MONTHS + r" \d{4}\b")


def norm(t):
    return t.replace("\\n", "\n") if isinstance(t, str) else ""


def us_ac_part(us):
    """Take the Acceptance Criteria part of the user story (where the business conditions are)."""
    us = norm(us)
    i = us.lower().find("acceptance criteria")
    return us[i:] if i >= 0 else us


def numbers(t):
    vals = set(n.rstrip("%").replace(",", ".") for n in NUM_RE.findall(t))
    vals |= {m.group(0) for m in DATE_TXT_RE.finditer(t)}
    return vals


def count(patterns, t):
    t = t.lower()
    return sum(len(re.findall(p, t)) for p in patterns)


def op_groups(t):
    t = t.lower()
    return {g for g, p in OPERATORS.items() if re.search(p, t)}


def main():
    us = pd.read_csv(REPO / "data" / "full_user_stories.csv")
    us.columns = [c.strip("﻿") for c in us.columns]
    gen = pd.read_csv(REPO / "results" / "full_gpt54mini_output.csv")
    gt = pd.read_csv(REPO / "data" / "full_ground_truth.csv")
    met = pd.read_csv(REPO / "results" / "full_per_row_metrics.csv")
    df = (gen[["id", "generated_gherkin"]]
          .merge(us[["id", "domain", "project_name", "user_story"]], on="id")
          .merge(gt[["id", "expert_filename", "gherkin_content"]], on="id")
          .merge(met[["id", "skeleton_cosine"]], on="id"))

    rows = []
    for _, r in df.iterrows():
        g, s, ref = norm(r.generated_gherkin), us_ac_part(r.user_story), norm(r.gherkin_content)
        n_us, n_gen = numbers(s), numbers(g)
        miss_num = sorted(n_us - n_gen)
        invented = sorted(n_gen - n_us - numbers(ref))  # numbers in gen but in neither the US nor the GT
        ops_us, ops_gen = op_groups(s), op_groups(g)
        miss_ops = sorted(ops_us - ops_gen)
        neg_us, neg_gen, neg_gt = count(NEGATION, s), count(NEGATION, g), count(NEGATION, ref)
        cond_us, cond_gen = count(CONDITIONAL, s), count(CONDITIONAL, g)
        flags = []
        if miss_num:
            flags.append("NUM_MISSING")
        if miss_ops:
            flags.append("OP_MISSING")
        if len(invented) >= 3:
            flags.append("NUM_INVENTED")
        if neg_us > 0 and neg_gen == 0:
            flags.append("NEG_DROPPED")
        elif neg_us > 0 and neg_gen < 0.5 * neg_us:
            flags.append("NEG_REDUCED")
        if cond_us > 0 and cond_gen == 0:
            flags.append("COND_DROPPED")
        # suspicion level: number of missing numbers + the other flags
        score = min(len(miss_num), 10) + min(len(invented), 10) // 2 + 2 * len(miss_ops) + 3 * ("NEG_DROPPED" in flags) \
            + 1 * ("NEG_REDUCED" in flags) + 2 * ("COND_DROPPED" in flags)
        rows.append(dict(
            id=r.id, domain=r.domain, project=r.project_name, expert_filename=r.expert_filename,
            skeleton_cosine=round(r.skeleton_cosine, 4), high_cos=r.skeleton_cosine >= THRESH,
            exemplar=r.id in EXEMPLAR_IDS,
            n_numbers_in_US_AC=len(n_us), numbers_missing_in_gen="; ".join(miss_num[:30]),
            n_numbers_missing=len(miss_num),
            n_numbers_invented=len(invented), numbers_invented_sample="; ".join(invented[:15]),
            ops_in_US=",".join(sorted(ops_us)), ops_missing_in_gen=",".join(miss_ops),
            neg_US=neg_us, neg_gen=neg_gen, neg_GT=neg_gt, cond_US=cond_us, cond_gen=cond_gen,
            flags="|".join(flags), suspicion_score=score))
    out = pd.DataFrame(rows)
    out.to_csv("b2_rule_flags_all.csv", index=False, encoding="utf-8")

    hc = out[out.high_cos & ~out.exemplar]
    cand = hc[hc["flags"] != ""].sort_values("suspicion_score", ascending=False)
    cand.to_csv("b2_candidates_highcos.csv", index=False, encoding="utf-8")

    print(f"Total: {len(out)} | high-cos (>= {THRESH}, 3 exemplars excluded): {len(hc)} | of which flagged: {len(cand)}")
    print("\nFlag rate by domain (high-cos):")
    print(hc.assign(flagged=hc["flags"] != "").groupby("domain").flagged.agg(["sum", "count"]).to_string())
    print("\nFrequency of each flag type (high-cos):")
    print(hc["flags"].str.split("|").explode().replace("", pd.NA).dropna().value_counts().to_string())


if __name__ == "__main__":
    main()
