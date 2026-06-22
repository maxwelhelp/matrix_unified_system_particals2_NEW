# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **125**
- edges: **211**
- src_label: `label_Hcc`
- tgt_label: `label_Tbqq`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 63, 'classifier_activation_dim': 8}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 16, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h6|muon<-muon | residual_block:mod.cls_blocks.0 | -1.4327 | 0.0000 | up | 0 | 1.2224 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|muon<-muon | residual_block:mod.cls_blocks.0 | -0.7682 | 0.0000 | up | 0 | 0.6218 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|muon<-muon | residual_block:mod.cls_blocks.0 | 0.5805 | 0.0000 | down | 0 | 0.5186 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|muon<-charged_hadron | residual_block:mod.cls_blocks.0 | 0.5550 | 0.0000 | up | 0 | 0.4962 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-muon | residual_block:mod.cls_blocks.0 | 0.2730 | 0.0000 | up | 0 | 0.2552 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|muon<-charged_hadron | residual_block:mod.cls_blocks.0 | -0.2945 | 0.0000 | down | 0 | 0.2520 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|muon<-muon | residual_block:mod.cls_blocks.0 | 0.2376 | 0.0000 | down | 0 | 0.2153 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h7|muon<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.1528 | 0.0000 | up | 0 | 0.1335 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h7|electron<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.0439 | 0.0000 | up | 0 | 0.0439 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-electron | residual_block:mod.cls_blocks.0 | 0.0354 | 0.0000 | up | 0 | 0.0354 |
| 11 | attention_pair:mod.cls_blocks.0.attn.h7|muon<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0374 | 0.0000 | down | 0 | 0.0341 |
| 12 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-electron | residual_block:mod.cls_blocks.0 | -0.0174 | 0.0000 | down | 0 | 0.0174 |
| 13 | attention_pair:mod.cls_blocks.0.attn.h7|electron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0106 | 0.0000 | down | 0 | 0.0106 |
| 14 | attention_pair:mod.blocks.6.attn.h1|muon<-electron | residual_block:mod.blocks.6 | -0.0066 | 0.0000 | down | 0 | 0.0065 |
| 15 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-muon | residual_block:mod.cls_blocks.0 | -0.0069 | 0.0000 | down | 0 | 0.0065 |
| 16 | attention_pair:mod.blocks.6.attn.h1|muon<-electron | residual_block:mod.blocks.6 | 0.0043 | 0.0000 | up | 0 | 0.0041 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.6188 | signed_hqql_tbl | A_Hqql_correct |
| 2 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.4945 | signed_hqql_tbl | C_Tbl_correct |
| 3 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.4435 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3797 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3772 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.3142 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 7 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3095 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 8 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2685 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.2594 | signed_hqql_tbl | A_Hqql_correct |
| 10 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2551 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2293 | signed_hqql_tbl | A_Hqql_correct |
| 12 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1919 | signed_hqql_tbl | C_Tbl_correct |
| 13 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1855 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 14 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1814 | signed_hqql_tbl | A_Hqql_correct |
| 15 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1759 | signed_hqql_tbl | C_Tbl_correct |
| 16 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1660 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 17 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1586 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1586 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 19 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1478 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 20 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1465 | signed_hqql_tbl | C_Tbl_correct |
| 21 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1354 | signed_hqql_tbl | A_Hqql_correct |
| 22 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1352 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 23 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1332 | signed_hqql_tbl | C_Tbl_correct |
| 24 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1245 | signed_hqql_tbl | C_Tbl_correct |
| 25 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.1027 | signed_hqql_tbl | C_Tbl_correct |
| 26 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0790 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0746 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 28 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0746 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 29 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0717 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 30 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0717 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 31 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0706 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0706 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0653 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0653 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0642 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0642 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 37 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0534 | signed_hqql_tbl | C_Tbl_correct |
| 38 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0495 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 39 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0322 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 40 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0297 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_103 | classifier:mod.fc | 1.2418 | 103 | label_Hcc | label_Tbqq |
| 2 | classifier_dim:fc_dim_121 | classifier:mod.fc | -1.1377 | 121 | label_Hcc | label_Tbqq |
| 3 | classifier_dim:fc_dim_34 | classifier:mod.fc | -1.0162 | 34 | label_Hcc | label_Tbqq |
| 4 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.9753 | 79 | label_Hcc | label_Tbqq |
| 5 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.9143 | 2 | label_Hcc | label_Tbqq |
| 6 | classifier_dim:fc_dim_3 | classifier:mod.fc | -0.8471 | 3 | label_Hcc | label_Tbqq |
| 7 | classifier_dim:fc_dim_8 | classifier:mod.fc | -0.6676 | 8 | label_Hcc | label_Tbqq |
| 8 | classifier_dim:fc_dim_66 | classifier:mod.fc | -0.5024 | 66 | label_Hcc | label_Tbqq |
| 9 | classifier_dim:fc_dim_124 | classifier:mod.fc | -0.4570 | 124 | label_Hcc | label_Tbqq |
| 10 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.4547 | 123 | label_Hcc | label_Tbqq |
| 11 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.3020 | 54 | label_Hcc | label_Tbqq |
| 12 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.2875 | 18 | label_Hcc | label_Tbqq |
| 13 | classifier_dim:fc_dim_45 | classifier:mod.fc | -0.2593 | 45 | label_Hcc | label_Tbqq |
| 14 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.2500 | 58 | label_Hcc | label_Tbqq |
| 15 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.2095 | 82 | label_Hcc | label_Tbqq |
| 16 | classifier_dim:fc_dim_76 | classifier:mod.fc | -0.1903 | 76 | label_Hcc | label_Tbqq |
| 17 | classifier_dim:fc_dim_96 | classifier:mod.fc | 0.0605 | 96 | label_Hcc | label_Tbqq |
| 18 | classifier_dim:fc_dim_10 | classifier:mod.fc | 0.0603 | 10 | label_Hcc | label_Tbqq |
| 19 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.0534 | 23 | label_Hcc | label_Tbqq |
| 20 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0485 | 6 | label_Hcc | label_Tbqq |
| 21 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.0216 | 91 | label_Hcc | label_Tbqq |
| 22 | classifier_dim:fc_dim_80 | classifier:mod.fc | -0.0194 | 80 | label_Hcc | label_Tbqq |
| 23 | classifier_dim:fc_dim_57 | classifier:mod.fc | -0.0192 | 57 | label_Hcc | label_Tbqq |
| 24 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0111 | 110 | label_Hcc | label_Tbqq |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
