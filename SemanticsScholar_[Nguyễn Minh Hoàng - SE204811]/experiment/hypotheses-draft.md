# Hypotheses Draft — LLM for Acceptance Test Automation (BDD/Gherkin)
Ngày: 2026-06-14

## RQ1 — Semantic Similarity
**RQ1:** GPT-4o (full version, zero-shot, temperature=0) có tạo Gherkin acceptance test scenarios từ Connextra-format user stories đạt cosine semantic similarity (all-MiniLM-L6-v2) ≥ 0.85 so với expert-written Gherkin không?

H0: GPT-4o (full version, zero-shot, temperature=0) KHÔNG đạt mức trung vị cosine semantic similarity ≥ 0.85 so với expert-written Gherkin.
H1: GPT-4o (full version, zero-shot, temperature=0) ĐẠT mức trung vị cosine semantic similarity ≥ 0.85 so với expert-written Gherkin.
Statistical test dự kiến: Wilcoxon signed-rank test (α = 0.05)

## RQ2 — Executable Syntax Rate
**RQ2:** GPT-4o (full version, zero-shot, temperature=0) có tạo Gherkin acceptance test scenarios từ Connextra-format user stories đạt executable syntax rate (parse thành công bằng `behave --dry-run`) ≥ 80% không?

H0: Tỉ lệ Gherkin acceptance test scenarios do GPT-4o sinh ra (zero-shot, temperature=0) có thể parse thành công bằng `behave --dry-run` KHÔNG đạt mức ≥ 80%.
H1: Tỉ lệ Gherkin acceptance test scenarios do GPT-4o sinh ra (zero-shot, temperature=0) có thể parse thành công bằng `behave --dry-run` ĐẠT mức ≥ 80%.
Statistical test dự kiến: Binomial exact test (α = 0.05)
