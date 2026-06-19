#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def loadjson(p):
    p=Path(p)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}
def wjson(p,o): p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rs])+'\n'
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--summary',default='reports/latest/tables/hqql_tbl_confusion_physics_summary.csv')
    ap.add_argument('--manifest',default='manifests/latest/hqql_tbl_confusion_physics_regime_v1.json')
    ap.add_argument('--min-confused',type=int,default=100)
    ap.add_argument('--out-json',default='manifests/latest/phase1_hqql_tbl_stats_gate_v1.json')
    ap.add_argument('--out-md',default='reports/latest/PHASE1_HQQL_TBL_STATS_GATE_V1.md')
    a=ap.parse_args(); rows=readcsv(a.summary); manifest=loadjson(a.manifest)
    by={r.get('group'):r for r in rows}
    h2t=int(float(by.get('Hqql_to_Tbl',{}).get('n',0) or 0)); t2h=int(float(by.get('Tbl_to_Hqql',{}).get('n',0) or 0))
    status='PASS' if h2t>=a.min_confused and t2h>=a.min_confused else 'NEEDS_MORE_STATS'
    rec=[]
    if h2t<a.min_confused: rec.append('increase samples/files for Hqql_to_Tbl')
    if t2h<a.min_confused: rec.append('increase samples/files for Tbl_to_Hqql')
    out={'ok':True,'status':status,'min_confused':a.min_confused,'Hqql_to_Tbl':h2t,'Tbl_to_Hqql':t2h,'groups':manifest.get('groups',{}),'recommendations':rec}
    wjson(a.out_json,out)
    md=['# Phase 1 Hqql/Tbl Stats Gate v1\n\n','This gate checks whether Phase 1 has enough confused events for physics-regime claims.\n\n',f'- Status: **{status}**\n',f'- Required confused events per direction: **{a.min_confused}**\n\n','## Counts\n',mdtab(['group','n'],[[k,v.get('n','')] for k,v in by.items()]),'\n## Recommendations\n']
    if rec: md += ['\n'.join('- '+x for x in rec)+'\n']
    else: md += ['- Enough confusion events for the next Phase 2/3 tests.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
