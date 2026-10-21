from pathlib import Path
import sys, contextlib, io
import pandas as pd
import behave
ROOT=Path(__file__).resolve().parent.parent
REPO=ROOT.parent.parent  # repository root (this script is in revision/audit/07_audit/)
sys.path.insert(0,str(ROOT/'03_H3_temporal_causal'))
from h3_order_check import analyse_text, ERRORS, WARNINGS
gt=pd.read_csv(REPO/'data/full_ground_truth.csv')
meta=gt[['id','domain','project_name']]
gen=pd.read_csv(REPO/'results/full_gpt54mini_output.csv')
rows=[]; details=[]
for source,df,col in [('generated',gen,'generated_gherkin'),('expert_GT',gt,'gherkin_content')]:
    for _,r in df[~df.id.isin([2,102,202])].iterrows():
        with contextlib.redirect_stdout(io.StringIO()): s,d=analyse_text(r[col])
        rows.append(dict(source=source,id=int(r.id),parse_ok=s is not None,**(s or {})))
        if d: details.extend(dict(source=source,id=int(r.id),**e) for e in d)
out=pd.DataFrame(rows).merge(meta,on='id',validate='many_to_one')
version=behave.__version__.replace('.','')
out.to_csv(ROOT/'03_H3_temporal_causal'/f'h3_structure_excluded_behave{version}.csv',index=False)
pd.DataFrame(details).merge(meta,on='id').to_csv(ROOT/'03_H3_temporal_causal'/f'h3_detail_excluded_behave{version}.csv',index=False)
summary=[]
for (src,dom),g in out.groupby(['source','domain']):
    ok=g[g.parse_ok]
    summary.append(dict(behave_version=behave.__version__,source=src,domain=dom,
      total_files=len(g),parse_ok=len(ok),parse_fail=len(g)-len(ok),
      error_files=int(ok.file_has_error.eq(True).sum()),n_scenarios=int(ok.n_scenarios.sum()),
      **{c:int(ok[c].sum()) for c in ERRORS+WARNINGS}))
pd.DataFrame(summary).to_csv(ROOT/'07_audit'/f'h3_summary_behave{version}.csv',index=False)
print(pd.DataFrame(summary).to_string(index=False))
