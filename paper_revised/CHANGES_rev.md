# Changes from the baseline (the version submitted for review), 16–18 Oct 2026

Note on paths (added when this log was committed, 19 Oct 2026). The log was written in the authors' working folders:
`../paper_lncs` is a working folder with a LaTeX transcription of the version submitted for review (not in this repository; the pre-revision paper as committed is in `paper/`, tag `v1-submitted`); `revision_round1/revision/` is `revision/`;
`hoang_15_phieu/frozen_2026-10-16/` is `revision/audit/independent_rater_15/`; files of An's package
`FISAT_gui_Hoang_2026-10-15/` are in `revision/audit/` under the same subfolder names; `THU_PHAN_HOI_draft.md`
and `goi_gui_co/Response_to_Reviewers_367005.pdf` are `revision/response_letter/Response_to_Reviewers_367005.*`;
`KHAI_BAO_BO_SUNG_2026-10-18.md` is `revision/audit/independent_rater_15/DECLARATION_ADDENDUM_2026-10-18.md`.
Other folder names (`FISAT_phan_hoi_Hoang_2026-10-17`, `KIEM_TRA_PHAN_HOI_AN_*`, `camera_ready/`) are working folders that are not in this repository.

Every number below comes from `revision_round1/revision/results/`, `hoang_15_phieu/frozen_2026-10-16/`
or An's package `FISAT_gui_Hoang_2026-10-15/` (file named per row). H2 results were added on 16 Oct 2026 (afternoon); no `\pending` marker is left.

## Action Tracker

| ID | What the paper now contains | Where | Source | State |
|---|---|---|---|---|
| B1 | Story construction described (GPT-5.4-mini, temperature 0, first 15,000 characters; 84 Fineract files cut). Trigram overlap story–reference: median 4.9%; Spearman ρ with cosine 0.29 / 0.33 / 0.11 (Sylius / Diaspora / Fineract; values after the 19 Oct correction below). External-validity claim narrowed. No external backlog | §3.1, §4.5, §6.1 | `b1_spearman.csv`, `b1_overlap_per_file.csv` | Done (proxy + narrowed claim) |
| B2 | Defect audit of 60 files ≥ 0.85: 25/60 defective (6/16/3). Example id 76. Perturbation test: 623 valid pairs, all ≥ 0.8995 | §3.6, §4.4 | `b2_annotation_An_CONFIRMED.csv`, `mutation_results.csv` | Done |
| B3 | Threshold sweep 0.80–0.90 (Table 6, Appendix A). No calibration possible; claims softened, 0.85 called a descriptive reference point | §3.4, §4.3, §5.2 | `b3_threshold_sweep.csv`, `b3_report.txt` | Done (softened) |
| H1 | Per-project table (Table 3), Kruskal–Wallis, Holm pairwise, Fig. 2 (Appendix A). Pooled claim removed | §4.2, §5.1 | `h1_domain_table.csv`, `h1_pairwise.csv` | Done |
| H2 | C1 zero-shot: median 0.819, 34.5% ≥ 0.85, 182/255 files lower than C0 (Holm p < 0.001). C2 other exemplars: median 0.875, 64.3% ≥ 0.85, one-sided p < 0.001 vs 0.85 (RQ1 decision would flip), driven by Fineract (0.827 → 0.876) | §3.2, §4.7, Table 4, §5.1–5.2, §6.1, §7, Abstract | `revision/h2/h2_report.txt`, `h2_results_*.csv`, plan sha256 bb2197dd…; encoder check `h2_cosine_check.txt`, `h2_cosine_st_check.txt` | Done |
| H3 | Temporal/causal facet of the audit; keyword-order check (5/255 generated, 40/244 reference); swap/then-first mutants | §3.6, §4.4 | `h3_annotation_An_CONFIRMED.csv`, `h3_structure_per_file.csv` | Done |
| M1 | Parser PASS 252 / 252 / 254 of 255 (C0 / C1 / C2), McNemar Holm p = 1.0; compliance does not depend on the exemplar | §4.7, §5.1 | `revision/h2/h2_syntax_C*.csv` | Done |
| L1 | Response letter grouped by the five themes | `../revision_round1/THU_PHAN_HOI_draft.md`; final copy `../revision_round1/goi_gui_co/Response_to_Reviewers_367005.pdf` | — | Done |

