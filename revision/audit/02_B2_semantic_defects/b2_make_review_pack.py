"""
b2_make_review_pack.py  --  Creates the manual review sample for B2 (also reused for H3)
==================================================================================
Draws a STRATIFIED random sample from the scenarios with skeleton_cosine >= 0.85 (3 exemplars 2/102/202 excluded):
    20 Sylius + 20 Fineract + 20 Diaspora = 60 scenarios, seed = 2026 (stated in the paper).
Random sample => the estimated defect rate is UNBIASED (not only easy/hard cases picked).

Output:
    b2_annotation_sheet.csv      -- annotation sheet (filled in by An), 1 row / id
    review_cards/<id>.md         -- 1 file per id: User Story | Generated | Expert GT (for reading)
    double_annotation_ids.txt    -- 15 ids (25%) that both An and Hoang annotate independently -> Cohen's kappa
Run:  python b2_make_review_pack.py      (after running b2_rule_check.py)
"""
from pathlib import Path

import pandas as pd

SEED = 2026
PER_DOMAIN = 20
N_DOUBLE = 15
GT_MAX_LINES = 250  # Fineract GT is very long; truncated for readability (noted in the card)

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent  # repository root (this script is in revision/audit/02_B2_semantic_defects/)


def main():
    flags = pd.read_csv(HERE / "b2_rule_flags_all.csv")
    us = pd.read_csv(REPO / "data" / "full_user_stories.csv")
    us.columns = [c.strip("﻿") for c in us.columns]
    gen = pd.read_csv(REPO / "results" / "full_gpt54mini_output.csv")
    gt = pd.read_csv(REPO / "data" / "full_ground_truth.csv")

    pool = flags[(flags.high_cos) & (~flags.exemplar)]
    parts = [pool[pool.domain == d].sample(n=min(PER_DOMAIN, (pool.domain == d).sum()), random_state=SEED)
             for d in sorted(pool.domain.unique())]
    sample = pd.concat(parts).sort_values(["domain", "id"])
    dbl = sample.sample(n=N_DOUBLE, random_state=SEED)["id"].sort_values().tolist()
    (HERE / "double_annotation_ids.txt").write_text("\n".join(map(str, dbl)) + "\n", encoding="utf-8")

    cols = ["id", "domain", "skeleton_cosine", "flags", "double_annotate"]
    sheet = sample.assign(double_annotate=sample.id.isin(dbl))[cols].copy()
    for c in ["annotator",
              "n_AC_total", "n_AC_covered_correctly",      # number of Acceptance Criteria in the US and number of ACs expressed correctly
              "D_NUM", "D_OP", "D_NEG", "D_COND", "D_OUTCOME", "D_MISSING_AC", "D_EXTRA", "D_ORDER",
              "severity_max",                             # 0 none, 1 minor, 2 major, 3 critical
              "has_business_defect",                      # Y / N  (Y if there is at least 1 defect with severity >= 2)
              "rule_flag_confirmed",                      # Y / N / NA : is the script's flag correct?
              "evidence_gen_line", "evidence_US_or_GT_line", "note"]:
        sheet[c] = ""
    sheet.to_csv(HERE / "b2_annotation_sheet.csv", index=False, encoding="utf-8-sig")

    cards = HERE / "review_cards"
    cards.mkdir(exist_ok=True)
    for _, r in sample.iterrows():
        i = int(r.id)
        u = us.loc[us.id == i, "user_story"].iloc[0].replace("\\n", "\n")
        g = gen.loc[gen.id == i, "generated_gherkin"].iloc[0].replace("\\n", "\n")
        ref_full = gt.loc[gt.id == i, "gherkin_content"].iloc[0].replace("\\n", "\n").split("\n")
        ref = "\n".join(ref_full[:GT_MAX_LINES])
        cut = (f"\n# ... [GT truncated: showing {GT_MAX_LINES}/{len(ref_full)} lines. See the full text in "
               f"data/full_ground_truth.csv, id={i}]") if len(ref_full) > GT_MAX_LINES else ""
        (cards / f"{i:03d}.md").write_text(
            f"# Review card id={i} | {r.domain} | skeleton_cosine={r.skeleton_cosine}\n\n"
            f"- Expert file: `{r.expert_filename}`\n- Rule flags: `{r.flags if isinstance(r.flags, str) else ''}`\n"
            f"- Numbers missing compared with the US: `{r.numbers_missing_in_gen if isinstance(r.numbers_missing_in_gen, str) else ''}`\n"
            f"- Missing operators: `{r.ops_missing_in_gen if isinstance(r.ops_missing_in_gen, str) else ''}`\n"
            f"- 'Invented' numbers (in neither the US nor the GT): {r.n_numbers_invented} -> e.g. `{r.numbers_invented_sample if isinstance(r.numbers_invented_sample, str) else ''}`\n\n"
            f"## 1. User story (the input the model received = SPEC used for grading)\n\n```text\n{u}\n```\n\n"
            f"## 2. Generated Gherkin (GPT-5.4-mini)\n\n```gherkin\n{g}\n```\n\n"
            f"## 3. Expert ground truth (reference)\n\n```gherkin\n{ref}{cut}\n```\n",
            encoding="utf-8")
    print(f"Sample: {len(sample)} ids ({sample.domain.value_counts().to_dict()}); double-annotate: {dbl}")
    print("Created b2_annotation_sheet.csv and review_cards/")


if __name__ == "__main__":
    main()
