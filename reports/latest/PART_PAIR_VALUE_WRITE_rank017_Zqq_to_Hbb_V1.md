# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **10032**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1105 | -0.9876 | 0.9876 | -1.2045 | -0.9876 | 152.1469 | 0.0647 | 1.8367 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0797 | -0.8065 | 0.8065 | -0.8280 | -0.6130 | 152.1468 | 0.0744 | 1.4221 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1045 | -0.4355 | 0.6579 | -0.7395 | -0.4355 | 152.1469 | 0.0486 | 0.9697 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0881 | 0.4448 | 0.4448 | 0.3374 | 0.4448 | 152.1469 | 0.0395 | 0.7247 |
| 5 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1027 | -0.3153 | 0.3153 | -0.4293 | -0.3153 | 102.3998 | 0.0358 | 0.6088 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1088 | -0.2116 | 0.2116 | -0.6787 | -0.2116 | 152.1469 | 0.0255 | 0.6038 |
| 7 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.7982 | 0.0000 | 0.0000 | 0.0000 | 0.3991 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0957 | -0.1546 | 0.2274 | -0.2931 | -0.1546 | 102.3998 | 0.0283 | 0.3580 |
| 9 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0736 | -0.1975 | 0.1975 | -0.2082 | -0.1358 | 102.3998 | 0.0326 | 0.3510 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0968 | -0.1334 | 0.1334 | -0.3046 | -0.1334 | 102.3998 | 0.0180 | 0.3190 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0434 | -0.1807 | 0.2075 | -0.1595 | -0.0709 | 11.0727 | 0.0153 | 0.3123 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0483 | -0.1232 | 0.1574 | -0.1343 | -0.0561 | 41.4020 | 0.0546 | 0.2296 |
| 13 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0806 | 0.1455 | 0.1455 | 0.0366 | 0.1455 | 102.3998 | 0.0237 | 0.2001 |
| 14 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0612 | -0.0622 | 0.0622 | -0.1150 | -0.0622 | 64.1643 | 0.0345 | 0.1353 |
| 15 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2397 | 0.0000 | 0.0000 | 0.0000 | 0.1199 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0416 | -0.0632 | 0.0778 | -0.0620 | -0.0312 | 8.3876 | 0.0088 | 0.1137 |
| 17 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0539 | -0.0370 | 0.0438 | -0.0893 | -0.0370 | 64.1643 | 0.0292 | 0.0926 |
| 18 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0521 | -0.0372 | 0.0372 | -0.0916 | -0.0372 | 64.1643 | 0.0276 | 0.0923 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0382 | 0.0500 | 0.0505 | 0.0499 | 0.0502 | 25.7871 | 0.0640 | 0.0876 |
| 20 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0321 | -0.0379 | 0.1075 | -0.0288 | -0.0288 | 2.4233 | 0.0050 | 0.0792 |
| 21 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0267 | -0.0374 | 0.0374 | -0.0635 | -0.0374 | 66.5560 | 0.0349 | 0.0785 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0365 | 0.0395 | 0.0469 | 0.0513 | 0.0332 | 9.5143 | 0.0305 | 0.0768 |
| 23 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.1236 | 0.0430 | 0.0430 | 0.0402 | 0.0372 | 14.8099 | 0.0206 | 0.0738 |
| 24 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0404 | 0.0423 | 0.0423 | 0.0416 | 0.0385 | 22.9663 | 0.0640 | 0.0737 |
| 25 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0318 | 0.0368 | 0.0440 | 0.0493 | 0.0249 | 2.0825 | 0.0052 | 0.0724 |
| 26 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0201 | -0.0327 | 0.0327 | -0.0430 | -0.0291 | 66.5561 | 0.0329 | 0.0624 |
| 27 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0395 | -0.0317 | 0.0382 | -0.0347 | -0.0088 | 31.0767 | 0.0276 | 0.0586 |
| 28 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0270 | -0.0229 | 0.0247 | -0.0568 | -0.0229 | 66.5560 | 0.0295 | 0.0574 |
| 29 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0317 | -0.0205 | 0.0205 | -0.0593 | -0.0205 | 66.5560 | 0.0290 | 0.0553 |
| 30 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0360 | 0.0290 | 0.0290 | 0.0381 | 0.0276 | 25.3055 | 0.0262 | 0.0553 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0797 | -0.8065 | 0.8065 | -0.8065 | -0.8065 | 152.1468 | 0.0744 | 1.4114 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0500 | -0.1936 | 0.2245 | -0.1936 | -0.1936 | 13.0997 | 0.0153 | 0.3465 |
| 3 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0736 | -0.1975 | 0.1975 | -0.1975 | -0.1975 | 102.3998 | 0.0326 | 0.3456 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0483 | -0.1232 | 0.1574 | -0.1232 | -0.1232 | 41.4020 | 0.0546 | 0.2241 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0485 | -0.0719 | 0.0876 | -0.0719 | -0.0719 | 10.0077 | 0.0088 | 0.1298 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0324 | -0.0321 | 0.1121 | -0.0321 | -0.0321 | 2.5101 | 0.0050 | 0.0762 |
| 7 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0296 | -0.0345 | 0.0938 | -0.0345 | -0.0345 | 2.5823 | 0.0044 | 0.0752 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0404 | 0.0423 | 0.0423 | 0.0423 | 0.0423 | 22.9663 | 0.0640 | 0.0741 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0319 | 0.0365 | 0.0438 | 0.0365 | 0.0365 | 2.1114 | 0.0052 | 0.0658 |
| 10 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0373 | 0.0351 | 0.0457 | 0.0351 | 0.0351 | 9.3756 | 0.0305 | 0.0640 |
| 11 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0201 | -0.0327 | 0.0327 | -0.0327 | -0.0327 | 66.5561 | 0.0329 | 0.0572 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0395 | -0.0317 | 0.0382 | -0.0317 | -0.0317 | 31.0767 | 0.0276 | 0.0570 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0341 | -0.0235 | 0.0763 | -0.0235 | -0.0235 | 7.9829 | 0.0183 | 0.0543 |
| 14 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.1022 | 0.0306 | 0.0338 | 0.0306 | 0.0306 | 11.2338 | 0.0206 | 0.0543 |
| 15 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0360 | -0.0282 | 0.0282 | -0.0282 | -0.0282 | 64.1643 | 0.0390 | 0.0493 |
| 16 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0242 | 0.0249 | 0.0249 | 0.0249 | 0.0249 | 18.9159 | 0.0262 | 0.0435 |
| 17 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0270 | 0.0225 | 0.0283 | 0.0225 | 0.0225 | 5.7828 | 0.0150 | 0.0408 |
| 18 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0218 | 0.0228 | 0.0268 | 0.0228 | 0.0228 | 2.0524 | 0.0055 | 0.0408 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0276 | 0.0208 | 0.0283 | 0.0208 | 0.0208 | 1.6540 | 0.0043 | 0.0383 |
| 20 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0422 | 0.0209 | 0.0209 | 0.0209 | 0.0209 | 14.2704 | 0.0206 | 0.0366 |
| 21 | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0221 | 0.0201 | 0.0237 | 0.0201 | 0.0201 | 2.9364 | 0.0106 | 0.0361 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0237 | 0.0164 | 0.0164 | 0.0164 | 0.0164 | 15.1255 | 0.0548 | 0.0287 |
| 23 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0303 | -0.0140 | 0.0279 | -0.0140 | -0.0140 | 2.0224 | 0.0025 | 0.0280 |
| 24 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0220 | 0.0127 | 0.0270 | 0.0127 | 0.0127 | 1.6307 | 0.0049 | 0.0258 |
| 25 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-muon | 0.0338 | 0.0144 | 0.0144 | 0.0144 | 0.0144 | 16.7343 | 0.0343 | 0.0252 |
| 26 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0292 | -0.0125 | 0.0249 | -0.0125 | -0.0125 | 2.1806 | 0.0022 | 0.0250 |
| 27 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0529 | -0.0143 | 0.0143 | -0.0143 | -0.0143 | 29.1176 | 0.0494 | 0.0250 |
| 28 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0416 | 0.0139 | 0.0139 | 0.0139 | 0.0139 | 22.7517 | 0.0437 | 0.0243 |
| 29 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0459 | 0.0135 | 0.0141 | 0.0135 | 0.0135 | 8.7160 | 0.0131 | 0.0238 |
| 30 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0219 | 0.0134 | 0.0145 | 0.0134 | 0.0134 | 0.8772 | 0.0031 | 0.0237 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
