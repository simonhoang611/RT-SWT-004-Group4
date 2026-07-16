# Experiment Design Rationale — LLM-Based BDD/Gherkin Test Generation
Ngày: 2025-06-10 | GAP source: SLR/gap-analysis.md

## Bảng Quyết Định

| Quyết định | Giá trị | Nguồn gốc |
|------------|---------|-----------|
| LLM/Tool | GPT-4o (gpt-4o-2024-05-13), zero-shot, temperature=0 | GAP-T: cột Tool/LLM — không paper nào dùng GPT-4o cho Gherkin từ user stories; *A systematic approach for assessing LLMs' test case generation capability (2025)* — cột Tool/LLM — "GPT-4o" — paper duy nhất dùng GPT-4o, xác nhận API accessible |
| Dataset | Connextra-format user stories từ môn học SE1905 (dự kiến 50–55 user stories) | GAP-D: không có public benchmark đúng định dạng Connextra; *Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024)* — cột Dataset — "50 user stories from Mendeley and blog posts" — không đúng Connextra → nhóm tự tạo |
| Metric chính | Cosine similarity (`sentence-transformers/all-MiniLM-L6-v2`) | GAP-M: không paper nào đo semantic similarity tự động cho Gherkin — đây là metric mới nhóm propose; rubric 3E — "all-MiniLM-L6-v2 for semantic matching" |
| Metric phụ 1 | BLEU-4 (`sacrebleu 2.3`) | *Harnessing LLMs for automated software testing: A leap towards scalable test case generation (2025)* — cột Metric — "BLEU score to evaluate similarity between generated and reference test cases" |
| Metric phụ 2 | Executable rate (`behave 1.2.6 + subprocess`) | *Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025)* — cột Metric — "Gherkin syntax accuracy = 93.3%" — dùng Behave để validate syntax; *Increasing Test Coverage by Automating BDD Tests in POCs using LLM (2024)* — cột Tool/LLM — "AutoDevSuite validated with Behave" |
| Baseline type | Human-level (expert-written Gherkin do giảng viên viết) | Loại claim của RQ = human-level; *AGORA: An Approach for Generating Acceptance Test Cases from Use Cases (2024)* — cột Metric — "Quality (Completeness/Clarity/Correctness)" — so sánh với oracle chuyên gia |
| Threshold RQ1 | ≥ 0.88 (cosine similarity) | Case 1 — *AGORA: An Approach for Generating Acceptance Test Cases from Use Cases (2024)* — cột Kết quả — "Quality value Mean = 88%" — paper đề xuất ngưỡng chất lượng cụ thể khi so với expert oracle |
| Threshold RQ2 | ≥ 90% (executable rate) | Case 1 — *Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025)* — cột Kết quả — "93.3% of Gherkin scenarios were syntactically correct" — làm tròn xuống 90% để thiết lập ngưỡng bảo thủ hơn |
| Pipeline base | AutoUAT / Test Flow | *Acceptance test generation with LLMs: An industrial case study (2025)* — cột Pipeline — "Step 1: sinh Gherkin từ user story; Step 2: sinh executable scripts" — evaluation paradigm gần nhất với RQ nhóm |

---

## Lý giải Threshold

### Threshold RQ1 — Cosine similarity ≥ 0.88

**Phân loại: Case 1** — paper đề xuất ngưỡng cụ thể, trích dẫn thẳng.

*AGORA: An Approach for Generating Acceptance Test Cases from Use Cases (2024)* — cột Kết quả — báo cáo điểm chất lượng trung bình đạt **88%** khi so sánh acceptance test case do GPT-4 sinh ra với oracle (chuyên gia). Đây là baseline human-level duy nhất trong 11 paper có con số cụ thể cho task gần nhất với RQ của nhóm (sinh acceptance test từ requirements, so với expert). Nhóm dùng đúng ngưỡng này — không điều chỉnh.

### Threshold RQ2 — Executable rate ≥ 90%

**Phân loại: Case 1** — paper báo cáo kết quả cụ thể, lấy làm floor value.

*Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025)* — cột Kết quả — "93.3% of Gherkin scenarios were syntactically correct upon generation". Nhóm lấy **90%** (làm tròn xuống từ 93.3%) làm ngưỡng bảo thủ — thấp hơn kết quả paper để giảm rủi ro claim sai. Ghi rõ: floor = 93.3% từ *Streamlining (2025)*, threshold = 90%.

---

## Pipeline Base

**Paper:** *Acceptance test generation with LLMs: An industrial case study (2025)*

**Lý do chọn:** Đây là paper duy nhất trong 11 có evaluation paradigm khớp trực tiếp với RQ của nhóm — sinh Gherkin từ user story (không phải từ use case hay code), đo chất lượng output Gherkin, và tách biệt rõ hai bước: (1) sinh scenario, (2) sinh executable script. Nhóm chỉ làm bước 1, đo cosine similarity của Gherkin output so với expert-written ground truth.

**Thay đổi so với base paper:**
- Thay GPT-4 Turbo → GPT-4o (lý do: GAP-T)
- Thay human helpfulness survey → cosine similarity tự động (lý do: GAP-M)
- Thay JIRA issues → Connextra user stories từ môn học (lý do: GAP-D)
