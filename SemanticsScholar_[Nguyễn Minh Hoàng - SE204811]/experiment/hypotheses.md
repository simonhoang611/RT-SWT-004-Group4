## Nguyên tắc viết H0/H1

|Quy tắc|Giải thích|
|-|-|
|**H0** = phủ định điều muốn chứng minh|Giả định "không có gì đặc biệt" — GPT-4o CHƯA đạt ngưỡng|
|**H1** = kỳ vọng đúng (one-tailed)|Điều nghiên cứu muốn chứng minh — GPT-4o ĐẠT ngưỡng|
|**alpha = 0.05**|Ngưỡng có ý nghĩa thống kê: nếu p < 0.05 → reject H0|
|**One-tailed test**|Chỉ quan tâm chiều "lớn hơn ngưỡng", không phải "khác ngưỡng"|

\---

## RQ1 — Semantic Similarity

### Phát biểu

> \\\*"Liệu GPT-4o zero-shot (temperature=0) có sinh Gherkin scenarios đạt cosine semantic similarity trung bình ≥ 0.85 so với expert-written scenarios không?"\\\*

### Cặp giả thuyết

$$H\_0^{(1)}: \\mu\_{sim} \\leq 0.85$$

$$H\_1^{(1)}: \\mu\_{sim} > 0.85$$

Trong đó `μ\\\_sim` = **median** cosine similarity (all-MiniLM-L6-v2) của tất cả cặp *(generated Gherkin, expert-written Gherkin)* trên ≥ 50 user stories.

> \\\*\\\*Lưu ý:\\\*\\\* Dùng \\\*\\\*median\\\*\\\* (micro-level) thay vì mean vì distribution cosine similarity thường lệch (skewed) — Wilcoxon test không yêu cầu normality.

### Kiểm định thống kê

|Thuộc tính|Giá trị|
|-|-|
|**Tên kiểm định**|Wilcoxon signed-rank test (one-tailed)|
|**Lý do chọn**|Không giả định normal distribution; phù hợp với dữ liệu similarity score (0–1, thường skewed); so sánh median với hằng số μ₀=0.85|
|**alpha**|0.05|
|**Chiều kiểm định**|One-tailed (greater than)|
|**μ₀ (null value)**|0.85|
|**Input data**|Vector cosine\_sim\[i] cho i = 1..N (N ≥ 50 user stories)|
|**Thư viện**|`scipy.stats.wilcoxon` (Python) hoặc `wilcox.test(mu=0.85, alternative="greater")` (R)|

### Cách đọc kết quả

|Kết quả kiểm định|Kết luận|
|-|-|
|**p < 0.05** (ví dụ: p = 0.03)|✅ **Reject H0** → Có đủ bằng chứng thống kê kết luận GPT-4o **ĐẠT** ngưỡng cosine similarity ≥ 0.85 (α=0.05)|
|**p ≥ 0.05** (ví dụ: p = 0.12)|❌ **Fail to reject H0** → Không đủ bằng chứng kết luận GPT-4o đạt ngưỡng — cần cải thiện prompt hoặc tăng dataset|
|**p = 0.001**|✅ Reject H0 mạnh — GPT-4o rõ ràng vượt ngưỡng 0.85|

**Ví dụ diễn giải cụ thể:**

> \\\*"Nếu p = 0.03 thì: vì 0.03 < α=0.05, ta reject H0(1). Kết luận: với mức ý nghĩa 5%, GPT-4o zero-shot đạt cosine semantic similarity trung bình > 0.85 so với expert-written Gherkin. Điều này hỗ trợ H1(1) — GPT-4o có khả năng tạo Gherkin scenarios đủ tương đồng ngữ nghĩa với expert."\\\*

\---

## RQ2 — Executable Syntax Rate

### Phát biểu

> \\\*"Liệu GPT-4o zero-shot (temperature=0) có sinh Gherkin scenarios với tỉ lệ parse không lỗi cú pháp ≥ 80% không (đo bằng Gherkin parser `behave`)?"\\\*

### Cặp giả thuyết

$$H\_0^{(2)}: p\_{exec} \\leq 0.80$$

$$H\_1^{(2)}: p\_{exec} > 0.80$$

