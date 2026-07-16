# GAP Analysis — LLM for Acceptance Test Automation (BDD/Gherkin)
Evidence table: N = 17 paper | Ngày: 2026-06-14

## Bảng GAP Tóm Tắt

| Cột | Phát hiện | Loại GAP | Phản chứng |
|-----|-----------|----------|------------|
| Tool/LLM | Chưa ai evaluate GPT-4o full version cho Gherkin generation | GAP-T | ✅ Kiểm tra 17 paper |
| Dataset | Các dataset thường nhỏ (<50 US) hoặc không chuẩn Connextra | GAP-D | ✅ Kiểm tra 17 paper |
| Metric | Thiếu đánh giá semantic similarity bằng cosine sim (all-MiniLM) | GAP-M1 | ✅ Kiểm tra 17 paper |
| Metric | Thiếu đánh giá executable rate bằng Gherkin parser (`behave`) | GAP-M2 | ✅ Kiểm tra 17 paper |
| Hạn chế | Dataset nhỏ (8/17), Thiếu semantic metric (8/17) | GAP-S | ✅ Kiểm tra 17 paper |

## GAP Chính: GAP-T kết hợp GAP-M1, M2
Không có nghiên cứu nào evaluate GPT-4o (full version, zero-shot, temperature=0) cho việc sinh Gherkin từ Connextra-format user stories, đo bằng cosine semantic similarity (all-MiniLM-L6-v2) so với expert-written Gherkin và đo executable syntax rate bằng chuẩn Gherkin parser (`behave`).

## GAP Secondary: GAP-D
Chưa có benchmark dataset chuẩn hóa theo Connextra format từ ≥3 SE projects độc lập phục vụ đánh giá LLM-based Gherkin generation.

## Chi tiết kiểm tra phản chứng
Xem Phần 2 của phần Phân tích chi tiết bên dưới.

## Feasibility Check — GAP Chính
| Tiêu chí | Mức | Ghi chú |
|----------|-----|---------|
| Dataset | ✅ | Có sẵn Mendeley dataset + public GitHub projects |
| Tool/API | ✅ | API GPT-4o chi phí rất rẻ (~$0.2) |
| Compute | ✅ | Chạy CPU Python script bình thường |
| Ground truth | ⚠️ | Cần expert viết Gherkin thủ công (khoảng 12 giờ/nhóm 4 người) |
| Skills | ✅ | Thư viện `openai`, `sentence-transformers`, `behave` chuẩn, dễ tích hợp |
| Thời gian | ✅ | Khả thi làm kịp trong 2 tuần |
| Contribution | ✅ | Sẽ là baseline report đầu tiên cho combination này |
**Kết quả:** 0 ❌ / 1 ⚠️ → **An toàn**

---

> **Nguồn số liệu:** Phân tích trực tiếp từ full-text 17 papers
> Papers số liệu đầy đủ nhất để dùng làm dẫn chứng: **Rathnayake et al. 2026**, **Fernandes et al. 2025**, **Karpurapu et al. 2024**, **Ferreira et al. 2025**, **Kavuri 2022**.

---

## Phần 1 — Quét 4 loại GAP từ Evidence

### GAP-T (Technology) — Công nghệ nào chưa thử?

**Cột Tool/LLM trong 17 papers đọc trực tiếp:**

