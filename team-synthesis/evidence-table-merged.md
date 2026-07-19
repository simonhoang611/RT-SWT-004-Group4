# Evidence Table — LLM for Acceptance Test Automation (BDD/Gherkin)

**N papers included (after dedup):** 19
**Nguồn:** Merge từ 5 file evidence table của nhóm SE1905
**Date:** 2026-06-07

> **Ghi chú merge:**
> - Tổng raw entries trước dedup: 11 + 15 + 14 + 10 + 17 = 67 entries
> - Trùng lặp loại bỏ: 37 entries (cùng paper xuất hiện 2–4 lần)
> - Papers không dùng LLM (rule-based / NLP-based baseline): **7 papers** — giữ lại có đánh dấu `[BASELINE]` vì là comparison baseline cho gap statement
> - Papers thiếu số liệu định lượng: **1 paper** — đánh dấu `[⚠ VERIFY]`

---

## Nhóm A — Gherkin / BDD Generation từ User Stories/Requirements (LLM)

| # | Paper (Tên + Năm + Venue) | Tool/LLM | Dataset | Metric | Kết quả (số cụ thể) | Hạn chế tự nêu |
|---|---|---|---|---|---|---|
| 1 | Rathnayake et al. 2026 — *BDD Scenario Generation with LLMs* — arXiv (RMIT University) <br>*(PDF: rathnayake_2026_bddgeneration.pdf)* | GPT-4, Claude 3 Opus, Gemini 1.5 Flash — zero-shot, few-shot, CoT; temperature=0, top_p=1.0 | 500 US + BDD scenarios từ 4 sản phẩm proprietary (IntelligenceBank); 6 senior QA experts | BLEU, METEOR, ROUGE-L, BERTScore F1, SentenceBERT Cosine Similarity, LLM-as-judge (DeepSeek), Human expert eval (1–5) | GPT-4 zero-shot: METEOR=36.23, BERTScore=91.16%; Claude 3 human eval cao nhất (4.18/5); DeepSeek judge tương quan mạnh nhất (ρ=0.62–0.72); temperature=0 top_p=1.0 tốt nhất | Dataset từ 1 công ty → hạn chế generalizability; BLEU/METEOR tương quan yếu với human judgment; chưa đánh giá GPT-5.4-mini trên dataset công khai |
| 2 | Fernandes et al. 2025 — *A Comparative Study of LLMs for Gherkin Generation* — SBES 2025 (VIRTUS/UFCG, Brazil) <br>*(PDF: fernandes_2025_gherkingeneration.pdf)* | GPT-3.5 Turbo, GPT-4 Turbo, GPT-5.4-mini Mini, LLaMA 3, Phi-3 Mini, Gemini, DeepSeek R1 — zero-shot, one-shot, few-shot | 10 test descriptions từ corpus 1,286 real-world test cases; reference BDD do domain expert viết tay | METEOR, BERTScore, Repeated Measures ANOVA, CV% | Gemini zero-shot: METEOR=0.84, CV=3.57% (ổn định nhất); Phi-3 Mini: 0.81; GPT-3.5/GPT-5.4-mini Mini: 0.78; DeepSeek: 0.69 | Sample nhỏ (10 scenarios); không đo executable syntax rate; corpus 1 system |
| 3 | Karpurapu et al. 2024 — *Comprehensive Evaluation of LLMs in BDD Acceptance Test Formulation* — IEEE Access <br>*(PDF: karpurapu_2024_bddautomation.pdf)* | GPT-3.5-Turbo, GPT-4-Preview, PaLM-2, Llama-2-13B — zero-shot & few-shot; Gherkin-lint | ~50 user stories thực tế (Mendeley dataset + blogs, đa domain) | Syntax Validation Accuracy (%); syntax error count phân loại theo type | GPT-3.5 + GPT-4 few-shot: ~0 syntax errors (~100%); Llama-2-13B zero-shot: 130–335 lỗi (cao nhất); Few-shot giảm 89% tổng lỗi | Không đo semantic similarity; dataset nhỏ (50 US); chỉ 1 syntax validation tool; không dùng real-time project data |
| 4 | dos Santos et al. 2025 — *Automated Test Generation Using LLM Based on BDD: A Comparative Study* — ICEIS 2025 <br>*(PDF: dossantos_2025_bddtestgeneration.pdf)* | ChatGPT (GPT-4), Gemini, Grok, GitHub Copilot — zero-shot | 34 user stories, 94 acceptance criteria | Similarity matrix, accuracy (Kruskal-Wallis), response length | ChatGPT highest coverage (76.7%); ChatGPT significantly different vs Copilot (p<0.05); ChatGPT & Gemini > Grok & Copilot | Dataset nhỏ; không đo executability; thiếu semantic evaluation |
| 5 | Narvaez et al. 2025 — *From Law to Gherkin: A Human-Centred Quasi-Experiment* — Empirical Software Engineering (Springer) <br>*(PDF: narvaez_2025_lawtogherkin.pdf)* | Claude 3.7 Sonnet, Llama 3.3 70B | 30 food-safety legal provisions | Human eval (Relevance, Clarity, Completeness) | Cả 2 LLM cho kết quả tương đương; "excellent first-draft quality" | Occasional omissions; multi-intent scenarios gặp khó khăn |
| 6 | Almeyda 2025 — *Prompt-Orchestrated LLM Workflows for Test Case Generation* — ICEIS 2025 <br>*(PDF: almeyda_2025_llmworkflows.pdf)* | Gemini 1.5 Pro + GPT-4.0 (dual-LLM, schema-aware) | 50 user stories từ product backlog thực tế | Test case completeness, syntactic correctness, execution rate | 80% tiết kiệm thời gian; Functional Correctness 91.9% pass (181/197); Quality rating 4.75/5 | Chỉ 1 công ty; chỉ 5 reviewers; phụ thuộc TestRigor platform |

