# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9120**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0815 | 0.7067 | 0.7067 | 0.9495 | 0.7067 | 152.1469 | 0.0699 | 1.3582 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0774 | 0.4105 | 0.4105 | 0.6951 | 0.4105 | 152.1469 | 0.0527 | 0.8607 |
| 3 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0743 | 0.1692 | 0.1775 | 0.1931 | 0.1692 | 102.3998 | 0.0457 | 0.3101 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0734 | 0.1143 | 0.1143 | 0.3014 | 0.1143 | 152.1469 | 0.0355 | 0.2935 |
| 5 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.1882 | -0.1377 | 0.1377 | -0.1320 | -0.1318 | 36.9031 | 0.0270 | 0.2381 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.4503 | 0.0000 | 0.0000 | 0.0000 | 0.2251 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0686 | 0.0768 | 0.1087 | 0.1171 | 0.0768 | 102.3998 | 0.0393 | 0.1625 |
| 8 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2236 | 0.0000 | 0.0000 | 0.0000 | 0.1118 |
| 9 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1891 | 0.0000 | 0.0000 | 0.0000 | 0.0945 |
| 10 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0395 | 0.0477 | 0.0477 | 0.0593 | 0.0477 | 64.1643 | 0.0398 | 0.0892 |
| 11 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0393 | 0.0405 | 0.0405 | 0.0603 | 0.0405 | 64.1643 | 0.0406 | 0.0807 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1575 | -0.0015 | 0.0000 | 0.0000 | 0.0787 |
| 13 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1564 | 0.0000 | 0.0000 | 0.0000 | 0.0782 |
| 14 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0390 | 0.0333 | 0.0333 | 0.0602 | 0.0333 | 64.1643 | 0.0413 | 0.0717 |
| 15 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0562 | -0.0379 | 0.0379 | -0.0417 | -0.0410 | 27.0695 | 0.0306 | 0.0682 |
| 16 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0231 | 0.0320 | 0.0320 | 0.0381 | 0.0320 | 66.5560 | 0.0424 | 0.0591 |
| 17 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | -0.1164 | 0.0000 | 0.0000 | 0.0000 | 0.0582 |
| 18 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0156 | 6.123e-04 | 6.123e-04 | -0.1138 | -8.649e-04 | 21.6675 | 0.0289 | 0.0577 |
| 19 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | -0.1058 | 0.0000 | 0.0000 | 0.0000 | 0.0529 |
| 20 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0223 | 0.0271 | 0.0271 | 0.0371 | 0.0271 | 66.5560 | 0.0419 | 0.0524 |
| 21 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1022 | 0.0000 | 0.0000 | 0.0000 | 0.0511 |
| 22 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0463 | -0.0272 | 0.0272 | -0.0323 | -0.0269 | 27.7941 | 0.0331 | 0.0501 |
| 23 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0000 | 0.0000 | 0.0000 | -0.0974 | 0.0000 | 0.0000 | 0.0000 | 0.0487 |
| 24 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0364 | 0.0255 | 0.0255 | 0.0331 | 0.0255 | 42.4997 | 0.0285 | 0.0484 |
| 25 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0963 | 0.0000 | 0.0000 | 0.0000 | 0.0482 |
| 26 | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0577 | -0.0274 | 0.0302 | -0.0233 | -0.0238 | 22.0942 | 0.0293 | 0.0466 |
| 27 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0215 | 0.0222 | 0.0222 | 0.0376 | 0.0222 | 66.5560 | 0.0413 | 0.0465 |
| 28 | mod.cls_blocks.1.attn.h3 | photon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0827 | 0.0000 | 0.0000 | 0.0000 | 0.0413 |
| 29 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0338 | 0.0193 | 0.0193 | 0.0292 | 0.0193 | 42.4997 | 0.0247 | 0.0387 |
| 30 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0304 | 0.0120 | 0.0181 | 0.0355 | 0.0031 | 6.7894 | 0.0069 | 0.0343 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.1882 | -0.1377 | 0.1377 | -0.1377 | -0.1377 | 36.9031 | 0.0270 | 0.2409 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0319 | 0.0450 | 0.0558 | 0.0450 | 0.0450 | 8.1359 | 0.0069 | 0.0814 |
| 3 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0562 | -0.0379 | 0.0379 | -0.0379 | -0.0379 | 27.0695 | 0.0306 | 0.0663 |
| 4 | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0604 | -0.0292 | 0.0294 | -0.0292 | -0.0292 | 20.4098 | 0.0293 | 0.0512 |
| 5 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0463 | -0.0272 | 0.0272 | -0.0272 | -0.0272 | 27.7941 | 0.0331 | 0.0475 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0258 | 0.0150 | 0.0243 | 0.0150 | 0.0150 | 5.4916 | 0.0064 | 0.0285 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0313 | 0.0112 | 0.0168 | 0.0112 | 0.0112 | 6.2898 | 0.0054 | 0.0210 |
| 8 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0585 | -0.0112 | 0.0112 | -0.0112 | -0.0112 | 19.8039 | 0.0182 | 0.0197 |
| 9 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0992 | 0.0109 | 0.0112 | 0.0109 | 0.0109 | 2.6241 | 0.0635 | 0.0192 |
| 10 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0211 | -0.0104 | 0.0115 | -0.0104 | -0.0104 | 19.7913 | 0.0491 | 0.0184 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0207 | -0.0091 | 0.0100 | -0.0091 | -0.0091 | 19.1760 | 0.0444 | 0.0161 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0174 | -0.0087 | 0.0106 | -0.0087 | -0.0087 | 1.8616 | 0.0030 | 0.0157 |
| 13 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0798 | 0.0087 | 0.0090 | 0.0087 | 0.0087 | 2.4751 | 0.0621 | 0.0153 |
| 14 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0227 | -0.0078 | 0.0127 | -0.0078 | -0.0078 | 1.0700 | 0.0017 | 0.0149 |
| 15 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0247 | -0.0080 | 0.0080 | -0.0080 | -0.0080 | 20.3210 | 0.0371 | 0.0140 |
| 16 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0314 | -0.0068 | 0.0130 | -0.0068 | -0.0068 | 18.6037 | 0.0347 | 0.0134 |
| 17 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0280 | -0.0076 | 0.0076 | -0.0076 | -0.0076 | 19.5261 | 0.0316 | 0.0133 |
| 18 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0280 | -0.0076 | 0.0076 | -0.0076 | -0.0076 | 19.5261 | 0.0316 | 0.0133 |
| 19 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0167 | -0.0066 | 0.0083 | -0.0066 | -0.0066 | 1.5035 | 0.0023 | 0.0119 |
| 20 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0261 | -0.0060 | 0.0096 | -0.0060 | -0.0060 | 2.8846 | 0.0058 | 0.0114 |
| 21 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0237 | 0.0040 | 0.0185 | 0.0040 | 0.0040 | 1.4474 | 0.0017 | 0.0106 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0163 | -0.0056 | 0.0072 | -0.0056 | -0.0056 | 1.3446 | 0.0020 | 0.0103 |
| 23 | mod.cls_blocks.1.attn.h5 | CLS<-muon | 0.0960 | 0.0057 | 0.0057 | 0.0057 | 0.0057 | 3.3524 | 0.0556 | 0.0100 |
| 24 | mod.cls_blocks.1.attn.h5 | charged_hadron<-muon | 0.0960 | 0.0057 | 0.0057 | 0.0057 | 0.0057 | 3.3524 | 0.0556 | 0.0100 |
| 25 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0257 | 0.0048 | 0.0086 | 0.0048 | 0.0048 | 4.5679 | 0.0051 | 0.0094 |
| 26 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0265 | 0.0039 | 0.0135 | 0.0039 | 0.0039 | 4.3663 | 0.0059 | 0.0092 |
| 27 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0238 | 0.0044 | 0.0071 | 0.0044 | 0.0044 | 5.3289 | 0.0063 | 0.0084 |
| 28 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0306 | 0.0045 | 0.0045 | 0.0045 | 0.0045 | 11.6889 | 0.0369 | 0.0078 |
| 29 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0306 | 0.0045 | 0.0045 | 0.0045 | 0.0045 | 11.6889 | 0.0369 | 0.0078 |
| 30 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0136 | -0.0044 | 0.0044 | -0.0044 | -0.0044 | 27.5361 | 0.0380 | 0.0077 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
