# Experiment Design Rationale — LLM for Acceptance Test Automation (BDD/Gherkin)
Ngày: 2026-06-14 | GAP source: SLR/gap-analysis.md

## Bảng Quyết Định

| Quyết định | Giá trị | Nguồn gốc |
|------------|---------|-----------|
| LLM/Tool | GPT-4o (official full version) | GAP-T: cột Tool/LLM (Chưa có nghiên cứu evaluate GPT-4o full version zero-shot) |
| Dataset | Mendeley BDD dataset + 2 public GitHub projects | GAP-D / benchmark (Cần Connextra format chuẩn từ ≥3 projects) |
| Metric chính | Cosine semantic similarity (all-MiniLM-L6-v2) | GAP-M: cột Metric (Chưa ai dùng cosine model này với ngưỡng cố định cho Gherkin) |
| Metric phụ | Executable syntax rate (`behave --dry-run`) | GAP-M: cột Metric (Thiếu đánh giá executable rate bằng Gherkin parser chuẩn) |
| Baseline type | Absolute threshold | Claim type RQ |
| Threshold RQ1 | 0.85 | Case 2: floor value từ Fernandes et al. 2025 |
| Threshold RQ2 | 80% | Case 2: floor value từ Kavuri 2022 |
| Pipeline base | Rathnayake et al. 2026 | Zero-shot prompting, temperature = 0 được chứng minh là config cho chất lượng tốt nhất |

## Lý giải threshold (ghi 1 đoạn cho mỗi threshold)

**Threshold 0.85 — Case 2 — floor = 0.84 từ Fernandes et al. 2025. Lý luận:**
Dựa trên báo cáo của Fernandes et al. 2025, model tốt nhất trong thực nghiệm zero-shot là Gemini đạt mức điểm ngữ nghĩa (METEOR) cao nhất là 0.84. Do chưa có công trình nào trước đó đặt mức ngưỡng cho cosine similarity trên tập dữ liệu Gherkin (Connextra format) để so sánh với expert-written baseline, ta chọn mức 0.84 làm floor value calibration point và làm tròn thành 0.85 để làm mức ngưỡng (threshold) đòi hỏi khắt khe nhưng khả thi cho bài toán sử dụng GPT-4o full version.

**Threshold 80% — Case 2 — floor = 79% từ Kavuri 2022. Lý luận:**
Kavuri 2022 báo cáo tỉ lệ execution success cho các mô hình ngôn ngữ lớn khác nhau, trong đó mô hình chạy zero-shot/few-shot như Code Llama-13B đạt mức 79%. Thay vì kiểm tra bằng Selenium hay PyTest, chúng ta sử dụng công cụ parser chuẩn mực (`behave --dry-run`) đòi hỏi độ chính xác cao về cú pháp Gherkin. Do vậy, mức 79% của mô hình Code Llama được chọn làm floor value và làm tròn thành 80% để tạo ra một conservative threshold hợp lý cho RQ2 khi đánh giá zero-shot prompting của GPT-4o.
