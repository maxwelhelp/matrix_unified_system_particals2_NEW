# PART_PAIR_ATLAS_HEAD_ROLE_SUMMARY_V1

Aggregates generated pair program graphs into a head/role/classifier-dimension atlas. This is a model-level summary over pair-specific program graphs, not a new model run. Near-zero pair edges are filtered so numerical no-op routes do not look universal.

- pair_graphs: **8**
- min_abs_pair_weight: **0.001**
- kept_pair_edges: **38**
- skipped_pair_edges: **45**
- unique_heads: **6**
- unique_role_pairs: **10**
- unique_classifier_dims: **24**

## Universal / repeated heads
| rank | head | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | 6 | 14 | 0.3922 | -0.7199 | label_Wqq->label_Zqq |
| 2 | mod.cls_blocks.0.attn.h6 | 2 | 8 | 0.2407 | -0.9907 | label_Hcc->label_Hgg |
| 3 | mod.cls_blocks.0.attn.h0 | 2 | 8 | 0.0473 | 0.1158 | label_Wqq->label_Zqq |
| 4 | mod.cls_blocks.0.attn.h1 | 1 | 4 | 0.0674 | 0.1132 | label_Hcc->label_Hbb |
| 5 | mod.cls_blocks.0.attn.h7 | 1 | 2 | 0.0287 | 0.0525 | label_H4q->label_Hgg |
| 6 | mod.cls_blocks.1.attn.h3 | 1 | 2 | 0.0174 | -0.0174 | label_Hcc->label_Hbb |

## Repeated causal role pairs
| rank | role_pair | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron<-neutral_hadron | 5 | 12 | 0.3459 | -0.9907 | label_Hcc->label_Hgg |
| 2 | CLS<-muon | 2 | 7 | 0.0498 | 0.1158 | label_Wqq->label_Zqq |
| 3 | neutral_hadron<-charged_hadron | 1 | 2 | 0.5784 | -0.7199 | label_Wqq->label_Zqq |
| 4 | neutral_hadron<-photon | 1 | 2 | 0.5475 | -0.6279 | label_Wqq->label_Zqq |
| 5 | electron<-electron | 1 | 2 | 0.2544 | -0.4486 | label_Hcc->label_Hbb |
| 6 | CLS<-electron | 1 | 2 | 0.1536 | 0.2883 | label_Hcc->label_Hgg |
| 7 | charged_hadron<-electron | 1 | 2 | 0.0987 | 0.1823 | label_Hcc->label_Hgg |
| 8 | charged_hadron<-muon | 1 | 2 | 0.0560 | 0.1020 | label_Wqq->label_Zqq |
| 9 | electron<-muon | 1 | 5 | 0.0444 | 0.1132 | label_Hcc->label_Hbb |
| 10 | neutral_hadron<-electron | 1 | 2 | 0.0287 | 0.0525 | label_H4q->label_Hgg |

## Query roles
| rank | query_role | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron | 5 | 18 | 0.3589 | -0.9907 | label_Hcc->label_Hgg |
| 2 | CLS | 3 | 9 | 0.0729 | 0.2883 | label_Hcc->label_Hgg |
| 3 | charged_hadron | 2 | 4 | 0.0773 | 0.1823 | label_Hcc->label_Hgg |
| 4 | electron | 1 | 7 | 0.1044 | -0.4486 | label_Hcc->label_Hbb |

## Key roles
| rank | key_role | graphs | edges | mean_abs | best_weight | best_pair |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | neutral_hadron | 5 | 12 | 0.3459 | -0.9907 | label_Hcc->label_Hgg |
| 2 | electron | 3 | 8 | 0.1338 | -0.4486 | label_Hcc->label_Hbb |
| 3 | muon | 2 | 14 | 0.0488 | 0.1158 | label_Wqq->label_Zqq |
| 4 | charged_hadron | 1 | 2 | 0.5784 | -0.7199 | label_Wqq->label_Zqq |
| 5 | photon | 1 | 2 | 0.5475 | -0.6279 | label_Wqq->label_Zqq |

## Shared classifier dimensions
| rank | dim | graphs | mean_abs_W | best_W | best_pair |
| --- | --- | --- | --- | --- | --- |
| 1 | 3 | 8 | 0.7031 | 1.4458 | label_Hgg->label_H4q |
| 2 | 8 | 8 | 0.6077 | -0.9769 | label_Hgg->label_H4q |
| 3 | 57 | 8 | 0.5685 | -1.6501 | label_Hbb->label_Hgg |
| 4 | 18 | 8 | 0.5605 | 1.4597 | label_Zqq->label_Wqq |
| 5 | 121 | 8 | 0.4582 | 1.0862 | label_Hbb->label_Hgg |
| 6 | 103 | 8 | 0.4565 | 1.1085 | label_Hcc->label_Hbb |
| 7 | 45 | 8 | 0.4454 | 0.8398 | label_Hgg->label_H4q |
| 8 | 79 | 8 | 0.4314 | -0.8393 | label_Hgg->label_H4q |
| 9 | 76 | 8 | 0.4231 | -0.9855 | label_Hcc->label_Hgg |
| 10 | 66 | 8 | 0.4216 | 0.9041 | label_Zqq->label_Wqq |
| 11 | 58 | 8 | 0.3749 | 0.7005 | label_Zqq->label_Wqq |
| 12 | 10 | 8 | 0.3746 | 0.9306 | label_Hgg->label_H4q |
| 13 | 82 | 8 | 0.2855 | 0.6835 | label_Zqq->label_Wqq |
| 14 | 96 | 8 | 0.2075 | -0.6741 | label_Zqq->label_Wqq |
| 15 | 2 | 8 | 0.2025 | 0.3781 | label_Hcc->label_Hgg |
| 16 | 54 | 8 | 0.1702 | 0.3205 | label_Hgg->label_H4q |
| 17 | 124 | 8 | 0.1635 | -0.3457 | label_Hgg->label_H4q |
| 18 | 23 | 8 | 0.1571 | 0.3665 | label_Hbb->label_Hgg |
| 19 | 34 | 8 | 0.0852 | 0.1541 | label_Hcc->label_Hbb |
| 20 | 123 | 8 | 0.0820 | 0.2567 | label_Hcc->label_Hgg |
| 21 | 91 | 8 | 0.0789 | -0.2277 | label_Hgg->label_H4q |
| 22 | 6 | 8 | 0.0118 | -0.0421 | label_Hcc->label_Hgg |
| 23 | 80 | 8 | 0.0084 | 0.0172 | label_Hbb->label_Hgg |
| 24 | 110 | 8 | 0.0068 | 0.0105 | label_Hgg->label_H4q |

## Interpretation

- Heads with `graphs > 1` and non-trivial edge weight are reusable mechanisms across multiple class-pairs.
- Role pairs with `graphs > 1` are repeated physical read routes after filtering numerical no-op edges.
- Classifier dims with `graphs > 1` are shared logit axes reused by multiple pair decisions.
- Pair-specific rows with high `best_weight` are local mechanisms, not universal ones.
