# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8688**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0728 | -0.1833 | 0.1833 | -0.1918 | -0.1833 | 152.1469 | 0.0277 | 0.3250 |
| 2 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0632 | -0.1496 | 0.1496 | -0.2698 | -0.1496 | 102.3998 | 0.0359 | 0.3219 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0632 | -0.1496 | 0.1496 | -0.2563 | -0.1496 | 102.3998 | 0.0359 | 0.3151 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0728 | -0.1833 | 0.1833 | -0.1533 | -0.1833 | 152.1469 | 0.0277 | 0.3058 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2374 | 0.0000 | 0.0000 | 0.0000 | 0.1187 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.2183 | 0.0000 | 0.0000 | 0.0000 | 0.1092 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1745 | 0.0000 | 0.0000 | 0.0000 | 0.0872 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1417 | 0.0000 | 0.0000 | 0.0000 | 0.0709 |
| 9 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0247 | 0.0350 | 0.0350 | -0.0311 | 0.0350 | 16.9518 | 0.0264 | 0.0593 |
| 10 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0171 | 0.0031 | 0.0079 | -0.1069 | 0.0031 | 12.8212 | 0.0179 | 0.0585 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0271 | -0.0251 | 0.0347 | -0.0353 | 0.0145 | 9.0273 | 0.0079 | 0.0515 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0203 | 0.0226 | 0.0226 | -0.0435 | 0.0218 | 14.6097 | 0.0221 | 0.0500 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0370 | -0.0165 | 0.0165 | -0.0478 | -0.0165 | 64.1643 | 0.0216 | 0.0445 |
| 14 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0370 | -0.0165 | 0.0165 | -0.0437 | -0.0165 | 64.1643 | 0.0216 | 0.0425 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0340 | -0.0240 | 0.0338 | 0.0043 | 0.0180 | 12.4932 | 0.0056 | 0.0346 |
| 16 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0676 | 0.0000 | 0.0000 | 0.0000 | 0.0338 |
| 17 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0672 | 0.0000 | 0.0000 | 0.0000 | 0.0336 |
| 18 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0637 | 0.0000 | 0.0000 | 0.0000 | 0.0319 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0470 | 0.0000 | 0.0000 | 0.0000 | 0.0235 |
| 20 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0455 | 0.0000 | 0.0000 | 0.0000 | 0.0227 |
| 21 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0360 | 0.0000 | 0.0000 | 0.0000 | 0.0180 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0134 | 0.0116 | 0.0116 | 0.0068 | 0.0116 | 13.4452 | 0.0232 | 0.0179 |
| 23 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0159 | 0.0102 | 0.0102 | 0.0102 | 0.0102 | 12.2677 | 0.0179 | 0.0179 |
| 24 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0344 | 0.0000 | 0.0000 | 0.0000 | 0.0172 |
| 25 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0226 | 0.0057 | 0.0073 | 0.0189 | 0.0014 | 5.7913 | 0.0062 | 0.0169 |
| 26 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0324 | 0.0000 | 0.0000 | 0.0000 | 0.0162 |
| 27 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0000 | 0.0000 | 0.0000 | 0.0299 | 0.0000 | 0.0000 | 0.0000 | 0.0149 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0168 | 0.0085 | 0.0109 | 0.0071 | 0.0017 | 1.1801 | 0.0022 | 0.0148 |
| 29 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0161 | 2.042e-04 | 2.042e-04 | -0.0279 | 2.042e-04 | 1.0345 | 0.0123 | 0.0142 |
| 30 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0163 | 0.0080 | 0.0105 | 0.0047 | 0.0013 | 1.1156 | 0.0020 | 0.0130 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0247 | 0.0350 | 0.0350 | 0.0350 | 0.0350 | 16.9518 | 0.0264 | 0.0612 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0271 | -0.0251 | 0.0347 | -0.0251 | -0.0251 | 9.0273 | 0.0079 | 0.0464 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0340 | -0.0240 | 0.0338 | -0.0240 | -0.0240 | 12.4932 | 0.0056 | 0.0445 |
| 4 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0203 | 0.0226 | 0.0226 | 0.0226 | 0.0226 | 14.6097 | 0.0221 | 0.0396 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0134 | 0.0116 | 0.0116 | 0.0116 | 0.0116 | 13.4452 | 0.0232 | 0.0203 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0159 | 0.0102 | 0.0102 | 0.0102 | 0.0102 | 12.2677 | 0.0179 | 0.0179 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0175 | 0.0093 | 0.0117 | 0.0093 | 0.0093 | 1.2421 | 0.0022 | 0.0169 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0168 | 0.0086 | 0.0110 | 0.0086 | 0.0086 | 1.1590 | 0.0020 | 0.0157 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0247 | 0.0079 | 0.0090 | 0.0079 | 0.0079 | 5.7553 | 0.0062 | 0.0142 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0151 | 0.0070 | 0.0094 | 0.0070 | 0.0070 | 0.9643 | 0.0015 | 0.0128 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0129 | 0.0073 | 0.0073 | 0.0073 | 0.0073 | 12.6443 | 0.0165 | 0.0127 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0220 | -0.0055 | 0.0153 | -0.0055 | -0.0055 | 1.2522 | 0.0013 | 0.0121 |
| 13 | mod.blocks.3.attn.h5 | muon<-muon | 0.2391 | -0.0058 | 0.0080 | -0.0058 | -0.0058 | 2.0347 | 0.0019 | 0.0107 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0162 | 0.0055 | 0.0062 | 0.0055 | 0.0055 | 1.4001 | 0.0016 | 0.0098 |
| 15 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0260 | 0.0049 | 0.0077 | 0.0049 | 0.0049 | 7.1558 | 0.0078 | 0.0093 |
| 16 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0225 | -0.0032 | 0.0155 | -0.0032 | -0.0032 | 5.7371 | 0.0083 | 0.0087 |
| 17 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0155 | 0.0047 | 0.0054 | 0.0047 | 0.0047 | 1.2766 | 0.0015 | 0.0084 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0156 | 0.0043 | 0.0071 | 0.0043 | 0.0043 | 0.7836 | 0.0013 | 0.0082 |
| 19 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0202 | -0.0033 | 0.0119 | -0.0033 | -0.0033 | 1.1231 | 0.0012 | 0.0079 |
| 20 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0211 | 0.0037 | 0.0096 | 0.0037 | 0.0037 | 4.7123 | 0.0084 | 0.0079 |
| 21 | mod.cls_blocks.0.attn.h5 | CLS<-muon | 0.0403 | -0.0043 | 0.0043 | -0.0043 | -0.0043 | 9.2874 | 0.0079 | 0.0075 |
| 22 | mod.cls_blocks.0.attn.h5 | neutral_hadron<-muon | 0.0403 | -0.0043 | 0.0043 | -0.0043 | -0.0043 | 9.2874 | 0.0079 | 0.0075 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0171 | 0.0031 | 0.0079 | 0.0031 | 0.0031 | 12.8212 | 0.0179 | 0.0066 |
| 24 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0171 | 0.0031 | 0.0079 | 0.0031 | 0.0031 | 12.8212 | 0.0179 | 0.0066 |
| 25 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0283 | -0.0028 | 0.0071 | -0.0028 | -0.0028 | 4.5654 | 0.0072 | 0.0060 |
| 26 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0215 | -6.933e-04 | 0.0189 | -6.933e-04 | -6.933e-04 | 1.0890 | 0.0017 | 0.0058 |
| 27 | mod.cls_blocks.0.attn.h3 | charged_hadron<-neutral_hadron | 0.0297 | -0.0031 | 0.0037 | -0.0031 | -0.0031 | 3.2175 | 0.0033 | 0.0056 |
| 28 | mod.blocks.4.attn.h5 | muon<-muon | 0.3367 | -0.0025 | 0.0070 | -0.0025 | -0.0025 | 1.4769 | 0.0020 | 0.0055 |
| 29 | mod.blocks.2.attn.h3 | muon<-muon | 0.1465 | 0.0029 | 0.0046 | 0.0029 | 0.0029 | 2.0617 | 0.0028 | 0.0055 |
| 30 | mod.blocks.0.attn.h5 | muon<-muon | 0.4684 | 0.0031 | 0.0031 | 0.0031 | 0.0031 | 3.1741 | 8.686e-04 | 0.0055 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
