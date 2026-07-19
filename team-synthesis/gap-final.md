# Gap Statement Final — LLM for Acceptance Test Automation (BDD/Gherkin)

**Nhóm:** 4  
**Evidence base:** 19 papers (merged) — 17 đọc full-text + 14 từ IEEE Xplore (overlap đã loại trùng)  
**Date:** 2026-06-11  

> Quy tắc: GAP cuối từ evidence merged, không phải bỏ phiếu đa số. Priority: GAP-T > GAP-M > GAP-D > GAP-S.

---

## GAP PRIMARY (composite): GPT-5.4-mini × (cosine semantic + executable) × Connextra

> **"Không có nghiên cứu nào đánh giá GPT-5.4-mini 2026-03-17 (latest version, official API, domain-specific few-shot prompting, temperature=0) cho việc sinh Gherkin acceptance test scenarios + step definitions từ user story format Connextra, đo bằng skeleton cosine semantic similarity (all-MiniLM-L6-v2) ≥ ngưỡng so với expert-written Gherkin VÀ executable syntax rate bằng Gherkin parser (`behave --dry-run`) ≥ ngưỡng."**

GAP composite gồm 3 thành phần con, mỗi thành phần đã verify phản chứng:

### GAP-T (Technology) — GPT-5.4-mini 2026-03-17 chưa được dùng
- **Bằng chứng:** 0/19 paper dùng GPT-5.4-mini 2026-03-17 API cho task này.
- **Paper gần nhất:** Rathnayake 2026 (GPT-4 `gpt-4-0613`, BERTScore F1=91.16%); Ferreira 2025 (GPT-4 Turbo, 100% syntactic, 95% helpful);
- **Lý do là GAP thật:** GPT-5.4-mini ra mắt 2026-03-17, sau khi đa số paper (2023–early 2024) đã thiết kế thí nghiệm. GPT-4o-mini ≠ GPT-5.4-mini (context 128K, reasoning mạnh hơn).

### GAP-M1 (Metric semantic) — cosine all-MiniLM + ngưỡng cố định chưa dùng
- **Bằng chứng:** 0/19 paper dùng cosine similarity (all-MiniLM-L6-v2) với ngưỡng cố định so với expert-written Gherkin.
- **Paper gần nhất:** Rathnayake 2026 dùng SBCS (SentenceBERT cosine) NHƯNG không ngưỡng cố định, không dùng all-MiniLM, không so expert Connextra; Varpe 2025 dùng BERTScore F1=80.58% (token-level, không sentence-level cosine).

### GAP-M2 (Metric executable) — Gherkin parser chuẩn (`behave`) chưa dùng
- **Bằng chứng:** 0/19 paper dùng `behave --dry-run` parse `.feature` files làm primary metric đo executable rate.
- **Paper gần nhất:**
  - Karpurapu 2024 dùng **Gherkin-lint** (linter check style tĩnh, KHÔNG parse/execute) — 93.3% file pass lint vẫn có thể fail parse.
  - Ferreira 2025 check **TypeScript syntax** (Cypress), không phải Gherkin `.feature`.
  - Kavuri 2022 đo **Selenium/PyTest execution** (92% GPT-4), không phải Gherkin parser.
  - Fonseca 2025 đo syntactic correctness 93.3% nhưng trên mobile UI (AToMIC), không phải behave parser chuẩn.
- **Lý do là GAP thật:** Gherkin-lint chỉ check style rules; file pass lint vẫn fail `behave --dry-run` nếu lỗi indentation/encoding/malformed scenario outline.

**Lý do kết hợp T+M1+M2:** GAP composite duy nhất tạo contribution hoàn chỉnh = **tool mới (GPT-5.4-mini 2026-03-17) × metric combo mới (cosine + executable parser) × dataset mới (Connextra)**. Nếu chỉ GAP-T → thiếu đóng góp metric; chỉ GAP-M → thiếu novelty tool.

---

## GAP SECONDARY: GAP-D (dataset Connextra benchmark)

> **"Chưa có benchmark dataset chuẩn hóa theo Connextra format ('As a [role], I want [feature], So that [benefit]') từ ≥3 SE projects độc lập, public, tiếng Anh — phần lớn nghiên cứu dùng dataset nhỏ (<50 US), single-project, hoặc mixed format (JIRA, SRS, free-form)."**

- **Bằng chứng:** 0/19 paper dùng Connextra chuẩn từ ≥3 project. Gần nhất: Karpurapu 2024 (~50 US đa domain nhưng không enforce Connextra); Ferreira 2025 (13 JIRA issues, 1 công ty); Varpe 2025 (SRS documents).

---

## 📋 BẢNG BẰNG CHỨNG TỔNG HỢP (cô kiểm tra ở đây)

> Mỗi dòng = 1 paper thật + số liệu cụ thể + vị trí (abstract/full-text) + chứng minh cho GAP nào. Tất cả số liệu đều mở được trên IEEE Xplore / publisher (abstract miễn phí).

### Bằng chứng GAP-T (GPT-5.4-mini chưa dùng)

