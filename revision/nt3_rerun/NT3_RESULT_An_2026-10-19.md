# NT3: results of An's own RUN CHECKS run (19 Oct 2026)

English translation (19 Oct 2026, prepared with an AI assistant, Claude) of the Vietnamese original `NT3_KET_QUA_An_2026-10-19.md` (SHA-256 f4749a7076761c63…), which the authors keep unchanged.

Source: An's run output, which in this repository is in `revision/nt3_rerun/An_run_20261019_011815/`, with `KET_QUA.json` and `execution_logs/` (names unchanged, as produced by the script; "KET_QUA" is Vietnamese for "results") [original copy: `RBL\KET_QUA_TU_CHAY_20261019_011815\20261019_011815\`, sent by An to Hoàng].

- `KET_QUA.json`:
  - executed_by "Nguyen Hieu An", run at 2026-10-19 01:18 (+07:00).
  - Windows 11 computer, Python 3.12.14.
  - Libraries: pandas 3.0.5, numpy 2.5.3, scipy 1.18.1, behave 1.3.3.
- 10/10 steps have exit 0. `all_15_tables_match: true`.
- Claude independently compared An's 15 tables again with `original/` in the package `FISAT_RUN_CHECKS_An_2026-10-18.zip`: 15/15 match. The largest numerical difference is 2.8×10⁻¹⁶, which is only rounding error.
- The log of step 02 has the line "ConfigError: No steps directory". This is as expected, not an error: this script deliberately reruns the old `--dry-run` check to illustrate error E1.
- Effect on the paper and the letter: no number changes; nothing needs to be corrected.
- Note added 19 Oct 2026, after this run: the B1 script that An's package ran (`b1_leakage_proxy.py`) was later found not to unescape the line breaks of the reference files, and was corrected. The rerun confirms that the earlier B1 tables were reproducible; it does not cover the corrected B1 numbers now in §4.5. See `paper_revised/CHANGES_rev.md`, Corrections.

NT3 status: An has run it personally on An's own computer. The part where An reads the logs personally and confirms personally still rests on An's confirmation (step 6 in `GUIDE.md` [was `HUONG_DAN.md`]).
