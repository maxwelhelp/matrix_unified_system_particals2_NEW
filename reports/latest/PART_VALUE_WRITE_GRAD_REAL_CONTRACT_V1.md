# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **128**
- events_per_group: **32**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **10352**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0965 | -0.4598 | 0.4601 | -0.5554 | 0.1175 | 115.8275 | 0.0327 | 0.8525 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.1114 | -0.4664 | 0.4670 | -0.4746 | 0.2594 | 135.0916 | 0.0334 | 0.8204 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0857 | -0.3289 | 0.3322 | -0.3797 | -0.0346 | 88.2643 | 0.0316 | 0.6017 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0861 | -0.2885 | 0.2932 | -0.2944 | 0.1614 | 91.3703 | 0.0394 | 0.5090 |
| 5 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0864 | -0.1959 | 0.1967 | -0.2687 | 0.0431 | 78.0694 | 0.0266 | 0.3794 |
| 6 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0971 | -0.2024 | 0.2024 | -0.2480 | 0.0724 | 91.2413 | 0.0281 | 0.3769 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0777 | -0.1408 | 0.1424 | -0.1849 | -0.0278 | 60.1486 | 0.0264 | 0.2688 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0750 | -0.1246 | 0.1287 | -0.1632 | 0.0418 | 63.5668 | 0.0293 | 0.2383 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.4608 | 0.0000 | 0.0000 | 0.0000 | 0.2304 |
| 10 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.3237 | 0.0000 | 0.0000 | 0.0000 | 0.1618 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2620 | 0.0000 | 0.0000 | 0.0000 | 0.1310 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2263 | 0.0000 | 0.0000 | 0.0000 | 0.1132 |
| 13 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0510 | -0.0481 | 0.1298 | -0.0493 | -0.0253 | 6.9859 | 0.0072 | 0.1052 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1718 | 0.0000 | 0.0000 | 0.0000 | 0.0859 |
| 15 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1482 | 0.0000 | 0.0000 | 0.0000 | 0.0741 |
| 16 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.1138 | 0.0399 | 0.0399 | 0.0400 | 0.0399 | 24.6384 | 0.0276 | 0.0699 |
| 17 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1398 | 0.0000 | 0.0000 | 0.0000 | 0.0699 |
| 18 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1344 | 0.0000 | 0.0000 | 0.0000 | 0.0672 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0660 | -0.0367 | 0.0367 | -0.0354 | -0.0368 | 27.6647 | 0.0332 | 0.0636 |
| 20 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1250 | 0.0000 | 0.0000 | 0.0000 | 0.0625 |
| 21 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.1477 | 9.817e-04 | 0.0098 | 0.1068 | 9.817e-04 | 30.0704 | 0.0299 | 0.0568 |
| 22 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0536 | -0.0253 | 0.0253 | -0.0490 | -0.0090 | 48.8936 | 0.0194 | 0.0561 |
| 23 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0597 | -0.0272 | 0.0272 | -0.0440 | -0.0048 | 57.6352 | 0.0223 | 0.0561 |
| 24 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1075 | 0.0000 | 0.0000 | 0.0000 | 0.0538 |
| 25 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0924 | 0.0396 | 0.0396 | 0.0069 | 0.0212 | 35.8112 | 0.0217 | 0.0530 |
| 26 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0519 | 0.0261 | 0.0388 | 0.0318 | 0.0217 | 3.4650 | 0.0072 | 0.0517 |
| 27 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0498 | -0.0272 | 0.0460 | -0.0242 | -0.0258 | 5.3942 | 0.0048 | 0.0508 |
| 28 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0601 | -0.0246 | 0.0785 | -0.0122 | -0.0083 | 3.8737 | 0.0037 | 0.0503 |
| 29 | mod.cls_blocks.0.attn.h7 | electron<-electron | 0.0415 | -0.0153 | 0.0155 | -0.0605 | -0.0046 | 32.6080 | 0.0183 | 0.0495 |
| 30 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0495 | -0.0177 | 0.0177 | -0.0537 | -0.0057 | 38.2557 | 0.0207 | 0.0490 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.1114 | -0.4664 | 0.4670 | -0.4664 | -0.4664 | 135.0916 | 0.0334 | 0.8163 |
| 2 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0965 | -0.4598 | 0.4601 | -0.4598 | -0.4598 | 115.8275 | 0.0327 | 0.8048 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0857 | -0.3289 | 0.3322 | -0.3289 | -0.3289 | 88.2643 | 0.0316 | 0.5763 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0861 | -0.2885 | 0.2932 | -0.2885 | -0.2885 | 91.3703 | 0.0394 | 0.5061 |
| 5 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0971 | -0.2024 | 0.2024 | -0.2024 | -0.2024 | 91.2413 | 0.0281 | 0.3541 |
| 6 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0864 | -0.1959 | 0.1967 | -0.1959 | -0.1959 | 78.0694 | 0.0266 | 0.3430 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0777 | -0.1408 | 0.1424 | -0.1408 | -0.1408 | 60.1486 | 0.0264 | 0.2468 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0750 | -0.1246 | 0.1287 | -0.1246 | -0.1246 | 63.5668 | 0.0293 | 0.2190 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0510 | -0.0481 | 0.1298 | -0.0481 | -0.0481 | 6.9859 | 0.0072 | 0.1046 |
| 10 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.1138 | 0.0399 | 0.0399 | 0.0399 | 0.0399 | 24.6384 | 0.0276 | 0.0699 |
| 11 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0924 | 0.0396 | 0.0396 | 0.0396 | 0.0396 | 35.8112 | 0.0217 | 0.0693 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0660 | -0.0367 | 0.0367 | -0.0367 | -0.0367 | 27.6647 | 0.0332 | 0.0642 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0601 | -0.0246 | 0.0785 | -0.0246 | -0.0246 | 3.8737 | 0.0037 | 0.0565 |
| 14 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0590 | 0.0319 | 0.0319 | 0.0319 | 0.0319 | 35.5978 | 0.0268 | 0.0558 |
| 15 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0498 | -0.0272 | 0.0460 | -0.0272 | -0.0272 | 5.3942 | 0.0048 | 0.0523 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0519 | 0.0261 | 0.0388 | 0.0261 | 0.0261 | 3.4650 | 0.0072 | 0.0489 |
| 17 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0597 | -0.0272 | 0.0272 | -0.0272 | -0.0272 | 57.6352 | 0.0223 | 0.0477 |
| 18 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0536 | -0.0253 | 0.0253 | -0.0253 | -0.0253 | 48.8936 | 0.0194 | 0.0443 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0677 | -0.0241 | 0.0241 | -0.0241 | -0.0241 | 24.0633 | 0.0454 | 0.0423 |
| 20 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.1036 | 0.0215 | 0.0215 | 0.0215 | 0.0215 | 18.5099 | 0.0220 | 0.0376 |
| 21 | mod.cls_blocks.0.attn.h4 | electron<-muon | 0.0214 | 0.0209 | 0.0209 | 0.0209 | 0.0209 | 18.8095 | 0.0666 | 0.0366 |
| 22 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0353 | -0.0207 | 0.0212 | -0.0207 | -0.0207 | 51.3815 | 0.0234 | 0.0363 |
| 23 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0377 | -0.0203 | 0.0203 | -0.0203 | -0.0203 | 59.5023 | 0.0274 | 0.0355 |
| 24 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0398 | -0.0183 | 0.0198 | -0.0183 | -0.0183 | 16.7571 | 0.0085 | 0.0323 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0465 | 0.0173 | 0.0252 | 0.0173 | 0.0173 | 8.9177 | 0.0191 | 0.0323 |
| 26 | mod.cls_blocks.0.attn.h1 | charged_hadron<-photon | 0.0696 | 0.0167 | 0.0250 | 0.0167 | 0.0167 | 8.3452 | 0.0092 | 0.0312 |
| 27 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0495 | -0.0177 | 0.0177 | -0.0177 | -0.0177 | 38.2557 | 0.0207 | 0.0310 |
| 28 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0791 | -0.0177 | 0.0177 | -0.0177 | -0.0177 | 20.1143 | 0.0324 | 0.0310 |
| 29 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0521 | -0.0154 | 0.0210 | -0.0154 | -0.0154 | 39.2431 | 0.0194 | 0.0283 |
| 30 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0634 | 0.0153 | 0.0204 | 0.0153 | 0.0153 | 7.1275 | 0.0087 | 0.0281 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
