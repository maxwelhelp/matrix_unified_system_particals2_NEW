# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9760**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0864 | -0.1377 | -0.3081 | -0.1377 | 0.2917 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0800 | -0.1002 | -0.1883 | -0.1002 | 0.1943 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0545 | -0.1210 | -0.1210 | 0.2586 | 0.1815 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0786 | -0.1137 | -0.0681 | -0.1137 | 0.1478 |
| 5 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0730 | -0.0934 | -0.0934 | -0.0934 | 0.1401 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0746 | -0.0833 | -0.1101 | -0.0833 | 0.1384 |
| 7 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0530 | -0.0462 | -0.1328 | -0.0462 | 0.1126 |
| 8 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.1042 | 0.0745 | 0.0755 | 0.0729 | 0.1122 |
| 9 | mod.cls_blocks.0.attn.h0 | electron<-muon | 0.1042 | 0.0745 | 0.0745 | 0.0745 | 0.1117 |
| 10 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0707 | -0.0708 | -0.0708 | -0.0708 | 0.1062 |
| 11 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0679 | -0.0621 | -0.0810 | -0.0621 | 0.1026 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0686 | -0.0861 | -0.0253 | -0.0861 | 0.0987 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0486 | -0.0411 | -0.1049 | -0.0411 | 0.0936 |
| 14 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0803 | -0.0570 | -0.0570 | 0.1340 | 0.0855 |
| 15 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0450 | -0.0366 | -0.0977 | -0.0366 | 0.0854 |
| 16 | mod.cls_blocks.1.attn.h3 | electron<-muon | 0.4982 | 0.0492 | 0.0492 | 0.0492 | 0.0738 |
| 17 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.4982 | 0.0492 | 0.0328 | 0.0491 | 0.0656 |
| 18 | mod.cls_blocks.0.attn.h1 | electron<-muon | 0.0631 | 0.0435 | 0.0435 | 0.0435 | 0.0653 |
| 19 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.1239 | 0.0000 | 0.0619 |
| 20 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0631 | 0.0435 | -0.0329 | 0.0478 | 0.0599 |
| 21 | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0432 | -0.0357 | -0.0357 | -0.0357 | 0.0535 |
| 22 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0000 | 0.0000 | -0.0982 | 0.0087 | 0.0491 |
| 23 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0237 | -0.0285 | -0.0316 | 0.0787 | 0.0443 |
| 24 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0958 | -0.0271 | -0.0271 | -0.0218 | 0.0406 |
| 25 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0000 | 0.0000 | -0.0752 | -0.0022 | 0.0376 |
| 26 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0000 | 0.0000 | -0.0651 | 0.0000 | 0.0326 |
| 27 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0416 | -0.0064 | -0.0472 | -0.0055 | 0.0300 |
| 28 | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0000 | 0.0000 | -0.0579 | 0.0000 | 0.0290 |
| 29 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0366 | -0.0120 | -0.0338 | 0.0416 | 0.0289 |
| 30 | mod.cls_blocks.1.attn.h4 | charged_hadron<-muon | 0.0000 | 0.0000 | -0.0572 | -4.563e-05 | 0.0286 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0749 | -0.1675 | -0.1675 | -0.1675 | 0.2513 |
| 2 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0694 | -0.0941 | -0.0941 | -0.0941 | 0.1411 |
| 3 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.1042 | 0.0745 | 0.0745 | 0.0745 | 0.1117 |
| 4 | mod.cls_blocks.0.attn.h0 | electron<-muon | 0.1042 | 0.0745 | 0.0745 | 0.0745 | 0.1117 |
| 5 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.4982 | 0.0492 | 0.0492 | 0.0492 | 0.0738 |
| 6 | mod.cls_blocks.1.attn.h3 | electron<-muon | 0.4982 | 0.0492 | 0.0492 | 0.0492 | 0.0738 |
| 7 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0631 | 0.0435 | 0.0435 | 0.0435 | 0.0653 |
| 8 | mod.cls_blocks.0.attn.h1 | electron<-muon | 0.0631 | 0.0435 | 0.0435 | 0.0435 | 0.0653 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0300 | -0.0401 | -0.0401 | -0.0401 | 0.0601 |
| 10 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0337 | -0.0275 | -0.0275 | -0.0275 | 0.0413 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0383 | -0.0242 | -0.0242 | -0.0242 | 0.0364 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0275 | -0.0221 | -0.0221 | -0.0221 | 0.0331 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0352 | -0.0199 | -0.0199 | -0.0199 | 0.0298 |
| 14 | mod.blocks.3.attn.h7 | electron<-muon | 0.4047 | -0.0177 | -0.0177 | -0.0177 | 0.0266 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-neutral_hadron | 0.0305 | 0.0175 | 0.0175 | 0.0175 | 0.0263 |
| 16 | mod.blocks.4.attn.h3 | electron<-muon | 0.3316 | -0.0170 | -0.0170 | -0.0170 | 0.0256 |
| 17 | mod.blocks.3.attn.h2 | electron<-muon | 0.3369 | 0.0167 | 0.0167 | 0.0167 | 0.0251 |
| 18 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0787 | 0.0163 | 0.0163 | 0.0163 | 0.0244 |
| 19 | mod.cls_blocks.0.attn.h7 | electron<-muon | 0.0787 | 0.0163 | 0.0163 | 0.0163 | 0.0244 |
| 20 | mod.cls_blocks.0.attn.h2 | photon<-neutral_hadron | 0.0420 | 0.0147 | 0.0147 | 0.0147 | 0.0220 |
| 21 | mod.blocks.4.attn.h3 | muon<-electron | 0.2720 | -0.0138 | -0.0138 | -0.0138 | 0.0208 |
| 22 | mod.blocks.2.attn.h0 | electron<-muon | 0.1685 | -0.0120 | -0.0120 | -0.0120 | 0.0181 |
| 23 | mod.blocks.4.attn.h2 | muon<-muon | 0.1898 | -0.0118 | -0.0118 | -0.0118 | 0.0177 |
| 24 | mod.blocks.7.attn.h5 | electron<-muon | 0.4394 | -0.0114 | -0.0114 | -0.0114 | 0.0171 |
| 25 | mod.blocks.1.attn.h2 | electron<-muon | 0.3231 | 0.0114 | 0.0114 | 0.0114 | 0.0171 |
| 26 | mod.cls_blocks.0.attn.h0 | electron<-neutral_hadron | 0.0268 | 0.0106 | 0.0106 | 0.0106 | 0.0159 |
| 27 | mod.blocks.3.attn.h5 | electron<-muon | 0.2874 | -0.0102 | -0.0102 | -0.0102 | 0.0153 |
| 28 | mod.cls_blocks.0.attn.h7 | electron<-electron | 0.0253 | -0.0099 | -0.0099 | -0.0099 | 0.0149 |
| 29 | mod.cls_blocks.0.attn.h0 | photon<-charged_hadron | 0.0398 | 0.0098 | 0.0098 | 0.0098 | 0.0148 |
| 30 | mod.blocks.3.attn.h7 | muon<-electron | 0.5159 | -0.0098 | -0.0098 | -0.0098 | 0.0147 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
