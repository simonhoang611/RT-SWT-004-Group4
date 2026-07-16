# PRISMA Flowchart — SLR Screening
---

```
┌─────────────────────────────────────────────┐
│         Records từ database searching        │
│               (N = 131)                      │
│  String A: 28 | String B: 40                 │
│  String C: 40 | String D: 19                 │
│  Snowballing: 8 (cross-ref)                  │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│         Sau khi xóa duplicate                │
│               (N = 127)                      │
│         (Removed: N = 4, EC1)                │
└─────────────────┬───────────────────────────┘
                  │
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Vòng 1 ━━━━━━━━
                  │
                  ▼
┌────────────────────────────┐     ┌────────────────────────────────────┐
│  Screened title + abstract  │────▶│  Excluded (N = 71)                 │
│        (N = 127)            │     │  IC1 (not English): 2              │
└────────────────┬────────────┘     │  IC3 (not peer-reviewed): 7        │
                 │                  │  IC5 (no empirical results): 10    │
                 │                  │  EC2 (no PDF): 3                   │
                 │                  │  EC4 (not test generation): 48     │
                 │                  │  No reason recorded: 1             │
                 │                  └────────────────────────────────────┘
                 │
                 │  INCLUDE + UNSURE → N = 56
                 │  (INCLUDE: 41, UNSURE: 15)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Vòng 2 ━━━━━━━━
                 │
                 ▼
┌────────────────────────────┐     ┌────────────────────────────────────┐
│   Full-text assessed        │────▶│  Excluded (N = 43)                 │
│        (N = 56)             │     │  IC3 (not peer-reviewed): 13       │
└────────────────┬────────────┘     │  IC4 (not relevant): 1             │
                 │                  │  IC5 (no empirical results): 10    │
                 │                  │  EC2 (no PDF): 6                   │
                 │                  │  EC4 (not test generation): 13     │
                 │                  └────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│       Included trong Evidence Table          │
│               (N = 13)                       │
└─────────────────────────────────────────────┘
```

---

## Tóm tắt số liệu

| Bước | N | Xác nhận |
|------|---|---|
| Records từ database searching | 131 | Search log (4 strings + snowballing) |
| Sau khi xóa duplicate (EC1) | 127 | CSV: 127 rows ✓ |
| Vòng 1 — Screened (title + abstract) | 127 | CSV: 127 rows ✓ |
| Vòng 1 — Excluded | 71 | CSV: v1_decision=EXCLUDE: 71 ✓ |
| Vòng 2 — Full-text assessed | 56 | CSV: v1∈{INCLUDE,UNSURE}: 56 ✓ |
| Vòng 2 — Excluded | 43 | CSV: v2_decision=EXCLUDE: 43 ✓ |
| **Final included** | **13** | **CSV: v2_decision=INCLUDE: 13 ✓** |

---

