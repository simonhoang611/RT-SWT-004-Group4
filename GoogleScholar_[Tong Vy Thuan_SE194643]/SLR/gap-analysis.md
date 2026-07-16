# GAP Analysis — LLM-Based Test Case Generation (BDD/Gherkin)
Evidence table: N = 11 paper | Ngày: 2025-06-10

## Bảng GAP

| Cột | Phát hiện | Loại GAP | Phản chứng |
|-----|-----------|----------|------------|
| Tool/LLM | GPT-4o chưa được dùng để sinh Gherkin từ Connextra user stories | GAP-T | ✅ Kiểm tra 11 paper: *A systematic approach for assessing LLMs' test case generation capability (2025)* dùng GPT-4o nhưng cho Python unit test; *Acceptance test generation with LLMs: An industrial case study (2025)* dùng GPT-4 Turbo; *Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024)* dùng GPT-3.5/GPT-4 — không paper nào dùng GPT-4o cho Gherkin từ user stories |
| Metric | Không paper nào đo semantic similarity tự động giữa Gherkin sinh ra và kịch bản chuyên gia viết | GAP-M | ✅ *Acceptance test generation with LLMs: An industrial case study (2025)* — cột Metric — "Human survey (Helpfulness score)" — có đo semantic relevance nhưng thủ công, không tự động; không paper nào dùng cosine similarity hay BERTScore |
| Dataset | Không có public benchmark cho task sinh Gherkin từ Connextra-format user stories | GAP-D | ✅ *Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024)* — cột Dataset — "50 user stories from Mendeley and blog posts" — không đúng định dạng Connextra; *Acceptance test generation with LLMs: An industrial case study (2025)* — cột Dataset — "13 JIRA issues, 1 công ty" — không public |
| Hạn chế | 7/11 paper thừa nhận mẫu nhỏ, khó tổng quát hóa | GAP-S | ✅ *Testbench: Evaluating class-level test case generation capability of LLMs (2024)*; *A systematic approach for assessing LLMs' test case generation capability (2025)*; *Increasing Test Coverage by Automating BDD Tests in POCs using LLM (2024)*; *Acceptance test generation with LLMs: An industrial case study (2025)*; *Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024)*; *Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025)*; *AGORA: An Approach for Generating Acceptance Test Cases from Use Cases (2024)* — cột Hạn chế — đều nêu sample size nhỏ |

---

## GAP Chính: GAP-T

GPT-4o chưa được đánh giá cho task sinh Gherkin/BDD acceptance test từ user stories định dạng Connextra. Paper gần nhất là *A systematic approach for assessing LLMs' test case generation capability (2025)* có dùng GPT-4o nhưng task là sinh Python unit test — không phải Gherkin từ user stories.

### Bằng chứng chi tiết

- **Dùng GPT-4o nhưng sai task**: *A systematic approach for assessing LLMs' test case generation capability (2025)* — cột Tool/LLM — "GPT-4o" — cột Dataset — "GBCV (786 Python programs, unit testing)"
- **Dùng GPT-4 Turbo, không phải GPT-4o**: *Acceptance test generation with LLMs: An industrial case study (2025)* — cột Tool/LLM — "GPT-4 Turbo (gpt-4-1106-preview)"
- **Dùng GPT-4/GPT-3.5, không phải GPT-4o**: *Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024)* — cột Tool/LLM — "GPT-3.5 / GPT-4 / Llama-2-13B / PaLM-2"; *Testbench: Evaluating class-level test case generation capability of LLMs (2024)* — "GPT-3.5-turbo / GPT-4-1106-preview"; *AGORA: An Approach for Generating Acceptance Test Cases from Use Cases (2024)* — "GPT-4 via API"; *XUAT-Copilot: Multi-Agent Collaborative System for Automated UAT with LLM (2024)* — "GPT-3.5 / GPT-4"
- **Dùng model cũ/nhỏ**: *Harnessing LLMs for automated software testing: A leap towards scalable test case generation (2025)* — cột Tool/LLM — "Llama-2-7b-chat-hf"; *Unit test case generation with transformers and focal context (2020)* — "BART Transformer"
- **Dùng model khác, sai domain**: *Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025)* — cột Tool/LLM — "DeepSeek-R1" — cột Dataset — "MyBMW app (Flutter/mobile)"; *Increasing Test Coverage by Automating BDD Tests in POCs using LLM (2024)* — "Google Gemini" — cột Metric — không đo semantic similarity

