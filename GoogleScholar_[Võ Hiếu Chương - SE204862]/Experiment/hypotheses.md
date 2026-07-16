# Hypotheses
*Date: 2026-05-31 | Derived from: 01_rq.md + gap-statement.md*

---

## Nguyên tắc viết H0/H1

| Quy tắc | Giải thích |
|---|---|
| **H0** = phủ định điều muốn chứng minh | Giả định "không có gì đặc biệt" — GPT-4o **CHƯA** đạt ngưỡng |
| **H1** = kỳ vọng đúng (one-tailed) | Điều nghiên cứu muốn chứng minh — GPT-4o **ĐẠT** ngưỡng |
| **alpha = 0.05** | Nếu p < 0.05 → reject H0 |
| **One-tailed** | Chỉ kiểm tra chiều "greater than" vì không quan tâm nếu GPT-4o kém hơn ngưỡng |

---

## RQ1 — Semantic Similarity

> *"Liệu GPT-4o zero-shot (temperature=0) có sinh Gherkin scenarios đạt cosine
> semantic similarity trung bình ≥ 0.85 so với expert-written scenarios không?"*

**H₀⁽¹⁾: μ\_sim ≤ 0.85** — GPT-4o CHƯA đạt ngưỡng semantic similarity

**H₁⁽¹⁾: μ\_sim > 0.85** — GPT-4o ĐẠT ngưỡng semantic similarity

