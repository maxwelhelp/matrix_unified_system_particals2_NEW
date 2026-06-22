# PART_PAIR_ATLAS_HEAD_ROLE_SUMMARY_V1

Aggregates generated pair program graphs into a head/role/classifier-dimension atlas. This is a model-level summary over pair-specific program graphs, not a new model run. Near-zero pair edges are filtered so numerical no-op routes do not look universal.

- pair_graphs: **20**
- min_abs_pair_weight: **0.001**
- kept_pair_edges: **91**
- skipped_pair_edges: **106**
- unique_heads: **6**
- unique_role_pairs: **16**
- unique_classifier_dims: **25**

## Universal / repeated heads
| rank | head | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | 16 | 58 | 0.4771 | -2.5652 | label_Hbb->label_Zqq |
| 2 | mod.cls_blocks.0.attn.h1 | 4 | 10 | 0.0685 | 0.2124 | label_Zqq->label_Hbb |
| 3 | mod.cls_blocks.0.attn.h6 | 3 | 10 | 0.2445 | -0.9907 | label_Hcc->label_Hgg |
| 4 | mod.cls_blocks.0.attn.h0 | 3 | 9 | 0.0440 | 0.1158 | label_Wqq->label_Zqq |
| 5 | mod.cls_blocks.0.attn.h7 | 1 | 2 | 0.0287 | 0.0525 | label_H4q->label_Hgg |
| 6 | mod.cls_blocks.1.attn.h3 | 1 | 2 | 0.0174 | -0.0174 | label_Hcc->label_Hbb |

## Repeated causal role pairs
| rank | role_pair | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron<-neutral_hadron | 12 | 22 | 0.4618 | -2.5652 | label_Hbb->label_Zqq |
| 2 | electron<-electron | 4 | 7 | 0.3415 | -0.9290 | label_Tbl->label_Hqql |
| 3 | CLS<-muon | 4 | 11 | 0.1654 | -0.8186 | label_Tbl->label_Hqql |
| 4 | neutral_hadron<-charged_hadron | 3 | 6 | 0.4198 | -0.7199 | label_Wqq->label_Zqq |
| 5 | photon<-neutral_hadron | 3 | 8 | 0.2625 | 0.7533 | label_Zqq->label_Hcc |
| 6 | neutral_hadron<-muon | 3 | 6 | 0.0804 | 0.2088 | label_Tbqq->label_H4q |
| 7 | muon<-muon | 2 | 4 | 0.9620 | -1.4079 | label_Hqql->label_Tbl |
| 8 | photon<-charged_hadron | 2 | 4 | 0.3930 | 0.7186 | label_Zqq->label_Hcc |
| 9 | CLS<-electron | 2 | 4 | 0.3143 | -0.9261 | label_Tbl->label_Hqql |
| 10 | neutral_hadron<-electron | 2 | 5 | 0.0614 | 0.2124 | label_Zqq->label_Hbb |
| 11 | CLS<-neutral_hadron | 1 | 1 | 2.4556 | -2.4556 | label_Hbb->label_Zqq |
| 12 | neutral_hadron<-photon | 1 | 2 | 0.5475 | -0.6279 | label_Wqq->label_Zqq |
| 13 | charged_hadron<-neutral_hadron | 1 | 2 | 0.3754 | 0.6068 | label_Zqq->label_Hbb |
| 14 | charged_hadron<-electron | 1 | 2 | 0.0987 | 0.1823 | label_Hcc->label_Hgg |
| 15 | charged_hadron<-muon | 1 | 2 | 0.0560 | 0.1020 | label_Wqq->label_Zqq |
| 16 | electron<-muon | 1 | 5 | 0.0444 | 0.1132 | label_Hcc->label_Hbb |

## Query roles
| rank | query_role | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron | 14 | 41 | 0.3552 | -2.5652 | label_Hbb->label_Zqq |
| 2 | CLS | 6 | 16 | 0.3458 | -2.4556 | label_Hbb->label_Zqq |
| 3 | electron | 4 | 12 | 0.2177 | -0.9290 | label_Tbl->label_Hqql |
| 4 | photon | 3 | 12 | 0.3060 | 0.7533 | label_Zqq->label_Hcc |
| 5 | charged_hadron | 3 | 6 | 0.1767 | 0.6068 | label_Zqq->label_Hbb |
| 6 | muon | 2 | 4 | 0.9620 | -1.4079 | label_Hqql->label_Tbl |

