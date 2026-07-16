# Search Log — SLR: LLM for Acceptance Test Automation (BDD/Gherkin)
**Student:** Võ Hiếu Chương — SE204862  
**Date:** 2026-05-31  
**Database:** Google Scholar  

---

## Search Strings Đã Chạy

| # | String | Kết quả (pre-dedup) | Ngày chạy |
|---|--------|-------------------|-----------|
| A | `("Gherkin" OR "BDD" OR "behavior-driven") AND ("generation" OR "automated") AND ("LLM" OR "GPT" OR "large language model") AND ("user story" OR "acceptance test" OR "test case")` | **215** | 2026-05-31 |

> **Ghi chú:** Chỉ 1 search string được sử dụng. String A đã bao phủ đủ các keyword từ tất cả 4 thành phần PICO (P: user story/BDD, I: LLM/GPT, C: generation/automated, O: acceptance test/test case), nên không cần thêm string bổ sung. Kết quả 215 records sau khi thu thập thủ công từ Google Scholar đã đủ để đạt ngưỡng ≥30 records sau dedup theo yêu cầu Checkpoint 1.2.

---

## PRISMA Record Count

| Bước | Số | File |
|------|----|------|
| Tổng records thu thập (pre-dedup) | **215** | `00_raw_records.csv` |
| Duplicate bị xóa (theo cột Title) | **146** | — |
| Sau dedup | **69** | `01_all_records.csv` |
| Excluded vòng 1 (title + abstract) | **36** | `02_after_screening_v1.csv` |
| Vào vòng 2 (full-text) | **32** | — |
| Excluded vòng 2 (full-text) | **20** | `03_final_included.csv` |
| **Included cuối (Evidence Table)** | **12** | `03_final_included.csv` |

---

## Ghi chú phương pháp

- Dedup thực hiện theo cột `Title` (exact match).
- Khi trùng, giữ bản xuất hiện đầu tiên (`keep='first'`).
- Metadata crawl thủ công từ Google Scholar: Title, Authors, Year, Venue, Link.
- Google Scholar không hỗ trợ export tự động nên metadata được nhập vào CSV thủ công.