| Paper | Tool/LLM dùng | GPT-4o full? |
|---|---|---|
| Rathnayake 2026 | GPT-4 (gpt-4-0613), Claude 3 Opus, Gemini 1.5 Flash | ❌ GPT-4 cũ, không phải GPT-4o |
| Fernandes 2025 | GPT-3.5, GPT-4 Turbo, **GPT-4o Mini**, LLaMA3, Phi-3, Gemini, DeepSeek | ❌ GPT-4o **Mini** (không phải full) |
| Karpurapu 2024 | GPT-3.5, GPT-4-Preview, PaLM-2, Llama-2-13B | ❌ Không có GPT-4o |
| Ferreira 2025 | GPT-4 Turbo (gpt-4-1106-preview) | ❌ Không phải GPT-4o |
| Kavuri 2022 | GPT-4 (temp=0.2), Code Llama-13B, Codex | ❌ Không phải GPT-4o |
| Tiwari 2025 | "Generic LLM custom" — không nêu tên | ❌ Không rõ |
| Almeyda 2025 | Gemini 1.5 Pro + GPT-4.0 | ❌ GPT-4.0 ≠ GPT-4o API |
| Sami et al. 2024 | GPT-3.5-turbo | ❌ |
| dos Santos 2025 | ChatGPT (GPT-4), Gemini, Grok, Copilot | ❌ Version GPT-4 không rõ |
| Mendoza 2024 | Copilot, ChatGPT-3.5/4, Gemini | ❌ Không rõ version |
| Santos & Maciel 2024 | PaLM, GPT-3.5 | ❌ |
| Rahman & Zhu 2024 | GPT-4.0 (RaT prompting) | ❌ GPT-4.0 ≠ GPT-4o |
| Bijili 2025 | GPT-3.5/4 (Streamlit) | ❌ Không rõ version |
| Narvaez 2025 | iStar → rule-based | ❌ Không dùng LLM |
| Raharjana 2020 | Codeception rule-based | ❌ Không dùng LLM |
| Barbosa 2020 | Feature-Trace static analysis | ❌ Không dùng LLM |
| Wolde & Boltana 2021 | QF-Test + Cucumber | ❌ Không dùng LLM |

**→ Kết luận GAP-T: 0/17 papers dùng GPT-4o (full, official API `gpt-4o-xxxx`) làm primary model cho Gherkin generation từ Connextra-format user stories.**

**Paper gần nhất:**
- Fernandes 2025 dùng GPT-4o **Mini** (không phải full) — METEOR=0.78
- Rathnayake 2026 dùng GPT-4 cũ (gpt-4-0613) — BERTScore F1=91.16%
- Không paper nào test GPT-4o full với task cụ thể: **Connextra US → Gherkin + step definitions, zero-shot, temperature=0**

---

### GAP-M (Metric) — Khía cạnh nào chưa đo?

**Quét cột Metric:**

| Paper | Semantic metric dùng | Cosine sim (sentence-level)? | Executable parser? |
|---|---|---|---|
| Rathnayake 2026 | BLEU, METEOR, ROUGE-L, **BERTScore F1**, SBCS, SBED, USECS | SBCS = SentenceBERT Cosine, nhưng **không đặt ngưỡng cố định** | ❌ Không dùng parser |
| Fernandes 2025 | METEOR, BERTScore, ANOVA, CV% | ❌ Không dùng cosine trực tiếp | ❌ Không đo executable |
| Karpurapu 2024 | Syntax Validation Accuracy (Gherkin-lint) | ❌ Không đo semantic | ❌ Gherkin-lint ≠ behave parser |
| Ferreira 2025 | Helpfulness%, Syntactic Correctness%, Semantic Relevance%, cost | ❌ Human survey, không phải embedding | ❌ Manual review |
| Kavuri 2022 | Syntactic validity, Semantic accuracy (manual), Execution success (Selenium/PyTest) | ❌ Manual review | ❌ Selenium/PyTest ≠ Gherkin parser |
| Almeyda 2025 | Test completeness, syntactic correctness, execution rate, quality Likert | ❌ Không dùng cosine | ❌ TestRigor platform riêng |
| Sami et al. 2024 | No quantitative metric (content analysis chỉ qualitative) | ❌ | ❌ |
| Tiwari 2025 | Time reduction%, defect reduction%, coverage increase% | ❌ | ❌ |
| dos Santos 2025 | Similarity matrix (không rõ model), accuracy Kruskal-Wallis | ❌ Không rõ embedding model | ❌ |

