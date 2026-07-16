# Gap Analysis — LLM for Acceptance Test Automation (BDD/Gherkin)

**Nhóm:** Cá nhân (Võ Hiếu Chương - SE204862) | **N papers đọc trực tiếp:** 12 | **Evidence base:** 12 papers
**Date:** 2026-06-10

> **Nguồn số liệu:** Phân tích trực tiếp từ full-text 12 papers trong `evidence_table.md`.
> Papers số liệu đầy đủ nhất để dùng làm dẫn chứng: **Rathnayake et al. 2026**, **Fernandes et al. 2025**, **Karpurapu et al. 2024**, **Ferreira et al. 2025**, **Fonseca et al. 2025**.

---

## Phần 1 — Quét 4 loại GAP từ Evidence

### GAP-T (Technology) — Công nghệ nào chưa thử?

**Cột Tool/LLM trong 12 papers đọc trực tiếp:**

| Paper | Tool/LLM dùng | GPT-4o full? |
|---|---|---|
| Rathnayake 2026 | GPT-4 (gpt-4-0613), Claude 3, Gemini | ❌ GPT-4 cũ, không phải GPT-4o |
| Fernandes 2025 | GPT-3.5, GPT-4 Turbo, **GPT-4o Mini**, LLaMA 3, Phi-3, Gemini, DeepSeek | ❌ GPT-4o **Mini** (không phải full) |
| Karpurapu 2024 | GPT-3.5, GPT-4, PaLM-2, Llama-2-13B | ❌ Không có GPT-4o |
| Ferreira 2025 | GPT-4 Turbo | ❌ Không phải GPT-4o |
| Fonseca 2025 | DeepSeek-R1, DeepSeek-Coder-V2, Gemma3:1b | ❌ Không dùng GPT-4o |
| Santos 2024 | Gemini | ❌ Không phải GPT-4o |
| Mendoza 2024 | ChatGPT-4, Copilot, Gemini | ❌ Không rõ version |
| dos Santos 2025 | ChatGPT (GPT-4), Gemini, Grok, Copilot | ❌ Không rõ version |
| Paduraru 2025 | Llama3.1 8B | ❌ |
| Almeyda 2025 | Gemini, GPT-4 | ❌ |
| Santos & Maciel 2024 | PaLM/GPT | ❌ |
| Adu 2024 | GPT-3.5-turbo | ❌ |

**→ Kết luận GAP-T: 0/12 papers dùng GPT-4o (full, zero-shot, temperature=0) làm primary model cho Gherkin generation.**

**Paper gần nhất:**
- Fernandes 2025 dùng GPT-4o **Mini** (không phải full)
- Rathnayake 2026 dùng GPT-4 cũ (gpt-4-0613)
- Không paper nào test GPT-4o full với task cụ thể: **Connextra US → Gherkin + step definitions, zero-shot, temperature=0**.

---

### GAP-M (Metric) — Khía cạnh nào chưa đo?

**Quét cột Metric:**

| Paper | Semantic metric dùng | Cosine sim (sentence-level)? | Executable parser (`behave`)? |
|---|---|---|---|
| Rathnayake 2026 | BLEU, METEOR, ROUGE-L, BERTScore | ❌ Không đặt ngưỡng cố định, không dùng all-MiniLM | ❌ Không dùng parser |
| Fernandes 2025 | METEOR, CV% | ❌ Không dùng cosine | ❌ Không đo executable |
| Karpurapu 2024 | Syntax validation (Gherkin-lint) | ❌ Không đo semantic | ❌ Gherkin-lint ≠ behave parser |
| Fonseca 2025 | Syntactic correctness rate | ❌ Không đo semantic | ❌ UI execution, không Gherkin parse |
| Ferreira 2025 | Semantic relevance (survey) | ❌ Human survey, không phải embedding | ❌ Manual review |
| Santos 2024 | Code coverage | ❌ Không | ❌ Code execution, không Gherkin parse |
| Mendoza 2024 | Rubric-based | ❌ | ❌ |
| dos Santos 2025 | Similarity matrix | ❌ Không rõ model | ❌ |
| Paduraru 2025 | Qualitative | ❌ | ❌ |
| Almeyda 2025 | Test completeness, execution rate | ❌ | ❌ TestRigor platform, không behave |
| Santos & Maciel 2024 | Survey | ❌ | ❌ |
| Adu 2024 | Gherkin-lint | ❌ | ❌ Gherkin-lint ≠ behave parser |

