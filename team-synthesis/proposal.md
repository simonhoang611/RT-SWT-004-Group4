# Research Proposal: Đánh giá khả năng sinh Gherkin từ Connextra User Stories bằng GPT-4o

- **Nhóm:** Nhóm 4
- **Thành viên:** Tống Vỹ Thuận (SE194643), Võ Hiếu Chương (SE204862), Nguyễn Hiếu An (SE205060), Trần Tuấn Khang (SE204881), Nguyễn Minh Hoàng (SE204811)
- **Topic code:** RT-SWT-004
- **Ngày nộp:** 2026-06-17
- **Version:** 1.0
- **Trạng thái:** Đang chờ phê duyệt

---

## 2. Research Problem Statement

### 2.1 Bối cảnh & Tầm quan trọng
Behavior-Driven Development (BDD) đang trở thành tiêu chuẩn trong Agile, kết nối requirement và testing thông qua ngôn ngữ Gherkin. Tuy nhiên, việc viết Gherkin scenarios tốn nhiều thời gian và dễ lỗi. Tự động hóa quá trình sinh Gherkin từ user stories có thể giảm đáng kể effort cho QA và Developer (Rathnayake et al., 2026).

### 2.2 State of the Art
Nhiều nghiên cứu đã áp dụng LLM cho task sinh BDD Gherkin. Rathnayake et al. (2026) sử dụng GPT-4 (gpt-4-0613) đạt BERTScore 91.16%. Ferreira et al. (2025) áp dụng GPT-4 Turbo trong môi trường công nghiệp cho kết quả 100% syntactic correctness. Fernandes et al. (2025) so sánh 7 LLM, trong đó có GPT-4o Mini đạt điểm METEOR 0.78, thấp hơn Gemini (0.84). Varpe et al. (2025) đạt BERTScore F1 80.58% với Qwen trên dataset SRS. Tuy nhiên, chưa có nghiên cứu nào dùng GPT-4o bản full.

### 2.3 GAP
**GAP Primary (GAP-T + GAP-M1 + GAP-M2):** Không có nghiên cứu nào đánh giá GPT-4o (full version, official API, zero-shot, temperature=0) cho việc sinh Gherkin acceptance test scenarios từ user story format Connextra, đo bằng cosine semantic similarity (`all-MiniLM-L6-v2`) ≥ ngưỡng so với expert-written Gherkin VÀ executable syntax rate bằng Gherkin parser (`behave --dry-run`) ≥ ngưỡng. 
*Support:* 13 papers từ evidence table.

### 2.4 Motivation
Nếu không giải quyết GAP này, cộng đồng SE sẽ thiếu một benchmark tiêu chuẩn về khả năng của frontier LLM (GPT-4o) trong việc dịch chuẩn xác requirement (Connextra) sang testable code (Gherkin parser-ready). Hậu quả là các nhóm Agile có thể áp dụng LLM nhưng tốn nhiều thời gian sửa lỗi cú pháp do output không parse được bằng các công cụ BDD tự động như Behave.

---

## 3. Related Work

### 3.1 Overview

