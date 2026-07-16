# Search Log — LLM for Acceptance Test Automation (BDD/Gherkin)

**Người thực hiện:** Tran Tuan Khang (SE204881)  
**Nhóm:** SE1905  
**Date:** 2026-05-28 đến 2026-05-31  

---

## 1. Database chính

| Database | URL | Lý do chọn |
|---|---|---|
| **OpenAlex** | https://openalex.org | Miễn phí, API công khai, bao phủ rộng từ IEEE / ACM / Springer / arXiv |

---

## 2. Query Strings đã dùng

| # | Query String | Kết quả (trước dedup) |
|---|---|---|
| Q1 | `"LLM" AND "Gherkin" AND "test generation"` | 113 records |
| Q2 | `"BDD" AND "acceptance test" AND "large language model"` | 127 records |

**Tổng cộng trước dedup:** 113 + 127 = **240 records**

---

## 3. Deduplication

| Bước | Số lượng |
|---|---|
| Tổng records cào được | 240 |
| Duplicate bị xóa (cùng DOI / tiêu đề) | 62 |
| **Records sau dedup (đưa vào V1)** | **178** |

---

## 4. V1 Screening (Title + Abstract)

| Kết quả V1 | Số lượng |
|---|---|
| INCLUDE | 30 |
| EXCLUDE | 9 |
| UNSURE *(xem ghi chú bên dưới)* | 139 |

### ⚠️ Ghi chú về tỷ lệ UNSURE cao ban đầu (78%)

Trong quá trình V1 screening, **139/178 papers (78%)** ban đầu được đánh dấu `UNSURE`. Lý do:

- OpenAlex không lưu đầy đủ Abstract cho nhiều papers (đặc biệt các bài từ ACM, Springer, SCITEPRESS). Khi không có Abstract, không thể đưa ra quyết định INCLUDE/EXCLUDE chắc chắn chỉ dựa vào tiêu đề.
- Thay vì loại bỏ vội, toàn bộ UNSURE được đưa vào V2 để đọc full-text — đây là thực hành chuẩn trong SLR để tránh bỏ sót papers tiềm năng.

---

## 5. V2 Screening (Full-text)

| Kết quả V2 | Số lượng |
|---|---|
| Full-text reviewed | 169 |
| Excluded tại V2 | 159 |
| **Included vào Evidence Table** | **10** |

> *Lưu ý: Trong 12 records V2 INCLUDE ban đầu, có 1 bản duplicate (preprint + journal version của cùng paper) và 1 replication data package (Zenodo) → sau deduplication còn **10 unique papers** trong Evidence Table.*

---

## 6. Inclusion/Exclusion Criteria áp dụng

Xem chi tiết tại [ie_criteria.md](ie_criteria.md)

| Mã | Loại | Tiêu chí |
|---|---|---|
| IC1 | Include | Nghiên cứu về tự động sinh Gherkin/BDD test từ user stories |
| IC2 | Include | Sử dụng LLM (hoặc NLP tool) làm phương pháp chính |
| IC3 | Include | Có kết quả đo lường định lượng (metric) |
| EC1 | Exclude | Không liên quan đến testing (y học, tài chính, v.v.) |
| EC2 | Exclude | Ngôn ngữ không phải tiếng Anh |
| EC3 | Exclude | Không truy cập được full-text |
| EC4 | Exclude | Chỉ là abstract / poster / workshop without proceedings |
