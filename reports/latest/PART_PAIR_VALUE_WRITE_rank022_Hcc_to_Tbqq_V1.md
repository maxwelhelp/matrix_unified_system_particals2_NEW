# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9680**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0834 | -0.7200 | 0.7200 | -0.7151 | -0.5129 | 152.1468 | 0.0865 | 1.2576 |
| 2 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0716 | -0.2745 | 0.2745 | -0.2746 | -0.1690 | 102.3998 | 0.0507 | 0.4804 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0430 | -0.2666 | 0.2742 | -0.2805 | -0.2615 | 70.0330 | 0.0594 | 0.4754 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0881 | -0.0949 | 0.1303 | -0.3521 | -0.0949 | 152.1469 | 0.0349 | 0.3035 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0432 | -0.1004 | 0.1055 | -0.1802 | -0.0945 | 48.0543 | 0.0349 | 0.2168 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0881 | -0.0949 | 0.1303 | -0.1784 | -0.0949 | 152.1469 | 0.0349 | 0.2167 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.3737 | 0.0000 | 0.0000 | 0.0000 | 0.1869 |
| 8 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.3705 | 0.0000 | 0.0000 | 0.0000 | 0.1852 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0869 | -0.0684 | 0.0684 | -0.1869 | -0.0684 | 102.3998 | 0.0234 | 0.1789 |
| 10 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0821 | -0.0966 | 0.0966 | -0.0966 | -0.0966 | 152.1468 | 0.0456 | 0.1690 |
| 11 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0869 | -0.0684 | 0.0684 | -0.1499 | -0.0684 | 102.3998 | 0.0234 | 0.1604 |
| 12 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0689 | -0.0914 | 0.0914 | -0.0914 | -0.0914 | 102.3998 | 0.0250 | 0.1599 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0323 | -0.0464 | 0.0725 | -0.0470 | -0.0425 | 9.5044 | 0.0094 | 0.0880 |
| 14 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1700 | 0.0000 | 0.0000 | 0.0000 | 0.0850 |
| 15 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0134 | 0.0029 | 0.0029 | -0.1564 | -0.0125 | 19.3105 | 0.0197 | 0.0819 |
| 16 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0513 | -0.0417 | 0.0417 | -0.0407 | -0.0353 | 64.1643 | 0.0311 | 0.0725 |
| 17 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1426 | 0.0000 | 0.0000 | 0.0000 | 0.0713 |
| 18 | mod.cls_blocks.1.attn.h2 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1171 | 0.0000 | 0.0000 | 0.0000 | 0.0585 |
| 19 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0218 | -0.0087 | 0.0111 | -0.0916 | -0.0186 | 66.5561 | 0.0441 | 0.0573 |
| 20 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0264 | 0.0312 | 0.0312 | 0.0312 | 0.0312 | 53.7968 | 0.0361 | 0.0546 |
| 21 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0508 | -0.0184 | 0.0184 | -0.0580 | -0.0184 | 64.1643 | 0.0173 | 0.0521 |
| 22 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0309 | -0.0188 | 0.0269 | -0.0498 | -0.0262 | 45.7353 | 0.0273 | 0.0504 |
| 23 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0121 | 0.0288 | 0.0288 | 0.0288 | 0.0229 | 31.0240 | 0.0999 | 0.0504 |
| 24 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0508 | -0.0184 | 0.0184 | -0.0526 | -0.0184 | 64.1643 | 0.0173 | 0.0494 |
| 25 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0256 | 0.0230 | 0.0321 | 0.0364 | 0.0200 | 1.8575 | 0.0056 | 0.0492 |
| 26 | mod.cls_blocks.0.attn.h7 | photon<-muon | 0.0542 | 0.0256 | 0.0273 | 0.0256 | 0.0253 | 9.2484 | 0.0287 | 0.0452 |
| 27 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0528 | -0.0245 | 0.0260 | -0.0245 | -0.0251 | 19.4114 | 0.0235 | 0.0433 |
| 28 | mod.cls_blocks.0.attn.h7 | muon<-neutral_hadron | 0.0345 | 0.0235 | 0.0257 | 0.0228 | -0.0069 | 3.1938 | 0.0070 | 0.0413 |
| 29 | mod.blocks.6.attn.h1 | muon<-electron | 0.4971 | 0.0210 | 0.0210 | 0.0210 | 0.0208 | 8.5444 | 0.0108 | 0.0367 |
| 30 | mod.cls_blocks.0.attn.h7 | electron<-neutral_hadron | 0.0287 | 0.0205 | 0.0223 | 0.0205 | 0.0205 | 2.6533 | 0.0056 | 0.0364 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0834 | -0.7200 | 0.7200 | -0.7200 | -0.7200 | 152.1468 | 0.0865 | 1.2601 |
| 2 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0716 | -0.2745 | 0.2745 | -0.2745 | -0.2745 | 102.3998 | 0.0507 | 0.4803 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0434 | -0.2645 | 0.2762 | -0.2645 | -0.2645 | 70.0770 | 0.0594 | 0.4657 |
| 4 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0359 | -0.1010 | 0.1048 | -0.1010 | -0.1010 | 47.7478 | 0.0349 | 0.1777 |
| 5 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0821 | -0.0966 | 0.0966 | -0.0966 | -0.0966 | 152.1468 | 0.0456 | 0.1690 |
| 6 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0689 | -0.0914 | 0.0914 | -0.0914 | -0.0914 | 102.3998 | 0.0250 | 0.1599 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0323 | -0.0464 | 0.0725 | -0.0464 | -0.0464 | 9.5044 | 0.0094 | 0.0877 |
| 8 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0513 | -0.0417 | 0.0417 | -0.0417 | -0.0417 | 64.1643 | 0.0311 | 0.0730 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0264 | 0.0312 | 0.0312 | 0.0312 | 0.0312 | 53.7968 | 0.0361 | 0.0546 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0121 | 0.0288 | 0.0288 | 0.0288 | 0.0288 | 31.0240 | 0.0999 | 0.0504 |
| 11 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0256 | 0.0230 | 0.0321 | 0.0230 | 0.0230 | 1.8575 | 0.0056 | 0.0425 |
| 12 | mod.cls_blocks.0.attn.h7 | muon<-neutral_hadron | 0.0345 | 0.0235 | 0.0257 | 0.0235 | 0.0235 | 3.1938 | 0.0070 | 0.0417 |
| 13 | mod.blocks.6.attn.h1 | muon<-electron | 0.4971 | 0.0210 | 0.0210 | 0.0210 | 0.0210 | 8.5444 | 0.0108 | 0.0367 |
| 14 | mod.cls_blocks.0.attn.h7 | electron<-neutral_hadron | 0.0287 | 0.0205 | 0.0223 | 0.0205 | 0.0205 | 2.6533 | 0.0056 | 0.0364 |
| 15 | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0310 | 0.0199 | 0.0240 | 0.0199 | 0.0199 | 4.2567 | 0.0137 | 0.0358 |
| 16 | mod.blocks.3.attn.h0 | muon<-electron | 0.5002 | -0.0203 | 0.0203 | -0.0203 | -0.0203 | 9.1077 | 0.0110 | 0.0354 |
| 17 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0309 | -0.0188 | 0.0269 | -0.0188 | -0.0188 | 45.7353 | 0.0273 | 0.0349 |
| 18 | mod.cls_blocks.0.attn.h1 | muon<-neutral_hadron | 0.0519 | -0.0186 | 0.0204 | -0.0186 | -0.0186 | 4.2570 | 0.0070 | 0.0330 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0300 | -0.0176 | 0.0236 | -0.0176 | -0.0176 | 6.7897 | 0.0061 | 0.0323 |
| 20 | mod.cls_blocks.0.attn.h6 | muon<-neutral_hadron | 0.0392 | 0.0184 | 0.0184 | 0.0184 | 0.0184 | 3.7772 | 0.0080 | 0.0322 |
| 21 | mod.cls_blocks.0.attn.h7 | electron<-charged_hadron | 0.0261 | 0.0177 | 0.0194 | 0.0177 | 0.0177 | 0.8796 | 0.0019 | 0.0315 |
| 22 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0589 | -0.0179 | 0.0179 | -0.0179 | -0.0179 | 64.1643 | 0.0218 | 0.0313 |
| 23 | mod.blocks.4.attn.h7 | electron<-muon | 0.2239 | -0.0169 | 0.0169 | -0.0169 | -0.0169 | 6.7530 | 0.0228 | 0.0296 |
| 24 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0398 | -0.0123 | 0.0435 | -0.0123 | -0.0123 | 69.3230 | 0.0451 | 0.0294 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0294 | -0.0159 | 0.0163 | -0.0159 | -0.0159 | 32.7840 | 0.0232 | 0.0279 |
| 26 | mod.cls_blocks.0.attn.h4 | muon<-photon | 0.0187 | 0.0148 | 0.0189 | 0.0148 | 0.0148 | 1.3477 | 0.0051 | 0.0269 |
| 27 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0243 | -0.0151 | 0.0151 | -0.0151 | -0.0151 | 17.5515 | 0.0626 | 0.0265 |
| 28 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0301 | -0.0145 | 0.0145 | -0.0145 | -0.0145 | 42.4997 | 0.0444 | 0.0254 |
| 29 | mod.blocks.7.attn.h3 | muon<-electron | 0.9526 | 0.0131 | 0.0131 | 0.0131 | 0.0131 | 5.5495 | 0.0049 | 0.0230 |
| 30 | mod.cls_blocks.0.attn.h1 | electron<-neutral_hadron | 0.0396 | -0.0122 | 0.0151 | -0.0122 | -0.0122 | 3.6330 | 0.0049 | 0.0221 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
