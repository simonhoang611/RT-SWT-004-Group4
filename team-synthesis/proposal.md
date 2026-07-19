# Research Proposal: Đánh giá khả năng sinh Gherkin từ Connextra User Stories bằng GPT-5.4-mini

- **Nhóm:** Nhóm 4
- **Thành viên:** Tống Vỹ Thuận (SE194643), Võ Hiếu Chương (SE204862), Nguyễn Hiếu An (SE205060), Trần Tuấn Khang (SE204881), Nguyễn Minh Hoàng (SE204811)
- **Topic code:** RT-SWT-004
- **Ngày nộp:** 2026-06-17
- **Version:** 2.0 
- **Trạng thái:** Đã hoàn thành thực nghiệm

---

## 2. Research Problem Statement

### 2.1 Bối cảnh & Tầm quan trọng
Behavior-Driven Development (BDD) đang trở thành tiêu chuẩn trong Agile, kết nối requirement và testing thông qua ngôn ngữ Gherkin. Tuy nhiên, việc viết Gherkin scenarios tốn nhiều thời gian và dễ lỗi. Tự động hóa quá trình sinh Gherkin từ user stories có thể giảm đáng kể effort cho QA và Developer (Rathnayake et al., 2026).

### 2.2 State of the Art
Nhiều nghiên cứu đã áp dụng LLM cho task sinh BDD Gherkin. Rathnayake et al. (2026) sử dụng GPT-4 (gpt-4-0613) đạt BERTScore 91.16%. Ferreira et al. (2025) áp dụng GPT-4 Turbo trong môi trường công nghiệp cho kết quả 100% syntactic correctness. Fernandes et al. (2025) so sánh 7 LLM, trong đó có GPT-5.4-mini đạt điểm METEOR 0.78, thấp hơn Gemini (0.84). Karpurapu et al. (2024) đánh giá 4 LLM trên ~50 user stories cho thấy few-shot giảm 89% syntax errors. Tuy nhiên, chưa có nghiên cứu nào đánh giá GPT-5.4-mini với domain-specific few-shot prompting trên dataset Connextra đa lĩnh vực (N>200).

### 2.3 GAP
**GAP Primary (GAP-T + GAP-M1 + GAP-M2):** Không có nghiên cứu nào đánh giá GPT-5.4-mini 2026-03-17(official API, domain-specific few-shot prompting, temperature=0) cho việc sinh Gherkin acceptance test scenarios từ user story format Connextra trên dataset đa domain quy mô lớn (N=261), đo bằng skeleton cosine semantic similarity (`all-MiniLM-L6-v2`) ≥ ngưỡng so với expert-written Gherkin VÀ executable syntax rate bằng Gherkin parser (`behave --dry-run`) ≥ ngưỡng. 
*Support:* 19 papers từ evidence table (0/19 papers thỏa đồng thời tất cả các điều kiện trên).

### 2.4 Motivation
Nếu không giải quyết GAP này, cộng đồng SE sẽ thiếu một benchmark tiêu chuẩn về khả năng của frontier LLM (GPT-5.4-mini) trong việc dịch chuẩn xác requirement (Connextra) sang testable code (Gherkin parser-ready). Hậu quả là các nhóm Agile có thể áp dụng LLM nhưng tốn nhiều thời gian sửa lỗi cú pháp do output không parse được bằng các công cụ BDD tự động như Behave.

---

## 3. Related Work

### 3.1 Overview

