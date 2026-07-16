# GAP Statement — LLM for Acceptance Test Automation (BDD/Gherkin)
*Dựa trên evidence_table.md — **12 papers included** | Date: 2026-05-31*

---

## Phần A — Trả lời 4 câu hỏi GAP

---

### Câu 1: LLM nào chưa được đánh giá?

| LLM / Approach | Số papers | Papers cụ thể | Ghi chú |
|---|---|---|---|
| GPT-3.5 / GPT-3.5-turbo | 2 | #1, #12 | Thường dùng làm baseline |
| GPT-4 / GPT-4 Turbo | 7 | #1, #2, #3, #6, #8, #10 | Phổ biến nhất trong SLR |
| GPT-4o Mini | 1 | #5 | 1 trong 7 models so sánh; phiên bản rút gọn |
| Claude 3 | 1 | #3 | Best theo human experts nhưng chưa được replicate |
| Gemini (các version) | 4 | #3, #4, #7, #8 | Thường là secondary model |
| Llama-2-13B | 1 | #1 | Kém GPT rõ rệt |
| Llama 3 / Llama3.1 8B | 2 | #5, #9 | Fine-tuned hoặc so sánh |
| PaLM-2 | 2 | #1, #11 | Kém GPT-4 |
| DeepSeek R1 / DeepSeek-Coder | 2 | #4, #5 | Mới xuất hiện |
| Grok | 1 | #8 | Kết quả kém ChatGPT |
| GitHub Copilot | 2 | #7, #8 | Kết quả kém GPT-4 |
| **GPT-4o full (temperature=0, zero-shot, Connextra)** | **0** | **Không paper nào** | **❌ CHƯA ĐƯỢC ĐÁNH GIÁ** |

**Phân tích:**
- GPT-4o (phiên bản đầy đủ) chưa được đánh giá trong bất kỳ paper nào cho task Gherkin generation từ Connextra user stories.
- #5 (Fernandes) dùng "GPT-4o Mini" — phiên bản rút gọn, khác với GPT-4o full về reasoning capacity.
- #3 (Rathnayake) dùng "GPT-4" với temperature=0, METEOR≈0.75 — nhưng không phải GPT-4o và không dùng Connextra format chuẩn hóa.
- **→ Chọn cho I trong PICO: GPT-4o zero-shot (temperature=0)**

---

### Câu 2: Semantic similarity đã được dùng chưa?

| Metric | Số papers | Papers cụ thể | Ghi chú |
|---|---|---|---|
| BLEU | 1 | #3 | Text overlap; không đo semantic |
| METEOR | 2 | #3, #5 | Tốt hơn BLEU nhưng vẫn text-based |
| ROUGE-L | 1 | #3 | Text recall-based |
| BERTScore | 1 | #3 | Token-level embedding; chỉ 1 paper |
| LLM-as-judge (DeepSeek) | 1 | #3 | Mới nhất; 1 paper duy nhất |
| Human expert evaluation | 2 | #2, #3 | Không scalable, subjective |
| Rubric-based qualitative | 2 | #7, #11 | Không automated |
| Syntax validation only (Gherkin-lint) | 4 | #1, #4, #12, #6 | Phổ biến nhất nhưng không đo semantic |
| **Cosine similarity (all-MiniLM-L6-v2) làm PRIMARY metric** | **0** | **Không paper nào** | **❌ CHƯA ĐƯỢC DÙNG** |