**→ GAP-M1: 0/17 papers dùng `cosine similarity với all-MiniLM-L6-v2` làm primary metric với ngưỡng cố định để so sánh LLM-generated vs expert-written Gherkin.**

**Gần nhất:** Rathnayake 2026 dùng SBCS (SentenceBERT Cosine Similarity) nhưng *không đặt ngưỡng cố định* và không dùng model `all-MiniLM-L6-v2` cụ thể. Đây vẫn là GAP vì metric + model + threshold combination chưa xuất hiện.

**→ GAP-M2: 0/17 papers dùng Gherkin parser chuẩn hóa (`behave --dry-run` hoặc tương đương) làm primary metric đo executable rate.**

- Karpurapu 2024 dùng Gherkin-lint (syntax linter, không phải parser chạy được)
- Ferreira 2025 dùng TypeScript syntax check (Cypress, không phải Gherkin parser)
- Kavuri 2022 dùng Selenium/PyTest execution (không phải Gherkin format)
- **Không ai dùng `behave --dry-run` trên Gherkin .feature files để đo executable rate.**

---

### GAP-D (Dataset) — Domain/quy mô nào thiếu?

**Quét cột Dataset:**

| Paper | Dataset format | Connextra format? | Multi-project ≥3? |
|---|---|---|---|
| Rathnayake 2026 | 500 US + descriptions từ 4 sản phẩm *1 công ty proprietary* | ❌ US + description (không chỉ Connextra) | ✅ 4 products |
| Fernandes 2025 | 10 test descriptions từ corpus 1,286 — free-form | ❌ Free-form, không phải Connextra | ❌ 1 system |
| Karpurapu 2024 | ~50 US từ Mendeley + blogs, đa domain | ⚠️ Mixed format, không enforce Connextra | ✅ Đa domain |
| Ferreira 2025 | 13 JIRA issues từ 1 công ty automotive | ❌ JIRA issues, không phải Connextra | ❌ 1 công ty |
| Kavuri 2022 | 120 NL requirements (user stories, Gherkin-style, functional desc) — 3 formats mixed | ❌ Mixed formats | ❌ 1 benchmark |
| Narvaez 2025 | iStar models | ❌ iStar, không liên quan | ❌ |
| dos Santos 2025 | 34 US, 94 ACs | ⚠️ Không rõ format chuẩn | ❌ 1 project |
| Almeyda 2025 | 50 US từ product backlog | ⚠️ Product backlog, không enforce Connextra | ❌ 1 công ty |
| Sami et al. 2024 | Epics → user stories (generated) | ❌ Không Connextra chuẩn | ❌ |

**→ GAP-D: 0/17 papers dùng dataset Connextra-format chuẩn ("As a [role], I want [feature], So that [benefit]") từ ≥3 SE projects độc lập, public, tiếng Anh.**

Gần nhất: Karpurapu 2024 (~50 US đa domain) nhưng không enforce Connextra format và dataset nhỏ.

---

### GAP-S (Shared Limitation) — Hạn chế nào ≥ ceil(0.4×17) = 7 papers cùng thừa nhận?

**ceil(0.4 × 17) = 7 papers**

| Hạn chế | Papers thừa nhận | Đếm |
|---|---|---|
| Dataset nhỏ / 1 project / generalizability thấp | Rathnayake [1 cty], Fernandes [10 scenarios], Karpurapu [50 US], Ferreira [13 US], Almeyda [1 cty], dos Santos [34 US], Sami [1 tool], Kavuri [120 reqs] | **8/17** ✅ |
| Không đo semantic similarity bằng embedding metric | Karpurapu [chỉ syntax], Ferreira [human survey], Wolde, Raharjana, Barbosa, Narvaez, Rahman, Bijili | **8/17** ✅ |
| Thiếu executable/parse validation chuẩn hóa | Fernandes [không đo], Karpurapu [chỉ lint], Ferreira [manual], Sami [không đo], dos Santos [không đo], Tiwari [không đo], Rahman [không đo] | **7/17** ✅ |
| Không có ground truth do expert BDD viết chuẩn hóa | Karpurapu [không có], Fernandes [domain expert limited], Ferreira [developer survey], Sami [không], Almeyda [không có], dos Santos [không rõ] | **6/17** ~ borderline |

