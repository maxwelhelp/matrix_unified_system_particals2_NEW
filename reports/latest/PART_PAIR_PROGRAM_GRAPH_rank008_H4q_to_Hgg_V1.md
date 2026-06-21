# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **125**
- edges: **205**
- src_label: `label_H4q`
- tgt_label: `label_Hgg`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 62, 'classifier_activation_dim': 9}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 10, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.3685 | 0.0000 | up | 0 | 0.2332 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.1846 | 0.0000 | down | 0 | 0.0982 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h7|neutral_hadron<-electron | residual_block:mod.cls_blocks.0 | 0.0525 | 0.0000 | up | 0 | 0.0504 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h7|neutral_hadron<-electron | residual_block:mod.cls_blocks.0 | -0.0049 | 0.0000 | down | 0 | 0.0049 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.980e-08 | 0.0000 | up | 0 | -2.794e-08 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | -2.980e-08 | 0.0000 | up | 0 | -2.794e-08 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.980e-08 | 0.0000 | up | 0 | -2.794e-08 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | -2.980e-08 | 0.0000 | up | 0 | -2.794e-08 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.980e-08 | 0.0000 | up | 0 | -2.794e-08 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.980e-08 | 0.0000 | up | 0 | -2.794e-08 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3015 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2374 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2128 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1995 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1779 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.1715 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 7 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.1715 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 8 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1587 | signed_hqql_tbl | C_Tbl_correct |
| 9 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1453 | signed_hqql_tbl | C_Tbl_correct |
| 10 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1437 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1118 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1004 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0925 | signed_hqql_tbl | A_Hqql_correct |
| 14 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0890 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 15 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0890 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 16 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0756 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 17 | residual_particle:mod.blocks.1 | classifier:mod.fc | 0.0717 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.1 | classifier:mod.fc | 0.0717 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 19 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0708 | signed_hqql_tbl | A_Hqql_correct |
| 20 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0663 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 21 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0539 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 22 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0539 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0487 | signed_hqql_tbl | A_Hqql_correct |
| 24 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0384 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 25 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0348 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 26 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0301 | signed_hqql_tbl | C_Tbl_correct |
| 27 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0277 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 28 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0277 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.0272 | signed_hqql_tbl | C_Tbl_correct |
| 30 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0246 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 31 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0246 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0245 | signed_hqql_tbl | C_Tbl_correct |
| 33 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0222 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0222 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0222 | signed_hqql_tbl | C_Tbl_correct |
| 36 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0206 | signed_hqql_tbl | C_Tbl_correct |
| 37 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0204 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 38 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0185 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 39 | residual_particle:mod.blocks.3 | classifier:mod.fc | 0.0149 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 40 | residual_particle:mod.blocks.3 | classifier:mod.fc | 0.0149 | signed_hqql_tbl | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_3 | classifier:mod.fc | -1.4458 | 3 | label_H4q | label_Hgg |
| 2 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.9769 | 8 | label_H4q | label_Hgg |
| 3 | classifier_dim:fc_dim_10 | classifier:mod.fc | -0.9306 | 10 | label_H4q | label_Hgg |
| 4 | classifier_dim:fc_dim_45 | classifier:mod.fc | -0.8398 | 45 | label_H4q | label_Hgg |
| 5 | classifier_dim:fc_dim_79 | classifier:mod.fc | 0.8393 | 79 | label_H4q | label_Hgg |
| 6 | classifier_dim:fc_dim_57 | classifier:mod.fc | -0.3788 | 57 | label_H4q | label_Hgg |
| 7 | classifier_dim:fc_dim_18 | classifier:mod.fc | -0.3531 | 18 | label_H4q | label_Hgg |
| 8 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.3457 | 124 | label_H4q | label_Hgg |
| 9 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.3305 | 58 | label_H4q | label_Hgg |
| 10 | classifier_dim:fc_dim_54 | classifier:mod.fc | -0.3205 | 54 | label_H4q | label_Hgg |
| 11 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.2978 | 66 | label_H4q | label_Hgg |
| 12 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.2277 | 91 | label_H4q | label_Hgg |
| 13 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.1248 | 103 | label_H4q | label_Hgg |
| 14 | classifier_dim:fc_dim_76 | classifier:mod.fc | 0.0979 | 76 | label_H4q | label_Hgg |
| 15 | classifier_dim:fc_dim_34 | classifier:mod.fc | -0.0802 | 34 | label_H4q | label_Hgg |
| 16 | classifier_dim:fc_dim_2 | classifier:mod.fc | -0.0740 | 2 | label_H4q | label_Hgg |
| 17 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.0649 | 23 | label_H4q | label_Hgg |
| 18 | classifier_dim:fc_dim_96 | classifier:mod.fc | -0.0572 | 96 | label_H4q | label_Hgg |
| 19 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.0465 | 121 | label_H4q | label_Hgg |
| 20 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.0124 | 82 | label_H4q | label_Hgg |
| 21 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0105 | 110 | label_H4q | label_Hgg |
| 22 | classifier_dim:fc_dim_123 | classifier:mod.fc | -0.0051 | 123 | label_H4q | label_Hgg |
| 23 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0022 | 80 | label_H4q | label_Hgg |
| 24 | classifier_dim:fc_dim_6 | classifier:mod.fc | 0.0015 | 6 | label_H4q | label_Hgg |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
