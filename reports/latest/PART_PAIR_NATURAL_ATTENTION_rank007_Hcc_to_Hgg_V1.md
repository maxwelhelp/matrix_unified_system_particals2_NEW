# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8688**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0632 | -0.1496 | -0.2698 | -0.1496 | 0.2845 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0728 | -0.1833 | -0.1918 | -0.1833 | 0.2792 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0632 | -0.1496 | -0.2563 | -0.1496 | 0.2777 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0728 | -0.1833 | -0.1533 | -0.1833 | 0.2600 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.2374 | 0.0000 | 0.1187 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.2183 | 0.0000 | 0.1092 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0000 | 0.0000 | -0.1745 | 0.0000 | 0.0872 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | -0.1417 | 0.0000 | 0.0709 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0171 | 0.0031 | -0.1069 | 0.0031 | 0.0565 |
| 10 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0247 | 0.0350 | -0.0311 | 0.0350 | 0.0505 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0203 | 0.0226 | -0.0435 | 0.0218 | 0.0443 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0271 | -0.0251 | -0.0353 | 0.0145 | 0.0428 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0370 | -0.0165 | -0.0478 | -0.0165 | 0.0403 |
| 14 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0370 | -0.0165 | -0.0437 | -0.0165 | 0.0383 |
| 15 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0676 | 0.0000 | 0.0338 |
| 16 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | -0.0672 | 0.0000 | 0.0336 |
| 17 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.0637 | 0.0000 | 0.0319 |
| 18 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0340 | -0.0240 | 0.0043 | 0.0180 | 0.0262 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | -0.0470 | 0.0000 | 0.0235 |
| 20 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | -0.0455 | 0.0000 | 0.0227 |
| 21 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | -0.0360 | 0.0000 | 0.0180 |
| 22 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0000 | 0.0000 | -0.0344 | 0.0000 | 0.0172 |
| 23 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0000 | 0.0000 | -0.0324 | 0.0000 | 0.0162 |
| 24 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0159 | 0.0102 | 0.0102 | 0.0102 | 0.0153 |
| 25 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0226 | 0.0057 | 0.0189 | 0.0014 | 0.0151 |
| 26 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0134 | 0.0116 | 0.0068 | 0.0116 | 0.0150 |
| 27 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0000 | 0.0000 | 0.0299 | 0.0000 | 0.0149 |
| 28 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0161 | 2.042e-04 | -0.0279 | 2.042e-04 | 0.0142 |
| 29 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0168 | 0.0085 | 0.0071 | 0.0017 | 0.0120 |
| 30 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0156 | 0.0043 | 0.0123 | -0.0052 | 0.0104 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0247 | 0.0350 | 0.0350 | 0.0350 | 0.0525 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0271 | -0.0251 | -0.0251 | -0.0251 | 0.0377 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0340 | -0.0240 | -0.0240 | -0.0240 | 0.0361 |
| 4 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0203 | 0.0226 | 0.0226 | 0.0226 | 0.0339 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0134 | 0.0116 | 0.0116 | 0.0116 | 0.0174 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0159 | 0.0102 | 0.0102 | 0.0102 | 0.0153 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0175 | 0.0093 | 0.0093 | 0.0093 | 0.0140 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0168 | 0.0086 | 0.0086 | 0.0086 | 0.0130 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0247 | 0.0079 | 0.0079 | 0.0079 | 0.0119 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0129 | 0.0073 | 0.0073 | 0.0073 | 0.0109 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0151 | 0.0070 | 0.0070 | 0.0070 | 0.0105 |
| 12 | mod.blocks.3.attn.h5 | muon<-muon | 0.2391 | -0.0058 | -0.0058 | -0.0058 | 0.0087 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0220 | -0.0055 | -0.0055 | -0.0055 | 0.0083 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0162 | 0.0055 | 0.0055 | 0.0055 | 0.0083 |
| 15 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0260 | 0.0049 | 0.0049 | 0.0049 | 0.0074 |
| 16 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0155 | 0.0047 | 0.0047 | 0.0047 | 0.0070 |
| 17 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0156 | 0.0043 | 0.0043 | 0.0043 | 0.0064 |
| 18 | mod.cls_blocks.0.attn.h5 | CLS<-muon | 0.0403 | -0.0043 | -0.0043 | -0.0043 | 0.0064 |
| 19 | mod.cls_blocks.0.attn.h5 | neutral_hadron<-muon | 0.0403 | -0.0043 | -0.0043 | -0.0043 | 0.0064 |
| 20 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0211 | 0.0037 | 0.0037 | 0.0037 | 0.0055 |
| 21 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0202 | -0.0033 | -0.0033 | -0.0033 | 0.0050 |
| 22 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0225 | -0.0032 | -0.0032 | -0.0032 | 0.0048 |
| 23 | mod.cls_blocks.0.attn.h3 | charged_hadron<-neutral_hadron | 0.0297 | -0.0031 | -0.0031 | -0.0031 | 0.0047 |
| 24 | mod.blocks.0.attn.h5 | muon<-muon | 0.4684 | 0.0031 | 0.0031 | 0.0031 | 0.0047 |
| 25 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0171 | 0.0031 | 0.0031 | 0.0031 | 0.0046 |
| 26 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0171 | 0.0031 | 0.0031 | 0.0031 | 0.0046 |
| 27 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0124 | 0.0030 | 0.0030 | 0.0030 | 0.0045 |
| 28 | mod.blocks.2.attn.h3 | muon<-muon | 0.1465 | 0.0029 | 0.0029 | 0.0029 | 0.0044 |
| 29 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0202 | 0.0029 | 0.0029 | 0.0029 | 0.0044 |
| 30 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0283 | -0.0028 | -0.0028 | -0.0028 | 0.0042 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
