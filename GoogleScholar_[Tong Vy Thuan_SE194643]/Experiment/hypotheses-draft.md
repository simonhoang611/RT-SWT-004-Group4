# Hypotheses Draft — LLM-Based BDD/Gherkin Test Generation
Ngày: 2025-06-10

## RQ1 — Độ tương đồng ngữ nghĩa

**H0:** GPT-4o zero-shot (temperature=0) KHÔNG đạt cosine similarity (all-MiniLM-L6-v2) trung bình ≥ 0.88 so với expert-written Gherkin khi sinh từ Connextra user stories.

**H1:** GPT-4o zero-shot (temperature=0) ĐẠT cosine similarity (all-MiniLM-L6-v2) trung bình ≥ 0.88 so với expert-written Gherkin khi sinh từ Connextra user stories.

**Statistical test dự kiến:** Wilcoxon signed-rank test (α = 0.05)

**Lý do:** Cosine similarity là dữ liệu liên tục (0–1), phân phối không rõ ràng → dùng non-parametric test. Wilcoxon signed-rank test xem median của mẫu có ≥ ngưỡng không — đúng với loại claim absolute threshold theo rubric 5B.

---

## RQ2 — Tính thực thi (Executable rate)

**H0:** GPT-4o zero-shot KHÔNG đạt tỷ lệ Gherkin scenarios thực thi thành công không lỗi cú pháp ≥ 90%.

**H1:** GPT-4o zero-shot ĐẠT tỷ lệ Gherkin scenarios thực thi thành công không lỗi cú pháp ≥ 90%.

**Statistical test dự kiến:** Binomial exact test (α = 0.05)

**Lý do:** Executable rate là dữ liệu nhị phân (pass/fail) — đếm tỉ lệ, không phải điểm số liên tục → Binomial exact test phù hợp để kiểm định tỉ lệ có ≥ ngưỡng không, theo bảng loại output rubric 5B.