| Paper | Model dùng | Số liệu | Chứng minh GAP-T | Nguồn |
|---|---|---|---|---|
| Rathnayake 2026 | GPT-4 (`gpt-4-0613`) | BERTScore F1 = 91.16%; human eval 4.63/5 | Dùng GPT-4 cũ, KHÔNG phải GPT-5.4-mini | full-text |
| Fernandes 2025 | GPT-4o-mini + 6 LLM khác | METEOR = 0.78 (Mini); 0.84 (Gemini best) | GPT-4o-mini ≠ GPT-5.4-mini | full-text, Table 2 |
| Ferreira 2025 | GPT-4 Turbo (`gpt-4-1106`) | Syntactic 100%; helpful 95% | GPT-4 Turbo, không phải GPT-5.4-mini | [doi](https://doi.org/10.1109/AST66626.2025.00007) |
| Karpurapu 2024 | GPT-3.5, GPT-4-Preview, PaLM-2, Llama-2 | BDD error-free (few-shot) | Dừng ở GPT-4-Preview, không GPT-5.4-mini | [doi](https://doi.org/10.1109/ACCESS.2024.3391815) |

→ **0/19 paper dùng GPT-5.4-mini 2026-03-17.** Paper gần nhất chỉ tới GPT-4 Turbo / GPT-4o-mini.

### Bằng chứng GAP-M1 (cosine all-MiniLM + ngưỡng chưa dùng)

| Paper | Metric semantic dùng | Vì sao vẫn là GAP | Nguồn |
|---|---|---|---|
| Rathnayake 2026 | SBCS (SentenceBERT Cosine) | Có cosine NHƯNG: không ngưỡng cố định, không dùng all-MiniLM-L6-v2, không so expert Connextra | full-text |
| Varpe 2025 | BERTScore F1 = 80.58% | BERTScore là token-level, KHÔNG phải sentence-level cosine | [doi](https://doi.org/10.1109/CASCON66301.2025.00084) |
| Fernandes 2025 | METEOR = 0.84, BERTScore | METEOR đo n-gram overlap, không phải cosine embedding | full-text |
| Ferreira 2025 | Semantic Relevance (human survey) | Đánh giá người, không phải embedding metric | full-text, Threats to Validity |

→ **0/19 paper dùng cosine all-MiniLM-L6-v2 + ngưỡng cố định** so với expert-written Connextra Gherkin.

### Bằng chứng GAP-M2 (executable behave parser chưa dùng) ⭐ phần Hiếu An

| Paper | Cách đo "chạy được" | Vì sao KHÁC behave parser | Số liệu | Nguồn |
|---|---|---|---|---|
| Karpurapu 2024 | **Gherkin-lint** (linter) | Chỉ check style/syntax tĩnh, KHÔNG verify parse được; file pass lint vẫn fail behave | few-shot ~0 lỗi; domain-specific few-shot prompting 89% lỗi | [doi](https://doi.org/10.1109/ACCESS.2024.3391815) |
| Fonseca 2025 | Syntactic correctness (AToMIC) | Trên mobile UI, không phải behave parser chuẩn | **93.3%** đúng cú pháp | [doi](https://doi.org/10.1109/ASE63991.2025.00273) |
| Ferreira 2025 | TypeScript syntax check (Cypress) | Check TypeScript, không phải Gherkin `.feature` | 100% syntactic | full-text |
| Kavuri 2022 | Selenium/PyTest execution | Chạy Python script, không phải Gherkin parser | 92% (GPT-4) | full-text |
| Storer 2019 | Generation success rate | Template-based, không LLM | **80%** white box | [doi](https://doi.org/10.1109/SCAM.2019.00033) |

→ **0/19 paper dùng `behave --dry-run`** parse `.feature` làm primary metric đo executable rate. Điểm mấu chốt: **Gherkin-lint ≠ parser** — file pass lint vẫn fail behave nếu lỗi indentation/encoding/scenario outline.

### Bằng chứng nguồn ngưỡng (Case 1/2/3)

| Ngưỡng | Case | Paper nguồn | Số cụ thể |
|---|---|---|---|
| Executable ≥ 80% | Case 2 (floor) | Storer 2019 | floor = 80% (white box); Kavuri 92%, Ferreira 100% → 80% bảo thủ |
| Cosine ≥ 0.85 | Case 3 (pilot) | Fernandes 2025 (tham khảo) | METEOR 0.84 chỉ calibration lỏng (METEOR≠cosine) → cần mini-pilot |

---

## Bảng đóng góp (minh bạch)

| Thành phần GAP | Nguồn evidence | Thành viên chủ trì |
|---|---|---|
| GAP-T (GPT-5.4-mini 2026-03-17) | Full-text 17 paper (Rathnayake, Fernandes, Ferreira...) | **Nguyễn Minh Hoàng** |
| GAP-M1 (cosine all-MiniLM) | Full-text + IEEE (Rathnayake SBCS, Varpe BERTScore) | Chung |
| **GAP-M2 (executable behave)** | IEEE (Fonseca 93.3%, Storer 80%, Karpurapu) + full-text (Gherkin-lint analysis) | **Nguyễn Hiếu An** |
| GAP-D (Connextra) | Cả 2 evidence table | **Nguyễn Minh Hoàng** |

---

## Threshold (theo Case 1/2/3)

| Threshold | Giá trị | Case | Nguồn |
|---|---|---|---|
| RQ1 — cosine semantic | ≥ 0.85 (cần mini-pilot xác nhận) | **Case 3** | Không paper dùng cosine all-MiniLM + ngưỡng; Fernandes METEOR=0.84 chỉ là calibration lỏng (METEOR ≠ cosine) → mini-pilot 5–10 sample |
| RQ2 — executable rate | ≥ 80% | **Case 2** | floor = Storer 2019 (80% white box); Kavuri 92%, Ferreira 100% → 80% bảo thủ, khả thi |

---

## Mapping GAP → RQ → H0/H1

| GAP | RQ | H0 | H1 | Kiểm định |
|---|---|---|---|---|
| GAP-T + GAP-M1 | RQ1: semantic | μ_cosine ≤ 0.85 | μ_cosine > 0.85 | Wilcoxon signed-rank (one-tailed, α=0.05) |
| GAP-T + GAP-M2 | RQ2: executable | p_exec ≤ 0.80 | p_exec > 0.80 | Binomial exact (one-tailed, p₀=0.80, α=0.05) |
| GAP-D | Population (P) trong PICO | — | — | Addressed bằng dataset design |

---

## PICO cuối cùng

- **P:** ≥ 50 user story Connextra từ ≥ 3 SE project public (Mendeley BDD + 2 GitHub repos)
- **I:** GPT-5.4-mini, domain-specific few-shot prompting, temperature=0
- **C:** expert-written Gherkin (ground truth, do nhóm có kinh nghiệm BDD viết theo rubric)
- **O:** cosine similarity (all-MiniLM-L6-v2) ≥ 0.85 + executable rate (`behave --dry-run`) ≥ 80%

---

---

## Đánh giá Khả thi (Feasibility Check) — GAP Composite

| Tiêu chí | Câu hỏi | Đánh giá | Ghi chú & Căn cứ xác minh thực tế |
|---|---|---|---|
| **Dataset** | Có nguồn dataset Connextra tải được không? | ⚠️ Cần xử lý | Crawl 3 mã nguồn mở (Sylius, Fineract, Diaspora) về để lấy bộ gherkin mẫu, sau đó reverse từ gherkin sang user stories |
| **Tool/API** | GPT-5.4-mini có khả thi truy cập không? | ✅ An toàn | Nhóm đã có ngân sách để chạy trực tiếp **GPT-5.4-mini**. Chi phí ước tính nằm trong khả năng đầu tư của nhóm. Đã check OpenAI platform. |
| **Compute** | Cần phần cứng gì? | ✅ An toàn | Thư viện `sentence-transformers` (all-MiniLM-L6-v2) có thể chạy mượt mà trên CPU hoặc Google Colab T4 miễn phí. Gherkin parser (`behave`) rất nhẹ. |
| **Ground truth**| Cần chuyên gia gán nhãn không? | ⚠️ Cần xử lý | Cần expert-written Gherkin cho 261 stories. Sẽ ưu tiên lấy ground truth `.feature` có sẵn từ các repo mã nguồn mở lớn thay vì tự gán hoàn toàn để giảm thiểu expert bias và tiết kiệm thời gian (ước tính < 5h). |
| **Skills** | Nhóm implement được pipeline? | ✅ An toàn | Python, gọi API OpenAI, dùng `sentence-transformers` và chạy file Python script gọi lệnh `behave` bằng subprocess đều là kiến thức cơ bản nhóm đã nắm rõ. |
| **Thời gian** | Có kịp timeline môn học? | ✅ An toàn | Pipeline (API call -> parser -> embedding) có thể được tự động hoá hoàn toàn bằng 1 script Python. Khả thi chạy trong 1-2 tuần. |
| **Contribution**| Kết quả âm có giá trị báo cáo không? | ✅ An toàn | Hoàn toàn có. Nếu GPT-5.4-mini thất bại (vd: parse fail nhiều), đây vẫn là báo cáo đầu tiên chứng minh điểm yếu của LLM với syntax khắt khe của Gherkin trên benchmark Connextra. |

> **Phương án Downscope (nếu cần):** 
> *   Nếu không tìm đủ 50 dataset chuẩn từ open source: Sẽ downscope N=30, ảnh hưởng đến statistical power một chút nhưng vẫn đủ để chạy non-parametric tests.

---

## Checklist (rubric team-synthesis)
- [x] GAP từ evidence merged, không bỏ phiếu đa số
- [x] Mỗi GAP trỏ về cột cụ thể + paper gần nhất + còn thiếu gì
- [x] Đã qua feasibility check (đánh giá An Toàn / Rủi ro và có mitigation cụ thể)
- [x] Ghi rõ đóng góp từng thành viên
- [x] Threshold có Case 1/2/3

