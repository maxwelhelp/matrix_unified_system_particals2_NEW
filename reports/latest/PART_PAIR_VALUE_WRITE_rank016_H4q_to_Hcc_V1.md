# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9152**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0678 | 0.1123 | 0.1123 | 0.1789 | 0.1123 | 102.3998 | 0.0306 | 0.2298 |
| 2 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0724 | 0.0809 | 0.0809 | 0.1415 | 0.0809 | 102.3998 | 0.0290 | 0.1718 |
| 3 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0740 | 0.0704 | 0.0704 | 0.1545 | 0.0704 | 102.3998 | 0.0285 | 0.1652 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0705 | 0.0586 | 0.0586 | 0.0629 | 0.0586 | 152.1469 | 0.0272 | 0.1047 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0754 | -0.0432 | 0.0432 | 0.0892 | -0.0432 | 152.1469 | 0.0284 | 0.0986 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0501 | -0.0347 | 0.0403 | -0.0327 | 0.0316 | 18.2411 | 0.0081 | 0.0612 |
| 7 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0443 | 0.0234 | 0.0234 | 0.0519 | 0.0234 | 24.7258 | 0.0378 | 0.0552 |
| 8 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0416 | 0.0129 | 0.0129 | 0.0413 | 0.0175 | 26.4890 | 0.0349 | 0.0367 |
| 9 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0507 | 0.0168 | 0.0210 | 0.0204 | 0.0162 | 8.8752 | 0.0113 | 0.0323 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0742 | -0.0177 | 0.0470 | -7.581e-04 | -0.0177 | 152.1469 | 0.0281 | 0.0299 |
| 11 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0338 | 0.0110 | 0.0135 | 0.0135 | 0.0103 | 13.5923 | 0.0224 | 0.0211 |
| 12 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0252 | -0.0095 | 0.0095 | -0.0180 | -0.0095 | 66.5560 | 0.0388 | 0.0209 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0411 | 0.0000 | 0.0000 | 0.0000 | 0.0205 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0253 | -0.0083 | 0.0083 | -0.0183 | -0.0083 | 66.5560 | 0.0376 | 0.0195 |
| 15 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0443 | 0.0103 | 0.0172 | 0.0074 | -0.0290 | 13.1126 | 0.0070 | 0.0183 |
| 16 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0444 | 0.0091 | 0.0091 | 0.0134 | 0.0091 | 64.1643 | 0.0204 | 0.0180 |
| 17 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0353 | 0.0098 | 0.0098 | 0.0083 | 0.0098 | 64.1643 | 0.0187 | 0.0165 |
| 18 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0421 | 0.0093 | 0.0093 | 0.0089 | 0.0093 | 64.1643 | 0.0200 | 0.0160 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0295 | 0.0000 | 0.0000 | 0.0000 | 0.0147 |
| 20 | mod.cls_blocks.1.attn.h2 | photon<-CLS | 0.2686 | 0.0082 | 0.0082 | 0.0083 | 0.0082 | 2.4856 | 0.0325 | 0.0144 |
| 21 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0254 | -0.0045 | 0.0045 | -0.0157 | -0.0045 | 66.5560 | 0.0339 | 0.0136 |
| 22 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0314 | -0.0065 | 0.0088 | -0.0097 | -0.0113 | 7.1284 | 0.0072 | 0.0135 |
| 23 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0363 | -5.730e-04 | 6.299e-04 | 0.0249 | -0.0011 | 3.5032 | 0.0234 | 0.0132 |
| 24 | mod.cls_blocks.1.attn.h3 | neutral_hadron<-muon | 0.0309 | 3.111e-05 | 3.126e-05 | 0.0255 | 3.111e-05 | 3.7703 | 0.0276 | 0.0128 |
| 25 | mod.cls_blocks.1.attn.h3 | charged_hadron<-electron | 0.2069 | 0.0040 | 0.0041 | 0.0151 | 0.0045 | 1.0214 | 0.0078 | 0.0126 |
| 26 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0322 | 0.0069 | 0.0094 | 0.0062 | 0.0045 | 1.4127 | 0.0021 | 0.0123 |
| 27 | mod.cls_blocks.1.attn.h0 | neutral_hadron<-muon | 0.1340 | 0.0065 | 0.0065 | 0.0066 | 0.0065 | 2.6974 | 0.0554 | 0.0114 |
| 28 | mod.cls_blocks.1.attn.h2 | CLS<-CLS | 0.2035 | 0.0061 | 0.0062 | 0.0062 | 0.0061 | 2.4089 | 0.0307 | 0.0108 |
| 29 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0267 | 0.0051 | 0.0081 | 0.0073 | -0.0090 | 5.0778 | 0.0058 | 0.0107 |
| 30 | mod.cls_blocks.0.attn.h3 | charged_hadron<-electron | 0.0185 | 9.504e-04 | 0.0019 | 0.0178 | 0.0077 | 4.7656 | 0.0071 | 0.0103 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0501 | -0.0347 | 0.0403 | -0.0347 | -0.0347 | 18.2411 | 0.0081 | 0.0622 |
| 2 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0443 | 0.0234 | 0.0234 | 0.0234 | 0.0234 | 24.7258 | 0.0378 | 0.0410 |
| 3 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0336 | 0.0129 | 0.0129 | 0.0129 | 0.0129 | 21.3602 | 0.0349 | 0.0226 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0443 | 0.0103 | 0.0172 | 0.0103 | 0.0103 | 13.1126 | 0.0070 | 0.0198 |
| 5 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0322 | 0.0069 | 0.0094 | 0.0069 | 0.0069 | 1.4127 | 0.0021 | 0.0127 |
| 6 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0314 | -0.0065 | 0.0088 | -0.0065 | -0.0065 | 7.1284 | 0.0072 | 0.0120 |
| 7 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-muon | 0.0341 | -0.0068 | 0.0068 | -0.0068 | -0.0068 | 20.7007 | 0.0281 | 0.0119 |
| 8 | mod.cls_blocks.1.attn.h0 | neutral_hadron<-muon | 0.1340 | 0.0065 | 0.0065 | 0.0065 | 0.0065 | 2.6974 | 0.0554 | 0.0114 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0289 | 0.0060 | 0.0086 | 0.0060 | 0.0060 | 5.1571 | 0.0058 | 0.0112 |
| 10 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0173 | -0.0056 | 0.0056 | -0.0056 | -0.0056 | 6.8503 | 0.0102 | 0.0098 |
| 11 | mod.blocks.3.attn.h0 | electron<-muon | 0.1659 | -0.0055 | 0.0056 | -0.0055 | -0.0055 | 2.6056 | 0.0016 | 0.0096 |
| 12 | mod.blocks.2.attn.h3 | muon<-electron | 0.1556 | 0.0055 | 0.0055 | 0.0055 | 0.0055 | 2.6214 | 0.0028 | 0.0096 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0289 | 0.0048 | 0.0063 | 0.0048 | 0.0048 | 1.4430 | 0.0018 | 0.0089 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0297 | -0.0036 | 0.0121 | -0.0036 | -0.0036 | 7.1930 | 0.0057 | 0.0085 |
| 15 | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0240 | 0.0045 | 0.0068 | 0.0045 | 0.0045 | 1.0958 | 0.0017 | 0.0084 |
| 16 | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0211 | 0.0044 | 0.0062 | 0.0044 | 0.0044 | 0.9914 | 0.0013 | 0.0082 |
| 17 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0338 | 0.0031 | 0.0136 | 0.0031 | 0.0031 | 10.4702 | 0.0098 | 0.0081 |
| 18 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-charged_hadron | 0.0312 | -0.0043 | 0.0046 | -0.0043 | -0.0043 | 1.0007 | 0.0016 | 0.0076 |
| 19 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0306 | -0.0029 | 0.0119 | -0.0029 | -0.0029 | 4.4566 | 0.0075 | 0.0073 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0203 | -0.0033 | 0.0094 | -0.0033 | -0.0033 | 1.6673 | 0.0016 | 0.0073 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0201 | 0.0037 | 0.0063 | 0.0037 | 0.0037 | 1.7697 | 0.0021 | 0.0071 |
| 22 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0159 | -0.0037 | 0.0044 | -0.0037 | -0.0037 | 12.6960 | 0.0172 | 0.0067 |
| 23 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0310 | 0.0038 | 0.0038 | 0.0038 | 0.0038 | 19.5529 | 0.0319 | 0.0067 |
| 24 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0232 | 0.0033 | 0.0061 | 0.0033 | 0.0033 | 1.0556 | 0.0019 | 0.0064 |
| 25 | mod.cls_blocks.0.attn.h3 | CLS<-muon | 0.0189 | -0.0034 | 0.0035 | -0.0034 | -0.0034 | 16.3094 | 0.0239 | 0.0060 |
| 26 | mod.cls_blocks.0.attn.h3 | CLS<-neutral_hadron | 0.0277 | -0.0032 | 0.0043 | -0.0032 | -0.0032 | 4.1181 | 0.0049 | 0.0059 |
| 27 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0155 | 0.0032 | 0.0039 | 0.0032 | 0.0032 | 26.1511 | 0.0294 | 0.0058 |
| 28 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0242 | -0.0033 | 0.0033 | -0.0033 | -0.0033 | 14.8867 | 0.0242 | 0.0057 |
| 29 | mod.cls_blocks.1.attn.h5 | neutral_hadron<-muon | 0.0250 | 0.0032 | 0.0038 | 0.0032 | 0.0032 | 2.9994 | 0.0749 | 0.0057 |
| 30 | mod.cls_blocks.1.attn.h0 | CLS<-muon | 0.0691 | 0.0032 | 0.0033 | 0.0032 | 0.0032 | 2.5071 | 0.0436 | 0.0057 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
