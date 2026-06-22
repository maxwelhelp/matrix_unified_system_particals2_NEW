# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9024**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0753 | 0.2539 | 0.2539 | 0.4906 | 0.2539 | 152.1469 | 0.0362 | 0.5627 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0834 | 0.0909 | 0.1630 | 0.2914 | 0.0909 | 152.1469 | 0.0327 | 0.2774 |
| 3 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0861 | -0.1378 | 0.1378 | -0.1079 | -0.1378 | 102.3998 | 0.0284 | 0.2262 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0659 | -0.0992 | 0.0992 | -0.1461 | -0.0992 | 102.3998 | 0.0263 | 0.1970 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0958 | -0.1002 | 0.1002 | 0.1328 | -0.1002 | 152.1469 | 0.0296 | 0.1916 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0874 | -0.0439 | 0.0439 | 0.1345 | -0.0439 | 152.1469 | 0.0289 | 0.1222 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0694 | -0.0506 | 0.0743 | -0.0729 | -0.0506 | 102.3998 | 0.0257 | 0.1056 |
| 8 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0118 | -0.0012 | 0.0012 | -0.2032 | -0.0012 | 13.9799 | 0.0223 | 0.1030 |
| 9 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2001 | 0.0000 | 0.0000 | 0.0000 | 0.1000 |
| 10 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0118 | -0.0012 | 0.0012 | -0.1321 | -0.0023 | 13.9799 | 0.0223 | 0.0675 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0627 | 0.0172 | 0.0301 | -0.0440 | 0.0172 | 102.3998 | 0.0240 | 0.0467 |
| 12 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0551 | -0.0182 | 0.0229 | -0.0402 | -0.0186 | 33.3590 | 0.0328 | 0.0440 |
| 13 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0551 | -0.0182 | 0.0229 | -0.0402 | -0.0197 | 33.3590 | 0.0328 | 0.0440 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0374 | 0.0037 | 0.0062 | -0.0752 | 0.0010 | 23.7664 | 0.0222 | 0.0428 |
| 15 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0374 | 0.0037 | 0.0062 | -0.0752 | 0.0018 | 23.7664 | 0.0222 | 0.0428 |
| 16 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0463 | -0.0116 | 0.0116 | -0.0379 | -0.0116 | 64.1643 | 0.0179 | 0.0334 |
| 17 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0217 | 0.0139 | 0.0139 | 0.0267 | 0.0139 | 66.5560 | 0.0351 | 0.0307 |
| 18 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0602 | 0.0000 | 0.0000 | 0.0000 | 0.0301 |
| 19 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0599 | 0.0000 | 0.0000 | 0.0000 | 0.0300 |
| 20 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0247 | -0.0098 | 0.0098 | -0.0345 | -0.0108 | 24.8299 | 0.0391 | 0.0295 |
| 21 | mod.cls_blocks.1.attn.h3 | charged_hadron<-muon | 0.0061 | 2.361e-05 | 2.361e-05 | 0.0562 | 2.361e-05 | 1.9683 | 0.0226 | 0.0281 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0248 | 0.0132 | 0.0132 | 0.0203 | 0.0132 | 66.5560 | 0.0372 | 0.0267 |
| 23 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0283 | 0.0128 | 0.0128 | 0.0205 | 0.0128 | 66.5560 | 0.0406 | 0.0263 |
| 24 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0276 | 0.0122 | 0.0122 | 0.0182 | 0.0122 | 66.5560 | 0.0380 | 0.0244 |
| 25 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0448 | 0.0069 | 0.0081 | -0.0279 | 0.0069 | 64.1643 | 0.0171 | 0.0229 |
| 26 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0286 | -0.0135 | 0.0217 | 0.0066 | -0.0207 | 7.6198 | 0.0076 | 0.0222 |
| 27 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0568 | -0.0053 | 0.0053 | -0.0284 | -0.0053 | 64.1643 | 0.0180 | 0.0208 |
| 28 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0386 | 0.0000 | 0.0000 | 0.0000 | 0.0193 |
| 29 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0185 | -0.0066 | 0.0093 | -0.0175 | -0.0039 | 4.9476 | 0.0052 | 0.0176 |
| 30 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0482 | -7.570e-04 | 0.0082 | -0.0251 | -7.570e-04 | 64.1643 | 0.0175 | 0.0154 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0341 | 0.0207 | 0.0577 | 0.0207 | 0.0207 | 11.7951 | 0.0076 | 0.0455 |
| 2 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0247 | -0.0098 | 0.0098 | -0.0098 | -0.0098 | 24.8299 | 0.0391 | 0.0171 |
| 3 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0247 | -0.0098 | 0.0098 | -0.0098 | -0.0098 | 24.8299 | 0.0391 | 0.0171 |
| 4 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0678 | 0.0097 | 0.0100 | 0.0097 | 0.0097 | 3.8996 | 0.0552 | 0.0171 |
| 5 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0678 | 0.0097 | 0.0100 | 0.0097 | 0.0097 | 3.8996 | 0.0552 | 0.0171 |
| 6 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0351 | 0.0075 | 0.0075 | 0.0075 | 0.0075 | 9.5610 | 0.0133 | 0.0132 |
| 7 | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0360 | -0.0071 | 0.0071 | -0.0071 | -0.0071 | 26.4892 | 0.0200 | 0.0124 |
| 8 | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0360 | -0.0071 | 0.0071 | -0.0071 | -0.0071 | 26.4892 | 0.0200 | 0.0124 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0270 | 0.0045 | 0.0142 | 0.0045 | 0.0045 | 7.3655 | 0.0063 | 0.0103 |
| 10 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0191 | 0.0052 | 0.0077 | 0.0052 | 0.0052 | 22.3699 | 0.0328 | 0.0097 |
| 11 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0191 | 0.0052 | 0.0077 | 0.0052 | 0.0052 | 22.3699 | 0.0328 | 0.0097 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0279 | 0.0052 | 0.0072 | 0.0052 | 0.0052 | 26.8278 | 0.0252 | 0.0096 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0279 | 0.0052 | 0.0072 | 0.0052 | 0.0052 | 26.8278 | 0.0252 | 0.0096 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0293 | -0.0041 | 0.0129 | -0.0041 | -0.0041 | 8.9105 | 0.0052 | 0.0093 |
| 15 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0280 | 0.0027 | 0.0082 | 0.0027 | 0.0027 | 7.6913 | 0.0078 | 0.0060 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0141 | -0.0028 | 0.0055 | -0.0028 | -0.0028 | 0.9156 | 0.0013 | 0.0056 |
| 17 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0166 | 0.0025 | 0.0035 | 0.0025 | 0.0025 | 1.1349 | 0.0012 | 0.0047 |
| 18 | mod.cls_blocks.0.attn.h5 | CLS<-muon | 0.0291 | -0.0026 | 0.0026 | -0.0026 | -0.0026 | 15.0309 | 0.0151 | 0.0046 |
| 19 | mod.cls_blocks.0.attn.h5 | charged_hadron<-muon | 0.0291 | -0.0026 | 0.0026 | -0.0026 | -0.0026 | 15.0309 | 0.0151 | 0.0046 |
| 20 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0331 | 0.0017 | 0.0077 | 0.0017 | 0.0017 | 6.4105 | 0.0082 | 0.0045 |
| 21 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0177 | 0.0024 | 0.0031 | 0.0024 | 0.0024 | 0.9267 | 9.563e-04 | 0.0043 |
| 22 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0238 | 0.0021 | 0.0045 | 0.0021 | 0.0021 | 5.2289 | 0.0049 | 0.0043 |
| 23 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0245 | 0.0022 | 0.0038 | 0.0022 | 0.0022 | 20.1695 | 0.0170 | 0.0043 |
| 24 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0245 | 0.0022 | 0.0038 | 0.0022 | 0.0022 | 20.1695 | 0.0170 | 0.0043 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0287 | 0.0023 | 0.0027 | 0.0023 | 0.0023 | 9.9745 | 0.0092 | 0.0041 |
| 26 | mod.cls_blocks.0.attn.h3 | CLS<-electron | 0.0141 | 0.0019 | 0.0034 | 0.0019 | 0.0019 | 21.7177 | 0.0202 | 0.0038 |
| 27 | mod.cls_blocks.0.attn.h3 | charged_hadron<-electron | 0.0141 | 0.0019 | 0.0034 | 0.0019 | 0.0019 | 21.7177 | 0.0202 | 0.0038 |
| 28 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-photon | 0.0160 | -0.0019 | 0.0035 | -0.0019 | -0.0019 | 0.7807 | 0.0013 | 0.0038 |
| 29 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0097 | -0.0021 | 0.0021 | -0.0021 | -0.0021 | 25.3501 | 0.0266 | 0.0037 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0097 | -0.0021 | 0.0021 | -0.0021 | -0.0021 | 25.3501 | 0.0266 | 0.0037 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
