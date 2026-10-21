# Addendum to `DECLARATION_AND_KAPPA.md` (was `frozen_2026-10-16/KHAI_BAO_VA_KAPPA.md`) (18 Oct 2026)

English translation (19 Oct 2026, prepared with an AI assistant, Claude) of the Vietnamese original `KHAI_BAO_BO_SUNG_2026-10-18.md` (SHA-256 5f2a902c49bf3882…), which the authors keep unchanged.

The original declaration file and the locked sheets are kept unchanged; their hashes do not change. This file only adds one missing point that An (together with Codex) pointed out on 18 Oct.

**Section 2 of the original declaration did not list all the operations of `make_clean.py`.** Besides changing `N/A` to `NA` and separating out the number in `n_AC_with_precondition`, the script has a third rule. The script's docstring states this rule, but section 2 left it out:
- In rows without a defect, the text in the evidence columns (`evidence_gen_line` and `evidence_US_or_GT_line` for B2, `counterexample_quote` for H3) is moved to `note` with the prefix "REFERENCE LINE (no defect)", and those columns are then set to `NA`. [Translator's note: the Vietnamese original of `make_clean.py` writes this prefix as "DÒNG THAM CHIẾU (không lỗi)"; the English version in this repository writes "REFERENCE LINE (no defect)". On these 15 cards the rule changed no row in either version, because every evidence cell in a no-defect row was `N/A`: neither CLEAN file contains the prefix, and the 13 `note` changes all come from the `n_AC_with_precondition` rule.]

Number of changes per column in `clean_changes.csv` (63 in total): `note` 13, `n_AC_with_precondition` 13, `rule_flag_confirmed` 12, `evidence_gen_line` 9, `evidence_US_or_GT_line` 9, `counterexample_quote` 7.

On 18 Oct, Claude checked the following points again:
- Rerunning `make_clean.py` on copies of the two ORIGINAL files gives two CLEAN files and a `clean_changes.csv` that are identical byte for byte (hashes `99a7dc39…`, `2a319e70…`, `68dbd6a2…`). [Translator's note: these hashes are of the Vietnamese-text files kept unchanged in the authors' archive. The English files in this repository have different hashes, listed in `revision/TRANSLATION_LOG.md`.]
- Changing the `rule_flag_confirmed` cell of card 224 back from Y to N/A gives exactly the declared hash from before the correction (`02f32067…`).
- No label, defect-count or severity column was changed.
