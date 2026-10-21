# H2 run and analysis notes (16 Oct 2026)

Facts recorded after the runs. The analysis plan itself (`H2_ANALYSIS_PLAN.md`, SHA-256 bb2197dd…c129) is unchanged.

- Runs by Hoàng on his machine: C1 11:50–12:40 UTC, C2 11:51–13:35 UTC (pilot ids 1, 101, 201 included).
  Script SHA-256 f634130978c4a7a441b7d1684632de866b442ea28194b9e97271a5cd67167fef.
  After the runs only comments were changed (cell numbers); the parsed code is identical.
- 261/261 OK in each condition, 0 ERROR, 0 EMPTY, finish_reason "stop" for all, response.model
  "gpt-5.4-mini-2026-03-17" for all 522 calls.
- Tokens: C1 prompt 91,918, completion 557,407. C2 prompt 1,188,083 (878,080 cached), completion 742,999.
  Cost at Standard list price ($0.75 input, $0.075 cached input, $4.50 output per 1M): C1 ≈ $2.58, C2 ≈ $3.64.
- Encoder: huggingface.co was not reachable from the analysis container, so `h2_cosine_onnx.py` uses the
  ONNX export of all-MiniLM-L6-v2 published by Chroma (archive SHA-256 913d7300…6ec3) with the same
  tokenisation, 256-token truncation, mean pooling and normalisation. It reproduces the original C0
  scores (`results/full_per_row_metrics.csv`) with max |diff| 3.6e-7 (`h2_cosine_check.txt`).
  This is an implementation detail, not a change of metric.
- Confirmation with sentence-transformers (Hoàng's machine, 16 Oct 2026, `h2_cosine_st_check.py`):
  sentence-transformers 5.6.0, model sentence-transformers/all-MiniLM-L6-v2 revision
  1110a243fdf4706b3f48f1d95db1a4f5529b4d41, Python 3.14.6, Windows 11. Versus ONNX: n = 783,
  max |diff| 2.98e-7 (C0 2.38e-7, C1 2.98e-7, C2 2.98e-7). C0 versus `results/full_per_row_metrics.csv`:
  max |diff| 3.58e-7. On the 255 analysed ids, medians and counts ≥ 0.85 are identical
  (C0 0.853 / 135, C1 0.819 / 88, C2 0.875 / 164); no file changes side of 0.85
  (closest ONNX score is 5.0e-5 from it). Output `h2_cosine_st.csv` (SHA-256 c7a9620e…7e30), `h2_cosine_st_check.txt`.
- Parser: `revision/check_syntax.py` with behave 1.3.3. FAIL ids: C0 136, 148, 154; C1 110, 130, 138; C2 135.

Reproduce (from the repository root):
    python revision/h2/h2_cosine_onnx.py --onnx-dir <folder with model.onnx and tokenizer.json>
    python revision/h2/h2_cosine_st_check.py   # optional, needs huggingface.co
    python revision/check_syntax.py --input revision/h2/h2_C1_output.csv --col generated_gherkin --out revision/h2/h2_syntax_C1.csv
    python revision/check_syntax.py --input revision/h2/h2_C2_output.csv --col generated_gherkin --out revision/h2/h2_syntax_C2.csv
    python revision/check_syntax.py --input results/full_gpt54mini_output.csv --col generated_gherkin --out revision/h2/h2_syntax_C0.csv
    python revision/h2/h2_analysis.py
