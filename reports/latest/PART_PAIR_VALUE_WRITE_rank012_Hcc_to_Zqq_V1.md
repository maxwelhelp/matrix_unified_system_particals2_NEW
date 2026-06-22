# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8288**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1168 | 0.2980 | 0.2980 | 1.7572 | 0.2980 | 152.1469 | 0.0257 | 1.2510 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0956 | 0.4700 | 0.4700 | 1.1441 | 0.4700 | 152.1469 | 0.0404 | 1.1595 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1021 | 0.3984 | 0.3984 | 1.0262 | 0.3984 | 152.1469 | 0.0351 | 1.0111 |
| 4 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.1003 | 0.3558 | 0.3558 | 0.3558 | 0.3558 | 152.1469 | 0.0339 | 0.6226 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.1023 | 0.0978 | 0.0978 | 0.5441 | 0.0978 | 102.3998 | 0.0176 | 0.3943 |
| 6 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0814 | 0.1477 | 0.1477 | 0.3941 | 0.1477 | 102.3998 | 0.0223 | 0.3816 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0878 | 0.1218 | 0.1218 | 0.3226 | 0.1218 | 102.3998 | 0.0210 | 0.3136 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.5502 | 0.0000 | 0.0000 | 0.0000 | 0.2751 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0650 | 0.1158 | 0.1217 | 0.1132 | 0.0471 | 35.7951 | 0.0129 | 0.2028 |
| 10 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0860 | 0.0941 | 0.0941 | 0.0941 | 0.0941 | 102.3998 | 0.0217 | 0.1647 |
| 11 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2622 | 0.0000 | 0.0000 | 0.0000 | 0.1311 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1654 | 0.0000 | 0.0000 | 0.0000 | 0.0827 |
| 13 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0780 | 0.0209 | 0.0209 | 0.1088 | 0.0209 | 64.1643 | 0.0128 | 0.0805 |
| 14 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0273 | 0.0338 | 0.0338 | 0.0563 | 0.0338 | 66.5560 | 0.0412 | 0.0703 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0303 | -0.0222 | 0.0248 | -0.0759 | -0.0155 | 2.7833 | 0.0028 | 0.0664 |
| 16 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1271 | 0.0000 | 0.0000 | 0.0000 | 0.0636 |
| 17 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0319 | -0.0261 | 0.0295 | -0.0563 | -0.0237 | 1.7828 | 0.0040 | 0.0616 |
| 18 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0418 | -0.0294 | 0.0386 | -0.0414 | -0.0212 | 8.7975 | 0.0154 | 0.0598 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0415 | 0.0348 | 0.0352 | 0.0269 | 0.0138 | 24.1952 | 0.0078 | 0.0570 |
| 20 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0577 | 0.0203 | 0.0258 | 0.0515 | 0.0203 | 64.1643 | 0.0184 | 0.0525 |
| 21 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0310 | 0.0324 | 0.0569 | 0.0106 | 0.0319 | 2.2004 | 0.0038 | 0.0519 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0273 | 0.0226 | 0.0226 | 0.0427 | 0.0226 | 66.5560 | 0.0333 | 0.0496 |
| 23 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0321 | 0.0117 | 0.0117 | 0.0640 | 0.0117 | 66.5560 | 0.0209 | 0.0466 |
| 24 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0916 | 0.0000 | 0.0000 | 0.0000 | 0.0458 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0621 | 0.0145 | 0.0190 | 0.0444 | 0.0145 | 64.1643 | 0.0176 | 0.0414 |
| 26 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.2214 | -0.0235 | 0.0235 | -0.0235 | -0.0260 | 54.8273 | 0.0209 | 0.0411 |
| 27 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0353 | 0.0235 | 0.0595 | 0.0047 | 0.0184 | 2.0219 | 0.0028 | 0.0407 |
| 28 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0757 | -9.565e-11 | 0.0000 | 0.0000 | 0.0378 |
| 29 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0712 | 2.463e-04 | 0.0000 | 0.0000 | 0.0356 |
| 30 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0511 | 0.0131 | 0.0131 | 0.0358 | 0.0131 | 42.4997 | 0.0138 | 0.0342 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0780 | 0.1759 | 0.1763 | 0.1759 | 0.1759 | 41.0778 | 0.0129 | 0.3079 |
| 2 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0447 | 0.1210 | 0.1210 | 0.1210 | 0.1210 | 20.2648 | 0.0113 | 0.2118 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0332 | 0.0624 | 0.0624 | 0.0624 | 0.0624 | 20.2428 | 0.0157 | 0.1093 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0668 | 0.0540 | 0.0546 | 0.0540 | 0.0540 | 28.8049 | 0.0078 | 0.0946 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0323 | 0.0396 | 0.0659 | 0.0396 | 0.0396 | 2.3861 | 0.0038 | 0.0759 |
| 6 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0424 | 0.0322 | 0.0322 | 0.0322 | 0.0322 | 14.7820 | 0.0072 | 0.0563 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0418 | -0.0294 | 0.0386 | -0.0294 | -0.0294 | 8.7975 | 0.0154 | 0.0538 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0353 | 0.0235 | 0.0595 | 0.0235 | 0.0235 | 2.0219 | 0.0028 | 0.0501 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0316 | -0.0229 | 0.0287 | -0.0229 | -0.0229 | 1.7641 | 0.0040 | 0.0415 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0299 | -0.0222 | 0.0250 | -0.0222 | -0.0222 | 2.7882 | 0.0028 | 0.0395 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0306 | 0.0158 | 0.0459 | 0.0158 | 0.0158 | 2.4423 | 0.0038 | 0.0352 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0319 | -0.0194 | 0.0237 | -0.0194 | -0.0194 | 5.6475 | 0.0100 | 0.0350 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0294 | 0.0163 | 0.0165 | 0.0163 | 0.0163 | 15.5461 | 0.0103 | 0.0286 |
| 14 | mod.cls_blocks.0.attn.h5 | electron<-neutral_hadron | 0.0505 | -0.0155 | 0.0176 | -0.0155 | -0.0155 | 7.0896 | 0.0110 | 0.0277 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0283 | -0.0147 | 0.0181 | -0.0147 | -0.0147 | 2.4841 | 0.0047 | 0.0266 |
| 16 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0320 | 0.0122 | 0.0192 | 0.0122 | 0.0122 | 1.9539 | 0.0020 | 0.0231 |
| 17 | mod.cls_blocks.1.attn.h3 | electron<-neutral_hadron | 0.3333 | -0.0110 | 0.0110 | -0.0110 | -0.0110 | 1.1086 | 0.0054 | 0.0192 |
| 18 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0419 | 0.0105 | 0.0105 | 0.0105 | 0.0105 | 29.5984 | 0.0257 | 0.0185 |
| 19 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0419 | -0.0099 | 0.0107 | -0.0099 | -0.0099 | 8.4844 | 0.0091 | 0.0176 |
| 20 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0516 | 0.0093 | 0.0098 | 0.0093 | 0.0093 | 18.9860 | 0.0059 | 0.0164 |
| 21 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0349 | 0.0076 | 0.0194 | 0.0076 | 0.0076 | 1.7881 | 0.0017 | 0.0162 |
| 22 | mod.cls_blocks.0.attn.h4 | electron<-photon | 0.0249 | -0.0087 | 0.0126 | -0.0087 | -0.0087 | 2.1335 | 0.0028 | 0.0162 |
| 23 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0394 | -0.0026 | 0.0411 | -0.0026 | -0.0026 | 9.8945 | 0.0119 | 0.0142 |
| 24 | mod.cls_blocks.0.attn.h4 | electron<-charged_hadron | 0.0262 | -0.0073 | 0.0116 | -0.0073 | -0.0073 | 1.4439 | 0.0020 | 0.0139 |
| 25 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0323 | -0.0029 | 0.0362 | -0.0029 | -0.0029 | 1.8094 | 0.0032 | 0.0133 |
| 26 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0616 | -0.0062 | 0.0098 | -0.0062 | -0.0062 | 8.9201 | 0.0134 | 0.0118 |
| 27 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0319 | -0.0063 | 0.0074 | -0.0063 | -0.0063 | 1.5955 | 0.0022 | 0.0113 |
| 28 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0298 | 0.0050 | 0.0134 | 0.0050 | 0.0050 | 2.0947 | 0.0022 | 0.0109 |
| 29 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0347 | -0.0055 | 0.0099 | -0.0055 | -0.0055 | 4.9580 | 0.0096 | 0.0107 |
| 30 | mod.cls_blocks.0.attn.h6 | electron<-neutral_hadron | 0.0614 | 0.0056 | 0.0056 | 0.0056 | 0.0056 | 8.1641 | 0.0072 | 0.0098 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
