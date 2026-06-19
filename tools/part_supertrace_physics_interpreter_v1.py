#!/usr/bin/env python3
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

LEPTONS = {'electron', 'muon'}
HADRONS = {'charged_hadron', 'neutral_hadron'}
EM = {'photon'}


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def fnum(x):
    try:
        return float(x)
    except Exception:
        return 0.0


def split_pair(pair):
    if '<-' not in pair:
        return pair, ''
    a, b = pair.split('<-', 1)
    return a, b


def role_family(role):
    if role in LEPTONS:
        return 'lepton'
    if role in HADRONS:
        return 'hadron'
    if role in EM:
        return 'photon'
    if role == 'CLS':
        return 'CLS'
    if role == 'pad':
        return 'pad'
    return 'other'


def path_tag(pair):
    q, k = split_pair(pair)
    fq, fk = role_family(q), role_family(k)
    if 'pad' in (fq, fk):
        return 'pad_artifact_or_sparse_particle_pattern'
    if fq == 'lepton' and fk == 'lepton':
        return 'lepton_lepton_correlation'
    if fq == 'lepton' and fk == 'hadron':
        return 'lepton_reads_hadron'
    if fq == 'hadron' and fk == 'lepton':
        return 'hadron_reads_lepton'
    if 'photon' in (fq, fk) and 'lepton' in (fq, fk):
        return 'lepton_photon_correlation'
    if fq == 'hadron' and fk == 'hadron':
        return 'hadron_hadron_topology'
    if 'photon' in (fq, fk) and 'hadron' in (fq, fk):
        return 'photon_hadron_topology'
    return f'{fq}_{fk}'


def top(rows, key, n=20, reverse=True):
    return sorted(rows, key=lambda r: fnum(r.get(key, 0)), reverse=reverse)[:n]


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    out = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for r in rows:
        out.append('| ' + ' | '.join(str(x) for x in r) + ' |')
    return '\n'.join(out) + '\n'


