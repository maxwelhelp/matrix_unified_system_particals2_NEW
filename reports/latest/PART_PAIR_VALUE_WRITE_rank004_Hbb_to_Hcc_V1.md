# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9744**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0776 | 0.1649 | 0.1649 | 0.2894 | 0.1649 | 152.1469 | 0.0189 | 0.3508 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0834 | -0.1000 | 0.1000 | 0.1923 | -0.1000 | 152.1469 | 0.0284 | 0.2211 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.3795 | 0.0000 | 0.0000 | 0.0000 | 0.1898 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0675 | 0.0804 | 0.0804 | 0.1775 | 0.0804 | 102.3998 | 0.0170 | 0.1893 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0910 | -0.0337 | 0.0470 | 0.2296 | -0.0337 | 152.1469 | 0.0147 | 0.1603 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0857 | -6.446e-04 | 0.0897 | 0.2395 | -6.446e-04 | 152.1469 | 0.0192 | 0.1428 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0845 | 0.0365 | 0.0365 | 0.1934 | 0.0365 | 102.3998 | 0.0174 | 0.1423 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0768 | 0.0389 | 0.0389 | 0.1867 | 0.0389 | 102.3998 | 0.0194 | 0.1420 |
| 9 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0599 | 0.0618 | 0.0618 | 0.1002 | 0.0618 | 64.1643 | 0.0436 | 0.1273 |
| 10 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.1325 | 0.0494 | 0.0494 | 0.1187 | 0.0494 | 47.8742 | 0.0357 | 0.1211 |
| 11 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0556 | 0.0509 | 0.0509 | 0.0912 | 0.0509 | 64.1643 | 0.0367 | 0.1092 |
| 12 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0592 | 0.0506 | 0.0506 | 0.0895 | 0.0506 | 64.1643 | 0.0347 | 0.1081 |
| 13 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1910 | 0.0000 | 0.0000 | 0.0000 | 0.0955 |
| 14 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0441 | 0.0404 | 0.0404 | 0.0828 | 0.0404 | 64.1643 | 0.0340 | 0.0919 |
| 15 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0707 | 0.0020 | 0.0020 | 0.1698 | 0.0020 | 102.3998 | 0.0256 | 0.0874 |
| 16 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1671 | 0.0000 | 0.0000 | 0.0000 | 0.0836 |
| 17 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1432 | 0.0000 | 0.0000 | 0.0000 | 0.0716 |
| 18 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0000 | 0.0000 | 0.0000 | -0.1235 | 0.0000 | 0.0000 | 0.0000 | 0.0617 |
| 19 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0700 | 0.0243 | 0.0243 | 0.0297 | 0.0154 | 39.1109 | 0.0361 | 0.0452 |
| 20 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0469 | 0.0166 | 0.0169 | 0.0432 | 0.0106 | 25.5624 | 0.0352 | 0.0424 |
| 21 | mod.cls_blocks.1.attn.h3 | photon<-muon | 1.647e-04 | -7.155e-07 | 7.155e-07 | -0.0766 | -7.155e-07 | 1.9886 | 0.0286 | 0.0383 |
| 22 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | -0.0755 | 0.0000 | 0.0000 | 0.0000 | 0.0377 |
| 23 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0429 | 0.0157 | 0.0157 | 0.0260 | 0.0157 | 42.4997 | 0.0207 | 0.0326 |
| 24 | mod.cls_blocks.1.attn.h3 | neutral_hadron<-muon | 0.9196 | 0.0177 | 0.0177 | 0.0184 | 0.0177 | 3.9812 | 0.0200 | 0.0314 |
| 25 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0202 | 0.0168 | 0.0168 | 0.0195 | 0.0168 | 66.5560 | 0.0428 | 0.0307 |
| 26 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.1100 | 0.0108 | 0.0108 | -0.0301 | 0.0108 | 29.8071 | 0.0187 | 0.0285 |
| 27 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0308 | 0.0125 | 0.0125 | 0.0234 | 0.0125 | 42.4997 | 0.0158 | 0.0273 |
| 28 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0536 | -0.0579 | 0.0000 | 0.0000 | 0.0268 |
| 29 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0741 | -0.0095 | 0.0095 | -0.0292 | -0.0095 | 17.1857 | 0.0161 | 0.0264 |
| 30 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0249 | 0.0135 | 0.0135 | 0.0182 | 0.0135 | 66.5560 | 0.0351 | 0.0259 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-muon | 0.0764 | -0.0407 | 0.0407 | -0.0407 | -0.0407 | 23.3665 | 0.0355 | 0.0713 |
| 2 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0510 | -0.0233 | 0.0233 | -0.0233 | -0.0233 | 24.4580 | 0.0259 | 0.0408 |
| 3 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0241 | -0.0136 | 0.0136 | -0.0136 | -0.0136 | 20.8767 | 0.0355 | 0.0239 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0350 | 0.0124 | 0.0139 | 0.0124 | 0.0124 | 8.0847 | 0.0036 | 0.0220 |
| 5 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0337 | -0.0111 | 0.0160 | -0.0111 | -0.0111 | 19.7151 | 0.0350 | 0.0207 |
| 6 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0290 | 0.0102 | 0.0103 | 0.0102 | 0.0102 | 7.0021 | 0.0071 | 0.0179 |
| 7 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0268 | 0.0094 | 0.0150 | 0.0094 | 0.0094 | 5.6902 | 0.0070 | 0.0178 |
| 8 | mod.blocks.1.attn.h5 | muon<-electron | 0.3002 | -0.0088 | 0.0088 | -0.0088 | -0.0088 | 7.5065 | 0.0070 | 0.0153 |
| 9 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0718 | -0.0085 | 0.0085 | -0.0085 | -0.0085 | 15.5033 | 0.0161 | 0.0149 |
| 10 | mod.cls_blocks.0.attn.h5 | neutral_hadron<-electron | 0.0427 | -0.0084 | 0.0084 | -0.0084 | -0.0084 | 16.4546 | 0.0162 | 0.0148 |
| 11 | mod.blocks.1.attn.h4 | electron<-muon | 0.2144 | -0.0080 | 0.0080 | -0.0080 | -0.0080 | 8.7343 | 0.0096 | 0.0141 |
| 12 | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0279 | -0.0080 | 0.0081 | -0.0080 | -0.0080 | 20.2925 | 0.0226 | 0.0141 |
| 13 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0347 | 0.0072 | 0.0121 | 0.0072 | 0.0072 | 5.8651 | 0.0079 | 0.0138 |
| 14 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0374 | 0.0065 | 0.0126 | 0.0065 | 0.0065 | 5.0534 | 0.0072 | 0.0129 |
| 15 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0324 | 0.0062 | 0.0124 | 0.0062 | 0.0062 | 7.2559 | 0.0110 | 0.0124 |
| 16 | mod.blocks.3.attn.h4 | electron<-muon | 0.8758 | 0.0063 | 0.0063 | 0.0063 | 0.0063 | 5.2880 | 0.0079 | 0.0111 |
| 17 | mod.blocks.3.attn.h4 | muon<-electron | 0.2794 | 0.0063 | 0.0063 | 0.0063 | 0.0063 | 8.6447 | 0.0052 | 0.0109 |
| 18 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0406 | 0.0040 | 0.0191 | 0.0040 | 0.0040 | 11.1661 | 0.0031 | 0.0108 |
| 19 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0172 | 0.0061 | 0.0061 | 0.0061 | 0.0061 | 15.6721 | 0.0346 | 0.0107 |
| 20 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0273 | -0.0049 | 0.0104 | -0.0049 | -0.0049 | 3.7810 | 0.0073 | 0.0099 |
| 21 | mod.cls_blocks.0.attn.h0 | photon<-neutral_hadron | 0.0294 | -0.0047 | 0.0114 | -0.0047 | -0.0047 | 4.8942 | 0.0108 | 0.0099 |
| 22 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0244 | 0.0051 | 0.0085 | 0.0051 | 0.0051 | 1.4384 | 0.0021 | 0.0098 |
| 23 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0241 | 0.0051 | 0.0085 | 0.0051 | 0.0051 | 1.1798 | 0.0019 | 0.0098 |
| 24 | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0251 | 0.0049 | 0.0085 | 0.0049 | 0.0049 | 1.4006 | 0.0020 | 0.0095 |
| 25 | mod.cls_blocks.0.attn.h1 | photon<-photon | 0.0205 | 0.0049 | 0.0081 | 0.0049 | 0.0049 | 1.4018 | 0.0021 | 0.0093 |
| 26 | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0258 | 0.0048 | 0.0084 | 0.0048 | 0.0048 | 1.5027 | 0.0020 | 0.0093 |
| 27 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0150 | -0.0049 | 0.0058 | -0.0049 | -0.0049 | 15.8414 | 0.0374 | 0.0089 |
| 28 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0282 | -0.0049 | 0.0049 | -0.0049 | -0.0049 | 26.9819 | 0.0185 | 0.0086 |
| 29 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0517 | -0.0047 | 0.0047 | -0.0047 | -0.0047 | 21.6735 | 0.0357 | 0.0083 |
| 30 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-photon | 0.0258 | -0.0043 | 0.0057 | -0.0043 | -0.0043 | 0.9860 | 0.0012 | 0.0078 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
