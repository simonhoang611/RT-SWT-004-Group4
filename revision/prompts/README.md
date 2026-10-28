# Prompt artifacts (Action Tracker H6 and H13)

This folder holds every component of the prompts sent to the API in conditions
C0, C1 and C2, as plain UTF-8 files with LF line breaks:

| File | Content |
|---|---|
| `system_message_ecommerce.txt`, `system_message_finance.txt`, `system_message_social.txt` | System message of Sylius, Apache Fineract and Diaspora (same in C0, C1 and C2) |
| `user_prompt_one_shot_template.txt` | User prompt of C0 and C2; `{example_user_story}`, `{example_gherkin}` and `{user_story}` are placeholders. The first line ends with a space. |
| `user_prompt_zero_shot_template.txt` | User prompt of C1; `{user_story}` is a placeholder |
| `exemplars/ex_<id>_user_story.txt`, `exemplars/ex_<id>.feature` | Story and reference Gherkin of the six exemplars (C0: 2, 102, 202; C2: 86, 119, 203) |
| `exemplar_mapping.csv` | Condition, project, domain and exemplar id |
| `MANIFEST_SHA256.txt` | SHA-256 of the 18 files above (`sha256sum -c` format) |
| `PROMPT_EXPORT_CHECK.json` | Result of the checks below, with the hashes of the source files |

A C0 or C2 prompt is the one-shot template with the project's exemplar story and
Gherkin inserted for `{example_user_story}` and `{example_gherkin}`. No newline is
added after the original text of any file.

## Rebuild and check

From the repository root (Python standard library only, no API calls):

    python revision/prompts/make_prompt_artifacts.py

The script reads `scripts/run_experiment.ipynb`, `revision/h2/h2_run_prompts.py`,
`data/full_user_stories.csv` and `data/full_ground_truth.csv`. It runs only the
literal constants and the pure prompt functions of these files, not the notebook
pipeline or the API runner. It stops with an error unless the three system
messages equal those of the notebook and the C0 prompt it assembles equals the
notebook's prompt for all 261 stories.

CSV fields are read with CRLF converted to LF, because `.gitattributes` does not
protect `data/` and a Windows checkout with `core.autocrlf=true` would otherwise
change the six exemplar stories and their hashes. The manifest is therefore the
same on every platform.

The files reconstruct the prompts from the archived code and data. The API logs
store token counts but not request bodies, so they are not a copy of the
transmitted requests. Run dates: C0 on 19 July 2026 (`results/full_api_log.jsonl`),
C1 and C2 on 16 October 2026 (`revision/h2/h2_C1_api_log.jsonl`,
`revision/h2/h2_C2_api_log.jsonl`).

The paper (Appendix A) refers to the release tag `fisat2026-camera-ready`.