| Paper | Tool/LLM | Dataset (size) | Metric | Best result / Hạn chế chính |
|---|---|---|---|---|
| Rathnayake et al. 2026 | GPT-4, Claude 3, Gemini 1.5 | 500 US (Proprietary) | BERTScore, METEOR | BERTScore 91.16% / Dataset private, chưa có GPT-4o full |
| Fernandes et al. 2025 | GPT-4o Mini, Gemini, Llama 3 | 10 test descriptions | METEOR, BERTScore | METEOR 0.84 / Sample quá nhỏ (N=10), không đo executable syntax |
| Ferreira et al. 2025 | GPT-4 Turbo | 13 US (Automotive) | Syntactic Correctness | 100% correct / Mẫu rất nhỏ (13), dùng GPT-4 Turbo, không đo cosine |
| Varpe et al. 2025 | Qwen, Llama 3, Mistral | PURE dataset | BERTScore F1 | 80.58% / Không dùng chuẩn Connextra, không test GPT-4o |
| Sami et al. | Các LLM mã nguồn mở | BDD Requirements | BLEU, ROUGE | Thiếu đánh giá semantic (cosine) và executable metric bằng parser |
| Rahman et al. | LLM-based Automator | User Stories | Độ bao phủ | Tập trung sinh test case logic, không focus vào BDD Gherkin syntax |
| FECSIT 2025 | Generative AI models | Agile specs | Efficiency rate | Đánh giá tốc độ là chính, bỏ qua semantic accuracy so với expert |
| Santos (AutomTest 3.0)| AutomTest 3.0 (LLMs) | User Stories | Code Quality | Focus vào unit/integration tests, không đo Gherkin executable |
| Agile Test Cloud | Custom LLM prompt | Cloud specs | Defect Rate | Domain hẹp (Cloud services), không đánh giá LLM cơ sở (GPT-4o) |
| Mendoza et al. | LLM BDD Tools | Gherkin BDD | Automation Rate | Tập trung sinh test data, không phải sinh Gherkin scenarios từ US |
| Narvaez et al. 2025 | iStar extensions | iStar requirements | Accuracy | Tập trung sinh acceptance criteria, không đo executable BDD |
| Kavuri | LLM Automation | Test scripts | Pass rate | Sinh Selenium/Appium scripts, không đo semantic của Gherkin |
| Raharjanar 2020 | BDD Gen Tool | BDD Specs | Thời gian sinh | Dùng phương pháp NLP cũ, chưa khai thác frontier LLMs như GPT-4o |

### 3.2 Pattern Analysis
- **Nhìn chung về LLM:** Các LLM mạnh (GPT-4) đang thống trị task sinh Gherkin với chất lượng syntactic cao, thể hiện qua Rathnayake (2026) và Ferreira (2025). Tuy nhiên, evaluation thường dùng các phiên bản LLM cũ hơn GPT-4o.
- **Nhìn chung về Metric:** Đa số dùng linter tĩnh (Karpurapu 2024) hoặc metric N-gram như METEOR (Fernandes 2025), thiếu việc kết hợp trực tiếp giữa một semantic embedding embedding model hiện đại (cosine similarity) và trình parse thực tế (behave).
- **Nhìn chung về Dataset:** Hầu hết sử dụng bộ dữ liệu nhỏ hoặc của riêng doanh nghiệp (Rathnayake 2026, Ferreira 2025), thiếu đánh giá trên Connextra dataset công khai.

### 3.3 GAP Mapping

| GAP-T/M/D/S | Evidence (số paper support) | Status |
|---|---|---|
| GAP-T (GPT-4o) | 13/13 (0 paper dùng GPT-4o bản full đánh giá Gherkin gen) | Confirmed |
| GAP-M1 (Cosine all-MiniLM + ngưỡng) | 13/13 (0 paper dùng cosine all-MiniLM-L6-v2 làm primary metric) | Confirmed |
| GAP-M2 (Executable behave parser) | 13/13 (0 paper dùng `behave --dry-run` làm primary executable metric) | Confirmed |
| GAP-D (100 Expert Gherkin Reversed) | 13/13 (0 paper dùng reverse engineering từ expert Gherkin để tránh bias) | Confirmed |

---

## 4. Research Questions

> **RQ1:** Liệu GPT-4o zero-shot (temperature=0) sinh Gherkin scenarios từ Connextra user stories có đạt cosine semantic similarity ≥ 0.85 so với expert-written scenarios không?

**Loại claim:** Absolute threshold + Human-level
**H0:** μ_sim ≤ 0.85
**H1:** μ_sim > 0.85
**Metric:** Cosine similarity (`sentence-transformers/all-MiniLM-L6-v2`)
**Ngưỡng:** 0.85 — Case 3: Không có baseline trực tiếp từ paper dùng all-MiniLM, tham khảo Fernandes 2025 (METEOR 0.84) và cần xác nhận qua pilot.
**Statistical test:** One-sample Wilcoxon signed-rank test (α = 0.05)