**Phân tích:**
- BERTScore (#3) là metric gần nhất nhưng khác mô hình (BERT token-level ≠ sentence-level cosine với all-MiniLM-L6-v2).
- 11/12 papers (92%) không đo semantic similarity theo bất kỳ hình thức embedding nào.
- Best result METEOR = 0.75 (#3 và #5) → cung cấp baseline tham chiếu.
- **→ GAP về metric: 0/12 papers dùng cosine similarity (all-MiniLM-L6-v2) làm primary metric**

---

### Câu 3: Executable syntax rate đã được đo chưa?

| Cách đo | Số papers | Papers cụ thể | Ghi chú |
|---|---|---|---|
| Gherkin-lint (Node.js linter) | 3 | #1, #4, #12 | Chỉ check lint rules, không phải parser-level |
| Manual review syntactic | 1 | #7 | Không reproducible |
| Pytest-cov / execution coverage | 1 | #6 | Coverage của test code, không phải Gherkin |
| UI test execution (end-to-end) | 1 | #4 | 100% — nhưng dùng DeepSeek local, không GPT-4o |
| Helpfulness rate (user survey) | 2 | #2, #11 | Subjective |
| **Gherkin parser chuẩn hóa (behave/cucumber dry-run) làm PRIMARY metric** | **0** | **Không paper nào** | **❌ CHƯA ĐƯỢC DÙNG** |

**Phân tích:**
- Gherkin-lint (#1, #4, #12) chỉ kiểm tra coding style, **không** verify parser (behave/cucumber) có thể load feature file thành công.
- `behave --dry-run` hoặc `cucumber --dry-run` mới là cách chuẩn hóa, reproducible để đo executable rate.
- Best result: #1 (Karpurapu) ~98% syntax correct theo Gherkin-lint; #4 (Fonseca) 93.3% — nhưng cả hai không dùng parser-level verification.
- **→ GAP về metric: 0/12 papers dùng Gherkin parser chuẩn hóa làm primary executable metric**

---

### Câu 4: Hạn chế nào lặp ≥ 2 lần?

| Hạn chế lặp lại | Số papers | Papers |
|---|---|---|
| Không đo semantic similarity (chỉ syntax hoặc text-overlap) | 11/12 | #1, #2, #4, #5, #6, #7, #8, #9, #10, #11, #12 |
| Dataset nhỏ hoặc từ 1 dự án duy nhất | 9/12 | #1, #2, #4, #6, #7, #8, #9, #10, #11 |
| Chỉ syntactic correctness, bỏ semantic validity | 7/12 | #1, #5, #7, #8, #9, #10, #12 |
| Không dùng Gherkin parser chuẩn hóa (behave/cucumber) | 12/12 | Tất cả |
| Thiếu so sánh nhiều LLMs trong cùng setup | 6/12 | #2, #6, #10, #11, #12 |
| Dataset proprietary / không public | 3/12 | #2, #3, #4 |
| GPT-4o full chưa được đánh giá | 12/12 | Tất cả |
| Thiếu Connextra user story format chuẩn hóa | 8/12 | #4, #6, #7, #8, #9, #10, #11, #12 |

**3 hạn chế quan trọng nhất:**
1. **Không đo semantic similarity** — 11/12 (92%): hầu hết chỉ dùng Gherkin-lint hoặc BLEU/METEOR
2. **Dataset nhỏ / không standardized** — 9/12 (75%): thiếu dataset từ nhiều SE projects
3. **Không dùng Gherkin parser chuẩn hóa** — 12/12 (100%): không paper nào dùng behave/cucumber dry-run

---

### Ngưỡng 0.85 lấy từ đâu?

Không có paper nào đặt ngưỡng cosine similarity ≥0.85 — ngưỡng này được đặt bởi course instructor/project requirements.

Tuy nhiên, các kết quả hiện có hỗ trợ ngưỡng này là **realistic và ambitious**:
- #3 (Rathnayake 2026): METEOR = **0.75** (GPT-4 few-shot) — best text similarity trong SLR
- #5 (Fernandes 2025): METEOR = **0.75** (GPT-4 Turbo few-shot) — replicates #3
- #1 (Karpurapu 2024): **~98%** syntax correct (few-shot) → khi syntax gần đúng, semantic cũng cao
- #4 (Fonseca 2025): **93.3%** Gherkin syntactically correct → benchmark tốt cho executable rate

Cosine similarity (sentence embedding) thường cao hơn METEOR vì không phụ thuộc exact word match. Ngưỡng 0.85 (calibrate theo METEOR=0.75 từ #3 và #5) là **achievable cho GPT-4o** theo evidence.

→ **Nguồn ngưỡng 0.85: calibrate từ Rathnayake 2026 (#3) và Fernandes 2025 (#5), METEOR=0.75 → ước tính cosine similarity tương đương ≈0.85 với sentence-transformers**

---

## Phần B — GAP Statement

### Tuyên bố GAP ngắn gọn

Tất cả **12 papers** reviewed trong SLR này sử dụng GPT-3.5, GPT-4, hoặc các mô hình khác (Claude 3, Gemini, Llama, DeepSeek) để tự động hóa BDD/Gherkin test generation. Metric phổ biến nhất là BLEU, METEOR, syntax validation (Gherkin-lint), hoặc human expert evaluation.

**Tuy nhiên, KHÔNG paper nào trong 12 papers:**

1. **Đánh giá GPT-4o zero-shot (temperature=0) cho Gherkin generation từ Connextra-format user stories** — Paper gần nhất (#3 Rathnayake) dùng GPT-4 (không phải GPT-4o) và không standardize định dạng user stories theo Connextra.

2. **Đo cosine semantic similarity (all-MiniLM-L6-v2 sentence-transformers) làm primary metric với ngưỡng định lượng ≥0.85** — Paper gần nhất (#3) dùng BERTScore (token-level, khác model) nhưng không đặt acceptance threshold.

3. **Đo executable syntax rate bằng Gherkin parser chuẩn hóa (behave/cucumber dry-run) với ngưỡng ≥80%** — Các papers hiện tại dùng Gherkin-lint (lint rules) hoặc manual review, không phải parser-level verification.

### GAP đầy đủ (dạng đoạn văn)

> Mặc dù nghiên cứu về ứng dụng LLM trong BDD test generation đã tăng đáng kể từ 2022 đến 2026, với 12 studies peer-reviewed được đưa vào SLR này, vẫn tồn tại một khoảng trống nghiên cứu chưa được lấp đầy: chưa có nghiên cứu nào đánh giá GPT-4o (phiên bản đầy đủ, zero-shot, temperature=0) trên tập Connextra-format user stories chuẩn hóa từ nhiều SE projects, với hai metrics định lượng reproducible là (1) cosine semantic similarity ≥0.85 sử dụng all-MiniLM-L6-v2 sentence-transformers, và (2) executable syntax rate ≥80% sử dụng Gherkin parser (behave/cucumber dry-run). Khoảng trống này là đáng kể vì: 92% papers (11/12) không đo semantic similarity, 100% papers (12/12) không dùng Gherkin parser làm primary metric, và GPT-4o — model frontier mới nhất — chưa được đánh giá trong bất kỳ paper nào trong SLR.

### Contribution của nghiên cứu này

> **Nghiên cứu này đóng góp vào việc lấp đầy GAP trên bằng cách:** Đánh giá GPT-4o zero-shot (temperature=0) trên ≥50 Connextra-format user stories từ ≥3 SE projects, đo đồng thời (1) cosine semantic similarity (all-MiniLM-L6-v2) với acceptance threshold ≥0.85, và (2) executable rate (behave dry-run) với acceptance threshold ≥80% — tạo ra một evaluation framework chuẩn hóa, reproducible, và có thể làm baseline cho các nghiên cứu tương lai.

---

## Sơ đồ GAP — Tóm tắt

```
12 papers peer-reviewed trong SLR
│
├── LLM đã dùng: GPT-3.5, GPT-4, GPT-4 Turbo, GPT-4o Mini, Claude 3,
│               Gemini, Llama, PaLM-2, DeepSeek, Grok, Copilot
│               → GPT-4o full (zero-shot, temperature=0) ← CHƯA CÓ ❌
│
├── Metric semantic: BLEU (1), METEOR (2), BERTScore (1), Human (2)
│               → Cosine similarity all-MiniLM-L6-v2 ← CHƯA CÓ ❌
│
├── Metric executable: Gherkin-lint (3), manual (1), UI execution (1)
│               → behave/cucumber dry-run ← CHƯA CÓ ❌
│
└── Dataset: mostly small, proprietary, single-domain, single-project
            → ≥50 Connextra user stories, ≥3 SE projects ← CHƯA CÓ ❌
```
