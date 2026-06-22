# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8672**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0963 | -1.2670 | 1.2670 | -1.2648 | -1.2670 | 152.1469 | 0.0912 | 2.2161 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1141 | -0.7504 | 0.7504 | -0.8964 | -0.7504 | 152.1469 | 0.0521 | 1.3862 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1074 | -0.6762 | 0.6762 | -0.7451 | -0.6762 | 152.1469 | 0.0468 | 1.2177 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1451 | -0.3821 | 0.3821 | -0.7337 | -0.3821 | 152.1469 | 0.0236 | 0.8445 |
| 5 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0894 | -0.3938 | 0.3938 | -0.3985 | -0.3938 | 102.3998 | 0.0510 | 0.6915 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1047 | -0.2444 | 0.2444 | -0.2952 | -0.2444 | 102.3998 | 0.0332 | 0.4531 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0909 | -0.2077 | 0.2077 | -0.2723 | -0.2077 | 102.3998 | 0.0299 | 0.3958 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.1476 | -0.1682 | 0.1682 | -0.2737 | -0.1682 | 102.3998 | 0.0221 | 0.3472 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0593 | -0.1470 | 0.2045 | -0.1286 | 0.2568 | 11.4398 | 0.0159 | 0.2625 |
| 10 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.2239 | 0.1065 | 0.1065 | 0.1065 | 0.1096 | 50.0006 | 0.0275 | 0.1864 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0524 | 0.0995 | 0.0995 | 0.0995 | 0.0780 | 44.2061 | 0.0503 | 0.1741 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0524 | 0.0995 | 0.0995 | 0.0901 | 0.2198 | 44.2061 | 0.0503 | 0.1694 |
| 13 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.2239 | 0.1065 | 0.1065 | 0.0672 | 0.1137 | 50.0006 | 0.0275 | 0.1668 |
| 14 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.3168 | 0.0000 | 0.0000 | 0.0000 | 0.1584 |
| 15 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.1097 | 0.0685 | 0.0685 | 0.0685 | 0.0610 | 47.1133 | 0.0270 | 0.1198 |
| 16 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.1097 | 0.0685 | 0.0685 | 0.0549 | 0.0877 | 47.1133 | 0.0270 | 0.1130 |
| 17 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0359 | -0.0413 | 0.1786 | -0.0417 | -0.0046 | 3.9240 | 0.0091 | 0.1068 |
| 18 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0669 | -0.0609 | 0.0609 | -0.0543 | -0.0609 | 64.1643 | 0.0212 | 0.1032 |
| 19 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0235 | -0.0501 | 0.0501 | -0.0602 | -0.0501 | 66.5560 | 0.0527 | 0.0927 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0338 | 0.0492 | 0.0664 | 0.0500 | 0.0228 | 2.2749 | 0.0072 | 0.0907 |
| 21 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0495 | -0.0478 | 0.0586 | -0.0467 | 0.0837 | 9.5302 | 0.0097 | 0.0858 |
| 22 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0322 | 0.0411 | 0.0444 | 0.0507 | 0.0145 | 1.9060 | 0.0051 | 0.0775 |
| 23 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0361 | 0.0325 | 0.0628 | 0.0380 | -4.898e-04 | 7.5169 | 0.0235 | 0.0672 |
| 24 | mod.cls_blocks.0.attn.h3 | CLS<-muon | 0.1549 | 0.0359 | 0.0359 | 0.0425 | 0.0315 | 21.0512 | 0.0278 | 0.0662 |
| 25 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0271 | -0.0315 | 0.0315 | -0.0500 | -0.0315 | 66.5560 | 0.0418 | 0.0644 |
| 26 | mod.cls_blocks.0.attn.h3 | charged_hadron<-muon | 0.1549 | 0.0359 | 0.0359 | 0.0359 | 0.0274 | 21.0512 | 0.0278 | 0.0629 |
| 27 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0784 | -0.0353 | 0.0353 | -0.0359 | -0.0353 | 64.1643 | 0.0162 | 0.0621 |
| 28 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0675 | -0.0330 | 0.0330 | -0.0375 | -0.0330 | 64.1643 | 0.0159 | 0.0600 |
| 29 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0231 | -0.0255 | 0.0255 | -0.0474 | -0.0255 | 66.5560 | 0.0383 | 0.0556 |
| 30 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0389 | -0.0248 | 0.0248 | -0.0489 | -0.0248 | 66.5560 | 0.0379 | 0.0555 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0671 | -0.1886 | 0.2555 | -0.1886 | -0.1886 | 15.8787 | 0.0159 | 0.3467 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0356 | -0.0970 | 0.2103 | -0.0970 | -0.0970 | 4.2237 | 0.0091 | 0.1981 |
| 3 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0651 | -0.0644 | 0.0812 | -0.0644 | -0.0644 | 12.0204 | 0.0097 | 0.1169 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0372 | 0.0610 | 0.0701 | 0.0610 | 0.0610 | 7.5377 | 0.0235 | 0.1090 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0357 | 0.0511 | 0.0703 | 0.0511 | 0.0511 | 2.2839 | 0.0072 | 0.0942 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0358 | 0.0435 | 0.0468 | 0.0435 | 0.0435 | 2.2544 | 0.0051 | 0.0770 |
| 7 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0365 | -0.0352 | 0.0581 | -0.0352 | -0.0352 | 3.1647 | 0.0047 | 0.0673 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0314 | -0.0223 | 0.0747 | -0.0223 | -0.0223 | 2.1218 | 0.0037 | 0.0521 |
| 9 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0575 | 0.0204 | 0.0224 | 0.0204 | 0.0204 | 7.3320 | 0.0118 | 0.0361 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0317 | 0.0196 | 0.0237 | 0.0196 | 0.0196 | 3.4185 | 0.0075 | 0.0353 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0221 | 0.0146 | 0.0226 | 0.0146 | 0.0146 | 1.5209 | 0.0036 | 0.0276 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0171 | 0.0152 | 0.0152 | 0.0152 | 0.0152 | 12.0435 | 0.0560 | 0.0266 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0171 | 0.0152 | 0.0152 | 0.0152 | 0.0152 | 12.0435 | 0.0560 | 0.0266 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0247 | 0.0126 | 0.0257 | 0.0126 | 0.0126 | 7.5345 | 0.0155 | 0.0254 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0326 | -0.0037 | 0.0711 | -0.0037 | -0.0037 | 2.1615 | 0.0044 | 0.0234 |
| 16 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0397 | 0.0130 | 0.0144 | 0.0130 | 0.0130 | 6.4170 | 0.0120 | 0.0230 |
| 17 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0324 | -0.0037 | 0.0633 | -0.0037 | -0.0037 | 8.5947 | 0.0171 | 0.0214 |
| 18 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0299 | -0.0089 | 0.0220 | -0.0089 | -0.0089 | 1.7344 | 0.0022 | 0.0189 |
| 19 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0342 | 0.0099 | 0.0149 | 0.0099 | 0.0099 | 1.7715 | 0.0037 | 0.0186 |
| 20 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0329 | 0.0102 | 0.0126 | 0.0102 | 0.0102 | 2.0861 | 0.0031 | 0.0185 |
| 21 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0682 | -0.0078 | 0.0143 | -0.0078 | -0.0078 | 7.8442 | 0.0043 | 0.0152 |
| 22 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0397 | 0.0082 | 0.0114 | 0.0082 | 0.0082 | 1.9745 | 0.0036 | 0.0151 |
| 23 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0397 | 0.0073 | 0.0107 | 0.0073 | 0.0073 | 2.0977 | 0.0037 | 0.0137 |
| 24 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0483 | -0.0061 | 0.0172 | -0.0061 | -0.0061 | 9.5131 | 0.0117 | 0.0134 |
| 25 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0162 | 0.0072 | 0.0072 | 0.0072 | 0.0072 | 9.4024 | 0.0324 | 0.0126 |
| 26 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0162 | 0.0072 | 0.0072 | 0.0072 | 0.0072 | 9.4024 | 0.0324 | 0.0126 |
| 27 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0247 | 8.248e-05 | 0.0477 | 8.248e-05 | 8.248e-05 | 2.0211 | 0.0046 | 0.0121 |
| 28 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0373 | 0.0059 | 0.0119 | 0.0059 | 0.0059 | 7.2350 | 0.0107 | 0.0118 |
| 29 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-photon | 0.0353 | 0.0060 | 0.0110 | 0.0060 | 0.0060 | 2.7544 | 0.0055 | 0.0117 |
| 30 | mod.cls_blocks.0.attn.h6 | CLS<-charged_hadron | 0.0309 | -0.0039 | 0.0199 | -0.0039 | -0.0039 | 1.7766 | 0.0025 | 0.0109 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
