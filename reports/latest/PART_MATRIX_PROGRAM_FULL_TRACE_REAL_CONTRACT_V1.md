# PART_MATRIX_PROGRAM_FULL_TRACE_REAL_CONTRACT_V1

ParT matrix-program full trace database. This is the ParT port of the old `matrix_program_full_trace_v3`: each attention head is treated as a candidate matrix-program node with all-head gradients, natural role/particle readout, zero-head ablation, compiled route rules, and bundle causal evidence.

- events: **256**
- events_per_group: **64**
- heads: **80**
- diagnosis_counts: `{'weak_or_distributed': 55, 'high_gradient_weak_ablation': 25}`
- groups_csv: `reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv`
- head_grad_csv: `reports/latest/tables/part_full_all_head_supertrace_head_gradients_v1.csv`

## Top Hqql→Tbl confusion-support candidates
| head | diag | conf_support | B_delta_margin | B_delta_tbl_pred | grad_signed | A_damage | C_damage | topA | topB | topC | routes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mod.cls_blocks.0.attn.h2 | high_gradient_weak_ablation | 1.2072 | -0.6447 | -0.2812 | 0.0771 | 0.1273 | -0.7816 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3542 | top1=muon:0.4219 top3=photon:0.3698 |  |
| mod.cls_blocks.0.attn.h1 | high_gradient_weak_ablation | 0.8950 | -0.5825 | -0.1562 | 0.1384 | 0.0643 | -0.7938 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3542 | top1=muon:0.4219 top3=photon:0.3698 |  |
| mod.cls_blocks.0.attn.h0 | high_gradient_weak_ablation | 0.5666 | -0.2854 | -0.1406 | -0.0407 | 0.0544 | -0.2686 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3542 | top1=muon:0.4219 top3=photon:0.3698 |  |
| mod.cls_blocks.1.attn.h2 | high_gradient_weak_ablation | 0.4404 | -0.2529 | -0.0938 | -0.0646 | -0.4458 | -0.1415 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3542 | top1=muon:0.4219 top3=photon:0.3698 |  |
| mod.cls_blocks.1.attn.h6 | high_gradient_weak_ablation | 0.3477 | -0.2227 | -0.0625 | 0.2679 | 0.2894 | -0.6483 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3542 | top1=muon:0.4219 top3=photon:0.3698 |  |
| mod.cls_blocks.1.attn.h1 | high_gradient_weak_ablation | 0.2889 | -0.1326 | -0.0781 | 0.0166 | -0.1000 | -0.1466 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3542 | top1=muon:0.4219 top3=photon:0.3698 |  |
| mod.cls_blocks.1.attn.h7 | high_gradient_weak_ablation | 0.2395 | -0.1145 | -0.0625 | 0.0231 | -0.0763 | -0.1466 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3542 | top1=muon:0.4219 top3=photon:0.3698 |  |
| mod.blocks.4.attn.h5 | weak_or_distributed | 0.2007 | -0.0445 | -0.0781 | -0.0089 | -0.0245 | -0.0774 | top1=electron:0.3125 top3=charged_hadron:0.4583 | top1=muon:0.3594 top3=charged_hadron:0.4115 | top1=electron:0.3594 top3=charged_hadron:0.3906 |  |
| mod.cls_blocks.0.attn.h6 | high_gradient_weak_ablation | 0.1882 | -0.0945 | -0.0469 | 0.1324 | 0.4616 | -0.1932 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3542 | top1=muon:0.4219 top3=photon:0.3698 |  |
| mod.blocks.3.attn.h4 | weak_or_distributed | 0.1601 | -0.0351 | -0.0625 | 0.0270 | 0.0643 | -0.0395 | top1=charged_hadron:0.5000 top3=charged_hadron:0.5104 | top1=charged_hadron:0.5312 top3=charged_hadron:0.5104 | top1=charged_hadron:0.4062 top3=charged_hadron:0.5052 |  |
| mod.blocks.5.attn.h1 | weak_or_distributed | 0.1556 | -0.0619 | -0.0469 | -0.0424 | -0.0673 | 0.0518 | top1=charged_hadron:0.3750 top3=charged_hadron:0.4948 | top1=muon:0.2812 top3=charged_hadron:0.4062 | top1=charged_hadron:0.3281 top3=charged_hadron:0.4479 |  |
| mod.blocks.1.attn.h4 | weak_or_distributed | 0.1517 | -0.0267 | -0.0625 | 0.0018 | -0.0405 | -0.0227 | top1=electron:0.2812 top3=charged_hadron:0.3906 | top1=muon:0.3594 top3=charged_hadron:0.3438 | top1=electron:0.3438 top3=charged_hadron:0.3594 |  |

