# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **7120**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0849 | 1.4209 | 1.4209 | 2.6267 | 1.4209 | 152.1469 | 0.1139 | 3.0895 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0871 | 1.0000 | 1.0000 | 1.5290 | 1.0000 | 152.1469 | 0.0853 | 2.0145 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0711 | 0.7485 | 0.7485 | 1.2407 | 0.7485 | 152.1469 | 0.0799 | 1.5559 |
| 4 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0710 | 0.4621 | 0.4621 | 0.8849 | 0.4621 | 102.3998 | 0.0679 | 1.0200 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1075 | 0.4098 | 0.4098 | 0.6225 | 0.4098 | 152.1469 | 0.0333 | 0.8234 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0720 | 0.3567 | 0.3567 | 0.6093 | 0.3567 | 102.3998 | 0.0584 | 0.7506 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0628 | 0.2723 | 0.2723 | 0.5086 | 0.2723 | 102.3998 | 0.0551 | 0.5946 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0832 | 0.2305 | 0.2305 | 0.4288 | 0.2305 | 102.3998 | 0.0429 | 0.5026 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0433 | 0.1635 | 0.1892 | 0.1633 | 0.0484 | 14.5549 | 0.0146 | 0.2924 |
| 10 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0422 | 0.0625 | 0.0625 | 0.1204 | 0.0625 | 64.1643 | 0.0351 | 0.1383 |
| 11 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0268 | 0.0597 | 0.0597 | 0.1135 | 0.0597 | 66.5560 | 0.0467 | 0.1314 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0363 | 0.0719 | 0.0869 | 0.0722 | 0.0141 | 10.2282 | 0.0129 | 0.1297 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0423 | 0.0390 | 0.0390 | 0.0621 | 0.0390 | 64.1643 | 0.0311 | 0.0799 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0300 | 0.0414 | 0.0684 | 0.0406 | -0.0075 | 8.0453 | 0.0159 | 0.0788 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.1477 | 0.0449 | 0.0449 | 0.0423 | 0.0418 | 40.8757 | 0.0367 | 0.0773 |
| 16 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0263 | 0.0390 | 0.0390 | 0.0571 | 0.0390 | 66.5560 | 0.0363 | 0.0773 |
| 17 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0223 | 0.0323 | 0.0323 | 0.0472 | 0.0323 | 66.5560 | 0.0362 | 0.0640 |
| 18 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0219 | -0.0240 | 0.0283 | -0.0490 | -0.0181 | 1.2117 | 0.0045 | 0.0556 |
| 19 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0289 | 0.0197 | 0.0197 | 0.0388 | 0.0197 | 42.4997 | 0.0301 | 0.0440 |
| 20 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0466 | -0.0223 | 0.0223 | -0.0307 | -0.0194 | 22.8181 | 0.0530 | 0.0432 |
| 21 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0927 | 0.0262 | 0.0262 | 0.0206 | 0.0223 | 49.9170 | 0.0394 | 0.0431 |
| 22 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0304 | 0.0182 | 0.0182 | 0.0384 | 0.0182 | 64.1643 | 0.0334 | 0.0420 |
| 23 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0237 | -0.0214 | 0.0231 | -0.0253 | -0.0114 | 2.0873 | 0.0050 | 0.0398 |
| 24 | mod.cls_blocks.1.attn.h3 | photon<-electron | 0.9895 | 0.0228 | 0.0228 | 0.0210 | 0.0227 | 6.3012 | 0.0352 | 0.0390 |
| 25 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0290 | -0.0166 | 0.0223 | -0.0242 | -0.0048 | 1.3933 | 0.0033 | 0.0342 |
| 26 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0235 | -0.0182 | 0.0182 | -0.0146 | -0.0188 | 17.8037 | 0.0921 | 0.0300 |
| 27 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0264 | 0.0159 | 0.0345 | 0.0110 | -0.0098 | 6.5747 | 0.0129 | 0.0300 |
| 28 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0264 | -0.0146 | 0.0191 | -0.0207 | -0.0040 | 2.1073 | 0.0044 | 0.0297 |
| 29 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0289 | -0.0122 | 0.0190 | -0.0252 | -0.0074 | 1.3519 | 0.0029 | 0.0296 |
| 30 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0251 | -0.0075 | 0.0355 | -0.0231 | -0.0030 | 1.3094 | 0.0035 | 0.0280 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0445 | 0.1836 | 0.2079 | 0.1836 | 0.1836 | 15.5093 | 0.0146 | 0.3273 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0421 | 0.0830 | 0.0978 | 0.0830 | 0.0830 | 11.1752 | 0.0129 | 0.1490 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0327 | -0.0787 | 0.0787 | -0.0787 | -0.0787 | 32.1279 | 0.0921 | 0.1377 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0304 | 0.0386 | 0.0772 | 0.0386 | 0.0386 | 8.3699 | 0.0159 | 0.0772 |
| 5 | mod.cls_blocks.0.attn.h7 | photon<-electron | 0.1241 | -0.0365 | 0.0365 | -0.0365 | -0.0365 | 26.5435 | 0.0319 | 0.0638 |
| 6 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.1152 | 0.0353 | 0.0353 | 0.0353 | 0.0353 | 32.3658 | 0.0367 | 0.0618 |
| 7 | mod.cls_blocks.0.attn.h5 | photon<-electron | 0.0892 | 0.0348 | 0.0348 | 0.0348 | 0.0348 | 25.9854 | 0.0368 | 0.0610 |
| 8 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0185 | 0.0292 | 0.0676 | 0.0292 | 0.0292 | 1.2736 | 0.0038 | 0.0608 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0229 | -0.0302 | 0.0302 | -0.0302 | -0.0302 | 27.2744 | 0.0664 | 0.0529 |
| 10 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0252 | 0.0175 | 0.0544 | 0.0175 | 0.0175 | 1.3493 | 0.0028 | 0.0398 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0250 | -0.0221 | 0.0240 | -0.0221 | -0.0221 | 2.1862 | 0.0050 | 0.0391 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0224 | -0.0209 | 0.0285 | -0.0209 | -0.0209 | 4.8889 | 0.0173 | 0.0385 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0291 | 0.0185 | 0.0384 | 0.0185 | 0.0185 | 7.1299 | 0.0129 | 0.0374 |
| 14 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0220 | -0.0185 | 0.0250 | -0.0185 | -0.0185 | 1.1817 | 0.0045 | 0.0340 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0274 | -0.0177 | 0.0211 | -0.0177 | -0.0177 | 6.1913 | 0.0157 | 0.0319 |
| 16 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0919 | -0.0175 | 0.0175 | -0.0175 | -0.0175 | 34.6939 | 0.0394 | 0.0305 |
| 17 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0288 | -0.0158 | 0.0218 | -0.0158 | -0.0158 | 1.3752 | 0.0033 | 0.0292 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0269 | -0.0157 | 0.0199 | -0.0157 | -0.0157 | 2.1510 | 0.0044 | 0.0286 |
| 19 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0242 | -0.0152 | 0.0152 | -0.0152 | -0.0152 | 24.1852 | 0.0530 | 0.0265 |
| 20 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0169 | -0.0132 | 0.0139 | -0.0132 | -0.0132 | 1.3533 | 0.0034 | 0.0232 |
| 21 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0187 | -0.0129 | 0.0140 | -0.0129 | -0.0129 | 1.2554 | 0.0030 | 0.0229 |
| 22 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0531 | -0.0126 | 0.0126 | -0.0126 | -0.0126 | 21.1083 | 0.0207 | 0.0220 |
| 23 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0385 | 0.0119 | 0.0148 | 0.0119 | 0.0119 | 7.7057 | 0.0059 | 0.0215 |
| 24 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0280 | -0.0112 | 0.0185 | -0.0112 | -0.0112 | 1.3289 | 0.0029 | 0.0214 |
| 25 | mod.cls_blocks.0.attn.h5 | CLS<-electron | 0.0519 | 0.0118 | 0.0118 | 0.0118 | 0.0118 | 16.0935 | 0.0301 | 0.0206 |
| 26 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0505 | 0.0117 | 0.0121 | 0.0117 | 0.0117 | 22.2225 | 0.0292 | 0.0205 |
| 27 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0217 | -0.0102 | 0.0175 | -0.0102 | -0.0102 | 1.1815 | 0.0031 | 0.0196 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0236 | 0.0069 | 0.0290 | 0.0069 | 0.0069 | 1.1885 | 0.0025 | 0.0176 |
| 29 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0187 | 0.0064 | 0.0306 | 0.0064 | 0.0064 | 1.1413 | 0.0027 | 0.0173 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0239 | -0.0086 | 0.0086 | -0.0086 | -0.0086 | 34.3553 | 0.0405 | 0.0150 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