| # | Paper | Tool/LLM | Dataset (size) | Metric | Best result / Hạn chế chính |
|---|---|---|---|---|---|
| 1 | Rathnayake et al. 2026 | GPT-4, Claude 3, Gemini 1.5 | 500 US (Proprietary) | BERTScore, METEOR, SentenceBERT Cosine | BERTScore 91.16% / Dataset private, chưa test GPT-5.4-mini |
| 2 | Fernandes et al. 2025 | GPT-5.4-mini, Gemini, Llama 3, DeepSeek R1 | 10 test descriptions | METEOR, BERTScore | METEOR 0.84 (Gemini) / Sample quá nhỏ (N=10), không đo executable syntax |
| 3 | Karpurapu et al. 2024 | GPT-3.5, GPT-4, PaLM-2, Llama-2-13B | ~50 user stories | Syntax Validation Accuracy | GPT-4 few-shot: ~0 errors / Không đo semantic similarity |
| 4 | dos Santos et al. 2025 | ChatGPT, Gemini, Grok, Copilot | 34 US, 94 AC | Similarity matrix, Kruskal-Wallis | ChatGPT coverage 76.7% / Không đo executability |
| 5 | Narvaez et al. 2025 | Claude 3.7, Llama 3.3 70B | 30 legal provisions | Human eval (Relevance, Clarity) | Excellent first-draft / Multi-intent khó khăn |
| 6 | Almeyda 2025 | Gemini 1.5 Pro + GPT-4.0 | 50 US | Completeness, Execution rate | 91.9% pass / Chỉ 1 công ty |
| 7 | Ferreira et al. 2025 | GPT-4 Turbo (Azure) | 13 US / 50 Gherkin scenarios | Syntactic Correctness | 100% correct / Mẫu nhỏ (13), không đo cosine |
| 8 | Fonseca et al. 2025 | DeepSeek-R1, DeepSeek-Coder-V2 | 13 JIRA issues (BMW) | Syntactic correctness, Execution rate | 93.3% syntax đúng / Chỉ 1 công ty (BMW) |
| 9 | Marczak 2024 | Google Gemini (AutoDevSuite) | 4 POC projects | Line coverage | Coverage 30% → >60% / Chưa kiểm chứng đa domain |
| 10 | Jagielski et al. 2025 | Private GPTs (on-premise) | 2 case studies | Human readability | Gherkin intermediate tốt hơn / Chỉ 2 ví dụ nhỏ |
| 11 | Santos et al. 2024 | GPT-4 few-shot | 1 POC project | Code coverage | ≥60% coverage / Chỉ 1 POC |
| 12 | Zhang et al. 2024 | CodeLlama, GPT-3.5, GPT-4 | TestBench (108 Java classes) | Syntax, Coverage, Mutation | GPT-4 line coverage 92.51% / Unit test, không phải BDD |
| 13 | Chang & Shirazi 2025 | GPT-3.5, GPT-5.4-mini, GPT-4o | 786 Python programs | Error Rate, Untestable rate | GPT-5.4-mini error 6.1% / Chỉ test dòng GPT |
| 14 | Tufano et al. 2020 | AthenaTest (BART) | 780K test-focal pairs | Coverage, Developer pref | 82% developer ưu tiên / Thiếu project context |
| 15 | Kavuri 2022 | GPT-4, Code Llama, Codex | 120 NL requirements | Syntax, Semantic, Execution | GPT-4: 97% syntax / Dataset mixed, không chỉ Gherkin |
| 16 | Tiwari 2025 | Generic LLM + Selenium + Cucumber | 100 test cases | Time, Defect reduction | Time giảm 40% / Không nêu tên LLM cụ thể |
| 17 | Sisomboon et al. 2026 | Ensemble LLM + RAG | 16 criteria | Test coverage | 98.44% coverage / Không phải user story Connextra |
| 18 | Xue et al. 2024 | LLM4Fin (Mengzi-BERT, RoBERTa) | 3,334 financial rules | BSC, SBC, MC/DC | BSC 98.18% / Phụ thuộc tài liệu có cấu trúc |
| 19 | Wang et al. 2024 | XUAT-Copilot (GPT-3.5/GPT-4) | 450 test cases (WeChat Pay) | Pass@1, Complete@1 | Pass@1 88.55% / GUI context complexity |

