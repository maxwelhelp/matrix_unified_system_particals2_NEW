#!/usr/bin/env python3
import argparse,csv,json,math
from pathlib import Path
from collections import Counter

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
def fnum(x,d=0.0):
    try:
        v=float(x)
        return v if math.isfinite(v) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def numeric_features(rows):
    banned={'event_index'}
    keys=set()
    for r in rows:
        for k,v in r.items():
            if k in banned or k.endswith('_idx') or k in ('group','true_label','pred_label','particle0_pid','leading_pid','best_lepton_pid'):
                continue
            try:
                float(v); keys.add(k)
            except Exception: pass
    return sorted(keys)
def stats(xs,feat):
    vals=[fnum(r.get(feat)) for r in xs if r.get(feat,'')!='']
    if not vals: return {'mean':0,'std':0,'n':0}
    m=sum(vals)/len(vals); var=sum((v-m)**2 for v in vals)/max(1,len(vals)-1)
    return {'mean':m,'std':math.sqrt(var),'n':len(vals)}
def compare(protected,confused,features):
    rows=[]
    for f in features:
        a=stats(protected,f); b=stats(confused,f)
        pooled=math.sqrt((a['std']**2+b['std']**2)/2)+1e-9
        diff=a['mean']-b['mean']
        ratio=(a['mean']+1e-9)/(b['mean']+1e-9) if abs(b['mean'])>1e-9 else 999.0
        direction='protected_higher_veto_candidate' if diff>0 else 'confused_higher_trigger_candidate'
        rows.append({'feature':f,'protected_mean':a['mean'],'confused_mean':b['mean'],'diff_protected_minus_confused':diff,'ratio_protected_over_confused':ratio,'std_effect':diff/pooled,'direction':direction,'protected_n':a['n'],'confused_n':b['n']})
    return sorted(rows,key=lambda r:abs(r['std_effect']),reverse=True)
def pid_modes(xs,key):
    c=Counter(r.get(key,'') for r in xs)
    return ', '.join(f'{k}:{v}' for k,v in c.most_common(8))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--phase1-events',default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv')
    ap.add_argument('--isolation-threshold',type=float,default=0.30)
    ap.add_argument('--out-md',default='reports/latest/VETO_SEARCH_V1.md')
    ap.add_argument('--out-csv',default='reports/latest/tables/veto_search_v1_feature_contrasts.csv')
    ap.add_argument('--out-json',default='manifests/latest/veto_search_v1.json')
    a=ap.parse_args(); rows=readcsv(a.phase1_events)
    high=[r for r in rows if r.get('true_label')=='label_Hqql' and fnum(r.get('particle0_iso_pt_ratio'))>=a.isolation_threshold]
    protected=[r for r in high if r.get('group')=='Hqql_correct']
    confused=[r for r in high if r.get('group')=='Hqql_to_Tbl']
    feats=numeric_features(rows)
    priority=['particle0_knn_charged_hadron_frac','particle0_knn_neutral_hadron_frac','particle0_knn_photon_frac','particle0_knn_electron_frac','particle0_knn_muon_frac','particle0_knn_pt_sum','missing_pt_proxy','best_lepton_iso_pt_ratio','deltaR_p0_lepton','deltaR_lead_lepton','leading_iso_pt_ratio','particle0_pt','leading_pt','has_lepton']
    ordered=[f for f in priority if f in feats]+[f for f in feats if f not in priority]
    contrasts=compare(protected,confused,ordered); wcsv(a.out_csv,contrasts)
    out={'ok':True,'isolation_threshold':a.isolation_threshold,'highiso_hqql_n':len(high),'protected_highiso_n':len(protected),'actual_confused_highiso_n':len(confused),'protected_rate':len(protected)/len(high) if high else 0,'confused_rate':len(confused)/len(high) if high else 0,'top_contrasts':contrasts[:30]}
    wjson(a.out_json,out)
    veto=[r for r in contrasts if r['direction']=='protected_higher_veto_candidate'][:20]
    trig=[r for r in contrasts if r['direction']=='confused_higher_trigger_candidate'][:20]
    md=['# VETO_SEARCH_V1\n\n','Question: what protects high-isolation true Hqql events from false Tbl-readout?\n\n','## Groups\n',mdtab(['group','n','particle0_pid_modes','leading_pid_modes'],[['protected_highiso = Hqql_correct iso>=thr',len(protected),pid_modes(protected,'particle0_pid'),pid_modes(protected,'leading_pid')],['actual_confused_highiso = Hqql_to_Tbl iso>=thr',len(confused),pid_modes(confused,'particle0_pid'),pid_modes(confused,'leading_pid')]]),'\n## Top protected-higher candidates (possible veto features)\n',mdtab(['feature','protected_mean','confused_mean','diff','ratio','std_effect'],[[r['feature'],fmt(r['protected_mean']),fmt(r['confused_mean']),fmt(r['diff_protected_minus_confused']),fmt(r['ratio_protected_over_confused']),fmt(r['std_effect'])] for r in veto[:15]]),'\n## Top confused-higher candidates (possible Tbl trigger features)\n',mdtab(['feature','protected_mean','confused_mean','diff','ratio','std_effect'],[[r['feature'],fmt(r['protected_mean']),fmt(r['confused_mean']),fmt(r['diff_protected_minus_confused']),fmt(r['ratio_protected_over_confused']),fmt(r['std_effect'])] for r in trig[:15]]),'\n## Interpretation\n\nProtected-higher features are candidate veto mechanisms: they may prevent a high-isolation Hqql event from becoming Tbl-like. Confused-higher features are candidate trigger mechanisms for false Tbl-readout. V1 uses Phase 1 CSV features only; if a candidate appears, V2 should recompute full KNN geometry such as max neighbor pT, pairwise deltaR spread, and hard charged neighbor counts.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'protected':len(protected),'confused':len(confused),'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
