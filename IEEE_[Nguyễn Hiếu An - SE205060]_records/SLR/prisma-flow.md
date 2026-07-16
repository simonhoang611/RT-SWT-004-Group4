# PRISMA Flow Diagram — Nhóm SE1905

**Thành viên:** Nguyễn Hiếu An (SE205060)  
**Topic:** LLM for Acceptance Test Automation (BDD/Gherkin)  
**Database:** IEEE Xplore · **Date:** 2026-06-__

---

## Sơ đồ PRISMA (số khớp CSV)

```
[Records từ database searching (N = 211)]        ← Tổng từ search-log.md (S1=39 + S2=17 + S3=155)
        ↓
[Sau khi xóa duplicate (N = 182)]                ← = số dòng trong 01_all_records.csv
        ↓
┌──────────────────────────────────────────────┐
│ Screened title + abstract (N = 182)           │
│ └── Excluded (N = 134):                       │
│       EC-O (off-topic)        = 130           │
│         • off-topic SE domain     73          │
│         • BDD = Binary Decision Diagram 35    │
│         • power/solar/electrical  20          │
│         • GUI test execution      2           │
│       EC-N (no empirical/retracted) = 4       │
│         • SLR/survey              3           │
│         • retracted               1           │
└──────────────────────────────────────────────┘
        ↓ 48 papers pass                         ← = INCLUDE (27) + Unsure (21) trong 02
┌──────────────────────────────────────────────┐
│ Full-text assessed (N = 48)                   │
│ └── Excluded (N = 34):                        │
│       EC-O (off-topic / sai task) = 29        │
│       EC-N (vision/no empirical)  = 5         │
└──────────────────────────────────────────────┘
        ↓
[Final included (N = 14)]                        ← = Count(v2_decision = Include) trong 03
```

---

## Bảng số liệu

| Giai đoạn | N |
|---|---|
| Records từ IEEE Xplore (trước dedup) | 211 |
| Sau khi xóa duplicate | 182 |
| Screened V1 | 182 |
| Excluded V1 | 134 (EC-O = 130, EC-N = 4) |
| Pass V1 (INCLUDE 27 + Unsure 21) | 48 |
| Full-text assessed V2 | 48 |
| Excluded V2 | 34 (EC-O = 29, EC-N = 5) |
| **Final included** | **14** |

---

## Kiểm tra nhất quán (tự check trước khi nộp)

```
✓ Rows trong 01_all_records.csv = 182 = N sau dedup
✓ Count(v1_decision = EXCLUDE) trong 02 = 134 = Excluded V1
✓ Count(v1 = INCLUDE + Unsure) trong 02 = 48 = Full-text assessed
✓ Count(v2_decision = Include) trong 03 = 14 = Final included

Phương trình: 182 − 134 (V1) − 34 (V2) = 14 ✓
Final list: 5 ≤ 14 ≤ 15 ✓
```

> **Lưu ý:** Nếu sau khi đọc full-text paper #12 (Lee 2023) bị loại do không thỏa IC-E, cập nhật: Excluded V2 = 35, Final included = 13, và EC-N V2 = 6.