**→ GAP-S xác nhận: "Dataset nhỏ" (8/17), "Thiếu semantic metric" (8/17), "Thiếu executable metric chuẩn hóa" (7/17) — tất cả đều ≥ 7 papers.**

---

## Phần 2 — Kiểm Tra Phản Chứng (BẮT BUỘC)

### Phản chứng cho GAP-T: "GPT-4o full chưa được evaluate"

```
GAP tuyên bố: Không có paper nào evaluate GPT-4o (full) zero-shot cho Gherkin generation từ Connextra US
```

| Paper | Đã dùng GPT-4o full? | Ghi chú |
|---|---|---|
| Rathnayake 2026 | ❌ Không | Dùng GPT-4 (gpt-4-0613), không phải gpt-4o |
| Fernandes 2025 | ❌ Không | Dùng GPT-4o **Mini** — model nhỏ hơn, khác biệt đáng kể |
| Karpurapu 2024 | ❌ Không | GPT-4-Preview (gpt-4-1106), không phải gpt-4o |
| Ferreira 2025 | ❌ Không | GPT-4 Turbo (gpt-4-1106-preview) |
| Kavuri 2022 | ❌ Không | GPT-4 (temp=0.2), không phải GPT-4o, không phải Gherkin |
| Chang & Shirazi 2025 | ⚠️ Dùng GPT-4o | Nhưng task là **Python unit test**, không phải Gherkin BDD |
| Almeyda 2025 | ❌ Không | "GPT-4.0" — có thể là GPT-4 cũ, không phải gpt-4o API |
| 10 papers còn lại | ❌ Không | Không ai dùng GPT-4o full |

**→ Kết luận: XÁC NHẬN GAP-T.**
Chang & Shirazi 2025 dùng GPT-4o nhưng task là Python unit test (không phải Gherkin), domain hoàn toàn khác. Không phải phản chứng hợp lệ.

---

### Phản chứng cho GAP-M1: "Cosine sim (all-MiniLM, ngưỡng ≥0.85) chưa được dùng"

| Paper | Dùng cosine sim + ngưỡng cố định? | Ghi chú |
|---|---|---|
| Rathnayake 2026 | ⚠️ SBCS (SentenceBERT Cosine) | Có cosine nhưng **không có ngưỡng cố định**, không dùng all-MiniLM-L6-v2, không so với expert-written Connextra |
| dos Santos 2025 | ⚠️ "Similarity matrix" | Không rõ model embedding, không có ngưỡng |
| 15 papers còn lại | ❌ Không | Không ai dùng |

**→ Kết luận: XÁC NHẬN GAP-M1.**
Rathnayake dùng cosine nhưng thiếu 3 yếu tố: (1) model `all-MiniLM-L6-v2` cụ thể, (2) ngưỡng ≥0.85 cố định, (3) dataset Connextra.

---

### Phản chứng cho GAP-M2: "Behave --dry-run parser chưa được dùng"

| Paper | Dùng Gherkin parser chạy được (behave/cucumber)? | Ghi chú |
|---|---|---|
| Karpurapu 2024 | ⚠️ Gherkin-lint | Linter chỉ check style/syntax tĩnh, **không parse/execute Gherkin** |
| Ferreira 2025 | ⚠️ TypeScript syntax check | Kiểm tra Cypress script, không phải Gherkin .feature file |
| Kavuri 2022 | ⚠️ Selenium/PyTest execution | Chạy Python test scripts, không phải Gherkin parser |
| Raharjana 2020 | ⚠️ Codeception | Chạy test code PHP, không phải Gherkin parser độc lập |
| 13 papers còn lại | ❌ Không | |

