# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9760**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0864 | -0.1377 | 0.1377 | -0.3081 | -0.1377 | 152.1469 | 0.0200 | 0.3262 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0800 | -0.1002 | 0.1002 | -0.1883 | -0.1002 | 102.3998 | 0.0184 | 0.2194 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0545 | -0.1210 | 0.1210 | -0.1210 | 0.2586 | 87.0852 | 0.0303 | 0.2117 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0786 | -0.1137 | 0.1137 | -0.0681 | -0.1137 | 152.1469 | 0.0183 | 0.1762 |
| 5 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0730 | -0.0934 | 0.0934 | -0.0934 | -0.0934 | 152.1469 | 0.0166 | 0.1635 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0746 | -0.0833 | 0.0833 | -0.1101 | -0.0833 | 102.3998 | 0.0169 | 0.1592 |
| 7 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.1042 | 0.0745 | 0.0745 | 0.0755 | 0.0729 | 12.5215 | 0.0194 | 0.1308 |
| 8 | mod.cls_blocks.0.attn.h0 | electron<-muon | 0.1042 | 0.0745 | 0.0745 | 0.0745 | 0.0745 | 12.5215 | 0.0194 | 0.1303 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0530 | -0.0462 | 0.0462 | -0.1328 | -0.0462 | 64.1643 | 0.0350 | 0.1241 |
| 10 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0707 | -0.0708 | 0.0708 | -0.0708 | -0.0708 | 102.3998 | 0.0155 | 0.1239 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0686 | -0.0861 | 0.0861 | -0.0253 | -0.0861 | 152.1469 | 0.0164 | 0.1202 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0679 | -0.0621 | 0.0621 | -0.0810 | -0.0621 | 102.3998 | 0.0154 | 0.1181 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0486 | -0.0411 | 0.0411 | -0.1049 | -0.0411 | 64.1643 | 0.0343 | 0.1039 |
| 14 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0803 | -0.0570 | 0.0604 | -0.0570 | 0.1340 | 68.2977 | 0.0220 | 0.1006 |
| 15 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0450 | -0.0366 | 0.0366 | -0.0977 | -0.0366 | 64.1643 | 0.0333 | 0.0945 |
| 16 | mod.cls_blocks.1.attn.h3 | electron<-muon | 0.4982 | 0.0492 | 0.0492 | 0.0492 | 0.0492 | 1.6979 | 0.0199 | 0.0861 |
| 17 | mod.cls_blocks.0.attn.h1 | electron<-muon | 0.0631 | 0.0435 | 0.0522 | 0.0435 | 0.0435 | 13.5826 | 0.0246 | 0.0783 |
| 18 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.4982 | 0.0492 | 0.0492 | 0.0328 | 0.0491 | 1.6979 | 0.0199 | 0.0779 |
| 19 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0631 | 0.0435 | 0.0522 | -0.0329 | 0.0478 | 13.5826 | 0.0246 | 0.0730 |
| 20 | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0432 | -0.0357 | 0.0357 | -0.0357 | -0.0357 | 64.1643 | 0.0337 | 0.0625 |
| 21 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1239 | 0.0000 | 0.0000 | 0.0000 | 0.0619 |
| 22 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0237 | -0.0285 | 0.0320 | -0.0316 | 0.0787 | 36.4467 | 0.0189 | 0.0523 |
| 23 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0982 | 0.0087 | 0.0000 | 0.0000 | 0.0491 |
| 24 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0958 | -0.0271 | 0.0311 | -0.0271 | -0.0218 | 57.5140 | 0.0413 | 0.0484 |
| 25 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0752 | -0.0022 | 0.0000 | 0.0000 | 0.0376 |
| 26 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0366 | -0.0120 | 0.0173 | -0.0338 | 0.0416 | 28.1726 | 0.0171 | 0.0332 |
| 27 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0416 | -0.0064 | 0.0106 | -0.0472 | -0.0055 | 28.2115 | 0.0340 | 0.0326 |
| 28 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0651 | 0.0000 | 0.0000 | 0.0000 | 0.0326 |
| 29 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0329 | 0.0184 | 0.0184 | 0.0184 | 0.0030 | 20.1449 | 0.0361 | 0.0322 |
| 30 | mod.blocks.3.attn.h7 | electron<-muon | 0.4047 | -0.0177 | 0.0179 | -0.0177 | -0.0181 | 2.8662 | 0.0081 | 0.0311 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0749 | -0.1675 | 0.1675 | -0.1675 | -0.1675 | 152.1468 | 0.0303 | 0.2932 |
| 2 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0694 | -0.0941 | 0.0941 | -0.0941 | -0.0941 | 102.3998 | 0.0220 | 0.1647 |
| 3 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.1042 | 0.0745 | 0.0745 | 0.0745 | 0.0745 | 12.5215 | 0.0194 | 0.1303 |
| 4 | mod.cls_blocks.0.attn.h0 | electron<-muon | 0.1042 | 0.0745 | 0.0745 | 0.0745 | 0.0745 | 12.5215 | 0.0194 | 0.1303 |
| 5 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.4982 | 0.0492 | 0.0492 | 0.0492 | 0.0492 | 1.6979 | 0.0199 | 0.0861 |
| 6 | mod.cls_blocks.1.attn.h3 | electron<-muon | 0.4982 | 0.0492 | 0.0492 | 0.0492 | 0.0492 | 1.6979 | 0.0199 | 0.0861 |
| 7 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0631 | 0.0435 | 0.0522 | 0.0435 | 0.0435 | 13.5826 | 0.0246 | 0.0783 |
| 8 | mod.cls_blocks.0.attn.h1 | electron<-muon | 0.0631 | 0.0435 | 0.0522 | 0.0435 | 0.0435 | 13.5826 | 0.0246 | 0.0783 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0300 | -0.0401 | 0.0437 | -0.0401 | -0.0401 | 53.6409 | 0.0189 | 0.0710 |
| 10 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0337 | -0.0275 | 0.0275 | -0.0275 | -0.0275 | 64.1643 | 0.0363 | 0.0482 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0383 | -0.0242 | 0.0283 | -0.0242 | -0.0242 | 13.4049 | 0.0044 | 0.0434 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0275 | -0.0221 | 0.0250 | -0.0221 | -0.0221 | 35.9289 | 0.0171 | 0.0394 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0352 | -0.0199 | 0.0230 | -0.0199 | -0.0199 | 9.2722 | 0.0042 | 0.0356 |
| 14 | mod.blocks.3.attn.h7 | electron<-muon | 0.4047 | -0.0177 | 0.0179 | -0.0177 | -0.0177 | 2.8662 | 0.0081 | 0.0311 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-neutral_hadron | 0.0305 | 0.0175 | 0.0183 | 0.0175 | 0.0175 | 8.9345 | 0.0132 | 0.0309 |
| 16 | mod.blocks.4.attn.h3 | electron<-muon | 0.3316 | -0.0170 | 0.0170 | -0.0170 | -0.0170 | 3.1032 | 0.0093 | 0.0298 |
| 17 | mod.blocks.3.attn.h2 | electron<-muon | 0.3369 | 0.0167 | 0.0167 | 0.0167 | 0.0167 | 4.0638 | 0.0088 | 0.0293 |
| 18 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0787 | 0.0163 | 0.0163 | 0.0163 | 0.0163 | 8.0929 | 0.0110 | 0.0285 |
| 19 | mod.cls_blocks.0.attn.h7 | electron<-muon | 0.0787 | 0.0163 | 0.0163 | 0.0163 | 0.0163 | 8.0929 | 0.0110 | 0.0285 |
| 20 | mod.cls_blocks.0.attn.h2 | photon<-neutral_hadron | 0.0420 | 0.0147 | 0.0149 | 0.0147 | 0.0147 | 8.4917 | 0.0081 | 0.0257 |
| 21 | mod.blocks.4.attn.h3 | muon<-electron | 0.2720 | -0.0138 | 0.0138 | -0.0138 | -0.0138 | 4.0714 | 0.0062 | 0.0242 |
| 22 | mod.blocks.2.attn.h0 | electron<-muon | 0.1685 | -0.0120 | 0.0120 | -0.0120 | -0.0120 | 4.2115 | 0.0122 | 0.0211 |
| 23 | mod.blocks.4.attn.h2 | muon<-muon | 0.1898 | -0.0118 | 0.0118 | -0.0118 | -0.0118 | 2.0764 | 0.0043 | 0.0206 |
| 24 | mod.blocks.7.attn.h5 | electron<-muon | 0.4394 | -0.0114 | 0.0114 | -0.0114 | -0.0114 | 4.7446 | 0.0041 | 0.0200 |
| 25 | mod.cls_blocks.0.attn.h0 | photon<-charged_hadron | 0.0398 | 0.0098 | 0.0209 | 0.0098 | 0.0098 | 1.4277 | 0.0024 | 0.0200 |
| 26 | mod.blocks.1.attn.h2 | electron<-muon | 0.3231 | 0.0114 | 0.0114 | 0.0114 | 0.0114 | 4.6852 | 0.0079 | 0.0199 |
| 27 | mod.cls_blocks.0.attn.h0 | electron<-neutral_hadron | 0.0268 | 0.0106 | 0.0123 | 0.0106 | 0.0106 | 2.8207 | 0.0056 | 0.0189 |
| 28 | mod.blocks.3.attn.h5 | electron<-muon | 0.2874 | -0.0102 | 0.0102 | -0.0102 | -0.0102 | 4.4417 | 0.0066 | 0.0178 |
| 29 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0247 | 0.0094 | 0.0138 | 0.0094 | 0.0094 | 5.1086 | 0.0099 | 0.0176 |
| 30 | mod.cls_blocks.0.attn.h7 | electron<-electron | 0.0253 | -0.0099 | 0.0099 | -0.0099 | -0.0099 | 42.4997 | 0.0187 | 0.0173 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