## Errors fixed (E1–E15)

| ID | Baseline | Revised |
|---|---|---|
| E1 | 261/261 = 100%, CI [98.6, 100] | 255/258 (98.84%), CI [96.64, 99.76], p = 4.6e-21; N = 261: 258/261. Dry-run bug explained (§3.5) |
| E2 | Table 3 min 0.742, Q1 0.831, Q3 0.874, max 0.921, SD 0.031, δ 0.038 | Recomputed (now Table 2), both N; δ formula stated; 0.038 dropped (not reproducible) |
| E3 | "removes structural keywords" | Keywords kept, tags removed, `<PARAM>`/`<NUM>` masking, non-keyword lines dropped (§2.2, §3.4, Table 5 in Appendix A) |
| E4 | not mentioned | 256-token truncation: 174/258 GT, 166/258 generated, 94/99 Fineract GT |
| E5 | "converted into a compact user story" | GPT-5.4-mini, temperature 0, first 15,000 characters, 84 files cut |
| E6 | exemplars in test set not mentioned | Excluded, N = 258 primary, exemplar scores 1.000 / 0.997 / 1.000 |
| E7 | "prespecified" | Pilot of 30 ids (in test set, mean 0.859) disclosed; no calibration |
| E8 | "social-network subset more consistent" | IQR: Diaspora 0.087 widest, Fineract 0.062 narrowest |
| E9 | dry-run "exercises the parsing/loading path" | parser only, no steps (§2.3, §3.5, §6.2) |
| E10 | log has "model version and cost" | requested model name, outdated price; recomputed ≈ $1.96 at Standard price |
| E11 | [12] no DOI | DOI added to Clopper–Pearson; 3 new references (Cohen, Kruskal–Wallis, Holm) need a publisher-page check |
| E12 | H0 on median, proposal on mean | stated in §3.7 |
| E13 | "each source scenario was first required to parse" | 14/261 GT fail with behave 1.3.3 (13 with 1.2.6) |
| E14 | unit unclear | feature file; 2,554 GT / 1,913 generated scenarios (behave 1.3.3, N = 258) |
| E15 | cap of 1,500 not mentioned | deviation declared (§3.2, §6.3) |

## Other changes
- κ below 0.7 and the skipped consensus round (deviation from RBL-4) declared in §4.4 and §6.2.
- H1 effect size reported as η²_H = 0.231 (the round-2 script had labelled this formula ε²; fixed 16/10).
- Fig. 3 (bar chart of PASS/FAIL) removed; Figs. 1–2 replaced by the N = 258 versions from An's package
  (`figures_recomputed_258/`, provenance in `figure_provenance.json`).
- Disclosure now names AI use: story writing (GPT-5.4-mini), audit labels (Codex), scripts and text (Codex, Claude).
- Length: the FISAT 2026 call for papers (checked 17 Oct 2026) allows 12–15 pages for full papers, excluding appendices and references, and charges for extra pages. On Hoàng's decision (17 Oct) the prompt listing, the skeleton example, Figs. 1–2, the threshold table, the RQ2 table and the perturbation details moved to Appendices A–B; §5.5 (duplicated by the conclusion) and three repeated sentences were removed. In the lmodern test build the conclusion now ends on page 15; disclosure and references follow on pages 15–16, appendices on pages 17–19. Recheck after the Overleaf build.

## Changes after An's review (17 Oct 2026)
Source: `FISAT_phan_hoi_Hoang_2026-10-17` (An, with Codex) and `revision_round1/KIEM_TRA_PHAN_HOI_AN_2026-10-17.md`. No number changed.
- §3.6: the 15-file rater is the first author, not "a third author"; independence is stated as self-declared (also §6.2, letter). κ recomputed from `hoang_15_phieu/frozen_2026-10-16/`: 0.571 / 0.609.
- §5.2: seeded defects keep the score at or above 0.8995 (was "above 0.91"; min is M_DROP_GIVEN).
- §5.1: the skeleton drops table rows (was "Background tables").
- Abstract, §5.1, §7: C2 is one different exemplar per project (was "three other exemplars").
- §4.2, §4.3, §4.7, §5, §6.2, §7: non-significant results no longer read as "do not differ" / "did not depend" / "not an artefact"; McNemar does not establish equivalence.
- §6.1: only the C1/C2 logs record the returned model name. §6.3: the missing output cap may affect both outcomes (was "not the analysis").
- §3.2: the H2 plan "was written before the C1 and C2 runs" and is shipped with its SHA-256. §3.3: C0 cost is an estimate. §3.7: symmetry assumption of the signed-rank test. §3.8: only the exemplars are excluded. RQ1 renamed "Skeleton similarity". Holm reference: JSTOR link.