**→ Kết luận: XÁC NHẬN GAP-M2.**
Không paper nào dùng `behave --dry-run` (hoặc `cucumber --dry-run`) để kiểm tra Gherkin .feature files có parse được không, làm primary metric đo executable rate.

---

## Phần 3 — Đánh Giá Khả Thi (Feasibility Check)

### GAP-T: GPT-4o zero-shot cho Gherkin từ Connextra US

| Tiêu chí | Đánh giá | Status |
|---|---|---|
| **Dataset** | Connextra US có sẵn public: Mendeley BDD dataset (Karpurapu 2024 dùng ~50 US), GitHub repos, JIRA public; có thể tổng hợp ≥50 US từ ≥3 projects trong 1 tuần | ✅ An toàn |
| **Tool/API** | GPT-4o API: OpenAI free tier $5 credit; 50 US × ~500 tokens = ~25K tokens ≈ $0.10–0.20 tổng cộng | ✅ An toàn |
| **Compute** | GPT-4o qua API — không cần GPU; Python script chạy CPU | ✅ An toàn |
| **Ground truth** | Expert software tester ≥2 năm BDD viết Gherkin cho 50 US: nhóm 4 người × 12.5 US × ~15 phút = ~12 giờ tổng | ⚠️ Cần xử lý (≤5 giờ/người, feasible) |
| **Skills** | `openai` Python SDK + `sentence-transformers` + `scipy.stats` — đều có tutorial; `behave` là package chuẩn | ✅ An toàn |
| **Thời gian** | Data collection 1 tuần + experiment 2 ngày + analysis 3 ngày = ~2 tuần; buffer ≥1 tuần | ✅ An toàn |
| **Contribution** | Ngay cả kết quả âm tính ("GPT-4o zero-shot không đạt 0.85") là baseline đầu tiên cho GPT-4o trên task này | ✅ An toàn |

**Kết quả: 1⚠️, 0❌ → AN TOÀN**
Mitigation cho ⚠️ Ground truth: phân công đều 4 thành viên (mỗi người ~12-13 US), dùng rubric chuẩn từ Narvaez 2025 [≥2 năm BDD experience].

---

### GAP-M1+M2 (Metric combo): Cosine sim ≥0.85 + executable rate ≥80%

| Tiêu chí | Đánh giá | Status |
|---|---|---|
| **Dataset** | Cùng dataset với GAP-T | ✅ An toàn |
| **Tool/API** | `sentence-transformers` (free, PyPI) + `behave` (free, PyPI) | ✅ An toàn |
| **Compute** | all-MiniLM-L6-v2 chạy CPU Colab T4 free; behave --dry-run chạy local | ✅ An toàn |
| **Ground truth** | Cùng expert-written Gherkin với GAP-T | ⚠️ Cùng effort với trên |
| **Skills** | `sentence-transformers.SentenceTransformer` + `sklearn.metrics.pairwise.cosine_similarity` + `scipy.stats.wilcoxon` — thư viện chuẩn, có tutorial | ✅ An toàn |
| **Thời gian** | Thêm ~1 ngày code pipeline metric; chạy tự động | ✅ An toàn |
| **Contribution** | 0/17 papers dùng combination này — là contribution rõ ràng | ✅ An toàn |

**Kết quả: 1⚠️, 0❌ → AN TOÀN**

---

### GAP-D: Dataset Connextra multi-project

| Tiêu chí | Đánh giá | Status |
|---|---|---|
| **Dataset** | Phải tự thu thập Connextra US từ ≥3 projects → crawl GitHub/Jira public, annotate format | ⚠️–❌ Cần 1-2 tuần nếu xây từ đầu |
| **Tool/API** | N/A | ✅ |
| **Ground truth** | Cần expert viết Gherkin cho từng US | ⚠️ |
| **Thời gian** | Dataset collection là bottleneck; nếu không có sẵn → blocker | ❌ Nếu không tìm được source |

