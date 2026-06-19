#!/usr/bin/env python3
import csv, json
from collections import Counter
from pathlib import Path

SUMMARY='reports/latest/tables/part_attention_path_summary_real_contract_v1.csv'
META='manifests/latest/part_attention_supertrace_real_contract_v1.json'
OUT_MD='reports/latest/PART_REAL_CONTRACT_PSEUDOCODE_COMPILER_V1.md'
OUT_JSON='manifests/latest/part_real_contract_pseudocode_compiler_v1.json'

def read_csv(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def num(x):
    try: return float(x)
    except Exception: return 0.0

def split_pair(p):
    return p.split('<-',1) if '<-' in p else [p,'']

def fam(r):
    if r in ('electron','muon'): return 'lepton'
    if r in ('charged_hadron','neutral_hadron'): return 'hadron'
    if r == 'photon': return 'photon'
    if r == 'CLS': return 'CLS'
    if r == 'pad': return 'pad'
    return 'other'

def route_type(pair):
    q,k=split_pair(pair); fq,fk=fam(q),fam(k)
    if 'pad' in (fq,fk): return 'PAD_MULTIPLICITY_OR_MASK_SIGNAL'
    if fq=='lepton' and fk=='lepton': return 'LEPTON_LEPTON_ROUTE'
    if 'lepton' in (fq,fk) and 'photon' in (fq,fk): return 'LEPTON_PHOTON_ROUTE'
    if fq=='hadron' and fk=='lepton': return 'HADRON_READS_LEPTON_ROUTE'
    if fq=='lepton' and fk=='hadron': return 'LEPTON_READS_HADRON_ROUTE'
    if fq=='hadron' and fk=='hadron': return 'HADRON_HADRON_TOPOLOGY_ROUTE'
    if 'photon' in (fq,fk) and 'hadron' in (fq,fk): return 'PHOTON_HADRON_ROUTE'
    return f'{fq.upper()}_{fk.upper()}_ROUTE'

def has_pad(pair):
    q,k=split_pair(pair)
    return q=='pad' or k=='pad'

def select(rows, key, mode, min_strength=0.70, limit=18):
    out=[]
    for r in rows:
        if has_pad(r['pair_role']): continue
        s=num(r.get(key,0))
        if s >= min_strength:
            out.append((s,r))
    out.sort(key=lambda x:x[0], reverse=True)
    rules=[]
    for s,r in out[:limit]:
        q,k=split_pair(r['pair_role'])
        module=r['module']; head=str(r['head'])
        if mode=='B_to_Tbl':
            cond='B_Hqql_to_Tbl'
            action='route Hqql event toward Tbl-like evidence'
            meaning='route is stronger in Hqql→Tbl mistakes than in correct Hqql'
        elif mode=='A_protect':
            cond='A_Hqql_correct'
            action='preserve Hqql evidence and resist Tbl-like confusion'
            meaning='route is stronger in correct Hqql than in Hqql→Tbl mistakes'
        else:
            cond='B_Hqql_to_Tbl_anomaly'
            action='mark nonstandard transition route'
            meaning='route separates mistake regime from both correct regimes'
        rid=f'R{len(rules)+1:03d}_{mode}'
        rules.append({
            'id':rid,'mode':mode,'module':module,'head':head,'query':q,'key':k,
            'pair':r['pair_role'],'type':route_type(r['pair_role']),
            'A':num(r.get('A',0)),'B':num(r.get('B',0)),'C':num(r.get('C',0)),'D':num(r.get('D',0)),
            'strength':s,'condition':cond,'action':action,'meaning':meaning,
            'pseudocode':f"IF group == {cond} AND HEAD[{module}][{head}] reads {q} <- {k}: {action}",
            'matrix_route':f"ROUTE[{module}, head={head}, {q}<-{k}] := attention_weight * role_gate({q},{k}) * class_regime({cond})"
        })
    return rules

def mdtab(h, rows):
    if not rows: return '_No rows._\n'
    s=['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']
    s += ['| '+' | '.join(str(x) for x in r)+' |' for r in rows]
    return '\n'.join(s)+'\n'

rows=read_csv(SUMMARY)
meta=json.loads(Path(META).read_text()) if Path(META).exists() else {}
trig=select(rows,'trigger_B_minus_A','B_to_Tbl')
prot=select(rows,'loss_A_minus_B','A_protect')
anom=select(rows,'anomaly_B_not_A_not_C','anomaly',0.52,12)
rules=trig+prot+anom

cnt=Counter(r['type'] for r in rules)
mods=Counter(r['module'] for r in rules)

obj={'ok':True,'source_summary':SUMMARY,'source_meta':META,'meta':meta,'rules_n':len(rules),'route_type_counts':dict(cnt),'module_counts':dict(mods),'rules':rules}
Path(OUT_JSON).parent.mkdir(parents=True, exist_ok=True)
Path(OUT_JSON).write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

lines=[]
lines.append('# PART_REAL_CONTRACT_PSEUDOCODE_COMPILER_V1\n')
lines.append('This report compiles real-contract ParT head/layer traces into readable matrix/pseudocode rules. It is not a standard attention plot.\n')
lines.append('## Validity base\n')
lines.append(f"- checkpoint: `{meta.get('checkpoint','unknown')}`")
lines.append(f"- data_config: `{meta.get('data_config','unknown')}`")
lines.append(f"- traced events: **{meta.get('events','unknown')}**")
lines.append(f"- pair rows: **{meta.get('pair_rows','unknown')}**")
lines.append(f"- summary rows: **{meta.get('summary_rows','unknown')}**")
lines.append(f"- compiled rules: **{len(rules)}**")
lines.append("- pad-linked routes: excluded in this compiler v1\n")
lines.append('## Route type counts\n')
lines.append(mdtab(['route_type','count'],cnt.most_common()))
lines.append('## Module concentration\n')
lines.append(mdtab(['module','count'],mods.most_common()))

def section(title, rs):
    lines.append(f'## {title}\n')
    lines.append(mdtab(['rule','module','head','route','type','strength','action'],[[r['id'],r['module'],r['head'],r['pair'],r['type'],round(r['strength'],5),r['action']] for r in rs]))
    for r in rs[:8]:
        lines.append(f"### {r['id']} `{r['module']}#h{r['head']}` `{r['pair']}`\n")
        lines.append('```text')
        lines.append(r['pseudocode'])
        lines.append(r['matrix_route'])
        lines.append('```')
        lines.append(f"- meaning: {r['meaning']}")
        lines.append(f"- A={r['A']:.5f} B={r['B']:.5f} C={r['C']:.5f} D={r['D']:.5f} strength={r['strength']:.5f}\n")

section('Rules where Hqql becomes Tbl-like',trig)
section('Rules where Hqql is protected',prot)
section('Anomaly rules',anom)

lines.append('## What this preserves\n')
lines.append('- head/layer provenance')
lines.append('- role-to-role route')
lines.append('- class-regime difference')
lines.append('- matrix-route form')
lines.append('- pseudocode form')
lines.append('- real-contract source trace\n')
lines.append('## Next validation\n')
lines.append('1. run pad-control report')
lines.append('2. test top rules by head/route drop-control')
lines.append('3. compare against WToQQ and TTBar regimes')
lines.append('4. promote stable rules into operation dictionary\n')

Path(OUT_MD).parent.mkdir(parents=True, exist_ok=True)
Path(OUT_MD).write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'ok':True,'rules':len(rules),'out_md':OUT_MD},indent=2))
