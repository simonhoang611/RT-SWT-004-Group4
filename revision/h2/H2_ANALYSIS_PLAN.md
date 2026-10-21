# H2 / M1 analysis plan (fixed 16 Oct 2026, before any C1 or C2 output exists)

Written before Hoàng runs `h2_run_prompts.py`. The SHA-256 of this file is recorded in
`revision/h2/H2_ANALYSIS_PLAN.sha256` so the plan can be shown to predate the outputs.
Any change after the outputs exist must be added as a dated amendment below, not edited in place.

## Conditions
- C0: the original run (same-project one-shot, exemplars 2, 102, 202), `results/full_gpt54mini_output.csv`.
- C1: zero-shot. Same model, temperature, system message and clean-up as C0; no example.
- C2: same-project one-shot with exemplars 86 (Sylius), 119 (Fineract), 203 (Diaspora), drawn with
  `numpy.random.default_rng(2026).choice` over the sorted ids of each project, excluding 2, 102, 202.

## Analysis set
- 255 ids: all 261 minus 2, 102, 202, 86, 119, 203, so the three conditions are compared on the same files.
- A call that ends with status ERROR after 5 retries stays in the denominator as a parser FAIL
  and is excluded from the cosine analysis; the count is reported per condition.

## Outcomes and tests
1. Skeleton cosine with the unchanged `to_skeleton` and all-MiniLM-L6-v2 (256-token limit).
   - Per condition: median, IQR, share >= 0.85 with exact 95% CI, one-sided one-sample Wilcoxon
     on x - 0.85 (descriptive for C1 and C2; the confirmatory RQ1 test stays on C0).
   - C1 vs C0 and C2 vs C0: paired two-sided Wilcoxon signed-rank on per-file differences,
     Holm correction over the two comparisons, median paired difference reported.
   - Per project: the same descriptives (no extra tests).
2. Parser compliance with `revision/check_syntax.py` (behave 1.3.3 parser).
   - Per condition: PASS/N with exact 95% Clopper-Pearson CI.
   - C1 vs C0 and C2 vs C0: exact McNemar test (two-sided), Holm over the two comparisons.
3. Output length: median generated characters and completion tokens per condition (descriptive).

## Interpretation fixed in advance
- C2 tests sensitivity to the choice of exemplar, C1 tests the effect of having an exemplar at all.
- A significant C1 vs C0 difference is reported as an effect of the exemplar, not of the model.
- No condition replaces C0 as the primary result.

## Amendments
(none)
