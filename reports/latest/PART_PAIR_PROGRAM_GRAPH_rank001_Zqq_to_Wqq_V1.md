# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **129**
- edges: **205**
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_particle': 8, 'residual_cls': 2, 'attention_pair': 8, 'residual_block': 10, 'residual_role': 65, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 10, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | -1.3754 | 0.0000 | down | 0 | 0.9138 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-charged_hadron | residual_block:mod.cls_blocks.0 | -1.3155 | 0.0000 | down | 0 | 0.6299 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-photon | residual_block:mod.cls_blocks.0 | -0.6371 | 0.0000 | down | 0 | 0.3711 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.4505 | 0.0000 | up | 0 | 0.2616 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.3192 | 0.0000 | down | 0 | 0.2093 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|CLS<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.2110 | 0.0000 | down | 0 | 0.1483 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h6|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0963 | 0.0000 | down | 0 | 0.0556 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.0642 | 0.0000 | down | 0 | 0.0408 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h1|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0365 | 0.0000 | down | 0 | 0.0329 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h1|neutral_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.1211 | 0.0000 | up | 0 | -0.0640 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1531 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1498 | signed_hqql_tbl | C_Tbl_correct |
| 3 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1181 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 4 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1181 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 5 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1181 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 6 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1181 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 7 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1149 | signed_hqql_tbl | A_Hqql_correct |
| 8 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1010 | signed_hqql_tbl | C_Tbl_correct |
| 9 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0960 | signed_hqql_tbl | A_Hqql_correct |
| 10 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0944 | signed_hqql_tbl | A_Hqql_correct |
| 11 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0926 | signed_hqql_tbl | A_Hqql_correct |
| 12 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0909 | signed_hqql_tbl | A_Hqql_correct |
| 13 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0896 | signed_hqql_tbl | A_Hqql_correct |
| 14 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0879 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 15 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0810 | signed_hqql_tbl | A_Hqql_correct |
| 16 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0759 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 17 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0707 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 18 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0689 | signed_hqql_tbl | A_Hqql_correct |
| 19 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0520 | signed_hqql_tbl | C_Tbl_correct |
| 20 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0511 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0511 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 22 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0507 | signed_hqql_tbl | C_Tbl_correct |
| 23 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0477 | signed_hqql_tbl | C_Tbl_correct |
| 24 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0474 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 25 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0474 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 26 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0473 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 27 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0464 | signed_hqql_tbl | C_Tbl_correct |
| 28 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.0463 | signed_hqql_tbl | A_Hqql_correct |
| 29 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0430 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 30 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0430 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 31 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0357 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0357 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0346 | signed_hqql_tbl | C_Tbl_correct |
| 34 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0333 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 35 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0293 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 36 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0293 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 37 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0211 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 38 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.0186 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 39 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0150 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 40 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0146 | signed_hqql_tbl | B_Hqql_to_Tbl |

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
