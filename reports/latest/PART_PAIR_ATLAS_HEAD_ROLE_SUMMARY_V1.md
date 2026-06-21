# PART_PAIR_ATLAS_HEAD_ROLE_SUMMARY_V1

Aggregates generated pair program graphs into a head/role/classifier-dimension atlas. This is a model-level summary over pair-specific program graphs, not a new model run. Near-zero pair edges are filtered so numerical no-op routes do not look universal.

- pair_graphs: **3**
- min_abs_pair_weight: **0.001**
- kept_pair_edges: **25**
- skipped_pair_edges: **12**
- unique_heads: **5**
- unique_role_pairs: **7**
- unique_classifier_dims: **24**

## Universal / repeated heads
| rank | head | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | 3 | 9 | 0.4483 | -0.7199 | label_Wqq->label_Zqq |
| 2 | mod.cls_blocks.0.attn.h0 | 2 | 8 | 0.0473 | 0.1158 | label_Wqq->label_Zqq |
| 3 | mod.cls_blocks.0.attn.h6 | 1 | 2 | 0.1385 | -0.1500 | label_Zqq->label_Wqq |
| 4 | mod.cls_blocks.0.attn.h1 | 1 | 4 | 0.0674 | 0.1132 | label_Hcc->label_Hbb |
| 5 | mod.cls_blocks.1.attn.h3 | 1 | 2 | 0.0174 | -0.0174 | label_Hcc->label_Hbb |

## Repeated causal role pairs
| rank | role_pair | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron<-neutral_hadron | 2 | 5 | 0.3103 | -0.6431 | label_Wqq->label_Zqq |
| 2 | CLS<-muon | 2 | 7 | 0.0498 | 0.1158 | label_Wqq->label_Zqq |
| 3 | neutral_hadron<-charged_hadron | 1 | 2 | 0.5784 | -0.7199 | label_Wqq->label_Zqq |
| 4 | neutral_hadron<-photon | 1 | 2 | 0.5475 | -0.6279 | label_Wqq->label_Zqq |
| 5 | electron<-electron | 1 | 2 | 0.2544 | -0.4486 | label_Hcc->label_Hbb |
| 6 | charged_hadron<-muon | 1 | 2 | 0.0560 | 0.1020 | label_Wqq->label_Zqq |
| 7 | electron<-muon | 1 | 5 | 0.0444 | 0.1132 | label_Hcc->label_Hbb |

## Query roles
| rank | query_role | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron | 2 | 9 | 0.4226 | -0.7199 | label_Wqq->label_Zqq |
| 2 | CLS | 2 | 7 | 0.0498 | 0.1158 | label_Wqq->label_Zqq |
| 3 | electron | 1 | 7 | 0.1044 | -0.4486 | label_Hcc->label_Hbb |
| 4 | charged_hadron | 1 | 2 | 0.0560 | 0.1020 | label_Wqq->label_Zqq |

## Key roles
| rank | key_role | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron | 2 | 5 | 0.3103 | -0.6431 | label_Wqq->label_Zqq |
| 2 | muon | 2 | 14 | 0.0488 | 0.1158 | label_Wqq->label_Zqq |
| 3 | charged_hadron | 1 | 2 | 0.5784 | -0.7199 | label_Wqq->label_Zqq |
| 4 | photon | 1 | 2 | 0.5475 | -0.6279 | label_Wqq->label_Zqq |
| 5 | electron | 1 | 2 | 0.2544 | -0.4486 | label_Hcc->label_Hbb |

## Shared classifier dimensions
| rank | dim | graphs | mean_abs_W | best_W | best_pair |
| --- | --- | --- | --- | --- | --- |
| 1 | 18 | 3 | 1.0392 | 1.4597 | label_Zqq->label_Wqq |
| 2 | 66 | 3 | 0.6278 | 0.9041 | label_Zqq->label_Wqq |
| 3 | 58 | 3 | 0.5711 | 0.7005 | label_Zqq->label_Wqq |
| 4 | 82 | 3 | 0.5052 | 0.6835 | label_Zqq->label_Wqq |
| 5 | 79 | 3 | 0.5014 | -0.6879 | label_Zqq->label_Wqq |
| 6 | 121 | 3 | 0.4668 | -0.6736 | label_Hcc->label_Hbb |
| 7 | 96 | 3 | 0.4650 | -0.6741 | label_Zqq->label_Wqq |
| 8 | 76 | 3 | 0.4060 | -0.5133 | label_Hcc->label_Hbb |
| 9 | 103 | 3 | 0.3950 | 1.1085 | label_Hcc->label_Hbb |
| 10 | 8 | 3 | 0.3814 | 0.8819 | label_Hcc->label_Hbb |
| 11 | 3 | 3 | 0.2712 | -0.2989 | label_Zqq->label_Wqq |
| 12 | 10 | 3 | 0.2434 | -0.3137 | label_Zqq->label_Wqq |
| 13 | 2 | 3 | 0.2387 | -0.3226 | label_Zqq->label_Wqq |
| 14 | 45 | 3 | 0.1895 | -0.5391 | label_Hcc->label_Hbb |
| 15 | 57 | 3 | 0.1634 | 0.3565 | label_Hcc->label_Hbb |
| 16 | 23 | 3 | 0.1313 | -0.2249 | label_Hcc->label_Hbb |
| 17 | 124 | 3 | 0.1238 | -0.1244 | label_Zqq->label_Wqq |
| 18 | 54 | 3 | 0.1048 | 0.1572 | label_Hcc->label_Hbb |
| 19 | 34 | 3 | 0.0710 | 0.1541 | label_Hcc->label_Hbb |
| 20 | 123 | 3 | 0.0442 | 0.1092 | label_Hcc->label_Hbb |
| 21 | 91 | 3 | 0.0382 | -0.0419 | label_Zqq->label_Wqq |
| 22 | 80 | 3 | 0.0095 | -0.0096 | label_Hcc->label_Hbb |
| 23 | 110 | 3 | 0.0043 | 0.0076 | label_Hcc->label_Hbb |
| 24 | 6 | 3 | 0.0023 | 0.0026 | label_Zqq->label_Wqq |

## Interpretation

- Heads with `graphs > 1` and non-trivial edge weight are reusable mechanisms across multiple class-pairs.
- Role pairs with `graphs > 1` are repeated physical read routes after filtering numerical no-op edges.
- Classifier dims with `graphs > 1` are shared logit axes reused by multiple pair decisions.
- Pair-specific rows with high `best_weight` are local mechanisms, not universal ones.
