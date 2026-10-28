"""Reconstruct exact saved prompt components. Standard library only; no API calls.

Run from a merged repository: python revision/prompts/make_prompt_artifacts.py
Optional: --repo PATH --out PATH. Does not execute notebook top-level code or
import the API runner. Only its literal constants and three pure functions run.

CSV fields are read with CRLF converted to LF. .gitattributes does not protect
data/, so a Windows checkout with core.autocrlf=true turns the LF line breaks
stored in Git into CRLF; without this step the six exemplar stories (and their
hashes) would depend on the checkout. Source hashes are likewise taken on LF bytes.
"""
import argparse, ast, csv, hashlib, json, pathlib

def digest(b): return hashlib.sha256(b).hexdigest()
def read_csv(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return [{k:v.replace('\r\n','\n') for k,v in r.items()} for r in csv.DictReader(f)]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[2]);ap.add_argument('--out',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parent);a=ap.parse_args()
    repo=a.repo.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
    csv.field_size_limit(2**31-1)
    inputs=['scripts/run_experiment.ipynb','revision/h2/h2_run_prompts.py','data/full_user_stories.csv','data/full_ground_truth.csv']
    nb=json.loads((repo/inputs[0]).read_text('utf-8'))
    tree=ast.parse((repo/inputs[1]).read_text('utf-8'))
    scope={}
    wanted={'MODEL','TEMPERATURE','C0_EXEMPLARS','C2_EXEMPLARS','SYS','SYS_SOCIAL'}
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in wanted:
            scope[node.targets[0].id]=ast.literal_eval(node.value)
    functions=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'sys_msg','one_shot_prompt','zero_shot_prompt'}]
    assert len(functions)==3
    exec(compile(ast.Module(body=functions,type_ignores=[]),'<isolated pure prompt functions>','exec'),scope)
    gt={int(r['id']):r for r in read_csv(repo/inputs[3])};us={int(r['id']):r for r in read_csv(repo/inputs[2])}
    original={}
    for stem,i in [('eco',2),('fin',102),('soc',202)]:original['us_'+stem]=us[i]['user_story'];original['gk_'+stem]=gt[i]['gherkin_content'].replace('\\n','\n')
    nodes=[n for n in ast.parse(''.join(nb['cells'][7]['source'])).body if isinstance(n,ast.FunctionDef) and n.name=='get_context_aware_prompt'];assert len(nodes)==1
    exec(compile(ast.Module(body=nodes,type_ignores=[]),'<isolated original notebook function>','exec'),original)
    artifacts={};mapping=[]
    for domain,stem in [('E-commerce','ecommerce'),('Finance/Banking','finance'),('Social Network','social')]:
        artifacts['system_message_'+stem+'.txt']=scope['sys_msg'](domain).encode('utf-8')
        assert original['get_context_aware_prompt'](domain,'{user_story}')[0]==scope['sys_msg'](domain)
    artifacts['user_prompt_one_shot_template.txt']=scope['one_shot_prompt']('{example_user_story}','{example_gherkin}','{user_story}').encode('utf-8')
    artifacts['user_prompt_zero_shot_template.txt']=scope['zero_shot_prompt']('{user_story}').encode('utf-8')
    for condition,key in [('C0','C0_EXEMPLARS'),('C2','C2_EXEMPLARS')]:
        for domain,i in scope[key].items():
            mapping.append({'condition':condition,'project':gt[i]['project_name'],'domain':domain,'exemplar_id':i})
            artifacts[f'exemplars/ex_{i}_user_story.txt']=us[i]['user_story'].encode('utf-8')
            artifacts[f'exemplars/ex_{i}.feature']=gt[i]['gherkin_content'].replace('\\n','\n').encode('utf-8')
    import io
    text=io.StringIO(newline='');w=csv.DictWriter(text,fieldnames=['condition','project','domain','exemplar_id'],lineterminator='\n');w.writeheader();w.writerows(mapping)
    artifacts['exemplar_mapping.csv']=text.getvalue().encode('utf-8')
    assert len(artifacts)==18
    # Check every reconstructed C0 message, including the trailing newline/spaces.
    for i,r in us.items():
        domain=r['domain'];ex=scope['C0_EXEMPLARS'][domain]
        actual=(scope['sys_msg'](domain),scope['one_shot_prompt'](us[ex]['user_story'],gt[ex]['gherkin_content'].replace('\\n','\n'),r['user_story']))
        assert original['get_context_aware_prompt'](domain,r['user_story'])==actual,i
    for name,data in artifacts.items():
        p=out/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    manifest=''.join(digest(data)+'  '+name+'\n' for name,data in sorted(artifacts.items()))
    (out/'MANIFEST_SHA256.txt').write_bytes(manifest.encode('utf-8'))
    info={'result':'PASS','API_calls':0,'system_messages_equal_to_notebook':3,'C0_messages_equal_to_notebook':len(us),'artifact_count_excluding_manifest':18,'ex_119_decoded_characters':len(artifacts['exemplars/ex_119.feature'].decode('utf-8')),'ex_119_bytes':len(artifacts['exemplars/ex_119.feature']),'artifact_sha256':{n:digest(b) for n,b in sorted(artifacts.items())},'source_sha256_lf':{n:digest((repo/n).read_bytes().replace(b'\r\n',b'\n')) for n in inputs},'historical_request_log':False,'note':'Exact reconstruction from saved source/data, not recovery of transmitted API payload logs.'}
    (out/'PROMPT_EXPORT_CHECK.json').write_bytes((json.dumps(info,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    print(json.dumps({k:v for k,v in info.items() if k not in {'artifact_sha256','source_sha256_lf'}},indent=2))
if __name__=='__main__':main()