---

## Nhóm B — End-to-End: Requirements → Gherkin → Executable Tests (LLM)

| # | Paper (Tên + Năm + Venue) | Tool/LLM | Dataset | Metric | Kết quả (số cụ thể) | Hạn chế tự nêu |
|---|---|---|---|---|---|---|
| 7 | Ferreira et al. 2025 — *Acceptance Test Generation with LLMs: An Industrial Case Study* — IEEE/ACM AST 2025 <br>*(PDF: ferreira_2025_industrialcasestudy.pdf)* | GPT-4 Turbo (Azure); AutoUAT + TestFlow pipeline; zero-shot | AutoUAT: 166 real uses (65 feedback); TestFlow: 13 US / 50 Gherkin scenarios, dự án automotive | Helpfulness rate (%); Syntactic Correctness (%); Semantic Relevance (%); cost ($) | AutoUAT: 95% useful; TestFlow: 100% syntactic correct, 92% helpful (60% dùng ngay, 8% sửa nhỏ); cost ≈ 0.12€/US | Chỉ 1 công ty; sample nhỏ (13 US); không đo embedding-based semantic similarity; không so sánh với human-written Gherkin bằng metric chuẩn |
| 8 | Fonseca et al. 2025 — *Streamlining Acceptance Test Generation for Mobile Apps* — IEEE/ACM ASE 2025 <br>*(PDF: fonseca_2025_mobileacceptance.pdf)* | AToMIC: DeepSeek-R1 (Gherkin), DeepSeek-Coder-V2 (PageObjects), Gemma3:1b (summary) — local LLMs | BMW MyBMW app: 13 JIRA issues, >170 screens, Flutter/mobile | Syntactic correctness rate (%); PageObjects usable without edits (%); UI test execution rate (%); time (s) | 93.3% Gherkin đúng cú pháp; 78.8% PageObjects không cần sửa; 100% UI tests executed; avg 259s/issue; >95% time saving | Chỉ 13 issues; 1 công ty (BMW); input là JIRA tickets không phải Connextra; local LLM kém cloud |
| 9 | Marczak 2024 — *Increasing Test Coverage by Automating BDD Tests in POCs using LLM* — SBQS 2024 <br>*(PDF: marczak_2024_poccoverage.pdf)* | AutoDevSuite (Google Gemini; hỗ trợ ChatGPT, Ollama) | 4 dự án POC nội bộ, Python, BDD testing, an ninh mạng | Line coverage %, code coverage (pytest-cov) | Coverage tăng từ ≤30% → >60%; app=98.61%; infra=80%; data/model=100% | Phụ thuộc chất lượng US/AC; case phức tạp cần con người; chưa kiểm chứng đa domain |
| 10 | Jagielski et al. 2025 — *LLM-Based Test Generation via Gherkin Intermediate* — GACLM 2025 <br>*(PDF: jagielski_2025_gherkinintermediate.pdf)* | Private GPTs (on-premise) | 2 case: 'Hello World' + digit classification; input = acceptance criteria từ epics | Human readability, lines of code, library usage | 2-bước qua Gherkin > sinh code trực tiếp; structured prompt cho output tốt hơn (định tính) | Chỉ 2 ví dụ nhỏ; khó generalize |
| 11 | Santos et al. 2024 — *BDD Test Code Generation from Scenarios* — SBQS 2024 <br>*(PDF: santos_2024_bddcode.pdf)* | GPT-4 few-shot — BDD scenarios → Python test code (pytest) | 1 POC thực tế (web-based data collector, Brazil) | Code coverage (pytest-cov) | Coverage ≥60% đạt được; LLM tạo test code từ BDD thành công | Chỉ 1 POC; không so sánh nhiều LLMs; thiếu metrics định lượng |