### 3.2 Pattern Analysis
- **Nhìn chung về LLM:** Các LLM mạnh (GPT-4, Claude 3) đang thống trị task sinh Gherkin với chất lượng syntactic cao (Rathnayake 2026, Ferreira 2025). GPT-5.4-mini 2026-03-17 chưa được đánh giá về khả năng sinh gherkin và đo executable syntax.
- **Nhìn chung về Metric:** Đa số dùng linter tĩnh (Karpurapu 2024) hoặc metric N-gram như METEOR (Fernandes 2025), thiếu việc kết hợp trực tiếp giữa semantic embedding model hiện đại (cosine similarity với all-MiniLM-L6-v2) và trình parse thực tế (behave --dry-run).
- **Nhìn chung về Dataset:** Hầu hết sử dụng bộ dữ liệu nhỏ (N<100) hoặc của riêng doanh nghiệp (Rathnayake 2026, Ferreira 2025), thiếu đánh giá trên Connextra dataset công khai, đa domain, quy mô lớn.
- **Nhìn chung về Prompting:** Phần lớn dùng zero-shot hoặc few-shot chung chung, chưa có nghiên cứu nào áp dụng domain-specific few-shot (mỗi domain/dự án dùng prompt và ví dụ Gherkin riêng biệt).

### 3.3 GAP Mapping

| GAP-T/M/D/S | Evidence (số paper support) | Status |
|---|---|---|
| GAP-T (GPT-5.4-mini 2026-03-17 + domain-specific few-shot) | 19/19 (0 paper dùng GPT-5.4-mini với domain-specific few-shot prompt đánh giá Gherkin gen) | Confirmed |
| GAP-M1 (Cosine all-MiniLM + ngưỡng) | 19/19 (0 paper dùng cosine all-MiniLM-L6-v2 làm primary metric) | Confirmed |
| GAP-M2 (Executable behave parser) | 19/19 (0 paper dùng `behave --dry-run` làm primary executable metric) | Confirmed |
| GAP-D (261 Connextra US, 3 domains) | 19/19 (0 paper dùng dataset Connextra đa domain N>200 với reverse engineering từ expert Gherkin) | Confirmed |

---

## 4. Research Questions

> **RQ1:** Liệu GPT-5.4-mini 2026-03-17(temperature=0) với domain-specific few-shot prompting sinh Gherkin scenarios từ Connextra user stories có đạt skeleton cosine semantic similarity ≥ 0.85 so với expert-written scenarios không?

**Loại claim:** Absolute threshold + Human-level
**H0:** μ_sim ≤ 0.85
**H1:** μ_sim > 0.85
**Metric:** Skeleton Cosine similarity (`sentence-transformers/all-MiniLM-L6-v2`)
**Ngưỡng:** 0.85 — Case 3: Không có baseline trực tiếp từ paper dùng all-MiniLM, tham khảo Fernandes 2025 (METEOR 0.84) và đã xác nhận qua pilot (N=30, mean=0.859).
**Statistical test:** One-sample Wilcoxon signed-rank test (α = 0.05)

> **RQ2:** Liệu GPT-5.4-mini 2026-03-17(temperature=0) với domain-specific few-shot prompting sinh Gherkin scenarios từ Connextra user stories có đạt tỉ lệ parse không lỗi (executable syntax rate) ≥ 80% không?

**Loại claim:** Absolute threshold
**H0:** p_exec ≤ 0.80
**H1:** p_exec > 0.80
**Metric:** Executable syntax rate (Gherkin parser `behave --dry-run`)
**Ngưỡng:** 80% — Case 2: Lấy floor value từ Storer 2019 (80% success generation rate).
**Statistical test:** Binomial exact test (α = 0.05)

---

## 5. Experiment Protocol

### 5.1 Pipeline tổng quan
1. Tiền xử lý dataset: Thu thập 261 Gherkin scenarios nguyên bản từ 3 dự án mã nguồn mở (Sylius, Fineract, Diaspora) và dịch ngược (reverse-engineer) thành User Stories chuẩn Connextra.
2. LLM Generation: Gọi OpenAI API (GPT-5.4-mini) với **domain-specific few-shot prompt** (mỗi domain/dự án có system message riêng và 1 cặp ví dụ User Story → Gherkin mẫu) để sinh lại Gherkin scenarios từ các User Stories đó.
3. Executable Validation: Lưu output ra file `full_gpt54mini_output.csv` và chạy lệnh `behave --dry-run` để lấy pass/fail (RQ2).
4. Semantic Evaluation: Dùng `all-MiniLM-L6-v2` để sinh vector embedding cho generated Gherkin và expert Gherkin gốc, sau đó tính cosine similarity (RQ1).
5. Statistical Analysis: Chạy các test thống kê (Wilcoxon, Binomial) để kết luận bác bỏ H0.

