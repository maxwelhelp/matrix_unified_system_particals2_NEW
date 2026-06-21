# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **131**
- edges: **207**
- src_label: `label_Hcc`
- tgt_label: `label_Hgg`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_cls': 2, 'residual_particle': 8, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 67, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 12, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.9907 | 0.0000 | up | 0 | 0.7396 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.6870 | 0.0000 | up | 0 | 0.5249 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-electron | residual_block:mod.cls_blocks.0 | 0.2883 | 0.0000 | up | 0 | 0.2331 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-electron | residual_block:mod.cls_blocks.0 | 0.1823 | 0.0000 | up | 0 | 0.1308 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.1535 | 0.0000 | down | 0 | 0.0925 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.1003 | 0.0000 | down | 0 | 0.0834 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-electron | residual_block:mod.cls_blocks.0 | -0.0190 | 0.0000 | down | 0 | 0.0158 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-electron | residual_block:mod.cls_blocks.0 | -0.0150 | 0.0000 | down | 0 | 0.0118 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | -2.086e-07 | 0.0000 | up | 0 | 1.192e-07 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.086e-07 | 0.0000 | up | 0 | 1.192e-07 |
| 11 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | -2.086e-07 | 0.0000 | up | 0 | 1.192e-07 |
| 12 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.086e-07 | 0.0000 | up | 0 | 1.192e-07 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3973 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3647 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2139 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1855 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1688 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1444 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 7 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1444 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 8 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1253 | signed_hqql_tbl | C_Tbl_correct |
| 9 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1241 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 10 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1241 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 11 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1029 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0994 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0952 | signed_hqql_tbl | A_Hqql_correct |
| 14 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0885 | signed_hqql_tbl | A_Hqql_correct |
| 15 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0849 | signed_hqql_tbl | A_Hqql_correct |
| 16 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0832 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 17 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0809 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 18 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0796 | signed_hqql_tbl | A_Hqql_correct |
| 19 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0756 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 20 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0756 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0732 | signed_hqql_tbl | C_Tbl_correct |
| 22 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0732 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 23 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0717 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 24 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0672 | signed_hqql_tbl | C_Tbl_correct |
| 25 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0619 | signed_hqql_tbl | C_Tbl_correct |
| 26 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0593 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0548 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 28 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0548 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0518 | signed_hqql_tbl | A_Hqql_correct |
| 30 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0483 | signed_hqql_tbl | A_Hqql_correct |
| 31 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0446 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0446 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0402 | signed_hqql_tbl | C_Tbl_correct |
| 34 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0385 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0385 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0383 | signed_hqql_tbl | C_Tbl_correct |
| 37 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0350 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 38 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0296 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 39 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0296 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 40 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0283 | signed_hqql_tbl | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_57 | classifier:mod.fc | -1.2936 | 57 | label_Hcc | label_Hgg |
| 2 | classifier_dim:fc_dim_76 | classifier:mod.fc | -0.9855 | 76 | label_Hcc | label_Hgg |
| 3 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.9829 | 103 | label_Hcc | label_Hgg |
| 4 | classifier_dim:fc_dim_3 | classifier:mod.fc | -0.7442 | 3 | label_Hcc | label_Hgg |
| 5 | classifier_dim:fc_dim_45 | classifier:mod.fc | -0.6574 | 45 | label_Hcc | label_Hgg |
| 6 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.4471 | 66 | label_Hcc | label_Hgg |
| 7 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.4126 | 121 | label_Hcc | label_Hgg |
| 8 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.4096 | 8 | label_Hcc | label_Hgg |
| 9 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.3781 | 2 | label_Hcc | label_Hgg |
| 10 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.3718 | 82 | label_Hcc | label_Hgg |
| 11 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.2567 | 123 | label_Hcc | label_Hgg |
| 12 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.2028 | 10 | label_Hcc | label_Hgg |
| 13 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.1416 | 23 | label_Hcc | label_Hgg |
| 14 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.1342 | 79 | label_Hcc | label_Hgg |
| 15 | classifier_dim:fc_dim_18 | classifier:mod.fc | -0.1319 | 18 | label_Hcc | label_Hgg |
| 16 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.0848 | 58 | label_Hcc | label_Hgg |
| 17 | classifier_dim:fc_dim_124 | classifier:mod.fc | -0.0595 | 124 | label_Hcc | label_Hgg |
| 18 | classifier_dim:fc_dim_34 | classifier:mod.fc | 0.0469 | 34 | label_Hcc | label_Hgg |
| 19 | classifier_dim:fc_dim_54 | classifier:mod.fc | -0.0459 | 54 | label_Hcc | label_Hgg |
| 20 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0421 | 6 | label_Hcc | label_Hgg |
| 21 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.0285 | 96 | label_Hcc | label_Hgg |
| 22 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0076 | 80 | label_Hcc | label_Hgg |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0028 | 110 | label_Hcc | label_Hgg |
| 24 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.0022 | 91 | label_Hcc | label_Hgg |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
