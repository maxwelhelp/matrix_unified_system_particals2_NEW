# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **7248**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0705 | 0.1364 | 0.1364 | 0.3367 | 0.1364 | 152.1469 | 0.0277 | 0.3388 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0714 | 0.1111 | 0.1111 | 0.3122 | 0.1111 | 152.1469 | 0.0265 | 0.2950 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0723 | 0.0859 | 0.0859 | 0.2759 | 0.0859 | 152.1469 | 0.0253 | 0.2453 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0601 | 0.0692 | 0.0692 | 0.1518 | 0.0692 | 102.3998 | 0.0281 | 0.1625 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0601 | 0.0496 | 0.0496 | 0.1326 | 0.0496 | 102.3998 | 0.0267 | 0.1283 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2219 | 0.0000 | 0.0000 | 0.0000 | 0.1109 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0601 | 0.0300 | 0.0300 | 0.1136 | 0.0300 | 102.3998 | 0.0253 | 0.0943 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0844 | 0.0000 | 0.0000 | 0.0000 | 0.0422 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0437 | 0.0128 | 0.0128 | 0.0211 | 0.0128 | 64.1643 | 0.0196 | 0.0265 |
| 10 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0397 | 0.0125 | 0.0125 | 0.0207 | 0.0125 | 64.1643 | 0.0198 | 0.0260 |
| 11 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0357 | 0.0123 | 0.0123 | 0.0200 | 0.0123 | 64.1643 | 0.0200 | 0.0254 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0248 | 0.0099 | 0.0145 | 0.0126 | -0.0086 | 5.6541 | 0.0043 | 0.0198 |
| 13 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0412 | 0.0068 | 0.0068 | 0.0136 | 0.0068 | 42.4997 | 0.0153 | 0.0154 |
| 14 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0372 | 0.0069 | 0.0069 | 0.0133 | 0.0069 | 42.4997 | 0.0151 | 0.0152 |
| 15 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0331 | 0.0069 | 0.0069 | 0.0129 | 0.0069 | 42.4997 | 0.0149 | 0.0150 |
| 16 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0249 | 0.0052 | 0.0052 | 0.0073 | 0.0052 | 66.5560 | 0.0252 | 0.0101 |
| 17 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0239 | 0.0045 | 0.0045 | 0.0071 | 0.0045 | 66.5560 | 0.0256 | 0.0092 |
| 18 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0184 | -0.0020 | 0.0036 | -0.0100 | -5.918e-04 | 1.0639 | 0.0011 | 0.0079 |
| 19 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0230 | 0.0039 | 0.0039 | 0.0060 | 0.0039 | 66.5560 | 0.0260 | 0.0079 |
| 20 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0189 | -0.0024 | 0.0048 | -0.0068 | -0.0017 | 1.0017 | 0.0011 | 0.0070 |
| 21 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0209 | 0.0033 | 0.0082 | 0.0034 | -0.0020 | 4.1339 | 0.0042 | 0.0070 |
| 22 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0150 | -0.0029 | 0.0036 | -0.0052 | -0.0023 | 1.0274 | 0.0011 | 0.0063 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0154 | -0.0028 | 0.0038 | -0.0050 | -0.0013 | 0.9844 | 0.0011 | 0.0062 |
| 24 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0218 | 0.0026 | 0.0068 | 0.0038 | -0.0028 | 4.3652 | 0.0040 | 0.0062 |
| 25 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0510 | -0.0034 | 0.0034 | -0.0035 | -0.0130 | 0.9943 | 0.0350 | 0.0061 |
| 26 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0510 | -0.0034 | 0.0034 | -0.0034 | -0.0229 | 0.9943 | 0.0350 | 0.0060 |
| 27 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0155 | -0.0018 | 0.0036 | -0.0067 | 0.0012 | 0.9073 | 0.0011 | 0.0060 |
| 28 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0161 | -0.0026 | 0.0043 | -0.0044 | 5.793e-04 | 0.8980 | 0.0011 | 0.0059 |
| 29 | mod.cls_blocks.0.attn.h6 | CLS<-charged_hadron | 0.0188 | -0.0016 | 0.0050 | -0.0052 | -0.0016 | 0.9785 | 9.792e-04 | 0.0054 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0195 | 3.899e-04 | 0.0063 | -0.0068 | -0.0011 | 1.0746 | 9.530e-04 | 0.0054 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0268 | 0.0161 | 0.0198 | 0.0161 | 0.0161 | 7.4048 | 0.0043 | 0.0291 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0253 | 0.0053 | 0.0098 | 0.0053 | 0.0053 | 5.8661 | 0.0042 | 0.0103 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0223 | 0.0043 | 0.0085 | 0.0043 | 0.0043 | 4.8331 | 0.0040 | 0.0086 |
| 4 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0270 | 0.0036 | 0.0051 | 0.0036 | 0.0036 | 3.5083 | 0.0038 | 0.0066 |
| 5 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0253 | 0.0035 | 0.0048 | 0.0035 | 0.0035 | 3.8802 | 0.0039 | 0.0065 |
| 6 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0212 | 0.0034 | 0.0040 | 0.0034 | 0.0034 | 4.7800 | 0.0040 | 0.0061 |
| 7 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0510 | -0.0034 | 0.0034 | -0.0034 | -0.0034 | 0.9943 | 0.0350 | 0.0060 |
| 8 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0510 | -0.0034 | 0.0034 | -0.0034 | -0.0034 | 0.9943 | 0.0350 | 0.0060 |
| 9 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0153 | -0.0033 | 0.0039 | -0.0033 | -0.0033 | 1.0703 | 0.0011 | 0.0059 |
| 10 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0158 | -0.0032 | 0.0041 | -0.0032 | -0.0032 | 1.0280 | 0.0011 | 0.0058 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0169 | -0.0029 | 0.0046 | -0.0029 | -0.0029 | 0.9431 | 0.0011 | 0.0054 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0163 | -0.0030 | 0.0030 | -0.0030 | -0.0030 | 12.2921 | 0.0109 | 0.0052 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0163 | -0.0030 | 0.0030 | -0.0030 | -0.0030 | 12.2921 | 0.0109 | 0.0052 |
| 14 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0163 | -0.0024 | 0.0038 | -0.0024 | -0.0024 | 0.9430 | 0.0011 | 0.0045 |
| 15 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0177 | -0.0020 | 0.0045 | -0.0020 | -0.0020 | 0.9476 | 0.0011 | 0.0042 |
| 16 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0198 | 0.0016 | 0.0069 | 0.0016 | 0.0016 | 1.0999 | 9.530e-04 | 0.0042 |
| 17 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0187 | 0.0022 | 0.0027 | 0.0022 | 0.0022 | 3.7693 | 0.0029 | 0.0040 |
| 18 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0146 | -0.0021 | 0.0033 | -0.0021 | -0.0021 | 1.0384 | 0.0011 | 0.0040 |
| 19 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0217 | 0.0021 | 0.0031 | 0.0021 | 0.0021 | 3.9665 | 0.0031 | 0.0040 |
| 20 | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0190 | 0.0020 | 0.0036 | 0.0020 | 0.0020 | 0.8799 | 9.420e-04 | 0.0039 |
| 21 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0138 | -0.0020 | 0.0030 | -0.0020 | -0.0020 | 1.0858 | 0.0012 | 0.0038 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0190 | 0.0019 | 0.0034 | 0.0019 | 0.0019 | 0.8708 | 9.748e-04 | 0.0037 |
| 23 | mod.cls_blocks.0.attn.h3 | CLS<-neutral_hadron | 0.0203 | 0.0019 | 0.0024 | 0.0019 | 0.0019 | 3.0061 | 0.0028 | 0.0035 |
| 24 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0187 | 0.0018 | 0.0030 | 0.0018 | 0.0018 | 0.8477 | 0.0011 | 0.0034 |
| 25 | mod.cls_blocks.0.attn.h3 | charged_hadron<-neutral_hadron | 0.0209 | 0.0018 | 0.0023 | 0.0018 | 0.0018 | 2.6906 | 0.0028 | 0.0032 |
| 26 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0165 | -0.0018 | 0.0018 | -0.0018 | -0.0018 | 8.5429 | 0.0123 | 0.0032 |
| 27 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0165 | -0.0018 | 0.0018 | -0.0018 | -0.0018 | 8.5429 | 0.0123 | 0.0032 |
| 28 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0181 | -0.0015 | 0.0034 | -0.0015 | -0.0015 | 1.0418 | 0.0011 | 0.0031 |
| 29 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0201 | -0.0010 | 0.0054 | -0.0010 | -0.0010 | 3.3787 | 0.0037 | 0.0029 |
| 30 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0216 | 7.989e-04 | 0.0067 | 7.989e-04 | 7.989e-04 | 4.1062 | 0.0039 | 0.0029 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