→ Không có paper nào hội tụ đủ ba yếu tố: **GPT-4o + Gherkin + Connextra user stories**.

---

## GAP Phụ: GAP-M

Chưa có nghiên cứu nào đo semantic similarity tự động — bằng cosine similarity hoặc BERTScore — giữa Gherkin do LLM sinh ra và kịch bản mẫu do chuyên gia viết.

### Bằng chứng chi tiết

- **Chỉ đo syntax**: *Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024)* — cột Metric — "Syntax Validation Accuracy (Gherkin-lint)"; *Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025)* — cột Kết quả — "Gherkin syntax accuracy = 93.3%"; *Testbench: Evaluating class-level test case generation capability of LLMs (2024)* — cột Metric — "Syntactic correctness, Compilation correctness"
- **Chỉ đo code coverage**: *Harnessing LLMs for automated software testing: A leap towards scalable test case generation (2025)* — cột Metric — "Precision, Recall, F1, BLEU"; *Increasing Test Coverage by Automating BDD Tests in POCs using LLM (2024)* — cột Metric — "Line coverage %"; *LLM4Fin: Fully Automating LLM-Powered Test Case Generation for FinTech (2024)* — cột Metric — "BSC, SBC, MC/DC"
- **Đo semantic nhưng thủ công**: *Acceptance test generation with LLMs: An industrial case study (2025)* — cột Metric — "Helpfulness, Semantic relevance" — cột Kết quả — "đánh giá qua human survey, không tự động"
- **Không paper nào** dùng cosine similarity (sentence-transformers) hay BERTScore để so Gherkin với requirement gốc

→ Áp dụng metric tự động chưa từng được dùng trong domain này.

---

## Chi tiết kiểm tra phản chứng

### Tuyên bố 1: GPT-4o chưa được dùng cho Gherkin generation từ Connextra user stories

| Paper | Đã làm không? | Ghi chú |
|-------|--------------|---------|
| A systematic approach for assessing LLMs' test case generation capability (2025) | ❌ Không | Dùng GPT-4o — cột Dataset — "GBCV, Python unit testing" — sai task |
| Acceptance test generation with LLMs: An industrial case study (2025) | ❌ Không | Dùng GPT-4 Turbo (gpt-4-1106-preview), không phải GPT-4o |
| Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024) | ❌ Không | Dùng GPT-3.5/GPT-4 — cột Dataset — "50 user stories, không đúng Connextra" |
| Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025) | ❌ Không | Dùng DeepSeek-R1 — cột Dataset — "MyBMW Flutter app" |
| Increasing Test Coverage by Automating BDD Tests in POCs using LLM (2024) | ❌ Không | Dùng Google Gemini — cột Dataset — "4 POC projects nội bộ" |
| AGORA: An Approach for Generating Acceptance Test Cases from Use Cases (2024) | ❌ Không | Dùng GPT-4 via API — cột Dataset — "10 use cases, telemedicine" |
| Testbench: Evaluating class-level test case generation capability of LLMs (2024) | ❌ Không | Dùng GPT-3.5/GPT-4 — cột Dataset — "108 Java classes, unit testing" |
| XUAT-Copilot: Multi-Agent Collaborative System for Automated UAT with LLM (2024) | ❌ Không | Dùng GPT-3.5/GPT-4 — cột Dataset — "450 test cases, WeChat Pay" |
| Harnessing LLMs for automated software testing: A leap towards scalable test case generation (2025) | ❌ Không | Dùng Llama-2-7b — cột Dataset — "methods2test, Java unit testing" |
| Unit test case generation with transformers and focal context (2020) | ❌ Không | Dùng BART — cột Dataset — "METHODS2TEST, Java unit testing" |
| LLM4Fin: Fully Automating LLM-Powered Test Case Generation for FinTech (2024) | ❌ Không | Dùng Mengzi-BERT/RoBERTa — cột Dataset — "tài liệu quy định tài chính" |

