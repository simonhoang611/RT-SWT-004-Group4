# Evidence Table — LLM for Acceptance Test Automation (BDD/Gherkin)

**N papers included:** 14  
**Thành viên:** Nguyễn Hiếu An (SE205060)  
**Nhóm:** SE1905 · **Database:** IEEE Xplore · **Date:** 2026-06-__

> Dữ liệu trong bảng trích từ **abstract** của paper (đã verify tên tác giả từ metadata IEEE). Ô ghi **N/A** = abstract không nêu, cần đọc full-text để xác nhận hoặc chấp nhận N/A (theo rubric: "ô N/A là bình thường").

---

| # | Paper (Tác giả + Năm + Venue) + DOI | Tool/LLM | Dataset | Metric | Kết quả (số cụ thể) | Hạn chế tự nêu |
|---|---|---|---|---|---|---|
| 1 | Sisomboon et al. 2026, IEEE Access. [doi.org/10.1109/ACCESS.2026.3667925](https://doi.org/10.1109/ACCESS.2026.3667925) | Ensemble (Claude, ChatGPT, Gemini, Qwen, Mistral) + RAG, weighted majority-voting | 16 criteria từ 4 black-box techniques (BVA, Equivalence Partitioning, Use Case, State Transition) | Test coverage, cross-validation robustness, complexity | **98.44%** test coverage; linear scalability O(n) | N/A (input là tiêu chí test tổng hợp, không phải user story Connextra) |
| 2 | Chatterjee 2025, ICICSE. [doi.org/10.1109/ICICSE66971.2025.11430054](https://doi.org/10.1109/ICICSE66971.2025.11430054) | AI synthesis engine + Cucumber/JUnit (tên LLM cụ thể: N/A — đọc full-text) | Swagger/OpenAPI specs từ internal microservices | Authoring time, negative-path coverage, spec–test alignment | Giảm authoring time + tăng negative-path coverage (abstract không nêu số → N/A, đọc Results) | N/A |
| 3 | Ferreira et al. 2025, AST (IEEE/ACM). [doi.org/10.1109/AST66626.2025.00007](https://doi.org/10.1109/AST66626.2025.00007) | GPT-4 Turbo (AutoUAT + Test Flow tools) | Real-world web apps (partner company) | Helpfulness rating (qualitative), test usability rate | **95%** scenarios helpful; **92%** test cases helpful (60% dùng trực tiếp, 8% sửa nhẹ, 24% regen) | N/A explicit (chỉ 1 công ty; không đo semantic similarity) |
| 4 | Alinezhadtilaki & Evans 2025, ICMI. [doi.org/10.1109/ICMI65310.2025.11141197](https://doi.org/10.1109/ICMI65310.2025.11141197) | BERT (đánh giá chất lượng scenario, không sinh) | BDD scenarios (size: N/A trong abstract) | Precision, Recall, F1 | **Precision = 70.1%, Recall = 80.5%, F1 = 75.3%** | N/A (raters chủ quan; chỉ detect ambiguity/inconsistency) |
| 5 | Jagielski et al. 2025, GACLM. [doi.org/10.1109/GACLM67198.2025.11232354](https://doi.org/10.1109/GACLM67198.2025.11232354) | Private GPTs (on-premise) | 2 case: 'Hello World' + digit classification model; input = acceptance criteria từ epics/stories | Human readability, lines of code, library usage | Quy trình 2 bước (qua Gherkin) > sinh code trực tiếp; structured prompt cho output tốt hơn (định tính) | Chỉ 2 ví dụ nhỏ → khó generalize |
| 6 | Patel et al. 2025, ICoDSE. [doi.org/10.1109/ICoDSE68111.2025.11351772](https://doi.org/10.1109/ICoDSE68111.2025.11351772) | LLaMA | 2 enterprise systems, 6 sprints | Authoring time reduction, coverage expansion, cost savings | **75%** giảm thời gian; **30%** mở rộng coverage; tiết kiệm **$7,725–$40,000** | Reverse-engineer từ code (không từ user story); chỉ 2 hệ thống |
| 7 | Galloy et al. 2025, ICSTW. [doi.org/10.1109/ICSTW64639.2025.10962479](https://doi.org/10.1109/ICSTW64639.2025.10962479) | LLM + SELF-INSTRUCT (sinh dataset BDD) | 2 synthetic dataset từ 175 seed chất lượng cao + 175 seed thấp | Quality criteria (completeness, single action, Gherkin syntax), inter-rater agreement | Chất lượng seed KHÔNG ảnh hưởng completeness, NHƯNG ảnh hưởng focus 1-action & tuân thủ cú pháp Gherkin | Raters bất đồng về tiêu chí riêng lẻ → quality criteria khó áp dụng |
| 8 | Fonseca et al. 2025, ASE (IEEE/ACM). [doi.org/10.1109/ASE63991.2025.00273](https://doi.org/10.1109/ASE63991.2025.00273) | Specialized LLMs (AToMIC framework) | BMW MyBMW app: 13 issues, codebase 170+ màn hình, JIRA tickets | Syntactic correctness, executable rate, time | **93.3%** Gherkin đúng cú pháp; **78.8%** PageObjects chạy không sửa; **100%** UI test chạy; <5 phút/feature | Chỉ mobile; chỉ 1 công ty (BMW); input là JIRA tickets không phải Connextra |
| 9 | Varpe et al. 2025, CASCON. [doi.org/10.1109/CASCON66301.2025.00084](https://doi.org/10.1109/CASCON66301.2025.00084) | 5 LLM zero-shot: Gemma, LLaMA3, Mistral, Phi, Qwen | PURE dataset (SRS documents) | Lexical similarity, **BERTScore (semantic)**, diversity, volume | Qwen **BERTScore F1 = 80.58%** (cao nhất); Gemma volume cao nhất | Dùng SRS không phải Connextra; không có GPT-4o; không đặt ngưỡng cố định |
| 10 | Karpurapu et al. 2024, IEEE Access. [doi.org/10.1109/ACCESS.2024.3391815](https://doi.org/10.1109/ACCESS.2024.3391815) | GPT-3.5, GPT-4, Llama-2-13B, PaLM-2 (zero + few-shot) | Dataset BDD acceptance test (size: N/A trong abstract — đọc Method) | Syntax error rate, validation accuracy | GPT-3.5 & GPT-4 sinh BDD **error-free**; few-shot accuracy > zero-shot | Paper tự nêu "có limitations" nhưng abstract không chi tiết → đọc Limitations |
| 11 | Waitchasarn et al. 2023, ICCCS. [doi.org/10.1109/ICCCS57501.2023.10151185](https://doi.org/10.1109/ICCCS57501.2023.10151185) | XML/XSD rule-based (KHÔNG dùng LLM — baseline) | UI structures web page; user stories + scenarios | Maintenance effort reduction | Giảm mạnh maintenance effort (abstract không nêu số → N/A, đọc Results) | N/A (rule-based, không AI) |
| 12 | Lee et al. 2023, SNPD-Winter. [doi.org/10.1109/SNPD-Winter57765.2023.10223873](https://doi.org/10.1109/SNPD-Winter57765.2023.10223873) | Generative AI model làm "compiler" | N/A (human-language UI test automation) | N/A | ⚠️ **N/A — abstract KHÔNG có số liệu** | N/A |
| 13 | Wang et al. 2022, IEEE TSE (UMTG). [doi.org/10.1109/TSE.2020.2998503](https://doi.org/10.1109/TSE.2020.2998503) | UMTG (NLP-based, KHÔNG dùng LLM — baseline) | 2 industrial case studies; use case specs (safety-critical) | % use case steps → formal constraints; scenario coverage | **95%** use case steps dịch đúng thành formal constraints; phủ tất cả expert scenarios + vài critical scenario mới | Use case không phải Connextra; cần domain model |
| 14 | Storer & Bob 2019, SCAM (behave_nicely). [doi.org/10.1109/SCAM.2019.00033](https://doi.org/10.1109/SCAM.2019.00033) | Template-based (rule-based, KHÔNG dùng LLM — baseline) | 20 white box + 50 black box projects (GitHub) | Generation success rate | **80%** success white box; **17%** success black box | Template-based; kém với black box; không hỗ trợ NL phức tạp |

---

## ⚠️ Cảnh báo về paper #12 (Lee et al. 2023)

Abstract paper này **không có bất kỳ con số kết quả nào** → có thể **không thỏa IC-E** ("có ít nhất 1 con số trong Table/Figure"). Bạn **bắt buộc đọc full-text**: nếu trong paper có số liệu thực nghiệm thì giữ INCLUDE và điền số; nếu không có → đổi `v2_decision` thành **Exclude** với lý do **EC-N** (no empirical). Nếu loại, final list còn 13 paper (vẫn đạt 5–15).

---

## Đọc bảng theo CỘT → GAP (cho gap-statement.md)

- **Cột Tool/LLM:** đã dùng GPT-3.5/4/4-Turbo, Claude, Gemini, LLaMA/Llama-2/LLaMA3, PaLM-2, Gemma, Mistral, Phi, Qwen, BERT + baseline NLP/template. **CHƯA ai dùng GPT-4o.** → GAP-T
- **Cột Metric:** chỉ #9 (Varpe) dùng BERTScore semantic; #8 (Fonseca), #10 (Karpurapu) đo executable/syntax. **KHÔNG ai kết hợp cosine semantic similarity (ngưỡng cố định) + executable rate trên Connextra.** → GAP-M
- **Cột Dataset:** OpenAPI specs, SRS, JIRA tickets, use case specs, GitHub projects. **KHÔNG ai dùng user story Connextra chuẩn.** → GAP-D

---

## Checklist Checkpoint 1.5 (rubric cô)

- [x] Mỗi paper có link DOI
- [x] Tool/LLM ghi tên cụ thể (không ghi "AI" chung — chỗ chưa rõ ghi "N/A — đọc full-text")
- [x] Metric ghi tên cụ thể (BERTScore, F1, syntactic correctness... không ghi "accuracy" chung)
- [x] Cột Kết quả có số ở phần lớn paper (98.44%, 95%, 80.58%, 75.3%, 93.3%, 80%...)
- [x] Có ô N/A (đúng tinh thần "ô trống là bình thường khi làm thật")

> **Việc bắt buộc trước khi nộp:** Đọc full-text để (1) xác nhận paper #12 có thỏa IC-E không, (2) điền số cho #2, #11 (đang N/A), (3) lấy dataset size cho #4, #10, (4) verify lại tất cả con số trong Table/Figure gốc.
