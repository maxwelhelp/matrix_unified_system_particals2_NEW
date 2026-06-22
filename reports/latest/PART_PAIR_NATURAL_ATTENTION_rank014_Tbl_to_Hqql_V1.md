# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9920**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.1102 | 0.3070 | 1.1484 | 0.3070 | 0.8812 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0968 | 0.2573 | 0.9816 | 0.2573 | 0.7481 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0924 | 0.2407 | 0.9256 | 0.2407 | 0.7035 |
| 4 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.1029 | 0.2181 | 0.5417 | 0.2181 | 0.4890 |
| 5 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0991 | 0.3227 | 0.2946 | 0.1512 | 0.4700 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.9109 | 0.0000 | 0.4555 |
| 7 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0896 | 0.2774 | 0.2471 | 0.1575 | 0.4009 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0849 | 0.1553 | 0.4401 | 0.1553 | 0.3754 |
| 9 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0789 | 0.1344 | 0.4232 | 0.1344 | 0.3460 |
| 10 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0813 | 0.1624 | 0.0607 | 0.0365 | 0.1927 |
| 11 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0969 | 0.1428 | 0.0901 | 0.0097 | 0.1878 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.3384 | 0.0000 | 0.1692 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0857 | 0.1220 | 0.0613 | 0.0295 | 0.1527 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0697 | 0.1238 | 0.0343 | 0.0202 | 0.1409 |
| 15 | mod.cls_blocks.1.attn.h3 | neutral_hadron<-electron | 0.0000 | 0.0000 | 0.2654 | 1.554e-14 | 0.1327 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.2628 | 0.0000 | 0.1314 |
| 17 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.2599 | 0.0000 | 0.1299 |
| 18 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0767 | 0.0906 | 0.0283 | -0.0059 | 0.1047 |
| 19 | mod.cls_blocks.1.attn.h0 | electron<-muon | 0.0000 | 0.0000 | -0.2074 | 0.0000 | 0.1037 |
| 20 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.1667 | -0.0127 | 0.1529 | -0.0127 | 0.0892 |
| 21 | mod.cls_blocks.1.attn.h0 | muon<-electron | 0.0718 | 9.434e-04 | -0.1676 | 9.434e-04 | 0.0847 |
| 22 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0000 | 0.0000 | -0.1638 | -0.0109 | 0.0819 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0669 | 0.0687 | -7.292e-04 | -0.0115 | 0.0691 |
| 24 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.3000 | -0.0124 | 0.1132 | -0.0124 | 0.0690 |
| 25 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.1362 | 0.0000 | 0.0681 |
| 26 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.1429 | -0.0109 | 0.1091 | -0.0109 | 0.0655 |
| 27 | mod.cls_blocks.0.attn.h1 | electron<-muon | 0.0000 | 0.0000 | -0.1286 | 0.0000 | 0.0643 |
| 28 | mod.cls_blocks.0.attn.h6 | electron<-muon | 0.0000 | 0.0000 | -0.1234 | 0.0000 | 0.0617 |
| 29 | mod.cls_blocks.0.attn.h6 | muon<-electron | 0.0215 | -0.0018 | -0.1199 | -0.0018 | 0.0617 |
| 30 | mod.cls_blocks.1.attn.h6 | neutral_hadron<-electron | 0.0000 | 0.0000 | 0.1179 | 2.058e-12 | 0.0589 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0961 | 0.3699 | 0.3699 | 0.3699 | 0.5549 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0871 | 0.3179 | 0.3179 | 0.3179 | 0.4768 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0817 | 0.2365 | 0.2365 | 0.2365 | 0.3548 |
| 4 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0949 | 0.1810 | 0.1810 | 0.1810 | 0.2715 |
| 5 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0699 | 0.1808 | 0.1808 | 0.1808 | 0.2712 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0840 | 0.1548 | 0.1548 | 0.1548 | 0.2322 |
| 7 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0740 | 0.1305 | 0.1305 | 0.1305 | 0.1958 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0648 | 0.0994 | 0.0994 | 0.0994 | 0.1492 |
| 9 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0508 | 0.0252 | 0.0252 | 0.0252 | 0.0378 |
| 10 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0483 | 0.0235 | 0.0235 | 0.0235 | 0.0353 |
| 11 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0462 | 0.0213 | 0.0213 | 0.0213 | 0.0319 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0325 | -0.0198 | -0.0198 | -0.0198 | 0.0298 |
| 13 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0371 | 0.0198 | 0.0198 | 0.0198 | 0.0297 |
| 14 | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0245 | -0.0186 | -0.0186 | -0.0186 | 0.0279 |
| 15 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0427 | 0.0180 | 0.0180 | 0.0180 | 0.0270 |
| 16 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0339 | 0.0169 | 0.0169 | 0.0169 | 0.0254 |
| 17 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0454 | 0.0162 | 0.0162 | 0.0162 | 0.0244 |
| 18 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0300 | 0.0148 | 0.0148 | 0.0148 | 0.0221 |
| 19 | mod.cls_blocks.0.attn.h7 | electron<-electron | 0.0431 | 0.0145 | 0.0145 | 0.0145 | 0.0217 |
| 20 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0276 | 0.0143 | 0.0143 | 0.0143 | 0.0214 |
| 21 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0415 | 0.0137 | 0.0137 | 0.0137 | 0.0206 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0354 | 0.0119 | 0.0119 | 0.0119 | 0.0178 |
| 23 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0376 | 0.0109 | 0.0109 | 0.0109 | 0.0163 |
| 24 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0284 | -0.0103 | -0.0103 | -0.0103 | 0.0154 |
| 25 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0295 | -0.0102 | -0.0102 | -0.0102 | 0.0153 |
| 26 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0549 | -0.0102 | -0.0102 | -0.0102 | 0.0152 |
| 27 | mod.cls_blocks.1.attn.h3 | electron<-neutral_hadron | 0.1000 | -0.0092 | -0.0092 | -0.0092 | 0.0138 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0598 | -0.0090 | -0.0090 | -0.0090 | 0.0135 |
| 29 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0163 | -0.0086 | -0.0086 | -0.0086 | 0.0129 |
| 30 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0386 | 0.0084 | 0.0084 | 0.0084 | 0.0126 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
