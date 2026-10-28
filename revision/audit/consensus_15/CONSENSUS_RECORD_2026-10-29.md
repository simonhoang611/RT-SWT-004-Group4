# Consensus meeting record — 2026-10-29

Status: HELD; decisions entered in consensus_15_files.csv; confirmations below
Date/time and timezone: Start at 2026-10-28, UTC+7 (exact time: 11:30 PM)
Participants: Nguyen Minh Hoang (independent rater), Nguyen Hieu An (reviewing author)
Mode: video call
Tools used during the meeting, if any: none for the decisions. After the meeting,
a transcription script filled evidence_lines: for rows labelled Y, the card line
numbers of the evidence quoted in Hoang's original rating files
(b2/h3_annotation_Hoang_CLEAN.csv, two blocks corrected by hand); for rows labelled
N, the acceptance-criteria lines and the whole generated file. It also converted
the dates to ISO format. Hoang wrote or approved every reason and chose every
final label and severity; no tool decided a label.

Review all 15 files, both facets (30 rows). Original labels are preserved. Each
row of consensus_15_files.csv records the final Y/N label, severity 0-3, reason,
numbered evidence (US/GEN/GT line numbers of the case card) and the date.

Outcome: both raters agreed to adopt the independent rater's label in every row.
The 24 rows that were already agreed keep the shared label; the 6 disagreements
take the independent rater's label.

Pre-consensus kappa: business logic 0.5714285714; temporal/causal 0.6086956522.
Kappa is not recomputed after adjudication.

Files with a decision changed from An's prior labels (4 files, 6 rows):
- 98 (E-commerce) business_logic: Y -> N
- 229 (Social Network) business_logic and temporal_causal: N -> Y
- 236 (Social Network) temporal_causal: N -> Y
- 255 (Social Network) business_logic and temporal_causal: N -> Y

Facet/union defect counts and rates among the 15 files (validate_consensus.py --final):
- business_logic: 6/15 (40.0%), before consensus 5/15
- temporal_causal: 8/15 (53.3%), before consensus 5/15
- union (either facet): 8/15 (53.3%), before consensus 5/15
Unresolved cases: none (30/30 resolved).

The other 45 audit files were not relabelled; no rater who had not seen their
labels was available. The 60-file audit remains exploratory.

Nguyen Hieu An confirmation: Nguyen Hieu An
Nguyen Minh Hoang confirmation: Nguyen Minh Hoang
