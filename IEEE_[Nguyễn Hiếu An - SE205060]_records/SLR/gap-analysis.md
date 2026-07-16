# GAP Analysis — LLM for Acceptance Test Automation (BDD/Gherkin)

**Thành viên:** Nguyễn Hiếu An (SE205060)  
**Evidence table:** N = 14 papers · **Ngày:** 2026-06-__

---

## Bảng GAP

> 4 loại GAP. Priority khi xung đột: **GAP-T > GAP-M > GAP-D > GAP-S**.

| Cột nguồn | Phát hiện | Loại GAP | Phản chứng (đã kiểm tra) |
|---|---|---|---|
| Tool/LLM | Chưa ai dùng GPT-4o (gần nhất: GPT-4 Turbo) | **GAP-T** | ✅ Đã quét 14/14 paper — 0 paper dùng GPT-4o |
| Metric | Chưa ai kết hợp cosine semantic similarity (ngưỡng cố định) + executable rate | **GAP-M** | ✅ Đã quét 14/14 paper — 0 paper kết hợp đủ 2 metric |
| Dataset | Chưa ai dùng user story Connextra chuẩn | **GAP-D** | ✅ Đã quét 14/14 paper — 0 paper dùng Connextra |
| Hạn chế | Hạn chế chung "single domain/dataset nhỏ" | **GAP-S** | ⚠️ Không đủ dữ liệu (nhiều paper cột Hạn chế = N/A) — không xác nhận được ≥ 6/14 paper (ceil 0.4×14) |

---

## GAP Chính: GAP-M (kèm GAP-T)

> GAP-M được chọn làm primary vì pass feasibility check tốt nhất (xem cuối file) và có bằng chứng mạnh nhất (0 paper).

**Phát biểu:** Trong 14 papers, semantic similarity (Varpe 2025 – BERTScore) và executable rate (Fonseca 2025, Karpurapu 2024) đã được đo RIÊNG LẺ, nhưng **không paper nào kết hợp cosine semantic similarity (ngưỡng cố định) ĐỒNG THỜI với executable syntax rate** so với expert-written Gherkin từ user story Connextra, dùng GPT-4o.

## GAP Secondary: GAP-T

**Phát biểu:** Không paper nào dùng **GPT-4o** — frontier model mới nhất (paper gần nhất Ferreira 2025 dùng GPT-4 Turbo). GAP-T được "ăn theo" miễn phí khi chọn GPT-4o làm intervention.

---

## Bằng chứng 2 nhánh metric của GAP-M (cả 2 đều có cơ sở từ paper)

> GAP-M nói "kết hợp cosine semantic similarity + executable rate". Để chứng minh GAP này hợp lệ, phải chỉ ra **cả 2 metric đều là metric có thật, đã được paper đo riêng lẻ** — rồi mới kết luận chưa ai ghép. Dưới đây là bằng chứng từng nhánh.

### Nhánh 1 — Semantic similarity (đã có paper đo)

