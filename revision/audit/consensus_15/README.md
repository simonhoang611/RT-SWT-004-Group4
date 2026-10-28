# H12: consensus on the 15 doubly labelled audit files

The 15 audit files labelled by both the reviewing author (An) and the independent rater
(Hoang) were discussed in the consensus round of the audit protocol on 28–29 October 2026.
Each of the 30 file-facet decisions (15 files x business_logic, temporal_causal) has a final
label, severity, reason and line evidence.

| File | Content |
|---|---|
| `consensus_15_files.csv` | the 30 decisions: labels before consensus, `final_label` (Y/N), `final_severity` (0-3), `reason`, `evidence_lines`, `decided_on` |
| `CONSENSUS_RECORD_2026-10-29.md` | meeting record: date, participants, outcome, changed decisions, counts, confirmations |
| `cards/case_<id>.md` | one card per file: user story, reference and generated file with numbered lines (US, GT, GEN) and the original notes of both raters, quoted unchanged |
| `INITIAL_LABEL_EVIDENCE.json` | labels and notes before consensus, with the SHA-256 of the source files they were transcribed from |
| `validate_consensus.py` | checks the entered decisions and prints the counts; it does not decide labels |

Check from the repository root:

    python revision/audit/consensus_15/validate_consensus.py --final

Expected result: `PASS`, 30 of 30 rows resolved; 6 of 15 files defective on the
business-logic facet, 8 of 15 on the temporal/causal facet, 8 of 15 on either facet
(5, 5 and 5 before consensus).

The labels before consensus are unchanged in `../02_B2_semantic_defects/`,
`../03_H3_temporal_causal/` and `../independent_rater_15/`, and so is the kappa computed from
them (0.571 and 0.609). Kappa is not recomputed after adjudication. The other 45 audit files
were not relabelled, so the 60-file audit remains exploratory.
