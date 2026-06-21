# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **132**
- edges: **204**
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 68, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 9, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.1500 | 0.0000 | down | 0 | 0.0980 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.2074 | 0.0000 | down | 0 | 0.0588 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -3.204e-07 | 0.0000 | down | 0 | 1.676e-07 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | -3.204e-07 | 0.0000 | down | 0 | 1.676e-07 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-CLS | residual_block:mod.cls_blocks.0 | -3.204e-07 | 0.0000 | down | 0 | 1.676e-07 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -3.204e-07 | 0.0000 | down | 0 | 1.676e-07 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | -3.204e-07 | 0.0000 | down | 0 | 1.676e-07 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|photon<-CLS | residual_block:mod.cls_blocks.0 | -3.204e-07 | 0.0000 | down | 0 | 1.676e-07 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.1270 | 0.0000 | up | 0 | -0.0535 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1460 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1438 | signed_hqql_tbl | C_Tbl_correct |
| 3 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1342 | signed_hqql_tbl | A_Hqql_correct |
| 4 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1282 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1172 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1070 | signed_hqql_tbl | A_Hqql_correct |
| 7 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1036 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 8 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1036 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 9 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1036 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 10 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1036 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 11 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1018 | signed_hqql_tbl | A_Hqql_correct |
| 12 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0995 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0992 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 14 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0980 | signed_hqql_tbl | C_Tbl_correct |
| 15 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0851 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 16 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0844 | signed_hqql_tbl | A_Hqql_correct |
| 17 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0806 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 18 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0710 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 19 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0710 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 20 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0614 | signed_hqql_tbl | A_Hqql_correct |
| 21 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0586 | signed_hqql_tbl | C_Tbl_correct |
| 22 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0543 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0538 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 24 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0538 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 25 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0531 | signed_hqql_tbl | C_Tbl_correct |
| 26 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0495 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 27 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0495 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 28 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0451 | signed_hqql_tbl | A_Hqql_correct |
| 29 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0415 | signed_hqql_tbl | C_Tbl_correct |
| 30 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0364 | signed_hqql_tbl | C_Tbl_correct |
| 31 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0326 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0326 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0325 | signed_hqql_tbl | C_Tbl_correct |
| 34 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0297 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 35 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0261 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 36 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0242 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 37 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0242 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0220 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 39 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0194 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 40 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0182 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_Tbl-Hqql | dim |
| --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.0000 | 18 |
| 2 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.0000 | 66 |
| 3 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.0000 | 58 |
| 4 | classifier_dim:fc_dim_79 | classifier:mod.fc | 0.0000 | 79 |
| 5 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.0000 | 82 |
| 6 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.0000 | 96 |
| 7 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.0000 | 121 |
| 8 | classifier_dim:fc_dim_76 | classifier:mod.fc | 0.0000 | 76 |
| 9 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.0000 | 2 |
| 10 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.0000 | 10 |
| 11 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.0000 | 3 |
| 12 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.0000 | 8 |
| 13 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.0000 | 124 |
| 14 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.0000 | 23 |
| 15 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.0000 | 54 |
| 16 | classifier_dim:fc_dim_57 | classifier:mod.fc | 0.0000 | 57 |
| 17 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.0000 | 91 |
| 18 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.0000 | 103 |
| 19 | classifier_dim:fc_dim_34 | classifier:mod.fc | 0.0000 | 34 |
| 20 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.0000 | 45 |
| 21 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.0000 | 123 |
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
