# Gap Statement — LLM for Acceptance Test Automation (BDD/Gherkin)

**Thành viên:** Nguyễn Hiếu An (SE205060)  
**Nhóm:** SE1905  
**Evidence table:** N = 14 papers  
**Date:** 2026-06-__

---

## Các khoảng trống phát hiện

### GAP-T (Technology): Chưa ai đánh giá GPT-4o cho Gherkin generation

**Mô tả:** Các paper đã dùng nhiều LLM (GPT-3.5, GPT-4, GPT-4 Turbo, LLaMA/Llama-2-13B/LLaMA3, PaLM-2, Gemma, Mistral, Phi, Qwen) và BERT, nhưng **chưa paper nào dùng GPT-4o** (frontier model mới nhất của OpenAI, khác GPT-4 Turbo).

**Bằng chứng (cột Tool/LLM):**
- Paper gần nhất: Ferreira 2025 dùng **GPT-4 Turbo** (không phải GPT-4o), và metric chỉ là helpfulness rating chủ quan.
- Karpurapu 2024 dừng ở **GPT-4** (không có GPT-4o).
- Varpe 2025 chỉ dùng **5 LLM open-source** (Gemma/LLaMA3/Mistral/Phi/Qwen), không có model OpenAI mới nhất.

---

### GAP-M (Metric): Chưa ai kết hợp cosine semantic similarity (ngưỡng cố định) + executable rate

**Mô tả:** Chưa paper nào dùng ĐỒNG THỜI (1) cosine semantic similarity với ngưỡng cố định 0.85 so với expert-written Gherkin, VÀ (2) executable syntax rate, làm primary metrics.

**Bằng chứng (cột Metric):**
- **Chỉ 1/14 paper** (Varpe 2025) dùng embedding-based semantic similarity (BERTScore F1 = 80.58%) — nhưng trên SRS documents, không đặt ngưỡng cố định.
- **Chỉ 2/14 paper** (Fonseca 2025: 93.3% syntactic correct; Karpurapu 2024: error-free rate) đo executable/syntactic — nhưng không kết hợp với semantic similarity.
- **Không paper nào** ghép cả 2 metric trên cùng dataset Connextra + GPT-4o.

---

### GAP-D (Dataset): Chưa ai dùng user stories Connextra chuẩn

**Mô tả:** Đa số dùng JIRA tickets, SRS documents, use case specs — **không dùng format Connextra chuẩn** ("As a... I want... So that...").

**Bằng chứng (cột Dataset):**
- Fonseca 2025: input là **JIRA tickets** (BMW app).
- Varpe 2025: **PURE SRS documents**.
- Wang 2022: **use case specifications**.
- Không paper nào benchmark trên user stories Connextra từ ≥ 3 dự án SE.

---

## Phát biểu GAP tổng hợp

> Trong 14 papers reviewed, các yếu tố [GPT-4o], [cosine semantic similarity ngưỡng 0.85], [executable syntax rate], và [user stories Connextra] **đã được nghiên cứu RIÊNG LẺ**, nhưng **chưa paper nào kết hợp đủ cả 4 yếu tố** trong một nghiên cứu — tức là chưa ai đánh giá **GPT-4o zero-shot (temperature=0)** sinh Gherkin từ **user stories Connextra**, đo **cosine semantic similarity ≥ 0.85** (vs expert-written) ĐỒNG THỜI với **executable syntax rate ≥ 80%**.

**Paper gần nhất và vẫn còn thiếu gì:**
- Ferreira 2025 (gần nhất về I): dùng GPT-4 Turbo, nhưng **thiếu** GPT-4o + semantic similarity định lượng + Connextra.
- Varpe 2025 (gần nhất về metric O1): dùng BERTScore, nhưng **thiếu** GPT-4o + executable rate + Connextra.
- Fonseca 2025 (gần nhất về metric O2): đo executable rate, nhưng **thiếu** semantic similarity + Connextra + GPT-4o.

---

## Ngưỡng 0.85 — nguồn

Không paper nào trong evidence table đặt 0.85 làm ngưỡng cosine similarity cố định.
→ **Threshold set by course instructor.** Context: Varpe 2025 đạt BERTScore F1 ≈ 0.81; mốc 0.8–0.85 thường được coi là "high semantic similarity" trong literature embeddings → 0.85 là ngưỡng hợp lý, hơi thách thức.

---

## Checklist Checkpoint 1.6 (theo rubric cô)

- [x] Mỗi GAP trỏ về **cột cụ thể** trong evidence table (Tool/LLM, Metric, Dataset)
- [x] **Không có GAP mơ hồ** "nhiều nghiên cứu chưa làm" — đã ghi rõ paper nào gần nhất và còn thiếu gì
- [x] GAP statement cite ≥ 2 papers (cite Ferreira, Varpe, Fonseca, Karpurapu)
- [x] Ngưỡng 0.85 có nguồn