## Top gradient-supported heads
| head | diag | grad_pred | grad_signed | B_delta_margin | topB | routes |
| --- | --- | --- | --- | --- | --- | --- |
| mod.cls_blocks.0.attn.h3 | high_gradient_weak_ablation | -3.5946 | -1.6206 | 1.5985 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.0.attn.h7 | high_gradient_weak_ablation | 0.6266 | 0.6910 | 0.4832 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.1.attn.h3 | high_gradient_weak_ablation | -1.3604 | -0.3158 | 0.4868 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.0.attn.h4 | high_gradient_weak_ablation | 0.3923 | 0.5459 | -0.0479 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.0.attn.h2 | high_gradient_weak_ablation | 1.6602 | 0.0771 | -0.6447 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.1.attn.h6 | high_gradient_weak_ablation | 0.1086 | 0.2679 | -0.2227 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.1.attn.h2 | high_gradient_weak_ablation | 0.8643 | -0.0646 | -0.2529 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.0.attn.h1 | high_gradient_weak_ablation | 0.3670 | 0.1384 | -0.5825 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.0.attn.h6 | high_gradient_weak_ablation | 0.1315 | 0.1324 | -0.0945 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.0.attn.h0 | high_gradient_weak_ablation | 0.3192 | -0.0407 | -0.2854 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.0.attn.h5 | high_gradient_weak_ablation | 0.0978 | 0.0765 | 0.0503 | top1=muon:0.4219 top3=photon:0.3542 |  |
| mod.cls_blocks.1.attn.h7 | high_gradient_weak_ablation | 0.1954 | 0.0231 | -0.1145 | top1=muon:0.4219 top3=photon:0.3542 |  |

## Heads with largest correct-regime damage
| head | diag | damage | A_delta | C_delta | B_delta | topA | topC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.cls_blocks.0.attn.h3 | high_gradient_weak_ablation | 5.6396 | -2.2270 | 3.4126 | 1.5985 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.0.attn.h7 | high_gradient_weak_ablation | 3.7766 | 2.2560 | -1.5206 | 0.4832 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.0.attn.h4 | high_gradient_weak_ablation | 2.2741 | 1.1493 | -1.1248 | -0.0479 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.1.attn.h3 | high_gradient_weak_ablation | 1.6121 | -0.5606 | 1.0516 | 0.4868 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.1.attn.h6 | high_gradient_weak_ablation | 0.9377 | 0.2894 | -0.6483 | -0.2227 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.0.attn.h2 | high_gradient_weak_ablation | 0.9089 | 0.1273 | -0.7816 | -0.6447 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.0.attn.h1 | high_gradient_weak_ablation | 0.8582 | 0.0643 | -0.7938 | -0.5825 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.0.attn.h6 | high_gradient_weak_ablation | 0.6548 | 0.4616 | -0.1932 | -0.0945 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.1.attn.h4 | high_gradient_weak_ablation | 0.6064 | 0.3462 | 0.2602 | 0.2959 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.1.attn.h2 | high_gradient_weak_ablation | 0.5873 | -0.4458 | -0.1415 | -0.2529 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.0.attn.h5 | high_gradient_weak_ablation | 0.4716 | 0.2462 | -0.2254 | 0.0503 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |
| mod.cls_blocks.0.attn.h0 | high_gradient_weak_ablation | 0.3230 | 0.0544 | -0.2686 | -0.2854 | top1=electron:0.3906 top3=photon:0.3490 | top1=muon:0.4219 top3=photon:0.3698 |

## Interpretation

Read each row as a matrix program: attention head reads particle/context roles, writes a residual channel slice, shifts the Hqql/Tbl margin, and can be checked by zero-head ablation plus bundle causal patch evidence. Strong discovery candidates are heads where all-head gradients, B-confusion ablation, role readout, compiled routes, and bundle evidence agree.