> **RQ2:** Liệu GPT-4o zero-shot (temperature=0) sinh Gherkin scenarios từ Connextra user stories có đạt tỉ lệ parse không lỗi (executable syntax rate) ≥ 80% không?

**Loại claim:** Absolute threshold
**H0:** p_exec ≤ 0.80
**H1:** p_exec > 0.80
**Metric:** Executable syntax rate (Gherkin parser `behave --dry-run`)
**Ngưỡng:** 80% — Case 2: Lấy floor value từ Storer 2019 (80% success generation rate).
**Statistical test:** Binomial exact test (α = 0.05)

---

## 5. Experiment Protocol

### 5.1 Pipeline tổng quan
1. Tiền xử lý dataset: Thu thập 100 Gherkin scenarios nguyên bản từ 3 dự án mã nguồn mở (Sylius, Fineract, Diaspora) và dịch ngược (reverse-engineer) thành User Stories chuẩn Connextra.
2. LLM Generation: Gọi OpenAI API (GPT-4o) với zero-shot prompt để sinh lại Gherkin scenarios từ các User Stories đó.
3. Executable Validation: Lưu output ra file `.feature` và chạy lệnh `behave --dry-run` để lấy pass/fail (RQ2).
4. Semantic Evaluation: Dùng `all-MiniLM-L6-v2` để sinh vector embedding cho generated Gherkin và expert Gherkin gốc, sau đó tính cosine similarity (RQ1).
5. Statistical Analysis: Chạy các test thống kê (Wilcoxon, Binomial) để kết luận bác bỏ H0.

### 5.2 Dataset
**Tên dataset:** Open-source GitHub `.feature` reversed.
**Nguồn (URL):** Trích xuất từ GitHub (Sylius, Apache Fineract, Diaspora).
**Quy mô (N):** N = 100 Gherkin scenarios
**Domain:** Đa domain (E-commerce, Finance, Social Network).
**Lý do chọn:** Lấy Gherkin trực tiếp từ production code của kỹ sư thật và dịch ngược thành User Story giúp loại bỏ hoàn toàn "Expert Bias" (thiên kiến gán nhãn của sinh viên), đảm bảo Construct Validity tuyệt đối.

### 5.3 LLM/Tool Configuration
**Model:** `gpt-4o-2024-11-20` (Sử dụng GPT-4o bản full snapshot mới nhất tại thời điểm thực hiện thí nghiệm để đánh giá trọn vẹn năng lực của model, nhóm đã chuẩn bị đủ ngân sách).
**Hyperparameters:** `temperature=0`, `top_p=1.0`, `max_tokens=1500`.
**Prompting strategy:** Zero-shot
**Prompt template:**
```text
You are an expert QA automation engineer. Convert the following Connextra user story into BDD Gherkin scenarios.
Output ONLY valid Gherkin syntax (Feature, Scenario, Given, When, Then) without any markdown formatting, explanations, or extra text.
User Story: "{user_story_text}"
```
**Lý do cấu hình:** Đảm bảo reproducibility tuyệt đối (temp=0) và đúng focus của evaluation (zero-shot baseline) dựa trên đề xuất của Rathnayake 2026.

### 5.4 Measurement
**Metric 1:** Cosine similarity | **Tool:** `sentence-transformers` (all-MiniLM-L6-v2) | **Ground truth:** 100 Expert-written `.feature` files nguyên bản từ 3 dự án mã nguồn mở.

**Metric 2:** Executable rate | **Tool:** `behave 1.2.6` (`--dry-run`) | **Ground truth:** Parser log (Exit code 0).

### 5.5 Baseline
Expert-written Gherkin (đóng vai trò human-level reference standard cho RQ1).

