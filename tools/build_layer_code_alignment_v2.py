#!/usr/bin/env python3
import argparse,csv,json,inspect,re,sys
from pathlib import Path
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def wjson(p,o): p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def parse(h):
    m=re.search(r'L(\d+)_ch(\d+):(\d+)',h or '')
    return tuple(map(int,m.groups())) if m else None
def shape(x):
    if torch.is_tensor(x): return list(x.shape)
    if isinstance(x,(list,tuple)): return [shape(y) for y in x]
    return str(type(x).__name__)
def src(obj):
    try:
        f=inspect.getsourcefile(obj) or ''; lines,start=inspect.getsourcelines(obj); return f,start,start+len(lines)-1
    except Exception: return '',None,None
def op(l):
    return ['EdgeConvBlock 0 output: local particle-edge feature map','EdgeConvBlock 1 output: neighborhood/context relay map','EdgeConvBlock 2 output: high-level class-evidence map before pooling'][l] if l in (0,1,2) else 'unknown'
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pseudocode',default='reports/latest/tables/pseudocode_operation_database.csv')
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid'); ap.add_argument('--samples-per-file',type=int,default=16); ap.add_argument('--max-files',type=int,default=10)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-csv',default='reports/latest/tables/layer_code_alignment_v2.csv'); ap.add_argument('--out-json',default='manifests/latest/layer_code_alignment_v2.json'); ap.add_argument('--out-md',default='reports/latest/LAYER_CODE_ALIGNMENT_V2.md')
    a=ap.parse_args(); pseudo=readcsv(a.pseudocode); model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    caps={}; hooks=[]
    for li in [0,1,2]:
        m=model.edge_convs[li]
        def hk(mod,inp,out,li=li): caps[f'edge_convs.{li}']={'module_path':f'edge_convs.{li}','module_type':type(mod).__name__,'input_shape':json.dumps(shape(inp),ensure_ascii=False),'output_shape':json.dumps(shape(out),ensure_ascii=False)}
        hooks.append(m.register_forward_hook(hk))
    with torch.no_grad(): _=model(batch['points'],batch['features'],batch['mask'])
    [h.remove() for h in hooks]
    import weaver.nn.model.ParticleNet as PN
    sf,ss,se=src(PN)
    rows=[]
    for r in pseudo:
        h=r.get('head_id',''); p=parse(h)
        if not p: continue
        l,c0,c1=p; mp=f'edge_convs.{l}'; cap=caps.get(mp,{})
        rows.append({'head_id':h,'layer':l,'channels':f'{c0}:{c1}','source_file':sf,'source_lines':f'{ss}-{se}' if ss else '', 'source_module':'weaver.nn.model.ParticleNet','module_path':mp,'module_type':cap.get('module_type','EdgeConvBlock'),'input_shape':cap.get('input_shape',''),'output_shape':cap.get('output_shape',''),'channel_slice':f'output[:, {c0}:{c1}, :]','code_operation':op(l),'semantic_pseudocode':r.get('pseudocode',''),'alignment_confidence':'HIGH_FOR_LAYER_OUTPUT','remaining_gap':'Need inner EdgeConv trace for knn/graph_feature/conv/aggregation substeps'})
    wcsv(a.out_csv,rows); wjson(a.out_json,{'ok':True,'captured_modules':list(caps.values()),'rows':len(rows),'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    md=['# Layer Code Alignment v2\n\nCorrected alignment: pseudo-heads map to EdgeConvBlock outputs, not inner conv sublayers.\n\n','## EdgeConv outputs\n',mdtab(['module','input','output'],[[c['module_path'],c['input_shape'],c['output_shape']] for c in caps.values()]),'\n## Pseudo-head alignment\n',mdtab(['head','module','slice','operation','shape'],[[r['head_id'],r['module_path'],r['channel_slice'],r['code_operation'],r['output_shape']] for r in rows])]
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'rows':len(rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
