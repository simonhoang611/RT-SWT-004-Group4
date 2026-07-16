# Bước 1.8 — Viết Giả thuyết H0 / H1

Dựa trên Research Question (RQ) chính thức đã tinh chỉnh, chúng ta chia bài toán thành 2 sub-RQs tương ứng với 2 mục tiêu đo lường: Semantic Similarity và Executable Syntax Rate.

---

## RQ1 — Semantic Similarity
*Mức độ tương đồng ngữ nghĩa trung bình (Cosine Similarity) giữa Gherkin do GPT-4o sinh ra và chuyên gia (expert) viết có vượt qua ngưỡng 0.85 không?*

*   **$H0_1$ (Null Hypothesis - Phủ định):** $\mu\_similarity \le 0.85$ 
    *(GPT-4o sinh ra các scenarios có độ tương đồng ngữ nghĩa trung bình CHƯA ĐẠT ngưỡng 0.85 so với chuyên gia).*
*   **$H1_1$ (Alternative Hypothesis - Kỳ vọng):** $\mu\_similarity > 0.85$ 
    *(GPT-4o sinh ra các scenarios có độ tương đồng ngữ nghĩa trung bình ĐẠT ngưỡng > 0.85 so với chuyên gia).*

**Phương pháp Kiểm định (Statistical Test):**
*   **Tên kiểm định:** One-sample Wilcoxon signed-rank test (Sử dụng biến thể one-sample vì ta so sánh điểm similarity của LLM với một ngưỡng cố định μ₀ = 0.85, không phải so sánh hai nhóm với nhau; kiểm định phi tham số phù hợp vì dữ liệu điểm similarity thường không tuân theo phân phối chuẩn hoàn hảo).
*   **Mức ý nghĩa ($\alpha$):** 0.05

---

## RQ2 — Executable Syntax
*Tỷ lệ các kịch bản Gherkin do GPT-4o sinh ra có thể chạy được (không dính lỗi cú pháp) có vượt qua ngưỡng 80% không?*

*   **$H0_2$ (Null Hypothesis - Phủ định):** $executable\_rate \le 0.80$ 
    *(Tỷ lệ Gherkin scenarios chạy được không lỗi cú pháp của GPT-4o sinh ra là $\le 80\%$).*
*   **$H1_2$ (Alternative Hypothesis - Kỳ vọng):** $executable\_rate > 0.80$ 
    *(Tỷ lệ Gherkin scenarios chạy được không lỗi cú pháp của GPT-4o sinh ra là $> 80\%$).*

**Phương pháp Kiểm định (Statistical Test):**
*   **Tên kiểm định:** Binomial test (one-tailed, với $p_0 = 0.80$) (Sử dụng Binomial vì kết quả Executable là nhị phân: Pass hoặc Fail lỗi cú pháp).
*   **Mức ý nghĩa ($\alpha$):** 0.05

---

## Trả lời Checkpoint 1.8: Phân tích P-value
**Câu hỏi:** *"Nếu chạy thực nghiệm xong, tool thống kê trả về p = 0.03 thì kết luận gì?"*

**Cách giải thích chuẩn học thuật:**
*   Trong thực nghiệm này, mức ý nghĩa (mức sai lầm cho phép) được đặt ở ngưỡng $\alpha = 0.05$.
*   Kết quả $p = 0.03$ tức là **$p < \alpha$ (0.03 < 0.05)**.
*   **Kết luận:** Ta có đủ bằng chứng toán học để **Bác bỏ giả thuyết Null ($H0$)** và **Chấp nhận giả thuyết Alternative ($H1$)**.
*   **Ý nghĩa thực tế:** Kết quả đạt **ý nghĩa thống kê (statistically significant)**. Điều này chứng minh rằng việc GPT-4o sinh ra kịch bản vượt ngưỡng yêu cầu (Similarity > 0.85 hoặc Executable > 80%) là khả năng thực sự của mô hình, chứ không phải do ăn may ngẫu nhiên (chỉ có 3% xác suất kết quả này xảy ra do ngẫu nhiên). Do đó, thí nghiệm thành công.