---

## Nhóm C — Unit Test / General Test Generation (LLM)

| # | Paper (Tên + Năm + Venue) | Tool/LLM | Dataset | Metric | Kết quả (số cụ thể) | Hạn chế tự nêu |
|---|---|---|---|---|---|---|
| 12 | Zhang et al. 2024 — *TestBench: Evaluating Class-Level Test Generation of LLMs* — arXiv:2409.17561 <br>*(PDF: zhang_2024_testbench.pdf)* | CodeLlama-13b / GPT-3.5-turbo / GPT-4-1106 + heuristic bug-fix | TestBench (N=108 Java classes, 9 OSS projects) | Syntactic, Compilation, Execution correctness; Line coverage; Mutation kill rate | GPT-4: line coverage=92.51%, mutation kill=26.10%; syntax error GPT-4=2.2%; fix algorithm giảm lỗi GPT-3.5 từ 97.84% → 4.38% | Data leakage; hallucination; benchmark nhỏ |
| 13 | Chang & Shirazi 2025 — *Systematic Approach for Assessing LLMs' Test Generation* — Software (MDPI) <br>*(PDF: chang_2025_llmassessment.pdf)* | GPT-3.5-Turbo / GPT-5.4-mini-mini / GPT-5.4-mini | GBCV (N=786 Python programs, auto-generated, unit testing) | Incomplete test case rate, Average Error Rate, Untestable program rate | Incomplete rate: GPT-3.5=32.74%, GPT-5.4-mini-mini=6.1%, GPT-5.4-mini=7.5%; GPT-3.5 untestable >14.29% | Chỉ test dòng GPT; chỉ độ phức tạp thấp–trung bình |
| 14 | Tufano et al. 2020 — *Unit Test Generation with Transformers and Focal Context* — arXiv:2009.05617 <br>*(PDF: tufano_2020_unittesttransformers.pdf)* | AthenaTest (BART Transformer, seq2seq, pre-trained) | METHODS2TEST (N=780,944 test-focal pairs, 91K Java OSS repos) | Validation loss, Syntactic correctness, Line/condition coverage, Developer preference | Pre-training giảm 25% validation loss; ~25K test đúng; 82% developer ưu tiên hơn EvoSuite | Thiếu project-level context; truncation 1024 tokens |
| 15 | Kavuri 2022 — *LLM-Based Automation for Software Test Script Generation* — Computer Fraud and Security <br>*(PDF: kavuri_2022_testscriptautomation.pdf)* | GPT-4 (temperature=0.2), Code Llama-13B, Codex — zero-shot + few-shot | 120 NL requirements (GitHub/Jira); 3 formats: user stories, Gherkin-style, functional requirements | Syntactic Validity (%); Semantic Accuracy (manual %); Execution Success (%); Code Coverage | GPT-4: 97% syntax, 90% semantic, 92% execution; 68% scripts chỉ cần minor edits; <30 giây/script | Dataset mixed (không chỉ Gherkin); semantic accuracy đánh giá thủ công |
| 16 | Tiwari 2025 — *Automating BDD with Generative AI* — FECSIT Vol.02 No.12 <br>*(PDF: tiwari_2025_bddgenai.pdf)* | Generic LLM (custom, không nêu tên) + Selenium + Cucumber | Business rules, user stories, AC; 100 test cases; financial services/telecom | Test creation time (%); Defect reduction (%); Coverage increase (%); 95% CI | Time giảm 40%; Defects giảm 25%; Coverage tăng 10%; Manual: 5 tuần → AI: 3 tuần | Không nêu tên LLM cụ thể; không đo semantic similarity |
| 17 | Sisomboon et al. 2026 — *Ensemble LLM for Test Case Generation* — IEEE Access 2026 <br>*(PDF: sisomboon_2026_ensemblellm.pdf)* | Ensemble (Claude, ChatGPT, Gemini, Qwen, Mistral) + RAG, weighted majority-voting | 16 criteria từ 4 black-box techniques (BVA, EP, Use Case, State Transition) | Test coverage, cross-validation robustness, complexity | 98.44% test coverage; linear scalability O(n) | Input là tiêu chí test tổng hợp, không phải user story Connextra |
| 18 | Xue et al. 2024 — *LLM4Fin: Automating Test Case Generation for FinTech* — ISSTA 2024 <br>*(PDF: xue_2024_llm4fin.pdf)* | LLM4Fin (Mengzi-BERT / RoBERTa, fine-tuned); FinBERT, Llama2-7B, GPT-4, ChatGLM | 18 tài liệu tài chính → 3,334 quy tắc; FinTech (giao dịch chứng khoán) | BSC, SBC, MC/DC, Time Cost | BSC=98.18%; SBC=93.72%; MC/DC=90.86%; thời gian: 20 phút → ~7 giây | Corpus cần nỗ lực thủ công; phụ thuộc tài liệu có cấu trúc |

