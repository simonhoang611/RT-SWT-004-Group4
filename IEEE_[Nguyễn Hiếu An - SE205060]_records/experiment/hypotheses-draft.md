# Hypotheses Draft — LLM for Acceptance Test Automation (BDD/Gherkin)

**Thành viên:** Nguyễn Hiếu An (SE205060)  
**Ngày:** 2026-06-__ · **Threshold source:** experiment/design-rationale.md

> File này thay thế `hypotheses.md` từ RBL-1 — cụ thể hơn vì threshold đã có nguồn (Case 1/2/3) thay vì draft sơ bộ.

---

## RQ cuối cùng

> "GPT-4o zero-shot (temperature=0) có sinh được Gherkin acceptance test từ **30–50 user story Connextra (P)** đạt **cosine semantic similarity ≥ 0.85 (O1)** so với **expert-written Gherkin (C)** VÀ **executable syntax rate ≥ 80% (O2)** không?"

---

## RQ1 — Semantic Similarity

- **H0₁:** GPT-4o KHÔNG đạt cosine similarity ≥ 0.85 (μ_similarity ≤ 0.85)
- **H1₁:** GPT-4o ĐẠT cosine similarity ≥ 0.85 (μ_similarity > 0.85)
- **Statistical test dự kiến:** Wilcoxon signed-rank test (α = 0.05)
- **Threshold source:** Case 3 — không có paper dùng cosine sentence-transformer; mini-pilot 5–10 sample xác nhận; tham chiếu Varpe 2025 (BERTScore ≈ 0.81)
- **Vì sao Wilcoxon:** output là điểm số liên tục (cosine 0–1); test median có > ngưỡng không; không giả định phân phối chuẩn (dataset nhỏ)

## RQ2 — Executable Syntax

- **H0₂:** GPT-4o KHÔNG đạt executable rate ≥ 80% (rate ≤ 0.80)
- **H1₂:** GPT-4o ĐẠT executable rate ≥ 80% (rate > 0.80)
- **Statistical test dự kiến:** Binomial exact test (one-tailed, p₀ = 0.80, α = 0.05)
- **Threshold source:** Case 2 — floor = 80% từ Storer 2019 (white box success rate)
- **Vì sao Binomial:** output nhị phân (mỗi scenario: parse được / lỗi cú pháp); test tỉ lệ pass có > 0.80 không

---

## Bảng chọn statistical test (tham chiếu)

| Loại output | Test | RQ áp dụng |
|---|---|---|
| Liên tục (cosine, F1, BLEU) | Wilcoxon signed-rank | RQ1 (cosine similarity) |
| Nhị phân (% executable, pass/fail) | Binomial exact test | RQ2 (executable rate) |
| So sánh 2 hệ thống | Mann-Whitney U | (không dùng — không so 2 LLM) |

---

## Giải thích p-value (cô sẽ hỏi: "p=0.03 thì kết luận gì?")

- p = 0.03 **<** α = 0.05 → **bác bỏ H0** → **chấp nhận H1** → GPT-4o ĐẠT ngưỡng (có ý nghĩa thống kê).
- Diễn giải: chỉ 3% khả năng kết quả này là ngẫu nhiên nếu H0 đúng; vì 3% < 5% nên đủ tự tin kết luận.
- ⚠️ Khi p > 0.05: chỉ nói "chưa đủ bằng chứng bác bỏ H0", KHÔNG nói "H0 đúng".

---

## Lưu ý về pilot (theo rubric)

Mini-pilot Tuần 7 chỉ để **confirm** threshold/test — nếu phân phối thực tế khác dự kiến → ghi amendment theo proposal §8.6, KHÔNG phải lần đầu chọn test. Test đã chọn ngay bây giờ (Wilcoxon + Binomial) dựa trên loại output, không đợi pilot.

---

## Checklist (rubric RBL-2)

- [x] H0 testable, có giá trị ngưỡng cụ thể (0.85; 0.80)
- [x] H1 là đối lập logic của H0
- [x] Statistical test dự kiến phù hợp loại dữ liệu (Wilcoxon cho liên tục, Binomial cho nhị phân)
- [x] Threshold trong H0 khớp với design-rationale.md (Case 3 cho RQ1, Case 2 cho RQ2)
