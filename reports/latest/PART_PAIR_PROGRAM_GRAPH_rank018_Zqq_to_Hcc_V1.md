# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **129**
- edges: **207**
- src_label: `label_Zqq`
- tgt_label: `label_Hcc`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_cls': 2, 'residual_particle': 8, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 65, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 12, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.7533 | 0.0000 | up | 0 | 0.6880 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-charged_hadron | residual_block:mod.cls_blocks.0 | 0.7186 | 0.0000 | up | 0 | 0.2928 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | -0.3000 | 0.0000 | down | 0 | 0.2525 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.1982 | 0.0000 | down | 0 | 0.1513 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-charged_hadron | residual_block:mod.cls_blocks.0 | -0.4441 | 0.0000 | down | 0 | 0.1147 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h1|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0274 | 0.0000 | down | 0 | 0.0200 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h1|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.0923 | 0.0000 | up | 0 | 0.0128 |
| 8 | attention_pair:mod.cls_blocks.1.attn.h2|charged_hadron<-CLS | residual_block:mod.cls_blocks.1 | -7.823e-08 | 0.0000 | down | 0 | -2.421e-08 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-CLS | residual_block:mod.cls_blocks.0 | -7.823e-08 | 0.0000 | up | 0 | -2.421e-08 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | -7.823e-08 | 0.0000 | up | 0 | -2.421e-08 |
| 11 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.823e-08 | 0.0000 | up | 0 | -2.421e-08 |
| 12 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | 0.1293 | 0.0000 | up | 0 | -0.1584 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.5416 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.4528 | signed_hqql_tbl | C_Tbl_correct |
| 3 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2698 | signed_hqql_tbl | A_Hqql_correct |
| 4 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2419 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2195 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 6 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2195 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 7 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.2180 | signed_hqql_tbl | A_Hqql_correct |
| 8 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2171 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1800 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 10 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1800 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 11 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1461 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1409 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1322 | signed_hqql_tbl | A_Hqql_correct |
| 14 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1178 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 15 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1169 | signed_hqql_tbl | A_Hqql_correct |
| 16 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1054 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 17 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1054 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1041 | signed_hqql_tbl | C_Tbl_correct |
| 19 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0994 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 20 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0994 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0908 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 22 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0888 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0732 | signed_hqql_tbl | C_Tbl_correct |
| 24 | residual_particle:mod.blocks.7 | classifier:mod.fc | -0.0718 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 25 | residual_particle:mod.blocks.7 | classifier:mod.fc | -0.0718 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 26 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0715 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0659 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 28 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0651 | signed_hqql_tbl | C_Tbl_correct |
| 29 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0534 | signed_hqql_tbl | A_Hqql_correct |
| 30 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0516 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 31 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0438 | signed_hqql_tbl | C_Tbl_correct |
| 32 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0396 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 33 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0352 | signed_hqql_tbl | A_Hqql_correct |
| 34 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0272 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0272 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0205 | signed_hqql_tbl | C_Tbl_correct |
| 37 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0197 | signed_hqql_tbl | C_Tbl_correct |
| 38 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0196 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 39 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0175 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 40 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0175 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_79 | classifier:mod.fc | 1.0130 | 79 | label_Zqq | label_Hcc |
| 2 | classifier_dim:fc_dim_10 | classifier:mod.fc | -0.9938 | 10 | label_Zqq | label_Hcc |
| 3 | classifier_dim:fc_dim_8 | classifier:mod.fc | -0.9532 | 8 | label_Zqq | label_Hcc |
| 4 | classifier_dim:fc_dim_2 | classifier:mod.fc | -0.8505 | 2 | label_Zqq | label_Hcc |
| 5 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.7085 | 66 | label_Zqq | label_Hcc |
| 6 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.7051 | 121 | label_Zqq | label_Hcc |
| 7 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.6072 | 45 | label_Zqq | label_Hcc |
| 8 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.5056 | 18 | label_Zqq | label_Hcc |
| 9 | classifier_dim:fc_dim_76 | classifier:mod.fc | 0.4996 | 76 | label_Zqq | label_Hcc |
| 10 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.3963 | 3 | label_Zqq | label_Hcc |
| 11 | classifier_dim:fc_dim_57 | classifier:mod.fc | 0.3537 | 57 | label_Zqq | label_Hcc |
| 12 | classifier_dim:fc_dim_23 | classifier:mod.fc | -0.3312 | 23 | label_Zqq | label_Hcc |
| 13 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.3028 | 82 | label_Zqq | label_Hcc |
| 14 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.2851 | 58 | label_Zqq | label_Hcc |
| 15 | classifier_dim:fc_dim_91 | classifier:mod.fc | -0.2576 | 91 | label_Zqq | label_Hcc |
| 16 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.2532 | 54 | label_Zqq | label_Hcc |
| 17 | classifier_dim:fc_dim_96 | classifier:mod.fc | -0.2272 | 96 | label_Zqq | label_Hcc |
| 18 | classifier_dim:fc_dim_123 | classifier:mod.fc | -0.2234 | 123 | label_Zqq | label_Hcc |
| 19 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.1691 | 103 | label_Zqq | label_Hcc |
| 20 | classifier_dim:fc_dim_34 | classifier:mod.fc | -0.0480 | 34 | label_Zqq | label_Hcc |
| 21 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0283 | 80 | label_Zqq | label_Hcc |
| 22 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0183 | 6 | label_Zqq | label_Hcc |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | 0.0164 | 110 | label_Zqq | label_Hcc |
| 24 | classifier_dim:fc_dim_124 | classifier:mod.fc | 9.467e-04 | 124 | label_Zqq | label_Hcc |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
