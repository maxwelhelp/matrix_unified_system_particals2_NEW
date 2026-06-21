# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **7744**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1379 | 0.8397 | 1.8190 | 0.8397 | 1.7492 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1459 | 0.6422 | 1.8042 | 0.6422 | 1.5443 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1439 | 0.6916 | 1.6474 | 0.6916 | 1.5153 |
| 4 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 1.0817 | 0.0000 | 0.5408 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0571 | 0.2304 | 0.2290 | 0.2083 | 0.3449 |
| 6 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1144 | 0.1487 | 0.3699 | 0.1487 | 0.3337 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.6643 | 0.0000 | 0.3322 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1118 | 0.1197 | 0.4217 | 0.1197 | 0.3306 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1125 | 0.1269 | 0.3758 | 0.1269 | 0.3148 |
| 10 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.4178 | 0.0000 | 0.2089 |
| 11 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0355 | 0.0539 | 0.1075 | 0.0539 | 0.1077 |
| 12 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0770 | 0.0515 | 0.0854 | 0.0515 | 0.0942 |
| 13 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0352 | 0.0423 | 0.0905 | 0.0423 | 0.0875 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | 0.1733 | 0.0000 | 0.0866 |
| 15 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0351 | 0.0384 | 0.0917 | 0.0384 | 0.0842 |
| 16 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0774 | 0.0388 | 0.0816 | 0.0388 | 0.0796 |
| 17 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0775 | 0.0346 | 0.0893 | 0.0346 | 0.0792 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0571 | 0.0523 | 0.0516 | 0.0460 | 0.0781 |
| 19 | mod.cls_blocks.0.attn.h3 | charged_hadron<-CLS | 0.0318 | 0.0418 | 0.0512 | 0.0418 | 0.0674 |
| 20 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | -0.1227 | 0.0000 | 0.0613 |
| 21 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0417 | 0.0397 | 0.0429 | 0.0445 | 0.0612 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0359 | -0.0175 | -0.0531 | -0.0060 | 0.0441 |
| 23 | mod.cls_blocks.0.attn.h3 | CLS<-CLS | 0.0263 | 0.0253 | 0.0349 | 0.0253 | 0.0428 |
| 24 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.1054 | 0.0226 | 0.0302 | 0.0226 | 0.0377 |
| 25 | mod.cls_blocks.0.attn.h3 | photon<-CLS | 0.0245 | 0.0198 | 0.0335 | 0.0198 | 0.0366 |
| 26 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0315 | -0.0193 | -0.0344 | -0.0128 | 0.0365 |
| 27 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0249 | -0.0099 | -0.0475 | -0.0017 | 0.0336 |
| 28 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0613 | 6.354e-04 | -0.0658 | 5.890e-04 | 0.0336 |
| 29 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0000 | 0.0000 | -0.0647 | 0.0000 | 0.0323 |
| 30 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0313 | 0.0221 | 0.0198 | 0.0128 | 0.0320 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0571 | 0.2304 | 0.2304 | 0.2304 | 0.3455 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0571 | 0.0523 | 0.0523 | 0.0523 | 0.0784 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0437 | -0.0346 | -0.0346 | -0.0346 | 0.0519 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0383 | 0.0308 | 0.0308 | 0.0308 | 0.0463 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0387 | 0.0260 | 0.0260 | 0.0260 | 0.0391 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0425 | 0.0239 | 0.0239 | 0.0239 | 0.0358 |
| 7 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0313 | 0.0221 | 0.0221 | 0.0221 | 0.0331 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0315 | -0.0193 | -0.0193 | -0.0193 | 0.0289 |
| 9 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0687 | 0.0141 | 0.0141 | 0.0141 | 0.0212 |
| 10 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0361 | -0.0130 | -0.0130 | -0.0130 | 0.0195 |
| 11 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0398 | 0.0105 | 0.0105 | 0.0105 | 0.0158 |
| 12 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0548 | -0.0103 | -0.0103 | -0.0103 | 0.0155 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0252 | -0.0098 | -0.0098 | -0.0098 | 0.0147 |
| 14 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0514 | 0.0082 | 0.0082 | 0.0082 | 0.0123 |
| 15 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0440 | 0.0078 | 0.0078 | 0.0078 | 0.0118 |
| 16 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0420 | 0.0076 | 0.0076 | 0.0076 | 0.0114 |
| 17 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0358 | 0.0067 | 0.0067 | 0.0067 | 0.0100 |
| 18 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0385 | 0.0066 | 0.0066 | 0.0066 | 0.0099 |
| 19 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0217 | -0.0064 | -0.0064 | -0.0064 | 0.0096 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0376 | -0.0058 | -0.0058 | -0.0058 | 0.0087 |
| 21 | mod.cls_blocks.0.attn.h3 | photon<-neutral_hadron | 0.0432 | -0.0056 | -0.0056 | -0.0056 | 0.0084 |
| 22 | mod.cls_blocks.0.attn.h2 | photon<-electron | 0.0829 | -0.0055 | -0.0055 | -0.0055 | 0.0083 |
| 23 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0368 | 0.0054 | 0.0054 | 0.0054 | 0.0081 |
| 24 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0198 | 0.0054 | 0.0054 | 0.0054 | 0.0081 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0442 | 0.0053 | 0.0053 | 0.0053 | 0.0079 |
| 26 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-charged_hadron | 0.0339 | -0.0052 | -0.0052 | -0.0052 | 0.0079 |
| 27 | mod.cls_blocks.0.attn.h2 | photon<-neutral_hadron | 0.0423 | -0.0051 | -0.0051 | -0.0051 | 0.0077 |
| 28 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0367 | -0.0050 | -0.0050 | -0.0050 | 0.0075 |
| 29 | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0417 | -0.0042 | -0.0042 | -0.0042 | 0.0063 |
| 30 | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0581 | -0.0039 | -0.0039 | -0.0039 | 0.0059 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
