# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9936**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1311 | -0.5465 | 0.5465 | -0.7496 | -0.5465 | 152.1469 | 0.0351 | 1.0579 |
| 2 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.1410 | -0.5568 | 0.5568 | -0.6966 | -0.5568 | 152.1469 | 0.0335 | 1.0444 |
| 3 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.1212 | -0.5361 | 0.5361 | -0.7077 | -0.5361 | 152.1469 | 0.0367 | 1.0240 |
| 4 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1231 | -0.2968 | 0.2968 | -0.4043 | -0.2968 | 102.3998 | 0.0320 | 0.5731 |
| 5 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.1133 | -0.3149 | 0.3380 | -0.3228 | 0.4228 | 94.4469 | 0.0318 | 0.5608 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1184 | -0.2700 | 0.2700 | -0.3929 | -0.2700 | 102.3998 | 0.0309 | 0.5339 |
| 7 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.1137 | -0.2432 | 0.2432 | -0.3762 | -0.2432 | 102.3998 | 0.0299 | 0.4921 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.8323 | 0.0000 | 0.0000 | 0.0000 | 0.4162 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0831 | -0.1809 | 0.1947 | -0.1819 | 0.3385 | 62.5816 | 0.0353 | 0.3205 |
| 10 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0981 | -0.1422 | 0.1579 | -0.1661 | 0.1400 | 67.3844 | 0.0277 | 0.2647 |
| 11 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0775 | -0.0931 | 0.1180 | -0.1054 | 0.5917 | 52.8777 | 0.0201 | 0.1753 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0698 | -0.0829 | 0.0926 | -0.1011 | 0.1147 | 45.2705 | 0.0272 | 0.1566 |
| 13 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0388 | -0.0590 | 0.1756 | -0.0603 | -0.0436 | 5.6514 | 0.0085 | 0.1330 |
| 14 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2620 | 0.0000 | 0.0000 | 0.0000 | 0.1310 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0646 | -0.0644 | 0.0892 | -0.0724 | 0.3027 | 42.5212 | 0.0220 | 0.1229 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2375 | 0.0000 | 0.0000 | 0.0000 | 0.1187 |
| 17 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.2500 | 0.0229 | 0.0229 | 0.1361 | 0.0229 | 3.2318 | 0.0284 | 0.0966 |
| 18 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0733 | -0.0430 | 0.0565 | -0.0631 | 0.2458 | 39.4855 | 0.0185 | 0.0887 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1754 | 0.0000 | 0.0000 | 0.0000 | 0.0877 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0419 | 0.0453 | 0.0505 | 0.0509 | 0.0412 | 2.6008 | 0.0080 | 0.0834 |
| 21 | mod.cls_blocks.1.attn.h3 | CLS<-electron | 0.1818 | 0.0167 | 0.0167 | 0.1004 | 0.0167 | 2.8831 | 0.0286 | 0.0710 |
| 22 | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0741 | -0.0321 | 0.0321 | -0.0591 | -0.0321 | 64.1643 | 0.0198 | 0.0697 |
| 23 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0692 | -0.0300 | 0.0300 | -0.0600 | -0.0300 | 64.1643 | 0.0218 | 0.0675 |
| 24 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1344 | 0.0000 | 0.0000 | 0.0000 | 0.0672 |
| 25 | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0643 | -0.0279 | 0.0279 | -0.0605 | -0.0279 | 64.1643 | 0.0237 | 0.0651 |
| 26 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0636 | -0.0281 | 0.0444 | -0.0459 | 0.1122 | 33.0087 | 0.0195 | 0.0622 |
| 27 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0000 | 0.0000 | 0.0000 | 0.1156 | -0.0150 | 0.0000 | 0.0000 | 0.0578 |
| 28 | mod.cls_blocks.0.attn.h1 | electron<-CLS | 0.0437 | -0.0266 | 0.0266 | -0.0478 | -0.0266 | 66.5560 | 0.0261 | 0.0572 |
| 29 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0000 | 0.0000 | 0.0000 | 0.1058 | 0.0000 | 0.0000 | 0.0000 | 0.0529 |
| 30 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0436 | 0.0255 | 0.0355 | 0.0362 | 0.0248 | 7.2587 | 0.0218 | 0.0525 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.1070 | -0.4600 | 0.4610 | -0.4600 | -0.4600 | 124.4320 | 0.0318 | 0.8053 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0795 | -0.2638 | 0.2650 | -0.2638 | -0.2638 | 79.7159 | 0.0353 | 0.4620 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0795 | -0.2404 | 0.2409 | -0.2404 | -0.2404 | 84.0481 | 0.0201 | 0.4208 |
| 4 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0968 | -0.2109 | 0.2109 | -0.2109 | -0.2109 | 84.2672 | 0.0277 | 0.3690 |
| 5 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0659 | -0.1729 | 0.1780 | -0.1729 | -0.1729 | 65.2714 | 0.0220 | 0.3038 |
| 6 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0688 | -0.1232 | 0.1247 | -0.1232 | -0.1232 | 56.7803 | 0.0185 | 0.2160 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0691 | -0.1222 | 0.1229 | -0.1222 | -0.1222 | 54.9179 | 0.0272 | 0.2140 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0565 | -0.0895 | 0.0910 | -0.0895 | -0.0895 | 44.1696 | 0.0195 | 0.1569 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0388 | -0.0590 | 0.1756 | -0.0590 | -0.0590 | 5.6514 | 0.0085 | 0.1324 |
| 10 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0419 | 0.0453 | 0.0505 | 0.0453 | 0.0453 | 2.6008 | 0.0080 | 0.0806 |
| 11 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0366 | -0.0252 | 0.0480 | -0.0252 | -0.0252 | 4.3702 | 0.0045 | 0.0499 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0436 | 0.0255 | 0.0355 | 0.0255 | 0.0255 | 7.2587 | 0.0218 | 0.0471 |
| 13 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0556 | -0.0243 | 0.0243 | -0.0243 | -0.0243 | 53.5546 | 0.0215 | 0.0425 |
| 14 | mod.cls_blocks.1.attn.h3 | photon<-neutral_hadron | 0.1429 | -0.0232 | 0.0232 | -0.0232 | -0.0232 | 1.0257 | 0.0155 | 0.0405 |
| 15 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0378 | -0.0204 | 0.0204 | -0.0204 | -0.0204 | 55.0936 | 0.0266 | 0.0356 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0398 | -0.0183 | 0.0198 | -0.0183 | -0.0183 | 16.7571 | 0.0085 | 0.0323 |
| 17 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0791 | -0.0177 | 0.0177 | -0.0177 | -0.0177 | 20.1143 | 0.0324 | 0.0310 |
| 18 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0422 | 0.0165 | 0.0178 | 0.0165 | 0.0165 | 2.4135 | 0.0043 | 0.0292 |
| 19 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0479 | -0.0161 | 0.0161 | -0.0161 | -0.0161 | 35.6032 | 0.0201 | 0.0282 |
| 20 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0471 | -0.0155 | 0.0155 | -0.0155 | -0.0155 | 35.5318 | 0.0147 | 0.0271 |
| 21 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0386 | -0.0142 | 0.0149 | -0.0142 | -0.0142 | 39.2826 | 0.0266 | 0.0250 |
| 22 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0323 | -0.0137 | 0.0147 | -0.0137 | -0.0137 | 38.1038 | 0.0174 | 0.0243 |
| 23 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0447 | -0.0119 | 0.0158 | -0.0119 | -0.0119 | 36.0879 | 0.0218 | 0.0218 |
| 24 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0575 | -0.0122 | 0.0122 | -0.0122 | -0.0122 | 19.3881 | 0.0408 | 0.0214 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0387 | -0.0108 | 0.0122 | -0.0108 | -0.0108 | 28.7114 | 0.0152 | 0.0192 |
| 26 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0581 | 0.0105 | 0.0105 | 0.0105 | 0.0105 | 18.0514 | 0.0250 | 0.0183 |
| 27 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0332 | 0.0102 | 0.0119 | 0.0102 | 0.0102 | 1.8332 | 0.0028 | 0.0183 |
| 28 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0355 | 0.0097 | 0.0136 | 0.0097 | 0.0097 | 8.1398 | 0.0119 | 0.0179 |
| 29 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0295 | -0.0093 | 0.0115 | -0.0093 | -0.0093 | 31.0707 | 0.0183 | 0.0169 |
| 30 | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0279 | 0.0086 | 0.0092 | 0.0086 | 0.0086 | 5.5074 | 0.0106 | 0.0151 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
