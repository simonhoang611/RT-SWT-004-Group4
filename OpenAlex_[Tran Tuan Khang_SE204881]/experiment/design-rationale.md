# Experiment Design Rationale — LLM for Gherkin/BDD Acceptance Test Generation
Ngày: 2026-06-07 | GAP source: SLR/gap-analysis.md

---

## Bảng Quyết Định

| Quyết định | Giá trị | Nguồn gốc |
|---|---|---|
| LLM/Tool | GPT-4o (OpenAI API, version `gpt-4o-2024-08-06`), temperature=0 | GAP-T: cột Tool/LLM trong evidence table — không có paper nào dùng GPT-4o |
| Dataset | Connextra-format user stories từ ≥ 3 dự án SE công khai trên GitHub (target: 30–50 stories) | GAP-D: không paper nào dùng Connextra format từ ≥ 3 dự án công khai |
| Metric chính | Cosine semantic similarity — tính bằng `sentence-transformers` model `all-MiniLM-L6-v2` (HuggingFace, Apr 2024 checkpoint) | GAP-M: cột Metric trong evidence table; Paper 1 (ICEIS 2025) dùng cosine similarity — metric gần nhất với task |
| Metric phụ 1 | Executable syntax rate (%) — tính bằng `behave 1.2.6` + subprocess capture | Kế thừa từ Paper 7 (IEEE Access 2024) — đo Gherkin syntax errors bằng parser |
| Metric phụ 2 | BLEU-4 — tính bằng `sacrebleu 2.3` | Kế thừa từ Paper 5 (SBES 2025) — METEOR, phổ biến trong NLG evaluation |
| Baseline type | Absolute threshold (không compare với tool khác) | Claim type của RQ: "đạt cosine ≥ 0.85" → absolute threshold, không comparative |
| Threshold RQ1 | cosine similarity ≥ **0.85** | Case 2 — Paper 5 (SBES 2025) báo cáo METEOR cao nhất = 0.84 (Gemini). Floor = 0.84, làm tròn lên = 0.85. Ghi rõ: *"floor=0.84 từ Paper 5/SBES 2025, threshold=0.85 (làm tròn)"* |
| Threshold RQ2 | executable rate ≥ **80%** | Case 2 — Paper 7 (IEEE Access 2024): GPT-3.5/4 đạt ~79–82% syntax validity (Table of Results). Floor = 79%, làm tròn lên = 80%. Ghi rõ: *"floor=79% từ Paper 7/IEEE Access 2024, threshold=80%"* |
| Pipeline base | Paper 7 (IEEE Access 2024) — "Evaluation and Insights Into LLMs in BDD" | Paradigm gần nhất: zero-shot prompt → Gherkin output → syntax validation; thích nghi thêm cosine similarity step |
| Prompt strategy | Zero-shot | GAP-T: test zero-shot capability vì chưa có baseline; Paper 7 & 5 đều dùng zero-shot làm điều kiện chính |
| Statistical test RQ1 | Wilcoxon signed-rank test (one-tailed, α=0.05) | Output cosine similarity là số liên tục [0,1] → Wilcoxon phù hợp; phân phối chưa biết → non-parametric an toàn hơn t-test |
| Statistical test RQ2 | Binomial exact test (one-tailed, p₀=0.80, α=0.05) | Output executable rate là nhị phân (pass/fail per scenario) → Binomial exact test |

---

## Lý giải Threshold (1 đoạn cho mỗi threshold)

### Threshold RQ1: cosine similarity ≥ 0.85

Paper 5 (SBES 2025 — "A Comparative Study of LLMs for Gherkin Generation") báo cáo Gemini đạt METEOR score cao nhất = **0.84** trên 10 real-world test cases. Đây là kết quả số cao nhất được báo cáo trong evidence table cho metric đo chất lượng ngữ nghĩa của Gherkin output. Áp dụng Case 2: floor = 0.84, làm tròn lên = **0.85**. Không tự đặt threshold vì "nghe có vẻ hợp lý" — threshold có nguồn gốc từ literature. Lưu ý: METEOR và cosine similarity là hai metric khác nhau về bản chất, nhưng đây là paper duy nhất cung cấp con số tham chiếu gần nhất.

### Threshold RQ2: executable syntax rate ≥ 80%

Paper 7 (IEEE Access 2024 — "Comprehensive Evaluation and Insights Into LLMs in BDD") đo lỗi cú pháp Gherkin bằng Gherkin-lint, báo cáo GPT-3.5 và GPT-4 đạt ~79–82% syntax validity. Áp dụng Case 2: floor = 79% (kết quả thấp nhất trong nhóm tốt nhất), làm tròn lên = **80%**. Threshold này phản ánh mức độ mà community đã đạt được với GPT-3.5/4; GPT-4o (mạnh hơn) cần ít nhất bằng mức đó.

---

## Pipeline (thích nghi từ base paper)

```
Input: Connextra user story (dạng: "As a [role], I want [action], so that [benefit]")
         ↓
Step 1: Zero-shot prompt → GPT-4o API (gpt-4o-2024-08-06, temperature=0)
         Prompt template: "Given the following user story, generate a complete Gherkin
         feature file with scenarios and step definitions:\n\n[USER_STORY]"
         ↓
Step 2: Parse output → extract Gherkin text
         ↓
Step 3a: Cosine similarity — sentence-transformers (all-MiniLM-L6-v2)
          encode(generated_gherkin) vs encode(expert_written_gherkin)
         ↓
Step 3b: Executable syntax — behave 1.2.6 + subprocess
          behave --dry-run → pass/fail per scenario
         ↓
Step 3c: BLEU-4 — sacrebleu 2.3 (secondary metric)
         ↓
Step 4: Statistical test
          RQ1: Wilcoxon signed-rank (cosine scores vs threshold 0.85)
          RQ2: Binomial exact test (executable count vs p₀=0.80)
```

**Thay đổi so với base paper (Paper 7):**
- Thêm cosine similarity step (Paper 7 chỉ dùng syntax validation)
- Dùng GPT-4o thay vì GPT-3.5/4
- Thêm Binomial exact test cho RQ2 (Paper 7 dùng descriptive stats)
- Dataset: Connextra user stories thay vì curated BDD scenarios
