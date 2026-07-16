# Search Log — LLM for Acceptance Test Automation (BDD/Gherkin)
**Thành viên:** Nguyễn Minh Hoàng
**Ngày thực hiện:** 2026-06-01

---

## Chuỗi tìm kiếm (Query Strings)

### String A
**Query nguyên văn:**
```
("Gherkin" OR "BDD" OR "acceptance test") AND ("semantic similarity" OR "evaluation" OR "executable")
```
**Database:** Semantics Scholar
**Bộ lọc:** Year 2018–2026, Conference + Journal
**Ngày search:** 2026-05-28 07:30
**Số kết quả:** 12 papers

---

### String B
**Query nguyên văn:**
```
("large language model" OR "LLM" OR "GPT" OR "ChatGPT") AND ("acceptance test" OR "Gherkin" OR "BDD")
```
**Database:** Semantics Scholar
**Bộ lọc:** Year 2024–2026, Conference + Journal
**Ngày search:** 2026-05-28 08:00
**Số kết quả:** 4 papers

---

### String C
**Query nguyên văn:**
```
("Gherkin" OR "BDD" OR "behavior-driven development") AND ("generation" OR "automated") AND ("user story" OR "requirements")
```
**Database:** Semantics Scholar
**Bộ lọc:** Year 2020–2026, Conference + Journal
**Ngày search:** 2026-05-28 08:15
**Số kết quả:** 138 papers

---

## Tổng hợp trước dedup

| Database | String | Kết quả |
|---------|--------|---------|
| Semantics Scholar | String A | 12 |
| Semantics Scholar | String B | 4 |
| Semantics Scholar | String C | 138 |
| **Tổng trước dedup** | | **154** |
| **Sau dedup** | | **142** |
| Số bị loại (trùng lặp) | | 12 |

---

## Ghi chú

- Thực hiện dedup bằng: Zotero
- Số lượng paper tìm được của String C hoàn toàn nhiều hơn số lượng paper tìm được của 2 String còn lại
