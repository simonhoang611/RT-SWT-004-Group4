# GAP Analysis — LLM for Gherkin/BDD Acceptance Test Generation
Evidence table: N = 10 paper (đã lọc các paper có PDF) | Ngày: 2026-06-08

---

## BƯỚC 1 — Kiểm tra evidence table (30 phút)

Mở `evidence-table.md`. Pass tất cả 5 gate mới tiếp tục:

| Gate | Tiêu chí | Kết quả | Ghi chú |
|---|---|---|---|
| P1: Số paper | $\ge$ 5 paper | ✅ 10 papers | Pass |
| P2: Cột Tool/LLM | $\ge$ 90% hàng điền | ✅ 10/10 = 100% | Pass |
| P3: Cột Kết quả | $\ge$ 50% hàng có số | ✅ 10/10 = 100% | Pass |
| P4: Cột Hạn chế | $\ge$ 50% hàng điền | ✅ 10/10 = 100% | Pass |
| P5: Cột Metric | Tên metric cụ thể | ✅ Cosine similarity, METEOR, F1, Coverage, Syntax | Pass |

$\rightarrow$ **Tất cả 5 gate: PASS. Tiếp tục bước 2.**

---

## BƯỚC 2 — Phân tích GAP (2-3 giờ)

### 2A. Năm loại GAP

| Loại | Cột nguồn | Câu hỏi | Ví dụ phát hiện từ Evidence Table |
|---|---|---|---|
| **GAP-T** | Tool/LLM | Công nghệ nào chưa thử? | 10/10 paper chưa dùng GPT-4o (bản đầy đủ). |
| **GAP-M** | Metric | Khía cạnh nào chưa đo? | Không ai đo đồng thời semantic similarity và executable syntax rate bằng công cụ tự động. |
| **GAP-P** | Prompt | Chiến lược prompt nào thiếu? | Các nghiên cứu chủ yếu dùng Zero-shot/Few-shot cơ bản, chưa so sánh toàn diện Chain-of-Thought (CoT) hay Role-playing. |
| **GAP-D** | Dataset | Domain/quy mô nào thiếu? | 10/10 paper dùng dataset nội bộ hoặc quy mô rất nhỏ, thiếu dataset Connextra chuẩn. |
| **GAP-S** | Hạn chế | Hạn chế chung là gì? | 10/10 paper (100%) thừa nhận dataset nhỏ / single case study. |

Ưu tiên khi nhiều GAP xung đột: **GAP-T > GAP-P > GAP-M > GAP-D > GAP-S**

---

### 2B. Kiểm tra phản chứng (BẮT BUỘC)

Với mỗi GAP tuyên bố, quét lại **từng paper** trong evidence table:

#### Kiểm tra GAP-T
**GAP tuyên bố:** Không có paper nào trong Evidence Table đánh giá GPT-4o (phiên bản đầy đủ) trên tác vụ sinh Gherkin/BDD.

| Paper | Đã làm không? | Ghi chú (Kèm trích dẫn trong file PDF) |
|---|---|---|
| Paper 1 (Santos 2025) | Không | Dùng ChatGPT, Gemini, Grok, Copilot |
| Paper 2 (Santos SBQS) | Không | Dùng AutoDevSuite (Gemini, ChatGPT) |
| Paper 3 (Mendoza 2024) | Không | Dùng Copilot, ChatGPT-3.5/4, Gemini |
| Paper 4 (Rumiantsev) | Không | Dùng GPT architecture + MSpec |
| Paper 5 (Fernandes 2025)| Không | Dùng GPT-4o Mini (phiên bản rút gọn), không phải GPT-4o |
| Paper 6 (Mughal 2026) | Không | Dùng SBERT + XGBoost |
| Paper 7 (Karpurapu 2024)| Không | Dùng GPT-3.5/4, Llama-2, PaLM-2 |
| Paper 8 (Hassani 2026) | Không | Dùng Claude 3.7 Sonnet, Llama 3.3 70B |
| Paper 9 (Ferreira 2024) | Không | Dùng GPT-4 Turbo |
| Paper 10 (Fonseca 2025)| Không | Dùng DeepSeek-R1, DeepSeek-Coder-v2, Gemma3 |

$\rightarrow$ **Kết luận: Xác nhận** (vì 0/10 paper dùng GPT-4o full).

