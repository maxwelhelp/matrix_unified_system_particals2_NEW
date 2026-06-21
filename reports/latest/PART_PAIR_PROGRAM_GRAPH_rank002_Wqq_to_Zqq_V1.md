# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **124**
- edges: **208**
- src_label: `label_Wqq`
- tgt_label: `label_Zqq`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 9, 'residual_role': 61, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 13, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | -0.7199 | 0.0000 | down | 0 | 0.5616 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-photon | residual_block:mod.cls_blocks.0 | -0.6279 | 0.0000 | down | 0 | 0.5153 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.6431 | 0.0000 | up | 0 | 0.4319 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | 0.4370 | 0.0000 | up | 0 | 0.3175 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-photon | residual_block:mod.cls_blocks.0 | 0.4671 | 0.0000 | up | 0 | 0.2891 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.4240 | 0.0000 | down | 0 | 0.2754 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h0|charged_hadron<-muon | residual_block:mod.cls_blocks.0 | 0.1020 | 0.0000 | up | 0 | 0.1020 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h0|CLS<-muon | residual_block:mod.cls_blocks.0 | 0.1158 | 0.0000 | up | 0 | 0.0104 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h0|charged_hadron<-muon | residual_block:mod.cls_blocks.0 | -0.0101 | 0.0000 | down | 0 | 0.0101 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h0|CLS<-muon | residual_block:mod.cls_blocks.0 | -0.0108 | 0.0000 | down | 0 | 0.0060 |
| 11 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.682e-07 | 0.0000 | up | 0 | 2.114e-07 |
| 12 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | -2.682e-07 | 0.0000 | up | 0 | 2.114e-07 |
| 13 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.682e-07 | 0.0000 | up | 0 | 2.114e-07 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0730 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0719 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0671 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0641 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0586 | signed_hqql_tbl | C_Tbl_correct |
| 6 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0535 | signed_hqql_tbl | C_Tbl_correct |
| 7 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0518 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 8 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0518 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 9 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0509 | signed_hqql_tbl | C_Tbl_correct |
| 10 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0497 | signed_hqql_tbl | C_Tbl_correct |
| 11 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0496 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 12 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0496 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 13 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0490 | signed_hqql_tbl | A_Hqql_correct |
| 14 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0425 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 15 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0425 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 16 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0422 | signed_hqql_tbl | C_Tbl_correct |
| 17 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0403 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0403 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 19 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0355 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 20 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0307 | signed_hqql_tbl | C_Tbl_correct |
| 21 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0293 | signed_hqql_tbl | A_Hqql_correct |
| 22 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0271 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 23 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0271 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 24 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0269 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 25 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0266 | signed_hqql_tbl | A_Hqql_correct |
| 26 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0248 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0225 | signed_hqql_tbl | C_Tbl_correct |
| 28 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0208 | signed_hqql_tbl | A_Hqql_correct |
| 29 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0182 | signed_hqql_tbl | A_Hqql_correct |
| 30 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0163 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 31 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0163 | signed_hqql_tbl | A_Hqql_correct |
| 32 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0148 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0148 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0130 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0130 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0121 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 37 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0110 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0110 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 39 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0097 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 40 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0097 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_18 | classifier:mod.fc | -1.4597 | 18 | label_Wqq | label_Zqq |
| 2 | classifier_dim:fc_dim_66 | classifier:mod.fc | -0.9041 | 66 | label_Wqq | label_Zqq |
| 3 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.7005 | 58 | label_Wqq | label_Zqq |
| 4 | classifier_dim:fc_dim_79 | classifier:mod.fc | 0.6879 | 79 | label_Wqq | label_Zqq |
| 5 | classifier_dim:fc_dim_82 | classifier:mod.fc | -0.6835 | 82 | label_Wqq | label_Zqq |
| 6 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.6741 | 96 | label_Wqq | label_Zqq |
| 7 | classifier_dim:fc_dim_121 | classifier:mod.fc | -0.3634 | 121 | label_Wqq | label_Zqq |
| 8 | classifier_dim:fc_dim_76 | classifier:mod.fc | -0.3524 | 76 | label_Wqq | label_Zqq |
| 9 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.3226 | 2 | label_Wqq | label_Zqq |
| 10 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.3137 | 10 | label_Wqq | label_Zqq |
| 11 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.2989 | 3 | label_Wqq | label_Zqq |
| 12 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.1311 | 8 | label_Wqq | label_Zqq |
| 13 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.1244 | 124 | label_Wqq | label_Zqq |
| 14 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.0845 | 23 | label_Wqq | label_Zqq |
| 15 | classifier_dim:fc_dim_54 | classifier:mod.fc | -0.0786 | 54 | label_Wqq | label_Zqq |
| 16 | classifier_dim:fc_dim_57 | classifier:mod.fc | -0.0668 | 57 | label_Wqq | label_Zqq |
| 17 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.0419 | 91 | label_Wqq | label_Zqq |
| 18 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.0383 | 103 | label_Wqq | label_Zqq |
| 19 | classifier_dim:fc_dim_34 | classifier:mod.fc | -0.0295 | 34 | label_Wqq | label_Zqq |
| 20 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.0148 | 45 | label_Wqq | label_Zqq |
| 21 | classifier_dim:fc_dim_123 | classifier:mod.fc | -0.0117 | 123 | label_Wqq | label_Zqq |
| 22 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0095 | 80 | label_Wqq | label_Zqq |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | 0.0027 | 110 | label_Wqq | label_Zqq |
| 24 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0026 | 6 | label_Wqq | label_Zqq |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