Trong đó `p\\\_exec` = tỉ lệ Gherkin feature files **parse thành công** (không có lỗi cú pháp khi chạy qua `behave --dry-run`) trên tổng N feature files được generate.

### Kiểm định thống kê

|Thuộc tính|Giá trị|
|-|-|
|**Tên kiểm định**|Binomial test (one-tailed, exact)|
|**Lý do chọn**|Mỗi Gherkin file là biến nhị phân: parse được (1) hoặc không (0); kiểm định tỉ lệ thực tế so với ngưỡng p₀=0.80; exact test không cần large-sample approximation|
|**alpha**|0.05|
|**Chiều kiểm định**|One-tailed (greater than)|
|**p₀ (null proportion)**|0.80|
|**Input data**|k = số file parse thành công; N = tổng số file được generate (N ≥ 50)|
|**Thư viện**|`scipy.stats.binomtest(k, n=N, p=0.80, alternative='greater')` (Python)|

### Cách đọc kết quả

|Kết quả kiểm định|Kết luận|
|-|-|
|**p < 0.05** (ví dụ: p = 0.03)|✅ **Reject H0** → Có đủ bằng chứng thống kê kết luận tỉ lệ executable **vượt** ngưỡng 80% (α=0.05)|
|**p ≥ 0.05** (ví dụ: p = 0.21)|❌ **Fail to reject H0** → Không đủ bằng chứng kết luận executable rate > 80%|
|**p = 0.001**|✅ Reject H0 mạnh — executable rate rõ ràng vượt 80%|

**Ví dụ diễn giải cụ thể:**

> \\\*"Nếu p = 0.03 thì: vì 0.03 < α=0.05, ta reject H0(2). Kết luận: với mức ý nghĩa 5%, GPT-4o zero-shot đạt tỉ lệ Gherkin parse thành công > 80%. Điều này hỗ trợ H1(2) — các feature file được GPT-4o sinh ra có cú pháp hợp lệ đủ để chạy được bằng behave."\\\*

\---

## Tổng Hợp Cặp Giả Thuyết

|RQ|H0 (phủ định)|H1 (kỳ vọng)|Kiểm định|Alpha|
|-|-|-|-|-|
|**RQ1** — Semantic Similarity|μ\_sim ≤ 0.85|μ\_sim > 0.85|Wilcoxon signed-rank (one-tailed)|0.05|
|**RQ2** — Executable Syntax|p\_exec ≤ 0.80|p\_exec > 0.80|Binomial test (one-tailed, exact)|0.05|

\---

## Kế Hoạch Thực Nghiệm (Preview Bước 2)

Để kiểm định H0/H1, cần thu thập dữ liệu theo sơ đồ:

```
Input: ≥ 50 Connextra-format User Stories (≥ 3 SE projects)
         │
         ▼
   GPT-4o zero-shot (temperature=0, top\\\_p=1.0)
         │
         ▼
  Generated Gherkin feature files \\\[N files]
         │
    ┌────┴────┐
    ▼         ▼
\\\[RQ1]       \\\[RQ2]
Cosine sim  behave --dry-run
(each file  (each file:
vs expert)   parse OK/FAIL)
    │              │
    ▼              ▼
cosine\\\_sim\\\[i]  exec\\\_result\\\[i] ∈ {0,1}
    │              │
    ▼              ▼
Wilcoxon test  Binomial test
μ₀=0.85        p₀=0.80
    │              │
    ▼              ▼
p-value → so  p-value → so
sánh α=0.05   sánh α=0.05
```

### Output cần ghi lại sau thực nghiệm

|Biến|Mô tả|Dùng cho|
|-|-|-|
|`N`|Tổng số user stories đã test|Cả 2 RQ|
|`cosine\\\_sim\\\[i]`|Cosine similarity của US thứ i|RQ1 — Wilcoxon|
|`median\\\_sim`|Median của toàn bộ cosine\_sim|RQ1 — report|
|`k`|Số feature files parse thành công|RQ2 — Binomial|
|`exec\\\_rate`|k/N|RQ2 — report|
|`p\\\_val\\\_RQ1`|p-value từ Wilcoxon test|RQ1 — kết luận|
|`p\\\_val\\\_RQ2`|p-value từ Binomial test|RQ2 — kết luận|



