# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8672**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0963 | -1.2670 | -1.2648 | -1.2670 | 1.8994 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1141 | -0.7504 | -0.8964 | -0.7504 | 1.1986 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1074 | -0.6762 | -0.7451 | -0.6762 | 1.0487 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1451 | -0.3821 | -0.7337 | -0.3821 | 0.7490 |
| 5 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0894 | -0.3938 | -0.3985 | -0.3938 | 0.5930 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1047 | -0.2444 | -0.2952 | -0.2444 | 0.3920 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0909 | -0.2077 | -0.2723 | -0.2077 | 0.3439 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.1476 | -0.1682 | -0.2737 | -0.1682 | 0.3051 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0593 | -0.1470 | -0.1286 | 0.2568 | 0.2113 |
| 10 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.2239 | 0.1065 | 0.1065 | 0.1096 | 0.1598 |
| 11 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | -0.3168 | 0.0000 | 0.1584 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0524 | 0.0995 | 0.0995 | 0.0780 | 0.1493 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0524 | 0.0995 | 0.0901 | 0.2198 | 0.1445 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.2239 | 0.1065 | 0.0672 | 0.1137 | 0.1401 |
| 15 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.1097 | 0.0685 | 0.0685 | 0.0610 | 0.1027 |
| 16 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.1097 | 0.0685 | 0.0549 | 0.0877 | 0.0959 |
| 17 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0669 | -0.0609 | -0.0543 | -0.0609 | 0.0880 |
| 18 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0235 | -0.0501 | -0.0602 | -0.0501 | 0.0802 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0338 | 0.0492 | 0.0500 | 0.0228 | 0.0742 |
| 20 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0495 | -0.0478 | -0.0467 | 0.0837 | 0.0712 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0322 | 0.0411 | 0.0507 | 0.0145 | 0.0664 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0359 | -0.0413 | -0.0417 | -0.0046 | 0.0622 |
| 23 | mod.cls_blocks.0.attn.h3 | CLS<-muon | 0.1549 | 0.0359 | 0.0425 | 0.0315 | 0.0572 |
| 24 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0271 | -0.0315 | -0.0500 | -0.0315 | 0.0565 |
| 25 | mod.cls_blocks.0.attn.h3 | charged_hadron<-muon | 0.1549 | 0.0359 | 0.0359 | 0.0274 | 0.0539 |
| 26 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0784 | -0.0353 | -0.0359 | -0.0353 | 0.0532 |
| 27 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0675 | -0.0330 | -0.0375 | -0.0330 | 0.0517 |
| 28 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0361 | 0.0325 | 0.0380 | -4.898e-04 | 0.0514 |
| 29 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0389 | -0.0248 | -0.0489 | -0.0248 | 0.0493 |
| 30 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0231 | -0.0255 | -0.0474 | -0.0255 | 0.0492 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0671 | -0.1886 | -0.1886 | -0.1886 | 0.2828 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0356 | -0.0970 | -0.0970 | -0.0970 | 0.1455 |
| 3 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0651 | -0.0644 | -0.0644 | -0.0644 | 0.0966 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0372 | 0.0610 | 0.0610 | 0.0610 | 0.0915 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0357 | 0.0511 | 0.0511 | 0.0511 | 0.0766 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0358 | 0.0435 | 0.0435 | 0.0435 | 0.0653 |
| 7 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0365 | -0.0352 | -0.0352 | -0.0352 | 0.0528 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0314 | -0.0223 | -0.0223 | -0.0223 | 0.0334 |
| 9 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0575 | 0.0204 | 0.0204 | 0.0204 | 0.0305 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0317 | 0.0196 | 0.0196 | 0.0196 | 0.0294 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0171 | 0.0152 | 0.0152 | 0.0152 | 0.0228 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0171 | 0.0152 | 0.0152 | 0.0152 | 0.0228 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0221 | 0.0146 | 0.0146 | 0.0146 | 0.0220 |
| 14 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0397 | 0.0130 | 0.0130 | 0.0130 | 0.0194 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0247 | 0.0126 | 0.0126 | 0.0126 | 0.0190 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0329 | 0.0102 | 0.0102 | 0.0102 | 0.0153 |
| 17 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0342 | 0.0099 | 0.0099 | 0.0099 | 0.0149 |
| 18 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0299 | -0.0089 | -0.0089 | -0.0089 | 0.0134 |
| 19 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0397 | 0.0082 | 0.0082 | 0.0082 | 0.0123 |
| 20 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0682 | -0.0078 | -0.0078 | -0.0078 | 0.0117 |
| 21 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0397 | 0.0073 | 0.0073 | 0.0073 | 0.0110 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0162 | 0.0072 | 0.0072 | 0.0072 | 0.0108 |
| 23 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0162 | 0.0072 | 0.0072 | 0.0072 | 0.0108 |
| 24 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0483 | -0.0061 | -0.0061 | -0.0061 | 0.0091 |
| 25 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-photon | 0.0353 | 0.0060 | 0.0060 | 0.0060 | 0.0090 |
| 26 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0373 | 0.0059 | 0.0059 | 0.0059 | 0.0088 |
| 27 | mod.blocks.1.attn.h6 | neutral_hadron<-muon | 0.3534 | 0.0056 | 0.0056 | 0.0056 | 0.0084 |
| 28 | mod.cls_blocks.0.attn.h3 | photon<-neutral_hadron | 0.0375 | 0.0054 | 0.0054 | 0.0054 | 0.0081 |
| 29 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0256 | 0.0051 | 0.0051 | 0.0051 | 0.0076 |
| 30 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0543 | 0.0048 | 0.0048 | 0.0048 | 0.0073 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
