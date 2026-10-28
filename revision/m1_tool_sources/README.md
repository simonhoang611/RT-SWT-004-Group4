# Official tool references (Action Tracker M1)

The paper cites four official sources for the tools it uses. For each source,
`SOURCE_ACCESS_RECORD.json` records the URL, what the page confirms, the access date,
and the file name and SHA-256 of an unedited screenshot of the page.

| Key in the paper | Source | Cited in | Screenshot |
|---|---|---|---|
| `openai_gpt54mini` | OpenAI, GPT-5.4 Mini model documentation | Section 3.2 | `openai_gpt54mini.png` |
| `openai_chat_api` | OpenAI, Create chat completion (API reference) | Section 3.2 | `openai_chat_api.png` |
| `minilm_card` | Sentence Transformers, all-MiniLM-L6-v2 model card, revision 1110a24 | Section 3.4 | `minilm_card.png` |
| `behave133` | behave v1.3.3 release on GitHub | Section 3.5 | `behave_v1.3.3.png` |

Notes:
- The OpenAI model page shows that the snapshot `gpt-5.4-mini-2026-03-17` exists. It
  does not show which model the C0 requests returned: the C0 log stores the requested
  model name (Section 3.3 of the paper). C1 and C2 log the name returned by the API.
- The model card URL points to revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`,
  the revision used for the sentence-transformers re-check (`revision/h2/`). The
  revision of the encoder used for the original C0 scoring was not recorded.
- For behave, the screenshot shows the GitHub release page; the PyPI page
  (https://pypi.org/project/behave/1.3.3/) lists the same version.
- The two DOIs flagged in the tracker:
  - TestBench: the publisher page
    (https://journal.hep.com.cn/fcs/EN/10.1007/s11704-025-50078-9) states the DOI
    `10.1007/s11704-025-50078-9`, but on 28 October 2026 the link
    https://doi.org/10.1007/s11704-025-50078-9 returned an error. The reference
    therefore links to the publisher page.
  - Agresti (2002): `10.1002/0471249688` matches the library records and the link
    resolves. In the PDF its URL was broken across two lines; the reference list is now
    set ragged right.
