# revision/audit/: defect audit, agreement check, structural checks and perturbation test

This folder holds the material behind Section 3.6 (method), Section 4.4 (results), Section 6
(threats) and Appendix B of the revised paper. All paths below are relative to the repository root.
Free-text columns and documents were translated from Vietnamese into English on 19 Oct 2026; labels,
counts and severities are unchanged. See `revision/TRANSLATION_LOG.md` for every translated file and
its original hash.

## How the labels were produced

| Date | Step | Files |
|---|---|---|
| 12 Oct 2026 | An AI coding assistant (OpenAI Codex) drafted B2 (business-logic) and H3 (temporal/causal) labels for the 60 sampled files | `02_B2_semantic_defects/b2_annotation_Codex_AI.csv`, `03_H3_temporal_causal/h3_annotation_Codex_AI.csv` |
| 15 Oct 2026, 22:00 +07:00 | An confirmed in one statement that all 60 cases were reviewed and all labels kept unchanged; the reviewer, decision and source were added to each row | `02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv`, `03_H3_temporal_causal/h3_annotation_An_CONFIRMED.csv`, `confirmation/` |
| 15–16 Oct 2026 | Hoàng labelled 15 files fixed in advance (`02_B2_semantic_defects/double_annotation_ids.txt`) without having seen the labels, by Hoàng's own declaration | `independent_rater_15/*_ORIGINAL.csv`, `independent_rater_15/DECLARATION_AND_KAPPA.md` |
| 16 Oct 2026, 08:33 UTC | Hoàng chose to report κ < 0.7 as a limitation, without the consensus round the protocol required; this deviation is stated in the paper | `independent_rater_15/DECLARATION_AND_KAPPA.md` §5 |
| 18 Oct 2026 | Addendum: a third rule of `make_clean.py` that §2 of the declaration had left out | `independent_rater_15/DECLARATION_ADDENDUM_2026-10-18.md` |

The audited labels are therefore AI-drafted and human-reviewed. The κ values compare one independent
human rater with those labels; they are not agreement between two independent human raters.

## Where each number in the paper comes from

| Paper number | Source file | Produced by |
|---|---|---|
| 60 files, 20 per project, all with skeleton cosine ≥ 0.85 (136 eligible of 258); 15 of them doubly labelled | `02_B2_semantic_defects/b2_annotation_sheet.csv`, `double_annotation_ids.txt` | `02_B2_semantic_defects/b2_make_review_pack.py` (seed 2026); the rule flags shown on each card come from `b2_rule_check.py` (`b2_rule_flags_all.csv`) |
| 25/60 defective (41.7%, 95% CI [29.1, 55.1]); 6/20 Sylius, 16/20 Fineract, 3/20 Diaspora | `07_audit/b2_An_confirmed_summary.txt`, `07_audit/h3_An_confirmed_summary.txt` | `02_B2_semantic_defects/summarize_annotations.py` |
| Business-logic defect types: wrong outcome 20, condition 9, number 8, operator 0, negation 0 | `07_audit/b2_An_confirmed_summary.txt` | same |
| Temporal/causal types: missing verifying Then 19, non-causal Then 9, missing precondition 8 | `07_audit/h3_An_confirmed_summary.txt` | same |
| κ = 0.571 (4/7, B2) and 0.609 (14/23, H3); 12/15 agreement per facet; disagreements on ids 98, 229, 255 (B2) and 229, 236, 255 (H3) | `independent_rater_15/kappa_result.json` | `independent_rater_15/verify_kappa.py` |
| Defects by cosine band (11/24, 10/16, 2/11, 2/9); Mann–Whitney p = 0.21; AUC 0.40 | `revision/results/b3_report.txt` | `revision/b3_threshold_sensitivity.py --audit … --mutation …` |
| Keyword-order flags on 5 of 255 parseable generated files and 40 of 244 parseable reference files | `03_H3_temporal_causal/h3_structure_exemplar_excluded.csv` (the rows of `h3_structure_per_file.csv` without exemplar ids 2, 102, 202) | `03_H3_temporal_causal/h3_order_check.py` |
| Perturbation: 120 scenarios, 683 mutants, 29 that do not parse, Background omitted in 74 of 120 | `06_mutation_test_SBERT/results_audited/mutation_results.csv`, `selected_scenarios.csv` | `06_mutation_test_SBERT/run_mutation_audited.py` |
| 623 valid pairs, minimum cosine 0.8995, 622/623 ≥ 0.90, 97.9% ≥ 0.95; 179 number/value pairs identical; 210 swap/reorder pairs ≥ 0.954, all flagged | `06_mutation_test_SBERT/results_audited/mutation_results.csv` (rows with `pair_parser_valid_baseline_no_hard_error` true) | same |

