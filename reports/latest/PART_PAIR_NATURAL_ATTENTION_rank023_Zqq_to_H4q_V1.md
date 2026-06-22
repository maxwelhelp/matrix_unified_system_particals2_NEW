# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9312**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0725 | -0.9473 | -1.3250 | -0.9473 | 1.6098 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0824 | -0.6079 | -0.7992 | -0.6079 | 1.0076 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0835 | -0.5028 | -0.7245 | -0.5028 | 0.8650 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0901 | -0.4789 | -0.4914 | -0.4789 | 0.7246 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0593 | -0.2534 | -0.4509 | -0.2534 | 0.4789 |
| 6 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0765 | -0.2186 | -0.3876 | -0.2186 | 0.4124 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0717 | -0.2187 | -0.3546 | -0.2187 | 0.3960 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0745 | -0.1842 | -0.2474 | -0.1842 | 0.3079 |
| 9 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | -0.2108 | 0.0000 | 0.1054 |
| 10 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0224 | -0.0495 | -0.0692 | -0.0495 | 0.0841 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0355 | -0.0602 | -0.0393 | 0.0247 | 0.0798 |
| 12 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | -0.1319 | 0.0000 | 0.0659 |
| 13 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0372 | -0.0335 | -0.0617 | -0.0335 | 0.0644 |
| 14 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | -0.1167 | 0.0000 | 0.0584 |
| 15 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0439 | -0.0290 | -0.0545 | -0.0290 | 0.0562 |
| 16 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0494 | -0.0272 | -0.0544 | -0.0272 | 0.0544 |
| 17 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0444 | -0.0276 | -0.0513 | -0.0276 | 0.0533 |
| 18 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0175 | 0.0321 | 0.0310 | 0.0321 | 0.0476 |
| 19 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0257 | -0.0266 | -0.0376 | -0.0266 | 0.0454 |
| 20 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0292 | -0.0257 | -0.0249 | -8.954e-04 | 0.0382 |
| 21 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0280 | -0.0221 | -0.0319 | -0.0221 | 0.0381 |
| 22 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0388 | -4.219e-04 | -0.0557 | 0.0014 | 0.0283 |
| 23 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | -0.0552 | 0.0000 | 0.0276 |
| 24 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0189 | -0.0166 | -0.0198 | -0.0021 | 0.0265 |
| 25 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0229 | 0.0036 | -0.0456 | 0.0036 | 0.0264 |
| 26 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0254 | 0.0157 | 0.0157 | 0.0157 | 0.0236 |
| 27 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0245 | -0.0128 | -0.0155 | -0.0128 | 0.0206 |
| 28 | mod.cls_blocks.0.attn.h3 | muon<-CLS | 0.0000 | 0.0000 | -0.0406 | 0.0000 | 0.0203 |
| 29 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0231 | 0.0104 | 0.0182 | -0.0052 | 0.0195 |
| 30 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0000 | 0.0000 | -0.0387 | 0.0000 | 0.0193 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0376 | -0.1034 | -0.1034 | -0.1034 | 0.1551 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0319 | -0.0382 | -0.0382 | -0.0382 | 0.0573 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0175 | 0.0321 | 0.0321 | 0.0321 | 0.0481 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0198 | -0.0232 | -0.0232 | -0.0232 | 0.0348 |
| 5 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0281 | -0.0167 | -0.0167 | -0.0167 | 0.0250 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0254 | 0.0157 | 0.0157 | 0.0157 | 0.0236 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0254 | 0.0157 | 0.0157 | 0.0157 | 0.0236 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0184 | 0.0129 | 0.0129 | 0.0129 | 0.0193 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0228 | 0.0118 | 0.0118 | 0.0118 | 0.0177 |
| 10 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0657 | 0.0112 | 0.0112 | 0.0112 | 0.0168 |
| 11 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0657 | 0.0112 | 0.0112 | 0.0112 | 0.0168 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0242 | -0.0109 | -0.0109 | -0.0109 | 0.0163 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0265 | 0.0106 | 0.0106 | 0.0106 | 0.0159 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0158 | 0.0102 | 0.0102 | 0.0102 | 0.0153 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0228 | 0.0087 | 0.0087 | 0.0087 | 0.0131 |
| 16 | mod.cls_blocks.0.attn.h3 | charged_hadron<-electron | 0.0200 | 0.0066 | 0.0066 | 0.0066 | 0.0100 |
| 17 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0231 | 0.0065 | 0.0065 | 0.0065 | 0.0098 |
| 18 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0204 | 0.0062 | 0.0062 | 0.0062 | 0.0093 |
| 19 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0219 | 0.0062 | 0.0062 | 0.0062 | 0.0093 |
| 20 | mod.cls_blocks.0.attn.h3 | CLS<-electron | 0.0193 | 0.0058 | 0.0058 | 0.0058 | 0.0088 |
| 21 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0235 | 0.0058 | 0.0058 | 0.0058 | 0.0087 |
| 22 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0214 | 0.0057 | 0.0057 | 0.0057 | 0.0086 |
| 23 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0238 | 0.0057 | 0.0057 | 0.0057 | 0.0086 |
| 24 | mod.cls_blocks.0.attn.h5 | photon<-electron | 0.0323 | -0.0054 | -0.0054 | -0.0054 | 0.0081 |
| 25 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0207 | -0.0052 | -0.0052 | -0.0052 | 0.0078 |
| 26 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0262 | -0.0047 | -0.0047 | -0.0047 | 0.0071 |
| 27 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0154 | 0.0047 | 0.0047 | 0.0047 | 0.0070 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0250 | 0.0047 | 0.0047 | 0.0047 | 0.0070 |
| 29 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0295 | -0.0043 | -0.0043 | -0.0043 | 0.0065 |
| 30 | mod.cls_blocks.0.attn.h3 | photon<-charged_hadron | 0.0242 | 0.0042 | 0.0042 | 0.0042 | 0.0064 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
