# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **133**
- edges: **204**
- src_label: `label_Zqq`
- tgt_label: `label_H4q`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 69, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 9, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-electron | residual_block:mod.cls_blocks.0 | 0.1522 | 0.0000 | up | 0 | 0.1403 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-electron | residual_block:mod.cls_blocks.0 | -0.0093 | 0.0000 | down | 0 | 0.0084 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -2.347e-07 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -2.347e-07 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -2.347e-07 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -2.347e-07 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -2.347e-07 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -2.347e-07 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -7.451e-09 | 0.0000 | up | 0 | -2.347e-07 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.3564 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3477 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3282 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2898 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2663 | signed_hqql_tbl | C_Tbl_correct |
| 6 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2374 | signed_hqql_tbl | C_Tbl_correct |
| 7 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2235 | signed_hqql_tbl | A_Hqql_correct |
| 8 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1996 | signed_hqql_tbl | C_Tbl_correct |
| 9 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1565 | signed_hqql_tbl | C_Tbl_correct |
| 10 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1504 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1503 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1337 | signed_hqql_tbl | C_Tbl_correct |
| 13 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1265 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 14 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1265 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 15 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1245 | signed_hqql_tbl | C_Tbl_correct |
| 16 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1178 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 17 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1126 | signed_hqql_tbl | A_Hqql_correct |
| 18 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1024 | signed_hqql_tbl | A_Hqql_correct |
| 19 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0969 | signed_hqql_tbl | A_Hqql_correct |
| 20 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0926 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0926 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 22 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0668 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 23 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0615 | signed_hqql_tbl | A_Hqql_correct |
| 24 | residual_particle:mod.blocks.1 | classifier:mod.fc | 0.0568 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 25 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0513 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 26 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0513 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 27 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0498 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 28 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0411 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0411 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 30 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0323 | signed_hqql_tbl | A_Hqql_correct |
| 31 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0304 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0304 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 33 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0295 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 34 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0295 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0240 | signed_hqql_tbl | C_Tbl_correct |
| 36 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0200 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 37 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0200 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0199 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 39 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0199 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 40 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0187 | signed_hqql_tbl | A_Hqql_correct |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_8 | classifier:mod.fc | -1.5206 | 8 | label_Zqq | label_H4q |
| 2 | classifier_dim:fc_dim_3 | classifier:mod.fc | 1.0979 | 3 | label_Zqq | label_H4q |
| 3 | classifier_dim:fc_dim_121 | classifier:mod.fc | 1.0711 | 121 | label_Zqq | label_H4q |
| 4 | classifier_dim:fc_dim_103 | classifier:mod.fc | 1.0272 | 103 | label_Zqq | label_H4q |
| 5 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.8579 | 66 | label_Zqq | label_H4q |
| 6 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.7896 | 45 | label_Zqq | label_H4q |
| 7 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.7268 | 18 | label_Zqq | label_H4q |
| 8 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.6622 | 82 | label_Zqq | label_H4q |
| 9 | classifier_dim:fc_dim_76 | classifier:mod.fc | -0.5838 | 76 | label_Zqq | label_H4q |
| 10 | classifier_dim:fc_dim_57 | classifier:mod.fc | -0.5611 | 57 | label_Zqq | label_H4q |
| 11 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.5277 | 54 | label_Zqq | label_H4q |
| 12 | classifier_dim:fc_dim_91 | classifier:mod.fc | -0.4830 | 91 | label_Zqq | label_H4q |
| 13 | classifier_dim:fc_dim_124 | classifier:mod.fc | -0.4042 | 124 | label_Zqq | label_H4q |
| 14 | classifier_dim:fc_dim_2 | classifier:mod.fc | -0.3984 | 2 | label_Zqq | label_H4q |
| 15 | classifier_dim:fc_dim_23 | classifier:mod.fc | -0.2544 | 23 | label_Zqq | label_H4q |
| 16 | classifier_dim:fc_dim_96 | classifier:mod.fc | -0.1415 | 96 | label_Zqq | label_H4q |
| 17 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.1396 | 10 | label_Zqq | label_H4q |
| 18 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.1301 | 58 | label_Zqq | label_H4q |
| 19 | classifier_dim:fc_dim_34 | classifier:mod.fc | 0.0790 | 34 | label_Zqq | label_H4q |
| 20 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0619 | 6 | label_Zqq | label_H4q |
| 21 | classifier_dim:fc_dim_79 | classifier:mod.fc | 0.0395 | 79 | label_Zqq | label_H4q |
| 22 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.0384 | 123 | label_Zqq | label_H4q |
| 23 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0337 | 80 | label_Zqq | label_H4q |
| 24 | classifier_dim:fc_dim_110 | classifier:mod.fc | 0.0242 | 110 | label_Zqq | label_H4q |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