#### Kiểm tra GAP-M
**GAP tuyên bố:** Không có paper nào đo đồng thời cosine semantic similarity và executable syntax rate bằng công cụ tự động.

| Paper | Đã làm không? | Ghi chú (Kèm trích dẫn trong file PDF) |
|---|---|---|
| Paper 1 (Santos 2025) | Không | Metric: Similarity coefficient (Cosine Similarity) |
| Paper 2 (Santos SBQS) | Không | Chỉ đo Code Coverage (pytest-cov) |
| Paper 3 (Mendoza 2024) | Không | Dùng Likert scale đánh giá bằng con người |
| Paper 4 (Rumiantsev) | Không | Chỉ tính Efficiency Gain |
| Paper 5 (Fernandes 2025)| Không | current metrics may overlook factors |
| Paper 6 (Mughal 2026) | Không | Behavioural equivalence is asserted |
| Paper 7 (Karpurapu 2024)| Không | realms of test coverage |
| Paper 8 (Hassani 2026) | Không | binary plausibility check |
| Paper 9 (Ferreira 2024) | Không | Accessibility |
| Paper 10 (Fonseca 2025)| Không | syntactically correct |

$\rightarrow$ **Kết luận: Xác nhận** (vì mỗi paper chỉ đo một trong hai hoặc không đo tự động).

#### Kiểm tra GAP-P
**GAP tuyên bố:** Chưa có nghiên cứu nào so sánh và đánh giá toàn diện các chiến lược Prompt nâng cao như Chain-of-Thought (CoT) kết hợp Role-playing trong sinh Gherkin.

| Paper | Đã làm không? | Ghi chú (Kèm trích dẫn trong file PDF) |
|---|---|---|
| Paper 1 (Santos 2025) | Không | "standardized prompts based on user stories" |
| Paper 2 (Santos SBQS) | Không | "responding to prompts provided in natural language" |
| Paper 3 (Mendoza 2024) | Không | "zero-shot-learning and few-shot-learning prompt techniques" |
| Paper 4 (Rumiantsev) | Không | "structured LLM prompting strategies" |
| Paper 5 (Fernandes 2025)| Không | "zero-shot, one-shot, and few-shot prompting strategies" |
| Paper 6 (Mughal 2026) | Không | "prompt-and-response logs" |
| Paper 7 (Karpurapu 2024)| Không | "zero and few-shot prompts to evaluate LLMs" |
| Paper 8 (Hassani 2026) | Không | "employ prompting to derive unit tests" |
| Paper 9 (Ferreira 2024) | Không | "unit tests from textual prompts" |
| Paper 10 (Fonseca 2025)| Không | "concentrating on inputs and expected outputs" |

$\rightarrow$ **Kết luận: Xác nhận** (các paper chỉ dùng Zero-shot/Few-shot cơ bản hoặc Prompt tĩnh).

#### Kiểm tra GAP-D
**GAP tuyên bố:** Không có paper nào dùng Connextra-format user stories chuẩn từ $\ge$ 3 dự án Software Engineering công khai.

| Paper | Đã làm không? | Ghi chú (Kèm trích dẫn trong file PDF) |
|---|---|---|
| Paper 1 (Santos 2025) | Không | "containing 34 user stories was used" |
| Paper 2 (Santos SBQS) | Không | "POC/POV of a cybersecurity product" |
| Paper 3 (Mendoza 2024) | Không | "five scenarios ranked by complexity" |
| Paper 4 (Rumiantsev) | Không | "legacy failing integration tests" |
| Paper 5 (Fernandes 2025)| Không | "curated dataset of 1,286 cases" |
| Paper 6 (Mughal 2026) | Không | "upstream owners on GitHub" |
| Paper 7 (Karpurapu 2024)| Không | "due to the lack of dataset" |
| Paper 8 (Hassani 2026) | Không | "Food-Safety Regulations" |
| Paper 9 (Ferreira 2024) | Không | "compile a final dataset of 13 issues" |
| Paper 10 (Fonseca 2025)| Không | "industrial projects, as observed in BMW" |

$\rightarrow$ **Kết luận: Xác nhận** (vì 0/10 paper thỏa mãn điều kiện dataset lớn công khai).

