# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **132**
- edges: **203**
- src_label: `label_Hbb`
- tgt_label: `label_Hcc`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 9, 'residual_role': 69, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 8, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 7.451e-08 | 0.0000 | up | 0 | -4.098e-08 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 7.451e-08 | 0.0000 | up | 0 | -4.098e-08 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h0|photon<-CLS | residual_block:mod.cls_blocks.0 | 7.451e-08 | 0.0000 | up | 0 | -4.098e-08 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h0|CLS<-CLS | residual_block:mod.cls_blocks.0 | 7.451e-08 | 0.0000 | up | 0 | -4.098e-08 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h0|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 7.451e-08 | 0.0000 | up | 0 | -4.098e-08 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h0|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 7.451e-08 | 0.0000 | up | 0 | -4.098e-08 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | 7.451e-08 | 0.0000 | up | 0 | -4.098e-08 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 7.451e-08 | 0.0000 | up | 0 | -4.098e-08 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3846 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3343 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3190 | signed_hqql_tbl | A_Hqql_correct |
| 4 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3155 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.3035 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2804 | signed_hqql_tbl | C_Tbl_correct |
| 7 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2506 | signed_hqql_tbl | A_Hqql_correct |
| 8 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2120 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1999 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 10 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1999 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 11 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1847 | signed_hqql_tbl | C_Tbl_correct |
| 12 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1828 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1826 | signed_hqql_tbl | C_Tbl_correct |
| 14 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1461 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 15 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1424 | signed_hqql_tbl | A_Hqql_correct |
| 16 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1372 | signed_hqql_tbl | C_Tbl_correct |
| 17 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1309 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1309 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 19 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1283 | signed_hqql_tbl | A_Hqql_correct |
| 20 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1185 | signed_hqql_tbl | C_Tbl_correct |
| 21 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1157 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 22 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1157 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 23 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1137 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 24 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0999 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 25 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0949 | signed_hqql_tbl | A_Hqql_correct |
| 26 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0924 | signed_hqql_tbl | C_Tbl_correct |
| 27 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0865 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 28 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0865 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0759 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 30 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0759 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 31 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0757 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 32 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0757 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0740 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0740 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0659 | signed_hqql_tbl | C_Tbl_correct |
| 36 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0636 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 37 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0636 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0556 | signed_hqql_tbl | A_Hqql_correct |
| 39 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0554 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 40 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0373 | signed_hqql_tbl | D_Tbl_to_Hqql |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_103 | classifier:mod.fc | -1.1085 | 103 | label_Hbb | label_Hcc |
| 2 | classifier_dim:fc_dim_8 | classifier:mod.fc | -0.8819 | 8 | label_Hbb | label_Hcc |
| 3 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.6736 | 121 | label_Hbb | label_Hcc |
| 4 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.5391 | 45 | label_Hbb | label_Hcc |
| 5 | classifier_dim:fc_dim_76 | classifier:mod.fc | 0.5133 | 76 | label_Hbb | label_Hcc |
| 6 | classifier_dim:fc_dim_57 | classifier:mod.fc | -0.3565 | 57 | label_Hbb | label_Hcc |
| 7 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.3124 | 58 | label_Hbb | label_Hcc |
| 8 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.2249 | 23 | label_Hbb | label_Hcc |
| 9 | classifier_dim:fc_dim_3 | classifier:mod.fc | -0.2157 | 3 | label_Hbb | label_Hcc |
| 10 | classifier_dim:fc_dim_18 | classifier:mod.fc | -0.1982 | 18 | label_Hbb | label_Hcc |
| 11 | classifier_dim:fc_dim_54 | classifier:mod.fc | -0.1572 | 54 | label_Hbb | label_Hcc |
| 12 | classifier_dim:fc_dim_34 | classifier:mod.fc | -0.1541 | 34 | label_Hbb | label_Hcc |
| 13 | classifier_dim:fc_dim_82 | classifier:mod.fc | -0.1485 | 82 | label_Hbb | label_Hcc |
| 14 | classifier_dim:fc_dim_79 | classifier:mod.fc | 0.1283 | 79 | label_Hbb | label_Hcc |
| 15 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.1225 | 124 | label_Hbb | label_Hcc |
| 16 | classifier_dim:fc_dim_123 | classifier:mod.fc | -0.1092 | 123 | label_Hbb | label_Hcc |
| 17 | classifier_dim:fc_dim_10 | classifier:mod.fc | -0.1028 | 10 | label_Hbb | label_Hcc |
| 18 | classifier_dim:fc_dim_66 | classifier:mod.fc | -0.0750 | 66 | label_Hbb | label_Hcc |
| 19 | classifier_dim:fc_dim_2 | classifier:mod.fc | -0.0708 | 2 | label_Hbb | label_Hcc |
| 20 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.0467 | 96 | label_Hbb | label_Hcc |
| 21 | classifier_dim:fc_dim_91 | classifier:mod.fc | -0.0307 | 91 | label_Hbb | label_Hcc |
| 22 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0096 | 80 | label_Hbb | label_Hcc |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0076 | 110 | label_Hbb | label_Hcc |
| 24 | classifier_dim:fc_dim_6 | classifier:mod.fc | 0.0016 | 6 | label_Hbb | label_Hcc |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