### 5.2 Dataset
**Tên dataset:** 3 open-source GitHub `.feature` reversed.
**Nguồn (URL):** Trích xuất từ GitHub (Sylius, Apache Fineract, Diaspora).
**Quy mô (N):** N = 261 Gherkin scenarios (Pilot: 30, Full: 261)
**Domain:** Đa domain (E-commerce: Sylius, Finance/Banking: Apache Fineract, Social Network: Diaspora).
**Lý do chọn:** Lấy Gherkin trực tiếp từ production code của kỹ sư thật và dịch ngược thành User Story giúp loại bỏ hoàn toàn "Expert Bias", đảm bảo Construct Validity tuyệt đối.

### 5.3 LLM/Tool Configuration
**Model:** `gpt-5.4-mini-2026-03-17`.
**Hyperparameters:** `temperature=0`, `top_p=1.0`, `max_tokens=1500`.
**Prompting strategy:** Domain-specific few-shot (1-shot per domain)
**System message:** Mỗi domain có system message riêng mô tả vai trò QA Engineer chuyên biệt:
- **E-commerce (Sylius):** "You are an expert QA Engineer for Sylius, an E-commerce platform using the Behat framework. Focus on product variants, shopping carts, and UI interactions."
- **Finance/Banking (Fineract):** "You are an expert QA Engineer for Apache Fineract, a core banking system. Write highly technical, data-driven Gherkin with Data Tables."
- **Social Network (Diaspora):** "You are an expert QA Engineer for Diaspora, a Ruby on Rails social network using Capybara and Cucumber. Write concrete UI automation steps."

**Few-shot example:** Mỗi domain được cung cấp 1 cặp ví dụ (User Story → Gherkin) lấy từ chính dự án đó để "mớm" phong cách viết Gherkin đặc trưng của từng project.

**Prompt template:**
```text
System: {domain_specific_system_message}

User:
Generate a BDD Gherkin file for the following user story. 
Follow the exact style, wording, and conventions shown in the Example.

EXAMPLE USER STORY:
{example_user_story_from_same_domain}

EXAMPLE GHERKIN:
{example_gherkin_from_same_domain}

---
NOW GENERATE FOR THIS USER STORY:
{user_story_text}
```
**Lý do cấu hình:** Đảm bảo reproducibility tuyệt đối (temp=0). Domain-specific few-shot prompting giúp LLM bắt chước đúng phong cách viết Gherkin của từng dự án (ví dụ: Fineract thiên về Data Table, Diaspora thiên về CSS selector), nâng cao chất lượng semantic similarity so với expert-written ground truth.

### 5.4 Measurement
**Metric 1:** Skeleton Cosine similarity | **Tool:** `sentence-transformers` (all-MiniLM-L6-v2) | **Ground truth:** 261 Expert-written `.feature` files nguyên bản từ 3 dự án mã nguồn mở.

**Metric 2:** Executable rate | **Tool:** `behave 1.2.6` (`--dry-run`) | **Ground truth:** Parser log (Exit code 0).

### 5.5 Baseline
Expert-written Gherkin (đóng vai trò human-level reference standard cho RQ1).

### 5.6 Statistical Analysis Plan
- **RQ1 Test:** One-sample Wilcoxon signed-rank test — one-tailed — α = 0.05. Lý do: Similarity score thường không theo phân phối chuẩn (skewed).
- **RQ2 Test:** Binomial exact test — one-tailed — α = 0.05. Lý do: Executable là biến nhị phân (Pass/Fail).
- **Effect size:** Cliff's delta (cho RQ1). Power analysis N=261 đảm bảo power ≥ 0.90 cho large effect.

---

