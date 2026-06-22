# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9152**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0678 | 0.1123 | 0.1789 | 0.1123 | 0.2017 |
| 2 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0724 | 0.0809 | 0.1415 | 0.0809 | 0.1516 |
| 3 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0740 | 0.0704 | 0.1545 | 0.0704 | 0.1476 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0705 | 0.0586 | 0.0629 | 0.0586 | 0.0901 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0754 | -0.0432 | 0.0892 | -0.0432 | 0.0878 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0501 | -0.0347 | -0.0327 | 0.0316 | 0.0511 |
| 7 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0443 | 0.0234 | 0.0519 | 0.0234 | 0.0494 |
| 8 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0416 | 0.0129 | 0.0413 | 0.0175 | 0.0335 |
| 9 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0507 | 0.0168 | 0.0204 | 0.0162 | 0.0270 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.0411 | 0.0000 | 0.0205 |
| 11 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0252 | -0.0095 | -0.0180 | -0.0095 | 0.0185 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0742 | -0.0177 | -7.581e-04 | -0.0177 | 0.0181 |
| 13 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0338 | 0.0110 | 0.0135 | 0.0103 | 0.0178 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0253 | -0.0083 | -0.0183 | -0.0083 | 0.0174 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0444 | 0.0091 | 0.0134 | 0.0091 | 0.0158 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0295 | 0.0000 | 0.0147 |
| 17 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0443 | 0.0103 | 0.0074 | -0.0290 | 0.0140 |
| 18 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0353 | 0.0098 | 0.0083 | 0.0098 | 0.0140 |
| 19 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0421 | 0.0093 | 0.0089 | 0.0093 | 0.0137 |
| 20 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0363 | -5.730e-04 | 0.0249 | -0.0011 | 0.0130 |
| 21 | mod.cls_blocks.1.attn.h3 | neutral_hadron<-muon | 0.0309 | 3.111e-05 | 0.0255 | 3.111e-05 | 0.0128 |
| 22 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0254 | -0.0045 | -0.0157 | -0.0045 | 0.0124 |
| 23 | mod.cls_blocks.1.attn.h2 | photon<-CLS | 0.2686 | 0.0082 | 0.0083 | 0.0082 | 0.0123 |
| 24 | mod.cls_blocks.1.attn.h3 | charged_hadron<-electron | 0.2069 | 0.0040 | 0.0151 | 0.0045 | 0.0116 |
| 25 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0314 | -0.0065 | -0.0097 | -0.0113 | 0.0113 |
| 26 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0322 | 0.0069 | 0.0062 | 0.0045 | 0.0100 |
| 27 | mod.cls_blocks.0.attn.h3 | charged_hadron<-electron | 0.0185 | 9.504e-04 | 0.0178 | 0.0077 | 0.0099 |
| 28 | mod.cls_blocks.1.attn.h0 | neutral_hadron<-muon | 0.1340 | 0.0065 | 0.0066 | 0.0065 | 0.0098 |
| 29 | mod.cls_blocks.1.attn.h2 | CLS<-CLS | 0.2035 | 0.0061 | 0.0062 | 0.0061 | 0.0092 |
| 30 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0267 | 0.0051 | 0.0073 | -0.0090 | 0.0087 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0501 | -0.0347 | -0.0347 | -0.0347 | 0.0521 |
| 2 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0443 | 0.0234 | 0.0234 | 0.0234 | 0.0352 |
| 3 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0336 | 0.0129 | 0.0129 | 0.0129 | 0.0194 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0443 | 0.0103 | 0.0103 | 0.0103 | 0.0154 |
| 5 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0322 | 0.0069 | 0.0069 | 0.0069 | 0.0104 |
| 6 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-muon | 0.0341 | -0.0068 | -0.0068 | -0.0068 | 0.0102 |
| 7 | mod.cls_blocks.1.attn.h0 | neutral_hadron<-muon | 0.1340 | 0.0065 | 0.0065 | 0.0065 | 0.0098 |
| 8 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0314 | -0.0065 | -0.0065 | -0.0065 | 0.0098 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0289 | 0.0060 | 0.0060 | 0.0060 | 0.0090 |
| 10 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0173 | -0.0056 | -0.0056 | -0.0056 | 0.0084 |
| 11 | mod.blocks.3.attn.h0 | electron<-muon | 0.1659 | -0.0055 | -0.0055 | -0.0055 | 0.0082 |
| 12 | mod.blocks.2.attn.h3 | muon<-electron | 0.1556 | 0.0055 | 0.0055 | 0.0055 | 0.0082 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0289 | 0.0048 | 0.0048 | 0.0048 | 0.0073 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0240 | 0.0045 | 0.0045 | 0.0045 | 0.0067 |
| 15 | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0211 | 0.0044 | 0.0044 | 0.0044 | 0.0066 |
| 16 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-charged_hadron | 0.0312 | -0.0043 | -0.0043 | -0.0043 | 0.0065 |
| 17 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0310 | 0.0038 | 0.0038 | 0.0038 | 0.0057 |
| 18 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0159 | -0.0037 | -0.0037 | -0.0037 | 0.0056 |
| 19 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0201 | 0.0037 | 0.0037 | 0.0037 | 0.0055 |
| 20 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0297 | -0.0036 | -0.0036 | -0.0036 | 0.0054 |
| 21 | mod.cls_blocks.0.attn.h3 | CLS<-muon | 0.0189 | -0.0034 | -0.0034 | -0.0034 | 0.0051 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0203 | -0.0033 | -0.0033 | -0.0033 | 0.0049 |
| 23 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0242 | -0.0033 | -0.0033 | -0.0033 | 0.0049 |
| 24 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0232 | 0.0033 | 0.0033 | 0.0033 | 0.0049 |
| 25 | mod.cls_blocks.1.attn.h0 | CLS<-muon | 0.0691 | 0.0032 | 0.0032 | 0.0032 | 0.0048 |
| 26 | mod.cls_blocks.0.attn.h3 | CLS<-neutral_hadron | 0.0277 | -0.0032 | -0.0032 | -0.0032 | 0.0048 |
| 27 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0155 | 0.0032 | 0.0032 | 0.0032 | 0.0048 |
| 28 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0172 | -0.0032 | -0.0032 | -0.0032 | 0.0048 |
| 29 | mod.cls_blocks.1.attn.h5 | neutral_hadron<-muon | 0.0250 | 0.0032 | 0.0032 | 0.0032 | 0.0048 |
| 30 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0238 | -0.0032 | -0.0032 | -0.0032 | 0.0048 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