| Paper | Metric semantic | Số liệu cụ thể | Nguồn |
|---|---|---|---|
| Varpe 2025 | BERTScore (embedding semantic similarity) | Qwen **BERTScore F1 = 80.58%** | Abstract — [doi](https://doi.org/10.1109/CASCON66301.2025.00084) |
| Alinezhadtilaki 2025 | BERT đánh giá chất lượng scenario | Precision 70.1%, Recall 80.5%, **F1 = 75.3%** | Abstract — [doi](https://doi.org/10.1109/ICMI65310.2025.11141197) |

→ Semantic similarity là metric **có thật, đã được dùng**. Ngưỡng tham chiếu: Varpe BERTScore ≈ 0.81.

### Nhánh 2 — Executable syntax rate (đã có paper đo) ⭐ phần cô cần

**Executable syntax rate = tỷ lệ % Gherkin scenario parse được không lỗi cú pháp** (chạy qua Gherkin parser như `behave`/`cucumber` không báo lỗi). Công thức: (số scenario parse được / tổng scenario) × 100%.

| Paper | Metric executable/syntactic | Số liệu cụ thể | Nguồn |
|---|---|---|---|
| Fonseca 2025 | Syntactic correctness + executable rate | **93.3%** Gherkin đúng cú pháp; 78.8% PageObjects chạy không sửa; **100%** UI test chạy | Abstract — [doi](https://doi.org/10.1109/ASE63991.2025.00273) |
| Karpurapu 2024 | Syntax error rate | GPT-3.5 & GPT-4 sinh BDD **error-free** (không lỗi cú pháp) | Abstract — [doi](https://doi.org/10.1109/ACCESS.2024.3391815) |
| Storer 2019 | Generation success rate | **80%** success (white box); 17% (black box) | Abstract — [doi](https://doi.org/10.1109/SCAM.2019.00033) |

→ Executable rate là metric **có thật, đã được dùng**. Ngưỡng 80% lấy floor từ Storer 2019 (Case 2).

### Kết luận 2 nhánh

Cả semantic similarity (Nhánh 1) và executable rate (Nhánh 2) **đều là metric hợp lệ, đã được paper đo riêng**. GAP-M KHÔNG nằm ở chỗ "metric mới", mà ở chỗ **chưa ai ĐO CẢ HAI cùng lúc** trên cùng dataset Connextra + GPT-4o, so với expert ground truth. Bảng dưới chứng minh điều đó.

---

## Chi tiết kiểm tra phản chứng — GAP-M (primary)

> Với mỗi paper, hỏi: "Paper này đã kết hợp cosine semantic similarity + executable rate trên Connextra+GPT-4o chưa?" Cột cuối ghi rõ paper đo nhánh nào (Sem = semantic, Exec = executable).

| Paper | Đã làm GAP-M chưa? | Chi tiết (đo nhánh nào) |
|---|---|---|
| Sisomboon 2026 | Không | Chỉ đo test coverage (98.44%) — không Sem, không Exec |
| Chatterjee 2025 | Không | Đo authoring time — không Sem, không Exec |
| Ferreira 2025 | Không | Chỉ helpfulness rating (định tính) — không Sem, không Exec |
| Alinezhadtilaki 2025 | Một phần | **Sem only** (BERT F1=75.3%, detect defect) — không Exec |
| Jagielski 2025 | Không | Readability định tính — không Sem, không Exec |
| Patel 2025 | Không | Đo time/cost — không Sem, không Exec |
| Galloy 2025 | Một phần | **Exec only** (Gherkin syntax compliance) — không Sem |
| Fonseca 2025 | Một phần | **Exec only** (93.3% syntactic correct) — không Sem; input JIRA không Connextra |
| Varpe 2025 | Một phần | **Sem only** (BERTScore 80.58%) — không Exec; SRS không Connextra; không GPT-4o |
| Karpurapu 2024 | Một phần | **Exec only** (error-free) — không Sem; không GPT-4o |
| Waitchasarn 2023 | Không | Maintenance effort — không Sem, không Exec |
| Lee 2023 | Không | Abstract không có số liệu |
| Wang 2022 | Không | Coverage (95% steps) — không Sem, không Exec |
| Storer 2019 | Một phần | **Exec only** (success rate 80%) — không Sem; template-based |

→ **Kết luận: XÁC NHẬN GAP-M.** Trong 14 paper: nhánh **Sem** có 2 paper (Varpe, Alinezhadtilaki); nhánh **Exec** có 4 paper (Fonseca, Karpurapu, Galloy, Storer). NHƯNG **0 paper đo CẢ HAI nhánh cùng lúc** trên Connextra + GPT-4o. Mỗi paper chỉ làm 1 trong 2.

---

## Feasibility Check — GAP Chính (GAP-M)

| Tiêu chí | Câu hỏi | Đánh giá | Ghi chú |
|---|---|---|---|
| Dataset | User story Connextra tải được ngay? | ⚠️ Cần xử lý | Cần build 30–50 Connextra story (< 1 tuần); hoặc lấy `.feature` từ GitHub rồi reverse |
| Tool/API | GPT-4o có free tier không? | ⚠️ Cần xử lý | GPT-4o API tốn phí (~< $5 cho 30–50 sample); hoặc dùng GPT-4o mini rẻ hơn |
| Compute | Cần phần cứng gì? | ✅ An toàn | sentence-transformers chạy CPU/Colab T4 free; Gherkin parser nhẹ |
| Ground truth | Cần label thủ công không? | ⚠️ Cần xử lý | Cần expert-written Gherkin; ước tính ≤ 5 giờ cả nhóm nếu lấy từ open-source `.feature` |
| Skills | Nhóm implement được pipeline? | ✅ An toàn | Có thư viện sẵn (sentence-transformers, behave/gherkin); có tutorial; nhóm biết Python/Java |
| Thời gian | Xong trong số tuần còn lại? | ✅ An toàn | Pipeline đơn giản; xong với buffer nếu bắt đầu sớm |
| Contribution | Kết quả âm có giá trị báo cáo không? | ✅ An toàn | Có — là framework đo đầu tiên kết hợp 2 metric; kết quả âm vẫn là baseline |

**Kết quả:** 0 ❌ / 3 ⚠️ → **Rủi ro trung bình.** Vì có 3 ⚠️ (≥ 3), cần viết mitigation cụ thể cho từng cái trước khi commit:

### Mitigation cho 3 ⚠️
1. **Dataset (Connextra):** Lấy file `.feature` chất lượng cao từ GitHub open-source làm ground truth → reverse ra user story Connextra. Hoặc dùng 30–50 story tự viết theo best practice (ghi rõ nguồn, không nhận là "expert").
2. **Tool/API (GPT-4o cost):** Downscope sang **GPT-4o mini** (rẻ hơn nhiều, vẫn là frontier, vẫn lấp GAP-T) nếu chi phí GPT-4o vượt ngân sách. Test API trước với 5 sample.
3. **Ground truth:** Giới hạn N = 30–50 sample để annotation ≤ 5 giờ; ưu tiên lấy ground truth có sẵn từ open-source thay vì tự viết toàn bộ.

---

## Checklist Checkpoint (rubric RBL-2)

- [x] Mỗi GAP có bảng kiểm tra phản chứng (tên paper cụ thể)
- [x] GAP primary đã qua feasibility check — 0 ❌, 3 ⚠️ (đã viết mitigation)
- [x] Đã chọn GAP primary (GAP-M) + secondary (GAP-T) + ghi lý do
- [x] Phát biểu GAP 1–2 câu rõ ràng