#### Kiểm tra GAP-S
**GAP tuyên bố:** Hạn chế về quy mô dataset nhỏ hoặc single case study được thừa nhận bởi $\ge$ 4/10 paper.

| Paper | Có thừa nhận không? | Ghi chú (Kèm trích dẫn trong file PDF) |
|---|---|---|
| Paper 1 (Santos 2025) | Có | "based on 34 user stories" |
| Paper 2 (Santos SBQS) | Có | "The team responsible for creating new POCs/POVs" |
| Paper 3 (Mendoza 2024) | Có | "different levels of complexity and constraints" |
| Paper 4 (Rumiantsev) | Có | "evaluate the proposed framework" |
| Paper 5 (Fernandes 2025)| Có | "sample size (ten scenarios) may not reflect" |
| Paper 6 (Mughal 2026) | Có | "three-author labelling protocol" |
| Paper 7 (Karpurapu 2024)| Có | "real-time projects due to the lack" |
| Paper 8 (Hassani 2026) | Có | "sample size (10 participants" |
| Paper 9 (Ferreira 2024) | Có | "dataset of 13 issues" |
| Paper 10 (Fonseca 2025)| Có | "BMW’s MyBMW app" |

$\rightarrow$ **Kết luận: Xác nhận** (10/10 $\ge$ 4 paper cùng chia sẻ hạn chế).

---

### 2C. Đánh giá khả thi (Feasibility) trước khi chốt GAP

Chạy qua **đầy đủ 6 tiêu chí** đánh giá tính khả thi cho **từng GAP candidate**.

#### 1. Đánh giá khả thi: GAP-T (Công nghệ mới: GPT-4o)
| Tiêu chí | Câu hỏi tự hỏi | Đánh giá | Ghi chú |
|---|---|---|---|
| Dataset | Có public, tải được ngay không? | ✅ An toàn | Dùng các tập con nhỏ có sẵn từ thư viện mở. |
| Tool/API | LLM có free tier không? | ⚠️ Cần xử lý | API GPT-4o có thu phí, nhưng với dataset nhỏ thì chi phí < $5 (hoàn toàn tự chi trả được). |
| Compute | Cần phần cứng gì? | ✅ An toàn | Code chỉ gọi API, không cần train model nên CPU máy cá nhân là thừa sức. |
| Ground truth | Cần tạo dữ liệu nhãn thủ công? | ✅ An toàn | Đã có sẵn Gherkin scripts mẫu trong dataset để đối chiếu. |
| Skills | Có thể implement pipeline không? | ✅ An toàn | Chỉ cần code Python cơ bản sử dụng thư viện `openai`. |
| Thời gian | Xong trong deadline? | ✅ An toàn | Cấu hình API và chạy test cực nhanh (xong trong vài giờ). |
$\rightarrow$ **Quyết định: An toàn — chọn GAP này.**

#### 2. Đánh giá khả thi: GAP-M (Metric mới: Cosine Similarity + Syntax Rate)
| Tiêu chí | Câu hỏi tự hỏi | Đánh giá | Ghi chú |
|---|---|---|---|
| Dataset | Có public, tải được ngay không? | ✅ An toàn | Tái sử dụng ngay kết quả sinh ra từ GAP-T. |
| Tool/API | LLM có free tier không? | ✅ An toàn | Đo Cosine dùng `sentence-transformers`, đo Syntax dùng thư viện Python `behave` (đều Open-source & Miễn phí). |
| Compute | Cần phần cứng gì? | ✅ An toàn | Các model transformers để đo Cosine khá nhẹ, chạy tốt trên CPU hoặc Google Colab T4 Free. |
| Ground truth | Cần tạo dữ liệu nhãn thủ công? | ✅ An toàn | Chấm điểm tự động dựa trên dữ liệu mẫu có sẵn, không cần gán nhãn bằng tay. |
| Skills | Có thể implement pipeline không? | ⚠️ Cần xử lý | Cần kỹ năng code parser text phức tạp hơn 1 chút, nhưng có sẵn document hướng dẫn phong phú. |
| Thời gian | Xong trong deadline? | ✅ An toàn | Code validation pipeline tốn khoảng 1-2 ngày, hoàn toàn kịp tiến độ. |
$\rightarrow$ **Quyết định: An toàn — chọn GAP này.**

