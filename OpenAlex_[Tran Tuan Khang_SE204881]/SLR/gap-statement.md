# Bước 1.6 — Xác nhận GAP từ Evidence Table

## 1. Trả lời 4 câu hỏi từ Evidence Table

**1. LLM nào chưa được đánh giá?**
*   **Liệt kê cột Tool/LLM:** Các nghiên cứu trước đây đã dùng GPT-3.5, GPT-4, Gemini, LLaMA 3, Claude 3.7, Phi-3, v.v. 
*   **Chưa được đánh giá:** `GPT-4o` (phiên bản frontier model mới nhất và mạnh nhất hiện nay chưa được đánh giá kỹ trong tác vụ này).
*   **Ghi nhận:** Chọn `GPT-4o` cho yếu tố (I) trong PICO.

**2. "Semantic similarity" đã dùng chưa?**
*   **Đếm papers:** Có **1** paper (Paper 1) dùng *Cosine Similarity* và **1** paper (Paper 5) dùng *METEOR*. 
*   Tuy nhiên, **0** paper nào sử dụng Strict Semantic Similarity dựa trên Embedding với ngưỡng cụ thể để làm thước đo chất lượng sinh Gherkin.
*   **Ghi nhận:** GAP về metric ✓

**3. Executable syntax đã đo chưa?**
*   **Đếm papers:** Có **1** paper (Paper 7) đo lỗi cú pháp (Syntax Errors bằng Gherkin-lint). 
*   Tuy nhiên, **0** paper nào kết hợp đo kiểm tra song song cả hai yếu tố (Semantic Similarity + Executable syntax) cùng lúc.
*   **Ghi nhận:** GAP về metric ✓

**4. Hạn chế nào lặp $\ge$ 2 lần?**
*   **Quét cột Hạn chế:** 
    *   *Quy mô dữ liệu nhỏ / Giới hạn ở 1 case study duy nhất* lặp lại **5 lần** (Papers 1, 4, 5, 7, 8).
    *   *Đánh giá mang tính chủ quan bởi con người (Subjective bias)* lặp lại **3 lần** (Papers 3, 6, 8).
*   **Ghi nhận:** Đây là GAP được cộng đồng thừa nhận (cần một nghiên cứu đánh giá khách quan bằng tool tự động trên tập dữ liệu đủ lớn).

---

## 2. Nguồn gốc ngưỡng 0.85 (Semantic Similarity $\ge$ 0.85)
*   Mặc dù Paper 1 có đo Similarity, họ không thiết lập một ngưỡng (threshold) cụ thể.
*   Do không tìm thấy ngưỡng tương tự trong các paper đã review: **"Threshold set by course instructor"**.

---

## 3. GAP Statement

Tất cả **8** papers reviewed đều tập trung nghiên cứu khả năng sinh acceptance tests (Gherkin/BDD) tự động của các LLM phổ biến (như GPT-3.5/4, Gemini, Llama), với metric đánh giá chủ yếu dựa vào con người (human evaluation), độ bao phủ (coverage), hoặc các lỗi cú pháp cơ bản.

Tuy nhiên, KHÔNG paper nào:
(1) Đánh giá mô hình frontier mạnh nhất hiện nay là **GPT-4o** trên tác vụ sinh Gherkin scenarios từ chuẩn user stories format Connextra.
(2) Đo lường chất lượng kịch bản sinh ra bằng metric **Semantic similarity** (so sánh ngữ nghĩa với expected behavior).
(3) Kết hợp đồng thời cả hai điều kiện: độ chính xác ngữ nghĩa và khả năng **Executable syntax** (chạy được không lỗi cú pháp) bằng công cụ tự động.

**→ GAP:** Chưa có đánh giá toàn diện và khách quan (không dùng con người) đối với GPT-4o trong việc sinh Gherkin scenarios, sử dụng đồng thời hai tiêu chí tự động khắt khe: Semantic similarity và Executable syntax.

**→ Contribution:** Nghiên cứu này đánh giá hiệu năng của GPT-4o trong việc sinh Gherkin scenarios và step definitions từ Connextra user stories, sử dụng hệ thống đo lường tự động để kiểm tra xem kết quả sinh ra có đạt semantic similarity $\ge 0.85$ và executable syntax hay không.
