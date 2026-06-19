#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path
from collections import defaultdict
import numpy as np
import uproot

LABELS = ['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
REQ = ['part_px','part_py','part_pz','part_energy','part_deta','part_dphi','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','jet_pt','jet_energy'] + LABELS
MAP = [('HToBB','label_Hbb'),('HToCC','label_Hcc'),('HToGG','label_Hgg'),('HToWW2Q1L','label_Hqql'),('HToWW4Q','label_H4q'),('TTBarLep','label_Tbl'),('TTBar','label_Tbqq'),('WToQQ','label_Wqq'),('ZToQQ','label_Zqq'),('ZJetsToNuNu','label_QCD')]

def expected(path):
    s=str(path)
    for key, lab in MAP:
        if key in s:
            return lab
    return ''

def tree_of(path):
    f=uproot.open(path)
    if 'tree' in f:
        return f['tree']
    return f[f.keys()[0]]

def wcsv(p, rows):
    p=Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with p.open('w', newline='', encoding='utf-8') as f:
        wr=csv.DictWriter(f, fieldnames=keys); wr.writeheader(); wr.writerows(rows)

def mdtab(h, rows):
    if not rows: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rows])+'\n'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--max-files', type=int, default=200)
    ap.add_argument('--entry-stop', type=int, default=2000)
    ap.add_argument('--out-md', default='reports/latest/PART_DATASET_CONTRACT_AUDIT_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_dataset_contract_audit_v1_files.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_dataset_contract_audit_v1.json')
    a=ap.parse_args()
    rows=[]; sums=defaultdict(float); miss=defaultdict(int)
    for path in sorted(Path(a.data_dir).rglob('*.root'))[:a.max_files]:
        row={'file':str(path),'expected':expected(path)}
        try:
            t=tree_of(path); keys=set(t.keys()); row['entries']=int(t.num_entries)
            missing=[x for x in REQ if x not in keys]
            row['missing']=';'.join(missing); row['missing_count']=len(missing)
            for m in missing: miss[m]+=1
            if all(x in keys for x in LABELS):
                arr=t.arrays(LABELS, library='np', entry_stop=a.entry_stop)
                M=np.stack([arr[x] for x in LABELS], axis=1)
                lab_sums=M.sum(axis=0); onehot=(M.sum(axis=1)==1)
                for lab,val in zip(LABELS, lab_sums): sums[lab]+=float(val)
                dom=LABELS[int(np.argmax(lab_sums))]
                row['dominant']=dom; row['onehot_rate']=float(onehot.mean()) if len(onehot) else 0.0
                row['name_matches_label']=int((not row['expected']) or row['expected']==dom)
            else:
                row['dominant']='NO_LABELS'; row['onehot_rate']=0.0; row['name_matches_label']=0
        except Exception as e:
            row['error']=repr(e)[:300]
        rows.append(row)
    bad=[r for r in rows if r.get('error') or int(r.get('missing_count') or 0)>0 or float(r.get('onehot_rate') or 0)<0.999 or (r.get('expected') and int(r.get('name_matches_label') or 0)==0)]
    out={'ok':True,'files_checked':len(rows),'bad_files':len(bad),'label_sums_sampled':dict(sums),'missing_counts':dict(miss)}
    Path(a.out_json).parent.mkdir(parents=True, exist_ok=True); Path(a.out_json).write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
    wcsv(a.out_csv, rows)
    md='# PART_DATASET_CONTRACT_AUDIT_V1\n\n'
    md+=f'- files_checked: **{len(rows)}**\n- bad_files: **{len(bad)}**\n\n'
    md+='## Label sums sampled\n'+mdtab(['label','sum'], [[k,int(v)] for k,v in sums.items()])
    md+='\n## Missing branches\n'+mdtab(['branch','files'], [[k,v] for k,v in sorted(miss.items())])
    md+='\n## Suspicious files\n'+mdtab(['file','expected','dominant','onehot','missing','error'], [[r.get('file'),r.get('expected'),r.get('dominant'),r.get('onehot_rate'),r.get('missing'),r.get('error','')] for r in bad[:80]])
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True); Path(a.out_md).write_text(md,encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
