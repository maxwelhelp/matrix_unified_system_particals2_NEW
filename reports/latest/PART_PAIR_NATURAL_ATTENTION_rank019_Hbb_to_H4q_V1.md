# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9120**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0815 | 0.7067 | 0.9495 | 0.7067 | 1.1815 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0774 | 0.4105 | 0.6951 | 0.4105 | 0.7580 |
| 3 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0743 | 0.1692 | 0.1931 | 0.1692 | 0.2657 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0734 | 0.1143 | 0.3014 | 0.1143 | 0.2650 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.4503 | 0.0000 | 0.2251 |
| 6 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.1882 | -0.1377 | -0.1320 | -0.1318 | 0.2037 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0686 | 0.0768 | 0.1171 | 0.0768 | 0.1354 |
| 8 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | 0.2236 | 0.0000 | 0.1118 |
| 9 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.1891 | 0.0000 | 0.0945 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0000 | 0.0000 | -0.1575 | -0.0015 | 0.0787 |
| 11 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0000 | 0.0000 | -0.1564 | 0.0000 | 0.0782 |
| 12 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0395 | 0.0477 | 0.0593 | 0.0477 | 0.0773 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0393 | 0.0405 | 0.0603 | 0.0405 | 0.0706 |
| 14 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0390 | 0.0333 | 0.0602 | 0.0333 | 0.0634 |
| 15 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0562 | -0.0379 | -0.0417 | -0.0410 | 0.0587 |
| 16 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0000 | 0.0000 | -0.1164 | 0.0000 | 0.0582 |
| 17 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0156 | 6.123e-04 | -0.1138 | -8.649e-04 | 0.0575 |
| 18 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.0000 | 0.0000 | -0.1058 | 0.0000 | 0.0529 |
| 19 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0231 | 0.0320 | 0.0381 | 0.0320 | 0.0511 |
| 20 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.1022 | 0.0000 | 0.0511 |
| 21 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0000 | 0.0000 | -0.0974 | 0.0000 | 0.0487 |
| 22 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | -0.0963 | 0.0000 | 0.0482 |
| 23 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0223 | 0.0271 | 0.0371 | 0.0271 | 0.0457 |
| 24 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0463 | -0.0272 | -0.0323 | -0.0269 | 0.0433 |
| 25 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0364 | 0.0255 | 0.0331 | 0.0255 | 0.0421 |
| 26 | mod.cls_blocks.1.attn.h3 | photon<-muon | 0.0000 | 0.0000 | -0.0827 | 0.0000 | 0.0413 |
| 27 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0215 | 0.0222 | 0.0376 | 0.0222 | 0.0410 |
| 28 | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0577 | -0.0274 | -0.0233 | -0.0238 | 0.0391 |
| 29 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0338 | 0.0193 | 0.0292 | 0.0193 | 0.0338 |
| 30 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | -0.0627 | 0.0000 | 0.0313 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.1882 | -0.1377 | -0.1377 | -0.1377 | 0.2065 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0319 | 0.0450 | 0.0450 | 0.0450 | 0.0674 |
| 3 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0562 | -0.0379 | -0.0379 | -0.0379 | 0.0568 |
| 4 | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0604 | -0.0292 | -0.0292 | -0.0292 | 0.0438 |
| 5 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0463 | -0.0272 | -0.0272 | -0.0272 | 0.0407 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0258 | 0.0150 | 0.0150 | 0.0150 | 0.0224 |
| 7 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0585 | -0.0112 | -0.0112 | -0.0112 | 0.0169 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0313 | 0.0112 | 0.0112 | 0.0112 | 0.0168 |
| 9 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0992 | 0.0109 | 0.0109 | 0.0109 | 0.0164 |
| 10 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0211 | -0.0104 | -0.0104 | -0.0104 | 0.0156 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0207 | -0.0091 | -0.0091 | -0.0091 | 0.0136 |
| 12 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0798 | 0.0087 | 0.0087 | 0.0087 | 0.0131 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0174 | -0.0087 | -0.0087 | -0.0087 | 0.0130 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0247 | -0.0080 | -0.0080 | -0.0080 | 0.0120 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0227 | -0.0078 | -0.0078 | -0.0078 | 0.0118 |
| 16 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0280 | -0.0076 | -0.0076 | -0.0076 | 0.0114 |
| 17 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0280 | -0.0076 | -0.0076 | -0.0076 | 0.0114 |
| 18 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0314 | -0.0068 | -0.0068 | -0.0068 | 0.0102 |
| 19 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0167 | -0.0066 | -0.0066 | -0.0066 | 0.0099 |
| 20 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0261 | -0.0060 | -0.0060 | -0.0060 | 0.0090 |
| 21 | mod.cls_blocks.1.attn.h5 | CLS<-muon | 0.0960 | 0.0057 | 0.0057 | 0.0057 | 0.0085 |
| 22 | mod.cls_blocks.1.attn.h5 | charged_hadron<-muon | 0.0960 | 0.0057 | 0.0057 | 0.0057 | 0.0085 |
| 23 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0163 | -0.0056 | -0.0056 | -0.0056 | 0.0085 |
| 24 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0257 | 0.0048 | 0.0048 | 0.0048 | 0.0072 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0306 | 0.0045 | 0.0045 | 0.0045 | 0.0067 |
| 26 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0306 | 0.0045 | 0.0045 | 0.0045 | 0.0067 |
| 27 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0136 | -0.0044 | -0.0044 | -0.0044 | 0.0066 |
| 28 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0136 | -0.0044 | -0.0044 | -0.0044 | 0.0066 |
| 29 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0238 | 0.0044 | 0.0044 | 0.0044 | 0.0066 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0237 | 0.0040 | 0.0040 | 0.0040 | 0.0060 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