**→ GAP-M1: 0/12 papers dùng `cosine similarity với all-MiniLM-L6-v2` làm primary metric với ngưỡng cố định ≥0.85.**
**→ GAP-M2: 0/12 papers dùng Gherkin parser chuẩn hóa (`behave --dry-run` hoặc tương đương) làm primary metric đo executable rate.**

---

### GAP-D (Dataset) — Domain/quy mô nào thiếu?

**Quét cột Dataset:**

| Paper | Dataset format | Connextra format? | Multi-project ≥3? |
|---|---|---|---|
| Rathnayake 2026 | 500 US từ 4 products (1 company) | ⚠️ US + description | ✅ 4 products |
| Karpurapu 2024 | ~50 US (Mendeley + blog) | ⚠️ Mixed format | ✅ Đa domain |
| Ferreira 2025 | 13 JIRA issues | ❌ JIRA issues, không phải Connextra | ❌ 1 company |
| Fonseca 2025 | 13 issues từ MyBMW | ❌ Không | ❌ 1 app |
| Fernandes 2025 | 10 free-form test descriptions | ❌ Free-form | ❌ 1 system |
| 7 papers còn lại | Hỗn hợp, không chuẩn hóa | ❌ | ❌ Hầu hết 1 dự án |

**→ GAP-D: 0/12 papers dùng dataset Connextra-format chuẩn ("As a [role], I want [feature], So that [benefit]") từ ≥3 SE projects.**

---

### GAP-S (Shared Limitation) — Hạn chế nào ≥ ceil(0.4×12) = 5 papers cùng thừa nhận?

**ceil(0.4 × 12) = 5 papers**

| Hạn chế | Papers thừa nhận | Đếm |
|---|---|---|
| Không đo semantic similarity bằng embedding metric | Tất cả trừ Rathnayake | **11/12** ✅ |
| Dataset nhỏ / 1 project / generalizability thấp | Karpurapu, Ferreira, Fonseca, Fernandes, Santos, Mendoza, dos Santos, Paduraru, Almeyda | **9/12** ✅ |
| Thiếu executable/parse validation chuẩn hóa | Tất cả | **12/12** ✅ |

**→ GAP-S xác nhận: "Dataset nhỏ" (9/12), "Thiếu semantic metric" (11/12), "Thiếu executable metric chuẩn hóa" (12/12) — tất cả đều ≥ 5 papers.**

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
| Karpurapu 2024 | ❌ Không | GPT-4, GPT-3.5 |
| Ferreira 2025 | ❌ Không | GPT-4 Turbo |
| 8 papers còn lại | ❌ Không | Không ai dùng GPT-4o full |

**→ Kết luận: XÁC NHẬN GAP-T.**

---

### Phản chứng cho GAP-M1: "Cosine sim (all-MiniLM, ngưỡng ≥0.85) chưa được dùng"

| Paper | Dùng cosine sim + ngưỡng cố định? | Ghi chú |
|---|---|---|
| Rathnayake 2026 | ⚠️ BERTScore | Có dùng embedding metric nhưng **không có ngưỡng cố định**, không dùng all-MiniLM-L6-v2 |
| dos Santos 2025 | ⚠️ "Similarity matrix" | Không rõ model embedding, không có ngưỡng |
| 10 papers còn lại | ❌ Không | Không ai dùng |

**→ Kết luận: XÁC NHẬN GAP-M1.**

---

### Phản chứng cho GAP-M2: "Behave --dry-run parser chưa được dùng"

| Paper | Dùng Gherkin parser chạy được (behave/cucumber)? | Ghi chú |
|---|---|---|
| Karpurapu 2024 | ⚠️ Gherkin-lint | Linter chỉ check style/syntax tĩnh, **không parse/execute Gherkin** |
| Adu 2024 | ⚠️ Gherkin-lint | Tương tự Karpurapu |
| Ferreira 2025 | ⚠️ TypeScript syntax check | Kiểm tra Cypress script, không phải Gherkin .feature file |
| Fonseca 2025 | ⚠️ UI execution | Chạy UI test e2e, không phải Gherkin parser |
| 8 papers còn lại | ❌ Không | |

**→ Kết luận: XÁC NHẬN GAP-M2.**

---

## Phần 3 — Đánh Giá Khả Thi (Feasibility Check)

### GAP-T: GPT-4o zero-shot cho Gherkin từ Connextra US

