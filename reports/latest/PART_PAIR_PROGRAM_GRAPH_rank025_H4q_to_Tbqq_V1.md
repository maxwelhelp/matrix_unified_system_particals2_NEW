# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **128**
- edges: **204**
- src_label: `label_H4q`
- tgt_label: `label_Tbqq`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 65, 'classifier_activation_dim': 9}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 9, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.5120 | 0.0000 | up | 0 | 0.4337 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0913 | 0.0000 | down | 0 | 0.0873 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | down | 0 | -1.006e-07 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | down | 0 | -1.006e-07 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -1.006e-07 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -1.006e-07 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -1.006e-07 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -1.006e-07 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h6|photon<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -1.006e-07 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.4968 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.4287 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 3 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.4287 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 4 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.3755 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3577 | signed_hqql_tbl | C_Tbl_correct |
| 6 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3371 | signed_hqql_tbl | C_Tbl_correct |
| 7 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3189 | signed_hqql_tbl | C_Tbl_correct |
| 8 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2763 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2474 | signed_hqql_tbl | A_Hqql_correct |
| 10 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2436 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 11 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.2052 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1910 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1612 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 14 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1539 | signed_hqql_tbl | A_Hqql_correct |
| 15 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.1498 | signed_hqql_tbl | C_Tbl_correct |
| 16 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1467 | signed_hqql_tbl | C_Tbl_correct |
| 17 | residual_particle:mod.blocks.1 | classifier:mod.fc | 0.1335 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.1 | classifier:mod.fc | 0.1335 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 19 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1190 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 20 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1190 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1139 | signed_hqql_tbl | A_Hqql_correct |
| 22 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1133 | signed_hqql_tbl | C_Tbl_correct |
| 23 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1117 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 24 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1109 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 25 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1109 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 26 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1048 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.1042 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 28 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1029 | signed_hqql_tbl | A_Hqql_correct |
| 29 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.1025 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 30 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.1025 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 31 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1014 | signed_hqql_tbl | C_Tbl_correct |
| 32 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.1003 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 33 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0964 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 34 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0718 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 35 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0718 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0631 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 37 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0631 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0621 | signed_hqql_tbl | A_Hqql_correct |
| 39 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0571 | signed_hqql_tbl | C_Tbl_correct |
| 40 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0564 | signed_hqql_tbl | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_3 | classifier:mod.fc | -1.5487 | 3 | label_H4q | label_Tbqq |
| 2 | classifier_dim:fc_dim_121 | classifier:mod.fc | -1.5038 | 121 | label_H4q | label_Tbqq |
| 3 | classifier_dim:fc_dim_34 | classifier:mod.fc | -1.1432 | 34 | label_H4q | label_Tbqq |
| 4 | classifier_dim:fc_dim_10 | classifier:mod.fc | -1.0732 | 10 | label_H4q | label_Tbqq |
| 5 | classifier_dim:fc_dim_57 | classifier:mod.fc | 0.8956 | 57 | label_H4q | label_Tbqq |
| 6 | classifier_dim:fc_dim_76 | classifier:mod.fc | 0.8931 | 76 | label_H4q | label_Tbqq |
| 7 | classifier_dim:fc_dim_66 | classifier:mod.fc | -0.6517 | 66 | label_H4q | label_Tbqq |
| 8 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.4622 | 2 | label_H4q | label_Tbqq |
| 9 | classifier_dim:fc_dim_45 | classifier:mod.fc | -0.4417 | 45 | label_H4q | label_Tbqq |
| 10 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.3838 | 103 | label_H4q | label_Tbqq |
| 11 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.2471 | 91 | label_H4q | label_Tbqq |
| 12 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.1929 | 123 | label_H4q | label_Tbqq |
| 13 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.1652 | 58 | label_H4q | label_Tbqq |
| 14 | classifier_dim:fc_dim_82 | classifier:mod.fc | -0.1499 | 82 | label_H4q | label_Tbqq |
| 15 | classifier_dim:fc_dim_8 | classifier:mod.fc | -0.1003 | 8 | label_H4q | label_Tbqq |
| 16 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.0663 | 18 | label_H4q | label_Tbqq |
| 17 | classifier_dim:fc_dim_124 | classifier:mod.fc | -0.0518 | 124 | label_H4q | label_Tbqq |
| 18 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.0274 | 54 | label_H4q | label_Tbqq |
| 19 | classifier_dim:fc_dim_96 | classifier:mod.fc | -0.0252 | 96 | label_H4q | label_Tbqq |
| 20 | classifier_dim:fc_dim_80 | classifier:mod.fc | -0.0249 | 80 | label_H4q | label_Tbqq |
| 21 | classifier_dim:fc_dim_23 | classifier:mod.fc | -0.0233 | 23 | label_H4q | label_Tbqq |
| 22 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0189 | 110 | label_H4q | label_Tbqq |
| 23 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0048 | 6 | label_H4q | label_Tbqq |
| 24 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.0018 | 79 | label_H4q | label_Tbqq |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
