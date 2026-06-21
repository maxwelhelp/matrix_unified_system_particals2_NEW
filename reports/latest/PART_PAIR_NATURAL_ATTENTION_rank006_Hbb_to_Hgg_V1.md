# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8880**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1033 | -0.4548 | -0.4375 | -0.4548 | 0.6736 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0766 | -0.3269 | -0.1967 | -0.3269 | 0.4252 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0802 | -0.2648 | -0.1602 | -0.2648 | 0.3449 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0686 | -0.2078 | -0.2371 | -0.2078 | 0.3263 |
| 5 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0766 | -0.1541 | -0.2131 | -0.1541 | 0.2607 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0665 | -0.1471 | -0.1858 | -0.1471 | 0.2400 |
| 7 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0703 | -0.1388 | 0.0683 | -0.1388 | 0.1729 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0605 | -0.1133 | -0.1180 | -0.1133 | 0.1723 |
| 9 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.1464 | 0.0000 | 0.0732 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0109 | -0.0025 | -0.1235 | -0.0025 | 0.0642 |
| 11 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0000 | 0.0000 | -0.1258 | 0.0000 | 0.0629 |
| 12 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0000 | 0.0000 | -0.1185 | 0.0000 | 0.0592 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0129 | 0.0045 | -0.0873 | 0.0045 | 0.0482 |
| 14 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0000 | 0.0000 | -0.0808 | 0.0000 | 0.0404 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0048 | 0.0011 | -0.0754 | 4.541e-04 | 0.0388 |
| 16 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | -0.0691 | 0.0000 | 0.0345 |
| 17 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | -0.0574 | 0.0000 | 0.0287 |
| 18 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.0000 | 0.0000 | -0.0554 | 0.0000 | 0.0277 |
| 19 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0463 | 0.0143 | 0.0266 | 0.0143 | 0.0276 |
| 20 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0362 | 0.0139 | 0.0232 | 0.0139 | 0.0256 |
| 21 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0396 | 0.0134 | 0.0188 | 0.0134 | 0.0228 |
| 22 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0149 | 0.0115 | -0.0226 | 0.0115 | 0.0228 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0154 | 0.0089 | -0.0258 | 0.0081 | 0.0218 |
| 24 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0207 | 0.0116 | 0.0183 | 0.0116 | 0.0207 |
| 25 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0220 | 0.0109 | 0.0178 | 0.0109 | 0.0198 |
| 26 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0227 | 0.0109 | 0.0174 | 0.0109 | 0.0196 |
| 27 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0142 | 0.0125 | 0.0134 | 0.0117 | 0.0192 |
| 28 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0397 | 0.0116 | 0.0135 | 0.0116 | 0.0183 |
| 29 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0274 | 0.0094 | 0.0172 | 0.0094 | 0.0181 |
| 30 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0417 | 0.0091 | 0.0147 | 0.0091 | 0.0164 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0252 | -0.0156 | -0.0156 | -0.0156 | 0.0235 |
| 2 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0142 | 0.0125 | 0.0125 | 0.0125 | 0.0188 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0149 | 0.0115 | 0.0115 | 0.0115 | 0.0173 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0227 | -0.0098 | -0.0098 | -0.0098 | 0.0146 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0154 | 0.0089 | 0.0089 | 0.0089 | 0.0133 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0160 | 0.0071 | 0.0071 | 0.0071 | 0.0106 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0160 | 0.0071 | 0.0071 | 0.0071 | 0.0106 |
| 8 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0165 | 0.0067 | 0.0067 | 0.0067 | 0.0101 |
| 9 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0148 | 0.0059 | 0.0059 | 0.0059 | 0.0088 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0221 | -0.0056 | -0.0056 | -0.0056 | 0.0084 |
| 11 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0207 | 0.0056 | 0.0056 | 0.0056 | 0.0083 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0163 | 0.0054 | 0.0054 | 0.0054 | 0.0081 |
| 13 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0168 | 0.0052 | 0.0052 | 0.0052 | 0.0078 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0162 | 0.0052 | 0.0052 | 0.0052 | 0.0078 |
| 15 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0129 | 0.0045 | 0.0045 | 0.0045 | 0.0068 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0204 | 0.0043 | 0.0043 | 0.0043 | 0.0065 |
| 17 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0147 | 0.0043 | 0.0043 | 0.0043 | 0.0064 |
| 18 | mod.cls_blocks.0.attn.h6 | CLS<-charged_hadron | 0.0172 | 0.0041 | 0.0041 | 0.0041 | 0.0061 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0194 | -0.0041 | -0.0041 | -0.0041 | 0.0061 |
| 20 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-muon | 0.0443 | -0.0039 | -0.0039 | -0.0039 | 0.0059 |
| 21 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0127 | 0.0037 | 0.0037 | 0.0037 | 0.0056 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0176 | 0.0037 | 0.0037 | 0.0037 | 0.0055 |
| 23 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0172 | 0.0031 | 0.0031 | 0.0031 | 0.0046 |
| 24 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0173 | 0.0030 | 0.0030 | 0.0030 | 0.0045 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0101 | 0.0028 | 0.0028 | 0.0028 | 0.0043 |
| 26 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0175 | -0.0026 | -0.0026 | -0.0026 | 0.0039 |
| 27 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0179 | 0.0025 | 0.0025 | 0.0025 | 0.0037 |
| 28 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0109 | -0.0025 | -0.0025 | -0.0025 | 0.0037 |
| 29 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0150 | -0.0024 | -0.0024 | -0.0024 | 0.0035 |
| 30 | mod.cls_blocks.0.attn.h3 | charged_hadron<-neutral_hadron | 0.0182 | -0.0024 | -0.0024 | -0.0024 | 0.0035 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
