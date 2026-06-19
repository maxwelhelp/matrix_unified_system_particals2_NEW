# Stream Task Watcher v1

This is an automatic watcher over the research stream. It scores only predefined tasks/questions, not arbitrary interpretations.

- Latest run index: **14**
- Stream events: **6795**
- Latest-run events: **481**

## Task scores
| priority | state | score | task | question | next_action |
| --- | --- | --- | --- | --- | --- |
| P0 | HIGH | 1.0000 | T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR | Is the all-head system over-dominated by particle0 / leading-core evidence? | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. |
| P0 | HIGH | 0.9625 | T4_HQQL_TBL_SIGNATURE | Is the current stream dominated by Hqql/Tbl high-confidence events? | Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq. |
| P0 | HIGH | 0.9571 | T2_HEAD_RANK_STABILITY | Do the same heads stay important across snapshots? | Keep tracking; if unstable, split by class/sample size and run heldout stability. |
| P1 | HIGH | 1.0000 | T3_NEGATIVE_SUPPRESSIVE_GATES | Are there heads that suppress the current class logit? | Add suppressive-head analysis and class-specific negative gate gradients. |
| P1 | HIGH | 1.0000 | T5_PATCH_VS_GRADIENT_DIVERGENCE | Which heads are patch-important but not gradient-important, or gradient-important but not patch-important? | Build patch-rank vs gate-rank report and run multi-head patch combinations. |
| P1 | LOW | 0.0600 | T6_WIDE_SECONDARY_CONTEXT | Besides particle0/core, is there stable wide/secondary particle context? | Run route-neighbor trace for top all-head particles and wide secondary particles. |

## What this means

- **T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR** is `HIGH` (1.0000). Next: Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls.
- **T4_HQQL_TBL_SIGNATURE** is `HIGH` (0.9625). Next: Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq.
- **T2_HEAD_RANK_STABILITY** is `HIGH` (0.9571). Next: Keep tracking; if unstable, split by class/sample size and run heldout stability.
- **T3_NEGATIVE_SUPPRESSIVE_GATES** is `HIGH` (1.0000). Next: Add suppressive-head analysis and class-specific negative gate gradients.
- **T5_PATCH_VS_GRADIENT_DIVERGENCE** is `HIGH` (1.0000). Next: Build patch-rank vs gate-rank report and run multi-head patch combinations.

## Files

- JSON: `manifests/latest/stream_task_watcher_v1.json`
- Scores: `reports/latest/tables/stream_task_watcher_scores.csv`
- Weak training dataset: `reports/latest/tables/stream_task_training_dataset.jsonl`
