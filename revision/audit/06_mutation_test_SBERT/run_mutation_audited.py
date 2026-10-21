"""Exact fixed legacy sample/operators plus explicit validity and batch CPU SBERT."""
from pathlib import Path
import argparse, json, random, sys, hashlib, contextlib, io, importlib.metadata
import pandas as pd
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
HERE=Path(__file__).resolve().parent
REPO=HERE.parent.parent.parent  # repository root (this script is in revision/audit/06_mutation_test_SBERT/)
sys.path.insert(0,str(HERE))
import mutation_sbert_test as legacy
from behave.parser import parse_feature
from h3_order_check import analyse_text, ERRORS

def parse_audit(text):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        try:
            f=parse_feature(text.replace('\\n','\n'))
            if f is None: raise ValueError('No Feature')
            summary, detail=analyse_text(text)
            return {'parse_status':'PASS','parser_error':'','h3_errors':'|'.join(e for e in ERRORS if summary[e]),
                    'h3_all_flags':'|'.join(sorted({v for d in detail for v in d['violations'].split('|')})),
                    'n_scenarios':summary['n_scenarios']}
        except Exception as e:
            return {'parse_status':'FAIL','parser_error':str(e)[:300],'h3_errors':'','h3_all_flags':'','n_scenarios':0}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--model',required=True,help='local safetensors snapshot path')
    ap.add_argument('--revision',required=True)
    a=ap.parse_args()
    out=HERE/'results_audited'; out.mkdir(exist_ok=True)
    gt=pd.read_csv(REPO/'data/full_ground_truth.csv')
    gt=gt[~gt.id.isin([2,102,202])]
    rng=random.Random(legacy.SEED)
    pool=[]
    for _,r in gt.iterrows():
        for header,sc in legacy.extract_scenarios(r.gherkin_content):
            pool.append((int(r.id),r.domain,header,sc,'Background:' in r.gherkin_content))
    chosen=[]
    for d in sorted({p[1] for p in pool}):
        cand=[p for p in pool if p[1]==d]; rng.shuffle(cand)
        chosen+=cand[:40]
    assert len(chosen)==120
    texts={}; rows=[]; examples=[]; samples=[]
    for sid,(fid,dom,header,sc,bg) in enumerate(chosen):
        orig='\n'.join(header+sc); orig_audit=parse_audit(orig)
        samples.append(dict(sample=sid,id=fid,domain=dom,scenario=sc[0].strip(),
                            background_present_in_source=bg,original_text=orig,**orig_audit))
        sk_o=legacy.to_skeleton(orig); texts[sk_o]=None
        for op,fn in legacy.OPERATORS.items():
            mut_sc=fn(sc)
            if mut_sc is None or mut_sc==sc: continue
            mut='\n'.join(header+mut_sc); sk_m=legacy.to_skeleton(mut); texts[sk_m]=None
            mut_audit=parse_audit(mut)
            r=dict(sample=sid,id=fid,domain=dom,family=legacy.FAMILY[op],operator=op,
                skeleton_identical=sk_o==sk_m,detected_by_h3=legacy.h3_detect(mut_sc),
                orig_detected_by_h3=legacy.h3_detect(sc),background_omitted_in_legacy_extraction=bg,
                original_parse_status=orig_audit['parse_status'],mutant_parse_status=mut_audit['parse_status'],
                original_h3_errors=orig_audit['h3_errors'],mutant_h3_errors=mut_audit['h3_errors'],
                original_h3_all_flags=orig_audit['h3_all_flags'],mutant_h3_all_flags=mut_audit['h3_all_flags'],
                mutant_parser_error=mut_audit['parser_error'])
            r['_sk_o']=sk_o; r['_sk_m']=sk_m; rows.append(r)
            if sum(e['operator']==op for e in examples)<3:
                examples.append(dict(operator=op,sample=sid,id=fid,domain=dom,original=orig,mutant=mut))
    torch.set_num_threads(4)
    model=SentenceTransformer(a.model,device='cpu',local_files_only=True,trust_remote_code=False)
    model.eval()
    print(f'Selected={len(chosen)}, mutants={len(rows)}, unique skeletons={len(texts)}',flush=True)
    emb=model.encode(list(texts),batch_size=32,normalize_embeddings=True,show_progress_bar=False)
    vectors=dict(zip(texts,emb))
    for r in rows:
        r['cosine_orig_vs_mutant']=float(np.dot(vectors[r.pop('_sk_o')],vectors[r.pop('_sk_m')]))
        r['cosine_ge_0_85']=r['cosine_orig_vs_mutant']>=legacy.THRESH
        r['pair_parser_valid_baseline_no_hard_error']=(r['original_parse_status']=='PASS' and
            r['mutant_parse_status']=='PASS' and not r['original_h3_errors'])
    res=pd.DataFrame(rows)
    res.to_csv(out/'mutation_results.csv',index=False)
    pd.DataFrame(samples).to_csv(out/'selected_scenarios.csv',index=False)
    def summarize(df):
        result=[]
        for (fam,op),g in df.groupby(['family','operator']):
            result.append(dict(family=fam,operator=op,N=len(g),
              median_cosine=g.cosine_orig_vs_mutant.median(),
              above_threshold_pct=100*g.cosine_ge_0_85.mean(),
              skeleton_identical_pct=100*g.skeleton_identical.mean(),
              detected_by_h3_error_pct=100*g.detected_by_h3.mean(),
              original_h3_error_pct=100*g.orig_detected_by_h3.mean(),
              mutant_parse_fail_n=int((g.mutant_parse_status!='PASS').sum())))
        return pd.DataFrame(result)
    summ=summarize(res); summ.to_csv(out/'mutation_summary.csv',index=False)
    valid=summarize(res[res.pair_parser_valid_baseline_no_hard_error])
    valid.to_csv(out/'mutation_summary_valid_pairs.csv',index=False)
    (out/'counterexamples').mkdir(exist_ok=True)
    for e in examples:
        fn=out/'counterexamples'/f"{e['operator']}_sample{e['sample']}_id{e['id']}.feature"
        fn.write_text(f"# Two separate features for side-by-side inspection; do not parse this combined file.\n# Original sample={e['sample']} id={e['id']} domain={e['domain']}\n{e['original']}\n\n# Perturbation {e['operator']}\n{e['mutant']}\n",encoding='utf-8')
    meta=dict(repo_id='sentence-transformers/all-MiniLM-L6-v2',revision=a.revision,
      seed=legacy.SEED,threshold=legacy.THRESH,n_per_domain=40,excluded_ids=[2,102,202],
      max_seq_length=model.max_seq_length,embedding_dimension=model.get_sentence_embedding_dimension(),
      device='cpu',dtype='float32',batch_size=32,normalize_embeddings=True,
      original_script_sha256=hashlib.sha256((HERE/'mutation_sbert_test.py').read_bytes()).hexdigest(),
      libraries={n:importlib.metadata.version(n) for n in ['sentence-transformers','transformers','torch','numpy','pandas','scipy','behave']},
      selected_n=len(chosen),mutants_n=len(res),
      original_parser_fail_n=sum(s['parse_status']!='PASS' for s in samples),
      original_h3_error_n=sum(bool(s['h3_errors']) for s in samples),
      samples_source_background_n=sum(s['background_present_in_source'] for s in samples),
      valid_pair_n=int(res.pair_parser_valid_baseline_no_hard_error.sum()))
    (HERE/'model_run_metadata.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    # Exact tokenizer audit of full original feature skeletons, not rough word counts.
    gen=pd.read_csv(REPO/'results/full_gpt54mini_output.csv')
    toks=[]
    for source,df,col in [('GT',pd.read_csv(REPO/'data/full_ground_truth.csv'),'gherkin_content'),
                          ('generated',gen,'generated_gherkin')]:
        skels=[legacy.to_skeleton(x) for x in df[col]]
        lengths=[len(x) for x in model.tokenizer(skels,add_special_tokens=True,truncation=False)['input_ids']]
        toks.extend(dict(source=source,id=int(fid),tokens_with_special=n,
            would_truncate_256=n>model.max_seq_length,exemplar=int(fid) in [2,102,202])
            for fid,n in zip(df.id,lengths))
    token_df=pd.DataFrame(toks)
    token_df.to_csv(out/'skeleton_token_lengths.csv',index=False)
    print(summ.round(6).to_string(index=False))
    print('Validity:',json.dumps({k:v for k,v in meta.items() if k.endswith('_n')}))
    print('Truncation:',token_df.groupby('source').would_truncate_256.agg(['sum','count']).to_dict())

if __name__=='__main__': main()
