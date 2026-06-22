# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9136**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0771 | 0.9810 | 0.9810 | 1.1128 | 0.9810 | 152.1469 | 0.1075 | 1.7826 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0797 | 0.5133 | 0.5562 | 0.9766 | 0.5133 | 152.1469 | 0.0771 | 1.1406 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0882 | 0.1771 | 0.1771 | 0.9190 | 0.1771 | 152.1469 | 0.0343 | 0.6808 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0423 | -0.2803 | 0.2803 | -0.2959 | -0.2890 | 56.3743 | 0.1495 | 0.4983 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0589 | 0.2472 | 0.2472 | 0.3137 | 0.2472 | 102.3998 | 0.0611 | 0.4659 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0747 | -0.1735 | 0.1735 | -0.2086 | -0.1765 | 42.4382 | 0.0826 | 0.3212 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0639 | 0.1201 | 0.1381 | 0.2345 | 0.1201 | 102.3998 | 0.0459 | 0.2719 |
| 8 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0339 | -0.1313 | 0.1490 | -0.1511 | -0.1400 | 36.4193 | 0.1101 | 0.2441 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0505 | -0.0862 | 0.0874 | -0.1695 | -0.0891 | 32.0128 | 0.0629 | 0.1928 |
| 10 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0765 | -0.0859 | 0.0859 | -0.0543 | -0.0859 | 152.1469 | 0.0590 | 0.1344 |
| 11 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0755 | 0.0220 | 0.0220 | 0.2073 | 0.0220 | 102.3998 | 0.0272 | 0.1312 |
| 12 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.2449 | 0.0000 | 0.0000 | 0.0000 | 0.1225 |
| 13 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0340 | -0.0283 | 0.0283 | -0.1179 | -0.0342 | 27.5205 | 0.0499 | 0.0943 |
| 14 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.1626 | -0.0511 | 0.0511 | -0.0584 | -0.0515 | 49.5948 | 0.0457 | 0.0931 |
| 15 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0624 | -0.0360 | 0.0360 | -0.0495 | -0.0360 | 102.3998 | 0.0342 | 0.0697 |
| 16 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0213 | -0.0132 | 0.0151 | -0.0998 | -0.0191 | 21.1721 | 0.0493 | 0.0669 |
| 17 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0290 | 0.0286 | 0.0553 | 0.0485 | 0.0317 | 7.2710 | 0.0141 | 0.0667 |
| 18 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0341 | 0.0357 | 0.0357 | 0.0314 | 0.0357 | 64.1643 | 0.0300 | 0.0603 |
| 19 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0264 | 0.0012 | 0.0012 | -0.1095 | 0.0012 | 21.5875 | 0.0431 | 0.0563 |
| 20 | mod.cls_blocks.0.attn.h7 | photon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1083 | 0.0000 | 0.0000 | 0.0000 | 0.0541 |
| 21 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1044 | 0.0000 | 0.0000 | 0.0000 | 0.0522 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0997 | -0.0300 | 0.0300 | -0.0233 | -0.0303 | 38.3226 | 0.0376 | 0.0491 |
| 23 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0231 | 0.0266 | 0.0266 | 0.0279 | 0.0266 | 66.5560 | 0.0384 | 0.0473 |
| 24 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0937 | 0.0000 | 0.0000 | 0.0000 | 0.0468 |
| 25 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0390 | 0.0240 | 0.0240 | 0.0333 | 0.0240 | 42.4997 | 0.0482 | 0.0466 |
| 26 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0375 | 0.0225 | 0.0225 | 0.0288 | 0.0225 | 64.1643 | 0.0257 | 0.0426 |
| 27 | mod.cls_blocks.1.attn.h3 | neutral_hadron<-muon | 0.8759 | -0.0182 | 0.0182 | 0.0371 | -0.0182 | 4.5374 | 0.0384 | 0.0413 |
| 28 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0385 | 0.0204 | 0.0204 | 0.0309 | 0.0204 | 42.4997 | 0.0501 | 0.0410 |
| 29 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0086 | 0.0019 | 0.0019 | -0.0742 | 0.0019 | 14.8236 | 0.0488 | 0.0394 |
| 30 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0367 | 0.0197 | 0.0197 | 0.0254 | 0.0197 | 42.4997 | 0.0576 | 0.0374 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0314 | 0.0970 | 0.1389 | 0.0970 | 0.0970 | 10.3514 | 0.0141 | 0.1803 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0460 | 0.0850 | 0.0850 | 0.0850 | 0.0850 | 29.0276 | 0.1495 | 0.1487 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0358 | 0.0514 | 0.0514 | 0.0514 | 0.0514 | 22.7459 | 0.1101 | 0.0899 |
| 4 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0591 | 0.0337 | 0.0337 | 0.0337 | 0.0337 | 25.2407 | 0.0457 | 0.0589 |
| 5 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0249 | 0.0242 | 0.0449 | 0.0242 | 0.0242 | 5.9375 | 0.0100 | 0.0476 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0283 | 0.0248 | 0.0341 | 0.0248 | 0.0248 | 7.6245 | 0.0083 | 0.0457 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0326 | 0.0205 | 0.0205 | 0.0205 | 0.0205 | 24.1262 | 0.0826 | 0.0360 |
| 8 | mod.cls_blocks.1.attn.h5 | neutral_hadron<-muon | 0.0756 | 0.0194 | 0.0194 | 0.0194 | 0.0194 | 4.5355 | 0.0707 | 0.0339 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0256 | 0.0178 | 0.0178 | 0.0178 | 0.0178 | 16.4642 | 0.0707 | 0.0311 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0200 | -0.0163 | 0.0251 | -0.0163 | -0.0163 | 1.0401 | 0.0032 | 0.0308 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0143 | -0.0138 | 0.0170 | -0.0138 | -0.0138 | 1.0994 | 0.0035 | 0.0250 |
| 12 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0479 | 0.0125 | 0.0212 | 0.0125 | 0.0125 | 26.1456 | 0.0376 | 0.0240 |
| 13 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0647 | 0.0118 | 0.0118 | 0.0118 | 0.0118 | 12.2216 | 0.0499 | 0.0207 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0295 | 0.0109 | 0.0109 | 0.0109 | 0.0109 | 22.8568 | 0.0629 | 0.0190 |
| 15 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-muon | 0.0503 | 0.0103 | 0.0103 | 0.0103 | 0.0103 | 24.8253 | 0.0468 | 0.0180 |
| 16 | mod.cls_blocks.1.attn.h5 | CLS<-muon | 0.0387 | 0.0096 | 0.0098 | 0.0096 | 0.0096 | 3.2666 | 0.0715 | 0.0169 |
| 17 | mod.cls_blocks.0.attn.h7 | photon<-electron | 0.0129 | -0.0092 | 0.0092 | -0.0092 | -0.0092 | 21.0188 | 0.0394 | 0.0162 |
| 18 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0367 | -0.0088 | 0.0088 | -0.0088 | -0.0088 | 27.0505 | 0.0295 | 0.0153 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0190 | 0.0061 | 0.0224 | 0.0061 | 0.0061 | 1.5369 | 0.0023 | 0.0147 |
| 20 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0186 | 0.0084 | 0.0084 | 0.0084 | 0.0084 | 19.4066 | 0.0581 | 0.0147 |
| 21 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0233 | 0.0069 | 0.0121 | 0.0069 | 0.0069 | 4.9135 | 0.0064 | 0.0134 |
| 22 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0302 | -0.0070 | 0.0070 | -0.0070 | -0.0070 | 23.2748 | 0.0278 | 0.0122 |
| 23 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0219 | 0.0057 | 0.0146 | 0.0057 | 0.0057 | 1.4076 | 0.0018 | 0.0121 |
| 24 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0366 | 0.0068 | 0.0068 | 0.0068 | 0.0068 | 13.5226 | 0.0493 | 0.0120 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0206 | -0.0057 | 0.0135 | -0.0057 | -0.0057 | 1.2513 | 0.0024 | 0.0119 |
| 26 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0209 | -0.0050 | 0.0170 | -0.0050 | -0.0050 | 1.2423 | 0.0024 | 0.0118 |
| 27 | mod.cls_blocks.0.attn.h3 | CLS<-muon | 0.0329 | 0.0058 | 0.0058 | 0.0058 | 0.0058 | 21.2348 | 0.0401 | 0.0101 |
| 28 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0421 | 0.0056 | 0.0056 | 0.0056 | 0.0056 | 1.4360 | 0.0252 | 0.0097 |
| 29 | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0162 | 0.0051 | 0.0051 | 0.0051 | 0.0051 | 18.0039 | 0.0496 | 0.0090 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0150 | -0.0048 | 0.0071 | -0.0048 | -0.0048 | 0.9178 | 0.0015 | 0.0089 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
