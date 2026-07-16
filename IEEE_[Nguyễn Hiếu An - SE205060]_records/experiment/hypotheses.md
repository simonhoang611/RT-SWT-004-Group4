# Giả thuyết H0 / H1

**Nhóm:** SE1905  
**Topic:** LLM for Acceptance Test Automation (BDD/Gherkin)  
**Date:** __/__/2026

---

## Nguyên tắc viết giả thuyết

- **H0 (null hypothesis):** PHỦ ĐỊNH điều muốn chứng minh — giả định "không có hiệu quả / chưa đạt ngưỡng". Đây là giả thuyết mặc định mà ta cố gắng **bác bỏ (reject)**.
- **H1 (alternative hypothesis):** điều ta KỲ VỌNG đúng — "có hiệu quả / đã đạt ngưỡng".
- Mỗi RQ con → 1 cặp H0/H1.

---

## RQ1 — Semantic Similarity

| | Giả thuyết |
|---|---|
| **H0₁** | μ_similarity **≤ 0.85**  (GPT-4o **CHƯA** đạt ngưỡng) |
| **H1₁** | μ_similarity **> 0.85**  (GPT-4o **ĐẠT** ngưỡng) |

- **Kiểm định:** Wilcoxon signed-rank test
- **Mức ý nghĩa:** α = 0.05
- **Vì sao chọn Wilcoxon?** Vì ta so sánh **median** của một tập điểm similarity với một giá trị cố định (0.85), và **KHÔNG giả định dữ liệu phân phối chuẩn** (similarity scores thường lệch, dataset nhỏ). Wilcoxon là kiểm định phi tham số (non-parametric), phù hợp khi không chắc về normal distribution.

---

## RQ2 — Executable Syntax

| | Giả thuyết |
|---|---|
| **H0₂** | executable_rate **≤ 0.80**  (GPT-4o **CHƯA** đạt ngưỡng) |
| **H1₂** | executable_rate **> 0.80**  (GPT-4o **ĐẠT** ngưỡng) |

- **Kiểm định:** Binomial test (one-tailed, p₀ = 0.80)
- **Mức ý nghĩa:** α = 0.05
- **Vì sao chọn Binomial test?** Vì mỗi Gherkin scenario chỉ có **2 kết quả**: parse được (pass) hoặc lỗi cú pháp (fail) — đây là dữ liệu **nhị phân (binary)**. Binomial test kiểm tra xem tỷ lệ "pass" có thực sự lớn hơn 0.80 không. (One-tailed vì ta chỉ quan tâm chiều "lớn hơn".)

---

## Giải thích p-value (cô sẽ hỏi: "nếu p=0.03 thì kết luận gì?")

**p-value** = xác suất quan sát được kết quả này (hoặc cực đoan hơn) **nếu H0 đúng**.

### Tình huống p = 0.03:

- p = 0.03 **<** α = 0.05
- → **Bác bỏ H0** (reject the null hypothesis)
- → **Chấp nhận H1**
- → **Kết luận:** GPT-4o **ĐẠT** ngưỡng một cách có ý nghĩa thống kê (statistically significant).

**Diễn giải bằng lời:** "Chỉ có 3% khả năng kết quả này xảy ra ngẫu nhiên nếu thực sự GPT-4o chưa đạt ngưỡng. Vì 3% < 5% (mức ý nghĩa ta đặt ra), ta đủ tự tin kết luận GPT-4o thực sự đạt ngưỡng."

### Ngược lại — tình huống p = 0.12:

- p = 0.12 **>** α = 0.05
- → **KHÔNG bác bỏ được H0** (fail to reject)
- → **Kết luận:** Chưa đủ bằng chứng thống kê để khẳng định GPT-4o đạt ngưỡng. (Lưu ý: KHÔNG nói "H0 đúng" — chỉ nói "chưa đủ bằng chứng để bác bỏ H0".)

### Bảng tổng kết nhanh:

| p-value | So với α=0.05 | Quyết định | Ý nghĩa |
|---|---|---|---|
| p = 0.03 | p < α | Reject H0 → Accept H1 | GPT-4o đạt ngưỡng (significant) |
| p = 0.001 | p < α | Reject H0 → Accept H1 | GPT-4o đạt ngưỡng (rất significant) |
| p = 0.12 | p > α | Fail to reject H0 | Chưa đủ bằng chứng |
| p = 0.50 | p > α | Fail to reject H0 | Chưa đủ bằng chứng |

---

## Bổ sung (nâng cao điểm) — Bootstrap CI

Ngoài p-value, có thể báo cáo thêm **95% Bootstrap Confidence Interval** cho mean similarity (vd: 95% CI [0.84, 0.90]). Nếu khoảng tin cậy **nằm hoàn toàn trên 0.85** → củng cố thêm cho H1. Đây là cách trình bày kết quả mạnh hơn chỉ dùng p-value đơn thuần.

---

## Checklist Checkpoint 1.8

- [x] **H0 là phủ định** của điều muốn chứng minh (≤ ngưỡng)
- [x] **H1 là kỳ vọng** (> ngưỡng)
- [x] **Có tên kiểm định**: RQ1 → Wilcoxon signed-rank test; RQ2 → Binomial test
- [x] **Giải thích được "nếu p=0.03 thì kết luận gì?"**: p < 0.05 → reject H0 → GPT-4o đạt ngưỡng (significant)