| Tiêu chí | Đánh giá | Status |
|---|---|---|
| **Dataset** | Mendeley BDD dataset (Karpurapu 2024) + bổ sung từ Github repos (đảm bảo ≥50 US, ≥3 projects) | ✅ An toàn |
| **Tool/API** | GPT-4o API: Rất rẻ (vài cents cho 50 US) | ✅ An toàn |
| **Compute** | Gọi API qua Python, không cần GPU | ✅ An toàn |
| **Ground truth** | Tự viết bộ Gherkin chuẩn (Expert-written) cho 50 US. Cần khoảng 10-12 giờ. | ⚠️ Cần xử lý (feasible) |
| **Skills** | Python, `openai` library | ✅ An toàn |
| **Thời gian** | Thí nghiệm nhanh, data preparation lâu nhất nhưng có thể làm trong 1 tuần | ✅ An toàn |
| **Contribution** | Ngay cả kết quả âm tính (GPT-4o không vượt ngưỡng) vẫn là một đóng góp học thuật | ✅ An toàn |

**Kết quả: 1⚠️, 0❌ → AN TOÀN**

---

### GAP-M1+M2 (Metric combo): Cosine sim ≥0.85 + executable rate ≥80%

| Tiêu chí | Đánh giá | Status |
|---|---|---|
| **Dataset** | Dùng chung với GAP-T | ✅ An toàn |
| **Tool/API** | `sentence-transformers` (free, PyPI) + `behave` (free, PyPI) | ✅ An toàn |
| **Compute** | all-MiniLM-L6-v2 nhẹ, chạy tốt trên CPU/Colab T4 | ✅ An toàn |
| **Ground truth** | Dùng chung expert-written Gherkin với GAP-T | ⚠️ Cùng effort |
| **Skills** | `sentence-transformers`, `scipy.stats.wilcoxon` | ✅ An toàn |
| **Thời gian** | Thêm 1-2 ngày code pipeline metric | ✅ An toàn |
| **Contribution** | 0/12 papers dùng combination này — là contribution rõ ràng | ✅ An toàn |

**Kết quả: 1⚠️, 0❌ → AN TOÀN**

---

### GAP-D: Dataset Connextra multi-project

| Tiêu chí | Đánh giá | Status |
|---|---|---|
| **Dataset** | Trích xuất từ Mendeley + GitHub | ⚠️ Cần thời gian lọc Connextra format |
| **Tool/API** | N/A | ✅ |
| **Ground truth** | Cần expert viết Gherkin | ⚠️ |
| **Thời gian** | Nếu làm từ đầu thì tốn thời gian, dùng dataset có sẵn để modify sẽ nhanh hơn | ⚠️ |

**Kết quả: 3⚠️ → Downscope: Dùng lại Mendeley BDD dataset và chuẩn hóa thay vì cào (crawl) từ đầu.**

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
| **Rathnayake et al. 2026** (500 US, 4 products) | Dùng GPT-4 (gpt-4-0613), không phải GPT-4o. Temperature=0, top_p=1.0 là best config. | "Our experiments indicate that setting temperature to 0 and top_p to 1.0 produced the highest-quality BDD scenarios across all models" |
| **Fernandes et al. 2025** (10 scenarios) | GPT-4o **Mini** (không phải full) METEOR = **0.78**. | Table 2: zero-shot METEOR scores; GPT-4o Mini ≠ GPT-4o full |
| **Karpurapu et al. 2024** (~50 US) | GPT-3.5 + GPT-4 few-shot. Không test GPT-4o. | "GPT-3.5 and GPT-4 generate error-free BDD acceptance tests..." |
| **Ferreira et al. 2025** (13 US, automotive) | GPT-4 Turbo. Không test GPT-4o. | "The users found the acceptance test scenarios generated by AutoUAT helpful 95% of the time" |

**Tại sao là GAP thực sự:**
- GPT-4o có context window lớn, multimodal và reasoning tốt hơn hẳn bản cũ. Bản "Mini" không đại diện được sức mạnh của GPT-4o.
- 0/12 papers dùng GPT-4o full cho task Connextra → Gherkin.

**Feasibility:** ✅ **AN TOÀN** — GPT-4o API $0.10-0.20 cho 50 US, chạy CPU, dataset có sẵn.

---

### 🥈 GAP 2: Cosine semantic similarity (all-MiniLM-L6-v2) với ngưỡng cố định chưa được dùng