| Thuộc tính | Giá trị | Lý do |
|---|---|---|
| **Tên kiểm định** | Wilcoxon signed-rank test (one-tailed) | Không giả định normal distribution; phù hợp similarity score (0–1, thường skewed left/right) |
| **Lý do chọn Wilcoxon** | Scores cosine similarity không đảm bảo phân phối chuẩn; Wilcoxon robust hơn t-test | #3 (Rathnayake) dùng human scores không chuẩn → precedent cho non-parametric test |
| **Alternative to Wilcoxon** | One-sample t-test nếu n≥30 và distribution gần chuẩn (Central Limit Theorem) | Kiểm tra shapiro-wilk trước khi chọn |
| **alpha (α)** | 0.05 | Standard threshold trong SE research |
| **Chiều kiểm định** | One-tailed (greater than μ₀=0.85) | Chỉ quan tâm GPT-4o có vượt ngưỡng không |
| **μ₀ (null value)** | 0.85 | **Instructor-assigned pilot threshold.** METEOR=0.75 (#3, #5) không convert trực tiếp sang cosine — hai metric khác nhau. Ngưỡng 0.85 là baseline đầu tiên cho cosine sentence-level trong domain này; sẽ được validate bằng kết quả thực nghiệm. |
| **Metric đo** | Cosine similarity (all-MiniLM-L6-v2, sentence-transformers) | 0/12 papers trong SLR dùng metric này — đây là contribution |
| **Unit of analysis** | 1 user story = 1 cosine score (GPT-4o scenario vs. expert scenario) | |

### Cách tính cosine similarity

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_cosine(gpt_scenario: str, expert_scenario: str) -> float:
    emb = model.encode([gpt_scenario, expert_scenario])
    return float(cosine_similarity([emb[0]], [emb[1]])[0][0])
```

### Cách đọc kết quả

| Kết quả p-value | Kết luận | Câu viết kết quả |
|---|---|---|
| **p = 0.03 < 0.05** | ✅ Reject H₀⁽¹⁾ → GPT-4o **ĐẠT** ngưỡng | "Vì p=0.03 < α=0.05, ta reject H₀⁽¹⁾. Kết luận: GPT-4o zero-shot đạt cosine semantic similarity > 0.85 so với expert-written Gherkin (α=0.05)." |
| **p = 0.12 ≥ 0.05** | ❌ Fail to reject H₀⁽¹⁾ → không đủ bằng chứng | "Vì p=0.12 ≥ α=0.05, ta fail to reject H₀⁽¹⁾. Không đủ bằng chứng thống kê để kết luận GPT-4o đạt ngưỡng similarity ≥ 0.85." |

### Ngữ cảnh từ SLR

- Best reported METEOR = **0.75** (#3 Rathnayake, #5 Fernandes) — đây là ceiling hiện tại của SLR
- Cosine similarity sentence-level thường > METEOR vì không yêu cầu exact token overlap
- Ngưỡng 0.85 là instructor-assigned pilot threshold — METEOR=0.75 không convert trực tiếp sang cosine. Tuy nhiên, cosine sentence-level thường cao hơn METEOR cho cùng scenario vì không yêu cầu exact token overlap → 0.85 là ambitious nhưng không phi lý. Đây là baseline đầu tiên cho metric này trong domain.

---

## RQ2 — Executable Syntax Rate

> *"Liệu GPT-4o zero-shot có sinh Gherkin scenarios với tỉ lệ parse không lỗi ≥ 80%
> khi dùng `behave --dry-run` không?"*

**H₀⁽²⁾: p\_exec ≤ 0.80** — Executable rate CHƯA đạt ngưỡng 80%

**H₁⁽²⁾: p\_exec > 0.80** — Executable rate ĐẠT ngưỡng 80%

| Thuộc tính | Giá trị | Lý do |
|---|---|---|
| **Tên kiểm định** | Binomial test (one-tailed, exact) | Mỗi file là nhị phân: parse được (1) hoặc không (0); exact vì n có thể nhỏ (<100) |
| **Lý do chọn Binomial** | Outcome là binary pass/fail; không cần giả định phân phối | Chuẩn cho proportion hypothesis testing |
| **alpha (α)** | 0.05 | |
| **p₀ (null proportion)** | 0.80 | Baseline: #1 (Karpurapu) ~98%, #4 (Fonseca) 93.3% → 80% là conservative lower bound |
| **Chiều kiểm định** | One-tailed (greater than p₀=0.80) | |
| **Unit of analysis** | 1 feature file = 1 binary outcome (behave parses / không parse) | |
| **Tool đo** | `behave --dry-run <feature_file>` — exit code 0 = pass, non-zero = fail | 0/12 papers dùng tool này — đây là contribution |

### Cách đo executable rate

```bash
#!/bin/bash
PASS=0; FAIL=0
for f in generated_scenarios/*.feature; do
    if behave --dry-run "$f" > /dev/null 2>&1; then
        PASS=$((PASS+1))
    else
        FAIL=$((FAIL+1))
    fi
done
echo "Executable rate: $PASS / $((PASS+FAIL))"
```

```python
from scipy.stats import binomtest

# Ví dụ: 45/50 files parse được
result = binomtest(k=45, n=50, p=0.80, alternative='greater')
print(f"p-value = {result.pvalue:.4f}")
# p-value = 0.0185 → reject H0
```

### Cách đọc kết quả

| Kết quả p-value | Kết luận | Câu viết kết quả |
|---|---|---|
| **p = 0.02 < 0.05** | ✅ Reject H₀⁽²⁾ → executable rate **vượt** 80% | "Vì p=0.02 < α=0.05, ta reject H₀⁽²⁾. Kết luận: GPT-4o zero-shot đạt executable syntax rate > 80% theo behave parser (α=0.05)." |
| **p = 0.21 ≥ 0.05** | ❌ Fail to reject H₀⁽²⁾ | "Vì p=0.21 ≥ α=0.05, ta fail to reject H₀⁽²⁾. Không đủ bằng chứng GPT-4o đạt executable rate ≥ 80%." |

### Ngữ cảnh từ SLR

- #1 (Karpurapu): ~**98%** feature files không syntax error (Gherkin-lint, few-shot) → upper bound
- #4 (Fonseca/AToMIC): **93.3%** Gherkin syntactically correct (DeepSeek, zero-shot local)
- Ngưỡng 80% là **conservative** so với SLR baselines → realistic để đạt được

---

## Tổng Hợp

| RQ | H₀ | H₁ | Kiểm định | Alpha | Metric | Ngưỡng |
|---|---|---|---|---|---|---|
| **RQ1** | μ\_sim ≤ 0.85 | μ\_sim > 0.85 | Wilcoxon signed-rank (one-tailed) | 0.05 | Cosine similarity (all-MiniLM-L6-v2) | 0.85 |
| **RQ2** | p\_exec ≤ 0.80 | p\_exec > 0.80 | Binomial test (one-tailed, exact) | 0.05 | Executable rate (behave --dry-run) | 80% |

---

## Kịch bản kết quả có thể xảy ra

| Kịch bản | RQ1 | RQ2 | Diễn giải |
|---|---|---|---|
| **Best case** | ✅ Reject H₀⁽¹⁾ | ✅ Reject H₀⁽²⁾ | GPT-4o đạt cả 2 ngưỡng → strong evidence for adoption |
| **Partial (semantic OK)** | ✅ Reject H₀⁽¹⁾ | ❌ Fail | Scenario có nghĩa nhưng syntax lỗi → cần post-processing |
| **Partial (syntax OK)** | ❌ Fail | ✅ Reject H₀⁽²⁾ | Syntax đúng nhưng ngữ nghĩa kém → cần few-shot hoặc fine-tuning |
| **Worst case** | ❌ Fail | ❌ Fail | GPT-4o zero-shot không đủ → đề xuất few-shot hoặc model khác |

---

*File này được derive từ: gap-statement.md (12 papers SLR) và 01_rq.md (PICO refinement).*
