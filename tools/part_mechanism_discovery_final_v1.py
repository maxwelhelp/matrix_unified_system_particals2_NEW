#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path
from collections import Counter, defaultdict


def fnum(x, default=0.0):
    try:
        if x is None or x == '':
            return default
        return float(x)
    except Exception:
        return default


def fmt(x):
    try:
        x = float(x)
    except Exception:
        return 'n/a'
    if abs(x) > 0 and (abs(x) < 1e-3 or abs(x) > 1e4):
        return f'{x:.3e}'
    return f'{x:.4f}'


def read_csv(path):
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def write_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    lines = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for r in rows:
        lines.append('| ' + ' | '.join(str(x) for x in r) + ' |')
    return '\n'.join(lines) + '\n'


def top(rows, key, n=10, reverse=True):
    return sorted(rows, key=lambda r: fnum(r.get(key)), reverse=reverse)[:n]


def load_json(path):
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return {}


def mechanism_summary(validation_rows):
    strong = []
    for r in validation_rows:
        b_delta = fnum(r.get('best_B_delta_margin'))
        b_flip = fnum(r.get('best_B_delta_tbl_pred'))
        score = fnum(r.get('score'))
        if int(float(r.get('direction_ok_runs') or 0)) > 0 and (abs(b_delta) > 0.05 or abs(b_flip) > 0.0 or score > 0.05):
            strong.append(r)
    return strong


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--discovery-csv', default='reports/latest/tables/part_discovery_candidates_real_contract_v1.csv')
    ap.add_argument('--validation-csv', default='reports/latest/tables/part_candidate_pair_validation_balanced_v1_summary.csv')
    ap.add_argument('--nat-csv', default='reports/latest/tables/part_natural_attention_manual_grad_real_contract_v1_summary.csv')
    ap.add_argument('--write-csv', default='reports/latest/tables/part_value_write_grad_real_contract_v1_summary.csv')
    ap.add_argument('--allhead-json', default='manifests/latest/part_full_all_head_supertrace_real_contract_v1.json')
    ap.add_argument('--matrix-json', default='manifests/latest/part_matrix_program_full_trace_real_contract_v1.json')
    ap.add_argument('--out-md', default='reports/latest/PART_MECHANISM_DISCOVERY_FINAL_V1.md')
    ap.add_argument('--out-json', default='manifests/latest/part_mechanism_discovery_final_v1.json')
    args = ap.parse_args()

    discovery = read_csv(args.discovery_csv)
    validation = read_csv(args.validation_csv)
    nat = read_csv(args.nat_csv)
    write = read_csv(args.write_csv)
    allhead = load_json(args.allhead_json)
    matrix = load_json(args.matrix_json)

    validated = mechanism_summary(validation)
    diagnosis_counts = Counter(r.get('diagnosis', '') for r in discovery)
    val_diag_counts = Counter(r.get('diagnosis', '') for r in validation)

    protective = [r for r in validated if r.get('diagnosis') == 'B_Tbl_resist_or_protective_read_write']
    push = [r for r in validated if r.get('diagnosis') == 'B_Tbl_push_read_write']
    causal = [r for r in validated if r.get('diagnosis') == 'causal_candidate']
    high_grad = [r for r in validated if r.get('diagnosis') == 'high_gradient_write_node']

    md = []
    md.append('# PART_MECHANISM_DISCOVERY_FINAL_V1\n\n')
    md.append('Final frozen mechanism-discovery report for current ParT Hqql/Tbl interpretation pass. This report summarizes the matrix decoder formula, validated mechanisms, evidence chain, and remaining work needed for full-model interpretation.\n\n')

    md.append('## Status\n\n')
    md.append('- **Current claim:** model is not fully decompiled end-to-end, but the Hqql/Tbl decision region now has validated matrix-program mechanisms.\n')
    md.append('- **Validated scope:** read routes, value/write contribution, head-level gradients, pair-level interventions, and Hqql/Tbl margin/flips.\n')
    md.append('- **Not yet full-model scope:** all residual paths, all MLP/classifier terms, every head/pair over all classes, and cross-layer path composition.\n\n')

    md.append('## Matrix decoder formula\n\n')
    md.append('For one attention head `h`:\n\n')
    md.append('```text\n')
    md.append('Q_h = X W_Q^h\n')
    md.append('K_h = X W_K^h\n')
    md.append('V_h = X W_V^h\n')
    md.append('S_h = Q_h K_h^T / sqrt(d) + mask\n')
    md.append('A_h = softmax(S_h)\n')
    md.append('C_h = A_h V_h\n')
    md.append('Y_h = C_h W_O^h\n')
    md.append('J = logit_Tbl - logit_Hqql  (or signed per group)\n')
    md.append('READ(h, q<-k)  = mean_{q in role_q, k in role_k} A_h[q,k] * dJ/dA_h[q,k]\n')
    md.append('WRITE(h, q<-k) = mean_{q in role_q, k in role_k} A_h[q,k] * dot(V_h[k], dJ/dC_h[q])\n')
    md.append('PATCH(h, q<-k) = S_h[q,k] += beta; measure Δ(logit_Tbl-logit_Hqql), ΔTbl_pred_rate\n')
    md.append('```\n\n')

    md.append('## Evidence pipeline\n\n')
    md.append('```text\n')
    md.append('real replay groups\n')
    md.append('→ all-head differentiable supertrace\n')
    md.append('→ natural attention A×grad\n')
    md.append('→ value/write A*dot(V,grad_C)\n')
    md.append('→ discovery candidates\n')
    md.append('→ exact head+role-pair causal validation\n')
    md.append('→ final mechanism report\n')
    md.append('```\n\n')

    md.append('## Input report sizes / counts\n\n')
    md.append(mdtab(['source','count/status'], [
        ['discovery_candidates', len(discovery)],
        ['balanced_validation_rows', len(validation)],
        ['validated_strong_rows', len(validated)],
        ['natural_attention_rows', len(nat)],
        ['value_write_rows', len(write)],
        ['allhead_events', allhead.get('events','n/a')],
        ['matrix_heads', matrix.get('heads','n/a')],
    ]))
    md.append('\n')

    md.append('## Diagnosis counts\n\n')
    md.append(mdtab(['diagnosis','discovery_count','validation_count'], [[k, diagnosis_counts.get(k,0), val_diag_counts.get(k,0)] for k in sorted(set(diagnosis_counts)|set(val_diag_counts))]))
    md.append('\n')

    md.append('## Mechanism 1: CLS h4 lepton self-route protective mechanism\n\n')
    md.append('Interpretation: `mod.cls_blocks.0.attn.h4` reads lepton self/CLS-lepton routes and writes a protective signal that suppresses erroneous Tbl-like margin in Hqql→Tbl cases.\n\n')
    md.append(mdtab(['rank','head','pair','action','B_delta','B_flip','A_damage','C_damage','B_write','Agrad','score'], [[i+1, r.get('head_id'), r.get('pair_role'), r.get('action'), fmt(r.get('best_B_delta_margin')), fmt(r.get('best_B_delta_tbl_pred')), fmt(r.get('A_damage_abs')), fmt(r.get('C_damage_abs')), fmt(r.get('B_write')), fmt(r.get('B_AxGrad')), fmt(r.get('score'))] for i,r in enumerate(protective[:8])]))
    md.append('\nPseudocode:\n\n')
    md.append('```text\n')
    md.append('HEAD mod.cls_blocks.0.attn.h4\n')
    md.append('IF CLS/electron/muon self-evidence is strong\n')
    md.append('THEN write anti-Tbl / Hqql-protective evidence into the decision stream\n')
    md.append('EVIDENCE: boosting these routes drives B_Hqql_to_Tbl margin downward and causes Tbl prediction-rate drops.\n')
    md.append('```\n\n')

    md.append('## Mechanism 2: CLS h4 photon/hadron Tbl-push mechanism\n\n')
    md.append('Interpretation: a smaller set of `mod.cls_blocks.0.attn.h4` photon/hadron routes pushes B examples toward Tbl-like margin.\n\n')
    md.append(mdtab(['rank','head','pair','action','B_delta','B_flip','A_damage','C_damage','B_write','Agrad','score'], [[i+1, r.get('head_id'), r.get('pair_role'), r.get('action'), fmt(r.get('best_B_delta_margin')), fmt(r.get('best_B_delta_tbl_pred')), fmt(r.get('A_damage_abs')), fmt(r.get('C_damage_abs')), fmt(r.get('B_write')), fmt(r.get('B_AxGrad')), fmt(r.get('score'))] for i,r in enumerate(push[:8])]))
    md.append('\nPseudocode:\n\n')
    md.append('```text\n')
    md.append('HEAD mod.cls_blocks.0.attn.h4\n')
    md.append('IF photon reads charged/neutral hadron context\n')
    md.append('THEN increase Tbl-like evidence\n')
    md.append('EVIDENCE: boosting push routes increases B Tbl-Hqql margin; suppressing can reduce margin/flips.\n')
    md.append('```\n\n')

    md.append('## Mechanism 3: blocks.7 h3 charged-hadron/lepton causal route\n\n')
    md.append('Interpretation: `mod.blocks.7.attn.h3` is a weaker but rule-supported particle-block route. It links charged-hadron/lepton relations before CLS aggregation.\n\n')
    md.append(mdtab(['rank','head','pair','action','B_delta','B_flip','A_damage','C_damage','B_write','Agrad','rules','score'], [[i+1, r.get('head_id'), r.get('pair_role'), r.get('action'), fmt(r.get('best_B_delta_margin')), fmt(r.get('best_B_delta_tbl_pred')), fmt(r.get('A_damage_abs')), fmt(r.get('C_damage_abs')), fmt(r.get('B_write')), fmt(r.get('B_AxGrad')), r.get('rules'), fmt(r.get('score'))] for i,r in enumerate(causal[:8])]))
    md.append('\nPseudocode:\n\n')
    md.append('```text\n')
    md.append('HEAD mod.blocks.7.attn.h3\n')
    md.append('IF charged_hadron attends to electron/muon route\n')
    md.append('THEN modify later Hqql/Tbl decision evidence\n')
    md.append('EVIDENCE: exact pair patch changes B margin in predicted direction; route has compiled rule support.\n')
    md.append('```\n\n')

    if high_grad:
        md.append('## Additional high-gradient validated nodes\n\n')
        md.append(mdtab(['rank','head','pair','action','B_delta','B_flip','B_write','Agrad','score'], [[i+1, r.get('head_id'), r.get('pair_role'), r.get('action'), fmt(r.get('best_B_delta_margin')), fmt(r.get('best_B_delta_tbl_pred')), fmt(r.get('B_write')), fmt(r.get('B_AxGrad')), fmt(r.get('score'))] for i,r in enumerate(high_grad[:8])]))
        md.append('\n')

    md.append('## What is already interpretable\n\n')
    md.append('- The Hqql/Tbl region has validated read/write mechanisms, not just saliency.\n')
    md.append('- For selected heads/pairs we know real attention route (`A×grad`), value/write direction (`A*dot(V,grad_C)`), causal direction, margin change, and prediction-flip change.\n')
    md.append('- The strongest currently validated node is `mod.cls_blocks.0.attn.h4`, especially lepton self/CLS-lepton routes.\n\n')

    md.append('## What remains for full-model interpretation\n\n')
    md.append('1. **All heads/all pairs sweep:** run balanced validation over every high-score pair, not only top 12 short mode.\n')
    md.append('2. **Residual path composition:** connect particle-block outputs → CLS blocks → classifier logits with per-layer residual contribution.\n')
    md.append('3. **MLP/classifier decoder:** decompose final classifier and any FFN/MLP residual terms into class directions.\n')
    md.append('4. **Cross-class expansion:** repeat beyond Hqql/Tbl for all JetClass class pairs.\n')
    md.append('5. **Stability:** rerun candidates at 128/256/512 events and multiple strengths; keep only stable mechanisms.\n')
    md.append('6. **Program compiler:** emit one machine-readable pseudocode graph: nodes=head/pair/write, edges=residual/CLS/classifier, weights=validated causal effects.\n\n')

    md.append('## Final claim\n\n')
    md.append('```text\n')
    md.append('Current project state:\n')
    md.append('  Not a full end-to-end decompiler of the whole ParT model yet.\n')
    md.append('  But it is a working matrix-program mechanism decoder for Hqql/Tbl.\n')
    md.append('  It has validated read→write→margin→causal-patch mechanisms.\n')
    md.append('Next goal:\n')
    md.append('  Extend from validated Hqql/Tbl mechanisms to full-model program graph.\n')
    md.append('```\n')

    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')

    out = {
        'ok': True,
        'discovery_candidates': len(discovery),
        'validation_rows': len(validation),
        'validated_strong_rows': len(validated),
        'diagnosis_counts': dict(diagnosis_counts),
        'validation_diagnosis_counts': dict(val_diag_counts),
        'top_protective': protective[:8],
        'top_push': push[:8],
        'top_causal': causal[:8],
        'out_md': args.out_md,
    }
    write_json(args.out_json, out)
    print(json.dumps({'ok': True, 'out_md': args.out_md, 'validated_strong_rows': len(validated)}, indent=2))


if __name__ == '__main__':
    main()
