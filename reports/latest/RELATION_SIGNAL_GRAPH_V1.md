# Relation Signal Graph v1

Automatic relationship mining over the stream/evidence graph. Signals are prioritization, not causal proof.

- Latest run index: **14**
- Nodes: **47**
- Edges: **89**

## Top relation signals
| signal | support | src | relation | dst | strength | lift | confidence | next_control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.9474 | 151 | pattern:core_high_pt | pattern_supports_hypothesis | hypothesis:AH1 | 0.1545 | 1.1643 | MEDIUM | remove particle0 / keep only particle0 / top-k controls |
| 0.9288 | 120 | pattern:particle0 | pattern_supports_hypothesis | hypothesis:AH1 | 0.2032 | 1.1512 | MEDIUM | remove particle0 / keep only particle0 / top-k controls |
| 0.9038 | 99 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Hqql | 0.0493 | 1.1512 | MEDIUM | particle0/top-k/random controls |
| 0.8884 | 126 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Hqql | 0.0357 | 1.1643 | MEDIUM | particle0/top-k/random controls |
| 0.8708 | 139 | pattern:charged | particle_pattern_associated_with_class | class:label_Hqql | 0.0312 | 1.0541 | MEDIUM | route-neighbor trace and heldout stability |
| 0.7623 | 17 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Tbl | 0.2837 | 1.0897 | MEDIUM | particle0/top-k/random controls |
| 0.7525 | 20 | pattern:wide | pattern_supports_hypothesis | hypothesis:T6_WIDE_SECONDARY_CONTEXT | 0.6261 | 5.0000 | MEDIUM | route-neighbor trace |
| 0.7406 | 20 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Tbl | 0.2266 | 1.0188 | MEDIUM | particle0/top-k/random controls |
| 0.7262 | 23 | pattern:charged | particle_pattern_associated_with_class | class:label_Tbl | 0.1879 | 0.9615 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6640 | 56 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Hqql | 0.0527 | 0.9193 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6272 | 7 | pattern:wide | particle_pattern_associated_with_class | class:label_Tbl | 0.4277 | 2.6923 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6248 | 7 | pattern:other_particle | particle_pattern_associated_with_class | class:label_QCD | 0.4240 | 2.0588 | MEDIUM | route-neighbor trace and heldout stability |
| 0.6101 | 12 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Zqq | 0.2583 | 1.3662 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5975 | 17 | pattern:charged | particle_pattern_associated_with_class | class:label_Zqq | 0.1888 | 0.8941 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5859 | 1 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Wqq | 5.0278 | 0.8333 | LOW | particle0/top-k/random controls |
| 0.5688 | 1 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Wqq | 5.0278 | 0.6623 | LOW | particle0/top-k/random controls |
| 0.5357 | 11 | pattern:wide | particle_pattern_associated_with_class | class:label_Hqql | 0.2732 | 0.7674 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5338 | 2 | pattern:particle0 | particle_pattern_associated_with_class | class:label_Zqq | 2.4129 | 0.1613 | LOW | particle0/top-k/random controls |
| 0.5242 | 3 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_Zqq | 1.4809 | 0.1923 | LOW | particle0/top-k/random controls |
| 0.5222 | 9 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Tbl | 0.3285 | 0.8145 | MEDIUM | route-neighbor trace and heldout stability |
| 0.5180 | 1 | pattern:wide | particle_pattern_associated_with_class | class:label_Wqq | 2.9497 | 5.0000 | LOW | route-neighbor trace and heldout stability |
| 0.5079 | 1 | pattern:particle0 | particle_pattern_associated_with_class | class:label_QCD | 4.8282 | 0.2083 | LOW | particle0/top-k/random controls |
| 0.5037 | 1 | pattern:core_high_pt | particle_pattern_associated_with_class | class:label_QCD | 4.8282 | 0.1656 | LOW | particle0/top-k/random controls |
| 0.4464 | 4 | pattern:charged | particle_pattern_associated_with_class | class:label_QCD | 0.7499 | 0.5435 | LOW | route-neighbor trace and heldout stability |
| 0.4438 | 1 | pattern:other_particle | particle_pattern_associated_with_class | class:label_Wqq | 3.0395 | 1.1765 | LOW | route-neighbor trace and heldout stability |

## Alerts / controls
| severity | relation | score | next_control | reason |
| --- | --- | --- | --- | --- |
| HIGH | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR->hypothesis:AH1 | 1.0000 | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. | Is the all-head system over-dominated by particle0 / leading-core evidence? |
| MEDIUM | task:T3_NEGATIVE_SUPPRESSIVE_GATES->hypothesis:NEGATIVE_GATES | 1.0000 | Add suppressive-head analysis and class-specific negative gate gradients. | Are there heads that suppress the current class logit? |
| MEDIUM | task:T5_PATCH_VS_GRADIENT_DIVERGENCE->hypothesis:AH3 | 1.0000 | Build patch-rank vs gate-rank report and run multi-head patch combinations. | Which heads are patch-important but not gradient-important, or gradient-important but not patch-important? |
| HIGH | task:T4_HQQL_TBL_SIGNATURE->hypothesis:AH2 | 0.9625 | Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq. | Is the current stream dominated by Hqql/Tbl high-confidence events? |
| HIGH | task:T2_HEAD_RANK_STABILITY->hypothesis:AH4 | 0.9571 | Keep tracking; if unstable, split by class/sample size and run heldout stability. | Do the same heads stay important across snapshots? |
| HIGH | task:T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR->hypothesis:AH1 | 0.2426 | Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls. | task score is deterministic weak signal |
| HIGH | task:T3_NEGATIVE_SUPPRESSIVE_GATES->hypothesis:NEGATIVE_GATES | 0.2426 | Add suppressive-head analysis and class-specific negative gate gradients. | task score is deterministic weak signal |
| HIGH | task:T5_PATCH_VS_GRADIENT_DIVERGENCE->hypothesis:AH3 | 0.2426 | Build patch-rank vs gate-rank report and run multi-head patch combinations. | task score is deterministic weak signal |

## Interpretation

- Strong particle0/core relations are currently candidates, not proof. They require particle0/top-k controls.
- Head relations are mostly gradient/support relations until class-specific gradients and causal patches are added.
- Wide/secondary relations need route-neighbor trace.

## Files

- JSON: `manifests/latest/relation_signal_graph_v1.json`
- Edges: `reports/latest/tables/relation_signal_edges.csv`
- Nodes: `reports/latest/tables/relation_signal_nodes.csv`
- Alerts: `reports/latest/tables/relation_signal_alerts.csv`
