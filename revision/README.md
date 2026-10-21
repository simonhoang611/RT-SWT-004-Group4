# revision/ (FISAT 2026 revision of paper 367005)

Contents: the analyses that answer the reviewers' Action Tracker (rounds 1–3 below), the defect audit
(`audit/`, round 4), An's own rerun of the analyses (`nt3_rerun/`), the response letter
(`response_letter/`) and the result notes of 16 Oct 2026 (`RESULTS_B3_H1_B1_2026-10-16.md`).
The revised paper is in `../paper_revised/`. Files translated from Vietnamese are listed in
`TRANSLATION_LOG.md` with the SHA-256 of each original.

## Round 1 (14 Oct 2026): plan items E1, E2, E6, E8

Nothing in `results/` or `data/` is changed. Every new number is written to `revision/results/`.
Run everything from the repository root (`RBL-to-commit/`).

    pip install behave pandas scipy numpy
    python revision/check_syntax.py --input results/full_gpt54mini_output.csv --col generated_gherkin --out revision/results/syntax_parse_n261.csv
    python revision/e1_old_check_demo.py
    python revision/recompute_descriptives.py

| Script | Plan item | Output |
|---|---|---|
| `check_syntax.py` | E1 | `results/syntax_parse_n261.csv` (one row per id, parser error message for the 3 FAIL files) |
| `e1_old_check_demo.py` | E1 | `results/e1_old_check_demo.txt` (the old `check_executable()` returns PASS even for plain text) |
| `recompute_descriptives.py` | E2, E6, E8 | `results/descriptives_skeleton_cosine.csv`, `results/exemplar_scores.csv` |

`results/numbers_round1.csv` lists each old value from the submitted PDF next to the recomputed value.
Its status column was written before NT3 and still reads "TO CONFIRM"; An's own rerun on 19 Oct 2026
reproduced all 15 output tables (`nt3_rerun/`).

Computed on 14 Oct 2026 with behave 1.3.3, Python 3.13, scipy 1.18, pandas 3.0. The original runs
used behave 1.2.6 according to the proposal; rerun `check_syntax.py` with 1.2.6 to confirm the 3 FAIL ids.

Definitions to state in the paper: quartiles by linear interpolation (Hyndman-Fan type 7); SD with
ddof = 1; Wilcoxon one-sample signed-rank on x - 0.85, one-sided "greater", zero differences dropped;
Cliff's delta against the threshold = P(x > 0.85) - P(x < 0.85). The reported 0.038 could not be
reproduced: `full_analysis.ipynb` has no cell that computes delta, so its formula is unknown. Exemplars (one-shot examples, ids 2, 102, 202) are reported both included
and excluded.

## Round 2 (16 Oct 2026): Action Tracker B3, H1, B1, H2

These analyses are post-hoc (planned after the reviews) and must be labelled that way in the paper.
They were run in the cloud container with Python 3.13.16, pandas 3.0.5, scipy 1.18.1, numpy 2.5.3.

    python revision/b3_threshold_sensitivity.py --audit <b2_annotation_An_CONFIRMED.csv> --mutation <mutation_results.csv>
    python revision/h1_domain_analysis.py
    python revision/b1_leakage_proxy.py

`--audit` used `FISAT_gui_Hoang_2026-10-15/02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv`
(SHA-256 7f6780dd...b28) and `--mutation` used `06_mutation_test_SBERT/results_audited/mutation_results.csv`
from the same package (the authors' working package). Both are now in this repository:
`audit/02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv` (English translation of the free-text columns;
the label columns the script reads are unchanged, see `TRANSLATION_LOG.md`) and
`audit/06_mutation_test_SBERT/results_audited/mutation_results.csv` (unchanged). From the repository root:

    python revision/b3_threshold_sensitivity.py --audit revision/audit/02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv --mutation revision/audit/06_mutation_test_SBERT/results_audited/mutation_results.csv

| Script | Item | Output in `results/` |
|---|---|---|
| `b3_threshold_sensitivity.py` | B3 | `b3_threshold_sweep.csv`, `b3_mutation_by_threshold.csv`, `b3_report.txt` |
| `h1_domain_analysis.py` | H1 | `h1_domain_table.csv`, `h1_pairwise.csv`, `h1_report.txt` |
| `b1_leakage_proxy.py` | B1 | `b1_overlap_per_file.csv`, `b1_spearman.csv`, `b1_report.txt` |
| `h2/h2_run_prompts.py` | H2/M1 | calls the API; writes `h2/h2_C1_*` and `h2/h2_C2_*` (run by Hoàng with Hoàng's own key; see `h2/H2_RUN_GUIDE.md`) |

H2 conditions: C1 zero-shot, C2 one-shot with exemplars 86, 119, 203 drawn with
`numpy.random.default_rng(2026)` before any C2 output existed. All H2 comparisons exclude
ids 2, 102, 202, 86, 119, 203 (255 ids).

## Round 3 (16 Oct 2026): H2 and M1 analysis

The plan `h2/H2_ANALYSIS_PLAN.md` was fixed before the runs (SHA-256 in `h2/H2_ANALYSIS_PLAN.sha256`).
Run facts, cost and the encoder note are in `h2/H2_NOTES.md`.

    python revision/h2/h2_cosine_onnx.py --onnx-dir <folder with model.onnx and tokenizer.json>
    python revision/check_syntax.py --input revision/h2/h2_C1_output.csv --col generated_gherkin --out revision/h2/h2_syntax_C1.csv
    python revision/check_syntax.py --input revision/h2/h2_C2_output.csv --col generated_gherkin --out revision/h2/h2_syntax_C2.csv
    python revision/check_syntax.py --input results/full_gpt54mini_output.csv --col generated_gherkin --out revision/h2/h2_syntax_C0.csv
    python revision/h2/h2_analysis.py
    python revision/h2/h2_cosine_st_check.py   # optional; needs huggingface.co

The ONNX export is Chroma's `all-MiniLM-L6-v2/onnx.tar.gz`
(https://chroma-onnx-models.s3.amazonaws.com/all-MiniLM-L6-v2/onnx.tar.gz, archive SHA-256 in `h2/H2_NOTES.md`).

| Script | Item | Output in `h2/` |
|---|---|---|
| `h2/h2_cosine_onnx.py` | H2 | `h2_cosine_per_file.csv`, `h2_cosine_check.txt` |
| `check_syntax.py` | M1 | `h2_syntax_C0.csv`, `h2_syntax_C1.csv`, `h2_syntax_C2.csv` |
| `h2/h2_analysis.py` | H2/M1 | `h2_results_table.csv`, `h2_results_pairwise.csv`, `h2_results_by_project.csv`, `h2_report.txt` |
| `h2/h2_cosine_st_check.py` | H2 | `h2_cosine_st.csv`, `h2_cosine_st_check.txt` (sentence-transformers confirmation) |

## Round 4: defect audit and perturbation test (B2, H3)

`audit/` holds the 60-file defect audit (AI-drafted labels, reviewed by a second author), the
independent rater's 15 files with Cohen's kappa, the keyword-order check and the perturbation test.
How each number in the paper is reproduced is described in `audit/README.md`.

## NT3: rerun by An (19 Oct 2026)

An ran the 10 scripts of rounds 1–3 on An's own machine with `nt3_rerun/run_checks.py`; all 15 output
tables matched the stored ones. The script, its input manifest, An's result file and logs, and a short
report are in `nt3_rerun/`.

## Response letter

`response_letter/Response_to_Reviewers_367005.md` (and `.pdf`) is the letter sent with the revision.
