# paper_revised/: revised paper (FISAT 2026, paper 367005)

Camera-ready version of "Evaluating GPT-5.4-mini for Gherkin Test Generation: An Empirical Study",
revised after the reviews. The version submitted for review is in `paper/` (git tag `v1-submitted`).

| Path | Content |
|---|---|
| `367005_Evaluating_GPT_5_4_mini_for_Gherkin_Test_Generation_An_Empirical_Study_Camera_Ready.pdf` | PDF compiled with pdflatex from the source in this folder |
| `main.tex`, `sections/`, `figures/`, `llncs.cls` | LaTeX source (Springer LNCS class v2.25) |
| `CHANGES_rev.md` | every change made in the revision, with the source of each new number |

Compile with `pdflatex main.tex` (twice). The reference list is written directly in
`sections/09_references.tex`, so no BibTeX run is needed. Supporting material is in
Appendices A–C (`sections/10_appendix.tex`).

The analyses behind the revised numbers are in `../revision/` (see `../revision/README.md`), and the
response letter to the reviewers is `../revision/response_letter/Response_to_Reviewers_367005.md`.
