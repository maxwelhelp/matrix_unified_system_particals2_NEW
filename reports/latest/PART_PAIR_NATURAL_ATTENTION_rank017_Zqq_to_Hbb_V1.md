# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **10032**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1105 | -0.9876 | -1.2045 | -0.9876 | 1.5898 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0797 | -0.8065 | -0.8280 | -0.6130 | 1.2205 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1045 | -0.4355 | -0.7395 | -0.4355 | 0.8053 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0881 | 0.4448 | 0.3374 | 0.4448 | 0.6135 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1088 | -0.2116 | -0.6787 | -0.2116 | 0.5509 |
| 6 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1027 | -0.3153 | -0.4293 | -0.3153 | 0.5300 |
| 7 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | -0.7982 | 0.0000 | 0.3991 |
| 8 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0736 | -0.1975 | -0.2082 | -0.1358 | 0.3016 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0957 | -0.1546 | -0.2931 | -0.1546 | 0.3012 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0968 | -0.1334 | -0.3046 | -0.1334 | 0.2857 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0434 | -0.1807 | -0.1595 | -0.0709 | 0.2604 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0483 | -0.1232 | -0.1343 | -0.0561 | 0.1903 |
| 13 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0806 | 0.1455 | 0.0366 | 0.1455 | 0.1638 |
| 14 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | -0.2397 | 0.0000 | 0.1199 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0612 | -0.0622 | -0.1150 | -0.0622 | 0.1197 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0416 | -0.0632 | -0.0620 | -0.0312 | 0.0942 |
| 17 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0521 | -0.0372 | -0.0916 | -0.0372 | 0.0830 |
| 18 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0539 | -0.0370 | -0.0893 | -0.0370 | 0.0817 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0382 | 0.0500 | 0.0499 | 0.0502 | 0.0750 |
| 20 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0267 | -0.0374 | -0.0635 | -0.0374 | 0.0691 |
| 21 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0365 | 0.0395 | 0.0513 | 0.0332 | 0.0651 |
| 22 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0404 | 0.0423 | 0.0416 | 0.0385 | 0.0631 |
| 23 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.1236 | 0.0430 | 0.0402 | 0.0372 | 0.0631 |
| 24 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0318 | 0.0368 | 0.0493 | 0.0249 | 0.0614 |
| 25 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0201 | -0.0327 | -0.0430 | -0.0291 | 0.0542 |
| 26 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0321 | -0.0379 | -0.0288 | -0.0288 | 0.0523 |
| 27 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0270 | -0.0229 | -0.0568 | -0.0229 | 0.0513 |
| 28 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0317 | -0.0205 | -0.0593 | -0.0205 | 0.0502 |
| 29 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0395 | -0.0317 | -0.0347 | -0.0088 | 0.0490 |
| 30 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0360 | 0.0290 | 0.0381 | 0.0276 | 0.0480 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0797 | -0.8065 | -0.8065 | -0.8065 | 1.2098 |
| 2 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0736 | -0.1975 | -0.1975 | -0.1975 | 0.2963 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0500 | -0.1936 | -0.1936 | -0.1936 | 0.2904 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0483 | -0.1232 | -0.1232 | -0.1232 | 0.1847 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0485 | -0.0719 | -0.0719 | -0.0719 | 0.1079 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0404 | 0.0423 | 0.0423 | 0.0423 | 0.0635 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0319 | 0.0365 | 0.0365 | 0.0365 | 0.0548 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0373 | 0.0351 | 0.0351 | 0.0351 | 0.0526 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0296 | -0.0345 | -0.0345 | -0.0345 | 0.0518 |
| 10 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0201 | -0.0327 | -0.0327 | -0.0327 | 0.0490 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0324 | -0.0321 | -0.0321 | -0.0321 | 0.0482 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0395 | -0.0317 | -0.0317 | -0.0317 | 0.0475 |
| 13 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.1022 | 0.0306 | 0.0306 | 0.0306 | 0.0458 |
| 14 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0360 | -0.0282 | -0.0282 | -0.0282 | 0.0422 |
| 15 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0242 | 0.0249 | 0.0249 | 0.0249 | 0.0373 |
| 16 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0341 | -0.0235 | -0.0235 | -0.0235 | 0.0353 |
| 17 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0218 | 0.0228 | 0.0228 | 0.0228 | 0.0341 |
| 18 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0270 | 0.0225 | 0.0225 | 0.0225 | 0.0338 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0422 | 0.0209 | 0.0209 | 0.0209 | 0.0314 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0276 | 0.0208 | 0.0208 | 0.0208 | 0.0313 |
| 21 | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0221 | 0.0201 | 0.0201 | 0.0201 | 0.0302 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0237 | 0.0164 | 0.0164 | 0.0164 | 0.0246 |
| 23 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-muon | 0.0338 | 0.0144 | 0.0144 | 0.0144 | 0.0216 |
| 24 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0529 | -0.0143 | -0.0143 | -0.0143 | 0.0214 |
| 25 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0303 | -0.0140 | -0.0140 | -0.0140 | 0.0210 |
| 26 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0416 | 0.0139 | 0.0139 | 0.0139 | 0.0209 |
| 27 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0459 | 0.0135 | 0.0135 | 0.0135 | 0.0203 |
| 28 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0219 | 0.0134 | 0.0134 | 0.0134 | 0.0201 |
| 29 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0220 | 0.0127 | 0.0127 | 0.0127 | 0.0190 |
| 30 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0292 | -0.0125 | -0.0125 | -0.0125 | 0.0188 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
