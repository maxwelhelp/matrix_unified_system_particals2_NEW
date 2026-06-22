# PART_PROGRAM_GRAPH_EXPORT_V1

Machine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.

- nodes: **127**
- edges: **208**
- src_label: `label_Zqq`
- tgt_label: `label_Hbb`
- node_kinds: `{'objective': 1, 'classifier': 1, 'classifier_dim': 24, 'residual_cls': 2, 'residual_particle': 8, 'attention_pair': 8, 'residual_block': 9, 'residual_role': 64, 'classifier_activation_dim': 10}`
- edge_kinds: `{'classifier_to_objective': 1, 'linear_direction': 24, 'residual_to_classifier': 50, 'validated_pair_to_residual': 13, 'role_to_residual': 80, 'classifier_dim_observed': 40}`

## Top validated pair → residual edges
| rank | source | target | weight/B_delta | B_flip | action | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.5397 | 0.0000 | up | 0 | 0.3837 |
| 2 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | 0.6068 | 0.0000 | up | 0 | 0.3639 |
| 3 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | -0.4713 | 0.0000 | down | 0 | 0.3152 |
| 4 | attention_pair:mod.cls_blocks.0.attn.h1|neutral_hadron<-electron | residual_block:mod.cls_blocks.0 | 0.2124 | 0.0000 | up | 0 | 0.1867 |
| 5 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-charged_hadron | residual_block:mod.cls_blocks.0 | 0.4614 | 0.0000 | up | 0 | 0.1683 |
| 6 | attention_pair:mod.cls_blocks.0.attn.h4|photon<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.1807 | 0.0000 | down | 0 | 0.1564 |
| 7 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-muon | residual_block:mod.cls_blocks.0 | 0.1731 | 0.0000 | up | 0 | 0.1479 |
| 8 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-neutral_hadron | residual_block:mod.cls_blocks.0 | -0.1440 | 0.0000 | down | 0 | 0.1357 |
| 9 | attention_pair:mod.cls_blocks.0.attn.h1|neutral_hadron<-electron | residual_block:mod.cls_blocks.0 | -0.0202 | 0.0000 | down | 0 | 0.0196 |
| 10 | attention_pair:mod.cls_blocks.0.attn.h0|neutral_hadron<-electron | residual_block:mod.cls_blocks.0 | -0.0171 | 0.0000 | down | 0 | 0.0145 |
| 11 | attention_pair:mod.cls_blocks.0.attn.h4|neutral_hadron<-muon | residual_block:mod.cls_blocks.0 | -0.0122 | 0.0000 | down | 0 | 0.0119 |
| 12 | attention_pair:mod.cls_blocks.0.attn.h4|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.906e-07 | 0.0000 | down | 0 | 1.388e-07 |
| 13 | attention_pair:mod.cls_blocks.0.attn.h6|charged_hadron<-CLS | residual_block:mod.cls_blocks.0 | -2.906e-07 | 0.0000 | down | 0 | 1.388e-07 |

## Top residual → classifier edges
| rank | source | target | weight | objective | group |
| --- | --- | --- | --- | --- | --- |
| 1 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.6011 | signed_hqql_tbl | C_Tbl_correct |
| 2 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.5244 | signed_hqql_tbl | C_Tbl_correct |
| 3 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.2900 | signed_hqql_tbl | A_Hqql_correct |
| 4 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2716 | signed_hqql_tbl | A_Hqql_correct |
| 5 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.2443 | signed_hqql_tbl | A_Hqql_correct |
| 6 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2398 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 7 | residual_cls:mod.cls_blocks.0 | classifier:mod.fc | 0.2398 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 8 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.2147 | signed_hqql_tbl | A_Hqql_correct |
| 9 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1766 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 10 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.1766 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 11 | residual_particle:mod.blocks.7 | classifier:mod.fc | 0.1730 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 12 | residual_particle:mod.blocks.7 | classifier:mod.fc | -0.1593 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 13 | residual_particle:mod.blocks.7 | classifier:mod.fc | -0.1593 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 14 | residual_particle:mod.blocks.1 | classifier:mod.fc | -0.1188 | signed_hqql_tbl | A_Hqql_correct |
| 15 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.1143 | signed_hqql_tbl | A_Hqql_correct |
| 16 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1103 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 17 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.1103 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 18 | residual_particle:mod.blocks.2 | classifier:mod.fc | -0.1079 | signed_hqql_tbl | A_Hqql_correct |
| 19 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.1030 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 20 | residual_particle:mod.blocks.0 | classifier:mod.fc | 0.1030 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 21 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0891 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 22 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0816 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 23 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0816 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 24 | residual_particle:mod.blocks.6 | classifier:mod.fc | 0.0744 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 25 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0590 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 26 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0590 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 27 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0570 | signed_hqql_tbl | B_Hqql_to_Tbl |
| 28 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0570 | B_tbl_minus_hqql | B_Hqql_to_Tbl |
| 29 | residual_cls:mod.cls_blocks.1 | classifier:mod.fc | -0.0564 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 30 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0532 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 31 | residual_particle:mod.blocks.4 | classifier:mod.fc | 0.0522 | signed_hqql_tbl | A_Hqql_correct |
| 32 | residual_particle:mod.blocks.5 | classifier:mod.fc | 0.0517 | signed_hqql_tbl | A_Hqql_correct |
| 33 | residual_particle:mod.blocks.6 | classifier:mod.fc | -0.0506 | signed_hqql_tbl | C_Tbl_correct |
| 34 | residual_particle:mod.blocks.2 | classifier:mod.fc | 0.0461 | signed_hqql_tbl | C_Tbl_correct |
| 35 | residual_particle:mod.blocks.5 | classifier:mod.fc | -0.0452 | signed_hqql_tbl | C_Tbl_correct |
| 36 | residual_particle:mod.blocks.3 | classifier:mod.fc | -0.0440 | signed_hqql_tbl | A_Hqql_correct |
| 37 | residual_particle:mod.blocks.4 | classifier:mod.fc | -0.0402 | signed_hqql_tbl | C_Tbl_correct |
| 38 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0372 | signed_hqql_tbl | D_Tbl_to_Hqql |
| 39 | residual_particle:mod.blocks.7 | classifier:mod.fc | -0.0303 | signed_hqql_tbl | C_Tbl_correct |
| 40 | residual_particle:mod.blocks.0 | classifier:mod.fc | -0.0263 | signed_hqql_tbl | C_Tbl_correct |

