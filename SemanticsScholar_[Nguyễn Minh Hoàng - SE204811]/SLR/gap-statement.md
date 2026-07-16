## Phần A — Trả lời 4 câu hỏi GAP

\---

### Câu 1: LLM nào chưa được đánh giá?

*Cách trả lời: Liệt kê cột Tool/LLM từ evidence table*

|LLM / Approach|Papers đã dùng|Ghi chú|
|-|-|-|
|GPT-3.5 / ChatGPT-3.5|#3, #4, #5, #9, #12|Phổ biến nhất — 5 papers|
|GPT-4 / GPT-4 Turbo / GPT-4-Preview|#1, #2, #7, #10, #12, #13, #17|7 papers, nhưng temperature không cố định = 0|
|GPT-4o Mini|#2|Chỉ trong so sánh nhóm, không evaluate riêng|
|Gemini / PaLM-2|#1, #2, #3, #11, #12, #13|6 papers|
|Claude 3|#1|Duy nhất 1 paper, không phải primary focus|
|LLaMA 2/3, Phi-3, DeepSeek, Codex|#1, #2, #12, #17|Các open-source/alternative models|
|Rule-based (không LLM)|#6, #8, #14, #15, #16|5/17 papers hoàn toàn không dùng LLM|
|**GPT-4o (full, temperature=0, zero-shot)**|**Không paper nào**|**❌ CHƯA ĐƯỢC ĐÁNH GIÁ**|

**→ Ghi nhận:** GPT-4o (full version, temperature cố định = 0 để reproducibility) chưa được bất kỳ paper nào trong 17 papers evaluate chính thức cho task Gherkin generation từ Connextra-format user stories.
Trong số 7 papers dùng GPT-4, không paper nào fix temperature=0 và evaluate trên Connextra user stories với quantitative metrics chuẩn hóa.

**→ Chọn cho I trong PICO:** GPT-4o zero-shot (temperature=0)

\---

### Câu 2: Semantic similarity đã được dùng chưa?

*Cách trả lời: Đếm papers dùng metric này từ cột Metric*

|Loại semantic metric|Số papers|Papers cụ thể|
|-|-|-|
|METEOR (word-overlap + synonym)|2|#2 (Fernandes 2025), #1 (Rathnayake 2026)|
|BLEU / ROUGE-L (word-overlap)|2|#1 (Rathnayake 2026), #17 (Kavuri 2022)|
|BERTScore (contextual embedding)|2|#1 (Rathnayake 2026)|
|SentenceBERT Cosine Similarity (SBCS)|1|#1 (Rathnayake 2026) — dùng nhưng **KHÔNG** phải primary metric; không so với expert-written Gherkin theo chuẩn Connextra|
|**Cosine similarity (sentence-transformer, e.g., all-MiniLM-L6-v2) vs expert-written Gherkin làm PRIMARY metric**|**0**|**❌ KHÔNG paper nào**|

**Lưu ý quan trọng**: Paper #1 (Rathnayake 2026) có dùng SentenceBERT Cosine Similarity, nhưng: (a) dataset là proprietary software products, không phải Connextra-format user stories từ SE projects; (b) metric này không phải primary metric — primary vẫn là BLEU/METEOR/human eval; (c) không đặt ngưỡng cụ thể (≥0.85) để kết luận pass/fail.

**→ Đếm papers dùng embedding-based cosine similarity làm primary metric = 0**

