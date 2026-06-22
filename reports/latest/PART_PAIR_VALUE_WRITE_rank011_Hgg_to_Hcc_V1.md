# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8768**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0779 | 0.1604 | 0.1604 | 0.3581 | 0.1604 | 152.1469 | 0.0259 | 0.3795 |
| 2 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0828 | 0.1573 | 0.1573 | 0.3099 | 0.1573 | 102.3998 | 0.0439 | 0.3516 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0678 | 0.1492 | 0.1492 | 0.2948 | 0.1492 | 102.3998 | 0.0421 | 0.3339 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0821 | 0.1208 | 0.1208 | 0.3205 | 0.1208 | 152.1469 | 0.0233 | 0.3112 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1043 | 0.1129 | 0.1129 | 0.3383 | 0.1129 | 152.1469 | 0.0243 | 0.3103 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0675 | 0.1176 | 0.1176 | 0.2705 | 0.1176 | 102.3998 | 0.0356 | 0.2823 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0683 | 0.0495 | 0.0495 | 0.2397 | 0.0495 | 152.1469 | 0.0168 | 0.1817 |
| 8 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.2059 | 0.0723 | 0.0723 | 0.0723 | 0.0723 | 41.7960 | 0.0268 | 0.1265 |
| 9 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0517 | 0.0148 | 0.0148 | 0.1945 | 0.0148 | 102.3998 | 0.0143 | 0.1158 |
| 10 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.1044 | 0.0597 | 0.0597 | 0.0597 | 0.0597 | 34.5482 | 0.0439 | 0.1045 |
| 11 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0681 | 0.0372 | 0.0372 | 0.0540 | 0.0372 | 64.1643 | 0.0234 | 0.0735 |
| 12 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0513 | 0.0266 | 0.0266 | 0.0422 | 0.0266 | 64.1643 | 0.0220 | 0.0544 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0524 | 0.0258 | 0.0258 | 0.0418 | 0.0258 | 64.1643 | 0.0209 | 0.0531 |
| 14 | mod.cls_blocks.1.attn.h3 | photon<-muon | 0.9770 | 0.0302 | 0.0302 | 0.0302 | 0.0302 | 2.9678 | 0.0266 | 0.0529 |
| 15 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0290 | 0.0282 | 0.0373 | 0.0282 | -0.0616 | 7.1954 | 0.0080 | 0.0516 |
| 16 | mod.cls_blocks.1.attn.h4 | neutral_hadron<-electron | 0.7833 | 0.0243 | 0.0243 | 0.0243 | 0.0243 | 3.5594 | 0.0221 | 0.0425 |
| 17 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0785 | 0.0219 | 0.0263 | 0.0219 | 0.0237 | 26.7939 | 0.0154 | 0.0394 |
| 18 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0471 | 0.0196 | 0.0203 | 0.0196 | 0.0076 | 19.4607 | 0.0194 | 0.0344 |
| 19 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0390 | 0.0125 | 0.0125 | 0.0295 | 0.0125 | 64.1643 | 0.0163 | 0.0304 |
| 20 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0316 | 0.0143 | 0.0214 | 0.0189 | -0.0434 | 10.8429 | 0.0046 | 0.0291 |
| 21 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-electron | 0.0785 | 0.0129 | 0.0129 | 0.0129 | 0.0129 | 23.4803 | 0.0143 | 0.0226 |
| 22 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.1002 | 0.0126 | 0.0126 | 0.0126 | 0.0126 | 47.6015 | 0.0194 | 0.0221 |
| 23 | mod.cls_blocks.1.attn.h4 | photon<-muon | 0.9369 | 0.0125 | 0.0125 | 0.0125 | 0.0125 | 2.2527 | 0.0264 | 0.0219 |
| 24 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0217 | -0.0085 | 0.0150 | -0.0155 | -0.0133 | 1.1289 | 0.0020 | 0.0201 |
| 25 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0385 | -0.0108 | 0.0108 | -0.0108 | -0.0108 | 26.4551 | 0.0234 | 0.0189 |
| 26 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0179 | -0.0073 | 0.0112 | -0.0138 | -0.0092 | 1.1210 | 0.0021 | 0.0170 |
| 27 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0186 | -0.0074 | 0.0106 | -0.0119 | -0.0058 | 1.1701 | 0.0022 | 0.0160 |
| 28 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.6164 | 0.0086 | 0.0115 | 0.0086 | 0.0086 | 2.1044 | 0.0146 | 0.0158 |
| 29 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0445 | -0.0090 | 0.0090 | -0.0090 | -0.0090 | 37.7163 | 0.0243 | 0.0157 |
| 30 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0279 | 0.0091 | 0.0100 | 0.0077 | 0.0062 | 5.3337 | 0.0076 | 0.0155 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0316 | 0.0289 | 0.0381 | 0.0289 | 0.0289 | 8.4250 | 0.0080 | 0.0529 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0342 | 0.0165 | 0.0238 | 0.0165 | 0.0165 | 11.8327 | 0.0046 | 0.0307 |
| 3 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0330 | 0.0124 | 0.0133 | 0.0124 | 0.0124 | 5.9908 | 0.0076 | 0.0219 |
| 4 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0245 | -0.0121 | 0.0121 | -0.0121 | -0.0121 | 25.4524 | 0.0439 | 0.0212 |
| 5 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0194 | -0.0093 | 0.0122 | -0.0093 | -0.0093 | 1.2475 | 0.0022 | 0.0169 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0242 | 0.0071 | 0.0202 | 0.0071 | 0.0071 | 5.7155 | 0.0088 | 0.0156 |
| 7 | mod.blocks.3.attn.h4 | electron<-electron | 0.1797 | -0.0082 | 0.0082 | -0.0082 | -0.0082 | 3.1959 | 0.0017 | 0.0143 |
| 8 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0219 | -0.0073 | 0.0121 | -0.0073 | -0.0073 | 10.3563 | 0.0218 | 0.0140 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0176 | 0.0072 | 0.0125 | 0.0072 | 0.0072 | 1.8973 | 0.0014 | 0.0139 |
| 10 | mod.blocks.1.attn.h4 | electron<-electron | 0.0955 | -0.0079 | 0.0079 | -0.0079 | -0.0079 | 3.9914 | 0.0035 | 0.0138 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0188 | -0.0073 | 0.0113 | -0.0073 | -0.0073 | 1.1793 | 0.0021 | 0.0137 |
| 12 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0223 | -0.0066 | 0.0152 | -0.0066 | -0.0066 | 1.1250 | 0.0020 | 0.0137 |
| 13 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0286 | -0.0078 | 0.0078 | -0.0078 | -0.0078 | 28.2222 | 0.0268 | 0.0136 |
| 14 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0280 | 0.0075 | 0.0075 | 0.0075 | 0.0075 | 13.0035 | 0.0153 | 0.0131 |
| 15 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0193 | -0.0059 | 0.0138 | -0.0059 | -0.0059 | 1.3167 | 0.0022 | 0.0123 |
| 16 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0272 | 0.0061 | 0.0087 | 0.0061 | 0.0061 | 5.6039 | 0.0064 | 0.0113 |
| 17 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0251 | -0.0056 | 0.0076 | -0.0056 | -0.0056 | 4.3218 | 0.0044 | 0.0103 |
| 18 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0230 | 0.0054 | 0.0054 | 0.0054 | 0.0054 | 15.5497 | 0.0166 | 0.0094 |
| 19 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0254 | 0.0049 | 0.0079 | 0.0049 | 0.0049 | 1.0590 | 0.0015 | 0.0093 |
| 20 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0183 | -0.0045 | 0.0084 | -0.0045 | -0.0045 | 12.9369 | 0.0193 | 0.0089 |
| 21 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0182 | -0.0051 | 0.0051 | -0.0051 | -0.0051 | 24.5209 | 0.0243 | 0.0089 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0226 | -0.0049 | 0.0060 | -0.0049 | -0.0049 | 1.2230 | 0.0012 | 0.0088 |
| 23 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0196 | 0.0022 | 0.0196 | 0.0022 | 0.0022 | 1.5945 | 0.0024 | 0.0083 |
| 24 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0172 | -0.0047 | 0.0047 | -0.0047 | -0.0047 | 14.0721 | 0.0194 | 0.0082 |
| 25 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0202 | -0.0031 | 0.0137 | -0.0031 | -0.0031 | 4.2905 | 0.0075 | 0.0080 |
| 26 | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0238 | 0.0042 | 0.0069 | 0.0042 | 0.0042 | 1.0796 | 0.0013 | 0.0080 |
| 27 | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0233 | 0.0041 | 0.0071 | 0.0041 | 0.0041 | 1.0883 | 0.0013 | 0.0080 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0229 | 0.0027 | 0.0159 | 0.0027 | 0.0027 | 1.1122 | 0.0018 | 0.0079 |
| 29 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0252 | -0.0041 | 0.0063 | -0.0041 | -0.0041 | 5.8027 | 0.0071 | 0.0078 |
| 30 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0308 | 0.0040 | 0.0053 | 0.0040 | 0.0040 | 5.4849 | 0.0041 | 0.0074 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
