# IE Criteria — LLM for Acceptance Test Automation (BDD/Gherkin)

**Thành viên:** Nguyễn Hiếu An (SE205060)  
**RQ:** "GPT-4o zero-shot (temperature=0) có sinh được Gherkin acceptance test từ user story Connextra đạt cosine semantic similarity ≥ 0.85 (vs expert) và executable syntax rate ≥ 80% không?"  
**PICO:** P = user stories Connextra | I = GPT-4o zero-shot | C = expert-written Gherkin (ground truth) | O = cosine similarity ≥ 0.85 + executable rate ≥ 80%

---

## Inclusion Criteria (IC) — paper PHẢI có đủ tất cả

| Mã | Tiêu chí |
|---|---|
| **IC-L** | Viết bằng tiếng Anh |
| **IC-Y** | Xuất bản từ 2018 đến nay — Lý do: bao gồm cả baseline NLP/template trước kỷ nguyên LLM (để so sánh) và các LLM thế hệ GPT-2/3+ (xuất hiện 2018–2020) |
| **IC-T** | Đăng trên conference hoặc journal có phản biện — không phải blog, thesis, hay báo cáo kỹ thuật |
| **IC-P** | Về task: sinh test case tự động (acceptance test / Gherkin / BDD scenario / step definition) từ requirement / user story |
| **IC-I** | Dùng kỹ thuật: LLM, NLP, hoặc AI-based (GPT, BERT, T5, LLaMA và tương đương); hoặc template/rule-based làm baseline so sánh |
| **IC-E** | Có ít nhất 1 con số kết quả trong Table hoặc Figure của paper gốc |

## Exclusion Criteria (EC) — loại nếu BẤT KỲ điều kiện nào đúng

| Mã | Tiêu chí |
|---|---|
| **EC-D** | Trùng lặp với paper đã có trong danh sách |
| **EC-A** | Không truy cập được full-text |
| **EC-S** | Dưới 4 trang (extended abstract, poster, short paper) |
| **EC-N** | Không có thực nghiệm (position paper, vision paper, tutorial, SLR/survey) |
| **EC-O** | Không về topic. Các task hay bị nhầm với IC-P: (1) test execution / debugging / maintenance; (2) test case prioritization / selection / redundancy reduction; (3) "BDD" = Binary Decision Diagram (mạch điện/quantum); (4) code generation / model validation không liên quan đến test từ requirement |

---

## Checklist tự kiểm (theo rubric cô)

- [x] Đủ 6 IC (IC-L, IC-Y, IC-T, IC-P, IC-I, IC-E) và 5 EC (EC-D, EC-A, EC-S, EC-N, EC-O)
- [x] IC-P là tên task cụ thể (không ghi "AI trong SE")
- [x] IC-I là loại kỹ thuật cụ thể (không ghi "công nghệ mới")
- [x] EC-O liệt kê ≥ 2 task hay bị nhầm (có 4 task)
- [x] IC-Y có lý do chọn năm (1 câu)
