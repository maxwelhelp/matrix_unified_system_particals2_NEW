# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9312**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0725 | -0.9473 | 0.9473 | -1.3250 | -0.9473 | 152.1469 | 0.0970 | 1.8466 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0824 | -0.6079 | 0.6079 | -0.7992 | -0.6079 | 152.1469 | 0.0679 | 1.1595 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0835 | -0.5028 | 0.5028 | -0.7245 | -0.5028 | 152.1469 | 0.0588 | 0.9907 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0901 | -0.4789 | 0.4789 | -0.4914 | -0.4789 | 152.1469 | 0.0570 | 0.8444 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0593 | -0.2534 | 0.2534 | -0.4509 | -0.2534 | 102.3998 | 0.0512 | 0.5422 |
| 6 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0765 | -0.2186 | 0.2186 | -0.3876 | -0.2186 | 102.3998 | 0.0382 | 0.4670 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0717 | -0.2187 | 0.2187 | -0.3546 | -0.2187 | 102.3998 | 0.0411 | 0.4507 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0745 | -0.1842 | 0.1842 | -0.2474 | -0.1842 | 102.3998 | 0.0367 | 0.3539 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0355 | -0.0602 | 0.1211 | -0.0393 | 0.0247 | 10.0691 | 0.0150 | 0.1101 |
| 10 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2108 | 0.0000 | 0.0000 | 0.0000 | 0.1054 |
| 11 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0224 | -0.0495 | 0.0495 | -0.0692 | -0.0495 | 66.5560 | 0.0482 | 0.0965 |
| 12 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0372 | -0.0335 | 0.0335 | -0.0617 | -0.0335 | 64.1643 | 0.0264 | 0.0727 |
| 13 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1319 | 0.0000 | 0.0000 | 0.0000 | 0.0659 |
| 14 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0439 | -0.0290 | 0.0290 | -0.0545 | -0.0290 | 64.1643 | 0.0222 | 0.0635 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0494 | -0.0272 | 0.0272 | -0.0544 | -0.0272 | 64.1643 | 0.0259 | 0.0612 |
| 16 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0444 | -0.0276 | 0.0276 | -0.0513 | -0.0276 | 64.1643 | 0.0183 | 0.0602 |
| 17 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1167 | 0.0000 | 0.0000 | 0.0000 | 0.0584 |
| 18 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0175 | 0.0321 | 0.0321 | 0.0310 | 0.0321 | 23.7199 | 0.1104 | 0.0556 |
| 19 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0257 | -0.0266 | 0.0266 | -0.0376 | -0.0266 | 66.5560 | 0.0393 | 0.0521 |
| 20 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0292 | -0.0257 | 0.0355 | -0.0249 | -8.954e-04 | 7.6314 | 0.0092 | 0.0471 |
| 21 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0280 | -0.0221 | 0.0221 | -0.0319 | -0.0221 | 66.5560 | 0.0357 | 0.0436 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0189 | -0.0166 | 0.0405 | -0.0198 | -0.0021 | 1.4208 | 0.0036 | 0.0366 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0388 | -4.219e-04 | 4.219e-04 | -0.0557 | 0.0014 | 28.7477 | 0.0322 | 0.0284 |
| 24 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0552 | 0.0000 | 0.0000 | 0.0000 | 0.0276 |
| 25 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0254 | 0.0157 | 0.0157 | 0.0157 | 0.0157 | 23.1737 | 0.0546 | 0.0275 |
| 26 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0229 | 0.0036 | 0.0036 | -0.0456 | 0.0036 | 15.0660 | 0.0275 | 0.0273 |
| 27 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0231 | 0.0104 | 0.0200 | 0.0182 | -0.0052 | 1.0393 | 0.0031 | 0.0245 |
| 28 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0245 | -0.0128 | 0.0128 | -0.0155 | -0.0128 | 66.5560 | 0.0375 | 0.0238 |
| 29 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0269 | -0.0087 | 0.0407 | 0.0090 | 0.0103 | 5.9958 | 0.0128 | 0.0234 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0255 | 0.0077 | 0.0195 | 0.0190 | -7.294e-04 | 5.3740 | 0.0130 | 0.0221 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0376 | -0.1034 | 0.1682 | -0.1034 | -0.1034 | 11.1475 | 0.0150 | 0.1971 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0319 | -0.0382 | 0.0492 | -0.0382 | -0.0382 | 8.4537 | 0.0092 | 0.0696 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0175 | 0.0321 | 0.0321 | 0.0321 | 0.0321 | 23.7199 | 0.1104 | 0.0561 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0198 | -0.0232 | 0.0466 | -0.0232 | -0.0232 | 1.5557 | 0.0036 | 0.0464 |
| 5 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0281 | -0.0167 | 0.0517 | -0.0167 | -0.0167 | 6.1708 | 0.0128 | 0.0379 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0242 | -0.0109 | 0.0461 | -0.0109 | -0.0109 | 1.4734 | 0.0029 | 0.0278 |
| 7 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0254 | 0.0157 | 0.0157 | 0.0157 | 0.0157 | 23.1737 | 0.0546 | 0.0275 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0254 | 0.0157 | 0.0157 | 0.0157 | 0.0157 | 23.1737 | 0.0546 | 0.0275 |
| 9 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0184 | 0.0129 | 0.0129 | 0.0129 | 0.0129 | 20.6236 | 0.0626 | 0.0225 |
| 10 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0228 | 0.0118 | 0.0192 | 0.0118 | 0.0118 | 1.2886 | 0.0035 | 0.0225 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0265 | 0.0106 | 0.0199 | 0.0106 | 0.0106 | 5.3256 | 0.0130 | 0.0208 |
| 12 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0657 | 0.0112 | 0.0112 | 0.0112 | 0.0112 | 34.7227 | 0.0337 | 0.0196 |
| 13 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0657 | 0.0112 | 0.0112 | 0.0112 | 0.0112 | 34.7227 | 0.0337 | 0.0196 |
| 14 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0228 | 0.0087 | 0.0190 | 0.0087 | 0.0087 | 1.0250 | 0.0031 | 0.0178 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0158 | 0.0102 | 0.0102 | 0.0102 | 0.0102 | 12.8632 | 0.0409 | 0.0178 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0204 | 0.0062 | 0.0195 | 0.0062 | 0.0062 | 1.7833 | 0.0051 | 0.0142 |
| 17 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0207 | -0.0052 | 0.0187 | -0.0052 | -0.0052 | 1.3286 | 0.0023 | 0.0125 |
| 18 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0235 | 0.0058 | 0.0142 | 0.0058 | 0.0058 | 3.8020 | 0.0108 | 0.0122 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0231 | 0.0065 | 0.0079 | 0.0065 | 0.0065 | 1.0038 | 0.0019 | 0.0117 |
| 20 | mod.cls_blocks.0.attn.h3 | charged_hadron<-electron | 0.0200 | 0.0066 | 0.0066 | 0.0066 | 0.0066 | 9.1099 | 0.0145 | 0.0116 |
| 21 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0262 | -0.0047 | 0.0173 | -0.0047 | -0.0047 | 5.1868 | 0.0078 | 0.0114 |
| 22 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0219 | 0.0062 | 0.0075 | 0.0062 | 0.0062 | 1.1871 | 0.0022 | 0.0111 |
| 23 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0238 | 0.0057 | 0.0074 | 0.0057 | 0.0057 | 3.4543 | 0.0067 | 0.0104 |
| 24 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0214 | 0.0057 | 0.0066 | 0.0057 | 0.0057 | 1.7032 | 0.0031 | 0.0103 |
| 25 | mod.cls_blocks.0.attn.h3 | CLS<-electron | 0.0193 | 0.0058 | 0.0059 | 0.0058 | 0.0058 | 10.2090 | 0.0186 | 0.0102 |
| 26 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0177 | -0.0027 | 0.0225 | -0.0027 | -0.0027 | 1.3417 | 0.0036 | 0.0097 |
| 27 | mod.cls_blocks.0.attn.h5 | photon<-electron | 0.0323 | -0.0054 | 0.0054 | -0.0054 | -0.0054 | 13.6887 | 0.0399 | 0.0095 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0232 | -0.0036 | 0.0159 | -0.0036 | -0.0036 | 1.2370 | 0.0018 | 0.0094 |
| 29 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0250 | 0.0047 | 0.0084 | 0.0047 | 0.0047 | 4.7501 | 0.0080 | 0.0091 |
| 30 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0235 | -4.023e-04 | 0.0326 | -4.023e-04 | -4.023e-04 | 1.3105 | 0.0031 | 0.0088 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
