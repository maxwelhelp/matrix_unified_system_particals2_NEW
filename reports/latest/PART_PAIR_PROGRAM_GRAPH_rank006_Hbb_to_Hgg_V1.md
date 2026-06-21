# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **124**
- edges: **203**
- src_label: `label_Hbb`
- tgt_label: `label_Hgg`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_cls': 2, 'residual_particle': 8, 'attention_pair': 8, 'residual_block': 9, 'residual_role': 62, 'classifier_activation_dim': 9}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 8, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 4.470e-08 | 0.0000 | down | 0 | -9.686e-08 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 4.470e-08 | 0.0000 | down | 0 | -9.686e-08 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | 4.470e-08 | 0.0000 | down | 0 | -9.686e-08 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 4.470e-08 | 0.0000 | down | 0 | -9.686e-08 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 4.470e-08 | 0.0000 | down | 0 | -9.686e-08 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | 4.470e-08 | 0.0000 | down | 0 | -9.686e-08 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-CLS | residual_block:mod.cls_blocks.0 | 4.470e-08 | 0.0000 | down | 0 | -9.686e-08 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|photon<-CLS | residual_block:mod.cls_blocks.0 | 4.470e-08 | 0.0000 | down | 0 | -9.686e-08 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3728 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3087 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.2037 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.2019 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1975 | signed_hqql_tbl | C_Tbl_correct |
| 6 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1565 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 7 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1565 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 8 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1429 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 9 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1253 | signed_hqql_tbl | A_Hqql_correct |
| 10 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1223 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1095 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1094 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1081 | signed_hqql_tbl | C_Tbl_correct |
| 14 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1030 | signed_hqql_tbl | A_Hqql_correct |
| 15 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1026 | signed_hqql_tbl | A_Hqql_correct |
| 16 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1003 | signed_hqql_tbl | A_Hqql_correct |
| 17 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0909 | signed_hqql_tbl | C_Tbl_correct |
| 18 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0851 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 19 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0851 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 20 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0836 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 21 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0765 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 22 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0657 | signed_hqql_tbl | C_Tbl_correct |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0650 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 24 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0650 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 25 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0613 | signed_hqql_tbl | C_Tbl_correct |
| 26 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0605 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0560 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 28 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0482 | signed_hqql_tbl | C_Tbl_correct |
| 29 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0473 | signed_hqql_tbl | C_Tbl_correct |
| 30 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0471 | signed_hqql_tbl | A_Hqql_correct |
| 31 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0466 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 32 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0441 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0441 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0421 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0421 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0416 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 37 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0416 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0393 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 39 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0393 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 40 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0379 | signed_hqql_tbl | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_57 | classifier:mod.fc | -1.6501 | 57 | label_Hbb | label_Hgg |
| 2 | classifier_dim:fc_dim_121 | classifier:mod.fc | 1.0862 | 121 | label_Hbb | label_Hgg |
| 3 | classifier_dim:fc_dim_3 | classifier:mod.fc | -0.9599 | 3 | label_Hbb | label_Hgg |
| 4 | classifier_dim:fc_dim_8 | classifier:mod.fc | -0.4723 | 8 | label_Hbb | label_Hgg |
| 5 | classifier_dim:fc_dim_76 | classifier:mod.fc | -0.4722 | 76 | label_Hbb | label_Hgg |
| 6 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.3721 | 66 | label_Hbb | label_Hgg |
| 7 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.3665 | 23 | label_Hbb | label_Hgg |
| 8 | classifier_dim:fc_dim_18 | classifier:mod.fc | -0.3300 | 18 | label_Hbb | label_Hgg |
| 9 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.3073 | 2 | label_Hbb | label_Hgg |
| 10 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.2277 | 58 | label_Hbb | label_Hgg |
| 11 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.2233 | 82 | label_Hbb | label_Hgg |
| 12 | classifier_dim:fc_dim_54 | classifier:mod.fc | -0.2030 | 54 | label_Hbb | label_Hgg |
| 13 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.1475 | 123 | label_Hbb | label_Hgg |
| 14 | classifier_dim:fc_dim_103 | classifier:mod.fc | -0.1256 | 103 | label_Hbb | label_Hgg |
| 15 | classifier_dim:fc_dim_45 | classifier:mod.fc | -0.1183 | 45 | label_Hbb | label_Hgg |
| 16 | classifier_dim:fc_dim_34 | classifier:mod.fc | -0.1072 | 34 | label_Hbb | label_Hgg |
| 17 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.1000 | 10 | label_Hbb | label_Hgg |
| 18 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.0752 | 96 | label_Hbb | label_Hgg |
| 19 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.0630 | 124 | label_Hbb | label_Hgg |
| 20 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0406 | 6 | label_Hbb | label_Hgg |
| 21 | classifier_dim:fc_dim_91 | classifier:mod.fc | -0.0285 | 91 | label_Hbb | label_Hgg |
| 22 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0172 | 80 | label_Hbb | label_Hgg |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0104 | 110 | label_Hbb | label_Hgg |
| 24 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.0058 | 79 | label_Hbb | label_Hgg |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
