# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8992**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0937 | 0.1668 | 0.1668 | 0.2891 | 0.1668 | 102.3998 | 0.0442 | 0.3531 |
| 2 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1040 | 0.1712 | 0.1712 | 0.2730 | 0.1712 | 102.3998 | 0.0393 | 0.3506 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1067 | 0.1517 | 0.1517 | 0.2874 | 0.1517 | 152.1469 | 0.0178 | 0.3333 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0938 | 0.1404 | 0.1404 | 0.2621 | 0.1404 | 152.1469 | 0.0191 | 0.3065 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0895 | 0.1338 | 0.1338 | 0.2390 | 0.1338 | 102.3998 | 0.0363 | 0.2867 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0912 | 0.1105 | 0.1105 | 0.2504 | 0.1105 | 152.1469 | 0.0169 | 0.2633 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0668 | 0.0304 | 0.0304 | 0.1315 | 0.0304 | 102.3998 | 0.0177 | 0.1037 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0705 | 0.0095 | 0.0095 | 0.1551 | 0.0095 | 152.1469 | 0.0117 | 0.0894 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.1097 | 0.0240 | 0.0240 | 0.0240 | 0.0113 | 22.4125 | 0.0316 | 0.0420 |
| 10 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0487 | -0.0112 | 0.0112 | -0.0318 | -0.0112 | 64.1643 | 0.0340 | 0.0299 |
| 11 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0258 | -0.0099 | 0.0099 | -0.0275 | -0.0099 | 66.5560 | 0.0221 | 0.0261 |
| 12 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0281 | -0.0090 | 0.0090 | -0.0227 | -0.0090 | 66.5560 | 0.0196 | 0.0226 |
| 13 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0256 | -0.0089 | 0.0089 | -0.0223 | -0.0089 | 66.5560 | 0.0195 | 0.0222 |
| 14 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0431 | -0.0079 | 0.0079 | -0.0242 | -0.0079 | 64.1643 | 0.0295 | 0.0220 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0546 | -0.0079 | 0.0079 | -0.0233 | -0.0079 | 64.1643 | 0.0320 | 0.0215 |
| 16 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0225 | -0.0066 | 0.0066 | -0.0189 | -0.0066 | 66.5560 | 0.0144 | 0.0177 |
| 17 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0265 | 0.0091 | 0.0091 | 0.0091 | 0.0013 | 36.0058 | 0.0216 | 0.0159 |
| 18 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0189 | -0.0077 | 0.0106 | -0.0105 | -0.0129 | 5.7503 | 0.0100 | 0.0156 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0213 | -0.0047 | 0.0108 | -0.0159 | -0.0118 | 1.2204 | 0.0019 | 0.0154 |
| 20 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0354 | -0.0061 | 0.0061 | -0.0123 | -0.0061 | 42.4997 | 0.0150 | 0.0138 |
| 21 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0284 | -0.0054 | 0.0054 | -0.0136 | -0.0054 | 42.4997 | 0.0162 | 0.0136 |
| 22 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0178 | -0.0051 | 0.0102 | -0.0102 | -0.0028 | 1.1880 | 0.0021 | 0.0127 |
| 23 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0204 | -0.0047 | 0.0115 | -0.0102 | -0.0107 | 0.9956 | 0.0016 | 0.0126 |
| 24 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0170 | -0.0046 | 0.0080 | -0.0084 | -0.0042 | 0.9682 | 0.0015 | 0.0108 |
| 25 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0099 | -0.0052 | 0.0052 | -0.0085 | -0.0074 | 23.8153 | 0.0314 | 0.0107 |
| 26 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0279 | -0.0040 | 0.0045 | -0.0107 | -0.0040 | 42.4997 | 0.0141 | 0.0105 |
| 27 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0177 | -0.0039 | 0.0094 | -0.0080 | -0.0015 | 1.0942 | 0.0018 | 0.0103 |
| 28 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0203 | -0.0014 | 0.0014 | -0.0167 | -0.0014 | 64.1643 | 0.0182 | 0.0101 |
| 29 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0404 | 0.0055 | 0.0067 | 0.0056 | 5.870e-04 | 13.3450 | 0.0221 | 0.0100 |
| 30 | mod.cls_blocks.0.attn.h6 | CLS<-charged_hadron | 0.0211 | -0.0018 | 0.0109 | -0.0095 | -0.0070 | 1.1295 | 0.0016 | 0.0093 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0271 | 0.0105 | 0.0272 | 0.0105 | 0.0105 | 5.2832 | 0.0056 | 0.0225 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0252 | 0.0091 | 0.0205 | 0.0091 | 0.0091 | 6.6650 | 0.0026 | 0.0188 |
| 3 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0188 | -0.0072 | 0.0117 | -0.0072 | -0.0072 | 1.2607 | 0.0021 | 0.0137 |
| 4 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0215 | 0.0069 | 0.0088 | 0.0069 | 0.0069 | 20.1524 | 0.0316 | 0.0126 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0251 | 0.0047 | 0.0184 | 0.0047 | 0.0047 | 5.7910 | 0.0075 | 0.0116 |
| 6 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0247 | -0.0038 | 0.0169 | -0.0038 | -0.0038 | 6.2093 | 0.0100 | 0.0099 |
| 7 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0281 | 0.0049 | 0.0083 | 0.0049 | 0.0049 | 4.8255 | 0.0074 | 0.0095 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0185 | -0.0045 | 0.0104 | -0.0045 | -0.0045 | 1.1590 | 0.0018 | 0.0094 |
| 9 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0175 | -0.0049 | 0.0082 | -0.0049 | -0.0049 | 0.9997 | 0.0015 | 0.0094 |
| 10 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0099 | -0.0052 | 0.0052 | -0.0052 | -0.0052 | 23.8153 | 0.0314 | 0.0091 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0216 | -0.0047 | 0.0052 | -0.0047 | -0.0047 | 19.7901 | 0.0100 | 0.0084 |
| 12 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0300 | 0.0046 | 0.0053 | 0.0046 | 0.0046 | 31.1300 | 0.0216 | 0.0083 |
| 13 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0193 | -0.0036 | 0.0104 | -0.0036 | -0.0036 | 0.9229 | 0.0016 | 0.0080 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0241 | -0.0042 | 0.0044 | -0.0042 | -0.0042 | 6.0231 | 0.0051 | 0.0073 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-charged_hadron | 0.0200 | 0.0033 | 0.0066 | 0.0033 | 0.0033 | 0.6997 | 0.0014 | 0.0066 |
| 16 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0197 | -0.0036 | 0.0040 | -0.0036 | -0.0036 | 20.5866 | 0.0121 | 0.0064 |
| 17 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0249 | 0.0022 | 0.0118 | 0.0022 | 0.0022 | 6.3780 | 0.0039 | 0.0063 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0231 | -0.0027 | 0.0084 | -0.0027 | -0.0027 | 23.8968 | 0.0360 | 0.0062 |
| 19 | mod.blocks.3.attn.h7 | electron<-muon | 0.4824 | -0.0034 | 0.0034 | -0.0034 | -0.0034 | 5.8907 | 0.0044 | 0.0060 |
| 20 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0268 | 0.0033 | 0.0037 | 0.0033 | 0.0033 | 19.1775 | 0.0139 | 0.0058 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0166 | -0.0030 | 0.0043 | -0.0030 | -0.0030 | 1.3792 | 9.695e-04 | 0.0056 |
| 22 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0202 | -0.0022 | 0.0095 | -0.0022 | -0.0022 | 1.1327 | 0.0019 | 0.0056 |
| 23 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-charged_hadron | 0.0217 | 0.0026 | 0.0062 | 0.0026 | 0.0026 | 0.8631 | 0.0016 | 0.0055 |
| 24 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0213 | -0.0031 | 0.0031 | -0.0031 | -0.0031 | 30.7762 | 0.0122 | 0.0054 |
| 25 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0231 | -0.0026 | 0.0051 | -0.0026 | -0.0026 | 1.4133 | 8.949e-04 | 0.0052 |
| 26 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0215 | 9.349e-04 | 0.0153 | 9.349e-04 | 9.349e-04 | 1.4938 | 0.0021 | 0.0052 |
| 27 | mod.cls_blocks.0.attn.h0 | charged_hadron<-photon | 0.0189 | 0.0023 | 0.0058 | 0.0023 | 0.0023 | 0.7799 | 0.0013 | 0.0048 |
| 28 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0208 | 0.0015 | 0.0106 | 0.0015 | 0.0015 | 1.1159 | 0.0015 | 0.0048 |
| 29 | mod.cls_blocks.0.attn.h0 | CLS<-charged_hadron | 0.0199 | 0.0022 | 0.0057 | 0.0022 | 0.0022 | 0.8280 | 0.0014 | 0.0047 |
| 30 | mod.cls_blocks.0.attn.h0 | CLS<-neutral_hadron | 0.0238 | 0.0019 | 0.0066 | 0.0019 | 0.0019 | 4.2687 | 0.0063 | 0.0046 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