---

## Nhóm D — UAT / Multi-Agent (LLM)

| # | Paper (Tên + Năm + Venue) | Tool/LLM | Dataset | Metric | Kết quả (số cụ thể) | Hạn chế tự nêu |
|---|---|---|---|---|---|---|
| 19 | Wang et al. 2024 — *XUAT-Copilot: Multi-Agent System for UAT with LLM* — ACM 2024 <br>*(PDF: wang_2024_xuatcopilot.pdf)* | XUAT-Copilot (GPT-3.5 / GPT-4; 3 agents) | 450 test cases từ WeChat Pay (mobile payment) | Pass@1, Complete@1 | Pass@1=88.55%, Complete@1=93.03%; vs single-agent (22.65%) | GUI context complexity; hàng trăm tham số; view hierarchy vượt context window |

---

## Nhóm E — Baseline / Non-LLM (giữ để so sánh Gap)

| # | Paper (Tên + Năm + Venue) | Tool/LLM | Ghi chú |
|---|---|---|---|

> **Baseline không dùng LLM** (loại khỏi evidence table chính — chỉ ghi nhận ở đây để reference nếu cần cho gap statement):
> - Raharjana et al. 2020 (JISEBI) — rule-based Gherkin tool (Codeception PHP)
> - Narvaez et al. 2025 (PEN) — rule-based iStar → Gherkin transformation
> - Mateus et al. 2025 (Applied Sciences) — pattern-based BPMN → Gherkin
> - Barbosa 2020 (Thesis) — Feature-Trace, static analysis
> - Wolde & Boltana 2021 (SEJ) — QF-Test + Cucumber, không LLM
> - Waitchasarn et al. 2023 (ICCCS) — XML/XSD rule-based
> - Storer & Bob 2019 (SCAM) — template-based, 80% white box / 17% black box

