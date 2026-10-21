"""Read-only verification of the supplied paired labels. Does not change annotations."""
from pathlib import Path
from fractions import Fraction
import csv,json

def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
    ids=[int(r['id']) for r in rows]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate IDs')
    return {int(r['id']):r for r in rows}

def main():
    root=Path(__file__).resolve().parent;out={}
    expected={72,76,88,91,98,100,132,164,185,207,224,229,236,238,255}
    for facet,label in [('b2','has_business_defect'),('h3','has_temporal_causal_defect')]:
        # Repository layout: An's confirmed sheets are in the sibling folders revision/audit/02_B2_semantic_defects/
        # and revision/audit/03_H3_temporal_causal/; Hoang's CLEAN sheets are next to this script.
        a=read(root.parent/{'b2':'02_B2_semantic_defects','h3':'03_H3_temporal_causal'}[facet]/f'{facet}_annotation_An_CONFIRMED.csv')
        b=read(root/f'{facet}_annotation_Hoang_CLEAN.csv')
        if len(a)!=60 or set(b)!=expected or not expected.issubset(a):raise ValueError('Wrong analysis IDs')
        pairs=[(a[i][label],b[i][label]) for i in sorted(b)]
        if any(v not in {'Y','N'} for p in pairs for v in p):raise ValueError('Nonbinary/blank label')
        matrix={x:{y:sum(p==(x,y) for p in pairs) for y in ['Y','N']} for x in ['Y','N']}
        n=len(pairs);po=Fraction(sum(x==y for x,y in pairs),n)
        pe=sum(Fraction(sum(x==c for x,y in pairs)*sum(y==c for x,y in pairs),n*n) for c in ['Y','N'])
        k=None if pe==1 else (po-pe)/(1-pe)
        out[facet]={'N':n,'rows_An_cols_Hoang':matrix,'observed_agreement':float(po),'expected_agreement':float(pe),'kappa':float(k) if k is not None else None,'exact_fraction':str(k),'disagreement_ids':[i for i in sorted(b) if a[i][label]!=b[i][label]]}
    print(json.dumps(out,indent=2))
    # Also write the same JSON to kappa_result.json next to this script (the annotation files are not changed).
    (root/'kappa_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
