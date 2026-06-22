# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **132**
- edges: **203**
- src_label: `label_Hcc`
- tgt_label: `label_Zqq`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_cls': 2, 'residual_particle': 8, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 69, 'classifier_activation_dim': 9}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 8, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.6378 | 0.0000 | down | 0 | 0.2943 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|electron<-electron | residual_block:mod.cls_blocks.0 | -0.2140 | 0.0000 | down | 0 | 0.2140 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | up | 0 | 9.313e-09 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | up | 0 | 9.313e-09 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|electron<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | up | 0 | 9.313e-09 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | up | 0 | 9.313e-09 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|photon<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | up | 0 | 9.313e-09 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | 1.118e-07 | 0.0000 | up | 0 | 9.313e-09 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.5416 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.4528 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2698 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2419 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2195 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 6 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.2180 | signed_hqql_tbl | C_Tbl_correct |
| 7 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2171 | signed_hqql_tbl | C_Tbl_correct |
| 8 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1800 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 9 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1461 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 10 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1461 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 11 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1409 | signed_hqql_tbl | C_Tbl_correct |
| 12 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1322 | signed_hqql_tbl | C_Tbl_correct |
| 13 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1178 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 14 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1178 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 15 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1169 | signed_hqql_tbl | C_Tbl_correct |
| 16 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1054 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 17 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1041 | signed_hqql_tbl | A_Hqql_correct |
| 18 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0994 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 19 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0908 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 20 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0908 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0888 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 22 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0888 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0732 | signed_hqql_tbl | A_Hqql_correct |
| 24 | residual_particle:mod.blocks.7 | classifier:mod.fc | -0.0718 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 25 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0715 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 26 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0715 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 27 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0659 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 28 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0659 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0651 | signed_hqql_tbl | A_Hqql_correct |
| 30 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0534 | signed_hqql_tbl | C_Tbl_correct |
| 31 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0516 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0516 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0438 | signed_hqql_tbl | A_Hqql_correct |
| 34 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0396 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0396 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0352 | signed_hqql_tbl | C_Tbl_correct |
| 37 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0272 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 38 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0205 | signed_hqql_tbl | A_Hqql_correct |
| 39 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0197 | signed_hqql_tbl | A_Hqql_correct |
| 40 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0196 | signed_hqql_tbl | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_79 | classifier:mod.fc | -1.0130 | 79 | label_Hcc | label_Zqq |
| 2 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.9938 | 10 | label_Hcc | label_Zqq |
| 3 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.9532 | 8 | label_Hcc | label_Zqq |
| 4 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.8505 | 2 | label_Hcc | label_Zqq |
| 5 | classifier_dim:fc_dim_66 | classifier:mod.fc | -0.7085 | 66 | label_Hcc | label_Zqq |
| 6 | classifier_dim:fc_dim_121 | classifier:mod.fc | -0.7051 | 121 | label_Hcc | label_Zqq |
| 7 | classifier_dim:fc_dim_45 | classifier:mod.fc | -0.6072 | 45 | label_Hcc | label_Zqq |
| 8 | classifier_dim:fc_dim_18 | classifier:mod.fc | -0.5056 | 18 | label_Hcc | label_Zqq |
| 9 | classifier_dim:fc_dim_76 | classifier:mod.fc | -0.4996 | 76 | label_Hcc | label_Zqq |
| 10 | classifier_dim:fc_dim_3 | classifier:mod.fc | -0.3963 | 3 | label_Hcc | label_Zqq |
| 11 | classifier_dim:fc_dim_57 | classifier:mod.fc | -0.3537 | 57 | label_Hcc | label_Zqq |
| 12 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.3312 | 23 | label_Hcc | label_Zqq |
| 13 | classifier_dim:fc_dim_82 | classifier:mod.fc | -0.3028 | 82 | label_Hcc | label_Zqq |
| 14 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.2851 | 58 | label_Hcc | label_Zqq |
| 15 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.2576 | 91 | label_Hcc | label_Zqq |
| 16 | classifier_dim:fc_dim_54 | classifier:mod.fc | -0.2532 | 54 | label_Hcc | label_Zqq |
| 17 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.2272 | 96 | label_Hcc | label_Zqq |
| 18 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.2234 | 123 | label_Hcc | label_Zqq |
| 19 | classifier_dim:fc_dim_103 | classifier:mod.fc | -0.1691 | 103 | label_Hcc | label_Zqq |
| 20 | classifier_dim:fc_dim_34 | classifier:mod.fc | 0.0480 | 34 | label_Hcc | label_Zqq |
| 21 | classifier_dim:fc_dim_80 | classifier:mod.fc | -0.0283 | 80 | label_Hcc | label_Zqq |
| 22 | classifier_dim:fc_dim_6 | classifier:mod.fc | 0.0183 | 6 | label_Hcc | label_Zqq |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0164 | 110 | label_Hcc | label_Zqq |
| 24 | classifier_dim:fc_dim_124 | classifier:mod.fc | -9.467e-04 | 124 | label_Hcc | label_Zqq |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