**Kết quả: 1❌ tiềm năng → Downscope: dùng Mendeley BDD dataset (Karpurapu 2024) + supplement thêm 2 GitHub projects → đạt ≥3 projects mà không cần crawl từ đầu.**
Sau downscope: trở thành ✅/⚠️ như GAP-T.

---

## Phần 4 — GAP Cuối Cùng (Sau Feasibility Check)

### GAP Primary (ưu tiên cao nhất): **GAP-T1 kết hợp GAP-M1+M2**

> **"Không có nghiên cứu nào evaluate GPT-4o (full version, zero-shot, temperature=0) cho việc sinh Gherkin acceptance test scenarios từ Connextra-format user stories, đo bằng cosine semantic similarity (all-MiniLM-L6-v2) so với expert-written Gherkin và executable syntax rate bằng Gherkin parser (`behave`)."**

Lý do kết hợp T+M: Đây là GAP composite duy nhất — nếu chỉ GAP-T thì thiếu contribution về metric; nếu chỉ GAP-M thì thiếu novelty về tool. Kết hợp tạo contribution hoàn chỉnh: **new tool × new metric × new dataset format**.

### GAP Secondary: **GAP-D1**

> **"Chưa có benchmark dataset chuẩn hóa theo Connextra format từ ≥3 SE projects độc lập phục vụ đánh giá LLM-based Gherkin generation — phần lớn nghiên cứu dùng datasets nhỏ (<50 US), single-project, hoặc mixed formats."**

---

## Phần 5 — Top 3 GAP với Dẫn Chứng Đầy Đủ

---

### 🥇 GAP 1 (PRIMARY): GPT-4o full chưa được evaluate cho Gherkin-from-Connextra-US

**Phát biểu chính thức:**
> GPT-4o (official full version, zero-shot prompting, temperature=0) has not been evaluated for generating Gherkin acceptance test scenarios and step definitions from Connextra-format user stories in any existing study.

**Bằng chứng số liệu từ các paper đầy đủ nhất:**

| Paper | Số liệu chứng minh GAP | Trích dẫn |
|---|---|---|
| **Rathnayake et al. 2026** (500 US, 4 products) | Dùng GPT-4 (gpt-4-0613), không phải GPT-4o. Best score: GPT-4 zero-shot human eval = **4.63/5**, BERTScore F1 = **91.16%**. Temperature=0, top_p=1.0 là best config. | "Our experiments indicate that setting temperature to 0 and top_p to 1.0 produced the highest-quality BDD scenarios across all models" |
| **Fernandes et al. 2025** (10 scenarios, 7 LLMs) | GPT-4o **Mini** (không phải full) METEOR = **0.78**; Gemini (không phải GPT-4o) đạt METEOR = **0.84** (best). GPT-4 Turbo = 0.74. | Table 2: zero-shot METEOR scores; GPT-4o Mini ≠ GPT-4o full |
| **Karpurapu et al. 2024** (~50 US, IEEE Access) | GPT-3.5 + GPT-4-Preview few-shot ≈ **0 syntax errors (~100%)**; zero-shot gây 89% tổng lỗi. Không test GPT-4o. | "GPT-3.5 and GPT-4 generate error-free BDD acceptance tests with better performance" |
| **Ferreira et al. 2025** (13 US, automotive) | GPT-4 Turbo: Syntactic correctness = **100%**, Helpful = **95%** (AutoUAT), **92%** (TestFlow). Không test GPT-4o. | "The users found the acceptance test scenarios generated by AutoUAT helpful 95% of the time" |

