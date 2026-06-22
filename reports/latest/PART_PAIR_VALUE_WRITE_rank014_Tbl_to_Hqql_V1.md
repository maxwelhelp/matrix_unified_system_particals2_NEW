# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9920**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.1102 | 0.3070 | 0.3070 | 1.1484 | 0.3070 | 152.1469 | 0.0253 | 0.9580 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0968 | 0.2573 | 0.2573 | 0.9816 | 0.2573 | 152.1469 | 0.0292 | 0.8124 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0924 | 0.2407 | 0.2407 | 0.9256 | 0.2407 | 152.1469 | 0.0305 | 0.7637 |
| 4 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0991 | 0.3227 | 0.3227 | 0.2946 | 0.1512 | 129.9786 | 0.0415 | 0.5507 |
| 5 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.1029 | 0.2181 | 0.2181 | 0.5417 | 0.2181 | 102.3998 | 0.0322 | 0.5435 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0896 | 0.2774 | 0.2774 | 0.2471 | 0.1575 | 115.3229 | 0.0393 | 0.4703 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.9109 | 0.0000 | 0.0000 | 0.0000 | 0.4555 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0849 | 0.1553 | 0.1553 | 0.4401 | 0.1553 | 102.3998 | 0.0289 | 0.4142 |
| 9 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0789 | 0.1344 | 0.1344 | 0.4232 | 0.1344 | 102.3998 | 0.0278 | 0.3796 |
| 10 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0813 | 0.1624 | 0.1705 | 0.0607 | 0.0365 | 73.6631 | 0.0241 | 0.2353 |
| 11 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0969 | 0.1428 | 0.1465 | 0.0901 | 0.0097 | 89.9998 | 0.0350 | 0.2244 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0857 | 0.1220 | 0.1259 | 0.0613 | 0.0295 | 79.1820 | 0.0333 | 0.1841 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0697 | 0.1238 | 0.1324 | 0.0343 | 0.0202 | 60.2323 | 0.0260 | 0.1740 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.3384 | 0.0000 | 0.0000 | 0.0000 | 0.1692 |
| 15 | mod.cls_blocks.1.attn.h3 | neutral_hadron<-electron | 0.0000 | 0.0000 | 0.0000 | 0.2654 | 1.554e-14 | 0.0000 | 0.0000 | 0.1327 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2628 | 0.0000 | 0.0000 | 0.0000 | 0.1314 |
| 17 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2599 | 0.0000 | 0.0000 | 0.0000 | 0.1299 |
| 18 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0767 | 0.0906 | 0.0935 | 0.0283 | -0.0059 | 53.6540 | 0.0227 | 0.1281 |
| 19 | mod.cls_blocks.1.attn.h0 | electron<-muon | 0.0000 | 0.0000 | 0.0000 | -0.2074 | 0.0000 | 0.0000 | 0.0000 | 0.1037 |
| 20 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.1667 | -0.0127 | 0.0127 | 0.1529 | -0.0127 | 3.6970 | 0.0505 | 0.0924 |
| 21 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0669 | 0.0687 | 0.0731 | -7.292e-04 | -0.0115 | 44.6367 | 0.0232 | 0.0873 |
| 22 | mod.cls_blocks.1.attn.h0 | muon<-electron | 0.0718 | 9.434e-04 | 9.434e-04 | -0.1676 | 9.434e-04 | 0.7917 | 0.0161 | 0.0850 |
| 23 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0000 | 0.0000 | 0.0000 | -0.1638 | -0.0109 | 0.0000 | 0.0000 | 0.0819 |
| 24 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.3000 | -0.0124 | 0.0124 | 0.1132 | -0.0124 | 4.2147 | 0.0325 | 0.0721 |
| 25 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.1429 | -0.0109 | 0.0109 | 0.1091 | -0.0109 | 3.4867 | 0.0491 | 0.0682 |
| 26 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1362 | 0.0000 | 0.0000 | 0.0000 | 0.0681 |
| 27 | mod.cls_blocks.0.attn.h1 | electron<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1286 | 0.0000 | 0.0000 | 0.0000 | 0.0643 |
| 28 | mod.cls_blocks.0.attn.h6 | muon<-electron | 0.0215 | -0.0018 | 0.0027 | -0.1199 | -0.0018 | 9.8201 | 0.0159 | 0.0624 |
| 29 | mod.cls_blocks.0.attn.h6 | electron<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1234 | 0.0000 | 0.0000 | 0.0000 | 0.0617 |
| 30 | mod.cls_blocks.1.attn.h3 | CLS<-electron | 0.2308 | -0.0096 | 0.0096 | 0.0946 | -0.0096 | 3.7613 | 0.0327 | 0.0592 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0961 | 0.3699 | 0.3699 | 0.3699 | 0.3699 | 152.1468 | 0.0415 | 0.6474 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0871 | 0.3179 | 0.3179 | 0.3179 | 0.3179 | 134.3242 | 0.0393 | 0.5563 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0817 | 0.2365 | 0.2369 | 0.2365 | 0.2365 | 113.4525 | 0.0241 | 0.4140 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0699 | 0.1808 | 0.1835 | 0.1808 | 0.1808 | 90.8396 | 0.0260 | 0.3171 |
| 5 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0949 | 0.1810 | 0.1810 | 0.1810 | 0.1810 | 102.3998 | 0.0350 | 0.3167 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0840 | 0.1548 | 0.1555 | 0.1548 | 0.1548 | 89.8106 | 0.0333 | 0.2710 |
| 7 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0740 | 0.1305 | 0.1308 | 0.1305 | 0.1305 | 76.2248 | 0.0227 | 0.2285 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0648 | 0.0994 | 0.1017 | 0.0994 | 0.0994 | 61.9988 | 0.0232 | 0.1746 |
| 9 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0508 | 0.0252 | 0.0252 | 0.0252 | 0.0252 | 64.1643 | 0.0273 | 0.0441 |
| 10 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0483 | 0.0235 | 0.0239 | 0.0235 | 0.0235 | 47.9650 | 0.0218 | 0.0413 |
| 11 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0462 | 0.0213 | 0.0219 | 0.0213 | 0.0213 | 57.2305 | 0.0271 | 0.0374 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0325 | -0.0198 | 0.0198 | -0.0198 | -0.0198 | 5.3053 | 0.0144 | 0.0347 |
| 13 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0371 | 0.0198 | 0.0198 | 0.0198 | 0.0198 | 66.5561 | 0.0300 | 0.0347 |
| 14 | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0245 | -0.0186 | 0.0201 | -0.0186 | -0.0186 | 5.8002 | 0.0086 | 0.0329 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0276 | 0.0143 | 0.0459 | 0.0143 | 0.0143 | 1.8289 | 0.0032 | 0.0329 |
| 16 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0427 | 0.0180 | 0.0188 | 0.0180 | 0.0180 | 39.2771 | 0.0219 | 0.0317 |
| 17 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0339 | 0.0169 | 0.0170 | 0.0169 | 0.0169 | 59.2135 | 0.0304 | 0.0296 |
| 18 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0454 | 0.0162 | 0.0162 | 0.0162 | 0.0162 | 42.4997 | 0.0256 | 0.0284 |
| 19 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0300 | 0.0148 | 0.0151 | 0.0148 | 0.0148 | 50.1545 | 0.0228 | 0.0259 |
| 20 | mod.cls_blocks.0.attn.h7 | electron<-electron | 0.0431 | 0.0145 | 0.0147 | 0.0145 | 0.0145 | 32.1493 | 0.0175 | 0.0254 |
| 21 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0415 | 0.0137 | 0.0141 | 0.0137 | 0.0137 | 38.7075 | 0.0248 | 0.0241 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0354 | 0.0119 | 0.0127 | 0.0119 | 0.0119 | 42.5699 | 0.0225 | 0.0210 |
| 23 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0376 | 0.0109 | 0.0118 | 0.0109 | 0.0109 | 27.0176 | 0.0174 | 0.0193 |
| 24 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0284 | -0.0103 | 0.0126 | -0.0103 | -0.0103 | 4.7874 | 0.0073 | 0.0186 |
| 25 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0295 | -0.0102 | 0.0119 | -0.0102 | -0.0102 | 5.7270 | 0.0107 | 0.0183 |
| 26 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0549 | -0.0102 | 0.0102 | -0.0102 | -0.0102 | 23.9238 | 0.0578 | 0.0178 |
| 27 | mod.cls_blocks.1.attn.h3 | electron<-neutral_hadron | 0.1000 | -0.0092 | 0.0092 | -0.0092 | -0.0092 | 0.7783 | 0.0081 | 0.0160 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0598 | -0.0090 | 0.0090 | -0.0090 | -0.0090 | 24.0962 | 0.0426 | 0.0158 |
| 29 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0163 | -0.0086 | 0.0099 | -0.0086 | -0.0086 | 1.2944 | 0.0030 | 0.0154 |
| 30 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0386 | 0.0084 | 0.0084 | 0.0084 | 0.0084 | 5.1960 | 0.0085 | 0.0148 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
