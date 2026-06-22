# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9984**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0739 | -0.0619 | -0.2883 | -0.0619 | 0.2061 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0698 | -0.0459 | -0.2059 | -0.0459 | 0.1488 |
| 3 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | -0.2177 | 0.0000 | 0.1089 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | -0.2136 | 0.0000 | 0.1068 |
| 5 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0728 | -0.0232 | -0.0911 | -0.0232 | 0.0688 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0292 | -0.0396 | -0.0511 | -0.0541 | 0.0651 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0677 | -0.0165 | -0.0696 | -0.0165 | 0.0512 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0201 | -0.0055 | -0.0901 | -0.0072 | 0.0505 |
| 9 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0406 | 0.0296 | 0.0407 | 0.0296 | 0.0500 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0573 | 0.0024 | -0.0854 | 0.0024 | 0.0451 |
| 11 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0296 | 0.0208 | 0.0457 | 0.0144 | 0.0437 |
| 12 | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0444 | -0.0293 | -0.0270 | -0.0264 | 0.0428 |
| 13 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0115 | -0.0022 | -0.0786 | 9.511e-04 | 0.0415 |
| 14 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0376 | 0.0252 | 0.0327 | 0.0252 | 0.0415 |
| 15 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0053 | -7.075e-04 | 0.0702 | 4.262e-04 | 0.0358 |
| 16 | mod.cls_blocks.0.attn.h7 | photon<-muon | 0.0289 | -0.0042 | 0.0567 | -0.0045 | 0.0326 |
| 17 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | -0.0634 | 0.0000 | 0.0317 |
| 18 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | -0.0632 | 0.0000 | 0.0316 |
| 19 | mod.cls_blocks.0.attn.h7 | photon<-electron | 0.0091 | -0.0013 | 0.0561 | -0.0087 | 0.0293 |
| 20 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0310 | -0.0202 | -0.0164 | -0.0224 | 0.0284 |
| 21 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | 0.0558 | 0.0000 | 0.0279 |
| 22 | mod.cls_blocks.0.attn.h7 | charged_hadron<-electron | 0.0020 | 6.657e-06 | 0.0555 | -0.0100 | 0.0278 |
| 23 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.0000 | 0.0000 | 0.0546 | 0.0000 | 0.0273 |
| 24 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0272 | 0.0047 | 0.0448 | -0.0016 | 0.0271 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0218 | 0.0077 | 0.0367 | 0.0073 | 0.0261 |
| 26 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0000 | 0.0000 | -0.0508 | 0.0000 | 0.0254 |
| 27 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0000 | 0.0000 | 0.0490 | -0.0067 | 0.0245 |
| 28 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0115 | 0.0149 | 0.0144 | -0.0238 | 0.0221 |
| 29 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0202 | 0.0127 | 0.0156 | 0.0127 | 0.0204 |
| 30 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0287 | 0.0118 | 0.0172 | 0.0118 | 0.0204 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0306 | -0.0386 | -0.0386 | -0.0386 | 0.0580 |
| 2 | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0444 | -0.0293 | -0.0293 | -0.0293 | 0.0440 |
| 3 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0296 | 0.0208 | 0.0208 | 0.0208 | 0.0312 |
| 4 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0310 | -0.0202 | -0.0202 | -0.0202 | 0.0303 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0115 | 0.0149 | 0.0149 | 0.0149 | 0.0224 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0176 | 0.0122 | 0.0122 | 0.0122 | 0.0183 |
| 7 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0185 | 0.0119 | 0.0119 | 0.0119 | 0.0178 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0183 | 0.0117 | 0.0117 | 0.0117 | 0.0175 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0343 | -0.0112 | -0.0112 | -0.0112 | 0.0168 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0162 | 0.0095 | 0.0095 | 0.0095 | 0.0143 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0137 | 0.0089 | 0.0089 | 0.0089 | 0.0133 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0237 | 0.0080 | 0.0080 | 0.0080 | 0.0120 |
| 13 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0136 | -0.0080 | -0.0080 | -0.0080 | 0.0120 |
| 14 | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0241 | -0.0080 | -0.0080 | -0.0080 | 0.0120 |
| 15 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0125 | -0.0080 | -0.0080 | -0.0080 | 0.0120 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0218 | 0.0077 | 0.0077 | 0.0077 | 0.0116 |
| 17 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0198 | 0.0075 | 0.0075 | 0.0075 | 0.0112 |
| 18 | mod.cls_blocks.0.attn.h7 | charged_hadron<-neutral_hadron | 0.0197 | 0.0072 | 0.0072 | 0.0072 | 0.0108 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0265 | -0.0071 | -0.0071 | -0.0071 | 0.0107 |
| 20 | mod.cls_blocks.1.attn.h2 | photon<-muon | 0.0473 | 0.0069 | 0.0069 | 0.0069 | 0.0104 |
| 21 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0150 | 0.0069 | 0.0069 | 0.0069 | 0.0103 |
| 22 | mod.cls_blocks.0.attn.h7 | CLS<-neutral_hadron | 0.0227 | 0.0067 | 0.0067 | 0.0067 | 0.0101 |
| 23 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0228 | -0.0065 | -0.0065 | -0.0065 | 0.0098 |
| 24 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-neutral_hadron | 0.0271 | 0.0065 | 0.0065 | 0.0065 | 0.0097 |
| 25 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0214 | 0.0064 | 0.0064 | 0.0064 | 0.0096 |
| 26 | mod.cls_blocks.0.attn.h7 | photon<-neutral_hadron | 0.0212 | 0.0063 | 0.0063 | 0.0063 | 0.0094 |
| 27 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0175 | 0.0062 | 0.0062 | 0.0062 | 0.0094 |
| 28 | mod.cls_blocks.1.attn.h1 | photon<-muon | 0.1262 | -0.0061 | -0.0061 | -0.0061 | 0.0091 |
| 29 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0140 | -0.0057 | -0.0057 | -0.0057 | 0.0086 |
| 30 | mod.cls_blocks.0.attn.h7 | charged_hadron<-charged_hadron | 0.0186 | 0.0056 | 0.0056 | 0.0056 | 0.0085 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