def summarize_set(rows):
    tags = Counter(path_tag(r['pair_role']) for r in rows)
    modules = Counter(r['module'] for r in rows)
    heads = Counter(f"{r['module']}#h{r['head']}" for r in rows)
    roles = Counter()
    for r in rows:
        q, k = split_pair(r['pair_role'])
        roles[q] += 1
        roles[k] += 1
    return tags, modules, heads, roles


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--summary', default='reports/latest/tables/part_attention_path_summary_real_contract_v1.csv')
    ap.add_argument('--manifest-json', default='manifests/latest/part_attention_supertrace_real_contract_v1.json')
    ap.add_argument('--out-md', default='reports/latest/PART_SUPERTRACE_PHYSICS_INTERPRETER_V1.md')
    ap.add_argument('--out-json', default='manifests/latest/part_supertrace_physics_interpreter_v1.json')
    ap.add_argument('--topn', type=int, default=25)
    a = ap.parse_args()

    rows = read_csv(a.summary)
    for r in rows:
        r['tag'] = path_tag(r['pair_role'])

    trigger = top(rows, 'trigger_B_minus_A', a.topn)
    loss = top(rows, 'loss_A_minus_B', a.topn)
    anomaly = top(rows, 'anomaly_B_not_A_not_C', a.topn)

    trig_tags, trig_mods, trig_heads, trig_roles = summarize_set(trigger)
    loss_tags, loss_mods, loss_heads, loss_roles = summarize_set(loss)
    anom_tags, anom_mods, anom_heads, anom_roles = summarize_set(anomaly)

    manifest = {}
    p = Path(a.manifest_json)
    if p.exists():
        manifest = json.loads(p.read_text(encoding='utf-8'))

    hypothesis = []
    if trig_tags.get('lepton_lepton_correlation', 0) + trig_tags.get('lepton_photon_correlation', 0) + trig_tags.get('lepton_reads_hadron', 0) + trig_tags.get('hadron_reads_lepton', 0) >= 5:
        hypothesis.append('B_Hqql_to_Tbl trigger is dominated by lepton-linked attention paths. The Hqql→Tbl confusion likely appears when the ParT representation routes semileptonic H→WW evidence into a top-leptonic-like lepton topology.')
    if loss_tags.get('lepton_lepton_correlation', 0) >= 3:
        hypothesis.append('A_Hqql_correct protection also uses lepton-lepton paths, but in different heads/layers. This suggests the same particle roles are used with different routing semantics, not simply presence/absence of leptons.')
    if trig_tags.get('pad_artifact_or_sparse_particle_pattern', 0) >= 2 or loss_tags.get('pad_artifact_or_sparse_particle_pattern', 0) >= 2:
        hypothesis.append('Several top paths include pad. Treat pad-linked paths as a detector/sparsity or masking signal until verified by controls; they may still be meaningful because particle multiplicity is physical, but they require a mask-control test.')
    if trig_mods:
        hypothesis.append('The highest trigger concentration is in late ParT blocks: ' + ', '.join([f'{m}({c})' for m, c in trig_mods.most_common(4)]) + '.')
    if loss_mods:
        hypothesis.append('The highest Hqql-correct protection concentration is in: ' + ', '.join([f'{m}({c})' for m, c in loss_mods.most_common(4)]) + '.')

    out = {
        'ok': True,
        'n_summary_rows': len(rows),
        'source_manifest': manifest,
        'trigger_tag_counts': dict(trig_tags),
        'loss_tag_counts': dict(loss_tags),
        'anomaly_tag_counts': dict(anom_tags),
        'hypothesis': hypothesis,
    }
    Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_json).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')

    lines = []
    lines.append('# PART_SUPERTRACE_PHYSICS_INTERPRETER_V1')
    lines.append('')
    lines.append('Automatic interpretation of the real-contract ParT Hqql/Tbl attention supertrace.')
    lines.append('')
    lines.append(f'- summary rows: **{len(rows)}**')
    lines.append(f'- traced events: **{manifest.get("events", "unknown")}**')
    lines.append(f'- pair rows: **{manifest.get("pair_rows", "unknown")}**')
    lines.append(f'- data_config: `{manifest.get("data_config", "unknown")}`')
    lines.append(f'- checkpoint: `{manifest.get("checkpoint", "unknown")}`')
    lines.append('')
    lines.append('## Main hypothesis')
    lines.append('')
    for h in hypothesis:
        lines.append(f'- {h}')
    if not hypothesis:
        lines.append('- No strong automatic hypothesis found. Inspect top path tables manually.')
    lines.append('')

    lines.append('## Trigger B>A tag counts')
    lines.append(mdtab(['tag', 'count'], trig_tags.most_common()))
    lines.append('## Hqql-correct A>B tag counts')
    lines.append(mdtab(['tag', 'count'], loss_tags.most_common()))
    lines.append('## Anomaly tag counts')
    lines.append(mdtab(['tag', 'count'], anom_tags.most_common()))

    lines.append('## Top trigger paths: B_Hqql_to_Tbl stronger than A_Hqql_correct')
    lines.append(mdtab(['module','head','pair_role','tag','A','B','C','B-A'], [[r['module'], r['head'], r['pair_role'], r['tag'], round(fnum(r['A']),5), round(fnum(r['B']),5), round(fnum(r['C']),5), round(fnum(r['trigger_B_minus_A']),5)] for r in trigger[:20]]))

    lines.append('## Top protection/loss paths: A_Hqql_correct stronger than B_Hqql_to_Tbl')
    lines.append(mdtab(['module','head','pair_role','tag','A','B','C','A-B'], [[r['module'], r['head'], r['pair_role'], r['tag'], round(fnum(r['A']),5), round(fnum(r['B']),5), round(fnum(r['C']),5), round(fnum(r['loss_A_minus_B']),5)] for r in loss[:20]]))

    lines.append('## Top anomaly paths')
    lines.append(mdtab(['module','head','pair_role','tag','A','B','C','score'], [[r['module'], r['head'], r['pair_role'], r['tag'], round(fnum(r['A']),5), round(fnum(r['B']),5), round(fnum(r['C']),5), round(fnum(r['anomaly_B_not_A_not_C']),5)] for r in anomaly[:20]]))

    lines.append('## Next tests')
    lines.append('')
    lines.append('1. Mask-control test for pad-linked paths.')
    lines.append('2. Lepton-ablation patch on top trigger heads.')
    lines.append('3. Compare Hqql/Tbl against WToQQ and TTBar to separate generic lepton routing from top-specific routing.')
    lines.append('4. Promote stable top heads into pseudocode rules.')
    lines.append('')
    lines.append('## Validity')
    lines.append('')
    lines.append('This report reads `part_attention_path_summary_real_contract_v1.csv`, which came from real `DataConfig.load(...)` and strict checkpoint loading.')

    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_md).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'ok': True, 'out_md': a.out_md, 'hypothesis_n': len(hypothesis)}, indent=2))


if __name__ == '__main__':
    main()
