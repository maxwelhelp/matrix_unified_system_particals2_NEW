# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **133**
- edges: **219**
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_cls': 2, 'residual_particle': 8, 'attention_pair': 12, 'residual_block': 8, 'residual_role': 67, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 24, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|electron<-electron | residual_block:mod.cls_blocks.0 | -1.1925 | -0.3750 | up | 0 | 1.2180 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-electron | residual_block:mod.cls_blocks.0 | -1.0486 | -0.4062 | up | 0 | 1.0916 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|muon<-muon | residual_block:mod.cls_blocks.0 | -1.1249 | -0.3438 | up | 0 | 0.8288 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|muon<-muon | residual_block:mod.cls_blocks.0 | 1.0003 | 0.0000 | down | 0 | 0.5953 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|electron<-electron | residual_block:mod.cls_blocks.0 | 0.9589 | 0.0000 | down | 0 | 0.4238 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-electron | residual_block:mod.cls_blocks.0 | 0.9461 | 0.0000 | down | 0 | 0.4224 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-charged_hadron | residual_block:mod.cls_blocks.0 | 0.3823 | 0.0000 | up | 0 | 0.3639 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.2301 | 0.0000 | up | 0 | 0.2140 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-charged_hadron | residual_block:mod.cls_blocks.0 | -0.1109 | -0.0625 | down | 0 | 0.1948 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h4|electron<-muon | residual_block:mod.cls_blocks.0 | 0.1421 | 0.0000 | up | 0 | 0.0724 |
| 11 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0366 | 0.0000 | down | 0 | 0.0340 |
| 12 | attention_pair:mod.blocks.7.attn.h3|charged_hadron<-electron | residual_block:mod.blocks.7 | -0.0682 | 0.0000 | up | 2 | 0.0291 |
| 13 | attention_pair:mod.cls_blocks.0.attn.h7|charged_hadron<-muon | residual_block:mod.cls_blocks.0 | 0.0257 | 0.0000 | up | 0 | 0.0145 |
| 14 | attention_pair:mod.blocks.7.attn.h3|charged_hadron<-electron | residual_block:mod.blocks.7 | 0.0402 | 0.0000 | down | 2 | 0.0131 |
| 15 | attention_pair:mod.cls_blocks.0.attn.h1|charged_hadron<-photon | residual_block:mod.cls_blocks.0 | 0.0554 | 0.0000 | up | 0 | 0.0124 |
| 16 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | -0.0391 | 0.0000 | up | 0 | 0.0104 |
| 17 | attention_pair:mod.cls_blocks.0.attn.h1|charged_hadron<-photon | residual_block:mod.cls_blocks.0 | -0.0126 | 0.0000 | down | 0 | 0.0080 |
| 18 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | 0.0564 | 0.0000 | down | 0 | 0.0064 |
| 19 | attention_pair:mod.blocks.7.attn.h3|muon<-electron | residual_block:mod.blocks.7 | 0.0036 | 0.0000 | down | 2 | 0.0034 |
| 20 | attention_pair:mod.cls_blocks.0.attn.h7|charged_hadron<-muon | residual_block:mod.cls_blocks.0 | -0.0027 | 0.0000 | down | 0 | 0.0021 |
| 21 | attention_pair:mod.blocks.7.attn.h3|electron<-muon | residual_block:mod.blocks.7 | 6.216e-04 | 0.0000 | down | 2 | 4.860e-04 |
| 22 | attention_pair:mod.blocks.7.attn.h3|muon<-electron | residual_block:mod.blocks.7 | -0.0017 | 0.0000 | up | 2 | -3.521e-04 |
| 23 | attention_pair:mod.blocks.7.attn.h3|electron<-muon | residual_block:mod.blocks.7 | -0.0033 | 0.0000 | up | 2 | -5.942e-04 |
| 24 | attention_pair:mod.cls_blocks.0.attn.h4|electron<-muon | residual_block:mod.cls_blocks.0 | -0.0059 | 0.0000 | down | 0 | -0.0136 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3406 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.3089 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2487 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2343 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.2268 | signed_hqql_tbl | C_Tbl_correct |
| 6 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1974 | signed_hqql_tbl | A_Hqql_correct |
| 7 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1905 | signed_hqql_tbl | A_Hqql_correct |
| 8 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1795 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1484 | signed_hqql_tbl | C_Tbl_correct |
| 10 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1444 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1197 | signed_hqql_tbl | C_Tbl_correct |
| 12 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0907 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0714 | signed_hqql_tbl | C_Tbl_correct |
| 14 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0711 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 15 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0711 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 16 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0675 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 17 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0671 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 18 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0671 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 19 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0650 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 20 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0650 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0649 | signed_hqql_tbl | A_Hqql_correct |
| 22 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0595 | signed_hqql_tbl | C_Tbl_correct |
| 23 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0397 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 24 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0369 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 25 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0369 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 26 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0345 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0339 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 28 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0304 | signed_hqql_tbl | C_Tbl_correct |
| 29 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0290 | signed_hqql_tbl | A_Hqql_correct |
| 30 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0275 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 31 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0249 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0249 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0242 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0242 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0190 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 36 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0168 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 37 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0161 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 38 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0161 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 39 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0143 | signed_hqql_tbl | A_Hqql_correct |
| 40 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0120 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_Tbl-Hqql | dim |
| --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_54 | classifier:mod.fc | -1.6964 | 54 |
| 2 | classifier_dim:fc_dim_76 | classifier:mod.fc | 1.4146 | 76 |
| 3 | classifier_dim:fc_dim_18 | classifier:mod.fc | -1.2686 | 18 |
| 4 | classifier_dim:fc_dim_103 | classifier:mod.fc | 1.2515 | 103 |
| 5 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.9775 | 121 |
| 6 | classifier_dim:fc_dim_96 | classifier:mod.fc | -0.7730 | 96 |
| 7 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.5745 | 58 |
| 8 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.5696 | 23 |
| 9 | classifier_dim:fc_dim_45 | classifier:mod.fc | -0.4822 | 45 |
| 10 | classifier_dim:fc_dim_57 | classifier:mod.fc | 0.4719 | 57 |
| 11 | classifier_dim:fc_dim_10 | classifier:mod.fc | -0.3489 | 10 |
| 12 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.2327 | 8 |
| 13 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.2039 | 2 |
| 14 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.1842 | 91 |
| 15 | classifier_dim:fc_dim_34 | classifier:mod.fc | -0.1708 | 34 |
| 16 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.1077 | 79 |
| 17 | classifier_dim:fc_dim_6 | classifier:mod.fc | 0.0887 | 6 |
| 18 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.0838 | 66 |
| 19 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.0658 | 3 |
| 20 | classifier_dim:fc_dim_80 | classifier:mod.fc | -0.0510 | 80 |
| 21 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0399 | 110 |
| 22 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.0129 | 123 |
| 23 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.0039 | 124 |
| 24 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.0031 | 82 |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=Tbl-Hqql
edge weights are signed causal/gradient/path contributions.
```
