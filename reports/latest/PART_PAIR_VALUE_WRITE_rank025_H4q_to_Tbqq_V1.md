# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9120**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0881 | -0.6735 | 0.6735 | -0.7643 | -0.6735 | 152.1469 | 0.0708 | 1.2241 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0732 | -0.3326 | 0.3615 | -0.3609 | -0.3326 | 152.1469 | 0.0452 | 0.6034 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0724 | -0.3573 | 0.3573 | -0.3012 | -0.3573 | 152.1469 | 0.0460 | 0.5973 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0716 | -0.1868 | 0.1868 | -0.1843 | -0.1868 | 102.3998 | 0.0418 | 0.3257 |
| 5 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0624 | -0.1072 | 0.1083 | -0.0643 | -0.1072 | 102.3998 | 0.0363 | 0.1664 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0626 | -0.0917 | 0.1094 | -0.0781 | -0.0917 | 102.3998 | 0.0350 | 0.1581 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0600 | 0.0578 | 0.0578 | 0.1068 | 0.0578 | 152.1469 | 0.0178 | 0.1256 |
| 8 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.2051 | -0.0459 | 0.0459 | -0.0462 | -0.0459 | 44.7018 | 0.0208 | 0.0804 |
| 9 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0541 | 0.0343 | 0.0343 | 0.0510 | 0.0343 | 102.3998 | 0.0253 | 0.0685 |
| 10 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0305 | 0.0198 | 0.0198 | 0.0750 | 0.0126 | 20.9715 | 0.0391 | 0.0623 |
| 11 | mod.cls_blocks.0.attn.h7 | charged_hadron<-electron | 0.0269 | 0.0176 | 0.0188 | 0.0759 | 0.0097 | 8.7992 | 0.0239 | 0.0602 |
| 12 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0353 | -0.0195 | 0.0195 | -0.0330 | -0.0195 | 64.1643 | 0.0255 | 0.0409 |
| 13 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0285 | 0.0156 | 0.0166 | 0.0406 | 0.0089 | 10.8215 | 0.0261 | 0.0401 |
| 14 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0280 | 0.0200 | 0.0279 | 0.0187 | 0.0244 | 5.2772 | 0.0099 | 0.0364 |
| 15 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0305 | 0.0198 | 0.0198 | 0.0198 | 0.0086 | 20.9715 | 0.0391 | 0.0347 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0701 | 0.0193 | 0.0193 | 0.0186 | 0.0193 | 42.0109 | 0.0253 | 0.0334 |
| 17 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0340 | -0.0145 | 0.0145 | -0.0261 | -0.0145 | 42.4997 | 0.0404 | 0.0311 |
| 18 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0260 | -0.0129 | 0.0129 | -0.0256 | -0.0129 | 42.4997 | 0.0367 | 0.0289 |
| 19 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0227 | -0.0141 | 0.0141 | -0.0221 | -0.0141 | 66.5560 | 0.0253 | 0.0287 |
| 20 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0249 | -0.0138 | 0.0138 | -0.0223 | -0.0138 | 66.5560 | 0.0226 | 0.0284 |
| 21 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0000 | 0.0000 | 0.0000 | 0.0552 | -0.0095 | 0.0000 | 0.0000 | 0.0276 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0201 | 0.0146 | 0.0154 | 0.0133 | 0.0169 | 1.2311 | 0.0026 | 0.0251 |
| 23 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0270 | -0.0111 | 0.0111 | -0.0223 | -0.0111 | 42.4997 | 0.0379 | 0.0250 |
| 24 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0358 | -0.0114 | 0.0114 | -0.0211 | -0.0114 | 64.1643 | 0.0197 | 0.0248 |
| 25 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0187 | 0.0093 | 0.0107 | 0.0224 | -0.0237 | 15.6065 | 0.0209 | 0.0232 |
| 26 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0337 | -0.0092 | 0.0120 | -0.0203 | -0.0092 | 64.1643 | 0.0205 | 0.0223 |
| 27 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0394 | 0.0151 | 0.0151 | 0.0068 | 0.0151 | 27.3259 | 0.0341 | 0.0223 |
| 28 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0231 | -0.0103 | 0.0105 | -0.0176 | -0.0103 | 66.5560 | 0.0228 | 0.0218 |
| 29 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0194 | 0.0100 | 0.0216 | 0.0076 | 0.0510 | 4.1233 | 0.0036 | 0.0192 |
| 30 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0308 | -0.0106 | 0.0106 | -0.0106 | -0.0129 | 33.0878 | 0.0413 | 0.0185 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0264 | 0.0219 | 0.0242 | 0.0219 | 0.0219 | 4.9266 | 0.0099 | 0.0389 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0238 | -0.0155 | 0.0509 | -0.0155 | -0.0155 | 1.9582 | 0.0033 | 0.0359 |
| 3 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0305 | 0.0198 | 0.0198 | 0.0198 | 0.0198 | 20.9715 | 0.0391 | 0.0347 |
| 4 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0305 | 0.0198 | 0.0198 | 0.0198 | 0.0198 | 20.9715 | 0.0391 | 0.0347 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0205 | 0.0131 | 0.0255 | 0.0131 | 0.0131 | 5.7993 | 0.0036 | 0.0260 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0208 | 0.0132 | 0.0146 | 0.0132 | 0.0132 | 16.2928 | 0.0209 | 0.0235 |
| 7 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0202 | 0.0117 | 0.0143 | 0.0117 | 0.0117 | 1.1806 | 0.0026 | 0.0211 |
| 8 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0198 | 0.0104 | 0.0123 | 0.0104 | 0.0104 | 18.2212 | 0.0261 | 0.0187 |
| 9 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0308 | -0.0106 | 0.0106 | -0.0106 | -0.0106 | 33.0878 | 0.0413 | 0.0185 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0201 | 0.0085 | 0.0161 | 0.0085 | 0.0085 | 4.5748 | 0.0072 | 0.0167 |
| 11 | mod.cls_blocks.0.attn.h3 | charged_hadron<-electron | 0.0259 | -0.0090 | 0.0091 | -0.0090 | -0.0090 | 11.9121 | 0.0192 | 0.0157 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0187 | -0.0061 | 0.0245 | -0.0061 | -0.0061 | 1.1787 | 0.0018 | 0.0153 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0180 | 0.0072 | 0.0122 | 0.0072 | 0.0072 | 4.6075 | 0.0036 | 0.0139 |
| 14 | mod.cls_blocks.0.attn.h7 | photon<-neutral_hadron | 0.0265 | 0.0072 | 0.0092 | 0.0072 | 0.0072 | 2.7690 | 0.0068 | 0.0131 |
| 15 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0582 | -0.0074 | 0.0074 | -0.0074 | -0.0074 | 14.8764 | 0.0343 | 0.0130 |
| 16 | mod.cls_blocks.0.attn.h3 | CLS<-electron | 0.0234 | -0.0071 | 0.0073 | -0.0071 | -0.0071 | 12.8766 | 0.0206 | 0.0125 |
| 17 | mod.cls_blocks.0.attn.h3 | photon<-neutral_hadron | 0.0280 | -0.0065 | 0.0065 | -0.0065 | -0.0065 | 3.8141 | 0.0047 | 0.0113 |
| 18 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0224 | -0.0052 | 0.0138 | -0.0052 | -0.0052 | 1.5535 | 0.0022 | 0.0113 |
| 19 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0184 | -0.0033 | 0.0199 | -0.0033 | -0.0033 | 1.1035 | 0.0017 | 0.0099 |
| 20 | mod.cls_blocks.0.attn.h5 | CLS<-muon | 0.0215 | 0.0056 | 0.0056 | 0.0056 | 0.0056 | 19.6987 | 0.0205 | 0.0098 |
| 21 | mod.cls_blocks.0.attn.h5 | charged_hadron<-muon | 0.0215 | 0.0056 | 0.0056 | 0.0056 | 0.0056 | 19.6987 | 0.0205 | 0.0098 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0186 | 0.0042 | 0.0120 | 0.0042 | 0.0042 | 4.2147 | 0.0074 | 0.0093 |
| 23 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0156 | -0.0052 | 0.0062 | -0.0052 | -0.0052 | 0.7418 | 7.628e-04 | 0.0093 |
| 24 | mod.cls_blocks.0.attn.h7 | charged_hadron<-electron | 0.0147 | 0.0049 | 0.0054 | 0.0049 | 0.0049 | 9.0054 | 0.0239 | 0.0087 |
| 25 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0311 | -0.0049 | 0.0052 | -0.0049 | -0.0049 | 1.4539 | 0.0460 | 0.0087 |
| 26 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0131 | 0.0046 | 0.0071 | 0.0046 | 0.0046 | 0.8833 | 0.0018 | 0.0086 |
| 27 | mod.cls_blocks.0.attn.h7 | CLS<-neutral_hadron | 0.0193 | 0.0044 | 0.0069 | 0.0044 | 0.0044 | 2.5408 | 0.0061 | 0.0084 |
| 28 | mod.cls_blocks.0.attn.h7 | charged_hadron<-neutral_hadron | 0.0173 | 0.0041 | 0.0068 | 0.0041 | 0.0041 | 2.4378 | 0.0061 | 0.0078 |
| 29 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0180 | 0.0044 | 0.0045 | 0.0044 | 0.0044 | 13.9036 | 0.0201 | 0.0077 |
| 30 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0179 | 0.0043 | 0.0046 | 0.0043 | 0.0043 | 10.2494 | 0.0261 | 0.0076 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
