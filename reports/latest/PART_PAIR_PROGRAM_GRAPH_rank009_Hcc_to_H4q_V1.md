# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **134**
- edges: **203**
- src_label: `label_Hcc`
- tgt_label: `label_H4q`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 70, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 8, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0517 | 0.0000 | down | 0 | 0.0123 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | up | 0 | -5.960e-08 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | up | 0 | -5.960e-08 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h6|photon<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | down | 0 | -5.960e-08 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | down | 0 | -5.960e-08 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | down | 0 | -5.960e-08 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | down | 0 | -5.960e-08 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | down | 0 | -5.960e-08 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.5307 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3850 | signed_hqql_tbl | C_Tbl_correct |
| 3 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.3130 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2898 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2595 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2054 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 7 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2054 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 8 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2032 | signed_hqql_tbl | C_Tbl_correct |
| 9 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1899 | signed_hqql_tbl | A_Hqql_correct |
| 10 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1649 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1645 | signed_hqql_tbl | C_Tbl_correct |
| 12 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1643 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 13 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1643 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 14 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1513 | signed_hqql_tbl | A_Hqql_correct |
| 15 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1422 | signed_hqql_tbl | C_Tbl_correct |
| 16 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1374 | signed_hqql_tbl | A_Hqql_correct |
| 17 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1348 | signed_hqql_tbl | A_Hqql_correct |
| 18 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1322 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 19 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1322 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 20 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1188 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 21 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1181 | signed_hqql_tbl | C_Tbl_correct |
| 22 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1101 | signed_hqql_tbl | A_Hqql_correct |
| 23 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1099 | signed_hqql_tbl | A_Hqql_correct |
| 24 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0936 | signed_hqql_tbl | C_Tbl_correct |
| 25 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0885 | signed_hqql_tbl | C_Tbl_correct |
| 26 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0864 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0757 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 28 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0757 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0756 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 30 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0732 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 31 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0716 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 32 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0716 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0487 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 34 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0469 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0469 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0461 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 37 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0383 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0383 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 39 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0363 | signed_hqql_tbl | C_Tbl_correct |
| 40 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0354 | signed_hqql_tbl | D_Tbl_to_Hqql |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_10 | classifier:mod.fc | 1.1334 | 10 | label_Hcc | label_H4q |
| 2 | classifier_dim:fc_dim_76 | classifier:mod.fc | -1.0834 | 76 | label_Hcc | label_H4q |
| 3 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.9735 | 79 | label_Hcc | label_H4q |
| 4 | classifier_dim:fc_dim_57 | classifier:mod.fc | -0.9148 | 57 | label_Hcc | label_H4q |
| 5 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.8581 | 103 | label_Hcc | label_H4q |
| 6 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.7016 | 3 | label_Hcc | label_H4q |
| 7 | classifier_dim:fc_dim_8 | classifier:mod.fc | -0.5673 | 8 | label_Hcc | label_H4q |
| 8 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.4520 | 2 | label_Hcc | label_H4q |
| 9 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.4152 | 58 | label_Hcc | label_H4q |
| 10 | classifier_dim:fc_dim_124 | classifier:mod.fc | -0.4052 | 124 | label_Hcc | label_H4q |
| 11 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.3661 | 121 | label_Hcc | label_H4q |
| 12 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.3594 | 82 | label_Hcc | label_H4q |
| 13 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.2746 | 54 | label_Hcc | label_H4q |
| 14 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.2618 | 123 | label_Hcc | label_H4q |
| 15 | classifier_dim:fc_dim_91 | classifier:mod.fc | -0.2254 | 91 | label_Hcc | label_H4q |
| 16 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.2212 | 18 | label_Hcc | label_H4q |
| 17 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.1824 | 45 | label_Hcc | label_H4q |
| 18 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.1494 | 66 | label_Hcc | label_H4q |
| 19 | classifier_dim:fc_dim_34 | classifier:mod.fc | 0.1270 | 34 | label_Hcc | label_H4q |
| 20 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.0857 | 96 | label_Hcc | label_H4q |
| 21 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.0767 | 23 | label_Hcc | label_H4q |
| 22 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0436 | 6 | label_Hcc | label_H4q |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | 0.0077 | 110 | label_Hcc | label_H4q |
| 24 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0055 | 80 | label_Hcc | label_H4q |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