## Top classifier linear directions
| rank | source | target | W_tgt-src | dim | src | tgt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | classifier_dim:fc_dim_103 | classifier:mod.fc | 1.2776 | 103 | label_Zqq | label_Hbb |
| 2 | classifier_dim:fc_dim_10 | classifier:mod.fc | -0.8910 | 10 | label_Zqq | label_Hbb |
| 3 | classifier_dim:fc_dim_79 | classifier:mod.fc | 0.8846 | 79 | label_Zqq | label_Hbb |
| 4 | classifier_dim:fc_dim_66 | classifier:mod.fc | 0.7835 | 66 | label_Zqq | label_Hbb |
| 5 | classifier_dim:fc_dim_2 | classifier:mod.fc | -0.7797 | 2 | label_Zqq | label_Hbb |
| 6 | classifier_dim:fc_dim_57 | classifier:mod.fc | 0.7103 | 57 | label_Zqq | label_Hbb |
| 7 | classifier_dim:fc_dim_18 | classifier:mod.fc | 0.7038 | 18 | label_Zqq | label_Hbb |
| 8 | classifier_dim:fc_dim_3 | classifier:mod.fc | 0.6121 | 3 | label_Zqq | label_Hbb |
| 9 | classifier_dim:fc_dim_23 | classifier:mod.fc | -0.5561 | 23 | label_Zqq | label_Hbb |
| 10 | classifier_dim:fc_dim_82 | classifier:mod.fc | 0.4513 | 82 | label_Zqq | label_Hbb |
| 11 | classifier_dim:fc_dim_54 | classifier:mod.fc | 0.4103 | 54 | label_Zqq | label_Hbb |
| 12 | classifier_dim:fc_dim_96 | classifier:mod.fc | -0.2739 | 96 | label_Zqq | label_Hbb |
| 13 | classifier_dim:fc_dim_91 | classifier:mod.fc | -0.2269 | 91 | label_Zqq | label_Hbb |
| 14 | classifier_dim:fc_dim_124 | classifier:mod.fc | -0.1215 | 124 | label_Zqq | label_Hbb |
| 15 | classifier_dim:fc_dim_123 | classifier:mod.fc | -0.1142 | 123 | label_Zqq | label_Hbb |
| 16 | classifier_dim:fc_dim_34 | classifier:mod.fc | 0.1061 | 34 | label_Zqq | label_Hbb |
| 17 | classifier_dim:fc_dim_8 | classifier:mod.fc | -0.0714 | 8 | label_Zqq | label_Hbb |
| 18 | classifier_dim:fc_dim_45 | classifier:mod.fc | 0.0681 | 45 | label_Zqq | label_Hbb |
| 19 | classifier_dim:fc_dim_121 | classifier:mod.fc | 0.0314 | 121 | label_Zqq | label_Hbb |
| 20 | classifier_dim:fc_dim_58 | classifier:mod.fc | -0.0273 | 58 | label_Zqq | label_Hbb |
| 21 | classifier_dim:fc_dim_110 | classifier:mod.fc | 0.0240 | 110 | label_Zqq | label_Hbb |
| 22 | classifier_dim:fc_dim_6 | classifier:mod.fc | -0.0198 | 6 | label_Zqq | label_Hbb |
| 23 | classifier_dim:fc_dim_80 | classifier:mod.fc | 0.0187 | 80 | label_Zqq | label_Hbb |
| 24 | classifier_dim:fc_dim_76 | classifier:mod.fc | -0.0138 | 76 | label_Zqq | label_Hbb |

## Graph formula

```text
attention_pair(h, q<-k) --validated_pair_to_residual--> residual_block
residual_block --residual_to_classifier--> classifier(fc)
classifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src
edge weights are signed causal/gradient/path contributions.
```
