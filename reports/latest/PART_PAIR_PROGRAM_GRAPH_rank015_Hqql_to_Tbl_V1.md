# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **126**
- edges: **201**
- src_label: `label_Hqql`
- tgt_label: `label_Tbl`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_cls': 2, 'residual_particle': 8, 'attention_pair': 3, 'residual_block': 9, 'residual_role': 68, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 6, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|muon<-muon | residual_block:mod.cls_blocks.0 | -1.4079 | -0.3750 | up | 0 | 1.0320 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|muon<-muon | residual_block:mod.cls_blocks.0 | 1.2846 | 0.0000 | down | 0 | 0.9410 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-charged_hadron | residual_block:mod.cls_blocks.0 | -0.1714 | -0.0625 | down | 0 | 0.2441 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.2564 | 0.0000 | up | 0 | 0.2327 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-charged_hadron | residual_block:mod.cls_blocks.0 | 0.2380 | 0.0000 | up | 0 | 0.2210 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.0520 | 0.0000 | down | 0 | 0.0500 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.7712 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.6055 | signed_hqql_tbl | A_Hqql_correct |
| 3 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.5364 | signed_hqql_tbl | C_Tbl_correct |
| 4 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.5124 | signed_hqql_tbl | C_Tbl_correct |
| 5 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.4979 | signed_hqql_tbl | C_Tbl_correct |
| 6 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.3875 | signed_hqql_tbl | A_Hqql_correct |
| 7 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.3438 | signed_hqql_tbl | C_Tbl_correct |
| 8 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.3391 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2816 | signed_hqql_tbl | A_Hqql_correct |
| 10 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.2726 | signed_hqql_tbl | C_Tbl_correct |
| 11 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.2036 | signed_hqql_tbl | A_Hqql_correct |
| 12 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1884 | signed_hqql_tbl | C_Tbl_correct |
| 13 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1832 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 14 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1442 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 15 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1442 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 16 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1408 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 17 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.1408 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1371 | signed_hqql_tbl | A_Hqql_correct |
| 19 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1244 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 20 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.1232 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 21 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1205 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 22 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1205 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 23 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.1162 | signed_hqql_tbl | C_Tbl_correct |
| 24 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0891 | signed_hqql_tbl | A_Hqql_correct |
| 25 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0889 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 26 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0889 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 27 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0835 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 28 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0798 | signed_hqql_tbl | C_Tbl_correct |
| 29 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.0750 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 30 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0617 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 31 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0560 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 32 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0560 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 33 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0534 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 34 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.0534 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 35 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0382 | signed_hqql_tbl | A_Hqql_correct |
| 36 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0381 | signed_hqql_tbl | C_Tbl_correct |
| 37 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0305 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 38 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0268 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 39 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0268 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 40 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0254 | B_tbl_minus_hqql | B_Hqql_to_Tbl |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_54 | classifier:mod.fc | -1.6964 | 54 | label_Hqql | label_Tbl |
| 2 | classifier_dim:fc_dim_76 | classifier:mod.fc | 1.4146 | 76 | label_Hqql | label_Tbl |
| 3 | classifier_dim:fc_dim_18 | classifier:mod.fc | -1.2686 | 18 | label_Hqql | label_Tbl |
| 4 | classifier_dim:fc_dim_103 | classifier:mod.fc | 1.2515 | 103 | label_Hqql | label_Tbl |
| 5 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.9775 | 121 | label_Hqql | label_Tbl |
| 6 | classifier_dim:fc_dim_96 | classifier:mod.fc | -0.7730 | 96 | label_Hqql | label_Tbl |
| 7 | classifier_dim:fc_dim_58 | classifier:mod.fc | 0.5745 | 58 | label_Hqql | label_Tbl |
| 8 | classifier_dim:fc_dim_23 | classifier:mod.fc | 0.5696 | 23 | label_Hqql | label_Tbl |
| 9 | classifier_dim:fc_dim_45 | classifier:mod.fc | -0.4822 | 45 | label_Hqql | label_Tbl |
| 10 | classifier_dim:fc_dim_57 | classifier:mod.fc | 0.4719 | 57 | label_Hqql | label_Tbl |
| 11 | classifier_dim:fc_dim_10 | classifier:mod.fc | -0.3489 | 10 | label_Hqql | label_Tbl |
| 12 | classifier_dim:fc_dim_8 | classifier:mod.fc | 0.2327 | 8 | label_Hqql | label_Tbl |
| 13 | classifier_dim:fc_dim_2 | classifier:mod.fc | 0.2039 | 2 | label_Hqql | label_Tbl |
| 14 | classifier_dim:fc_dim_91 | classifier:mod.fc | 0.1842 | 91 | label_Hqql | label_Tbl |
| 15 | classifier_dim:fc_dim_34 | classifier:mod.fc | -0.1708 | 34 | label_Hqql | label_Tbl |
| 16 | classifier_dim:fc_dim_79 | classifier:mod.fc | -0.1077 | 79 | label_Hqql | label_Tbl |
| 17 | classifier_dim:fc_dim_6 | classifier:mod.fc | 0.0887 | 6 | label_Hqql | label_Tbl |
| 18 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.0838 | 66 | label_Hqql | label_Tbl |
| 19 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.0658 | 3 | label_Hqql | label_Tbl |
| 20 | classifier_dim:fc_dim_80 | classifier:mod.fc | -0.0510 | 80 | label_Hqql | label_Tbl |
| 21 | classifier_dim:fc_dim_110 | classifier:mod.fc | -0.0399 | 110 | label_Hqql | label_Tbl |
| 22 | classifier_dim:fc_dim_123 | classifier:mod.fc | 0.0129 | 123 | label_Hqql | label_Tbl |
| 23 | classifier_dim:fc_dim_124 | classifier:mod.fc | 0.0039 | 124 | label_Hqql | label_Tbl |
| 24 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.0031 | 82 | label_Hqql | label_Tbl |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
