"""Validate the 30-row meeting form; never decide labels or sign for raters.
Default checks the prepared template. --final checks entered decisions and
reports counts, leaving the original pre-consensus kappa unchanged.
"""
import argparse, csv, datetime, json, pathlib
IDS={72,76,88,91,98,100,132,164,185,207,224,229,236,238,255}
FACETS={'business_logic','temporal_causal'}
COLS=['id','domain','facet','label_An_confirmed','label_Hoang_independent','agreed_before','final_label','final_severity','reason','evidence_lines','decided_on']
def main():
    p=argparse.ArgumentParser();p.add_argument('--final',action='store_true');p.add_argument('--file',type=pathlib.Path,default=pathlib.Path(__file__).with_name('consensus_15_files.csv'));a=p.parse_args()
    with a.file.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f);assert reader.fieldnames==COLS;rows=list(reader)
    assert len(rows)==30 and {(int(r['id']),r['facet']) for r in rows}=={(i,f) for i in IDS for f in FACETS}
    previous=json.loads(pathlib.Path(__file__).with_name('INITIAL_LABEL_EVIDENCE.json').read_text('utf-8'))
    expected={(r['id'],r['facet']):r for r in previous['rows']}
    for r in rows:
        old=expected[(int(r['id']),r['facet'])]
        assert r['label_An_confirmed']==old['An_label'] and r['label_Hoang_independent']==old['Hoang_label']
        assert r['agreed_before']==('Y' if r['label_An_confirmed']==r['label_Hoang_independent'] else 'N')
        if a.final:
            assert r['final_label'] in {'Y','N','unresolved'},(r['id'],r['facet'],'label')
            assert r['reason'].strip() and r['evidence_lines'].strip()
            datetime.date.fromisoformat(r['decided_on'])
            if r['final_label']!='unresolved':
                assert r['final_severity'] in {'0','1','2','3'}
                assert (int(r['final_severity'])>=2)==(r['final_label']=='Y')
            else:assert r['final_severity']==''
        else:
            assert all(r[k]=='' for k in ['final_label','final_severity','reason','evidence_lines','decided_on'])
    summary={'result':'PASS','mode':'entered_decisions_checked_not_human_attestation' if a.final else 'blank_template_checked','rows':30,'pre_consensus_kappa_B2':0.5714285714285714,'pre_consensus_kappa_H3':0.6086956521739131,'labels_decided_by_script':False,'human_signatures_verified':False}
    if a.final:
        summary['facets']={f:{'resolved':sum(r['facet']==f and r['final_label']!='unresolved' for r in rows),'unresolved':sum(r['facet']==f and r['final_label']=='unresolved' for r in rows),'defective':sum(r['facet']==f and r['final_label']=='Y' for r in rows),'changed_from_An':sum(r['facet']==f and r['final_label'] in {'Y','N'} and r['final_label']!=r['label_An_confirmed'] for r in rows)} for f in FACETS}
        for s in summary['facets'].values():s['defect_rate_of_15']=s['defective']/15 if s['resolved']==15 else None
        summary['files_changed_from_An']=len({r['id'] for r in rows if r['final_label'] in {'Y','N'} and r['final_label']!=r['label_An_confirmed']})
        summary['union_defect_rate_of_15']=len({r['id'] for r in rows if r['final_label']=='Y'})/15 if not any(r['final_label']=='unresolved' for r in rows) else None
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