**Tại sao là GAP thực sự:**
- GPT-4o ra mắt tháng 5/2024, sau khi hầu hết các papers trên thiết kế thí nghiệm (2023–early 2024)
- GPT-4o Mini ≠ GPT-4o full: GPT-4o có context window 128K tokens, multimodal, reasoning superior
- 0/17 papers đọc trực tiếp + 0/30 papers merged dùng GPT-4o full cho task Connextra → Gherkin

**Feasibility:** ✅ **AN TOÀN** — GPT-4o API $0.10-0.20 cho 50 US, chạy CPU, dataset có sẵn.

---

### 🥈 GAP 2: Cosine semantic similarity (all-MiniLM-L6-v2) với ngưỡng cố định chưa được dùng

**Phát biểu chính thức:**
> No existing study measures the semantic quality of LLM-generated Gherkin scenarios using sentence-level cosine similarity (all-MiniLM-L6-v2 model) with a fixed threshold against expert-written Gherkin as ground truth.

**Bằng chứng số liệu từ các paper đầy đủ nhất:**

| Paper | Số liệu chứng minh GAP | Ghi chú |
|---|---|---|
| **Rathnayake et al. 2026** | Dùng SBCS (SentenceBERT Cosine) nhưng: (1) không dùng all-MiniLM-L6-v2, (2) không đặt ngưỡng cố định ≥0.85, (3) dataset từ 1 công ty proprietary | Best SBCS không được báo cáo riêng; BERTScore F1 = 91.16% là best GPT-4 |
| **Fernandes et al. 2025** | Dùng METEOR (0.84 best — Gemini zero-shot) và BERTScore, nhưng **không dùng cosine similarity**. Ghi nhận: "không đo executability" | "The study acknowledges the absence of executable syntax rate measurement" |
| **Karpurapu et al. 2024** | **Chỉ đo Syntax Validation Accuracy** bằng Gherkin-lint. **Không đo semantic similarity bằng bất kỳ embedding metric nào.** Hạn chế tự nêu: "we haven't explored the realms of test coverage and the validity of generated tests" | Table 6-7: chỉ có syntax error counts, zero semantic metric |
| **Ferreira et al. 2025** | "Semantic Relevance" đo bằng human survey (60% initially, 92% sau minor fixes) — **không phải embedding-based metric** | "not measuring embedding-based semantic similarity" — Threats to Validity |
| **Kavuri 2022** | Semantic accuracy đo bằng manual review (~90% GPT-4) — **không tự động, không reproducible** | "assessed through manual review by experienced testers" |

**Tại sao là GAP thực sự:**
- METEOR và BLEU đo n-gram overlap, yếu trong capturing semantic equivalence khi phrasing khác nhau
- BERTScore dùng token-level matching, không sentence-level
- Cosine similarity với sentence encoder (all-MiniLM) là metric reproducible, automated, có ngưỡng rõ ràng — chưa ai standardize cho Gherkin generation
- Fernandes 2025 METEOR=0.84 (best trong SLR) → cung cấp calibration point: cosine ≥0.85 là reasonable và challenging threshold

**Feasibility:** ✅ **AN TOÀN** — `sentence-transformers` free PyPI, CPU inference, `scipy.stats.wilcoxon` standard.

---

### 🥉 GAP 3: Executable rate bằng Gherkin parser chuẩn hóa (`behave`) chưa được đo

**Phát biểu chính thức:**
> No existing study uses a standardized Gherkin parser (such as `behave --dry-run`) as primary metric to measure the executable syntax rate of LLM-generated Gherkin feature files.

**Bằng chứng số liệu từ các paper đầy đủ nhất:**

