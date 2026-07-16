# Experiment Design Rationale — LLM for Acceptance Test Automation (BDD/Gherkin)

**Thành viên:** Nguyễn Hiếu An (SE205060)  
**Ngày:** 2026-06-__ · **GAP source:** SLR/gap-analysis.md

> Quy tắc: mỗi quyết định thiết kế phải trỏ về 1 ô cụ thể trong evidence table. Không có nguồn → không hợp lệ.

---

## Bảng Quyết Định

| Quyết định | Giá trị | Nguồn gốc |
|---|---|---|
| **LLM/Tool** | GPT-4o (zero-shot); downscope: GPT-4o mini nếu chi phí cao | GAP-T — cột Tool/LLM (0 paper dùng GPT-4o) |
| **Prompt strategy** | Zero-shot | Ferreira 2025, Varpe 2025 dùng zero-shot; đơn giản, reproducible |
| **Temperature** | 0 | Reproducibility (output ổn định mỗi lần chạy) |
| **Dataset** | 30–50 user story Connextra (từ GitHub `.feature` reverse hoặc tự viết best-practice) | GAP-D — cột Dataset (0 paper dùng Connextra) |
| **Metric chính** | Cosine semantic similarity — `sentence-transformers` (all-MiniLM-L6-v2) | GAP-M — cột Metric |
| **Metric phụ** | Executable syntax rate — Gherkin parser (`behave` / `gherkin-official`) | Kế thừa từ Fonseca 2025 (đo syntactic correctness) |
| **Baseline type** | Absolute threshold (cosine ≥ ngưỡng) + Human-level (so với expert-written Gherkin) | Claim type RQ (3A) — absolute + human |
| **Threshold RQ1** | cosine ≥ 0.85 (cần mini-pilot xác nhận) | **Case 3** — xem lý giải dưới |
| **Threshold RQ2** | executable rate ≥ 80% | **Case 2** — floor từ Storer 2019 |
| **Pipeline base** | Varpe 2025 (User Acceptance Test Gen Using LLMs) | Evaluation paradigm gần nhất (LLM sinh test + đo semantic similarity) |

---

## Lý giải threshold (1 đoạn cho mỗi threshold)

### Threshold RQ1 — Cosine semantic similarity ≥ 0.85 → **Case 3**

Không paper nào trong evidence table dùng **cosine similarity (sentence-transformer)** với một ngưỡng cố định. Paper gần nhất là Varpe 2025 dùng **BERTScore** (metric semantic khác) và đạt F1 = 80.58% (≈ 0.81) — đây là *kết quả*, không phải *ngưỡng được đề xuất*, và lại là metric khác (BERTScore ≠ cosine all-MiniLM). Vì không có con số trực tiếp so sánh được → áp dụng **Case 3**: ghi rõ lý do + chạy **mini-pilot PRE-PROPOSAL (5–10 sample thủ công)** để xác nhận ngưỡng trước khi chốt. Ngưỡng khởi đầu 0.85 được tham chiếu từ Varpe (0.81) cho thấy 0.85 nằm trong khoảng hợp lý (cao hơn một chút, đặt mục tiêu thách thức). **Sau mini-pilot, nếu phân phối thực tế lệch nhiều, sẽ điều chỉnh ngưỡng và ghi amendment.**

> ⚠️ **Lưu ý cho bạn:** Lần trước ghi "0.85 set by course instructor" — RBL-2 KHÔNG chấp nhận cách này. Phải dùng Case 3 (mini-pilot) như trên. Nếu cô muốn giữ đúng 0.85 mà không pilot, hỏi cô xem có paper nào cô muốn dùng làm nguồn (Case 1) không.

### Threshold RQ2 — Executable syntax rate ≥ 80% → **Case 2**

Có kết quả số nhưng không paper nào đề xuất ngưỡng → dùng **floor value** (kết quả thấp nhất hợp lý trong bảng). Storer 2019 đạt **80%** generation success (white box); Fonseca 2025 đạt **93.3%** syntactic correctness. Lấy floor = **80% từ Storer 2019** → threshold = **80%**. Ghi rõ: *"floor = 80% từ Storer 2019 (white box success rate), threshold = 80%"*. Đây là ngưỡng bảo thủ (thấp hơn Fonseca 93.3%) nên khả thi đạt được.

---

## Pipeline chi tiết (mỗi thành phần có nguồn)

| Thành phần | Ghi rõ | Nguồn |
|---|---|---|
| LLM/Tool | GPT-4o, version `gpt-4o` (hoặc `gpt-4o-mini`) | GAP-T — cột Tool/LLM |
| Prompt strategy | Zero-shot | Ferreira 2025, Varpe 2025 |
| Temperature | 0 | Reproducibility |
| Metric tool 1 | `sentence-transformers` v2.x, model all-MiniLM-L6-v2 | GAP-M — cột Metric |
| Metric tool 2 | `behave` / `gherkin-official` (Gherkin parser) | Fonseca 2025 |
| Baseline type | Absolute threshold + human (expert-written Gherkin) | Claim type RQ (3A) |

---

## Checklist (rubric RBL-2)

- [x] Mỗi dòng trong bảng quyết định có nguồn từ evidence table
- [x] Threshold ghi Case (1/2/3) + lý luận văn xuôi
- [x] Pipeline ghi base paper (Varpe 2025) + liệt kê thay đổi (đổi BERTScore→cosine, đổi SRS→Connextra, đổi 5 LLM→GPT-4o)
