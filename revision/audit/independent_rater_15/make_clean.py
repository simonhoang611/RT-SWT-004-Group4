"""Mechanical clean-up of Hoang's two sheets. Labels, counts and severities are not touched.
Changes: 'N/A' -> 'NA'; n_AC_with_precondition text like '3 (AC1, AC2)' -> 3 with the list moved to note;
in rows with no defect, text in evidence/quote columns is moved to note and the column set to NA (rule: NA when no error).
Every change is written to clean_changes.csv."""
import csv, re, sys, os
d = os.path.dirname(os.path.abspath(__file__))
log = []
def rd(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        r = csv.DictReader(f); return r.fieldnames, list(r)
def wr(p, cols, rows):
    with open(p, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, cols); w.writeheader(); w.writerows(rows)
def setv(sheet, r, k, v):
    if r[k] != v: log.append([sheet, r['id'], k, r[k], v]); r[k] = v
D = ['D_NUM','D_OP','D_NEG','D_COND','D_OUTCOME','D_MISSING_AC','D_EXTRA','D_ORDER']
cols, rows = rd(os.path.join(d, 'b2_annotation_Hoang_ORIGINAL.csv'))
for r in rows:
    for k in cols:
        if r[k].strip() == 'N/A': setv('B2', r, k, 'NA')
    if sum(float(r[k]) for k in D) == 0:
        moved = [f"{k}: {r[k].strip()}" for k in ('evidence_gen_line','evidence_US_or_GT_line') if r[k].strip() not in ('', 'NA')]
        if moved:
            setv('B2', r, 'note', r['note'].rstrip() + ' | REFERENCE LINE (no defect): ' + ' ; '.join(moved))
            for k in ('evidence_gen_line','evidence_US_or_GT_line'): setv('B2', r, k, 'NA')
wr(os.path.join(d, 'b2_annotation_Hoang_CLEAN.csv'), cols, rows)
H = ['PRE_missing','ACTION_wrong','POST_missing','CAUSAL_wrong','ORDER_wrong']
cols, rows = rd(os.path.join(d, 'h3_annotation_Hoang_ORIGINAL.csv'))
for r in rows:
    for k in cols:
        if r[k].strip() == 'N/A': setv('H3', r, k, 'NA')
    m = re.match(r'^\s*(\d+)\s*(?:\((.*)\))?\s*$', r['n_AC_with_precondition'])
    if not m: sys.exit(f"cannot parse n_AC_with_precondition for id {r['id']}: {r['n_AC_with_precondition']!r}")
    if m.group(2):
        setv('H3', r, 'note', r['note'].rstrip() + f' | ACS WITH PRECONDITION: {m.group(2).strip()}')
    setv('H3', r, 'n_AC_with_precondition', m.group(1))
    if all(float(r[k]) == 0 for k in H) and r['counterexample_quote'].strip() not in ('', 'NA'):
        setv('H3', r, 'note', r['note'].rstrip() + ' | REFERENCE LINE (no defect): ' + r['counterexample_quote'].strip())
        setv('H3', r, 'counterexample_quote', 'NA')
wr(os.path.join(d, 'h3_annotation_Hoang_CLEAN.csv'), cols, rows)
with open(os.path.join(d, 'clean_changes.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f); w.writerow(['sheet','id','column','old','new']); w.writerows(log)
print(len(log), 'changes')
