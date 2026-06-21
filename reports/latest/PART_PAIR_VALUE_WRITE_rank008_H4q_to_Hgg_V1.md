# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **7792**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0701 | -0.1752 | 0.1752 | -0.2008 | -0.1752 | 152.1469 | 0.0300 | 0.3194 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0649 | -0.1365 | 0.1365 | -0.1906 | -0.1365 | 152.1469 | 0.0279 | 0.2659 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0635 | -0.0637 | 0.0637 | -0.0563 | -0.0637 | 102.3998 | 0.0235 | 0.1078 |
| 4 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0576 | -0.0528 | 0.0528 | -0.0617 | -0.0528 | 102.3998 | 0.0229 | 0.0969 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0493 | -0.0204 | 0.0204 | -0.1398 | -0.0204 | 152.1469 | 0.0217 | 0.0954 |
| 6 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.1136 | 0.0352 | 0.0352 | 0.0352 | 0.0352 | 32.5287 | 0.0213 | 0.0616 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0399 | -0.0202 | 0.0202 | -0.0660 | -0.0202 | 102.3998 | 0.0213 | 0.0583 |
| 8 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0397 | -0.0131 | 0.0131 | -0.0286 | -0.0131 | 64.1643 | 0.0219 | 0.0307 |
| 9 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0371 | -0.0109 | 0.0109 | -0.0269 | -0.0109 | 64.1643 | 0.0209 | 0.0271 |
| 10 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | -0.0529 | 0.0000 | 0.0000 | 0.0000 | 0.0264 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0228 | -0.0127 | 0.0173 | -0.0107 | 0.0291 | 5.8876 | 0.0039 | 0.0224 |
| 12 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0670 | 0.0127 | 0.0127 | 0.0126 | 0.0141 | 15.2434 | 0.0122 | 0.0222 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0832 | 0.0084 | 0.0084 | 0.0175 | 0.0084 | 19.4319 | 0.0207 | 0.0192 |
| 14 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0218 | -0.0076 | 0.0076 | -0.0161 | -0.0076 | 66.5560 | 0.0278 | 0.0176 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0492 | 0.0098 | 0.0098 | 0.0105 | 0.0098 | 27.6846 | 0.0318 | 0.0174 |
| 16 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0294 | -0.0043 | 0.0043 | -0.0223 | -0.0043 | 64.1643 | 0.0177 | 0.0166 |
| 17 | mod.blocks.0.attn.h3 | electron<-electron | 0.2307 | 0.0087 | 0.0116 | 0.0085 | 0.0088 | 5.1302 | 0.0015 | 0.0159 |
| 18 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0338 | -0.0071 | 0.0071 | -0.0120 | -0.0071 | 42.4997 | 0.0150 | 0.0149 |
| 19 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0832 | 0.0084 | 0.0084 | 0.0084 | 0.0084 | 19.4319 | 0.0207 | 0.0146 |
| 20 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0308 | -0.0062 | 0.0062 | -0.0121 | -0.0062 | 42.4997 | 0.0144 | 0.0138 |
| 21 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0214 | -0.0056 | 0.0058 | -0.0128 | -0.0056 | 66.5560 | 0.0267 | 0.0134 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0486 | -0.0050 | 0.0050 | 0.0127 | -0.0050 | 32.3614 | 0.0261 | 0.0126 |
| 23 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0694 | 0.0042 | 0.0042 | 0.0144 | 0.0042 | 5.7381 | 0.0116 | 0.0124 |
| 24 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0641 | 0.0069 | 0.0069 | 0.0075 | 0.0069 | 27.2772 | 0.0263 | 0.0124 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0676 | 0.0051 | 0.0051 | 0.0105 | 0.0049 | 12.9178 | 0.0165 | 0.0116 |
| 26 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0234 | 0.0049 | 0.0049 | 0.0084 | 0.0089 | 15.7191 | 0.0215 | 0.0104 |
| 27 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.8221 | -0.0019 | 0.0019 | 0.0151 | -0.0019 | 3.8689 | 0.0215 | 0.0100 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0191 | 0.0056 | 0.0056 | -0.0056 | 0.0056 | 11.6635 | 0.0116 | 0.0099 |
| 29 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0218 | -0.0035 | 0.0035 | -0.0109 | -0.0035 | 42.4997 | 0.0125 | 0.0099 |
| 30 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0606 | 0.0017 | 0.0017 | 0.0138 | 0.0017 | 13.7118 | 0.0143 | 0.0090 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.1136 | 0.0352 | 0.0352 | 0.0352 | 0.0352 | 32.5287 | 0.0213 | 0.0617 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0244 | -0.0134 | 0.0179 | -0.0134 | -0.0134 | 6.1913 | 0.0039 | 0.0245 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0263 | 0.0124 | 0.0124 | 0.0124 | 0.0124 | 32.2804 | 0.0266 | 0.0218 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0263 | 0.0124 | 0.0124 | 0.0124 | 0.0124 | 32.2804 | 0.0266 | 0.0218 |
| 5 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0467 | 0.0113 | 0.0122 | 0.0113 | 0.0113 | 15.1552 | 0.0122 | 0.0200 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0492 | 0.0098 | 0.0098 | 0.0098 | 0.0098 | 27.6846 | 0.0318 | 0.0171 |
| 7 | mod.blocks.0.attn.h3 | electron<-electron | 0.2307 | 0.0087 | 0.0116 | 0.0087 | 0.0087 | 5.1302 | 0.0015 | 0.0160 |
| 8 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0278 | 0.0085 | 0.0085 | 0.0085 | 0.0085 | 16.8330 | 0.0116 | 0.0150 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0641 | 0.0069 | 0.0069 | 0.0069 | 0.0069 | 27.2772 | 0.0263 | 0.0121 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0226 | -0.0060 | 0.0091 | -0.0060 | -0.0060 | 5.2548 | 0.0035 | 0.0112 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0260 | 0.0052 | 0.0061 | 0.0052 | 0.0052 | 18.4278 | 0.0159 | 0.0094 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0201 | 0.0045 | 0.0071 | 0.0045 | 0.0045 | 3.9923 | 0.0045 | 0.0085 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0241 | 0.0047 | 0.0047 | 0.0047 | 0.0047 | 16.0580 | 0.0215 | 0.0082 |
| 14 | mod.blocks.2.attn.h3 | muon<-muon | 0.0889 | 0.0047 | 0.0047 | 0.0047 | 0.0047 | 8.7413 | 0.0096 | 0.0081 |
| 15 | mod.cls_blocks.1.attn.h5 | neutral_hadron<-electron | 0.0567 | 0.0045 | 0.0045 | 0.0045 | 0.0045 | 2.7212 | 0.1075 | 0.0078 |
| 16 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0219 | -0.0033 | 0.0109 | -0.0033 | -0.0033 | 4.8342 | 0.0042 | 0.0076 |
| 17 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0266 | -0.0041 | 0.0054 | -0.0041 | -0.0041 | 3.5725 | 0.0043 | 0.0075 |
| 18 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0128 | 0.0035 | 0.0045 | 0.0035 | 0.0035 | 1.0236 | 0.0013 | 0.0063 |
| 19 | mod.cls_blocks.1.attn.h5 | photon<-neutral_hadron | 0.0404 | -0.0035 | 0.0037 | -0.0035 | -0.0035 | 0.4209 | 0.0077 | 0.0061 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0161 | -0.0025 | 0.0090 | -0.0025 | -0.0025 | 1.4790 | 0.0012 | 0.0060 |
| 21 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0185 | 0.0031 | 0.0048 | 0.0031 | 0.0031 | 0.9308 | 9.449e-04 | 0.0058 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0193 | -0.0019 | 0.0116 | -0.0019 | -0.0019 | 1.0714 | 0.0011 | 0.0058 |
| 23 | mod.cls_blocks.0.attn.h3 | photon<-neutral_hadron | 0.0225 | -0.0030 | 0.0031 | -0.0030 | -0.0030 | 2.8129 | 0.0032 | 0.0053 |
| 24 | mod.blocks.0.attn.h4 | electron<-electron | 0.0698 | 0.0028 | 0.0041 | 0.0028 | 0.0028 | 4.8268 | 0.0018 | 0.0052 |
| 25 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0204 | 0.0029 | 0.0029 | 0.0029 | 0.0029 | 22.3428 | 0.0261 | 0.0051 |
| 26 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0204 | 0.0029 | 0.0029 | 0.0029 | 0.0029 | 22.3428 | 0.0261 | 0.0051 |
| 27 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0141 | 0.0028 | 0.0034 | 0.0028 | 0.0028 | 0.9771 | 0.0011 | 0.0050 |
| 28 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0233 | -0.0025 | 0.0045 | -0.0025 | -0.0025 | 3.7799 | 0.0041 | 0.0048 |
| 29 | mod.cls_blocks.0.attn.h3 | charged_hadron<-neutral_hadron | 0.0215 | -0.0027 | 0.0032 | -0.0027 | -0.0027 | 2.7550 | 0.0035 | 0.0048 |
| 30 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0131 | 0.0026 | 0.0033 | 0.0026 | 0.0026 | 0.9016 | 9.145e-04 | 0.0048 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