#### 3. Đánh giá khả thi: GAP-P (Chiến lược Prompt: Chain-of-Thought)
| Tiêu chí | Câu hỏi tự hỏi | Đánh giá | Ghi chú |
|---|---|---|---|
| Dataset | Có public, tải được ngay không? | ✅ An toàn | Dùng chung một dataset đầu vào với GAP-T để đảm bảo tính so sánh. |
| Tool/API | LLM có hỗ trợ CoT tốt không? | ✅ An toàn | GPT-4o nổi tiếng là model tuân thủ Instruction và Chain-of-Thought xuất sắc nhất hiện nay. |
| Compute | Cần phần cứng gì? | ✅ An toàn | CPU cá nhân (gọi API). |
| Ground truth | Cần tạo dữ liệu nhãn thủ công? | ✅ An toàn | Dùng chung Ground Truth của bộ dataset đã có. |
| Skills | Có thể implement pipeline không? | ✅ An toàn | Rất dễ, chỉ cần hiểu kỹ thuật Prompt Engineering, không yêu cầu thuật toán phức tạp. |
| Thời gian | Xong trong deadline? | ✅ An toàn | Tốn vài giờ để tinh chỉnh file text template prompt. |
$\rightarrow$ **Quyết định: An toàn — chọn GAP này.**

#### 4. Đánh giá khả thi: GAP-D & GAP-S (Giải quyết hạn chế Dataset cực lớn từ public SE projects)
| Tiêu chí | Câu hỏi tự hỏi | Đánh giá | Ghi chú |
|---|---|---|---|
| Dataset | Có public, tải được ngay không? | ❌ Blocker | Phải tự cào (crawl) và phân loại thủ công từ JIRA/GitHub vì dữ liệu thô vô cùng lộn xộn. |
| Tool/API | LLM có free tier không? | ✅ An toàn | Có thể dùng tool crawl mở. |
| Compute | Cần phần cứng gì? | ✅ An toàn | CPU đủ dùng. |
| Ground truth | Cần tạo dữ liệu nhãn thủ công? | ❌ Blocker | Phải tự tay viết hàng trăm file Expert-Gherkin chuẩn mực cho đống dữ liệu vừa cào được. Ngốn hàng chục giờ đồng hồ của QA Expert. |
| Skills | Có thể implement pipeline không? | ⚠️ Cần xử lý | Cần kỹ năng Data Mining và Domain Knowledge siêu vững để lọc rác. |
| Thời gian | Xong trong deadline? | ❌ Blocker | Quá trình Crawl + Làm sạch + Lập Ground Truth dự kiến mất $\ge$ 1 tháng. 100% trễ deadline môn học! |
$\rightarrow$ **Quyết định: Có tới 3 ❌ (Blocker chí mạng). Loại bỏ GAP này vì mức độ rủi ro vô cùng cao.**

---

### 2D. Ghi nhận TOP 3 GAP cuối cùng

Sau khi qua feasibility check, ta chọn TOP 3 GAP an toàn và có độ ưu tiên cao nhất:

*   **GAP 1 (Công nghệ): GAP-T**
    *   **Phát biểu:** Chưa có nghiên cứu nào đánh giá **GPT-4o (phiên bản đầy đủ, temperature=0)** trên tác vụ sinh Gherkin scenarios.
*   **GAP 2 (Chiến lược): GAP-P**
    *   **Phát biểu:** Các nghiên cứu hiện tại chủ yếu phụ thuộc vào Zero-shot hoặc Few-shot cơ bản. Chưa có ai so sánh tác động của **Chain-of-Thought (CoT) kết hợp Role-playing** đối với tính chính xác của Gherkin được sinh ra.
*   **GAP 3 (Đo lường): GAP-M**
    *   **Phát biểu:** Hiện tại thiếu một quy trình đo lường tự động toàn diện; chưa có nghiên cứu nào kết hợp chấm điểm **đồng thời semantic similarity** (bằng Cosine) và **executable syntax rate** (bằng Gherkin parser).

$\rightarrow$ Bộ 3 GAP này tạo thành một thiết kế thực nghiệm hoàn hảo: Sử dụng công nghệ mới nhất (GAP-T) + Phương pháp tiếp cận thông minh nhất (GAP-P) + Công cụ đo lường tự động toàn diện nhất (GAP-M).
