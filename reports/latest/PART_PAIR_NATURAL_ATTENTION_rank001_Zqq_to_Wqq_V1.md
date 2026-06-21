# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **96**
- events_per_group: **24**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9024**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 1.0850 | 0.0000 | 0.5425 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 1.0817 | 0.0000 | 0.5408 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.9806 | 0.0000 | 0.4903 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0000 | 0.0000 | 0.9166 | 0.0000 | 0.4583 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.6789 | 0.0000 | 0.3394 |
| 6 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.4178 | 0.0000 | 0.2089 |
| 7 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0000 | 0.0000 | 0.3780 | 0.0000 | 0.1890 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.3006 | 0.0000 | 0.1503 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0717 | 0.0989 | 0.0974 | 0.0899 | 0.1476 |
| 10 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0000 | 0.0000 | 0.2459 | 0.0000 | 0.1229 |
| 11 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.2255 | 0.0000 | 0.1128 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.1811 | 0.0000 | 0.0905 |
| 13 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0000 | 0.0000 | 0.1593 | 0.0000 | 0.0796 |
| 14 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | -0.1227 | 0.0000 | 0.0613 |
| 15 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0000 | 0.0000 | -0.0821 | 0.0000 | 0.0411 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0638 | 0.0259 | 0.0250 | 0.0224 | 0.0384 |
| 17 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0410 | -0.0263 | -0.0154 | -8.426e-05 | 0.0340 |
| 18 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0613 | 6.354e-04 | -0.0658 | 5.890e-04 | 0.0336 |
| 19 | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0000 | 0.0000 | 0.0623 | 0.0000 | 0.0312 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0372 | 0.0267 | 0.0043 | -0.0019 | 0.0289 |
| 21 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0365 | 0.0190 | 0.0177 | 0.0037 | 0.0279 |
| 22 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0000 | 0.0000 | -0.0539 | 0.0000 | 0.0269 |
| 23 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0241 | -0.0077 | -0.0375 | -3.026e-04 | 0.0264 |
| 24 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0000 | 0.0000 | 0.0528 | 0.0000 | 0.0264 |
| 25 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0525 | 0.0000 | 0.0263 |
| 26 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0000 | 0.0000 | 0.0497 | 0.0000 | 0.0248 |
| 27 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0126 | -3.799e-05 | -0.0492 | -3.799e-05 | 0.0247 |
| 28 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0350 | -0.0046 | -0.0366 | 0.0068 | 0.0229 |
| 29 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0000 | 0.0000 | 0.0457 | 0.0000 | 0.0228 |
| 30 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0357 | -0.0091 | -0.0262 | -0.0055 | 0.0222 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0717 | 0.0989 | 0.0989 | 0.0989 | 0.1483 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0372 | 0.0267 | 0.0267 | 0.0267 | 0.0401 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0410 | -0.0263 | -0.0263 | -0.0263 | 0.0395 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0638 | 0.0259 | 0.0259 | 0.0259 | 0.0388 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0365 | 0.0190 | 0.0190 | 0.0190 | 0.0285 |
| 6 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0353 | 0.0151 | 0.0151 | 0.0151 | 0.0227 |
| 7 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0687 | 0.0141 | 0.0141 | 0.0141 | 0.0212 |
| 8 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0332 | -0.0118 | -0.0118 | -0.0118 | 0.0177 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0332 | -0.0118 | -0.0118 | -0.0118 | 0.0177 |
| 10 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0371 | -0.0118 | -0.0118 | -0.0118 | 0.0176 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0357 | -0.0091 | -0.0091 | -0.0091 | 0.0137 |
| 12 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0514 | 0.0082 | 0.0082 | 0.0082 | 0.0123 |
| 13 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.0336 | -0.0080 | -0.0080 | -0.0080 | 0.0121 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0459 | 0.0079 | 0.0079 | 0.0079 | 0.0118 |
| 15 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0327 | -0.0077 | -0.0077 | -0.0077 | 0.0116 |
| 16 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0241 | -0.0077 | -0.0077 | -0.0077 | 0.0115 |
| 17 | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0415 | -0.0060 | -0.0060 | -0.0060 | 0.0090 |
| 18 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0470 | 0.0060 | 0.0060 | 0.0060 | 0.0090 |
| 19 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0359 | 0.0059 | 0.0059 | 0.0059 | 0.0089 |
| 20 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0396 | 0.0059 | 0.0059 | 0.0059 | 0.0088 |
| 21 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0370 | 0.0058 | 0.0058 | 0.0058 | 0.0087 |
| 22 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0829 | -0.0055 | -0.0055 | -0.0055 | 0.0083 |
| 23 | mod.blocks.5.attn.h4 | muon<-neutral_hadron | 0.2870 | 0.0055 | 0.0055 | 0.0055 | 0.0082 |
| 24 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0442 | 0.0053 | 0.0053 | 0.0053 | 0.0079 |
| 25 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0541 | -0.0051 | -0.0051 | -0.0051 | 0.0076 |
| 26 | mod.blocks.5.attn.h7 | electron<-muon | 0.7233 | 0.0051 | 0.0051 | 0.0051 | 0.0076 |
| 27 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0452 | 0.0050 | 0.0050 | 0.0050 | 0.0075 |
| 28 | mod.cls_blocks.0.attn.h2 | charged_hadron<-electron | 0.0329 | -0.0049 | -0.0049 | -0.0049 | 0.0073 |
| 29 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0350 | -0.0046 | -0.0046 | -0.0046 | 0.0069 |
| 30 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0342 | 0.0046 | 0.0046 | 0.0046 | 0.0068 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
