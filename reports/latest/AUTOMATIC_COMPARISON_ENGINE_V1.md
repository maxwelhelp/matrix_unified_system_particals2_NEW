# Automatic Comparison Engine v1

This report automates the specific comparisons the human analyst currently performs manually.

## Comparison rows
| priority | status | comparison | claim | support | missing_control | next |
| --- | --- | --- | --- | --- | --- | --- |
| P0 | CANDIDATE_STRONG_MISSING_CONTROL | C1_STREAM_RELATION_VS_MISSING_CONTROL | particle0/core_high_pt relation supports AH1 core-anchor hypothesis | relation_signal=0.9474324892454034 support=151 | particle0/top-k/random controls | run particle0 removal / keep-only particle0 / top-k removal / same-count random controls |
| P0 | NEEDS_CLASS_SPECIFIC_TEST | C5_CLASS_SIGNATURE_VS_CLASS_SPECIFIC_GRADIENT | Hqql/Tbl signature is strong in stream but global gradients are not class-specific | watcher_score=0.9625 state=HIGH | class-specific all-head gradients | run class-specific all-head gradients for Hqql/Tbl/Tbqq/Wqq/Zqq |
| P0 | NEEDS_ROUTE_TRACE | C2_WIDE_PATTERN_VS_ROUTE_TRACE | wide particle pattern may be secondary context rather than noise | relation_signal=0.7525254963492034 support=20 dst=hypothesis:T6_WIDE_SECONDARY_CONTEXT | route-neighbor trace / causal route controls | run route-neighbor trace for top all-head particles and wide non-particle0 particles |
| P1 | NEEDS_CLASS_SPECIFIC_TEST | C3_PATCH_VS_GRADIENT_DIVERGENCE | some heads are jointly supportive by gradient but not individually important by patch | divergent_heads=12 top=[{'head_id': 'L1_ch112:128', 'gate_abs_grad': 0.8689268512214768, 'patch_acc_drop': 0.0, 'role': 'middle learned-neighborhood / route-composition head'}, {'head_id': 'L1_ch16:32', 'gate_abs_grad': 0.748019616522652, 'patch_acc_drop': 0.0, 'role': 'middle learned-neighborhood / route-composition head'}, {'head_id': 'L0_ch40:48', 'gate_abs_grad': 0.715566657370073, 'patch_acc_drop': 0.0, 'role': 'early feature/geometry/PID reader'}] | multi-head patch combinations / patch-rank-vs-gate-rank table | build patch-rank vs gate-rank report and run multi-head patch combinations |
| P1 | NEEDS_CLASS_SPECIFIC_TEST | C6_NEGATIVE_GATES_VS_SUPPRESSIVE_ROLE | negative gate gradients may indicate suppressive heads | watcher_score=1.0 state=HIGH | class-specific negative gradients / suppressive patch analysis | add suppressive-head analysis and compare patch effects |
| P1 | NEEDS_HELDOUT | C4_HEAD_RANK_STABILITY_VS_RUN_CHANGES | top all-head gates may be stable mechanism candidates | stability_score=0.9455 top_heads=['L1_ch112:128', 'L0_ch40:48', 'L2_ch224:256', 'L1_ch16:32', 'L0_ch48:56'] | more distinct snapshots / heldout files / controls | run heldout subsets and controls with HISTORY_COPY=1, then compare head ranks |

## Main interpretation

- Strong particle0/core signals are not enough. They must be compared against missing particle0/top-k controls.
- Wide secondary signals are useful only after route-neighbor trace.
- Head gradient and patch evidence must be compared, not merged blindly.
- Hqql/Tbl stream dominance requires class-specific gradients.

## Files

- JSON: `manifests/latest/automatic_comparison_engine_v1.json`
- CSV: `reports/latest/tables/automatic_comparison_rows.csv`
- Training rows: `reports/latest/tables/automatic_comparison_training_dataset.jsonl`
