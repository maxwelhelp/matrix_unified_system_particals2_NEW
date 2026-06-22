# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **134**
- edges: **203**
- src_label: `label_Hbb`
- tgt_label: `label_H4q`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 70, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 8, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.5688 | 0.0000 | down | 0 | 0.4867 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -1.863e-07 | 0.0000 | down | 0 | -3.725e-08 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | -1.863e-07 | 0.0000 | down | 0 | -3.725e-08 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -1.863e-07 | 0.0000 | down | 0 | -3.725e-08 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -1.863e-07 | 0.0000 | down | 0 | -3.725e-08 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h6|CLS<-CLS | residual_block:mod.cls_blocks.0 | -1.863e-07 | 0.0000 | down | 0 | -3.725e-08 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h0|neutral_hadron<-CLS | residual_block:mod.cls_blocks.0 | -1.863e-07 | 0.0000 | down | 0 | -3.725e-08 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h0|CLS<-CLS | residual_block:mod.cls_blocks.0 | -1.863e-07 | 0.0000 | down | 0 | -3.725e-08 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.5248 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.5046 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.4217 | signed_hqql_tbl | A_Hqql_correct |
| 4 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.3638 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3494 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.3065 | signed_hqql_tbl | A_Hqql_correct |
| 7 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2725 | signed_hqql_tbl | C_Tbl_correct |
| 8 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2667 | signed_hqql_tbl | C_Tbl_correct |
| 9 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2511 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 10 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2511 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 11 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2275 | signed_hqql_tbl | A_Hqql_correct |
| 12 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1896 | signed_hqql_tbl | C_Tbl_correct |
| 13 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1704 | signed_hqql_tbl | A_Hqql_correct |
| 14 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1644 | signed_hqql_tbl | A_Hqql_correct |
| 15 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1616 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 16 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1616 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 17 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1450 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1450 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 19 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1415 | signed_hqql_tbl | A_Hqql_correct |
| 20 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1283 | signed_hqql_tbl | C_Tbl_correct |
| 21 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1227 | signed_hqql_tbl | A_Hqql_correct |
| 22 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1223 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1171 | signed_hqql_tbl | A_Hqql_correct |
| 24 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1116 | signed_hqql_tbl | C_Tbl_correct |
| 25 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1054 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 26 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0787 | signed_hqql_tbl | C_Tbl_correct |
| 27 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0723 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 28 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0723 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0703 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 30 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0686 | signed_hqql_tbl | C_Tbl_correct |
| 31 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0645 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 32 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0628 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0628 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.0596 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 35 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0542 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 36 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0406 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 37 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0406 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0403 | signed_hqql_tbl | C_Tbl_correct |
| 39 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0396 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 40 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0396 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_8 | classifier:mod.fc | -1.4492 | 8 | label_Hbb | label_H4q |
| 2 | classifier_dim:fc_dim_57 | classifier:mod.fc | -1.2713 | 57 | label_Hbb | label_H4q |
| 3 | classifier_dim:fc_dim_121 | classifier:mod.fc | 1.0397 | 121 | label_Hbb | label_H4q |
| 4 | classifier_dim:fc_dim_10 | classifier:mod.fc | 1.0307 | 10 | label_Hbb | label_H4q |
| 5 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.8452 | 79 | label_Hbb | label_H4q |
| 6 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.7216 | 45 | label_Hbb | label_H4q |
| 7 | classifier_dim:fc_dim_76 | classifier:mod.fc | -0.5701 | 76 | label_Hbb | label_H4q |
| 8 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.4859 | 3 | label_Hbb | label_H4q |
| 9 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.3812 | 2 | label_Hbb | label_H4q |
| 10 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.3016 | 23 | label_Hbb | label_H4q |
| 11 | classifier_dim:fc_dim_124 | classifier:mod.fc | -0.2827 | 124 | label_Hbb | label_H4q |
| 12 | classifier_dim:fc_dim_91 | classifier:mod.fc | -0.2561 | 91 | label_Hbb | label_H4q |
| 13 | classifier_dim:fc_dim_103 | classifier:mod.fc | -0.2504 | 103 | label_Hbb | label_H4q |
| 14 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.2109 | 82 | label_Hbb | label_H4q |
| 15 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.1526 | 123 | label_Hbb | label_H4q |
| 16 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.1324 | 96 | label_Hbb | label_H4q |
| 17 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.1174 | 54 | label_Hbb | label_H4q |
| 18 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.1028 | 58 | label_Hbb | label_H4q |
| 19 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.0744 | 66 | label_Hbb | label_H4q |
| 20 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0421 | 6 | label_Hbb | label_H4q |
| 21 | classifier_dim:fc_dim_34 | classifier:mod.fc | -0.0271 | 34 | label_Hbb | label_H4q |
| 22 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.0230 | 18 | label_Hbb | label_H4q |
| 23 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0150 | 80 | label_Hbb | label_H4q |
| 24 | classifier_dim:fc_dim_78 | classifier:mod.fc | 3.448e-04 | 78 | label_Hbb | label_H4q |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
