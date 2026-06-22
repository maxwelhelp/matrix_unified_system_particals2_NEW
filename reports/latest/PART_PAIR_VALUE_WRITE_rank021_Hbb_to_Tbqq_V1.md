# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9984**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0739 | -0.0619 | 0.0619 | -0.2883 | -0.0619 | 152.1469 | 0.0249 | 0.2216 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0698 | -0.0459 | 0.0471 | -0.2059 | -0.0459 | 152.1469 | 0.0255 | 0.1606 |
| 3 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2177 | 0.0000 | 0.0000 | 0.0000 | 0.1089 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2136 | 0.0000 | 0.0000 | 0.0000 | 0.1068 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0292 | -0.0396 | 0.0696 | -0.0511 | -0.0541 | 7.7414 | 0.0087 | 0.0826 |
| 6 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0728 | -0.0232 | 0.0232 | -0.0911 | -0.0232 | 102.3998 | 0.0208 | 0.0746 |
| 7 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0406 | 0.0296 | 0.0296 | 0.0407 | 0.0296 | 64.1643 | 0.0295 | 0.0574 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0677 | -0.0165 | 0.0184 | -0.0696 | -0.0165 | 102.3998 | 0.0212 | 0.0558 |
| 9 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0201 | -0.0055 | 0.0055 | -0.0901 | -0.0072 | 25.9351 | 0.0260 | 0.0519 |
| 10 | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0444 | -0.0293 | 0.0293 | -0.0270 | -0.0264 | 32.6173 | 0.0521 | 0.0501 |
| 11 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0296 | 0.0208 | 0.0208 | 0.0457 | 0.0144 | 29.5004 | 0.0404 | 0.0489 |
| 12 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0376 | 0.0252 | 0.0252 | 0.0327 | 0.0252 | 64.1643 | 0.0279 | 0.0478 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0573 | 0.0024 | 0.0024 | -0.0854 | 0.0024 | 152.1469 | 0.0272 | 0.0457 |
| 14 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0115 | -0.0022 | 0.0031 | -0.0786 | 9.511e-04 | 7.6084 | 0.0158 | 0.0423 |
| 15 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0053 | -7.075e-04 | 7.075e-04 | 0.0702 | 4.262e-04 | 12.0309 | 0.0343 | 0.0360 |
| 16 | mod.cls_blocks.0.attn.h7 | photon<-muon | 0.0289 | -0.0042 | 0.0103 | 0.0567 | -0.0045 | 23.8762 | 0.0376 | 0.0351 |
| 17 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0310 | -0.0202 | 0.0202 | -0.0164 | -0.0224 | 24.1348 | 0.0453 | 0.0334 |
| 18 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0634 | 0.0000 | 0.0000 | 0.0000 | 0.0317 |
| 19 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0632 | 0.0000 | 0.0000 | 0.0000 | 0.0316 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0218 | 0.0077 | 0.0205 | 0.0367 | 0.0073 | 44.5111 | 0.0441 | 0.0312 |
| 21 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0272 | 0.0047 | 0.0120 | 0.0448 | -0.0016 | 23.2288 | 0.0368 | 0.0301 |
| 22 | mod.cls_blocks.0.attn.h7 | photon<-electron | 0.0091 | -0.0013 | 0.0013 | 0.0561 | -0.0087 | 8.4748 | 0.0188 | 0.0297 |
| 23 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0558 | 0.0000 | 0.0000 | 0.0000 | 0.0279 |
| 24 | mod.cls_blocks.0.attn.h7 | charged_hadron<-electron | 0.0020 | 6.657e-06 | 6.657e-06 | 0.0555 | -0.0100 | 9.9829 | 0.0404 | 0.0278 |
| 25 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | 0.0546 | 0.0000 | 0.0000 | 0.0000 | 0.0273 |
| 26 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0115 | 0.0149 | 0.0149 | 0.0144 | -0.0238 | 24.9867 | 0.0937 | 0.0259 |
| 27 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | -0.0508 | 0.0000 | 0.0000 | 0.0000 | 0.0254 |
| 28 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | 0.0490 | -0.0067 | 0.0000 | 0.0000 | 0.0245 |
| 29 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0202 | 0.0127 | 0.0127 | 0.0156 | 0.0127 | 66.5560 | 0.0274 | 0.0236 |
| 30 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0287 | 0.0118 | 0.0118 | 0.0172 | 0.0118 | 64.1643 | 0.0232 | 0.0233 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0306 | -0.0386 | 0.0702 | -0.0386 | -0.0386 | 8.7501 | 0.0087 | 0.0755 |
| 2 | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0444 | -0.0293 | 0.0293 | -0.0293 | -0.0293 | 32.6173 | 0.0521 | 0.0513 |
| 3 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0296 | 0.0208 | 0.0208 | 0.0208 | 0.0208 | 29.5004 | 0.0404 | 0.0364 |
| 4 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0310 | -0.0202 | 0.0202 | -0.0202 | -0.0202 | 24.1348 | 0.0453 | 0.0353 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0115 | 0.0149 | 0.0149 | 0.0149 | 0.0149 | 24.9867 | 0.0937 | 0.0261 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0185 | 0.0119 | 0.0154 | 0.0119 | 0.0119 | 3.8500 | 0.0064 | 0.0217 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0176 | 0.0122 | 0.0122 | 0.0122 | 0.0122 | 16.0587 | 0.0937 | 0.0214 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0183 | 0.0117 | 0.0128 | 0.0117 | 0.0117 | 4.0397 | 0.0100 | 0.0207 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0343 | -0.0112 | 0.0112 | -0.0112 | -0.0112 | 18.7129 | 0.0232 | 0.0196 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0228 | -0.0065 | 0.0342 | -0.0065 | -0.0065 | 5.7093 | 0.0088 | 0.0184 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0162 | 0.0095 | 0.0139 | 0.0095 | 0.0095 | 1.3021 | 0.0025 | 0.0177 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0218 | 0.0077 | 0.0205 | 0.0077 | 0.0077 | 44.5112 | 0.0441 | 0.0167 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0265 | -0.0071 | 0.0217 | -0.0071 | -0.0071 | 6.2367 | 0.0058 | 0.0161 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0137 | 0.0089 | 0.0109 | 0.0089 | 0.0089 | 1.0971 | 0.0027 | 0.0160 |
| 15 | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0241 | -0.0080 | 0.0084 | -0.0080 | -0.0080 | 23.6998 | 0.0402 | 0.0141 |
| 16 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0237 | 0.0080 | 0.0080 | 0.0080 | 0.0080 | 15.6892 | 0.0534 | 0.0140 |
| 17 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0136 | -0.0080 | 0.0080 | -0.0080 | -0.0080 | 35.0486 | 0.0402 | 0.0140 |
| 18 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0125 | -0.0080 | 0.0080 | -0.0080 | -0.0080 | 12.8033 | 0.0221 | 0.0140 |
| 19 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0150 | 0.0069 | 0.0137 | 0.0069 | 0.0069 | 1.2165 | 0.0025 | 0.0137 |
| 20 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0198 | 0.0075 | 0.0075 | 0.0075 | 0.0075 | 19.4387 | 0.0320 | 0.0131 |
| 21 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0175 | 0.0062 | 0.0140 | 0.0062 | 0.0062 | 32.1063 | 0.0511 | 0.0128 |
| 22 | mod.cls_blocks.0.attn.h7 | charged_hadron<-neutral_hadron | 0.0197 | 0.0072 | 0.0080 | 0.0072 | 0.0072 | 2.8078 | 0.0058 | 0.0128 |
| 23 | mod.cls_blocks.0.attn.h7 | CLS<-neutral_hadron | 0.0227 | 0.0067 | 0.0083 | 0.0067 | 0.0067 | 3.0543 | 0.0058 | 0.0122 |
| 24 | mod.cls_blocks.1.attn.h2 | photon<-muon | 0.0473 | 0.0069 | 0.0070 | 0.0069 | 0.0069 | 3.0321 | 0.0526 | 0.0121 |
| 25 | mod.cls_blocks.0.attn.h7 | photon<-neutral_hadron | 0.0212 | 0.0063 | 0.0095 | 0.0063 | 0.0063 | 2.4309 | 0.0052 | 0.0118 |
| 26 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-neutral_hadron | 0.0271 | 0.0065 | 0.0079 | 0.0065 | 0.0065 | 3.7012 | 0.0060 | 0.0117 |
| 27 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0198 | -0.0022 | 0.0330 | -0.0022 | -0.0022 | 1.1373 | 0.0022 | 0.0115 |
| 28 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0214 | 0.0064 | 0.0064 | 0.0064 | 0.0064 | 15.6623 | 0.0318 | 0.0112 |
| 29 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0195 | 0.0054 | 0.0103 | 0.0054 | 0.0054 | 1.1491 | 0.0023 | 0.0106 |
| 30 | mod.cls_blocks.1.attn.h1 | photon<-muon | 0.1262 | -0.0061 | 0.0061 | -0.0061 | -0.0061 | 3.2536 | 0.0354 | 0.0106 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
