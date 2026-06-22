# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **130**
- edges: **203**
- src_label: `label_Hgg`
- tgt_label: `label_Zqq`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_cls': 2, 'residual_particle': 8, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 66, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 8, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.071e-07 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.071e-07 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.071e-07 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h6|photon<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.071e-07 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.071e-07 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.071e-07 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.071e-07 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.071e-07 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3708 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3356 | signed_hqql_tbl | C_Tbl_correct |
| 3 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3071 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2856 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1454 | signed_hqql_tbl | C_Tbl_correct |
| 6 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1293 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 7 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1293 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 8 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1214 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1192 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 10 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1192 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 11 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.1128 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1054 | signed_hqql_tbl | C_Tbl_correct |
| 13 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1047 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 14 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1047 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 15 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0982 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 16 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0982 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 17 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0880 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 18 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0828 | signed_hqql_tbl | A_Hqql_correct |
| 19 | residual_particle:mod.blocks.7 | classifier:mod.fc | -0.0804 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 20 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0744 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0744 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 22 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0728 | signed_hqql_tbl | A_Hqql_correct |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0715 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 24 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0666 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 25 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0609 | signed_hqql_tbl | C_Tbl_correct |
| 26 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0582 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0576 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 28 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0576 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0551 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 30 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0551 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 31 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0531 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 32 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0522 | signed_hqql_tbl | C_Tbl_correct |
| 33 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0501 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0501 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0496 | signed_hqql_tbl | C_Tbl_correct |
| 36 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0452 | signed_hqql_tbl | A_Hqql_correct |
| 37 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0449 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0449 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 39 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0439 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 40 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0387 | signed_hqql_tbl | C_Tbl_correct |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_66 | classifier:mod.fc | -1.1556 | 66 | label_Hgg | label_Zqq |
| 2 | classifier_dim:fc_dim_103 | classifier:mod.fc | -1.1520 | 103 | label_Hgg | label_Zqq |
| 3 | classifier_dim:fc_dim_121 | classifier:mod.fc | -1.1177 | 121 | label_Hgg | label_Zqq |
| 4 | classifier_dim:fc_dim_57 | classifier:mod.fc | 0.9398 | 57 | label_Hgg | label_Zqq |
| 5 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.8788 | 79 | label_Hgg | label_Zqq |
| 6 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.7910 | 10 | label_Hgg | label_Zqq |
| 7 | classifier_dim:fc_dim_82 | classifier:mod.fc | -0.6747 | 82 | label_Hgg | label_Zqq |
| 8 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.5436 | 8 | label_Hgg | label_Zqq |
| 9 | classifier_dim:fc_dim_76 | classifier:mod.fc | 0.4859 | 76 | label_Hgg | label_Zqq |
| 10 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.4724 | 2 | label_Hgg | label_Zqq |
| 11 | classifier_dim:fc_dim_18 | classifier:mod.fc | -0.3737 | 18 | label_Hgg | label_Zqq |
| 12 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.3478 | 3 | label_Hgg | label_Zqq |
| 13 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.2553 | 91 | label_Hgg | label_Zqq |
| 14 | classifier_dim:fc_dim_54 | classifier:mod.fc | -0.2073 | 54 | label_Hgg | label_Zqq |
| 15 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.2003 | 58 | label_Hgg | label_Zqq |
| 16 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.1988 | 96 | label_Hgg | label_Zqq |
| 17 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.1895 | 23 | label_Hgg | label_Zqq |
| 18 | classifier_dim:fc_dim_6 | classifier:mod.fc | 0.0604 | 6 | label_Hgg | label_Zqq |
| 19 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.0585 | 124 | label_Hgg | label_Zqq |
| 20 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.0502 | 45 | label_Hgg | label_Zqq |
| 21 | classifier_dim:fc_dim_80 | classifier:mod.fc | -0.0359 | 80 | label_Hgg | label_Zqq |
| 22 | classifier_dim:fc_dim_123 | classifier:mod.fc | -0.0333 | 123 | label_Hgg | label_Zqq |
| 23 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0136 | 110 | label_Hgg | label_Zqq |
| 24 | classifier_dim:fc_dim_34 | classifier:mod.fc | 0.0011 | 34 | label_Hgg | label_Zqq |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