→ **Kết luận: XÁC NHẬN** — không paper nào dùng GPT-4o cho Gherkin từ Connextra user stories.

### Tuyên bố 2: Chưa có metric tự động đo semantic similarity cho Gherkin

| Paper | Đã làm không? | Ghi chú |
|-------|--------------|---------|
| Acceptance test generation with LLMs: An industrial case study (2025) | ❌ Không | Cột Metric — "Semantic relevance" — cột Kết quả — "human survey only, không tự động" |
| Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024) | ❌ Không | Cột Metric — "Gherkin-lint syntax validation" — chỉ đo cú pháp |
| Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025) | ❌ Không | Cột Metric — "Accuracy & Completeness" — human review |
| Harnessing LLMs for automated software testing: A leap towards scalable test case generation (2025) | ❌ Không | Cột Metric — "BLEU" — đo token overlap, không phải semantic similarity |
| Testbench: Evaluating class-level test case generation capability of LLMs (2024) | ❌ Không | Cột Metric — "Mutation kill rate, Line coverage" — không liên quan Gherkin |
| AGORA: An Approach for Generating Acceptance Test Cases from Use Cases (2024) | ❌ Không | Cột Metric — "Quality (Completeness/Clarity/Correctness)" — human Likert scale |
| Increasing Test Coverage by Automating BDD Tests in POCs using LLM (2024) | ❌ Không | Cột Metric — "Line coverage %" — không đo semantic |
| LLM4Fin: Fully Automating LLM-Powered Test Case Generation for FinTech (2024) | ❌ Không | Cột Metric — "BSC, SBC, MC/DC" — coverage-based, không semantic |
| XUAT-Copilot: Multi-Agent Collaborative System for Automated UAT with LLM (2024) | ❌ Không | Cột Metric — "Pass@1, Complete@1" — execution-based, không semantic |
| A systematic approach for assessing LLMs' test case generation capability (2025) | ❌ Không | Cột Metric — "Incomplete rate, Error rate" — không đo similarity |
| Unit test case generation with transformers and focal context (2020) | ❌ Không | Cột Metric — "BLEU, Line coverage" — không đo semantic similarity |

→ **Kết luận: XÁC NHẬN** — không paper nào dùng cosine similarity hay BERTScore để đo Gherkin vs requirement gốc.

---

## Feasibility Check — GAP Chính (GAP-T: GPT-4o)

| Tiêu chí | Mức | Ghi chú |
|----------|-----|---------|
| Dataset | ✅ An toàn | Dùng Connextra user stories từ môn học — có sẵn, không cần crawl |
| Tool/API | ⚠️ Cần xử lý | GPT-4o có API public — *A systematic approach for assessing LLMs' test case generation capability (2025)* — cột Tool/LLM — đã dùng thành công; cần trả phí nhưng < $5 tổng (55 user stories × ~$0.01) |
| Compute | ✅ An toàn | Zero-shot chỉ gọi API — *Acceptance test generation with LLMs: An industrial case study (2025)* — cột Kết quả — "cost ≈ 0.12€/user story" — CPU đủ |
| Ground truth | ⚠️ Cần xử lý | Cần lecturer/nhóm viết Gherkin mẫu — *AGORA: An Approach for Generating Acceptance Test Cases from Use Cases (2024)* — cột Hạn chế — "1 oracle duy nhất" — ước tính ≤ 5 giờ cả nhóm |
| Skills | ✅ An toàn | sentence-transformers có sẵn trên PyPI, có tutorial; *Streamlining Acceptance Test Generation for Mobile Apps Through LLMs (2025)* — cột Pipeline — dùng Behave cho executable rate |
| Thời gian | ✅ An toàn | Zero-shot nhanh — *LLM4Fin: Fully Automating LLM-Powered Test Case Generation for FinTech (2024)* — cột Kết quả — "~7 giây/test case" — xong với buffer ≥ 1 tuần |
| Contribution | ✅ An toàn | Baseline đầu tiên cho GPT-4o + Connextra → Gherkin — không paper nào trong 11 đã làm |

**Kết quả: 2 ⚠️ Cần xử lý, 0 ✗ Blocker → An toàn, tiếp tục với GAP này.**