| Paper | Số liệu chứng minh GAP | Ghi chú |
|---|---|---|
| **Karpurapu et al. 2024** | Dùng **Gherkin-lint** (syntax linter): GPT-3.5 + GPT-4 few-shot ≈ 0 lỗi; zero-shot gây **89%** tổng lỗi syntax. NHƯNG Gherkin-lint ≠ parser — không verify feature file có chạy được không. | "we employed the Gherkin-lint tool to detect syntax violations" — static analysis only |
| **Kavuri 2022** | GPT-4: Execution success = **92%** (Selenium/PyTest). Code Llama: **79%**. Codex: **85%**. NHƯNG đây là Python test script execution, **không phải Gherkin .feature file parsing**. | "Execution Success – Whether the script executed successfully without runtime errors" — Selenium/PyTest context |
| **Ferreira et al. 2025** | Syntactic Correctness = **100%** (TypeScript, Cypress framework). Nhưng kiểm tra TypeScript syntax, **không phải Gherkin parser**. | "100% of the generated test cases adhered to TypeScript syntax" |
| **Almeyda 2025** | Functional Correctness pass rate = **91.9%** (181/197 test cases). Nhưng dùng TestRigor BDD 2.0 platform riêng, **không phải standardized Gherkin parser**. | Platform-specific, không reproducible với behave |
| **Fernandes et al. 2025** | **Không đo executable rate**. Hạn chế tự nêu: "the study does not measure executable syntax rate". | "não avalia executabilidade" |

**Tại sao là GAP thực sự:**
- Gherkin-lint (Karpurapu) chỉ check style rules (missing tags, keyword order), **không verify parsability**
- Một file pass Gherkin-lint vẫn có thể fail `behave --dry-run` nếu có indentation issues, encoding problems, malformed scenario outlines
- `behave --dry-run` là tiêu chuẩn industry Python BDD: parse feature file + check step definitions structure mà không chạy browser/API
- 0/17 papers

**Feasibility:** ✅ **AN TOÀN** — `behave` là PyPI package free, chạy local, exit code 0/non-zero cho automated testing.

---

## Phần 6 — Mapping GAP → RQ → H0/H1

| GAP | RQ | H0 | H1 | Kiểm định |
|---|---|---|---|---|
| GAP-T1 + GAP-M1 | RQ1: Semantic similarity | μ_sim ≤ 0.85 | μ_sim > 0.85 | Wilcoxon signed-rank (one-tailed) |
| GAP-T1 + GAP-M2 | RQ2: Executable syntax | p_exec ≤ 0.80 | p_exec > 0.80 | Binomial test (one-tailed, exact) |
| GAP-D1 | Population (P) trong PICO | N/A — addressed bằng dataset design | N/A | N/A |

---

## Phần 7 — Papers Số Liệu Tốt Nhất Để Trích Dẫn

Để support gap statement trong proposal, ưu tiên cite các papers sau (đã đọc full-text, có số liệu cụ thể):

| Mục đích | Paper đề xuất | Số liệu key |
|---|---|---|
| Chứng minh GPT-4o chưa test | Rathnayake 2026 + Fernandes 2025 | Best model = GPT-4 (4.63/5) và Gemini (METEOR=0.84); không có GPT-4o full |
| Calibrate ngưỡng 0.85 | Fernandes 2025 | Gemini METEOR=0.84 (best in 7 LLMs, zero-shot) |
| Justify temperature=0 | Rathnayake 2026 | "temperature=0 and top_p=1.0 produced highest-quality BDD scenarios across all models" |
| Chứng minh GAP-M (thiếu cosine metric) | Karpurapu 2024 | Chỉ dùng Gherkin-lint; "we haven't explored semantic validity" |
| Chứng minh GAP-M (thiếu executable parser) | Karpurapu 2024 + Fernandes 2025 | Gherkin-lint ≠ parser; Fernandes không đo executable |
| Calibrate ngưỡng 80% executable | Kavuri 2022 + Ferreira 2025 | GPT-4 execution success = 92% (Kavuri); 100% syntactic correctness (Ferreira) — 80% là conservative |
| Justify expert ground truth | Ferreira 2025 | "95% helpful" từ experienced product owners |
| Justify dataset size ≥50 | Karpurapu 2024 + Fernandes 2025 | 50 US bị chỉ trích nhỏ; 10 scenarios thiếu generalizability |