## Changes after An's second review (18 Oct 2026)
Source: `FISAT_phan_hoi_Hoang_2026-10-18` (An, with Codex) and `revision_round1/KIEM_TRA_PHAN_HOI_AN_2026-10-18.md`. No number or label changed; κ 0.571 / 0.609 reproduced from the frozen sheets.
- Disclosure: Claude prepared the 15-file rater's reading aids (rubric notes, AC map, Fineract reading sheets and glossary), none containing labels. Letter updated to match. (Placed in the disclosure, not §3.6, because a sentence in §3.6 pushed the conclusion to page 16.)
- §7: κ described as "below our protocol's threshold of 0.7" (was "moderate").
- The cleaning rule omitted from the 16 Oct declaration (evidence text of defect-free rows moved to `note`) is recorded in `hoang_15_phieu/KHAI_BAO_BO_SUNG_2026-10-18.md`.
- Test build after this change: 19 pages, 0 errors; the conclusion still ends on page 15.

## Decisions confirmed by Hoàng (18 Oct 2026)
- The paper is in the Final Track (camera-ready deadline 29 Oct 2026). The 20 Oct date is for the mentor's last check.
- The mentor agreed to report κ < 0.7 as a limitation, with no consensus round or relabelling (as in §4.4 and §6.2).
- Template: the folder `Springer_Nature_LaTeX_Template` (sn-jnl.cls; its user manual says "Journal article LaTeX authoring template") is Springer Nature's journal template, not the proceedings template the CFP asks for (LNICST Authors' Kit, linked to Springer's LNCS proceedings guidelines). The CFP's own kit (`Springer_Latex_Template.zip`, downloaded by Hoàng 18 Oct) is the LNCS package with llncs.cls v2.20 (2018); the paper uses Springer's current llncs.cls v2.25 (2026), the same class. A test build with each version gives identical text on all 19 pages (conclusion ends on page 15), so the paper keeps v2.25.

## Float placement (18 Oct 2026, after Hoàng's Overleaf check)
- Tables 1 and 2 were defined before their section heading, so Table 1 appeared inside §2 and Table 2 before §4. Both definitions now follow the first paragraph of §3.1 and §4.1. `flafter` (main.tex and main_test_lmodern.tex) keeps every float after the text that defines it, and `\clearpage` before Appendix B keeps the Appendix A floats out of B.
- Test build: body unchanged in length (conclusion ends on page 15); Tables 1–4 on pages 5, 9, 9, 12; Appendix A floats on pages 18–19; Appendix B on page 20 (20 pages in total, appendices excluded from the limit). No text changed.

