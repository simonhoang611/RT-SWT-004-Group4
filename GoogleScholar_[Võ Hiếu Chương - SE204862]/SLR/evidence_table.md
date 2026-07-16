# Evidence Table — LLM for Acceptance Test Automation (BDD/Gherkin)
*N papers included: **12** | Date: **2026-05-31***

> **Ghi chú:** Số liệu trích từ abstract/full-text đã truy cập. Cột Limitations lấy từ section "Limitations / Threats to Validity / Future Work" của từng paper. Papers #9, #14, #18 đã bị loại ở vòng 2 (EC3/EC5) vì không peer-reviewed hoặc thiếu số liệu định lượng. Papers Poth 2025, Patel 2025, Matveeva 2025 bị loại vì không tìm được file PDF (EC2).
>
> **Lý do giữ Adu 2024 (Master Thesis, #12):** IE criteria cho phép grey literature (master thesis từ trường đại học có uy tín — University of Eastern Finland) nếu có số liệu định lượng rõ ràng và đáp ứng EC1–EC4. Adu 2024 đáp ứng đủ: có Gherkin syntax metric (Gherkin-lint), có so sánh zero-shot vs. few-shot+RAG, và cung cấp contribution độc lập (GPT-3.5-turbo, RAG pipeline). Papers #9/#14/#18 bị loại vì vi phạm EC3 (thiếu quantitative metric) hoặc EC5 (blog/preprint không có review process) — khác với Adu 2024 là academic thesis có supervisor review.

---

| # | Paper (Tên + Năm + Venue) | Tool/LLM | Dataset | Metric | Kết quả | Hạn chế tự nêu |
|---|---|---|---|---|---|---|
| 1 | Karpurapu et al. 2024 — *Comprehensive Evaluation: LLMs in BDD Acceptance Test Formulation* — IEEE Access 2024 | GPT-3.5, GPT-4, Llama-2-13B, PaLM-2 — zero-shot & few-shot | ~50 user stories (Mendeley dataset + blog) | Syntax validation accuracy (Gherkin-lint), số syntax errors | GPT-3.5 & GPT-4 few-shot: ~98% feature files không có syntax error; Llama-2-13B và PaLM-2 kém hơn đáng kể | Dataset nhỏ (~50 user stories); chỉ syntactic correctness, không đo semantic validity; user stories từ nguồn công khai |
| 2 | Ferreira et al. 2025 — *Acceptance Test Generation with LLMs: An Industrial Case Study* — arXiv/IEEE 2025 | GPT-4 Turbo — structured prompting; Gherkin + Cypress (TypeScript) | Dự án công nghiệp (automotive); user stories thực tế từ partner company | Syntactic correctness, semantic relevance (survey), helpfulness rate, cost ($) | AutoUAT helpful 95%; Test Flow: 92% test cases helpful (60% usable as-is, 8% minor fix); ~$0.12/user story | Đánh giá dài hạn chưa thực hiện; phụ thuộc HTML code trang; chỉ 1 partner company |
| 3 | Rathnayake et al. 2026 — *BDD Scenario Generation with LLMs* — arXiv 2026 (RMIT) | GPT-4 (zero-shot best), Claude 3 (CoT best), Gemini (few-shot best) — temperature=0, top_p=1.0 | 500 user stories + BDD scenarios từ 4 sản phẩm công nghiệp (proprietary) | BLEU, METEOR, ROUGE-L, BERTScore, LLM-as-judge (DeepSeek), human expert eval | GPT-4: METEOR few-shot ≈0.75 (best text similarity); Claude 3: highest human expert rating; DeepSeek correlates strongly with human judgment | Dataset từ 1 công ty → generalizability hạn chế; dataset proprietary; LLM-based evaluation còn mới |
| 4 | Fonseca et al. 2025 — *Streamlining Acceptance Test Generation for Mobile Apps: BMW Case Study* — arXiv 2025 | DeepSeek-R1 (Gherkin), DeepSeek-Coder-V2 (Page Objects), Gemma3:1b (summary) — local via Ollama | 13 real-world issues từ BMW MyBMW app (Flutter) | Syntactic correctness rate, PageObject usable without edits (%), UI test execution rate (%), time (s) | 93.3% Gherkin syntactically correct; 78.8% PageObjects không cần sửa; 100% UI tests executed; avg. 259s/issue; >95% time saving | Chỉ 13 issues; chỉ Flutter/Dart; local LLM kém cloud models; complex widgets còn hạn chế |
| 5 | Fernandes et al. 2025 — *A Comparative Study of LLMs for Gherkin Generation* — SBES 2025 | GPT-4 Turbo, GPT-3.5, GPT-4o Mini, LLaMA 3, Phi-3 Mini, Gemini, DeepSeek R1 — zero-shot, one-shot, few-shot | Free-form test case descriptions từ 1 domain (GitHub dataset) | METEOR, coefficient of variation (CV), Shapiro-Wilk, Kruskal-Wallis, Bonferroni | GPT-4 Turbo few-shot: METEOR=0.75 (best); GPT-4o Mini & LLaMA 3: CV=4.11%/4.17% (most stable); Gemini: CV=8.11% | Chỉ dùng METEOR; không đo executability; dataset từ 1 domain |
| 6 | Santos et al. 2024 — *Increasing Test Coverage by Automating BDD Tests in POCs using LLM* — SBQS 2024 (ACM) | GPT-4 few-shot — BDD scenarios → Python test code (pytest) | 1 POC thực tế (web-based data collector, Brazil) | Code coverage (pytest-cov), test generation feasibility | Coverage target ≥60% đạt được; LLM tạo test code từ BDD thành công | Chỉ 1 POC; không so sánh nhiều LLMs; thiếu metrics định lượng chi tiết |
| 7 | Mendoza et al. 2024 — *Comparative Analysis of LLM Tools for Automated Test Data Generation from BDD* — SBES 2024 | ChatGPT-4, GitHub Copilot, Gemini — zero-shot | BDD scenarios từ dự án thực | Learning, assertiveness, response structuring, quality, representativeness, coverage (rubric) | ChatGPT-4 & Gemini tốt nhất; GPT-4 & Gemini vượt GPT-3.5 và Copilot | Chỉ đánh giá test data generation, không Gherkin generation; metrics dựa trên rubric định tính; thiếu ground truth |
| 8 | dos Santos et al. 2025 — *Automated Test Generation Using LLM Based on BDD: A Comparative Study* — ICEIS 2025 (SCITEPRESS) | ChatGPT (GPT-4), Gemini, Grok, GitHub Copilot — zero-shot | BDD scenarios thực tế từ dự án phần mềm | Similarity matrix, accuracy (Kruskal-Wallis), response length distribution | ChatGPT significantly different accuracy vs. Copilot (p<0.05); ChatGPT & Gemini > Grok & Copilot; p=0.3944 (Copilot vs. ChatGPT) | Dataset nhỏ; không đo executability; thiếu semantic evaluation |
| 9 | Paduraru et al. 2025 — *Agentic AI for BDD Testing Using LLMs* — ICAART 2025 (SCITEPRESS) | Llama3.1 8B fine-tuned + Agentic AI + NLP (human-in-the-loop) — BDDTestAIGen framework | 2 public games (Amber & Gameloft) | Framework evaluation (qualitative), computational feasibility, user-acceptance | 7B/8B model cân bằng efficiency và ease of use; BDD tests tạo được với AI autocorrection; open-source | Chỉ 2 games; thiếu quantitative metrics; human-in-the-loop giảm tự động hóa |
| 10 | Almeyda 2025 — *Engineering Prompt-Orchestrated LLM Workflows for Test Case Generation* — ICEIS 2025 | Gemini, GPT-4 — multi-step prompt orchestration | Use cases/requirements từ dự án phần mềm | Test case completeness, syntactic correctness, execution rate | Prompt orchestration cải thiện đáng kể vs. single-prompt; execution rate cao hơn | Workflow phức tạp; thiếu comparison với simpler baselines; limited scalability |
| 11 | Santos & Maciel 2024 — *AutomTest 3.0* — SBES 2024 | Generative AI (PaLM/GPT-based) — user story → test case (TDD/BDD hybrid) | User stories từ software professionals (exploratory study) | Test case quality (survey), scenario coverage, speed | "Promising results" trong coverage và speed; user feedback tích cực | Evaluation qua survey; thiếu automated metrics; không so sánh baseline LLMs |
| 12 | Adu 2024 — *Test Scenario and Case Generation with GPT-3.5-turbo* — Master Thesis (UEF) | GPT-3.5-turbo — zero-shot & few-shot + RAG; Gherkin-lint validation | BDD Gherkin scenarios (action research, iterative) | Gherkin syntax correctness (Gherkin-lint), test relevancy | Few-shot + RAG cải thiện syntax correctness đáng kể vs. zero-shot; GPT-3.5 đủ generate basic BDD | Thesis không peer-reviewed; GPT-3.5 không phải SOTA; single-domain; limited generalizability |

---

## Tóm tắt phân loại theo nội dung

| Nhóm | Papers |
|------|--------|
| **Gherkin generation từ user stories/requirements** | #1, #3, #5, #12 |
| **End-to-end: requirements → Gherkin → executable tests** | #2, #4, #10 |
| **Test data generation từ BDD scenarios** | #7, #8 |
| **BDD test code generation từ Gherkin** | #6 |
| **Agentic / framework / tool** | #9, #11 |

---

## Tóm tắt GAP rút từ cột Limitations

1. **Thiếu semantic similarity metric** — 11/12 papers không đo cosine/embedding similarity
2. **Dataset nhỏ, đơn domain, không chuẩn hóa** — 9/12 papers
3. **Không dùng Gherkin parser chuẩn hóa** — 12/12 papers
4. **GPT-4o (full, zero-shot, temperature=0) chưa được đánh giá** — 12/12 papers