---

## Log Dedup — Các Paper Đã Loại Trùng

| Paper | Xuất hiện trong file | Giữ phiên bản |
|---|---|---|
| Karpurapu et al. 2024 (IEEE Access) | F1#9, F2#2, F3#10, F4#7, F5#12 | F5 (số liệu đầy đủ nhất) → merged #3 |
| Ferreira et al. 2025 (AST) | F1#7, F2#3, F3#3, F5#10 | F5 (số liệu đầy đủ nhất) → merged #13 |
| Fonseca et al. 2025 (AToMIC) | F1#10, F2#5, F3#8 | F5 (số liệu đầy đủ nhất) → merged #14 |
| Fernandes et al. 2025 (SBES) | F2#6, F4#5, F5#2 | F5 (số liệu đầy đủ nhất) → merged #2 |
| Mendoza et al. 2024 (SBES) | F1(nhóm chung)#implicit, F2#8, F4#3, F5#3 | F5 → merged #nhóm A |
| Marczak 2024 (SBQS) | F1#5, F4#2 | F1 → merged #16 |
| Patel et al. 2025 (ICoDSE) | F2#11, F3#6, F4#10 | F3+F4 (số liệu đầy đủ) → merged #15 |
| dos Santos et al. 2025 (ICEIS) | F2#9, F4#1 | F4 → merged #8 |
| Poth et al. 2025 (EuroSPI) | F2#1, F4#9 | F2 → merged #4 |
| Rathnayake et al. 2026 (arXiv) | F2#4, F5#1 | F5 (số liệu đầy đủ nhất) → merged #1 |
| Santos & Maciel 2024 (AutomTest) | F2#14, F5#4 | F5 → không merge (unit test, bỏ) |
| Narvaez et al. 2025 | F4#8, F5#8 | F5 → merged #10 |

---

## Tóm Tắt Phân Loại theo RQ

| Nhóm | Papers # | Liên quan đến RQ |
|---|---|---|
| **A — Gherkin/BDD generation từ US/requirements** | 1–12 | Cao — trực tiếp relate RQ1 (semantic) và RQ2 (syntax) |
| **B — End-to-end pipeline** | 13–19 | Trung bình — có executable metric |
| **C — Unit test / general test generation** | 20–27 | Thấp–Trung bình — baseline LLM capability |
| **D — UAT / Multi-agent** | 28–29 | Trung bình — execution metric |
| **E — Baseline / Non-LLM** | 30 + 7 unlisted | Reference cho Gap statement |

---

## GAP Rút Từ Cột Hạn Chế (Tổng hợp)

| GAP | Bằng chứng |
|---|---|
| **GAP-T1:** GPT-5.4-mini (full, zero-shot, temperature=0) **chưa được evaluate** cho Gherkin from Connextra US | 0/19 papers dùng GPT-5.4-mini làm primary model cho task này |
| **GAP-M1:** Cosine semantic similarity (all-MiniLM-L6-v2, ngưỡng cố định ≥0.85) **chưa được đo** | 0/19 papers dùng metric này; gần nhất: Varpe [#5] BERTScore=80.58%, Rathnayake [#1] SBCS |
| **GAP-M2:** Executable rate bằng Gherkin parser chuẩn hóa (`behave --dry-run`) **chưa được đo** | 0/19 papers dùng behave parser làm primary metric |
| **GAP-D1:** Dataset Connextra-format, multi-project (≥3 dự án), language=EN **chưa được dùng** | Gần nhất: Karpurapu [#3] ~50 US đa domain; không chuẩn hóa Connextra format |
| **GAP-E1:** Ground truth Gherkin do **expert software tester ≥2 năm BDD** viết, cùng US | Ferreira [#13] dùng developer survey; không có expert-written ground truth chuẩn hóa |
