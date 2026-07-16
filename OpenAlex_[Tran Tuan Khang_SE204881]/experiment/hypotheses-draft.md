# Hypotheses Draft — LLM for Gherkin/BDD Acceptance Test Generation
Ngày: 2026-06-07

> Threshold sources: design-rationale.md | GAP source: SLR/gap-analysis.md

---

## RQ1 — Semantic Similarity

**RQ1:** Does GPT-4o zero-shot (temperature=0) generate Gherkin scenarios that achieve
cosine semantic similarity ≥ 0.85 (using `sentence-transformers/all-MiniLM-L6-v2`)
compared to expert-written Gherkin for the same Connextra user stories?

**H0:** GPT-4o zero-shot KHÔNG đạt cosine semantic similarity ≥ 0.85 so với expert-written Gherkin.
> Formal: median(cosine_similarity) ≤ 0.85

**H1:** GPT-4o zero-shot ĐẠT cosine semantic similarity ≥ 0.85 so với expert-written Gherkin.
> Formal: median(cosine_similarity) > 0.85

**Statistical test dự kiến:** Wilcoxon signed-rank test (one-tailed, α = 0.05)
- Output là điểm số liên tục [0,1] → non-parametric test phù hợp
- Threshold 0.85 từ Paper 5 (SBES 2025): floor = 0.84, làm tròn = 0.85

---

## RQ2 — Executable Syntax Rate

**RQ2:** Does GPT-4o zero-shot (temperature=0) achieve an executable syntax rate ≥ 80%
when generating Gherkin scenarios from Connextra user stories (measured by `behave 1.2.6`
dry-run parser)?

**H0:** GPT-4o zero-shot KHÔNG đạt executable syntax rate ≥ 80% (tỷ lệ scenario parse thành công ≤ 80%).
> Formal: executable_rate ≤ 0.80

**H1:** GPT-4o zero-shot ĐẠT executable syntax rate > 80% (tỷ lệ scenario parse thành công > 80%).
> Formal: executable_rate > 0.80

**Statistical test dự kiến:** Binomial exact test (one-tailed, p₀ = 0.80, α = 0.05)
- Output là nhị phân (pass/fail per scenario) → Binomial exact test phù hợp
- Threshold 80% từ Paper 7 (IEEE Access 2024): floor = 79%, làm tròn = 80%

---

## Ghi chú

- Hypothesis phải viết **sau** khi có Metric và Threshold từ design-rationale.md — không viết trước.
- Cả hai H0 đều là absolute threshold claim (không so sánh với tool khác).
- Nếu pilot (Tuần 7) cho thấy phân phối cosine similarity gần normal → có thể xem xét chuyển sang one-sample t-test, ghi amendment vào proposal §8.6.
- `rq-final.md` **chưa cập nhật** ở bước này — RQ final nằm ở `proposal.md` Section 4 (RBL-3).