### 5.6 Statistical Analysis Plan
- **RQ1 Test:** One-sample Wilcoxon signed-rank test — one-tailed — α = 0.05. Lý do: Similarity score thường không theo phân phối chuẩn (skewed).
- **RQ2 Test:** Binomial exact test — one-tailed — α = 0.05. Lý do: Executable là biến nhị phân (Pass/Fail) và N ~ 50.
- **Effect size:** Cliff's delta (cho RQ1). Power analysis N=100 đảm bảo power ≥ 0.90 cho large effect.

---

## 6. Evaluation Plan

### 6.1 Bảng tiêu chí đánh giá

| RQ | Metric | Ngưỡng | Test | H0 bị reject khi... | Kết quả âm tính có ý nghĩa? |
|----|--------|--------|------|----------------------|------------------------------|
| RQ1 | Cosine similarity | 0.85 | Wilcoxon (one-tail) | p-value < 0.05 | Có. Chứng tỏ LLM chưa bắt kịp chuyên gia về ngữ nghĩa. |
| RQ2 | Executable rate | 80% | Binomial (one-tail) | p-value < 0.05 | Có. Chỉ ra Gherkin syntax quá khắt khe đối với zero-shot LLM. |

### 6.2 Diễn giải tổ hợp kết quả
- **Double positive (Reject cả 2 H0):** GPT-4o zero-shot đủ tốt để áp dụng thẳng vào CI/CD pipeline cho BDD automation.
- **Mixed (Reject H01, Fail H02):** Sinh đúng ý nghĩa (semantic) nhưng sai cú pháp. Cần build custom post-processor/linter sửa syntax.
- **Mixed (Fail H01, Reject H02):** Chạy được parser nhưng sai nghiệp vụ (hallucination). Cần RAG hoặc few-shot prompting.
- **Double negative:** GPT-4o zero-shot thất bại toàn diện. Cần đổi model hoặc dùng full fine-tuning.

---

## 7. Threats to Validity

### 7.1 Internal Validity
**Threat:** OpenAI có thể silent-update model (model drift).
**Mitigation:** Pin version chính xác = `gpt-4o-2024-11-20`. Lưu trữ toàn bộ raw JSON response bao gồm fingerprint của API call.

### 7.2 External Validity
**Threat:** User stories từ một domain không phản ánh tính tổng quát.
**Mitigation:** Chọn dataset tổng hợp từ 3 open-source SE projects (Sylius, Fineract, Diaspora) phủ 3 lĩnh vực thương mại, tài chính, mạng xã hội.

### 7.3 Construct Validity
**Threat:** Cosine similarity có thể không phản ánh đúng "sự đúng đắn nghiệp vụ" (logical equivalence).
**Mitigation:** Dùng `behave` parser (RQ2) làm metric bảo vệ (executable).

### 7.4 Conclusion Validity
**Threat:** Kích thước mẫu quá nhỏ (thiếu statistical power).
**Mitigation:** N = 100 được chọn dựa trên power analysis đảm bảo statistical power vượt mức tiêu chuẩn. Dùng exact test (Binomial) thay vì z-approximation cho biến nhị phân.

---

## 8. Timeline & Resources

### 8.0 Phân công vai trò

| Role | Thành viên | Trách nhiệm trong experiment | Phần báo cáo phụ trách |
|------|------------|-------------------------------|------------------------|
| PL | Nguyễn Minh Hoàng | Coordinate tiến độ, review nhất quán toàn bộ, tổng hợp cuối | §1 Introduction, §8 Conclusion, tổng hợp & chỉnh sửa final |
| DG | Trần Tuấn Khang | Thu thập + clean dataset, tạo expert ground truth (baseline), format chuẩn Connextra | §3 Dataset & Sampling, §4 Ground Truth Construction |
| LR | Nguyễn Hiếu An | Cấu hình OpenAI API, viết Python script, batch processing, **chạy thí nghiệm + đo metric (Cosine Similarity, behave parser, Wilcoxon, Binomial) luôn** | §5 Experiment Setup, §6 Results & Statistical Analysis, figures/plots |
| MS | Võ Hiếu Chương | Hỗ trợ LR verify kết quả metric, review tính đúng đắn của statistical tests, kiểm tra cross-check | §6.3 Validity Check (peer-review kết quả của LR) |
| RW | Tống Vỹ Thuận | Thu thập + tổng hợp Related Work, viết phần lý thuyết nền | §2 Related Work & Background, §7 Threats to Validity |

