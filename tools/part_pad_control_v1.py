#!/usr/bin/env python3
import argparse, csv, json
from collections import Counter
from pathlib import Path


def rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def fnum(x):
    try:
        return float(x)
    except Exception:
        return 0.0


def has_pad(pair):
    return pair.startswith('pad<-') or pair.endswith('<-pad') or '<-pad' in pair or 'pad<-' in pair


def tag(pair):
    left, right = pair.split('<-', 1) if '<-' in pair else (pair, '')
    leps = {'electron', 'muon'}
    hads = {'charged_hadron', 'neutral_hadron'}
    if has_pad(pair): return 'pad'
    if left in leps and right in leps: return 'lepton_lepton'
    if left in leps and right == 'photon' or right in leps and left == 'photon': return 'lepton_photon'
    if left in hads and right in leps: return 'hadron_reads_lepton'
    if left in leps and right in hads: return 'lepton_reads_hadron'
    if left in hads and right in hads: return 'hadron_hadron'
    if left == 'photon' or right == 'photon': return 'photon_other'
    return 'other'


def top(rs, key, n=20):
    return sorted(rs, key=lambda r: fnum(r.get(key, 0)), reverse=True)[:n]


def mdtab(h, rs):
    if not rs: return '_No rows._\n'
    out = ['| ' + ' | '.join(h) + ' |', '| ' + ' | '.join(['---']*len(h)) + ' |']
    out += ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rs]
    return '\n'.join(out) + '\n'


def summarize(rs):
    return Counter(tag(r['pair_role']) for r in rs)


def fmt_path(r, key):
    return [r['module'], r['head'], r['pair_role'], tag(r['pair_role']), round(fnum(r['A']),5), round(fnum(r['B']),5), round(fnum(r['C']),5), round(fnum(r[key]),5)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--summary', default='reports/latest/tables/part_attention_path_summary_real_contract_v1.csv')
    ap.add_argument('--out-md', default='reports/latest/PART_PAD_CONTROL_V1.md')
    ap.add_argument('--out-json', default='manifests/latest/part_pad_control_v1.json')
    a = ap.parse_args()
    rs = rows(a.summary)
    pad = [r for r in rs if has_pad(r['pair_role'])]
    nonpad = [r for r in rs if not has_pad(r['pair_role'])]
    trigger_all = top(rs, 'trigger_B_minus_A', 25)
    trigger_np = top(nonpad, 'trigger_B_minus_A', 25)
    loss_np = top(nonpad, 'loss_A_minus_B', 25)
    anomaly_np = top(nonpad, 'anomaly_B_not_A_not_C', 25)
    trig_all_tags = summarize(trigger_all)
    trig_np_tags = summarize(trigger_np)
    conclusion = []
    if trig_np_tags.get('lepton_lepton',0) + trig_np_tags.get('lepton_photon',0) + trig_np_tags.get('hadron_reads_lepton',0) + trig_np_tags.get('lepton_reads_hadron',0) >= 10:
        conclusion.append('PASS: after removing pad-linked paths, the Hqql->Tbl trigger remains lepton-dominated.')
    else:
        conclusion.append('WEAK: after removing pad-linked paths, lepton dominance is not strong enough; inspect manually.')
    if len(trigger_all) and sum(1 for r in trigger_all if has_pad(r['pair_role'])) <= 5:
        conclusion.append('Pad paths are present but not dominant in top trigger paths.')
    else:
        conclusion.append('Pad paths are numerous in top trigger paths; run a stronger mask-control later.')
    obj = {
        'ok': True,
        'summary_rows': len(rs),
        'pad_rows': len(pad),
        'nonpad_rows': len(nonpad),
        'top_trigger_all_tags': dict(trig_all_tags),
        'top_trigger_nonpad_tags': dict(trig_np_tags),
        'conclusion': conclusion,
    }
    Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_json).write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')
    lines = []
    lines.append('# PART_PAD_CONTROL_V1')
    lines.append('')
    lines.append('Pad-control check for real-contract ParT Hqql/Tbl supertrace. This removes all paths where query or key role is `pad`, then re-ranks the strongest trigger/protection/anomaly paths.')
    lines.append('')
    lines.append(f'- summary rows: **{len(rs)}**')
    lines.append(f'- pad-linked rows: **{len(pad)}**')
    lines.append(f'- non-pad rows: **{len(nonpad)}**')
    lines.append('')
    lines.append('## Conclusion')
    lines.append('')
    for c in conclusion: lines.append(f'- {c}')
    lines.append('')
    lines.append('## Top trigger tag counts before pad removal')
    lines.append(mdtab(['tag','count'], trig_all_tags.most_common()))
    lines.append('## Top trigger tag counts after pad removal')
    lines.append(mdtab(['tag','count'], trig_np_tags.most_common()))
    lines.append('## Top non-pad B>A trigger paths')
    lines.append(mdtab(['module','head','pair_role','tag','A','B','C','B-A'], [fmt_path(r, 'trigger_B_minus_A') for r in trigger_np[:20]]))
    lines.append('## Top non-pad A>B protection paths')
    lines.append(mdtab(['module','head','pair_role','tag','A','B','C','A-B'], [fmt_path(r, 'loss_A_minus_B') for r in loss_np[:20]]))
    lines.append('## Top non-pad anomaly paths')
    lines.append(mdtab(['module','head','pair_role','tag','A','B','C','score'], [fmt_path(r, 'anomaly_B_not_A_not_C') for r in anomaly_np[:20]]))
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_md).write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(json.dumps({'ok': True, 'out_md': a.out_md, 'conclusion': conclusion}, indent=2))

if __name__ == '__main__':
    main()
