# Gap Statement — LLM-Based Test Case Generation
Evidence table: N = 11 paper

---

## Các khoảng trống phát hiện

### GAP-T1 (Technology — LLM model diversity):
Hầu hết nghiên cứu tập trung vào dòng GPT (OpenAI), chưa đánh giá đầy đủ các open-source LLM hiện đại.

**Bằng chứng:**
- Dùng GPT-4/GPT-3.5: Testbench (2024), A systematic approach (2025), Acceptance test generation with LLMs (2025), XUAT-Copilot (2024), Comprehensive evaluation of LLMs in automation of BDD (2024), AGORA (2024) — 6/11 bài
- Dùng open-source nhưng cũ/nhỏ: Harnessing LLMs for automated software testing (2025) dùng Llama-2-7B; Unit test case generation with transformers (2020) dùng BART
- Không bài nào dùng LLaMA-3, Mistral, Gemini 1.5, Claude cho unit/BDD test generation (chỉ Streamlining Acceptance Test Generation for Mobile Apps (2025) dùng DeepSeek cho acceptance test mobile)
- Bài gần nhất: Comprehensive evaluation of LLMs in automation of BDD acceptance test formulation (2024) so sánh GPT-3.5/GPT-4/Llama-2-13B/PaLM-2 — nhưng chỉ đo syntax accuracy, không đo coverage hay semantic correctness

### GAP-T2 (Technology — Gherkin/BDD generation từ requirements):
Rất ít nghiên cứu tập trung sinh Gherkin/BDD scenarios trực tiếp từ user stories bằng LLM, và chưa ai dùng GPT-4o cho task này.

**Bằng chứng:**
- Có BDD/Gherkin: Increasing Test Coverage by Automating BDD Tests (2024), Acceptance test generation with LLMs (2025), Comprehensive evaluation of LLMs in automation of BDD (2024), Streamlining Acceptance Test Generation for Mobile Apps (2025) — 4/11 bài
- Trong đó chỉ Comprehensive evaluation of LLMs in automation of BDD (2024) đo syntax accuracy; Acceptance test generation with LLMs (2025) đo helpfulness qua human feedback
- A systematic approach for assessing LLMs' test case generation capability (2025) dùng GPT-4o nhưng cho Python unit test, không phải Gherkin từ user stories
- Không bài nào đo semantic correctness của Gherkin so với requirement gốc một cách tự động
- Bài gần nhất: Acceptance test generation with LLMs: An industrial case study (2025) sinh Gherkin từ JIRA issues nhưng chỉ 13 user stories, 1 công ty

### GAP-M1 (Metric — thiếu semantic correctness):
Các nghiên cứu chủ yếu đo syntax/coverage, chưa đo semantic relevance giữa test case sinh ra và requirement.

**Bằng chứng:**
- Đo syntax/compilation: Testbench (2024), Comprehensive evaluation of LLMs in automation of BDD (2024), Streamlining Acceptance Test Generation for Mobile Apps (2025)
- Đo code coverage: Harnessing LLMs (2025), Testbench (2024), Unit test case generation with transformers (2020), Increasing Test Coverage (2024), LLM4Fin (2024)
- Đo semantic relevance: chỉ Acceptance test generation with LLMs (2025) — nhưng qua human judgment, không có metric tự động
- Không bài nào dùng BERTScore hoặc cosine similarity để đo test case vs requirement

### GAP-M2 (Metric — thiếu mutation testing):
Mutation kill rate — thước đo hiệu quả phát hiện lỗi — hầu như không được dùng.

**Bằng chứng:**
- Đo mutation kill rate: chỉ Testbench: Evaluating class-level test case generation capability of LLMs (2024) — GPT-4 đạt 26.10%, còn thấp
- 10/11 bài còn lại không đo mutation score
- Bài gần nhất: Unit test case generation with transformers (2020) đo defect detection qua Defects4J nhưng không dùng mutation testing

### GAP-D1 (Dataset — domain hẹp):
Phần lớn dataset tập trung vào Java unit testing hoặc một domain công nghiệp cụ thể, chưa có benchmark đa domain chuẩn hóa.

**Bằng chứng:**
- Java unit testing: Harnessing LLMs (2025) — methods2test; Testbench (2024) — TestBench; Unit test case generation with transformers (2020) — METHODS2TEST
- Domain đơn lẻ: LLM4Fin (2024) — FinTech; XUAT-Copilot (2024) — WeChat Pay; Streamlining Acceptance Test Generation for Mobile Apps (2025) — BMW Flutter app
- Python: chỉ A systematic approach for assessing LLMs' test case generation capability (2025) — GBCV, tự tạo
- Không bài nào dùng benchmark đa ngôn ngữ + đa domain + public

### GAP-D2 (Dataset — thiếu dataset cho BDD/Gherkin generation):
Không có public benchmark chuẩn cho task sinh Gherkin từ user stories.

**Bằng chứng:**
- Increasing Test Coverage by Automating BDD Tests (2024): 4 dự án POC nội bộ, không public
- Acceptance test generation with LLMs (2025): 13 JIRA issues, 1 công ty automotive, không public
- Comprehensive evaluation of LLMs in automation of BDD (2024): 50 user stories từ Mendeley/blogs — nhỏ nhất, bán công khai, không đúng định dạng Connextra
- Streamlining Acceptance Test Generation for Mobile Apps (2025): dữ liệu BMW, confidential
- Không bài nào dùng hoặc tạo public benchmark cho Gherkin generation

---

## Phát biểu GAP tổng hợp

Mặc dù các nghiên cứu hiện tại đã chứng minh khả năng của LLM (chủ yếu dòng GPT) trong sinh unit test case cho Java, vẫn tồn tại khoảng trống đáng kể về việc đánh giá GPT-4o trong task sinh Gherkin/BDD test từ Connextra-format user stories — cụ thể là chưa có benchmark công khai phù hợp, chưa có metric semantic correctness tự động (BERTScore-F1), và chưa có đánh giá nào kết hợp cả ba yếu tố này trong một nghiên cứu.