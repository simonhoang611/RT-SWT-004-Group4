# Independence declaration and agreement results, 15 B2/H3 cards (16 Oct 2026)

English translation (19 Oct 2026, prepared with an AI assistant, Claude) of the Vietnamese original `KHAI_BAO_VA_KAPPA.md` (SHA-256 f960cc4a95bd4ccd…), which the authors keep unchanged.

## 1. Hoàng's declaration

Recorded from Hoàng's replies in the thread on 16 Oct 2026, 08:15 and 08:28 UTC.

1. Hoàng **did not open** the folder `FISAT_gui_Hoang_2026-10-15` (authors' working package, not in this repository; the package with the AI labels confirmed by An) until Hoàng had finished rating both the B2 sheet and the H3 sheet.
2. Hoàng **had not read** the summary figures of the AI labels (25/60; by domain 6/16/3) in the 15 Oct review file before rating.
3. An **did not tell** Hoàng the result for any id among the 15 cards.
4. Hoàng rated on 15 Oct and 16 Oct 2026.

After the sheets had been saved, Hoàng changed one cell at Claude's request. This cell was a missing entry, not a label change:
- Card 224: `rule_flag_confirmed` changed from N/A to Y (the card has the flag `OP_MISSING`).
- At the time of this change, Hoàng had still not seen any AI label.

Card 236 (H3) keeps `PRE_missing = 2` and `n_AC_with_precondition = 0`. The reason is in `note`: no AC states an initial state, but the scenarios need Bob's posts in order to run, and the Background creates no post. This is Hoàng's interpretation of the `PRE_missing` column and needs to be discussed (section 4).

What Claude knows and records in addition:
- The three AI labels that the 15 Oct review says were "read" were read by Claude. They are ids 24, 34 and 43, which are not among the 15 cards.
- The files Claude gave Hoàng during the rating contain no label or conclusion for any card: the rating rules, the AC map, the per-AC reading file for Fineract, and the Fineract glossary.
- Claude only gave comments on the rules and made no comment on the conclusion for any card.
- Claude has no way to verify whether Hoàng opened a file or not. Section 1 is Hoàng's own statement.

## 2. Locked files (SHA-256)

[Translator's note: the hashes below are of the files as locked on 16 Oct 2026, whose free-text columns are in Vietnamese. They are kept unchanged in the authors' archive. The files in this repository have the same labels, counts and severities but English free text, so their hashes differ; `revision/TRANSLATION_LOG.md` maps each original hash to the English file's hash.]

| File | SHA-256 |
|---|---|
| `b2_annotation_Hoang_ORIGINAL.csv` (after the correction to the cell of card 224, 16 Oct 08:13 UTC) | `9cd9d14a71ccaecedb2ea2c28c9afacfac12603f00589fbd5c1cbe5e79458fe7` |
| `b2_annotation_Hoang.csv` before the correction to card 224 (recorded for comparison) | `02f32067d8121fe5e0de5dc9528554fe9305720cc7bbd6dba26fbd61a6a0b983` |
| `h3_annotation_Hoang_ORIGINAL.csv` (16 Oct 07:28 UTC) | `817274f73de08fa94eebbdfde5f8678cc689d101ebddc672dc0550aae60153f4` |
| `b2_annotation_Hoang_CLEAN.csv` | `99a7dc39046b0879111d5e334139052ce66723d2bc403c1ebd8a6333f4f32733` |
| `h3_annotation_Hoang_CLEAN.csv` | `2a319e70d0053e9cb3856fd2a58430106853f30ffa584f6cb7b72c20cbf45117` |
| `b2_annotation_An_CONFIRMED.csv` (comparison side) | `7f6780dd4eb7e617715355ef50f503c7e59c3f8a427bd71c8379493c49103b28` |
| `h3_annotation_An_CONFIRMED.csv` (comparison side) | `a76c6fc5e2322e804f5e138f6b721eb35ab3d76d79f5f74537ccd271c3b472d5` |

The CLEAN versions were created with `make_clean.py` and only change the formatting. All 63 changes are recorded in `clean_changes.csv`:
- `N/A` changed to `NA`.
- `n_AC_with_precondition` in the form "3 (AC1, AC2…)" changed to the number 3, with the list of ACs moved to `note`.

The script has been checked again: no label, defect count or severity was changed.

## 3. Results

Hoàng's labels were compared with `*_An_CONFIRMED.csv`. The comparison side is **labels drafted by Codex (AI), which An reviewed and kept entirely unchanged**, not labels rated independently by a person. So the results below are **the agreement between one independent rater and human-reviewed AI labels**, not a kappa between two independent raters.

Computed with `summarize_annotations.py` in An's package, then computed again with a separate piece of code: both ways give the same results.

| Label | n | AI/An: Y | Hoàng: Y | Agreement | Cohen's κ | Ids with disagreement |
|---|---|---|---|---|---|---|
| B2 `has_business_defect` | 15 | 5 | 6 | 12/15 (80%) | **0.571** | 98, 229, 255 |
| H3 `has_temporal_causal_defect` | 15 | 5 | 8 | 12/15 (80%) | **0.609** | 229, 236, 255 |

Details of the ids with disagreement:
- **B2:**
  - 98 (E-commerce): AI/An = Y, Hoàng = N.
  - 229 and 255 (Social Network): AI/An = N, Hoàng = Y.
- **H3:**
  - 229, 236 and 255 (Social Network): AI/An = N, Hoàng = Y.

By domain:
- **Fineract:** agreement on all 3/3 cards for both labels.
- **Social Network:** AI/An marked 0/6 cards as having defects; Hoàng marked 2/6 (B2) and 3/6 (H3).

**Both κ values are below the RBL-4 threshold of 0.7.** With n = 15, κ has a very wide confidence interval: a single id changing its label is enough to change κ a lot.

## 4. Next steps under RBL-4 (κ < 0.7)

1. Hoàng and An meet about the 4 ids **98, 229, 236, 255**. Each side gives its reasons based on the rules; then the two sides agree on one label and record the reason in the log.
2. Write down clearly the points where the rules are still ambiguous that have come to light. At least:
   - Does `PRE_missing` count preconditions that the scenario needs but the AC does not state (card 236)?
   - The convention "if the AC only states a state, it counts as checked if that state is in Given/Background".
3. If the rules are clarified, apply the clarified rules again to all 60 cards, not only the 4 ids. Record which cards change label.
4. In the paper: report the κ values **before discussion** (0.571 and 0.609) exactly as above, describe the comparison side correctly as human-reviewed AI labels, then state how the disagreements were handled. Do not replace κ with a value computed after discussion.

## 5. Hoàng's decision (16 Oct 2026, 08:33 UTC)

Hoàng chose **"Report as a limitation"**: no meeting, no re-rating, all labels kept unchanged, and the κ below the threshold reported as a limitation of the study.

Because RBL-4 requires a meeting and re-rating when κ < 0.7, this approach **deviates from the procedure set in advance**. This deviation must be declared in the paper and in the response letter.

English draft for the Threats section, for Hoàng to integrate and edit the wording:

> To gauge annotation reliability, one author (Hoàng), who had not seen the existing labels or their aggregate rates, independently labelled a fixed subset of 15 of the 60 files. We compared these labels with the AI-drafted labels that a second author had reviewed and retained unchanged. This is agreement between an independent human rater and AI-assisted, human-reviewed labels, not agreement between two independent human raters. Cohen's κ was 0.571 for business-logic defects and 0.609 for temporal/causal defects (12/15 agreement for each). Both values are below the 0.7 threshold set in our protocol. Disagreements concentrated in the social-networking domain, where the independent rater flagged defects in files the reviewed labels marked as defect-free. Contrary to the protocol, we did not run a consensus round or relabel. All labels are reported unchanged, and the defect rates should be read as indicative only. With n = 15, κ is imprecise.
