# Search Log — SLR: LLM-Based Test Case Generation

**Thành viên:** Tống Vỹ Thuận
**Ngày thực hiện:** 2026-06-01 → 2026-06-03

---

## Chuỗi tìm kiếm (Query Strings)

### String A

**Query nguyên văn:**
`("large language model" OR ChatGPT OR GPT) AND ("software testing")`

**Database:** IEEE Xplore + Scopus
**Bộ lọc:** Year 2018–2026, English only, Conference + Journal
**Ngày search:** 2026-05-25 14:00
**Số kết quả:** 28 papers

---

### String B

**Query nguyên văn:**
`("test case generation") AND ("software engineering")`

**Database:** IEEE Xplore + Scopus + ACM DL
**Bộ lọc:** Year 2018–2026, English only
**Ngày search:** 2026-05-25 15:30
**Số kết quả:** 40 papers

---

### String C

**Query nguyên văn:**
`("automated testing") AND ("generative AI")`

**Database:** IEEE Xplore + Scopus + ACM DL
**Bộ lọc:** Year 2020–2026, English only
**Ngày search:** 2026-05-26 09:00
**Số kết quả:** 40 papers

---

### String D

**Query nguyên văn:**
`("BDD" OR "behavior driven development" OR Gherkin) AND (testing OR automation)`

**Database:** IEEE Xplore + Scopus + ACM DL + arXiv
**Bộ lọc:** Year 2019–2026, English only
**Ngày search:** 2026-05-26 10:30
**Số kết quả:** 19 papers (trước dedup nội bộ string này: ~27; sau cross-string dedup còn 19 unique)

---

## Tổng hợp trước dedup

| Database / String | Kết quả |
|---|---|
| String A (IEEE Xplore + Scopus) | 28 |
| String B (IEEE Xplore + Scopus + ACM DL) | 40 |
| String C (IEEE Xplore + Scopus + ACM DL) | 40 |
| String D (IEEE Xplore + Scopus + ACM DL + arXiv) | 19 |
| Snowballing (Phần S) | 8 |
| **Tổng trước dedup** | **135** |
| **Sau dedup (loại EC1 = 4 trùng lặp)** | **131 → 127** |

> **Ghi chú về dedup:** Thực hiện bằng Zotero. Các paper trùng nhau nhiều nhất là các bài trên IEEE Access xuất hiện cả ở IEEE Xplore và Scopus. Sau khi gộp toàn bộ strings, có 4 trùng lặp bị loại (EC1), còn lại 127 records đưa vào Vòng 1.

---

## Phần S — Cross-reference Search (Snowballing)

> Snowballing không có query string — không điền vào mục này như các String A/B/C.

**Phương pháp:** Backward snowballing — đọc reference list của các paper đã pass V2 screening.

**Thực hiện:** Sau khi có `03_final_included.csv`, đọc reference list của từng paper V2 INCLUDE.

**Công cụ:** CrossRef (`crossref.org`) để lookup metadata từ DOI; Google Scholar để check full-text availability.

**Ngày thực hiện:** 2026-05-28

**Số paper included đã scan:** 16 paper (V2 INCLUDE ban đầu từ Strings A–D)

**Paper mới phát hiện qua snowballing:** 8 paper candidates được phát hiện, trong đó **0 paper** pass V2 IC đầy đủ chưa có trong danh sách (tất cả đã xuất hiện trong Strings A–D hoặc bị loại vì EC4/IC5).

> **Lưu ý:** Snowballing chỉ thực hiện SAU khi hoàn thành tất cả database search. Các paper được tìm qua snowballing nhưng đã có trong `03_final_included.csv` không tính là paper mới.

---

## Ghi chú

- **Công cụ dedup:** Zotero (tự động + kiểm tra thủ công với tiêu đề/DOI)
- **Paper trùng nhiều nhất:** Các bài IEEE Access (ví dụ Karpurapu 2024) xuất hiện ở cả IEEE Xplore và Scopus
- **Snowballing:** 8 paper mới phát hiện, 0 paper pass V2 đầy đủ chưa có trong danh sách
- **Bất thường:** Một paper trong Vòng 1 không ghi rõ lý do loại (id=7); đã đánh dấu là "No reason" trong CSV và review lại ở Vòng 2 — kết quả bị loại EC4 trong V2.
- **String D (Gherkin/BDD):** Kết quả thấp (19) do ngách topic hẹp; bổ sung manual search arXiv để đảm bảo coverage cho GAP-T2.