## Key roles
| rank | key_role | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron | 15 | 33 | 0.4687 | -2.5652 | label_Hbb->label_Zqq |
| 2 | muon | 7 | 28 | 0.2316 | -1.4079 | label_Hqql->label_Tbl |
| 3 | electron | 7 | 18 | 0.2306 | -0.9290 | label_Tbl->label_Hqql |
| 4 | charged_hadron | 4 | 10 | 0.4091 | -0.7199 | label_Wqq->label_Zqq |
| 5 | photon | 1 | 2 | 0.5475 | -0.6279 | label_Wqq->label_Zqq |

## Shared classifier dimensions
| rank | dim | graphs | mean_abs_W | best_W | best_pair |
| --- | --- | --- | --- | --- | --- |
| 1 | 57 | 20 | 0.7280 | -1.6501 | label_Hbb->label_Hgg |
| 2 | 3 | 20 | 0.6458 | 1.5487 | label_Tbqq->label_H4q |
| 3 | 103 | 20 | 0.6253 | -1.2776 | label_Hbb->label_Zqq |
| 4 | 76 | 20 | 0.6164 | -1.4146 | label_Tbl->label_Hqql |
| 5 | 10 | 20 | 0.6069 | 1.1334 | label_Hcc->label_H4q |
| 6 | 121 | 20 | 0.5934 | 1.5038 | label_Tbqq->label_H4q |
| 7 | 8 | 20 | 0.5471 | -1.4492 | label_Hbb->label_H4q |
| 8 | 18 | 20 | 0.5217 | 1.4597 | label_Zqq->label_Wqq |
| 9 | 79 | 20 | 0.5198 | -1.0130 | label_Hcc->label_Zqq |
| 10 | 66 | 20 | 0.4184 | 0.9041 | label_Zqq->label_Wqq |
| 11 | 45 | 20 | 0.4091 | 0.8398 | label_Hgg->label_H4q |
| 12 | 2 | 20 | 0.3861 | 0.8505 | label_Hcc->label_Zqq |
| 13 | 54 | 20 | 0.3512 | 1.6964 | label_Tbl->label_Hqql |
| 14 | 58 | 20 | 0.3092 | 0.7005 | label_Zqq->label_Wqq |
| 15 | 82 | 20 | 0.2737 | 0.6835 | label_Zqq->label_Wqq |
| 16 | 23 | 20 | 0.2579 | -0.5696 | label_Tbl->label_Hqql |
| 17 | 96 | 20 | 0.2320 | 0.7730 | label_Tbl->label_Hqql |
| 18 | 91 | 20 | 0.1477 | 0.2576 | label_Hcc->label_Zqq |
| 19 | 34 | 20 | 0.1455 | 1.1432 | label_Tbqq->label_H4q |
| 20 | 124 | 20 | 0.1414 | -0.4052 | label_Hcc->label_H4q |
| 21 | 123 | 20 | 0.1315 | 0.2618 | label_Hcc->label_H4q |
| 22 | 6 | 20 | 0.0282 | -0.0887 | label_Tbl->label_Hqql |
| 23 | 80 | 20 | 0.0169 | 0.0510 | label_Tbl->label_Hqql |
| 24 | 110 | 19 | 0.0138 | 0.0399 | label_Tbl->label_Hqql |
| 25 | 78 | 1 | 3.448e-04 | 3.448e-04 | label_Hbb->label_H4q |

## Interpretation

- Heads with `graphs > 1` and non-trivial edge weight are reusable mechanisms across multiple class-pairs.
- Role pairs with `graphs > 1` are repeated physical read routes after filtering numerical no-op edges.
- Classifier dims with `graphs > 1` are shared logit axes reused by multiple pair decisions.
- Pair-specific rows with high `best_weight` are local mechanisms, not universal ones.
