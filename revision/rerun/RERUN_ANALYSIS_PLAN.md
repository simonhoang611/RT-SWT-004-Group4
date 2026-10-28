# Rerun analysis plan for H2, H4, H11 and M11 (fixed 28 Oct 2026, before any rerun output exists)

Written before `revision/rerun/rerun_conditions.py` is run. The SHA-256 of this file is recorded in
`revision/rerun/RERUN_ANALYSIS_PLAN.sha256`, and this file is committed before the run, so the plan
can be shown to predate the outputs. Any change after the outputs exist is added as a dated
amendment at the end, not edited in place. All analyses here were planned after the reviews and are
exploratory.

## Purpose (Action Tracker v1)
- H2: rerun C0 at the same time and with the same logging path as C1 and C2.
- H4: repeat C0, C1 and C2 on a stratified subset; report intraclass / run-to-run variance and the
  share of files that change parser outcome or side of the 0.85 reference point.
- H11: repeat C0 and C2 on a subset stratified by project; report within-prompt variance, the
  between-prompt effect and per-file confidence intervals.
- M11: run the capped condition planned in the research proposal (1,500 output tokens).

## Design
- Conditions: C0 (exemplars 2, 102, 202), C1 (zero-shot), C2 (exemplars 86, 119, 203) and C0cap
  (C0 with `max_completion_tokens` = 1500). Model, temperature, system messages, prompt wording and
  clean-up are those of the original run and of `revision/h2/h2_run_prompts.py`.
- Rep 1: all 261 stories in all four conditions. Reps 2 to 5: the 60-story subset (20 per project),
  conditions C0, C1, C2. The subset was drawn with `numpy.random.default_rng(20261028).choice`
  over the sorted ids of each project that are not an exemplar in C0 or C2; the ids are fixed in
  the script.
- All jobs are shuffled once with seed 20261028 and run by 4 parallel workers, so the conditions
  are interleaved in time. Each call logs the returned model name, response id, system fingerprint,
  finish reason, token usage and timestamp.

## Measures
- Skeleton cosine: unchanged `to_skeleton` of `scripts/compute_metrics.py`, all-MiniLM-L6-v2
  (256-token limit, mean pooling, normalisation), computed as in `revision/h2/h2_cosine_onnx.py`;
  the original C0 scores are recomputed as a check.
- Parser outcome: `revision/check_syntax.py` (behave 1.3.3 parser).
- Analysis sets: 255 files (not an exemplar in any condition) for comparisons between conditions;
  258 files (not a C0 exemplar) for the RQ1/RQ2 statistics of the new C0 and of C0cap; the 60
  subset files for the repeat analyses.
- A job that is not OK after the script's retries and one resumed rerun stays in the denominator
  as a parser FAIL and is excluded from the cosine analysis; the count is reported per condition.

## Analyses
1. Same-time ablation (H2), rep 1, 255 files. Per condition: median, IQR, share >= 0.85 with exact
   95% CI, parser PASS with Clopper-Pearson CI. C1 vs new C0 and C2 vs new C0: paired two-sided
   Wilcoxon signed-rank on cosine and exact McNemar on parser outcome, Holm over the two
   comparisons, median paired difference. The same descriptives per project, without tests.
2. RQ1 and RQ2 on the new C0, rep 1, 258 files: exact sign test and one-sided Wilcoxon against 0.85,
   bootstrap 95% CI of the median (10,000 resamples, seed 2026), PASS rate with Clopper-Pearson CI
   and risk difference from 0.80. Reported next to the original C0; the original C0 stays the
   primary result.
3. Change over time: new C0 (rep 1) against the original C0 run on the 258 files: number of
   byte-identical outputs, per-file cosine difference (median, IQR, paired Wilcoxon), files whose
   parser outcome or side of 0.85 differs.
4. Run-to-run variation (H4), 60 files x 5 reps, for each of C0, C1, C2: number of files whose 5
   outputs are byte-identical; per-file SD of cosine and its median; pooled within-file SD;
   ICC(1,1) (one-way random effects, files as targets, reps as repetitions) with its 95% CI;
   number of files whose parser outcome changes across the 5 reps; number whose side of 0.85
   changes. The pooled within-file SD is compared, descriptively, with the paired median
   differences of analysis 1 and of the original ablation (-0.028 for C1, +0.008 for C2).
5. Within- and between-prompt variation (H11), C0 and C2 on the 60 files x 5 reps: two-way
   ANOVA with replication (file random, prompt fixed) giving the within-prompt (residual) variance,
   the file x prompt variance and the mean between-prompt effect (mean over files of the C2 mean
   minus the C0 mean) with a 95% CI from a paired t-interval over the 60 file means. Per file: the
   C2 - C0 difference of the 5-rep means with a Welch 95% CI; we report how many CIs lie wholly
   above 0, wholly below 0 or include 0. The same per project, descriptively.
6. Capped condition (M11), rep 1, 258 files: number of outputs stopped by the cap
   (`finish_reason` = length), parser PASS with Clopper-Pearson CI, median cosine; C0cap vs new C0:
   exact McNemar and paired Wilcoxon (two-sided, no correction, descriptive).

## Interpretation fixed in advance
- The rerun does not replace the original C0 as the primary result of RQ1 and RQ2.
- A C1 or C2 difference against the new C0 is attributed to the prompt only for this time window.
- If the outputs vary between reps, the ablation and RQ1 decisions are read against that variation;
  a median difference smaller than the pooled within-file SD is not reported as a prompt effect.

## Amendments
(none)