**Phát biểu chính thức:**
> No existing study measures the semantic quality of LLM-generated Gherkin scenarios using sentence-level cosine similarity (all-MiniLM-L6-v2 model) with a fixed threshold against expert-written Gherkin as ground truth.

**Bằng chứng số liệu từ các paper đầy đủ nhất:**

| Paper | Số liệu chứng minh GAP | Ghi chú |
|---|---|---|
| **Rathnayake et al. 2026** | Dùng BERTScore nhưng không dùng all-MiniLM-L6-v2 và **không đặt ngưỡng cố định** | |
| **Fernandes et al. 2025** | Dùng METEOR (0.84 best — Gemini zero-shot), **không dùng cosine similarity**. | "The study acknowledges the absence of executable syntax rate measurement" |
| **Karpurapu et al. 2024** | **Chỉ đo Syntax Validation** bằng Gherkin-lint. **Không đo semantic similarity.** | "we haven't explored the realms of test coverage and the validity of generated tests" |
| **Ferreira et al. 2025** | "Semantic Relevance" đo bằng human survey — **không phải embedding-based metric** | "helpful 95% of the time" |

**Tại sao là GAP thực sự:**
- METEOR và BLEU đo n-gram overlap, yếu trong việc bắt ngữ nghĩa khi từ đồng nghĩa được sử dụng.
- Cosine similarity là metric reproducible, automated, có ngưỡng rõ ràng.

**Feasibility:** ✅ **AN TOÀN** — `sentence-transformers` free PyPI.

---

### 🥉 GAP 3: Executable rate bằng Gherkin parser (`behave`) chưa được đo

**Phát biểu chính thức:**
> No existing study uses a standardized Gherkin parser (such as `behave --dry-run`) as primary metric to measure the executable syntax rate of LLM-generated Gherkin feature files.

**Bằng chứng số liệu từ các paper đầy đủ nhất:**

| Paper | Số liệu chứng minh GAP | Ghi chú |
|---|---|---|
| **Karpurapu et al. 2024** | Dùng **Gherkin-lint** (syntax linter). Gherkin-lint ≠ parser — không verify feature file có chạy được không. | "we employed the Gherkin-lint tool to detect syntax violations" |
| **Ferreira 2025** | Syntactic Correctness = **100%** (Cypress framework). Không phải Gherkin parser. | "100% of the generated test cases adhered to TypeScript syntax" |
| **Fonseca 2025** | UI test execution 100%. Nhưng không parse Gherkin tĩnh. | |
| **Fernandes et al. 2025** | **Không đo executable rate**. Hạn chế tự nêu: "does not capture all quality dimensions". | "METEOR, though effective, does not capture all quality dimensions relevant to BDD" |

**Tại sao là GAP thực sự:**
- Linter tĩnh (Gherkin-lint) không thể phát hiện lỗi logic cấu trúc như thụt lề sai, outline thiếu bảng (Examples table) - những lỗi khiến Parser crash.
- `behave --dry-run` là tiêu chuẩn industry cho Python BDD.

**Feasibility:** ✅ **AN TOÀN** — `behave` là PyPI package free, chạy local.

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
| Chứng minh GPT-4o chưa test | Rathnayake 2026 + Fernandes 2025 | Best model = GPT-4 và GPT-4o Mini; không có GPT-4o full |
| Calibrate ngưỡng 0.85 | Fernandes 2025 | Gemini METEOR=0.84 (best in 7 LLMs, zero-shot) |
| Justify temperature=0 | Rathnayake 2026 | "temperature=0 and top_p=1.0 produced highest-quality BDD scenarios across all models" |
| Chứng minh GAP-M (thiếu cosine metric) | Karpurapu 2024 | Chỉ dùng Gherkin-lint; "we haven't explored semantic validity" |
| Chứng minh GAP-M (thiếu executable parser) | Karpurapu 2024 + Fernandes 2025 | Gherkin-lint ≠ parser; Fernandes không đo executable |
| Calibrate ngưỡng 80% executable | Ferreira 2025 | 100% syntactic correctness (TypeScript) — 80% là conservative |
| Justify expert ground truth | Ferreira 2025 | "95% helpful" từ experienced product owners |
| Justify dataset size ≥50 | Karpurapu 2024 + Fernandes 2025 | 50 US bị chỉ trích nhỏ; 10 scenarios thiếu generalizability |
