# Translation log (19 Oct 2026)

The study was carried out in Vietnamese. Before the revision was committed, every document, script
comment, script message and free-text annotation in the files below was translated into English with an
AI assistant (Claude). This log records how, so that the authors and readers can check the translation
against the originals. The Vietnamese originals are kept unchanged in the
authors' archive; their SHA-256 hashes are listed so that each English file can be matched to the file
that was actually used.

## Rules that were followed

- **Scripts.** Only comments, docstrings and printed messages were translated. Each Python file was checked
  with an AST comparison (comments and docstrings removed, string literals blanked): the code is identical,
  except in scripts that moved into `revision/audit/`, where only the lines that locate the repository root
  and the data folder changed. The PowerShell script was compared line by line: only messages and comments
  changed. Prompt strings sent to the model were not changed.
- **Annotation files.** Only free-text columns (notes, evidence descriptions written in Vietnamese) were
  translated. Ids, labels (Y/N), defect counts, severities and coverage counts are identical to the
  originals. Gherkin text quoted in evidence columns is unchanged; only the Vietnamese words around it were
  translated. In Hoàng's H3 sheet, six `n_AC_with_precondition` cells have the form "3 (AC1, AC2 and AC3)"; only the
  connecting words in the bracketed list were translated, and the number is unchanged. The decision value `GIU`
  ("keep") was written as `KEEP`; no script reads that column.
- **Verbatim quotes.** Where a file records someone's words verbatim (An's confirmation), the English
  text is stored under a key ending in `_english_translation`, with a `translation_note`; the original
  wording is in the original file.
- **Documents.** Each translated document starts with a line naming its Vietnamese original and the first
  16 hex digits of its SHA-256.
- **Outputs.** Outputs whose text comes from a translated script or file were regenerated with the English
  version. On 19 Oct 2026 all 19 result tables and the five text reports computed from the English files
  equalled those computed from the originals (same numbers; κ = 4/7 and 14/23; 25/60).

## What was checked by the NT3 rerun

An's independent rerun (`revision/nt3_rerun/`, 19 Oct 2026) verified the files listed in
`revision/nt3_rerun/MANIFEST_SHA256.txt`. Those hashes are of the Vietnamese-comment versions. Four files
in this repository are English versions of files in that manifest: `revision/README.md`,
`revision/check_syntax.py`, `revision/h2/H2_RUN_GUIDE.md` and
`revision/audit/02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv`. Their original hashes in the table
below are the hashes in the manifest. The names `ket_qua` and `KET_QUA.json` ("results") are kept because
`RUN_CHECKS.ps1` and `run_checks.py` write them and An's run record uses them.

## Hashes recorded inside other files

- `revision/audit/06_mutation_test_SBERT/model_run_metadata.json`, field `original_script_sha256`
  (`089a37b0cab412d7…`): the Vietnamese-comment `mutation_sbert_test.py` that was run. The English file is
  listed below.
- `revision/audit/independent_rater_15/DECLARATION_AND_KAPPA.md` §2 and the addendum: hashes of the locked
  Vietnamese-text sheets (for example `b2_annotation_An_CONFIRMED.csv` = `7f6780dd…`). They are kept as
  written, with a translator's note; the English hashes are below.
- `revision/audit/confirmation/An_confirmation_2026-10-15.json`, `translation_note`: original hash
  `35ba7cfa5e878fb8…`.

## Translations the authors should double-check

- Card 141 (Codex note, B2 and H3): a Vietnamese phrase was translated as "the earlier payment of 100"; it
  may instead mean a prepayment or down payment of 100.
