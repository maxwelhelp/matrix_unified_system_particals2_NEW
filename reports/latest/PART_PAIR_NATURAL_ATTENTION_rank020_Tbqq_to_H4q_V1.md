# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9136**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0771 | 0.9810 | 1.1128 | 0.9810 | 1.5374 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0797 | 0.5133 | 0.9766 | 0.5133 | 1.0016 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0882 | 0.1771 | 0.9190 | 0.1771 | 0.6366 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0423 | -0.2803 | -0.2959 | -0.2890 | 0.4283 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0589 | 0.2472 | 0.3137 | 0.2472 | 0.4041 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0747 | -0.1735 | -0.2086 | -0.1765 | 0.2779 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0639 | 0.1201 | 0.2345 | 0.1201 | 0.2374 |
| 8 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0339 | -0.1313 | -0.1511 | -0.1400 | 0.2068 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0505 | -0.0862 | -0.1695 | -0.0891 | 0.1709 |
| 10 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0755 | 0.0220 | 0.2073 | 0.0220 | 0.1257 |
| 11 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.2449 | 0.0000 | 0.1225 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0765 | -0.0859 | -0.0543 | -0.0859 | 0.1130 |
| 13 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0340 | -0.0283 | -0.1179 | -0.0342 | 0.0872 |
| 14 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.1626 | -0.0511 | -0.0584 | -0.0515 | 0.0803 |
| 15 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0213 | -0.0132 | -0.0998 | -0.0191 | 0.0631 |
| 16 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0624 | -0.0360 | -0.0495 | -0.0360 | 0.0607 |
| 17 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0264 | 0.0012 | -0.1095 | 0.0012 | 0.0560 |
| 18 | mod.cls_blocks.0.attn.h7 | photon<-muon | 0.0000 | 0.0000 | -0.1083 | 0.0000 | 0.0541 |
| 19 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0290 | 0.0286 | 0.0485 | 0.0317 | 0.0528 |
| 20 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0000 | 0.0000 | -0.1044 | 0.0000 | 0.0522 |
| 21 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0341 | 0.0357 | 0.0314 | 0.0357 | 0.0514 |
| 22 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | -0.0937 | 0.0000 | 0.0468 |
| 23 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0997 | -0.0300 | -0.0233 | -0.0303 | 0.0416 |
| 24 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0390 | 0.0240 | 0.0333 | 0.0240 | 0.0406 |
| 25 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0231 | 0.0266 | 0.0279 | 0.0266 | 0.0406 |
| 26 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0086 | 0.0019 | -0.0742 | 0.0019 | 0.0390 |
| 27 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0375 | 0.0225 | 0.0288 | 0.0225 | 0.0369 |
| 28 | mod.cls_blocks.1.attn.h3 | neutral_hadron<-muon | 0.8759 | -0.0182 | 0.0371 | -0.0182 | 0.0368 |
| 29 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0385 | 0.0204 | 0.0309 | 0.0204 | 0.0359 |
| 30 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0000 | 0.0000 | 0.0709 | 0.0000 | 0.0355 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0314 | 0.0970 | 0.0970 | 0.0970 | 0.1456 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0460 | 0.0850 | 0.0850 | 0.0850 | 0.1275 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0358 | 0.0514 | 0.0514 | 0.0514 | 0.0770 |
| 4 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0591 | 0.0337 | 0.0337 | 0.0337 | 0.0505 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0283 | 0.0248 | 0.0248 | 0.0248 | 0.0372 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0249 | 0.0242 | 0.0242 | 0.0242 | 0.0363 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0326 | 0.0205 | 0.0205 | 0.0205 | 0.0308 |
| 8 | mod.cls_blocks.1.attn.h5 | neutral_hadron<-muon | 0.0756 | 0.0194 | 0.0194 | 0.0194 | 0.0291 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0256 | 0.0178 | 0.0178 | 0.0178 | 0.0266 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0200 | -0.0163 | -0.0163 | -0.0163 | 0.0245 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0143 | -0.0138 | -0.0138 | -0.0138 | 0.0207 |
| 12 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0479 | 0.0125 | 0.0125 | 0.0125 | 0.0187 |
| 13 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0647 | 0.0118 | 0.0118 | 0.0118 | 0.0177 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0295 | 0.0109 | 0.0109 | 0.0109 | 0.0163 |
| 15 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-muon | 0.0503 | 0.0103 | 0.0103 | 0.0103 | 0.0154 |
| 16 | mod.cls_blocks.1.attn.h5 | CLS<-muon | 0.0387 | 0.0096 | 0.0096 | 0.0096 | 0.0144 |
| 17 | mod.cls_blocks.0.attn.h7 | photon<-electron | 0.0129 | -0.0092 | -0.0092 | -0.0092 | 0.0139 |
| 18 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0367 | -0.0088 | -0.0088 | -0.0088 | 0.0131 |
| 19 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0186 | 0.0084 | 0.0084 | 0.0084 | 0.0126 |
| 20 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0302 | -0.0070 | -0.0070 | -0.0070 | 0.0104 |
| 21 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0233 | 0.0069 | 0.0069 | 0.0069 | 0.0103 |
| 22 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0366 | 0.0068 | 0.0068 | 0.0068 | 0.0103 |
| 23 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0190 | 0.0061 | 0.0061 | 0.0061 | 0.0091 |
| 24 | mod.cls_blocks.0.attn.h3 | CLS<-muon | 0.0329 | 0.0058 | 0.0058 | 0.0058 | 0.0087 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0206 | -0.0057 | -0.0057 | -0.0057 | 0.0085 |
| 26 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0219 | 0.0057 | 0.0057 | 0.0057 | 0.0085 |
| 27 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0421 | 0.0056 | 0.0056 | 0.0056 | 0.0083 |
| 28 | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0162 | 0.0051 | 0.0051 | 0.0051 | 0.0077 |
| 29 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0209 | -0.0050 | -0.0050 | -0.0050 | 0.0076 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0150 | -0.0048 | -0.0048 | -0.0048 | 0.0072 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
