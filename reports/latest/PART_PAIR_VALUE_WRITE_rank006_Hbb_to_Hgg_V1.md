# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8880**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1033 | -0.4548 | 0.4548 | -0.4375 | -0.4548 | 152.1469 | 0.0326 | 0.7873 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0766 | -0.3269 | 0.3269 | -0.1967 | -0.3269 | 152.1469 | 0.0324 | 0.5069 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0802 | -0.2648 | 0.2648 | -0.1602 | -0.2648 | 152.1469 | 0.0267 | 0.4111 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0686 | -0.2078 | 0.2078 | -0.2371 | -0.2078 | 102.3998 | 0.0467 | 0.3783 |
| 5 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0766 | -0.1541 | 0.1541 | -0.2131 | -0.1541 | 102.3998 | 0.0314 | 0.2992 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0665 | -0.1471 | 0.1471 | -0.1858 | -0.1471 | 102.3998 | 0.0379 | 0.2768 |
| 7 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0703 | -0.1388 | 0.1388 | 0.0683 | -0.1388 | 152.1469 | 0.0208 | 0.2076 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0605 | -0.1133 | 0.1133 | -0.1180 | -0.1133 | 102.3998 | 0.0368 | 0.2007 |
| 9 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1464 | 0.0000 | 0.0000 | 0.0000 | 0.0732 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0109 | -0.0025 | 0.0025 | -0.1235 | -0.0025 | 20.6502 | 0.0327 | 0.0648 |
| 11 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1258 | 0.0000 | 0.0000 | 0.0000 | 0.0629 |
| 12 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1185 | 0.0000 | 0.0000 | 0.0000 | 0.0592 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0129 | 0.0045 | 0.0070 | -0.0873 | 0.0045 | 23.5984 | 0.0324 | 0.0500 |
| 14 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | -0.0808 | 0.0000 | 0.0000 | 0.0000 | 0.0404 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0048 | 0.0011 | 0.0011 | -0.0754 | 4.541e-04 | 9.6771 | 0.0301 | 0.0390 |
| 16 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0691 | 0.0000 | 0.0000 | 0.0000 | 0.0345 |
| 17 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0463 | 0.0143 | 0.0143 | 0.0266 | 0.0143 | 64.1643 | 0.0360 | 0.0312 |
| 18 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0362 | 0.0139 | 0.0139 | 0.0232 | 0.0139 | 64.1643 | 0.0357 | 0.0290 |
| 19 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0574 | 0.0000 | 0.0000 | 0.0000 | 0.0287 |
| 20 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | -0.0554 | 0.0000 | 0.0000 | 0.0000 | 0.0277 |
| 21 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0396 | 0.0134 | 0.0134 | 0.0188 | 0.0134 | 64.1643 | 0.0364 | 0.0262 |
| 22 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0149 | 0.0115 | 0.0115 | -0.0226 | 0.0115 | 26.5465 | 0.0321 | 0.0257 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0154 | 0.0089 | 0.0089 | -0.0258 | 0.0081 | 29.6687 | 0.0306 | 0.0240 |
| 24 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0207 | 0.0116 | 0.0116 | 0.0183 | 0.0116 | 66.5560 | 0.0271 | 0.0236 |
| 25 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0220 | 0.0109 | 0.0109 | 0.0178 | 0.0109 | 66.5560 | 0.0275 | 0.0225 |
| 26 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0142 | 0.0125 | 0.0125 | 0.0134 | 0.0117 | 27.2485 | 0.0354 | 0.0224 |
| 27 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0227 | 0.0109 | 0.0109 | 0.0174 | 0.0109 | 66.5560 | 0.0278 | 0.0223 |
| 28 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0397 | 0.0116 | 0.0116 | 0.0135 | 0.0116 | 64.1643 | 0.0379 | 0.0212 |
| 29 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0274 | 0.0094 | 0.0094 | 0.0172 | 0.0094 | 66.5560 | 0.0294 | 0.0204 |
| 30 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0417 | 0.0091 | 0.0091 | 0.0147 | 0.0091 | 42.4997 | 0.0178 | 0.0187 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0252 | -0.0156 | 0.0242 | -0.0156 | -0.0156 | 7.6147 | 0.0031 | 0.0295 |
| 2 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0142 | 0.0125 | 0.0125 | 0.0125 | 0.0125 | 27.2485 | 0.0354 | 0.0219 |
| 3 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0227 | -0.0098 | 0.0221 | -0.0098 | -0.0098 | 6.2056 | 0.0052 | 0.0202 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0149 | 0.0115 | 0.0115 | 0.0115 | 0.0115 | 26.5465 | 0.0321 | 0.0202 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0154 | 0.0089 | 0.0089 | 0.0089 | 0.0089 | 29.6687 | 0.0306 | 0.0155 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0160 | 0.0071 | 0.0091 | 0.0071 | 0.0071 | 1.0264 | 0.0014 | 0.0129 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0165 | 0.0067 | 0.0103 | 0.0067 | 0.0067 | 4.8747 | 0.0065 | 0.0127 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0160 | 0.0071 | 0.0071 | 0.0071 | 0.0071 | 30.8789 | 0.0282 | 0.0123 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0221 | -0.0056 | 0.0141 | -0.0056 | -0.0056 | 6.2155 | 0.0035 | 0.0119 |
| 10 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0207 | 0.0056 | 0.0125 | 0.0056 | 0.0056 | 4.9554 | 0.0074 | 0.0115 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0163 | 0.0054 | 0.0106 | 0.0054 | 0.0054 | 1.0884 | 0.0015 | 0.0107 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0148 | 0.0059 | 0.0071 | 0.0059 | 0.0059 | 1.0409 | 0.0016 | 0.0106 |
| 13 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0168 | 0.0052 | 0.0098 | 0.0052 | 0.0052 | 0.8605 | 0.0014 | 0.0103 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0162 | 0.0052 | 0.0083 | 0.0052 | 0.0052 | 0.8765 | 0.0012 | 0.0099 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0194 | -0.0041 | 0.0116 | -0.0041 | -0.0041 | 1.0696 | 8.147e-04 | 0.0090 |
| 16 | mod.cls_blocks.0.attn.h6 | CLS<-charged_hadron | 0.0172 | 0.0041 | 0.0100 | 0.0041 | 0.0041 | 0.8984 | 0.0013 | 0.0086 |
| 17 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0129 | 0.0045 | 0.0070 | 0.0045 | 0.0045 | 23.5984 | 0.0324 | 0.0085 |
| 18 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0147 | 0.0043 | 0.0050 | 0.0043 | 0.0043 | 1.1614 | 0.0010 | 0.0077 |
| 19 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0179 | 0.0025 | 0.0156 | 0.0025 | 0.0025 | 1.2164 | 0.0017 | 0.0076 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0204 | 0.0043 | 0.0044 | 0.0043 | 0.0043 | 4.7024 | 0.0036 | 0.0076 |
| 21 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-muon | 0.0443 | -0.0039 | 0.0039 | -0.0039 | -0.0039 | 12.1063 | 0.0309 | 0.0069 |
| 22 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0207 | -0.0017 | 0.0167 | -0.0017 | -0.0017 | 5.5483 | 0.0061 | 0.0067 |
| 23 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0176 | 0.0037 | 0.0044 | 0.0037 | 0.0037 | 5.0782 | 0.0043 | 0.0066 |
| 24 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0127 | 0.0037 | 0.0037 | 0.0037 | 0.0037 | 16.0731 | 0.0305 | 0.0065 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0175 | -0.0026 | 0.0087 | -0.0026 | -0.0026 | 1.3809 | 8.149e-04 | 0.0060 |
| 26 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0172 | 0.0031 | 0.0040 | 0.0031 | 0.0031 | 0.9166 | 7.460e-04 | 0.0056 |
| 27 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0173 | 0.0030 | 0.0032 | 0.0030 | 0.0030 | 0.9175 | 6.742e-04 | 0.0053 |
| 28 | mod.cls_blocks.0.attn.h0 | photon<-neutral_hadron | 0.0191 | -0.0022 | 0.0076 | -0.0022 | -0.0022 | 3.2545 | 0.0065 | 0.0052 |
| 29 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0101 | 0.0028 | 0.0028 | 0.0028 | 0.0028 | 13.9411 | 0.0304 | 0.0050 |
| 30 | mod.cls_blocks.0.attn.h2 | charged_hadron<-photon | 0.0182 | -0.0024 | 0.0044 | -0.0024 | -0.0024 | 0.8330 | 0.0015 | 0.0046 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