- Card 229 (Hoàng's H3 note): the source word reads "if", which was taken as a typo for the near-identical
  word "state" and translated "state the initial state".
- Card 210 (Codex note): "after closing, a sign-in attempt is rejected"; the source does not name what is
  closed.
- An's answer, "Reviewed all 60 cases, keep everything unchanged": the Vietnamese has no tense marker on
  "keep"; it answers the question "do you agree to keep all labels … unchanged".

## Files

Files not listed here were copied unchanged. Course material committed before the revision (team folders,
`paper/`, presentation) is left in its original language as a record of the course project.

For files that were already tracked at commit 48082cd, the original SHA-256 is that of the authors' Windows
working copy (CRLF line endings), which is not the same byte sequence as the blob stored in git. The English
versions of these files use LF line endings, as the files in git did before (line endings changed on 21 Oct
2026; the text is unchanged). Files under `revision/` and `paper_revised/` are stored byte for byte
(see `.gitattributes`), so their SHA-256 values can be checked directly.

| File in this repository | Original (where kept) | Original SHA-256 | English SHA-256 | Change |
|---|---|---|---|---|
| `.gitignore` | `.gitignore` (HEAD 48082cd) | `f4668d48f2a9abadae19c98e636a99cc1c4f6c4a3f72d10c6564a2345110e757` | `eabe5f0bd02b2466850bfa72a6b2a0a5b6d166a6e482b40a4df2538f6a65ae7c` | one comment translated |
| `README.md` | `README.md` (HEAD 48082cd) | `ac07199108107375a0f49e8856b8914daf1eef57b194fc3a07afd8a7b2edc986` | `4a68b93b2d69858b7371d4458bc1fcb9f45590e4a4370295f29fcbeeb2b58c23` | document translated |
| `data/raw/README.md` | `data/raw/README.md` (HEAD 48082cd) | `6025baadde63fca6ff67f11b7d5643c78a9fc25443ed78e402853ff9dc0aec69` | `bc7f22e504d7ae9c680897467c79963c2b73583e368d867a35ff44aa8b0f3eb5` | document translated |
| `scripts/compute_metrics.py` | `scripts/compute_metrics.py` (HEAD 48082cd) | `421810288283420c521a3ca833272a9264d2903cacddafd1a9f080b7744d11f5` | `ba18af8042ac333ca5d1502ef49444127a60090282ee654f8243f8b985cdfbce` | comments, docstrings and messages translated; code AST-identical |
| `scripts/local_reverse_engineer_us.py` | `scripts/local_reverse_engineer_us.py` (HEAD 48082cd) | `de7507aa45dfa3a2133168d3e7080ad810c682d32e60cab049da5c68c0ecb37a` | `50dd7aac573a0384eba29935aae99762ca8693bbf4e7ebb2efd4c5bebfb64b92` | comments, docstrings and messages translated; code AST-identical; prompt strings unchanged |
| `scripts/run_experiment.ipynb` | `scripts/run_experiment.ipynb` (HEAD 48082cd) | `11465f155b43d1f6002a73877aea088b82e883d0d8a972a933a06f2aeb4578eb` | `f139daf1d9a725a900013f5e096b0b6354c6211e384676cdfe7f3c4210450dbb` | markdown cells and code comments translated; code and prompts unchanged |
| `scripts/run_pilot_experiment.ipynb` | `scripts/run_pilot_experiment.ipynb` (HEAD 48082cd) | `6e4a3630dfd275e7129b0b7b2cb3c44e3f15d3b8e87378876667889ee0d76764` | `7fe4d8a0c7b79c6a83a6f561f574635d0f2ac6e531addab3aec3c2aef6856ed1` | markdown cells and code comments translated; code and prompts unchanged |
| `revision/README.md` | `revision/README.md` (working copy) | `cbaa70a38fe87f0ae102e4e01c8ea4556045b51c06f758834b5c97eacaa7bc69` | `4ce1a89672f3a04a6bc7fa008a709a97009e15174f043cf23c4e5671ab13c365` | rewritten in English and extended (audit, NT3 rerun, response letter) |
| `revision/RESULTS_B3_H1_B1_2026-10-16.md` | `revision/KET_QUA_B3_H1_B1_2026-10-16.md` (working copy) | `f094cb422a99ffca1388ea0f9182f53447c0da1bfc48f151532623cfb0974a29` | `68b5e1f09cbfcc50f8cb8053ac2910accff80da98443d22af6e4e6b56e9b2b39` | document translated; renamed; B1 table updated to the corrected script on 19 Oct |
| `revision/check_syntax.py` | `revision/check_syntax.py` (working copy) | `77cd9e8af7c1eb647c710e73c9f674e6bf396cdda79cf9c53fd72dd0d5441f06` | `4f428de5a4e9059ab4e8154b34c1486660c3456b8626efdd580977eb1d7f91af` | comments, docstrings and messages translated; code AST-identical; usage line in the docstring corrected |
| `revision/h2/H2_RUN_GUIDE.md` | `revision/h2/HUONG_DAN_CHAY_H2.md` (working copy) | `69139c9ba367593ef60fbec86beebe11d8d5659cd512b2db2effbf3e71c09ccc` | `bc46adbd8471f3583cac5dcbbd5d766a9afb7aac54fd77b4473d2e0fefd03aad` | document translated; renamed |
| `revision/response_letter/Response_to_Reviewers_367005.md` | `revision/THU_PHAN_HOI_draft.md` (working copy) | `8fa4525a023cca50d2bd27d208434cf8dc61d5539d5ba9586c07e20fb8ae1d03` | `9423311c89a836ca196152b2787f7d493e560223ec62fde68e18e0eef4053626` | final English letter replaces the working draft (see paper_revised/CHANGES_rev.md, 19 Oct) and the B1 numbers of 19 Oct |
| `revision/nt3_rerun/RUN_CHECKS.ps1` | `RUN_CHECKS_AN.ps1` (package FISAT_RUN_CHECKS_An_2026-10-18) | `50e93741a89edc4687c83e50d93e8659ab4d15e14c73f894b6a83fca6bf95ec1` | `39f639a9bbf29902ca97f9fe21278cfaff93b462f7d87b4378b9cbb0bcd5b87e` | comments, docstrings and messages translated; code AST-identical; renamed |
| `revision/nt3_rerun/GUIDE.md` | `HUONG_DAN.md` (package FISAT_RUN_CHECKS_An_2026-10-18) | `1bb13b9ad497037c10b52fa7230d84ca62680a2518303bd113f1b230692ed062` | `84e737adb72473ea5f64e460ffc211882ca7407b17a552d6dc033c5b43bc6b96` | document translated; renamed; note on the corrected B1 script added 19 Oct |
| `revision/nt3_rerun/NT3_RESULT_An_2026-10-19.md` | `revision/NT3_KET_QUA_An_2026-10-19.md` (working copy) | `f4749a7076761c631bc1a71bdd1cb29c78f7c33ad64c955e05329cb9b3af16b7` | `a63b8655865de8b3292d034963ce6a422cd287151f4c0b43df7dce8e00179f37` | document translated; renamed; note on the corrected B1 script added 19 Oct |
| `revision/audit/02_B2_semantic_defects/b2_rule_check.py` | `02_B2_semantic_defects/b2_rule_check.py` (package FISAT_gui_Hoang_2026-10-15) | `5c091520986901a0560bd14aa595d4df1733994d17b0aa40b1a8aae95c230ef9` | `7bc88db805680e442fa9b5cf8bd7049859843347aa588e9f1714f6c06466b8ea` | comments, docstrings and messages translated; code AST-identical except the lines that locate the repository root and data folders (the script moved to a new folder) |
| `revision/audit/02_B2_semantic_defects/b2_make_review_pack.py` | `02_B2_semantic_defects/b2_make_review_pack.py` (package FISAT_gui_Hoang_2026-10-15) | `40b6ab54950fe67a8cb3a68c736ab521fb751cbe971e15ddb0c0b3aa5db60dcb` | `a7fc2b350ac130a6842aae9e0ebd4f1853aa568d3f5f1ef8fd5ca8473beb424d` | comments, docstrings and messages translated; code AST-identical except the lines that locate the repository root and data folders (the script moved to a new folder) |
| `revision/audit/02_B2_semantic_defects/summarize_annotations.py` | `02_B2_semantic_defects/summarize_annotations.py` (package FISAT_gui_Hoang_2026-10-15) | `62803673dfb07f3d54b327e3c023f8eb29a83d9e5242eb01a173f1e125324153` | `e5afe7bac3196ba56946766874b98f6d47b30692c5b269059384cf03467265b3` | comments, docstrings and messages translated; code AST-identical |
| `revision/audit/03_H3_temporal_causal/h3_order_check.py` | `03_H3_temporal_causal/h3_order_check.py` (package FISAT_gui_Hoang_2026-10-15) | `e12bac936ed16d5010bedf151d2ebba2d89966ff0b2711eea295e09c071d8e82` | `ede25e4b358cfe7b1315f2134500e1f73682b997e8369d6bd576916070bbc20d` | comments, docstrings and messages translated; code AST-identical except the lines that locate the repository root and data folders (the script moved to a new folder) |
| `revision/audit/03_H3_temporal_causal/h3_make_annotation_sheet.py` | `03_H3_temporal_causal/h3_make_annotation_sheet.py` (package FISAT_gui_Hoang_2026-10-15) | `49abcfe80ac09999fe6ac54b4b62f8a87994e103a0569cbed6edd38baa50e9e9` | `f892c9bf6deecf705ada88f025e4fd3aea10632704a4ea8a25f03dfe9bdb9e93` | comments, docstrings and messages translated; code AST-identical |
| `revision/audit/06_mutation_test_SBERT/mutation_sbert_test.py` | `06_mutation_test_SBERT/mutation_sbert_test.py` (package FISAT_gui_Hoang_2026-10-15) | `089a37b0cab412d77998f0354f3977643025fef4fd406899c5dc3468166fdbc0` | `8379878fc702f99b061a3e46f8a1acce58e70e34d5ede396eecf3f5f869705c4` | comments, docstrings and messages translated; code AST-identical except the lines that locate the repository root and data folders (the script moved to a new folder) |
| `revision/audit/06_mutation_test_SBERT/run_mutation_audited.py` | `06_mutation_test_SBERT/run_mutation_audited.py` (package FISAT_gui_Hoang_2026-10-15) | `85b76185d2164c58be41f0b093a27352ab8c403fca118d356a49d2125bf169be` | `d34cc66439e0c8ae5e2bcae9659207e8184410629950b176f1a32f0b211873c3` | comments, docstrings and messages translated; code AST-identical except the lines that locate the repository root and data folders (the script moved to a new folder) |
| `revision/audit/07_audit/audit_h3_parser_version.py` | `07_audit/audit_h3_parser_version.py` (package FISAT_gui_Hoang_2026-10-15) | `b9a994bd04f4275431d71af23b9daf07cd33f1b0cb72634ee442cb380fb1925d` | `5988576dc5bc4aaae0fbaa231bb558d49febc8ef5dba0d64fdad9a900d02d1d7` | comments, docstrings and messages translated; code AST-identical except the lines that locate the repository root and data folders (the script moved to a new folder) |
| `revision/audit/02_B2_semantic_defects/b2_annotation_Codex_AI.csv` | `02_B2_semantic_defects/b2_annotation_Codex_AI.csv` (package FISAT_gui_Hoang_2026-10-15) | `d4a1ba0094346751b6ab55e444f98ea3009e8799997669745af1a92dd23aefac` | `fffeed3104ad40a595314a0ab8b5f47e6912bc99113bd99653c0b27169e38d3f` | free-text columns translated; label, count, severity and id columns identical |
| `revision/audit/02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv` | `02_B2_semantic_defects/b2_annotation_An_CONFIRMED.csv` (package FISAT_gui_Hoang_2026-10-15) | `7f6780dd4eb7e617715355ef50f503c7e59c3f8a427bd71c8379493c49103b28` | `221119c49b872532edc21c151308dc7d5fbbd0f414eaad8fd056be2b492d72c4` | free-text columns translated; label, count, severity and id columns identical; decision value GIU written as KEEP |
| `revision/audit/03_H3_temporal_causal/h3_annotation_Codex_AI.csv` | `03_H3_temporal_causal/h3_annotation_Codex_AI.csv` (package FISAT_gui_Hoang_2026-10-15) | `a07f5d0fbe1ddd4281ab3c853ca597868a071c4f6bd6642cb150ce8ffb2f8aa7` | `14768ecae206d032d1257e8bfce464856de86a584363b3fc960b50df7243ecfa` | free-text columns translated; label, count, severity and id columns identical |
| `revision/audit/03_H3_temporal_causal/h3_annotation_An_CONFIRMED.csv` | `03_H3_temporal_causal/h3_annotation_An_CONFIRMED.csv` (package FISAT_gui_Hoang_2026-10-15) | `a76c6fc5e2322e804f5e138f6b721eb35ab3d76d79f5f74537ccd271c3b472d5` | `aca9f024e14c8cd9b6257953610731c789d13d25f9915ed4ba0dbd8dc809b3fc` | free-text columns translated; label, count, severity and id columns identical; decision value GIU written as KEEP |
| `revision/audit/06_mutation_test_SBERT/PROTOCOL_Codex.md` | `06_mutation_test_SBERT/PROTOCOL_Codex.md` (package FISAT_gui_Hoang_2026-10-15) | `b5bfef4b3ecd3125f540cfcd274450349d4dad98fa64c6b754677b396e1e62b9` | `e7cdece7d53c79ee2b6dd2095eb0958663ec29c8952ad04d29d674369c8b41a6` | document translated |
| `revision/audit/06_mutation_test_SBERT/ADDENDUM_REVIEW_2026-10-15.md` | `06_mutation_test_SBERT/ADDENDUM_REVIEW_2026-10-15.md` (package FISAT_gui_Hoang_2026-10-15) | `6b2240dd713fe252624530e3da13b9fca678c947da72878d24fbefe1cb37168c` | `78d80e4cdf2a9b952ef6f61bf85276f7c8e13340dda298dd3360983eff154fd8` | document translated |
| `revision/audit/06_mutation_test_SBERT/requirements_measured.txt` | `07_audit/requirements_measured.txt` (package FISAT_gui_Hoang_2026-10-15) | `2e2fe3287a949fa7c1cf713ff56b6503a736c4ada0ea5afd081c2b72ce6f9607` | `2e2fe3287a949fa7c1cf713ff56b6503a736c4ada0ea5afd081c2b72ce6f9607` | moved only |
| `revision/audit/confirmation/An_confirmation_2026-10-15.json` | `07_audit/An_confirmation_2026-10-15.json` (package FISAT_gui_Hoang_2026-10-15) | `35ba7cfa5e878fb8024b1a4581377eb09c8a7aa284a83b9792db95950ddc4e32` | `5cad1fcc9bb4a7b69a0a4729b6d7097e99ac39a4b2a5b5d87fbd9503ccc905dd` | moved; values translated, verbatim Vietnamese quotes given as *_english_translation keys with a translation_note |
| `revision/audit/confirmation/An_confirmation_changes.json` | `07_audit/An_confirmation_changes.json` (package FISAT_gui_Hoang_2026-10-15) | `b72eb2512e1c58b611495222faef90b19a6495c9498eeb67970cd905c9959a72` | `b72eb2512e1c58b611495222faef90b19a6495c9498eeb67970cd905c9959a72` | moved only |
| `revision/audit/confirmation/AN_CONFIRMATION_2026-10-15.md` | `09_An_review/XAC_NHAN_CUA_AN.md` (package FISAT_gui_Hoang_2026-10-15) | `c88b0e59554262925246c13f2f698a42a1c564ffcab99e69c9a9ada434314680` | `97933336f042005d982265f2bc85d9b3d3f2b2bd5de504cbf0aa0d82a49b045c` | document translated; renamed |
| `revision/audit/confirmation/REVIEW_GUIDE_60_CASES.md` | `09_An_review/HUONG_DAN_DUYET_60_CASE.md` (package FISAT_gui_Hoang_2026-10-15) | `dfcbfefa4548a4874d6e1b91e2008077fb8793dbe2453b23086627c7c91a8f36` | `31d3b653d25a1a203bdf7266c9d7810505f1d38e3e9c2d8a95826695cfca5dbe` | document translated; renamed |
| `revision/audit/07_audit/b2_An_confirmed_summary.txt` | `07_audit/b2_An_confirmed_summary.txt` (package FISAT_gui_Hoang_2026-10-15) | `fddd61772abfefa9ff9f0710418588c40282bd93fd8439e82a7deed44ffc138d` | `30f817ce9c886978cce5d10064a23b381a470006bec8b77077a776843bce5077` | regenerated by the English summarize_annotations.py; numbers identical |
| `revision/audit/07_audit/h3_An_confirmed_summary.txt` | `07_audit/h3_An_confirmed_summary.txt` (package FISAT_gui_Hoang_2026-10-15) | `cba4925a6160053da5efdd36f0f67f432e7f3d25beb7408dbb463094ffbe9f02` | `3abf8ada4c3a8f81c51ffa22879733a44b87a5b4da73c1e6ceb040b179bf0de9` | regenerated by the English summarize_annotations.py; numbers identical |
| `revision/audit/independent_rater_15/b2_annotation_Hoang_ORIGINAL.csv` | `frozen_2026-10-16/b2_annotation_Hoang_ORIGINAL.csv` (hoang_15_phieu) | `9cd9d14a71ccaecedb2ea2c28c9afacfac12603f00589fbd5c1cbe5e79458fe7` | `8f9e293d20814256727990a8824b5b228f62742774a42d78dc561b556eb58cf9` | free-text columns translated; label, count, severity and id columns identical |
| `revision/audit/independent_rater_15/h3_annotation_Hoang_ORIGINAL.csv` | `frozen_2026-10-16/h3_annotation_Hoang_ORIGINAL.csv` (hoang_15_phieu) | `817274f73de08fa94eebbdfde5f8678cc689d101ebddc672dc0550aae60153f4` | `a73ca1250f30d2845547528a1e2dd4b91d410e6e89ae981d54cc528d99a8407d` | free-text columns translated; label, count, severity and id columns identical |
| `revision/audit/independent_rater_15/b2_annotation_Hoang_CLEAN.csv` | `frozen_2026-10-16/b2_annotation_Hoang_CLEAN.csv` (hoang_15_phieu) | `99a7dc39046b0879111d5e334139052ce66723d2bc403c1ebd8a6333f4f32733` | `cfba74670ef130eb554615c6a0a52e7a099efe0ef1c0164ede191834bee92835` | regenerated by the English make_clean.py from the English ORIGINAL |
| `revision/audit/independent_rater_15/h3_annotation_Hoang_CLEAN.csv` | `frozen_2026-10-16/h3_annotation_Hoang_CLEAN.csv` (hoang_15_phieu) | `2a319e70d0053e9cb3856fd2a58430106853f30ffa584f6cb7b72c20cbf45117` | `596c5a190d217dd76173dd384a9d11ac0cc61f04985c3f74c237428a6f42a228` | regenerated by the English make_clean.py from the English ORIGINAL |
| `revision/audit/independent_rater_15/clean_changes.csv` | `frozen_2026-10-16/clean_changes.csv` (hoang_15_phieu) | `68dbd6a243a819a381ce273ab2b403dc3b7cdec9acfc3fe92bef2165cf1bae01` | `31b41cd1edcb513d754986bbddd22fa77bcce0bb140410c534896b973238341b` | regenerated; same 63 changes, English note prefix |
| `revision/audit/independent_rater_15/make_clean.py` | `frozen_2026-10-16/make_clean.py` (hoang_15_phieu) | `58249df6287a190dad4bed95cc17880db04997070299ce69d06b9ec0b4f5cd8e` | `844cb1fd59028a77e92d58d05f54bac256bdec6da32c4df8a584fd3e5bca80f4` | comments, docstrings and messages translated; code AST-identical; note prefixes written in English |
| `revision/audit/independent_rater_15/verify_kappa.py` | `verify_kappa.py` (An's package FISAT_phan_hoi_Hoang_2026-10-18) | `37bed0473559e743451f4f2f26b4fe2597a29112be550cc49684111e0b11891f` | `c78faa38e171c9ad85defe28cfcdbdcc1dc8ad529ad6032d21bbfa2c213e2d4b` | comments, docstrings and messages translated; code AST-identical except the lines that locate the repository root and data folders (the script moved to a new folder) |
| `revision/audit/independent_rater_15/kappa_result.json` | `KAPPA_PORTABLE_CHECK.json` (An's package FISAT_phan_hoi_Hoang_2026-10-18) | `86d432a8922d7390537e298cc8d887c5fb940595a0a806f3287020b579353b80` | `85c0fb7fc37e89cbe329986f6e00f9c4f23399e746ae1517cff0c859809132c7` | regenerated by the English verify_kappa.py, which now writes this file; content identical (parsed JSON equal) |
| `revision/audit/independent_rater_15/DECLARATION_AND_KAPPA.md` | `frozen_2026-10-16/KHAI_BAO_VA_KAPPA.md` (hoang_15_phieu) | `f960cc4a95bd4ccdd06c878570222a8719114aff57bcd53c8c44d2b593fccf3d` | `eec2f9df658c59b28188ea44c85ad27d1f05f007e25a25223f60f2df7e827c84` | document translated; renamed; translator's note on hashes |
| `revision/audit/independent_rater_15/DECLARATION_ADDENDUM_2026-10-18.md` | `KHAI_BAO_BO_SUNG_2026-10-18.md` (hoang_15_phieu) | `5f2a902c49bf3882422338d9790bc07d2b93417131741ac5fbc25ffd105eaf24` | `875e86dc6285cb8a49c3b228a201b9441b37eb6854871fce5fcf437b175ece82` | document translated; renamed; translator's notes |
