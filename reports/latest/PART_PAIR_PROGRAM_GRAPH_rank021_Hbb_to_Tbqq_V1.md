# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **134**
- edges: **205**
- src_label: `label_Hbb`
- tgt_label: `label_Tbqq`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 71, 'classifier_activation_dim': 9}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 10, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.8494 | 0.0000 | up | 0 | 0.4782 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h2|charged_hadron<-muon | residual_block:mod.cls_blocks.0 | -0.0866 | 0.0000 | up | 0 | 0.0390 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h2|charged_hadron<-muon | residual_block:mod.cls_blocks.0 | 0.0042 | 0.0000 | down | 0 | 0.0034 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h7|charged_hadron<-muon | residual_block:mod.cls_blocks.0 | -0.0016 | 0.0000 | down | 0 | 0.0011 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h0|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.490e-08 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h0|CLS<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | up | 0 | 1.490e-08 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | down | 0 | 1.490e-08 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | down | 0 | 1.490e-08 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | 2.831e-07 | 0.0000 | down | 0 | 1.490e-08 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h7|charged_hadron<-muon | residual_block:mod.cls_blocks.0 | 0.0467 | 0.0000 | up | 0 | -0.0510 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.4709 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.4649 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3889 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3310 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3153 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.2353 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 7 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2112 | signed_hqql_tbl | A_Hqql_correct |
| 8 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2074 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1696 | signed_hqql_tbl | A_Hqql_correct |
| 10 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1558 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1489 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1359 | signed_hqql_tbl | C_Tbl_correct |
| 13 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1336 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 14 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1322 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 15 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1320 | signed_hqql_tbl | A_Hqql_correct |
| 16 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1266 | signed_hqql_tbl | C_Tbl_correct |
| 17 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1261 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 18 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1246 | signed_hqql_tbl | C_Tbl_correct |
| 19 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1245 | signed_hqql_tbl | C_Tbl_correct |
| 20 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1210 | signed_hqql_tbl | C_Tbl_correct |
| 21 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.1021 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 22 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.1021 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0874 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 24 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0874 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 25 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0816 | signed_hqql_tbl | A_Hqql_correct |
| 26 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0777 | signed_hqql_tbl | C_Tbl_correct |
| 27 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0777 | signed_hqql_tbl | A_Hqql_correct |
| 28 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0767 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 29 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0623 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 30 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0570 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 31 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0570 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0489 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0489 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0457 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0457 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 36 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0404 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 37 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0404 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0389 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 39 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0334 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 40 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0334 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_8 | classifier:mod.fc | -1.5495 | 8 | label_Hbb | label_Tbqq |
| 2 | classifier_dim:fc_dim_34 | classifier:mod.fc | -1.1703 | 34 | label_Hbb | label_Tbqq |
| 3 | classifier_dim:fc_dim_3 | classifier:mod.fc | -1.0628 | 3 | label_Hbb | label_Tbqq |
| 4 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.8470 | 79 | label_Hbb | label_Tbqq |
| 5 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.8435 | 2 | label_Hbb | label_Tbqq |
| 6 | classifier_dim:fc_dim_66 | classifier:mod.fc | -0.5774 | 66 | label_Hbb | label_Tbqq |
| 7 | classifier_dim:fc_dim_121 | classifier:mod.fc | -0.4641 | 121 | label_Hbb | label_Tbqq |
| 8 | classifier_dim:fc_dim_57 | classifier:mod.fc | -0.3757 | 57 | label_Hbb | label_Tbqq |
| 9 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.3455 | 123 | label_Hbb | label_Tbqq |
| 10 | classifier_dim:fc_dim_124 | classifier:mod.fc | -0.3345 | 124 | label_Hbb | label_Tbqq |
| 11 | classifier_dim:fc_dim_76 | classifier:mod.fc | 0.3230 | 76 | label_Hbb | label_Tbqq |
| 12 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.2798 | 45 | label_Hbb | label_Tbqq |
| 13 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.2783 | 23 | label_Hbb | label_Tbqq |
| 14 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.1449 | 54 | label_Hbb | label_Tbqq |
| 15 | classifier_dim:fc_dim_103 | classifier:mod.fc | 0.1333 | 103 | label_Hbb | label_Tbqq |
| 16 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.1072 | 96 | label_Hbb | label_Tbqq |
| 17 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.0893 | 18 | label_Hbb | label_Tbqq |
| 18 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.0625 | 58 | label_Hbb | label_Tbqq |
| 19 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.0610 | 82 | label_Hbb | label_Tbqq |
| 20 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0469 | 6 | label_Hbb | label_Tbqq |
| 21 | classifier_dim:fc_dim_10 | classifier:mod.fc | -0.0425 | 10 | label_Hbb | label_Tbqq |
| 22 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0187 | 110 | label_Hbb | label_Tbqq |
| 23 | classifier_dim:fc_dim_80 | classifier:mod.fc | -0.0099 | 80 | label_Hbb | label_Tbqq |
| 24 | classifier_dim:fc_dim_91 | classifier:mod.fc | -0.0091 | 91 | label_Hbb | label_Tbqq |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
