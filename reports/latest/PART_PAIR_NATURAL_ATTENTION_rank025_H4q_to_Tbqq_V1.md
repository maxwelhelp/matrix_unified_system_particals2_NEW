# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9120**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0881 | -0.6735 | -0.7643 | -0.6735 | 1.0557 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0732 | -0.3326 | -0.3609 | -0.3326 | 0.5130 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0724 | -0.3573 | -0.3012 | -0.3573 | 0.5079 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0716 | -0.1868 | -0.1843 | -0.1868 | 0.2790 |
| 5 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0624 | -0.1072 | -0.0643 | -0.1072 | 0.1393 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0626 | -0.0917 | -0.0781 | -0.0917 | 0.1308 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0600 | 0.0578 | 0.1068 | 0.0578 | 0.1112 |
| 8 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.2051 | -0.0459 | -0.0462 | -0.0459 | 0.0689 |
| 9 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0541 | 0.0343 | 0.0510 | 0.0343 | 0.0599 |
| 10 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0305 | 0.0198 | 0.0750 | 0.0126 | 0.0573 |
| 11 | mod.cls_blocks.0.attn.h7 | charged_hadron<-electron | 0.0269 | 0.0176 | 0.0759 | 0.0097 | 0.0556 |
| 12 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0353 | -0.0195 | -0.0330 | -0.0195 | 0.0360 |
| 13 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0285 | 0.0156 | 0.0406 | 0.0089 | 0.0359 |
| 14 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0305 | 0.0198 | 0.0198 | 0.0086 | 0.0298 |
| 15 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0280 | 0.0200 | 0.0187 | 0.0244 | 0.0294 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0701 | 0.0193 | 0.0186 | 0.0193 | 0.0286 |
| 17 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0000 | 0.0000 | 0.0552 | -0.0095 | 0.0276 |
| 18 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0340 | -0.0145 | -0.0261 | -0.0145 | 0.0275 |
| 19 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0260 | -0.0129 | -0.0256 | -0.0129 | 0.0257 |
| 20 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0227 | -0.0141 | -0.0221 | -0.0141 | 0.0251 |
| 21 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0249 | -0.0138 | -0.0223 | -0.0138 | 0.0250 |
| 22 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0270 | -0.0111 | -0.0223 | -0.0111 | 0.0223 |
| 23 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0358 | -0.0114 | -0.0211 | -0.0114 | 0.0219 |
| 24 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0201 | 0.0146 | 0.0133 | 0.0169 | 0.0213 |
| 25 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0187 | 0.0093 | 0.0224 | -0.0237 | 0.0205 |
| 26 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0337 | -0.0092 | -0.0203 | -0.0092 | 0.0193 |
| 27 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0231 | -0.0103 | -0.0176 | -0.0103 | 0.0191 |
| 28 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0394 | 0.0151 | 0.0068 | 0.0151 | 0.0185 |
| 29 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0212 | -0.0085 | -0.0147 | -0.0085 | 0.0159 |
| 30 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0308 | -0.0106 | -0.0106 | -0.0129 | 0.0158 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0264 | 0.0219 | 0.0219 | 0.0219 | 0.0329 |
| 2 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0305 | 0.0198 | 0.0198 | 0.0198 | 0.0298 |
| 3 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0305 | 0.0198 | 0.0198 | 0.0198 | 0.0298 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0238 | -0.0155 | -0.0155 | -0.0155 | 0.0232 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0208 | 0.0132 | 0.0132 | 0.0132 | 0.0198 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0205 | 0.0131 | 0.0131 | 0.0131 | 0.0196 |
| 7 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0202 | 0.0117 | 0.0117 | 0.0117 | 0.0175 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0308 | -0.0106 | -0.0106 | -0.0106 | 0.0158 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0198 | 0.0104 | 0.0104 | 0.0104 | 0.0156 |
| 10 | mod.cls_blocks.0.attn.h3 | charged_hadron<-electron | 0.0259 | -0.0090 | -0.0090 | -0.0090 | 0.0134 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0201 | 0.0085 | 0.0085 | 0.0085 | 0.0127 |
| 12 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0582 | -0.0074 | -0.0074 | -0.0074 | 0.0112 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0180 | 0.0072 | 0.0072 | 0.0072 | 0.0109 |
| 14 | mod.cls_blocks.0.attn.h7 | photon<-neutral_hadron | 0.0265 | 0.0072 | 0.0072 | 0.0072 | 0.0108 |
| 15 | mod.cls_blocks.0.attn.h3 | CLS<-electron | 0.0234 | -0.0071 | -0.0071 | -0.0071 | 0.0107 |
| 16 | mod.cls_blocks.0.attn.h3 | photon<-neutral_hadron | 0.0280 | -0.0065 | -0.0065 | -0.0065 | 0.0097 |
| 17 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0187 | -0.0061 | -0.0061 | -0.0061 | 0.0092 |
| 18 | mod.cls_blocks.0.attn.h5 | CLS<-muon | 0.0215 | 0.0056 | 0.0056 | 0.0056 | 0.0084 |
| 19 | mod.cls_blocks.0.attn.h5 | charged_hadron<-muon | 0.0215 | 0.0056 | 0.0056 | 0.0056 | 0.0084 |
| 20 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0224 | -0.0052 | -0.0052 | -0.0052 | 0.0078 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0156 | -0.0052 | -0.0052 | -0.0052 | 0.0077 |
| 22 | mod.cls_blocks.0.attn.h7 | charged_hadron<-electron | 0.0147 | 0.0049 | 0.0049 | 0.0049 | 0.0074 |
| 23 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0311 | -0.0049 | -0.0049 | -0.0049 | 0.0074 |
| 24 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0131 | 0.0046 | 0.0046 | 0.0046 | 0.0069 |
| 25 | mod.cls_blocks.0.attn.h7 | CLS<-neutral_hadron | 0.0193 | 0.0044 | 0.0044 | 0.0044 | 0.0067 |
| 26 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0180 | 0.0044 | 0.0044 | 0.0044 | 0.0066 |
| 27 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0179 | 0.0043 | 0.0043 | 0.0043 | 0.0064 |
| 28 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0186 | 0.0042 | 0.0042 | 0.0042 | 0.0063 |
| 29 | mod.cls_blocks.0.attn.h7 | charged_hadron<-neutral_hadron | 0.0173 | 0.0041 | 0.0041 | 0.0041 | 0.0061 |
| 30 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0272 | -0.0040 | -0.0040 | -0.0040 | 0.0059 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
