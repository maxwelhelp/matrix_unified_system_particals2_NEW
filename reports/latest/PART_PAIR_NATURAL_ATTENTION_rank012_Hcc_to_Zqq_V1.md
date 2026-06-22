# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8288**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1168 | 0.2980 | 1.7572 | 0.2980 | 1.1766 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0956 | 0.4700 | 1.1441 | 0.4700 | 1.0420 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1021 | 0.3984 | 1.0262 | 0.3984 | 0.9115 |
| 4 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.1003 | 0.3558 | 0.3558 | 0.3558 | 0.5336 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.1023 | 0.0978 | 0.5441 | 0.0978 | 0.3698 |
| 6 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0814 | 0.1477 | 0.3941 | 0.1477 | 0.3447 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0878 | 0.1218 | 0.3226 | 0.1218 | 0.2831 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.5502 | 0.0000 | 0.2751 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0650 | 0.1158 | 0.1132 | 0.0471 | 0.1724 |
| 10 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0860 | 0.0941 | 0.0941 | 0.0941 | 0.1412 |
| 11 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.2622 | 0.0000 | 0.1311 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.1654 | 0.0000 | 0.0827 |
| 13 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0780 | 0.0209 | 0.1088 | 0.0209 | 0.0753 |
| 14 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0000 | 0.0000 | -0.1271 | 0.0000 | 0.0636 |
| 15 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0273 | 0.0338 | 0.0563 | 0.0338 | 0.0619 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0303 | -0.0222 | -0.0759 | -0.0155 | 0.0602 |
| 17 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0319 | -0.0261 | -0.0563 | -0.0237 | 0.0542 |
| 18 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0418 | -0.0294 | -0.0414 | -0.0212 | 0.0501 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0415 | 0.0348 | 0.0269 | 0.0138 | 0.0482 |
| 20 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0577 | 0.0203 | 0.0515 | 0.0203 | 0.0460 |
| 21 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0000 | 0.0000 | -0.0916 | 0.0000 | 0.0458 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0273 | 0.0226 | 0.0427 | 0.0226 | 0.0440 |
| 23 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0321 | 0.0117 | 0.0640 | 0.0117 | 0.0437 |
| 24 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | -0.0757 | -9.565e-11 | 0.0378 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0310 | 0.0324 | 0.0106 | 0.0319 | 0.0377 |
| 26 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0621 | 0.0145 | 0.0444 | 0.0145 | 0.0367 |
| 27 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0000 | 0.0000 | -0.0712 | 2.463e-04 | 0.0356 |
| 28 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.2214 | -0.0235 | -0.0235 | -0.0260 | 0.0352 |
| 29 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0511 | 0.0131 | 0.0358 | 0.0131 | 0.0309 |
| 30 | mod.cls_blocks.1.attn.h4 | neutral_hadron<-electron | 0.7991 | -0.0190 | -0.0190 | -0.0192 | 0.0285 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0780 | 0.1759 | 0.1759 | 0.1759 | 0.2638 |
| 2 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0447 | 0.1210 | 0.1210 | 0.1210 | 0.1815 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0332 | 0.0624 | 0.0624 | 0.0624 | 0.0937 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0668 | 0.0540 | 0.0540 | 0.0540 | 0.0810 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0323 | 0.0396 | 0.0396 | 0.0396 | 0.0594 |
| 6 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0424 | 0.0322 | 0.0322 | 0.0322 | 0.0483 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0418 | -0.0294 | -0.0294 | -0.0294 | 0.0441 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0353 | 0.0235 | 0.0235 | 0.0235 | 0.0352 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0316 | -0.0229 | -0.0229 | -0.0229 | 0.0344 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0299 | -0.0222 | -0.0222 | -0.0222 | 0.0332 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0319 | -0.0194 | -0.0194 | -0.0194 | 0.0290 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0294 | 0.0163 | 0.0163 | 0.0163 | 0.0245 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0306 | 0.0158 | 0.0158 | 0.0158 | 0.0237 |
| 14 | mod.cls_blocks.0.attn.h5 | electron<-neutral_hadron | 0.0505 | -0.0155 | -0.0155 | -0.0155 | 0.0233 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0283 | -0.0147 | -0.0147 | -0.0147 | 0.0221 |
| 16 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0320 | 0.0122 | 0.0122 | 0.0122 | 0.0183 |
| 17 | mod.cls_blocks.1.attn.h3 | electron<-neutral_hadron | 0.3333 | -0.0110 | -0.0110 | -0.0110 | 0.0165 |
| 18 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0419 | 0.0105 | 0.0105 | 0.0105 | 0.0158 |
| 19 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0419 | -0.0099 | -0.0099 | -0.0099 | 0.0149 |
| 20 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0516 | 0.0093 | 0.0093 | 0.0093 | 0.0140 |
| 21 | mod.cls_blocks.0.attn.h4 | electron<-photon | 0.0249 | -0.0087 | -0.0087 | -0.0087 | 0.0130 |
| 22 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0349 | 0.0076 | 0.0076 | 0.0076 | 0.0113 |
| 23 | mod.cls_blocks.0.attn.h4 | electron<-charged_hadron | 0.0262 | -0.0073 | -0.0073 | -0.0073 | 0.0110 |
| 24 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0319 | -0.0063 | -0.0063 | -0.0063 | 0.0094 |
| 25 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0616 | -0.0062 | -0.0062 | -0.0062 | 0.0093 |
| 26 | mod.cls_blocks.0.attn.h6 | electron<-neutral_hadron | 0.0614 | 0.0056 | 0.0056 | 0.0056 | 0.0084 |
| 27 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0347 | -0.0055 | -0.0055 | -0.0055 | 0.0082 |
| 28 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-neutral_hadron | 0.0394 | 0.0054 | 0.0054 | 0.0054 | 0.0081 |
| 29 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0276 | -0.0054 | -0.0054 | -0.0054 | 0.0080 |
| 30 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0298 | 0.0050 | 0.0050 | 0.0050 | 0.0076 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