## Rerunning

From the repository root, with `pip install pandas scipy numpy behave`:

```
python revision/audit/02_B2_semantic_defects/summarize_annotations.py --a revision/audit/02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv --label has_business_defect
python revision/audit/02_B2_semantic_defects/summarize_annotations.py --a revision/audit/03_H3_temporal_causal/h3_annotation_An_CONFIRMED.csv --label has_temporal_causal_defect
python revision/audit/independent_rater_15/verify_kappa.py
python revision/b3_threshold_sensitivity.py --audit revision/audit/02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv --mutation revision/audit/06_mutation_test_SBERT/results_audited/mutation_results.csv
```

On 19 Oct 2026 these four commands, and `make_clean.py` run inside `independent_rater_15/`, reproduced
the committed outputs byte for byte (the two summaries, `kappa_result.json`, the three B3 outputs and
`clean_changes.csv`).

Two parts need more than the packages above:
- The perturbation test needs the SBERT model `sentence-transformers/all-MiniLM-L6-v2` at revision
  `1110a243fdf4706b3f48f1d95db1a4f5529b4d41` (`run_mutation_audited.py --model <local snapshot> --revision 1110a243…`).
  The library versions of the recorded run are in `06_mutation_test_SBERT/model_run_metadata.json` and
  `requirements_measured.txt`. The field `original_script_sha256` in that file is the hash of the
  Vietnamese-comment version of `mutation_sbert_test.py` that was run; the English version differs in
  comments, docstrings and messages and in its default `--data` folder, which now points to `data/`
  (see `revision/TRANSLATION_LOG.md`).
- `07_audit/audit_h3_parser_version.py` compares the structural check under behave 1.2.6 with behave 1.3.3
  (`h3_summary_behave126.csv`, `03_H3_temporal_causal/*_behave126.csv`).

The per-file review cards (`02_B2_semantic_defects/review_cards/`) are not committed; `b2_make_review_pack.py`
regenerates them, together with the sample, after `b2_rule_check.py` has run. The review guide in `confirmation/`
also names a review log (`NHAT_KY_DUYET_60_CASE.xlsx`) and working folders that stayed in the authors' working
package; the outcome of that review is recorded in `confirmation/An_confirmation_2026-10-15.json`.

## Folder contents

| Folder | Content |
|---|---|
| `02_B2_semantic_defects/` | sampling and rule flags, the AI-drafted and the confirmed B2 labels, the label summary script |
| `03_H3_temporal_causal/` | keyword-order check over all files, the AI-drafted and the confirmed H3 labels |
| `06_mutation_test_SBERT/` | perturbation-test protocol and addendum, scripts, recorded run (`results_audited/`, with 24 counterexample files) |
| `07_audit/` | label summaries and the behave-version check |
| `independent_rater_15/` | Hoàng's 15 labels (as rated, and with formatting normalised by `make_clean.py`), the κ script and result, the declaration and its addendum |
| `confirmation/` | record of An's confirmation, its JSON log, and the guide written for the review of the 60 cases |