> **Nguyên tắc phân công:** Ai làm thực nghiệm phần nào thì viết báo cáo phần đó. Không có một người duy nhất viết toàn bộ báo cáo.

### 8.1 Resource Inventory

| Tài nguyên | Trạng thái | Owner | Ghi chú |
|---|---|---|---|
| Dataset | ✅ | DG | 100 file Gherkin từ 3 open-source projects, đã reverse-engineer |
| API key | ✅ | LR | OpenAI API (GPT-4o, ngân sách đã duyệt) |
| Compute | ✅ | LR | Google Colab T4 (free) cho embedding + behave |
| Ground truth | ⚠️ | DG | Expert-written (có sẵn từ dataset hoặc viết tay, ~5h) |

### 8.2 Chi phí ước tính
- **OpenAI API (`gpt-4o`):** Input 200 tokens, output 300 tokens × 100 stories. Ngân sách dự kiến trong khoảng $10 - $20, hoàn toàn nằm trong khả năng đầu tư của nhóm.

### 8.3 Timeline chi tiết (Tuần 5–10)
| Tuần | Hoạt động | Owner | Checkpoint — output cụ thể |
|---|---|---|---|
| **5** | Viết proposal §2–§7 | DG + RW + PL | `proposal.md` v1.0 |
| **5** | Verify + download dataset, kiểm tra format | DG | `data/raw/` folder |
| **5** | Setup API, test 1 sample case | LR | `test_api.py` chạy được |
| **5** | Implement metric script sơ bộ | LR | `compute_metric.py` draft |
| **6** | ★ **GV phê duyệt proposal** | GV | `proposal.md` Approved |
| **7** | Annotate ground truth pilot (10 sample) | DG | `data/pilot_ground_truth.csv` |
| **7** | Chạy LLM + đo metric pilot (cosine + behave) | LR | `results/pilot_llm_output.csv`, `metric_pilot.json` |
| **7** | Cross-check kết quả metric pilot | MS | Meeting note. Amendment (nếu cần) |
| **8** | Full experiment batch run + đo metric toàn bộ + statistical tests | LR | `results/full_llm_output.csv`, `full_analysis.ipynb` |
| **8** | Cross-check & verify kết quả full | MS | Review report |
| **8** | Tạo figures (≥ 2 plots) | LR | `figures/` folder |
| **9** | Viết §5, §6 (Experiment + Results) | LR | Draft §5–§6 |
| **9** | Viết §3, §4 (Dataset + Ground Truth) | DG | Draft §3–§4 |
| **9** | Viết §2, §7 (Related Work + Threats) | RW | Draft §2, §7 |
| **9** | Viết §1, §8 (Intro + Conclusion) + tổng hợp | PL | Draft §1, §8 + merge toàn bộ |
| **10** | Review chéo + chỉnh sửa final + present | All | Final report + Slide |

### 8.4 Contingency Plan
- **Nếu chi phí OpenAI đột ngột tăng:** Nếu có sự cố ngoài ý muốn, dùng local Llama 3 qua Ollama.
- **Nếu pilot Tuần 7 phát hiện phân phối cosine lệch nhiều so với 0.85:** Áp dụng Quy trình Amendment (§8.6) nộp GV trong 24 giờ.
- **Nếu có file Gherkin nguồn không parse được:** Loại bỏ và lấy file Gherkin khác thay thế từ cùng dự án để đảm bảo đủ 100 samples.
