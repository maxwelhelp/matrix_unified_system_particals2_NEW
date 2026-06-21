# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **96**
- events_per_group: **24**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9024**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 1.0850 | 0.0000 | 0.0000 | 0.0000 | 0.5425 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 1.0817 | 0.0000 | 0.0000 | 0.0000 | 0.5408 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.9806 | 0.0000 | 0.0000 | 0.0000 | 0.4903 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.9166 | 0.0000 | 0.0000 | 0.0000 | 0.4583 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.6789 | 0.0000 | 0.0000 | 0.0000 | 0.3394 |
| 6 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.4178 | 0.0000 | 0.0000 | 0.0000 | 0.2089 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0717 | 0.0989 | 0.1834 | 0.0974 | 0.0899 | 37.5838 | 0.0146 | 0.1934 |
| 8 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | 0.3780 | 0.0000 | 0.0000 | 0.0000 | 0.1890 |
| 9 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.3006 | 0.0000 | 0.0000 | 0.0000 | 0.1503 |
| 10 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2459 | 0.0000 | 0.0000 | 0.0000 | 0.1229 |
| 11 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2255 | 0.0000 | 0.0000 | 0.0000 | 0.1128 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1811 | 0.0000 | 0.0000 | 0.0000 | 0.0905 |
| 13 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0000 | 0.0000 | 0.0000 | 0.1593 | 0.0000 | 0.0000 | 0.0000 | 0.0796 |
| 14 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1227 | 0.0000 | 0.0000 | 0.0000 | 0.0613 |
| 15 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0638 | 0.0259 | 0.0395 | 0.0250 | 0.0224 | 28.4037 | 0.0086 | 0.0483 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0410 | -0.0263 | 0.0329 | -0.0154 | -8.426e-05 | 8.1666 | 0.0111 | 0.0422 |
| 17 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0821 | 0.0000 | 0.0000 | 0.0000 | 0.0411 |
| 18 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0372 | 0.0267 | 0.0445 | 0.0043 | -0.0019 | 3.4881 | 0.0029 | 0.0400 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0365 | 0.0190 | 0.0433 | 0.0177 | 0.0037 | 2.2216 | 0.0026 | 0.0387 |
| 20 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0613 | 6.354e-04 | 6.354e-04 | -0.0658 | 5.890e-04 | 13.8143 | 0.0107 | 0.0337 |
| 21 | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0623 | 0.0000 | 0.0000 | 0.0000 | 0.0312 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0241 | -0.0077 | 0.0133 | -0.0375 | -3.026e-04 | 1.6646 | 0.0028 | 0.0297 |
| 23 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0459 | 0.0079 | 0.0603 | 0.0105 | 0.0141 | 15.2630 | 0.0133 | 0.0282 |
| 24 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0353 | 0.0151 | 0.0254 | 0.0132 | 0.0104 | 19.5674 | 0.0148 | 0.0280 |
| 25 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0539 | 0.0000 | 0.0000 | 0.0000 | 0.0269 |
| 26 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0528 | 0.0000 | 0.0000 | 0.0000 | 0.0264 |
| 27 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0350 | -0.0046 | 0.0133 | -0.0366 | 0.0068 | 2.0105 | 0.0024 | 0.0263 |
| 28 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0525 | 0.0000 | 0.0000 | 0.0000 | 0.0263 |
| 29 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0357 | -0.0091 | 0.0159 | -0.0262 | -0.0055 | 1.6981 | 0.0026 | 0.0262 |
| 30 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0497 | 0.0000 | 0.0000 | 0.0000 | 0.0248 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0717 | 0.0989 | 0.1834 | 0.0989 | 0.0989 | 37.5838 | 0.0146 | 0.1942 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0372 | 0.0267 | 0.0445 | 0.0267 | 0.0267 | 3.4881 | 0.0029 | 0.0512 |
| 3 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0638 | 0.0259 | 0.0395 | 0.0259 | 0.0259 | 28.4037 | 0.0086 | 0.0487 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0410 | -0.0263 | 0.0329 | -0.0263 | -0.0263 | 8.1666 | 0.0111 | 0.0477 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0365 | 0.0190 | 0.0433 | 0.0190 | 0.0190 | 2.2216 | 0.0026 | 0.0394 |
| 6 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0353 | 0.0151 | 0.0254 | 0.0151 | 0.0151 | 19.5674 | 0.0148 | 0.0290 |
| 7 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0459 | 0.0079 | 0.0603 | 0.0079 | 0.0079 | 15.2630 | 0.0133 | 0.0269 |
| 8 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0687 | 0.0141 | 0.0141 | 0.0141 | 0.0141 | 30.2158 | 0.0350 | 0.0247 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0371 | -0.0118 | 0.0211 | -0.0118 | -0.0118 | 9.5776 | 0.0143 | 0.0229 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0332 | -0.0118 | 0.0118 | -0.0118 | -0.0118 | 30.1302 | 0.0163 | 0.0206 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0332 | -0.0118 | 0.0118 | -0.0118 | -0.0118 | 30.1302 | 0.0163 | 0.0206 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0357 | -0.0091 | 0.0159 | -0.0091 | -0.0091 | 1.6981 | 0.0026 | 0.0177 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0359 | 0.0059 | 0.0287 | 0.0059 | 0.0059 | 2.0398 | 0.0025 | 0.0160 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0241 | -0.0077 | 0.0133 | -0.0077 | -0.0077 | 1.6646 | 0.0028 | 0.0148 |
| 15 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0514 | 0.0082 | 0.0082 | 0.0082 | 0.0082 | 20.0791 | 0.0196 | 0.0143 |
| 16 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.0336 | -0.0080 | 0.0083 | -0.0080 | -0.0080 | 24.1314 | 0.0135 | 0.0141 |
| 17 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0327 | -0.0077 | 0.0077 | -0.0077 | -0.0077 | 22.9099 | 0.0310 | 0.0135 |
| 18 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0541 | -0.0051 | 0.0193 | -0.0051 | -0.0051 | 8.3158 | 0.0117 | 0.0124 |
| 19 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0452 | 0.0050 | 0.0162 | 0.0050 | 0.0050 | 12.9535 | 0.0076 | 0.0116 |
| 20 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0370 | 0.0058 | 0.0102 | 0.0058 | 0.0058 | 2.9167 | 0.0017 | 0.0113 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0396 | 0.0059 | 0.0097 | 0.0059 | 0.0059 | 25.6271 | 0.0139 | 0.0112 |
| 22 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0470 | 0.0060 | 0.0087 | 0.0060 | 0.0060 | 17.3382 | 0.0051 | 0.0112 |
| 23 | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0415 | -0.0060 | 0.0061 | -0.0060 | -0.0060 | 16.4540 | 0.0143 | 0.0106 |
| 24 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0350 | -0.0046 | 0.0133 | -0.0046 | -0.0046 | 2.0105 | 0.0024 | 0.0103 |
| 25 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0342 | 0.0046 | 0.0118 | 0.0046 | 0.0046 | 1.8817 | 0.0014 | 0.0098 |
| 26 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0829 | -0.0055 | 0.0055 | -0.0055 | -0.0055 | 20.3240 | 0.0124 | 0.0096 |
| 27 | mod.blocks.5.attn.h4 | muon<-neutral_hadron | 0.2870 | 0.0055 | 0.0055 | 0.0055 | 0.0055 | 1.7418 | 0.0017 | 0.0096 |
| 28 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0442 | 0.0053 | 0.0053 | 0.0053 | 0.0053 | 19.8150 | 0.0126 | 0.0092 |
| 29 | mod.blocks.5.attn.h7 | electron<-muon | 0.7233 | 0.0051 | 0.0051 | 0.0051 | 0.0051 | 9.6670 | 0.0014 | 0.0089 |
| 30 | mod.cls_blocks.0.attn.h2 | charged_hadron<-electron | 0.0329 | -0.0049 | 0.0049 | -0.0049 | -0.0049 | 10.0458 | 0.0154 | 0.0085 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
