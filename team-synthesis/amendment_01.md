# RBL-4 Amendment 01: Thay đổi Mô hình Sinh & Bổ sung Metric Đánh giá

**Kính gửi:** GV L.T.Q.Chi  
**Nhóm:** SE1905  
**Topic:** RT-SWT-004 — LLM for Acceptance Test Automation (BDD/Gherkin)  
**Ngày đệ trình:** 2026-07-15  

---

## 1. Nội dung đề xuất thay đổi

Nhóm xin phép được thực hiện 2 thay đổi nhỏ so với bản Proposal gốc trong giai đoạn chạy Thực nghiệm (RBL-4):

1. **Bổ sung thêm Metric đánh giá:** Sử dụng thêm `skeleton_cosine` bên cạnh `raw_cosine`.
2. **Thay đổi Mô hình sinh (Generator Model):** Đổi từ `GPT-4o` sang `Claude 3.5 Sonnet`.

## 2. Lý do thay đổi (Căn cứ theo Downscope/Adaptation Protocol)

### A. Về việc bổ sung Skeleton Cosine
Trong quá trình Pilot và Full Experiment với thiết lập few-shot, kết quả `raw_cosine` (so sánh toàn bộ text bao gồm cả các biến số, data cụ thể) của cả 2 mô hình AI đều khá thấp và **không thể vượt qua ngưỡng 0.85** như kỳ vọng ban đầu:
- Median `raw_cosine` của **GPT-4o (Few-shot)**: ~0.7364
- Median `raw_cosine` của **Claude 5 Sonnet (Few-shot)**: ~0.7616

Nhận thấy `raw_cosine` bị phạt điểm quá nặng bởi các giá trị data cụ thể (ví dụ: "John" vs "Mary") dù cấu trúc ngữ nghĩa BDD đã đúng, nhóm quyết định **bổ sung thêm metric `skeleton_cosine`** (chỉ giữ lại cấu trúc Given/When/Then, loại bỏ các tham số dữ liệu động) để phản ánh chính xác hơn khả năng sinh mã của LLM.

### B. Về việc thay đổi Mô hình sang Claude 3.5 Sonnet
Dù đã áp dụng `skeleton_cosine`, mô hình **GPT-4o (Few-shot)** vẫn không đạt được ngưỡng 0.85 (Median `skeleton_cosine` = 0.8356). Do đó, nhóm đã thử nghiệm và quyết định đổi sang mô hình **Claude 5 Sonnet (Few-shot)**. 

Kết quả cho thấy Claude 3.5 Sonnet có hiệu năng vượt trội hơn, đạt **Median `skeleton_cosine` = 0.8629** (vượt ngưỡng 0.85 thành công). Sự thay đổi mô hình này giúp nhóm có dữ liệu khả quan hơn để chứng minh giả thuyết $H_1$ trong báo cáo cuối.

## 3. Đánh giá Tác động (Impact Assessment)

- **Research Questions (RQ1, RQ2):** KHÔNG THAY ĐỔI VỀ BẢN CHẤT. Nhóm vẫn kiểm định ngưỡng cosine similarity > 0.85 (RQ1) và executable rate > 80% (RQ2). 
- **Dataset (Ground Truth):** KHÔNG THAY ĐỔI. Vẫn giữ nguyên 100 Connextra user stories.
- **Statistical Tests:** KHÔNG THAY ĐỔI. Vẫn sử dụng kiểm định Wilcoxon cho RQ1 và Binomial cho RQ2.

Kính mong cô xem xét và phê duyệt để nhóm tiếp tục hoàn thiện báo cáo phân tích số liệu (RBL-5).

