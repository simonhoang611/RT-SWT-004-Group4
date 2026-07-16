# Search Log — LLM for Acceptance Test Automation (BDD/Gherkin)

**Thành viên:** Nguyễn Hiếu An (SE205060)  
**Nhóm/Lớp:** SE1905  
**Database được giao:** IEEE Xplore  
**Ngày thực hiện:** 2026-06-__

---

## Chuỗi tìm kiếm (Query Strings)

### String S1 — Sinh Gherkin/BDD từ user story / requirements

**Query nguyên văn:**
```
("Gherkin" OR "BDD" OR "behavior-driven development") AND ("generation" OR "automated" OR "synthesis") AND ("user story" OR "requirements")
```
**Database:** IEEE Xplore
**Trường tìm:** All Metadata
**Bộ lọc:** Year 2018–2026, English only, Conferences + Journals
**Ngày search:** 2026-06-__
**Số kết quả:** 39 papers

---

### String S2 — LLM sinh acceptance test / BDD

**Query nguyên văn:**
```
("large language model" OR "LLM" OR "GPT" OR "ChatGPT") AND ("acceptance test" OR "Gherkin" OR "BDD")
```
**Database:** IEEE Xplore
**Trường tìm:** All Metadata
**Bộ lọc:** Year 2018–2026, English only, Conferences + Journals
**Ngày search:** 2026-06-__
**Số kết quả:** 17 papers

---

### String S3 — Đánh giá chất lượng test (semantic similarity / executable)

**Query nguyên văn:**
```
("Gherkin" OR "BDD" OR "acceptance test") AND ("semantic similarity" OR "evaluation" OR "executable")
```
**Database:** IEEE Xplore
**Trường tìm:** All Metadata
**Bộ lọc:** Year 2018–2026, English only, Conferences + Journals
**Ngày search:** 2026-06-__
**Số kết quả:** 155 papers

---

## Tổng hợp trước dedup

| Database | String | Kết quả |
|---|---|---|
| IEEE Xplore | S1 | 39 |
| IEEE Xplore | S2 | 17 |
| IEEE Xplore | S3 | 155 |
| **Tổng trước dedup** | | **211** |
| **Sau dedup** | | **182** |
| Số bị loại (trùng lặp) | | 29 |

---

## Ghi chú

- **Phương pháp dedup:** dùng Python (pandas) — normalize title (lowercase + strip whitespace) rồi `groupby` để gộp các bản trùng. Các search string của paper trùng được gộp lại (vd `S1+S3` = paper xuất hiện ở cả S1 và S3).
- **Paper trùng nhau nhiều nhất:** các paper bắt được bởi cả S1+S3 (10 paper) và S2+S3 (7 paper) — do từ khóa "BDD"/"acceptance test" xuất hiện ở nhiều string. 6 paper xuất hiện ở cả 3 string (S1+S2+S3) — đây là các paper "vàng" liên quan trực tiếp nhất.
- **Điểm bất thường:** String S3 trả về 155 paper (nhiều nhất) nhưng chứa nhiều noise — từ "BDD" bị nhầm sang "Binary Decision Diagram" (mạch điện/quantum), và từ "evaluation"/"executable" bắt nhiều paper off-topic. Đa số sẽ bị loại ở screening Vòng 1 (xem 02_after_screening_v1.csv).
- **File export gốc:** S1.csv (39), S2.csv (17), S3.csv (155) — export trực tiếp từ IEEE Xplore với option "Citation and Abstract".

---

## Phần S — Cross-reference Search (Snowballing)

> Snowballing không có query string — không điền vào mục này như String S1/S2/S3.

**Phương pháp:** Backward snowballing — đọc reference list của các paper đã pass Vòng 2.
**Thực hiện:** Sau khi có `03_final_included.csv`, đọc reference list của 14 paper final → kiểm tra paper mới qua Semantic Scholar/CrossRef.
**Công cụ:** CrossRef (crossref.org) để lookup metadata từ DOI.
**Ngày thực hiện:** ____ _(cần điền)_
**Paper included đã scan:** ___ / 14 paper _(cần điền)_
**Paper mới phát hiện:** ___ paper pass IC _(ghi rõ từ paper nào → tìm được paper nào; nếu không có ghi: "Đã scan 14 paper, không có paper mới pass IC")_

> **Lưu ý:** Đây là mục BẮT BUỘC theo rubric — dù không tìm được paper mới vẫn phải ghi "Đã scan [N] paper, không có paper mới pass IC". Hiện mục này đang chờ bạn thực hiện snowballing thật và điền số.