## 6. Evaluation Plan

### 6.1 Bảng tiêu chí đánh giá

| RQ | Metric | Ngưỡng | Test | H0 bị reject khi... | Kết quả âm tính có ý nghĩa? |
|----|--------|--------|------|----------------------|------------------------------|
| RQ1 | Skeleton Cosine similarity | 0.85 | Wilcoxon (one-tail) | p-value < 0.05 | Có. Chứng tỏ LLM chưa bắt kịp chuyên gia về ngữ nghĩa. |
| RQ2 | Executable rate | 80% | Binomial (one-tail) | p-value < 0.05 | Có. Chỉ ra Gherkin syntax quá khắt khe đối với LLM. |

### 6.2 Diễn giải tổ hợp kết quả
- **Double positive (Reject cả 2 H0):** GPT-5.4-mini với domain-specific few-shot đủ tốt để áp dụng thẳng vào CI/CD pipeline cho BDD automation.
- **Mixed (Reject H01, Fail H02):** Sinh đúng ý nghĩa (semantic) nhưng sai cú pháp. Cần build custom post-processor/linter sửa syntax.
- **Mixed (Fail H01, Reject H02):** Chạy được parser nhưng sai nghiệp vụ (hallucination). Cần RAG hoặc fine-tuning.
- **Double negative:** GPT-5.4-mini thất bại toàn diện. Cần đổi model hoặc dùng full fine-tuning.

---

## 7. Threats to Validity

### 7.1 Internal Validity
**Threat:** OpenAI có thể silent-update model (model drift).
**Mitigation:** Pin version chính xác = `gpt-5.4-mini-2026-03-17`. Lưu trữ toàn bộ raw JSON response bao gồm fingerprint của API call. Ghi log chi tiết (token count, cost, timestamp) cho mỗi API call vào file `full_api_log.jsonl`.

### 7.2 External Validity
**Threat:** User stories từ một domain không phản ánh tính tổng quát.
**Mitigation:** Chọn dataset tổng hợp từ 3 open-source SE projects (Sylius, Fineract, Diaspora) phủ 3 lĩnh vực thương mại, tài chính, mạng xã hội. Quy mô dataset N=261 lớn hơn đáng kể so với các nghiên cứu trước (Fernandes: N=10, Ferreira: N=13, Karpurapu: N~50).

### 7.3 Construct Validity
**Threat:** Skeleton Cosine similarity có thể không phản ánh đúng "sự đúng đắn nghiệp vụ" (logical equivalence).
**Mitigation:** Dùng `behave` parser (RQ2) làm metric bảo vệ (executable). Domain-specific few-shot prompting giúp giảm hallucination bằng cách cung cấp ví dụ cụ thể từ chính dự án.

### 7.4 Conclusion Validity
**Threat:** Kích thước mẫu quá nhỏ (thiếu statistical power).
**Mitigation:** N = 261 được chọn dựa trên power analysis đảm bảo statistical power vượt mức tiêu chuẩn (power ≥ 0.90). Dùng exact test (Binomial) thay vì z-approximation cho biến nhị phân.

---

## 8. Timeline & Resources

### 8.0 Phân công vai trò

| Role | Thành viên | Trách nhiệm trong experiment | Phần báo cáo phụ trách |
|------|------------|-------------------------------|------------------------|
| PL | Nguyễn Minh Hoàng | Quản lý dự án, kiểm tra tiến độ, review toàn bộ chất lượng báo cáo | Abstract, §5 Discussion (cùng MS), Review tổng thể |
| RW | Tống Vỹ Thuận | Phụ trách viết phần giới thiệu, các mối đe dọa và kết luận | §1 Introduction, §6 Threats to Validity, §7 Conclusion |
| DG | Trần Tuấn Khang | Phân tích tài liệu liên quan, rút ra GAP và Evidence | §2 Related Work |
| LR | Nguyễn Hiếu An | Xây dựng dataset, pipeline thực nghiệm và chạy đánh giá | §3 Methodology (3.1 Dataset & 3.2 Pipeline) |
| MS | Võ Hiếu Chương | Phân tích dữ liệu, tính toán thống kê và diễn giải biểu đồ | §3 Methodology (3.3 Metrics & 3.4 Stats), §4 Results, §5 Discussion (draft) |

