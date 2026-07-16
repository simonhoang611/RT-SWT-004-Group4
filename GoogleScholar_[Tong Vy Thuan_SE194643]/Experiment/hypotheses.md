# Hypotheses — SLR: LLM-Based Test Case Generation

---

## RQ1 — Gherkin Syntax Accuracy

**H₀:** Các open-source LLM (LLaMA-3-8B-Instruct, Mistral-7B-Instruct, DeepSeek-Coder-7B) với few-shot prompting KHÔNG đạt Gherkin syntax accuracy ≥ 90% khi sinh test scenarios từ user stories.

**H₁:** Ít nhất một trong ba open-source LLM nói trên ĐẠT Gherkin syntax accuracy ≥ 90% với few-shot prompting.

**Statistical test:** Binomial exact test (one-tailed)
- **Lý do:** Output là nhị phân (scenario pass/fail Gherkin-lint) trên N scenarios per model
- **Null proportion p₀:** 0.90
- **α:** 0.05
- **Cách thực hiện:** `scipy.stats.binomtest(k=n_pass, n=N, p=0.90, alternative='greater')`

---

## RQ2 — Semantic Similarity (BERTScore F1)

**H₀:** BERTScore F1 trung vị của Gherkin scenarios sinh bởi các open-source LLM KHÔNG đạt ≥ 0.70 so với reference scenarios chuyên gia.

**H₁:** BERTScore F1 trung vị của Gherkin scenarios sinh bởi ít nhất một mô hình ĐẠT ≥ 0.70.

**Statistical test:** Wilcoxon signed-rank test (one-sample, one-tailed)
- **Lý do:** Output là liên tục (BERTScore F1 ∈ [0,1] per scenario); phân phối không chắc normal; paired so với threshold
- **μ₀:** 0.70
- **α:** 0.05
- **Cách thực hiện:** `scipy.stats.wilcoxon(bertscore_f1 - 0.70, alternative='greater')`
- **Effect size:** Cliff's delta (d) hoặc r = Z/√N

---

## RQ3 — So sánh giữa các mô hình

**H₀:** Không có sự khác biệt thống kê đáng kể về BERTScore F1 giữa các open-source LLM và GPT-3.5-Turbo baseline.

**H₁:** Ít nhất một open-source LLM có phân phối BERTScore F1 khác biệt có ý nghĩa thống kê so với GPT-3.5-Turbo.

**Statistical test:** Mann-Whitney U test (two-tailed, pairwise)
- **Lý do:** So sánh 2 hệ thống độc lập trên phân phối BERTScore F1; không giả định normal distribution
- **α:** 0.05 (với Bonferroni correction cho 3 cặp so sánh: α_adjusted = 0.05/3 ≈ 0.017)
- **Cách thực hiện:** `scipy.stats.mannwhitneyu(scores_llm_i, scores_gpt35, alternative='two-sided')`
- **Effect size:** r = Z/√(n₁+n₂) hoặc Cohen's d nếu phân phối gần normal

---

## Bảng tóm tắt lựa chọn statistical test

| RQ | Output type | Test | Lý do chọn |
|---|---|---|---|
| RQ1 (syntax %) | Nhị phân (pass/fail) | Binomial exact test | So với ngưỡng cố định p₀=0.90 |
| RQ2 (BERTScore) | Liên tục (F1 per scenario) | Wilcoxon signed-rank | So với ngưỡng μ₀=0.70, non-parametric |
| RQ3 (model comparison) | Liên tục (F1 per scenario) | Mann-Whitney U | So sánh 2 hệ thống, non-parametric |

> **Nguyên tắc chọn test (áp dụng ngay, không đợi pilot):**
> - Output liên tục (cosine similarity, F1, BERTScore) → **Wilcoxon signed-rank** (so với ngưỡng) hoặc **Mann-Whitney U** (so với hệ thống khác)
> - Output nhị phân (% pass syntax, % executable) → **Binomial exact test**
> - So sánh 2 hệ thống trên output liên tục → **Mann-Whitney U**
> - Nếu N > 30 và phân phối gần normal (kiểm tra với Shapiro-Wilk) → có thể bổ sung paired t-test để cross-validate

---

## Ghi chú về power analysis

Với N ≈ 836 user stories, power tối thiểu 0.80 ở α=0.05:

| Test | Effect size cần phát hiện | N tối thiểu | N thực tế |
|---|---|---|---|
| Binomial (RQ1) | p-p₀ = 0.05 | ~220 | 836 ✓ |
| Wilcoxon (RQ2) | d = 0.20 (small) | ~200 | 836 ✓ |
| Mann-Whitney (RQ3) | d = 0.20 (small) | ~400 per group | 836 tổng ✓ |

Kích thước mẫu đủ để phát hiện effect nhỏ. Không cần pilot power analysis trước khi chạy experiment.
