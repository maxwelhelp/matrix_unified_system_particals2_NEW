# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8768**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0779 | 0.1604 | 0.3581 | 0.1604 | 0.3394 |
| 2 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0828 | 0.1573 | 0.3099 | 0.1573 | 0.3123 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0678 | 0.1492 | 0.2948 | 0.1492 | 0.2966 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1043 | 0.1129 | 0.3383 | 0.1129 | 0.2820 |
| 5 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0821 | 0.1208 | 0.3205 | 0.1208 | 0.2810 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0675 | 0.1176 | 0.2705 | 0.1176 | 0.2529 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0683 | 0.0495 | 0.2397 | 0.0495 | 0.1693 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0517 | 0.0148 | 0.1945 | 0.0148 | 0.1121 |
| 9 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.2059 | 0.0723 | 0.0723 | 0.0723 | 0.1084 |
| 10 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.1044 | 0.0597 | 0.0597 | 0.0597 | 0.0896 |
| 11 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0681 | 0.0372 | 0.0540 | 0.0372 | 0.0642 |
| 12 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0513 | 0.0266 | 0.0422 | 0.0266 | 0.0478 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0524 | 0.0258 | 0.0418 | 0.0258 | 0.0466 |
| 14 | mod.cls_blocks.1.attn.h3 | photon<-muon | 0.9770 | 0.0302 | 0.0302 | 0.0302 | 0.0453 |
| 15 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0290 | 0.0282 | 0.0282 | -0.0616 | 0.0423 |
| 16 | mod.cls_blocks.1.attn.h4 | neutral_hadron<-electron | 0.7833 | 0.0243 | 0.0243 | 0.0243 | 0.0364 |
| 17 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0785 | 0.0219 | 0.0219 | 0.0237 | 0.0329 |
| 18 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0471 | 0.0196 | 0.0196 | 0.0076 | 0.0294 |
| 19 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0390 | 0.0125 | 0.0295 | 0.0125 | 0.0273 |
| 20 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0316 | 0.0143 | 0.0189 | -0.0434 | 0.0237 |
| 21 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-electron | 0.0785 | 0.0129 | 0.0129 | 0.0129 | 0.0194 |
| 22 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.1002 | 0.0126 | 0.0126 | 0.0126 | 0.0190 |
| 23 | mod.cls_blocks.1.attn.h4 | photon<-muon | 0.9369 | 0.0125 | 0.0125 | 0.0125 | 0.0188 |
| 24 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0217 | -0.0085 | -0.0155 | -0.0133 | 0.0163 |
| 25 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0385 | -0.0108 | -0.0108 | -0.0108 | 0.0162 |
| 26 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0179 | -0.0073 | -0.0138 | -0.0092 | 0.0142 |
| 27 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0445 | -0.0090 | -0.0090 | -0.0090 | 0.0134 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0186 | -0.0074 | -0.0119 | -0.0058 | 0.0134 |
| 29 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0279 | 0.0091 | 0.0077 | 0.0062 | 0.0130 |
| 30 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.6164 | 0.0086 | 0.0086 | 0.0086 | 0.0130 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0316 | 0.0289 | 0.0289 | 0.0289 | 0.0433 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0342 | 0.0165 | 0.0165 | 0.0165 | 0.0247 |
| 3 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0330 | 0.0124 | 0.0124 | 0.0124 | 0.0186 |
| 4 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0245 | -0.0121 | -0.0121 | -0.0121 | 0.0182 |
| 5 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0194 | -0.0093 | -0.0093 | -0.0093 | 0.0139 |
| 6 | mod.blocks.3.attn.h4 | electron<-electron | 0.1797 | -0.0082 | -0.0082 | -0.0082 | 0.0123 |
| 7 | mod.blocks.1.attn.h4 | electron<-electron | 0.0955 | -0.0079 | -0.0079 | -0.0079 | 0.0118 |
| 8 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0286 | -0.0078 | -0.0078 | -0.0078 | 0.0117 |
| 9 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0280 | 0.0075 | 0.0075 | 0.0075 | 0.0112 |
| 10 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0219 | -0.0073 | -0.0073 | -0.0073 | 0.0110 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0188 | -0.0073 | -0.0073 | -0.0073 | 0.0109 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0176 | 0.0072 | 0.0072 | 0.0072 | 0.0108 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0242 | 0.0071 | 0.0071 | 0.0071 | 0.0106 |
| 14 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0223 | -0.0066 | -0.0066 | -0.0066 | 0.0099 |
| 15 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0272 | 0.0061 | 0.0061 | 0.0061 | 0.0092 |
| 16 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0193 | -0.0059 | -0.0059 | -0.0059 | 0.0089 |
| 17 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0251 | -0.0056 | -0.0056 | -0.0056 | 0.0084 |
| 18 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0230 | 0.0054 | 0.0054 | 0.0054 | 0.0080 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0182 | -0.0051 | -0.0051 | -0.0051 | 0.0076 |
| 20 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0254 | 0.0049 | 0.0049 | 0.0049 | 0.0074 |
| 21 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0226 | -0.0049 | -0.0049 | -0.0049 | 0.0073 |
| 22 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0172 | -0.0047 | -0.0047 | -0.0047 | 0.0070 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0183 | -0.0045 | -0.0045 | -0.0045 | 0.0068 |
| 24 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0161 | -0.0042 | -0.0042 | -0.0042 | 0.0063 |
| 25 | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0238 | 0.0042 | 0.0042 | 0.0042 | 0.0063 |
| 26 | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0233 | 0.0041 | 0.0041 | 0.0041 | 0.0062 |
| 27 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0252 | -0.0041 | -0.0041 | -0.0041 | 0.0062 |
| 28 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0308 | 0.0040 | 0.0040 | 0.0040 | 0.0061 |
| 29 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0233 | 0.0035 | 0.0035 | 0.0035 | 0.0053 |
| 30 | mod.cls_blocks.0.attn.h2 | photon<-muon | 0.0238 | -0.0035 | -0.0035 | -0.0035 | 0.0053 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