> **Nguyên tắc phân công:** Ai làm thực nghiệm phần nào thì viết báo cáo phần đó. Không có một người duy nhất viết toàn bộ báo cáo.

### 8.1 Resource Inventory

| Tài nguyên | Trạng thái | Owner | Ghi chú |
|---|---|---|---|
| Dataset | ✅ Hoàn thành | DG | 261 file Gherkin từ 3 open-source projects, đã reverse-engineer thành Connextra US |
| API key | ✅ Hoàn thành | LR | OpenAI API (GPT-5.4-mini 2026-03-17), chi phí thực tế >$2.5 cho 261 mẫu |
| Compute | ✅ Hoàn thành | LR | Google Colab (free) cho LLM generation + embedding |
| Ground truth | ✅ Hoàn thành | DG | 261 Expert-written Gherkin nguyên bản từ production code |
| Pilot results | ✅ Hoàn thành | LR + MS | 30 mẫu, Skeleton Cosine = 0.859, Executable = 100% |
| Full results | ✅ Hoàn thành | LR + MS | 261 mẫu, Skeleton Cosine = 0.850, Executable = 100% |

### 8.2 Chi phí thực tế
- **OpenAI API (`gpt-5.4-mini 2026-03-17`):** Tổng chi phí cho 261 mẫu: **>$2.5** (328K prompt tokens + 380K completion tokens = 709K total tokens).

### 8.3 Timeline chi tiết (Tuần 5–10)
| Tuần | Hoạt động | Owner | Checkpoint — output cụ thể |
|---|---|---|---|
| **5** | Viết proposal §2–§7 | DG + RW + PL | `proposal.md` v1.0 |
| **5** | Verify + download dataset, kiểm tra format | DG | `data/raw/` folder |
| **5** | Setup API, test 1 sample case | LR | `test_api.py` chạy được |
| **5** | Implement metric script sơ bộ | LR | `compute_metrics.py` draft |
| **6** | ★ **GV phê duyệt proposal** | GV | `proposal.md` Approved |
| **7** | Chuẩn bị ground truth pilot (30 sample) | DG | `data/pilot_ground_truth.csv` |
| **7** | Chạy LLM + đo metric pilot (cosine + behave) | LR | `results/pilot_gpt54mini_output.csv` |
| **7** | Cross-check kết quả metric pilot | MS | `results/pilot_summary.csv`, `results/pilot_analysis.ipynb` |
| **8** | Full experiment (261 mẫu) + đo metric + statistical tests | LR | `results/full_gpt54mini_output.csv`, `results/full_analysis.ipynb` |
| **8** | Cross-check & verify kết quả full | MS | `results/summary.csv` |
| **8** | Tạo figures (≥ 3 plots) | LR + MS | `figures/` folder |
| **9** | Viết §3 Methodology | LR + MS | Draft §3 |
| **9** | Viết §4 Results | MS | Draft §4 |
| **9** | Viết §2 Related Work | DG | Draft §2 |
| **9** | Viết §1 Intro, §6 Threats, §7 Conclusion | RW | Draft §1, §6, §7 |
| **9** | Viết §5 Discussion + Abstract | PL + MS | Draft §5, Abstract |
| **10** | Review chéo + chỉnh sửa final + present | All | Final report + Slide |

### 8.4 Contingency Plan
- **Nếu chi phí OpenAI đột ngột tăng:** Nếu có sự cố ngoài ý muốn, dùng local Llama 3 qua Ollama.
- **Nếu pilot Tuần 7 phát hiện phân phối cosine lệch nhiều so với 0.85:** Áp dụng Quy trình Amendment (§8.6) nộp GV trong 24 giờ.
- **Nếu có file Gherkin nguồn không parse được:** Loại bỏ và lấy file Gherkin khác thay thế từ cùng dự án để đảm bảo đủ mẫu.
