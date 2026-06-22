# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8992**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0937 | 0.1668 | 0.2891 | 0.1668 | 0.3114 |
| 2 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1040 | 0.1712 | 0.2730 | 0.1712 | 0.3078 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1067 | 0.1517 | 0.2874 | 0.1517 | 0.2954 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0938 | 0.1404 | 0.2621 | 0.1404 | 0.2714 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0895 | 0.1338 | 0.2390 | 0.1338 | 0.2533 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0912 | 0.1105 | 0.2504 | 0.1105 | 0.2357 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0668 | 0.0304 | 0.1315 | 0.0304 | 0.0961 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0705 | 0.0095 | 0.1551 | 0.0095 | 0.0870 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.1097 | 0.0240 | 0.0240 | 0.0113 | 0.0360 |
| 10 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0487 | -0.0112 | -0.0318 | -0.0112 | 0.0271 |
| 11 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0258 | -0.0099 | -0.0275 | -0.0099 | 0.0237 |
| 12 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0281 | -0.0090 | -0.0227 | -0.0090 | 0.0204 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0431 | -0.0079 | -0.0242 | -0.0079 | 0.0200 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0256 | -0.0089 | -0.0223 | -0.0089 | 0.0200 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0546 | -0.0079 | -0.0233 | -0.0079 | 0.0195 |
| 16 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0225 | -0.0066 | -0.0189 | -0.0066 | 0.0161 |
| 17 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0265 | 0.0091 | 0.0091 | 0.0013 | 0.0136 |
| 18 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0189 | -0.0077 | -0.0105 | -0.0129 | 0.0129 |
| 19 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0213 | -0.0047 | -0.0159 | -0.0118 | 0.0127 |
| 20 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0354 | -0.0061 | -0.0123 | -0.0061 | 0.0123 |
| 21 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0284 | -0.0054 | -0.0136 | -0.0054 | 0.0123 |
| 22 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0178 | -0.0051 | -0.0102 | -0.0028 | 0.0102 |
| 23 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0204 | -0.0047 | -0.0102 | -0.0107 | 0.0098 |
| 24 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0203 | -0.0014 | -0.0167 | -0.0014 | 0.0097 |
| 25 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0099 | -0.0052 | -0.0085 | -0.0074 | 0.0094 |
| 26 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0279 | -0.0040 | -0.0107 | -0.0040 | 0.0094 |
| 27 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0170 | -0.0046 | -0.0084 | -0.0042 | 0.0088 |
| 28 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0404 | 0.0055 | 0.0056 | 5.870e-04 | 0.0083 |
| 29 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0177 | -0.0039 | -0.0080 | -0.0015 | 0.0079 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0214 | -0.0052 | -0.0052 | -0.0034 | 0.0078 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0271 | 0.0105 | 0.0105 | 0.0105 | 0.0157 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0252 | 0.0091 | 0.0091 | 0.0091 | 0.0137 |
| 3 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0188 | -0.0072 | -0.0072 | -0.0072 | 0.0108 |
| 4 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0215 | 0.0069 | 0.0069 | 0.0069 | 0.0104 |
| 5 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0099 | -0.0052 | -0.0052 | -0.0052 | 0.0078 |
| 6 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0281 | 0.0049 | 0.0049 | 0.0049 | 0.0074 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0175 | -0.0049 | -0.0049 | -0.0049 | 0.0073 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0216 | -0.0047 | -0.0047 | -0.0047 | 0.0071 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0251 | 0.0047 | 0.0047 | 0.0047 | 0.0070 |
| 10 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0300 | 0.0046 | 0.0046 | 0.0046 | 0.0069 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0185 | -0.0045 | -0.0045 | -0.0045 | 0.0068 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0241 | -0.0042 | -0.0042 | -0.0042 | 0.0062 |
| 13 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0247 | -0.0038 | -0.0038 | -0.0038 | 0.0057 |
| 14 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0193 | -0.0036 | -0.0036 | -0.0036 | 0.0054 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0197 | -0.0036 | -0.0036 | -0.0036 | 0.0054 |
| 16 | mod.blocks.3.attn.h7 | electron<-muon | 0.4824 | -0.0034 | -0.0034 | -0.0034 | 0.0052 |
| 17 | mod.cls_blocks.0.attn.h0 | photon<-charged_hadron | 0.0200 | 0.0033 | 0.0033 | 0.0033 | 0.0049 |
| 18 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0268 | 0.0033 | 0.0033 | 0.0033 | 0.0049 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0213 | -0.0031 | -0.0031 | -0.0031 | 0.0046 |
| 20 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0166 | -0.0030 | -0.0030 | -0.0030 | 0.0046 |
| 21 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0231 | -0.0027 | -0.0027 | -0.0027 | 0.0041 |
| 22 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0231 | -0.0026 | -0.0026 | -0.0026 | 0.0040 |
| 23 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-charged_hadron | 0.0217 | 0.0026 | 0.0026 | 0.0026 | 0.0039 |
| 24 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0209 | 0.0024 | 0.0024 | 0.0024 | 0.0036 |
| 25 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0158 | -0.0024 | -0.0024 | -0.0024 | 0.0036 |
| 26 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0154 | -0.0024 | -0.0024 | -0.0024 | 0.0036 |
| 27 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-photon | 0.0186 | 0.0024 | 0.0024 | 0.0024 | 0.0036 |
| 28 | mod.cls_blocks.0.attn.h1 | photon<-photon | 0.0192 | 0.0024 | 0.0024 | 0.0024 | 0.0035 |
| 29 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0211 | -0.0023 | -0.0023 | -0.0023 | 0.0035 |
| 30 | mod.cls_blocks.0.attn.h0 | charged_hadron<-photon | 0.0189 | 0.0023 | 0.0023 | 0.0023 | 0.0034 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
