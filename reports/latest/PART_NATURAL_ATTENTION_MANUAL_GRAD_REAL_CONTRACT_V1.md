# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **128**
- events_per_group: **32**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **10352**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0965 | -0.4598 | -0.5554 | 0.1175 | 0.7375 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.1114 | -0.4664 | -0.4746 | 0.2594 | 0.7037 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0857 | -0.3289 | -0.3797 | -0.0346 | 0.5187 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0861 | -0.2885 | -0.2944 | 0.1614 | 0.4357 |
| 5 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0864 | -0.1959 | -0.2687 | 0.0431 | 0.3303 |
| 6 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0971 | -0.2024 | -0.2480 | 0.0724 | 0.3264 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0777 | -0.1408 | -0.1849 | -0.0278 | 0.2332 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.4608 | 0.0000 | 0.2304 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0750 | -0.1246 | -0.1632 | 0.0418 | 0.2062 |
| 10 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | -0.3237 | 0.0000 | 0.1618 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | -0.2620 | 0.0000 | 0.1310 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0000 | 0.0000 | -0.2263 | 0.0000 | 0.1132 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.1718 | 0.0000 | 0.0859 |
| 14 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | -0.1482 | 0.0000 | 0.0741 |
| 15 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0510 | -0.0481 | -0.0493 | -0.0253 | 0.0727 |
| 16 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | -0.1398 | 0.0000 | 0.0699 |
| 17 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | -0.1344 | 0.0000 | 0.0672 |
| 18 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0000 | 0.0000 | -0.1250 | 0.0000 | 0.0625 |
| 19 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.1138 | 0.0399 | 0.0400 | 0.0399 | 0.0599 |
| 20 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0660 | -0.0367 | -0.0354 | -0.0368 | 0.0544 |
| 21 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.1477 | 9.817e-04 | 0.1068 | 9.817e-04 | 0.0544 |
| 22 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0000 | 0.0000 | -0.1075 | 0.0000 | 0.0538 |
| 23 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0536 | -0.0253 | -0.0490 | -0.0090 | 0.0498 |
| 24 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0597 | -0.0272 | -0.0440 | -0.0048 | 0.0492 |
| 25 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | -0.0942 | 0.0000 | 0.0471 |
| 26 | mod.cls_blocks.1.attn.h3 | charged_hadron<-muon | 9.317e-20 | -1.146e-20 | 0.0938 | -7.602e-18 | 0.0469 |
| 27 | mod.cls_blocks.0.attn.h7 | electron<-electron | 0.0415 | -0.0153 | -0.0605 | -0.0046 | 0.0456 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | -0.0910 | 0.0000 | 0.0455 |
| 29 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0495 | -0.0177 | -0.0537 | -0.0057 | 0.0446 |
| 30 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0924 | 0.0396 | 0.0069 | 0.0212 | 0.0430 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.1114 | -0.4664 | -0.4664 | -0.4664 | 0.6995 |
| 2 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0965 | -0.4598 | -0.4598 | -0.4598 | 0.6897 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0857 | -0.3289 | -0.3289 | -0.3289 | 0.4933 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0861 | -0.2885 | -0.2885 | -0.2885 | 0.4328 |
| 5 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0971 | -0.2024 | -0.2024 | -0.2024 | 0.3035 |
| 6 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0864 | -0.1959 | -0.1959 | -0.1959 | 0.2939 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0777 | -0.1408 | -0.1408 | -0.1408 | 0.2112 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0750 | -0.1246 | -0.1246 | -0.1246 | 0.1869 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0510 | -0.0481 | -0.0481 | -0.0481 | 0.0721 |
| 10 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.1138 | 0.0399 | 0.0399 | 0.0399 | 0.0599 |
| 11 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0924 | 0.0396 | 0.0396 | 0.0396 | 0.0594 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0660 | -0.0367 | -0.0367 | -0.0367 | 0.0551 |
| 13 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0590 | 0.0319 | 0.0319 | 0.0319 | 0.0478 |
| 14 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0597 | -0.0272 | -0.0272 | -0.0272 | 0.0409 |
| 15 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0498 | -0.0272 | -0.0272 | -0.0272 | 0.0408 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0519 | 0.0261 | 0.0261 | 0.0261 | 0.0392 |
| 17 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0536 | -0.0253 | -0.0253 | -0.0253 | 0.0379 |
| 18 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0601 | -0.0246 | -0.0246 | -0.0246 | 0.0369 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0677 | -0.0241 | -0.0241 | -0.0241 | 0.0362 |
| 20 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.1036 | 0.0215 | 0.0215 | 0.0215 | 0.0322 |
| 21 | mod.cls_blocks.0.attn.h4 | electron<-muon | 0.0214 | 0.0209 | 0.0209 | 0.0209 | 0.0314 |
| 22 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0353 | -0.0207 | -0.0207 | -0.0207 | 0.0310 |
| 23 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0377 | -0.0203 | -0.0203 | -0.0203 | 0.0304 |
| 24 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0398 | -0.0183 | -0.0183 | -0.0183 | 0.0274 |
| 25 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0495 | -0.0177 | -0.0177 | -0.0177 | 0.0266 |
| 26 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0791 | -0.0177 | -0.0177 | -0.0177 | 0.0266 |
| 27 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0465 | 0.0173 | 0.0173 | 0.0173 | 0.0260 |
| 28 | mod.cls_blocks.0.attn.h1 | charged_hadron<-photon | 0.0696 | 0.0167 | 0.0167 | 0.0167 | 0.0250 |
| 29 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0521 | -0.0154 | -0.0154 | -0.0154 | 0.0231 |
| 30 | mod.cls_blocks.0.attn.h7 | electron<-electron | 0.0415 | -0.0153 | -0.0153 | -0.0153 | 0.0230 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