**→ Ghi nhận: GAP về metric** — Cộng đồng chưa adopt cosine semantic similarity (sentence-transformer) làm primary metric để đánh giá Gherkin quality.
Lặp hạn chế này: 11/17 papers tự ghi nhận không đo hoặc thiếu semantic similarity (#2, #3, #4, #5, #7, #9, #10, #11, #12, #13, #17).

\---

### Câu 3: Executable syntax rate đã được đo chưa?

*Cách trả lời: Đếm papers đo executable rate từ cột Metric*

|Cách đo executable|Số papers|Papers cụ thể|
|-|-|-|
|Gherkin-lint syntax validation (không chạy thật)|1|#12 (Karpurapu 2024) — đo số lỗi syntax, nhưng dùng gherkin-lint tool, không phải parse+execute|
|Syntactic Correctness (human manual check)|2|#10 (Ferreira 2025): 100% syntactic correct — manual; #12: validation accuracy|
|Execution Success (PyTest/Selenium scripts)|1|#17 (Kavuri 2022): 92% execution success — nhưng là test scripts (Selenium/PyTest), **không phải Gherkin feature file**|
|Functional Correctness (Pass/Fail trên platform)|1|#13 (Almeyda 2025): 91.9% pass trên TestRigor — platform-specific, không reproducible với Gherkin parser chuẩn|
|**Executable syntax rate bằng Gherkin parser chuẩn hóa (behave / cucumber) làm PRIMARY metric**|**0**|**❌ KHÔNG paper nào**|

**→ Đếm papers đo executable rate bằng Gherkin parser = 0**

**→ Ghi nhận: GAP về metric** — Không có paper nào dùng Gherkin parser (behave hoặc cucumber) để đo tỉ lệ generated scenarios parse được không lỗi cú pháp, làm primary metric.
Lặp hạn chế này: 13/17 papers không đo executable syntax rate chuẩn hóa (#2, #3, #4, #5, #6, #7, #8, #9, #11, #12, #14, #15, #16).

\---

### Câu 4: Hạn chế nào lặp ≥ 2 lần?

*Cách trả lời: Quét cột Hạn chế tự nêu toàn bộ 17 papers*

|Hạn chế lặp lại|Số papers|Papers|
|-|-|-|
|Không đo / thiếu embedding-based semantic similarity|**11/17**|#1–5, #7, #10–13, #17|
|Không đo executable syntax rate chuẩn hóa|**13/17**|#2, #3, #4, #5, #6, #7, #8, #9, #11, #12, #14, #15, #16|
|Dataset nhỏ hoặc không có benchmark chuẩn|**11/17**|#2, #3, #4, #5, #7, #8, #9, #10, #12, #13, #14|
|Chỉ test 1 LLM hoặc không test GPT-4o full|**9/17**|#4, #5, #7, #9, #10, #11, #14, #15, #16|
|Đánh giá subjective / thiếu kiểm định thống kê|**8/17**|#3, #4, #5, #6, #8, #9, #11, #14|
|Chỉ 1 domain / 1 công ty, thiếu generalizability|**7/17**|#7, #10, #11, #13, #14, #15, #16|
|Không so sánh với human-written/expert Gherkin|**7/17**|#4, #5, #6, #9, #10, #11, #15|

**→ Ghi nhận:** Hạn chế **"không đo executable syntax" (13/17)** và **"không đo semantic similarity" (11/17)** là 2 GAP được cộng đồng thừa nhận rộng rãi nhất — đây là cơ sở vững chắc để justify 2 metrics O trong PICO.

\---

### Ngưỡng 0.85 lấy từ đâu?

*Tìm trong cột Kết quả/Metric của 17 papers*

Kết quả tìm kiếm:

* **Paper #2 (Fernandes 2025):** Gemini đạt METEOR = **0.84** (zero-shot) — gần nhất với ngưỡng 0.85, nhưng METEOR ≠ cosine similarity
* **Paper #1 (Rathnayake 2026):** BERTScore >89%, SBCS được báo cáo nhưng không đặt ngưỡng cụ thể
* **Không paper nào** đặt ngưỡng cosine similarity ≥0.85 như một acceptance threshold rõ ràng

**→ Kết luận về ngưỡng 0.85:**

> Không có paper nào trong 17 papers reviewed đặt ngưỡng cosine semantic similarity ≥0.85 làm acceptance threshold. Ngưỡng này được đặt bởi course instructor. Tuy nhiên, kết quả METEOR=0.84 của Fernandes et al. (2025) — model tốt nhất trong nghiên cứu so sánh 7 LLMs — cho thấy ngưỡng 0.85 là \\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\*realistic và challenging\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\* (frontier model hiện tại vừa đạt gần ngưỡng với word-overlap metric; embedding-based metric thường cho score cao hơn word-overlap).

**Nguồn ghi:** *Threshold ≥0.85 set by course instructor; consistent with top METEOR score reported by Fernandes et al. (2025) \[SBES 2025] — Gemini zero-shot METEOR=0.84.*

\---

## Phần B — GAP Statement

```
Tất cả 17 papers reviewed đều dùng template-based/rule-based approaches (6/17 papers)
hoặc GPT-3.5/GPT-4 với metric chủ yếu là BLEU, METEOR, human evaluation, hoặc
qualitative feedback (13/17 papers). Không có paper nào evaluate GPT-4o một cách
hệ thống trên Connextra-format user stories với metrics định lượng chuẩn hóa.

Tuy nhiên, KHÔNG paper nào trong 17 papers:

(1) Đánh giá GPT-4o zero-shot (temperature=0) cho task sinh Gherkin scenarios từ
    Connextra-format user stories ("As a... I want... So that...") từ SE projects
    \\\\\\\\\\\\\\\[gap về I trong PICO — xác nhận từ cột Tool/LLM: 0/17 papers]

(2) Đo cosine semantic similarity (sentence-transformer, all-MiniLM-L6-v2) giữa
    generated Gherkin và expert-written Gherkin làm primary metric với ngưỡng
    acceptance cụ thể \\\\\\\\\\\\\\\[gap về O-Metric 1 — xác nhận từ cột Metric: 0/17 papers dùng
    metric này làm primary; 11/17 papers tự ghi nhận hạn chế này]

(3) Đo executable syntax rate bằng Gherkin parser chuẩn hóa (behave/cucumber) làm
    primary metric \\\\\\\\\\\\\\\[gap về O-Metric 2 — xác nhận từ cột Metric: 0/17 papers; 13/17
    papers tự ghi nhận hạn chế này]
```

**→ GAP:**
Chưa có nghiên cứu nào đánh giá frontier LLM (GPT-4o zero-shot, temperature=0) trên Gherkin acceptance test generation từ Connextra-format user stories, sử dụng embedding-based semantic similarity và executable syntax rate làm primary metrics so sánh với expert-written scenarios. Các nghiên cứu gần nhất (Rathnayake et al., 2026; Fernandes et al., 2025) hoặc dùng dataset proprietary không phải Connextra user stories, hoặc chỉ dùng word-overlap metrics (METEOR, BLEU) mà không đặt ngưỡng acceptance threshold rõ ràng, hoặc không test GPT-4o full version.

**→ Contribution:**
Nghiên cứu này lấp GAP bằng cách đánh giá GPT-4o zero-shot (temperature=0) trên ≥50 Connextra-format user stories từ ≥3 SE projects, đo: (1) cosine similarity (all-MiniLM-L6-v2) ≥0.85 so với expert-written Gherkin, và (2) executable syntax rate ≥80% bằng Gherkin parser (behave). Đây là nghiên cứu đầu tiên kết hợp cả 2 metrics chuẩn hóa này cho GPT-4o trên Connextra user stories.

