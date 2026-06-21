# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **126**
- edges: **210**
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 9, 'residual_role': 63, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 15, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|electron<-electron | residual_block:mod.cls_blocks.0 | -0.4486 | 0.0000 | up | 0 | 0.2908 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h1|electron<-muon | residual_block:mod.cls_blocks.0 | 0.1132 | 0.0000 | up | 0 | 0.1132 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h0|electron<-muon | residual_block:mod.cls_blocks.0 | 0.0533 | 0.0000 | up | 0 | 0.0533 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|electron<-electron | residual_block:mod.cls_blocks.0 | 0.0601 | 0.0000 | down | 0 | 0.0329 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h1|electron<-muon | residual_block:mod.cls_blocks.0 | -0.0215 | 0.0000 | down | 0 | 0.0215 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h1|CLS<-muon | residual_block:mod.cls_blocks.0 | -0.0215 | 0.0000 | down | 0 | 0.0187 |
| 7 | attention_pair:mod.cls_blocks.1.attn.h3|electron<-muon | residual_block:mod.cls_blocks.1 | -0.0174 | 0.0000 | down | 0 | 0.0174 |
| 8 | attention_pair:mod.cls_blocks.1.attn.h3|CLS<-muon | residual_block:mod.cls_blocks.1 | -0.0174 | 0.0000 | down | 0 | 0.0173 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h0|electron<-muon | residual_block:mod.cls_blocks.0 | -0.0167 | 0.0000 | down | 0 | 0.0167 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h0|CLS<-muon | residual_block:mod.cls_blocks.0 | -0.0167 | 0.0000 | down | 0 | 0.0096 |
| 11 | attention_pair:mod.cls_blocks.1.attn.h3|electron<-muon | residual_block:mod.cls_blocks.1 | 9.989e-05 | 0.0000 | up | 0 | 9.981e-05 |
| 12 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 3.204e-07 | 0.0000 | down | 0 | 2.384e-07 |
| 13 | attention_pair:mod.cls_blocks.1.attn.h3|CLS<-muon | residual_block:mod.cls_blocks.1 | 9.989e-05 | 0.0000 | up | 0 | -0.0174 |
| 14 | attention_pair:mod.cls_blocks.0.attn.h1|CLS<-muon | residual_block:mod.cls_blocks.0 | 0.1132 | 0.0000 | up | 0 | -0.0187 |
| 15 | attention_pair:mod.cls_blocks.0.attn.h0|CLS<-muon | residual_block:mod.cls_blocks.0 | 0.0533 | 0.0000 | up | 0 | -0.1872 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3846 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3343 | signed_hqql_tbl | C_Tbl_correct |
| 3 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3190 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3155 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.3035 | signed_hqql_tbl | C_Tbl_correct |
| 6 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2804 | signed_hqql_tbl | A_Hqql_correct |
| 7 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2506 | signed_hqql_tbl | C_Tbl_correct |
| 8 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2120 | signed_hqql_tbl | C_Tbl_correct |
| 9 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1999 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 10 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1847 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1828 | signed_hqql_tbl | C_Tbl_correct |
| 12 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1826 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1461 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 14 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1461 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 15 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1424 | signed_hqql_tbl | C_Tbl_correct |
| 16 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1372 | signed_hqql_tbl | A_Hqql_correct |
| 17 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1309 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 18 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1283 | signed_hqql_tbl | C_Tbl_correct |
| 19 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1185 | signed_hqql_tbl | A_Hqql_correct |
| 20 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1157 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 21 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1137 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 22 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1137 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 23 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0999 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 24 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0999 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 25 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0949 | signed_hqql_tbl | C_Tbl_correct |
| 26 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0924 | signed_hqql_tbl | A_Hqql_correct |
| 27 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0865 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 28 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0759 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 29 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0757 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 30 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0740 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 31 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0659 | signed_hqql_tbl | A_Hqql_correct |
| 32 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0636 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 33 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0556 | signed_hqql_tbl | C_Tbl_correct |
| 34 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0554 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0554 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0373 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 37 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0373 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0337 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 39 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0315 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 40 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0315 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_Tbl-Hqql | dim |
| --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.0000 | 103 |
| 2 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.0000 | 8 |
| 3 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.0000 | 121 |
| 4 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.0000 | 45 |
| 5 | classifier_dim:fc_dim_76 | classifier:mod.fc | 0.0000 | 76 |
| 6 | classifier_dim:fc_dim_57 | classifier:mod.fc | 0.0000 | 57 |
| 7 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.0000 | 58 |
| 8 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.0000 | 23 |
| 9 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.0000 | 3 |
| 10 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.0000 | 18 |
| 11 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.0000 | 54 |
| 12 | classifier_dim:fc_dim_34 | classifier:mod.fc | 0.0000 | 34 |
| 13 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.0000 | 82 |
| 14 | classifier_dim:fc_dim_79 | classifier:mod.fc | 0.0000 | 79 |
| 15 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.0000 | 124 |
| 16 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.0000 | 123 |
| 17 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.0000 | 10 |
| 18 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.0000 | 66 |
| 19 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.0000 | 2 |
| 20 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.0000 | 96 |
| 21 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.0000 | 91 |
| 22 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0000 | 80 |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | 0.0000 | 110 |
| 24 | classifier_dim:fc_dim_6 | classifier:mod.fc | 0.0000 | 6 |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=Tbl-Hqql
edge weights are signed causal/gradient/path contributions.
```
