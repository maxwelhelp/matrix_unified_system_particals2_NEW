# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8352**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0980 | -0.7573 | 0.7573 | -1.1384 | -0.7573 | 152.1469 | 0.0541 | 1.5159 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1125 | -0.7030 | 0.7030 | -1.0860 | -0.7030 | 152.1469 | 0.0472 | 1.4218 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1270 | -0.6487 | 0.6487 | -0.7810 | -0.6487 | 152.1469 | 0.0403 | 1.2014 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0806 | -0.1906 | 0.1906 | -0.2801 | -0.1906 | 102.3998 | 0.0311 | 0.3782 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0946 | -0.1589 | 0.1589 | -0.2462 | -0.1589 | 102.3998 | 0.0264 | 0.3218 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.5753 | 0.0000 | 0.0000 | 0.0000 | 0.2876 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0463 | -0.1423 | 0.1807 | -0.1256 | -0.0077 | 11.3503 | 0.0147 | 0.2502 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.1086 | -0.1273 | 0.1273 | -0.1561 | -0.1273 | 102.3998 | 0.0218 | 0.2372 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0328 | -0.0653 | 0.0880 | -0.0518 | -0.0107 | 8.4898 | 0.0145 | 0.1132 |
| 10 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0972 | 0.0613 | 0.0613 | 0.0613 | 0.0613 | 25.4470 | 0.0395 | 0.1072 |
| 11 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0567 | -0.0438 | 0.0438 | -0.0651 | -0.0438 | 64.1643 | 0.0248 | 0.0873 |
| 12 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0268 | -0.0370 | 0.0370 | -0.0618 | -0.0370 | 66.5560 | 0.0390 | 0.0772 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0638 | -0.0360 | 0.0360 | -0.0593 | -0.0360 | 64.1643 | 0.0181 | 0.0746 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0308 | -0.0348 | 0.0348 | -0.0602 | -0.0348 | 66.5560 | 0.0380 | 0.0736 |
| 15 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.1262 | 0.0000 | 0.0000 | 0.0000 | 0.0631 |
| 16 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0349 | -0.0326 | 0.0326 | -0.0437 | -0.0326 | 66.5560 | 0.0370 | 0.0627 |
| 17 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0876 | 0.0348 | 0.0348 | 0.0348 | 0.0658 | 19.4563 | 0.0311 | 0.0608 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0385 | -0.0342 | 0.0398 | -0.0331 | 0.0022 | 8.6551 | 0.0066 | 0.0607 |
| 19 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0709 | -0.0281 | 0.0281 | -0.0435 | -0.0281 | 64.1643 | 0.0114 | 0.0569 |
| 20 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0572 | -0.0266 | 0.0266 | -0.0266 | -0.0266 | 21.2356 | 0.0398 | 0.0466 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0309 | 0.0235 | 0.0318 | 0.0247 | 0.0142 | 1.6229 | 0.0043 | 0.0438 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0210 | -0.0225 | 0.0269 | -0.0114 | 0.0551 | 1.5198 | 0.0020 | 0.0349 |
| 23 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0191 | 0.0167 | 0.0208 | 0.0247 | 0.0051 | 1.4696 | 0.0040 | 0.0343 |
| 24 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0248 | 0.0185 | 0.0248 | 0.0179 | 0.0042 | 1.9174 | 0.0052 | 0.0336 |
| 25 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0572 | 0.0185 | 0.0185 | 0.0185 | 0.0185 | 20.1788 | 0.0230 | 0.0324 |
| 26 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0214 | 0.0144 | 0.0228 | 0.0223 | 0.0310 | 1.6406 | 0.0043 | 0.0313 |
| 27 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0434 | -0.0168 | 0.0168 | -0.0168 | 0.5235 | 19.4340 | 0.0372 | 0.0295 |
| 28 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0186 | -0.0026 | 0.0071 | -0.0455 | -0.0026 | 14.3395 | 0.0332 | 0.0271 |
| 29 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0276 | -0.0135 | 0.0479 | -0.0027 | 0.0158 | 1.4366 | 0.0031 | 0.0268 |
| 30 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0291 | -0.0147 | 0.0197 | -0.0134 | 0.0014 | 6.9390 | 0.0074 | 0.0263 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0490 | -0.1879 | 0.2182 | -0.1879 | -0.1879 | 13.1345 | 0.0147 | 0.3365 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0342 | -0.0838 | 0.1038 | -0.0838 | -0.0838 | 9.0891 | 0.0145 | 0.1517 |
| 3 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0972 | 0.0613 | 0.0613 | 0.0613 | 0.0613 | 25.4470 | 0.0395 | 0.1072 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0453 | -0.0430 | 0.0483 | -0.0430 | -0.0430 | 10.0283 | 0.0066 | 0.0765 |
| 5 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0876 | 0.0348 | 0.0348 | 0.0348 | 0.0348 | 19.4563 | 0.0311 | 0.0608 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0277 | -0.0241 | 0.0570 | -0.0241 | -0.0241 | 1.5043 | 0.0031 | 0.0503 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0572 | -0.0266 | 0.0266 | -0.0266 | -0.0266 | 21.2356 | 0.0398 | 0.0466 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0313 | 0.0228 | 0.0323 | 0.0228 | 0.0228 | 1.6395 | 0.0043 | 0.0423 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0210 | -0.0225 | 0.0269 | -0.0225 | -0.0225 | 1.5198 | 0.0020 | 0.0404 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0259 | 0.0201 | 0.0262 | 0.0201 | 0.0201 | 2.0088 | 0.0052 | 0.0367 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0333 | -0.0184 | 0.0238 | -0.0184 | -0.0184 | 7.6129 | 0.0074 | 0.0335 |
| 12 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0572 | 0.0185 | 0.0185 | 0.0185 | 0.0185 | 20.1788 | 0.0230 | 0.0324 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0201 | 0.0169 | 0.0212 | 0.0169 | 0.0169 | 1.5140 | 0.0040 | 0.0307 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0434 | -0.0168 | 0.0168 | -0.0168 | -0.0168 | 19.4340 | 0.0372 | 0.0295 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0224 | 0.0151 | 0.0235 | 0.0151 | 0.0151 | 1.6992 | 0.0043 | 0.0286 |
| 16 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0485 | -0.0149 | 0.0149 | -0.0149 | -0.0149 | 33.3922 | 0.0523 | 0.0260 |
| 17 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0353 | -0.0132 | 0.0132 | -0.0132 | -0.0132 | 31.0286 | 0.0550 | 0.0232 |
| 18 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0220 | -0.0116 | 0.0116 | -0.0116 | -0.0116 | 28.6649 | 0.0577 | 0.0203 |
| 19 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0291 | -0.0056 | 0.0450 | -0.0056 | -0.0056 | 1.5377 | 0.0034 | 0.0196 |
| 20 | mod.blocks.0.attn.h6 | muon<-electron | 0.1521 | 0.0109 | 0.0109 | 0.0109 | 0.0109 | 8.7729 | 0.0051 | 0.0191 |
| 21 | mod.cls_blocks.0.attn.h1 | photon<-photon | 0.0149 | 0.0100 | 0.0144 | 0.0100 | 0.0100 | 1.3344 | 0.0034 | 0.0186 |
| 22 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0419 | 0.0101 | 0.0101 | 0.0101 | 0.0101 | 15.2236 | 0.0198 | 0.0176 |
| 23 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0305 | -0.0082 | 0.0146 | -0.0082 | -0.0082 | 7.5509 | 0.0099 | 0.0159 |
| 24 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0371 | -0.0090 | 0.0090 | -0.0090 | -0.0090 | 26.5675 | 0.0375 | 0.0157 |
| 25 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0355 | 0.0077 | 0.0148 | 0.0077 | 0.0077 | 1.5073 | 0.0029 | 0.0152 |
| 26 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0263 | -0.0072 | 0.0147 | -0.0072 | -0.0072 | 1.2889 | 0.0016 | 0.0145 |
| 27 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0780 | 0.0083 | 0.0083 | 0.0083 | 0.0083 | 13.4657 | 0.0226 | 0.0144 |
| 28 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0296 | -0.0082 | 0.0082 | -0.0082 | -0.0082 | 24.0854 | 0.0360 | 0.0143 |
| 29 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0359 | -0.0078 | 0.0097 | -0.0078 | -0.0078 | 6.8263 | 0.0039 | 0.0142 |
| 30 | mod.blocks.6.attn.h1 | electron<-muon | 0.2340 | -0.0076 | 0.0076 | -0.0076 | -0.0076 | 6.0757 | 0.0029 | 0.0133 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
