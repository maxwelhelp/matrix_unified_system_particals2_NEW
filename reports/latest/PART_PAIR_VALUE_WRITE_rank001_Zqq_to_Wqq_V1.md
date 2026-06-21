# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **7744**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1379 | 0.8397 | 0.8397 | 1.8190 | 0.8397 | 152.1469 | 0.0596 | 1.9591 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1459 | 0.6422 | 0.6422 | 1.8042 | 0.6422 | 152.1469 | 0.0481 | 1.7049 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1439 | 0.6916 | 0.6916 | 1.6474 | 0.6916 | 152.1469 | 0.0510 | 1.6882 |
| 4 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 1.0817 | 0.0000 | 0.0000 | 0.0000 | 0.5408 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0571 | 0.2304 | 0.2553 | 0.2290 | 0.2083 | 27.4894 | 0.0198 | 0.4087 |
| 6 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1144 | 0.1487 | 0.1487 | 0.3699 | 0.1487 | 102.3998 | 0.0211 | 0.3709 |
| 7 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1118 | 0.1197 | 0.1197 | 0.4217 | 0.1197 | 102.3998 | 0.0224 | 0.3605 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1125 | 0.1269 | 0.1269 | 0.3758 | 0.1269 | 102.3998 | 0.0221 | 0.3466 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.6643 | 0.0000 | 0.0000 | 0.0000 | 0.3322 |
| 10 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.4178 | 0.0000 | 0.0000 | 0.0000 | 0.2089 |
| 11 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0355 | 0.0539 | 0.0539 | 0.1075 | 0.0539 | 66.5560 | 0.0400 | 0.1212 |
| 12 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0770 | 0.0515 | 0.0515 | 0.0854 | 0.0515 | 64.1643 | 0.0170 | 0.1071 |
| 13 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0352 | 0.0423 | 0.0423 | 0.0905 | 0.0423 | 66.5560 | 0.0381 | 0.0981 |
| 14 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0351 | 0.0384 | 0.0384 | 0.0917 | 0.0384 | 66.5560 | 0.0375 | 0.0938 |
| 15 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0571 | 0.0523 | 0.0557 | 0.0516 | 0.0460 | 22.6729 | 0.0091 | 0.0920 |
| 16 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0774 | 0.0388 | 0.0388 | 0.0816 | 0.0388 | 64.1643 | 0.0144 | 0.0893 |
| 17 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0775 | 0.0346 | 0.0346 | 0.0893 | 0.0346 | 64.1643 | 0.0136 | 0.0879 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1733 | 0.0000 | 0.0000 | 0.0000 | 0.0866 |
| 19 | mod.cls_blocks.0.attn.h3 | charged_hadron<-CLS | 0.0318 | 0.0418 | 0.0418 | 0.0512 | 0.0418 | 43.6006 | 0.0356 | 0.0778 |
| 20 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0417 | 0.0397 | 0.0604 | 0.0429 | 0.0445 | 12.8490 | 0.0150 | 0.0762 |
| 21 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | 0.0000 | -0.1227 | 0.0000 | 0.0000 | 0.0000 | 0.0613 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0359 | -0.0175 | 0.0249 | -0.0531 | -0.0060 | 2.2478 | 0.0028 | 0.0503 |
| 23 | mod.cls_blocks.0.attn.h3 | CLS<-CLS | 0.0263 | 0.0253 | 0.0253 | 0.0349 | 0.0253 | 43.6006 | 0.0290 | 0.0491 |
| 24 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.1054 | 0.0226 | 0.0226 | 0.0302 | 0.0226 | 42.4997 | 0.0131 | 0.0433 |
| 25 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0315 | -0.0193 | 0.0234 | -0.0344 | -0.0128 | 1.4895 | 0.0035 | 0.0423 |
| 26 | mod.cls_blocks.0.attn.h3 | photon<-CLS | 0.0245 | 0.0198 | 0.0198 | 0.0335 | 0.0198 | 43.6006 | 0.0268 | 0.0415 |
| 27 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0313 | 0.0221 | 0.0285 | 0.0198 | 0.0128 | 15.1335 | 0.0151 | 0.0391 |
| 28 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0249 | -0.0099 | 0.0151 | -0.0475 | -0.0017 | 1.6365 | 0.0030 | 0.0374 |
| 29 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0613 | 6.354e-04 | 6.354e-04 | -0.0658 | 5.890e-04 | 13.8143 | 0.0107 | 0.0337 |
| 30 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0000 | 0.0000 | 0.0000 | -0.0647 | 0.0000 | 0.0000 | 0.0000 | 0.0323 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0571 | 0.2304 | 0.2553 | 0.2304 | 0.2304 | 27.4894 | 0.0198 | 0.4094 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0571 | 0.0523 | 0.0557 | 0.0523 | 0.0523 | 22.6729 | 0.0091 | 0.0923 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0437 | -0.0346 | 0.0428 | -0.0346 | -0.0346 | 9.1060 | 0.0136 | 0.0626 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0383 | 0.0308 | 0.0504 | 0.0308 | 0.0308 | 3.5343 | 0.0032 | 0.0589 |
| 5 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0425 | 0.0239 | 0.0715 | 0.0239 | 0.0239 | 12.2901 | 0.0150 | 0.0537 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0387 | 0.0260 | 0.0570 | 0.0260 | 0.0260 | 2.6408 | 0.0032 | 0.0533 |
| 7 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0313 | 0.0221 | 0.0285 | 0.0221 | 0.0221 | 15.1335 | 0.0151 | 0.0403 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0315 | -0.0193 | 0.0234 | -0.0193 | -0.0193 | 1.4895 | 0.0035 | 0.0348 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0361 | -0.0130 | 0.0221 | -0.0130 | -0.0130 | 8.7742 | 0.0141 | 0.0251 |
| 10 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0687 | 0.0141 | 0.0141 | 0.0141 | 0.0141 | 30.2158 | 0.0350 | 0.0247 |
| 11 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0548 | -0.0103 | 0.0183 | -0.0103 | -0.0103 | 9.4727 | 0.0136 | 0.0201 |
| 12 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0398 | 0.0105 | 0.0123 | 0.0105 | 0.0105 | 13.0562 | 0.0056 | 0.0189 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0252 | -0.0098 | 0.0156 | -0.0098 | -0.0098 | 1.6508 | 0.0030 | 0.0186 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0368 | 0.0054 | 0.0358 | 0.0054 | 0.0054 | 2.2548 | 0.0031 | 0.0171 |
| 15 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0440 | 0.0078 | 0.0183 | 0.0078 | 0.0078 | 11.4412 | 0.0078 | 0.0163 |
| 16 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0514 | 0.0082 | 0.0082 | 0.0082 | 0.0082 | 20.0791 | 0.0196 | 0.0143 |
| 17 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0358 | 0.0067 | 0.0138 | 0.0067 | 0.0067 | 2.1600 | 0.0017 | 0.0134 |
| 18 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0420 | 0.0076 | 0.0076 | 0.0076 | 0.0076 | 20.9524 | 0.0346 | 0.0133 |
| 19 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0376 | -0.0058 | 0.0161 | -0.0058 | -0.0058 | 2.2346 | 0.0028 | 0.0127 |
| 20 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0385 | 0.0066 | 0.0114 | 0.0066 | 0.0066 | 2.9559 | 0.0018 | 0.0127 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0217 | -0.0064 | 0.0095 | -0.0064 | -0.0064 | 1.2765 | 0.0032 | 0.0120 |
| 22 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0367 | -0.0050 | 0.0147 | -0.0050 | -0.0050 | 1.4874 | 0.0027 | 0.0111 |
| 23 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0283 | 0.0032 | 0.0247 | 0.0032 | 0.0032 | 2.1329 | 0.0031 | 0.0110 |
| 24 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0198 | 0.0054 | 0.0095 | 0.0054 | 0.0054 | 9.6292 | 0.0101 | 0.0105 |
| 25 | mod.cls_blocks.0.attn.h3 | photon<-neutral_hadron | 0.0432 | -0.0056 | 0.0061 | -0.0056 | -0.0056 | 5.0538 | 0.0077 | 0.0099 |
| 26 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0829 | -0.0055 | 0.0055 | -0.0055 | -0.0055 | 20.3240 | 0.0124 | 0.0096 |
| 27 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-charged_hadron | 0.0339 | -0.0052 | 0.0069 | -0.0052 | -0.0052 | 0.9686 | 0.0018 | 0.0096 |
| 28 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0442 | 0.0053 | 0.0053 | 0.0053 | 0.0053 | 19.8150 | 0.0126 | 0.0092 |
| 29 | mod.cls_blocks.0.attn.h2 | photon<-neutral_hadron | 0.0423 | -0.0051 | 0.0057 | -0.0051 | -0.0051 | 8.4953 | 0.0075 | 0.0091 |
| 30 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0417 | -0.0042 | 0.0091 | -0.0042 | -0.0042 | 9.8229 | 0.0076 | 0.0086 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