## Camera-ready package (18 Oct 2026)
- `main.tex` header comment no longer says "draft"; the comment in `09_references.tex` records that the four added references were checked against Crossref (Holm: GESIS record and JSTOR URL). No text in the PDF changed.
- Package in `revision_round1/camera_ready/` (device: `RBL\FISAT_camera_ready_367005\`): `SUBMISSION_INFO.txt` (title, abstract, keywords, authors, corresponding author), `367005_camera_ready.pdf` (Overleaf build of 18 Oct), `367005_source.zip` (main.tex, llncs.cls, sections/, figures/, README.txt; no .bib/.bbl needed). The zip compiles with 0 errors; its text matches the Overleaf PDF.

## Corrections (19 Oct 2026)
- §5.2: "A different exemplar per project, drawn at random, move … and make it" corrected to "moves … makes it" (grammar only).
- §4.5: the p-value of Spearman's ρ for Sylius corrected from 0.006 to 0.005. `revision/results/b1_spearman.csv` gave p = 0.00547; 0.006 came from rounding the four-decimal value 0.0055 in `b1_report.txt` a second time. The same correction was made in the response letter. This value was later replaced by the recomputation in the next item.
- §4.5 and §6, leakage proxy recomputed. `revision/b1_leakage_proxy.py` tokenised the reference files without first turning their stored line breaks (the two characters backslash and n) into real ones, so the first word of every line was read with a leading "n" (for example "nfeature", "ngiven") and the reference trigrams were wrong. Every other script in the repository does this step (for example `scripts/compute_metrics.py`). After the fix, the three `b1_*` outputs were regenerated. Story–reference overlap: median 4.9% (was 4.1%); Sylius 8.3% (6.7%), Fineract 1.6% (1.5%), Diaspora 5.8% (5.2%). Spearman ρ with skeleton cosine: Sylius 0.29, p = 0.003 (0.28, p = 0.005); Diaspora 0.33, p = 0.009 (0.31, p = 0.015); Fineract 0.11, p = 0.30 (0.11, p = 0.26); pooled 0.43 (0.41). The conclusion is unchanged: overlap correlates with similarity in Sylius and Diaspora, not in Fineract. The response letter was updated with the same numbers. An's offline rerun (`revision/nt3_rerun/`, 19 Oct) ran the earlier version of this script, so its B1 logs show the earlier numbers.
- The PDF was rebuilt with pdflatex (TeX Live 2023, two runs, 0 errors; the only warning is amsmath's note that it cannot redefine \vec, which comes from the LNCS class). Its text differs from the 18 Oct Overleaf build only in these corrections; page count (20), embedded fonts and page size are the same. `367005_source.zip` was rebuilt with the corrected section files and compiles. The 18 Oct PDF is kept as `revision_round1/superseded_2026-10-19/367005_camera_ready_before_5.2_fix.pdf`, and the build of the morning of 19 Oct (before the B1 correction) as `revision_round1/superseded_2026-10-19/367005_camera_ready_before_b1_fix.pdf`, in the authors' working folder.
- Response letter, comment on the threshold sweep: "The project ranking is the same at every threshold" was not accurate (Fineract and Diaspora swap places at 0.83 in `revision/results/b3_threshold_sweep.csv`) and now reads "At every threshold Sylius has the largest share of files above it; Fineract has the smallest from 0.83 upwards, and Diaspora below that."
- A recount of 403 numbers in the paper against the data and the output files of the scripts (Vietnamese study notes, 19 Oct) found no other discrepancy among the numbers computed from this study's data (numbers cited from other papers were not rechecked). The recount checks that each number matches its output file; it did not find the B1 tokenising error, which was found afterwards by reading the scripts line by line.

## Publisher's camera-ready rules (22 Oct 2026)
- EAI's camera-ready instructions ask that the use of an LLM be documented in the Acknowledgements, the Introduction or the Preface. The paragraph on AI tools, formerly part of "Data, Tool, and Ethics Disclosure", is now the Acknowledgments in the `credits` environment of llncs.cls; its wording is unchanged except that its last clause ("all numbers were recomputed ...") is now a separate sentence. The rest of that section is split into "Data and Ethics" and "Disclosure of Interests", with the same wording (`sections/08_disclosure.tex`).
- Alt text for Fig. 1 and Fig. 2 added with the `\Description` command of llncs.cls v2.25 (`sections/10_appendix.tex`); the class writes it to `DescriptionTexts.txt` when the paper is compiled. Its numbers come from `revision/results/descriptives_skeleton_cosine.csv` (rows `no_exemplars_N258`) and `revision/results/h1_domain_table.csv`. The figures are plots of this study's data; no image was generated or edited with AI.
- The PDF is renamed `367005_Evaluating_GPT_5_4_mini_for_Gherkin_Test_Generation_An_Empirical_Study_Camera_Ready.pdf` and was rebuilt with pdflatex (TeX Live 2023, three runs, 0 errors): 20 pages, all fonts embedded, and its text differs from the 19 Oct build only in the back matter on pages 15–16.
- The archive for the publisher (`367005_camera_ready.zip`, in the authors' working folder) holds the PDF as well as the LaTeX source, as the instructions require; the earlier `367005_source.zip` held only the source.

## Final content check (22 Oct 2026)
Every number in the paper was recomputed from the released data and outputs or matched to its output file, the 15 references were checked against Crossref, arXiv or the publisher, and each claim about a cited work was checked against that work. No number computed from this study's data was wrong. The following were corrected:
- §1 and §2.1, Rathnayake et al.: "a proprietary BDD dataset" and "the private dataset limits independent replication" were wrong; that study released its dataset and code (its Sections 1 and 4.2.1 and reference [34]). The text now says it used 500 user stories from four proprietary products of one company and released the dataset.
- §1 and §2.1, Fernandes et al.: "public sample" and "used public material" were not supported; its test cases come from a single production system (its Section 4), and only the study's artifacts were released. The text now says so.
- §5.1 and §5.4: Ferreira et al. report the syntactic correctness of generated Cypress (TypeScript) code, not of Gherkin. The two sentences now attribute Gherkin syntax to Fonseca et al. and test-code syntax to Ferreira et al.
- §3.1: the scenario counts 2,554 and 1,913 come from the 244 parseable references and the 255 parseable generated files among the 258; the sentence now says so (numbers unchanged).
- §4.4: the five Diaspora disagreements concern three files (229 and 255 on both facets, 236 on the temporal/causal facet); "five are Diaspora files" now reads "five concern three Diaspora files".
- References: Karpurapu et al., pages 58715–58721 added; Ferreira et al., venue corrected from "Workshop" to "Conference on Automation of Software Test", pages 1–11 and DOI 10.1109/AST66626.2025.00007 added (replacing the arXiv id); Fonseca et al., pages 3311–3321 added; Fernandes et al., "Gorgonio" corrected to "Gorgônio".
- Fig. 1: the legend said "Prespecified threshold 0.85", which E7 had removed from the text; it now says "Threshold 0.85", as in Fig. 2. The figure was re-rendered with the same plotting script and data (`plot_verified_figures.py`, `results/full_per_row_metrics.csv`); only the legend label changed.
- PDF rebuilt (pdflatex, TeX Live 2023, three runs, 0 errors, 20 pages, all fonts embedded); the conclusion still ends on page 15.

## Action Tracker v1 (27–29 Oct 2026)

Changes for the second review round. Every new number comes from the file named in the row (paths relative to the repository root).

| ID | What the paper now contains | Where | Source |
|---|---|---|---|
| B1, H8 | Table 1 compares this study with [1]–[5] on data and openness, syntax oracle, semantic oracle, human defect labels, metric perturbation and exemplar variation, with a line per study on its focus, models and prompting, and main finding; one delta paragraph per contribution; background on correctness oracles, test evaluation, mutation-based validation, LLMs in requirements engineering and reporting guidelines (7 new references) | §1.1, §2.2, §2.3, References | the cited papers |
| H1, H10 | Fineract files with truncated story input versus the 15 without; rescoring against the 15,000-character prefix; task named reconstruction from reverse-engineered stories | §4.2, RQ1, Abstract, §7 | `revision/results/h1_truncation_*` |
| H2, H4, H11, M7, M11 | Same-time rerun of C0, C1, C2 and capped C0cap (28 Oct 2026); ablation from the rerun with the original runs alongside (Table 5); run-to-run variation on 60 files × 5 runs; failure policy of every run; C0cap result | §3.2, §3.3, §4.7, §4.8, §6, Fig. 1 | `revision/rerun/results/rerun_report.txt`, `rerun_per_job.csv`, `rerun_h11_per_file.csv` |
| H3, M8 | RQ1 describes the distribution around the 0.85 reference point; "threshold" replaced by "reference point"; Figs. 2 and 3 re-rendered with the legend "Reference point 0.85" (same data) | §1.2, §3.4, §3.7, §4.1, §4.3, Appendix A | `results/full_per_row_metrics.csv` |
| H5 | RQ1 renamed "Structural skeleton resemblance"; "semantic" replaced by "structural" for the metric | Abstract, §1–§5 | — |
| H6, H13 | Prompts verbatim (Listings 1 and 2), exemplar mapping (Table 6), SHA-256 of the 18 prompt files, run dates | Appendix A | `revision/prompts/` |
| H7 | Flowchart of the denominators (Fig. 1) | §3 | `sections/fig_flow.tex` |
| H9 | Exact sign test and bootstrap CI for the median as primary test; Wilcoxon as sensitivity analysis; skewness with CI | §3.7, §4.1, Table 3, Abstract, §7 | `revision/results/h9_*` |
| H12 | Kappa with 95% CI; consensus round on the 15 doubly labelled files (8 of 15 defective after consensus, 5 before); 25/60 reported as exploratory | §3.6, §4.4, §6, §7 | `revision/h12/results/h12_kappa_ci.txt`, `revision/audit/consensus_15/` |
| M1 | References for the model page, the Chat Completions API, the all-MiniLM-L6-v2 model card and the behave 1.3.3 release | §3.2, §3.4, §3.5, References | `revision/m1_tool_sources/` |
| M2 | "expert-written" replaced by "project-maintained" | Abstract, §1.2, §3.1, §6.2 | `data/raw/README.md` |
| M3 | The human-review advice is followed by its scope: exploratory, high-similarity, stratified sample | §7 | — |
| M4, M5, M12 | Abstract shortened to 192 words with δ for RQ1; roadmap paragraph; main-contribution sentence | Abstract, §1, §7 | — |
| M6 | Dataset sources (Table 2) and the three source repositories as references | §3.1, References | `revision/m6_sources/` |
| M9 | Effect sizes reported without categorical labels, with 95% CIs for δ, η²H and ρ | §3.7, §4.1, §4.2, §4.5 | `revision/results/m9_effect_size_ci.txt` |
| M10 | RQ2 risk difference +18.84 percentage points [16.64, 19.76]; interpretive sentences moved to §5 | §3.7, §4.6, §5 | `revision/results/m10_rq2_risk_difference.txt` |
| M13, M14 | Sentences flagged in Appendix A of the tracker (kappa per facet in the Abstract; requested model name in §3.2; "pinned model identifier" in §1.2) | Abstract, §1.2, §3.2 | — |

Final check (29 Oct 2026): all tables, figures, listings and Appendix B were recomputed from the files above; the references were checked against Crossref, arXiv, ACL Anthology or the publisher. Corrections from that check: the exemplar sentences in §2.3 and the Abstract now follow the rerun; kang2023libro pages 2312–2323, fakhoury2024ticoder issue 9, the author order of foster2025ach as in the ACM version, and "accepted manuscript" removed from baltes2026guidelines. Fig. 1 had a TikZ key error that produced 17 LaTeX errors; it is fixed, and the figure is redrawn so that every arrow is straight and no two arrows cross (same boxes and counts; the exclusion of the C0 and C2 exemplars is now stated in the ablation box). Appendix tables and figures are now placed in reading order. The appendix tables, listings and hash list now share one type size (9 pt), and Figs. 2 and 3 are redrawn from the same data in the paper's font at their printed size by `paper_revised/figures/make_figures.py`.

## Page limit (29 Oct 2026)

On Hoàng's decision (17 Oct), the body must end within page 15. After the Action Tracker v1 changes it ended on page 22. The body now ends on the last line of page 15 (Abstract to Disclosure of Interests); references start on page 16, and the PDF has 29 pages. No number was dropped from the paper: every number in the earlier source is still in the paper, in the body or in the new Appendix C. Only one sentence was changed in content (last item below). Build: pdflatex, three runs, 0 errors, no overfull boxes, no undefined references.

- New Appendix C, "Further Method and Result Details" (`\label{app:more}`). It holds, moved from the body with the same wording or with only the sentence joined to its neighbours:
  - the comparison with [1]–[5] (now Table 8) and the data-flow figure (now Fig. 3);
  - from §3: the unit of analysis, the full "Sources and selection" paragraph, the details of the sign test and of the ONNX encoder, the computations of the rerun plan, the full failure policy with cost and model-name logging, the two defect facets and the four keyword-order flags;
  - from §4: the RQ1 descriptive table (now Table 9), the IQR asymmetry, the full truncated-story paragraph, the AUC and the defect counts per cosine range, the example of file 76, the defect types, the course of the consensus round, the three C0 parser failures, the output lengths of the ablation, the original-run half of the ablation table (now Table 10), the ICC intervals, the comparison of the new with the original C0, and the variance components;
  - from §6: the C0cap results and one paragraph with the details of the threats.
- Removed: §3.8 (its sentence "no generated file was excluded because of its content" is now in §3.2; the replication URL is in Data and Ethics) and §4.9 (the same summary is in §7).
- Shortened without dropping a number: §1 (the two opening paragraphs merged; the research gap refers to §2 instead of restating [1]–[4]), §2.1–§2.3 (all citations kept), §5 (§5.4 merged into §5.1–§5.2), §6 (every threat keeps its mitigation and residual risk; three pairs of threats merged; "Uncontrolled limitations" unchanged) and §7 (the main-contribution sentence is still the second one, and the scope sentence still follows the advice).
- Float numbers changed: Table 1 is now the dataset table (was Table 2), Table 2 the per-project table (was 4), Table 3 the ablation (was 5), and in the appendices Table 4 (was 6), Table 5 (was 7), Tables 6–7 (were 8–9), Figs. 1–2 (were 2–3), Table 8 (was 1), Fig. 3 (was 1), Table 9 (was 3) and Table 10 (new, split from 5). Tables 8 and 9 are top floats (`[!t]`), because with `[H]` they left about a third of a page empty; every float is on the page of the sentence that introduces it or on the next page.
- Appendix C, details of the threats: "the C0 of the same-time rerun has the same median as the original C0" now reads "almost the same median ... (0.852 against 0.853)", the medians of Table 3 and Table 10.

## Paper text without revision history (29 Oct 2026)

On the mentor's comment that the paper must be rewritten with the revised content rather than marked up, the body now reads as one final text. No result, number or claim was changed; only the wording that told the reader what had changed since the submitted version. Build: pdflatex, three runs, 0 errors, no overfull boxes, no undefined references. The body still ends on page 15; the PDF has 28 pages.

- Removed the six "(added in revision)" labels (the run-in headings "Sources and selection", "Prompt ablation", "Same-time rerun" and "Truncated story input", and the headings of §3.6 and §4.8) and renamed "Analyses added in revision" to "Exploratory analyses"; its first sentence still states that these analyses were planned after the reviews and are exploratory.
- Removed the pointers to Appendices B and C that only said "details are in the appendix"; pointers to a table, figure or listing in the appendices are kept (34 → 15 pointers in §1–§8). The appendices are unchanged.
- Rewrote the sentences that described the revision itself:
  - §1: "this revised version adds a leakage measurement, ..." → "this study therefore includes a leakage measurement, ...";
  - §1, §2.3, Data and Ethics: "revision analyses" → "additional analyses";
  - §3.5: the sentence on the dry-run check of the submitted version now gives only the reason the dry run is not used (it stops with a configuration error before parsing the file);
  - §3.7: "Following review, the median is therefore tested" → "The median is therefore tested" (the deviation from the proposal's Wilcoxon test is still stated);
  - §4.6 and §7: the sentences saying that 98.84% corrects the 100% of the submitted version were removed (the correction is recorded in table row E1 above);
  - §6.2: "the faulty dry-run check was replaced by behave's parser" → "validity is checked with behave's parser rather than a dry run".
- To keep the body within page 15 after defining the two defect facets in §3.6, three sentences were shortened (the ONNX sentence in §3.2, one discussion sentence in §5 and the exploratory-analysis sentence in §6) without dropping a number.
- The Acknowledgments still state that an AI coding assistant drafted the audit labels in the revision; this is the required AI disclosure, not revision history.

## Paper without appendices (29 Oct 2026)

On the mentor's instruction, the paper ends with the references and has no appendices. The former Appendices A–C are now a separate document, the supplementary material (`supplementary.tex`, PDF in this folder), with the same text, tables and figures. Its sections are numbered S1–S3 (were A–C), its tables S1–S7 (were Tables 4–10), its figures S1–S3 (were Figs. 1–3) and its listings S1–S2 (were Listings 1–2); numbers without the prefix S refer to the paper, and it repeats the paper's reference list so that citation numbers are the same.

- The paper now has 18 pages: the body still ends on the last line of page 15 and the references fill pages 16–18. Build: pdflatex, three runs, 0 errors, no overfull boxes, no undefined references; the supplementary material has 14 pages and builds with the same result.
- In the body, the pointers to an appendix table, figure or listing now name the supplementary item (for example "Table S5 of the supplementary material" for the comparison with [1]–[5]); the roadmap sentence in §1 names Sections S1–S3 and refers to Data and Ethics, which gives the direct link to the supplementary PDF in this folder of the repository.
- `\appendix` was removed from `sections/10_appendix.tex`; its references to the paper's sections and tables are read from `main.aux` with the `xr-hyper` package (prefix `P-`).
- No number was dropped: the numbers in the body and the supplementary material together are the same as in the previous version.
