# Scope Comparability Guard v1

This report prevents a methodology bug: comparing a one-batch/local control delta as if it were a whole-stream trend.

- Status: **PASS_WITH_WARNINGS**
- Stream events: **6795**
- Stream snapshots: **15**
- Control-run events: **2560**
- Embedding rows: **6928**

## Checks
| status | severity | check | allowed | forbidden |
| --- | --- | --- | --- | --- |
| PASS | HIGH | control_is_local_not_global_stream_delta | remove_particle0 vs baseline/random_remove1 inside same control run | treat remove_particle0 acc_drop as a stream-history delta |
| PASS | MEDIUM | stream_history_available | head rank stability / stream signal stability | causal claim from stream relation alone |
| WARN | HIGH | comparison_bridge_status | stream suggested particle0; local control supports causality; still needs order/residual | claim discovery or global stream-wide causality without remaining controls |
| WARN | HIGH | embedding_pool_is_mixed | train with source/scope splits and flags | train one model treating all embedding rows as homogeneous facts |
| WARN | HIGH | remaining_required_controls | next tests: order control, residual, class gradients, heldout | physics discovery claim |

## Scope manifest
| artifact | scope | directly comparable to | not directly comparable to | rule |
| --- | --- | --- | --- | --- |
| research_stream_events.jsonl | history_stream | other stream snapshots with same schema | local control deltas | use for trends/stability, not local causal deltas |
| research_stream_index_v1.json | latest_stream_summary | latest relation/task summaries | control-run baseline unless linked as evidence type | use as current dashboard |
| particle0_topk_controls_v2.json | control_run_local | baseline/random controls inside same run | global stream history numeric deltas | use for causal control evidence only inside run |
| relation_signal_edges.csv | latest_relation_meta | latest stream and task watcher | causal controls without explicit bridge | prioritization signal, not causal proof |
| automatic_comparison_rows_v2.csv | comparison_meta | mixed evidence only with explicit status/risk | raw numeric training without scope flags | safe bridge layer |
| all_feature_embeddings.jsonl | mixed_embedding_pool | same source/scope first | all rows as one homogeneous dataset | train with source/scope features or split by source |

## Short answer

Yes, there is a real risk if we train/analyze the mixed embedding pool blindly. The fix is to keep scope labels and compare only within valid scope.

The current particle0 control conclusion is valid as a **local causal control**: `remove_particle0` is compared against the same-run baseline and random same-count controls. It is not a global stream-history delta.

The comparison engine is allowed to bridge evidence types, but only with explicit status and remaining risks: order control, residual, class-specific gradients, and heldout.
