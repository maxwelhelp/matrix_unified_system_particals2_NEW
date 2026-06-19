#!/usr/bin/env python3
import argparse,json,glob,os
from pathlib import Path

def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')

def pick_tree(f):
    import uproot
    trees=[]
    for k,v in f.items():
        try:
            if hasattr(v,'num_entries') and hasattr(v,'keys'):
                trees.append((k,v))
        except Exception:
            pass
    if not trees: return None,None
    trees=sorted(trees,key=lambda kv: getattr(kv[1],'num_entries',0),reverse=True)
    return trees[0]

def short_arr_info(tree, branches, n=3):
    info={}
    try:
        arrs=tree.arrays(branches[:min(len(branches),40)],entry_stop=n,library='ak')
        for b in arrs.fields:
            a=arrs[b]
            info[b]={'type':str(a.type),'preview':str(a[:1])[:300]}
    except Exception as e:
        info['_error']=repr(e)
    return info

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--data-dir',default=os.path.expanduser('~/Рабочий стол/jetclass_tiny')); ap.add_argument('--max-files',type=int,default=5); ap.add_argument('--out-dir',default='runs/jetclass_root_probe_v1')
    a=ap.parse_args(); out=Path(a.out_dir); mkdir(out)
    import uproot
    files=sorted(glob.glob(str(Path(a.data_dir)/'**/*.root'),recursive=True))[:a.max_files]
    rec={'data_dir':a.data_dir,'n_files':len(files),'files':[],'global_branch_counts':{}}
    for fp in files:
        f=uproot.open(fp); tname,tree=pick_tree(f)
        item={'file':fp,'tree':tname,'num_entries':int(tree.num_entries) if tree is not None else 0,'branches':[],'groups':{},'sample':{}}
        if tree is not None:
            branches=list(tree.keys())
            item['branches']=branches
            for b in branches: rec['global_branch_counts'][b]=rec['global_branch_counts'].get(b,0)+1
            groups={
              'part':[b for b in branches if b.startswith('part_') or b.startswith('pf') or b.startswith('pfcand')],
              'sv':[b for b in branches if b.startswith('sv_')],
              'label':[b for b in branches if b.startswith('label') or b.startswith('truth')],
              'jet':[b for b in branches if b.startswith('jet_')],
              'weight':[b for b in branches if 'weight' in b.lower()],
            }
            item['groups']=groups
            sample_br=[]
            for g in ['part','sv','label','jet']:
                sample_br += groups[g][:12]
            item['sample']=short_arr_info(tree,sample_br)
        rec['files'].append(item)
    wjson(out/'jetclass_root_probe.json',rec)
    md=['# JetClass ROOT probe v1\n\n',f"data_dir={a.data_dir}\nn_files={len(files)}\n\n"]
    for item in rec['files']:
        md.append(f"## {Path(item['file']).name}\n")
        md.append(f"tree={item['tree']} entries={item['num_entries']} branches={len(item['branches'])}\n\n")
        for g,bs in item.get('groups',{}).items(): md.append(f"- {g}: {bs[:30]}\n")
        md.append('\n')
    (out/'JETCLASS_ROOT_PROBE_REPORT.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False)[:20000])
if __name__=='__main__': main()
