# PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2

Residual path composition trace with correct CLS-block residual capture. Particle blocks use residual `x`; CLS blocks use residual `x_cls`. Contribution is `dot(block_out - residual_in, dJ/dblock_out)`.

- events: **96**
- rows: **1200**
- summary_rows: **50**
- kind_rows: `{'particle': 960, 'cls': 240}`
- missed_rows: **0**

## Top residual block contributions
| rank | objective | module | kind | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.0896 | 0.6205 | 101.4551 | 9.150e-04 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1531 | 0.1531 | 49.3893 | 0.0486 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.1010 | 0.3603 | 126.1736 | 0.0014 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.1498 | 0.1498 | 151.9818 | 0.0275 |
| 5 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.0960 | 0.3226 | 101.4515 | 7.427e-04 |
| 6 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.1149 | 0.2127 | 97.5726 | 4.316e-04 |
| 7 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0909 | 0.2595 | 86.0251 | 6.648e-04 |
| 8 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0944 | 0.2416 | 88.5918 | 5.416e-04 |
| 9 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0879 | 0.2590 | 130.2940 | 0.0014 |
| 10 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1181 | 0.1236 | 49.5645 | 0.0490 |
| 11 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1181 | 0.1236 | 49.5645 | 0.0490 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1181 | 0.1232 | 150.6837 | 0.0277 |
| 13 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1181 | 0.1232 | 150.6837 | 0.0277 |
| 14 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0108 | 0.5059 | 128.7371 | 0.0018 |
| 15 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0926 | 0.1706 | 120.6836 | 3.386e-04 |
| 16 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.0689 | 0.2619 | 263.5382 | 1.475e-04 |
| 17 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0293 | 0.3903 | 130.1997 | 0.0016 |
| 18 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0293 | 0.3903 | 130.1997 | 0.0016 |
| 19 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0759 | 0.1658 | 121.5561 | 8.119e-04 |
| 20 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0707 | 0.1373 | 154.4406 | 6.368e-04 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.0810 | 0.0874 | 149.9881 | 0.0278 |
| 22 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0473 | 0.1974 | 102.4148 | 9.903e-04 |
| 23 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0464 | 0.1743 | 126.2946 | 0.0011 |
| 24 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.0507 | 0.1511 | 306.1964 | 2.320e-04 |
| 25 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0474 | 0.1588 | 313.7739 | 2.538e-04 |
| 26 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0474 | 0.1588 | 313.7738 | 2.538e-04 |
| 27 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0333 | 0.1996 | 110.2122 | 0.0012 |
| 28 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0511 | 0.1215 | 120.3932 | 7.429e-04 |
| 29 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0511 | 0.1215 | 120.3932 | 7.429e-04 |
| 30 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0520 | 0.0982 | 196.5475 | 3.656e-04 |
| 31 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | 0.0477 | 0.1014 | 118.2988 | 6.634e-04 |
| 32 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0186 | 0.2083 | 314.8766 | 2.948e-04 |
| 33 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0430 | 0.0982 | 203.2092 | 4.038e-04 |
| 34 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0430 | 0.0982 | 203.2092 | 4.038e-04 |
| 35 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0146 | 0.1972 | 131.6497 | 0.0013 |
| 36 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0146 | 0.1972 | 131.6497 | 0.0013 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.0463 | 0.0693 | 49.6516 | 0.0567 |
| 38 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0357 | 0.0974 | 154.3033 | 5.984e-04 |
| 39 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0357 | 0.0974 | 154.3033 | 5.984e-04 |
| 40 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | 0.0346 | 0.0933 | 151.8852 | 5.410e-04 |
| 41 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0092 | 0.1579 | 111.1076 | 0.0011 |
| 42 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0092 | 0.1579 | 111.1076 | 0.0011 |
| 43 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0105 | 0.1293 | 108.9585 | 9.710e-04 |
| 44 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | -0.0150 | 0.1085 | 200.3411 | 4.387e-04 |
| 45 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0030 | 0.1543 | 156.1949 | 2.271e-04 |
| 46 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0056 | 0.1310 | 101.2531 | 9.091e-04 |
| 47 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0056 | 0.1310 | 101.2531 | 9.091e-04 |
| 48 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0021 | 0.1290 | 101.8949 | 7.962e-04 |
| 49 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0211 | 0.0472 | 163.3513 | 0.0254 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0014 | 0.0469 | 52.8654 | 0.0484 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1531 | 0.1531 | 49.3893 | 0.0486 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.1498 | 0.1498 | 151.9818 | 0.0275 |
| 3 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1181 | 0.1236 | 49.5645 | 0.0490 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1181 | 0.1236 | 49.5645 | 0.0490 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1181 | 0.1232 | 150.6837 | 0.0277 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1181 | 0.1232 | 150.6837 | 0.0277 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.0810 | 0.0874 | 149.9881 | 0.0278 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.0463 | 0.0693 | 49.6516 | 0.0567 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0211 | 0.0472 | 163.3513 | 0.0254 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0014 | 0.0469 | 52.8654 | 0.0484 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1772 | 0.1772 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.1704 | 0.1704 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1640 | 0.1640 |
| 4 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1640 | 0.1640 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.1547 | 0.1547 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1531 | 0.1531 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1527 | 0.1527 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1505 | 0.1505 |
| 9 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1505 | 0.1505 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.1498 | 0.1498 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.1488 | 0.1488 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.1328 | 0.1328 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.1308 | 0.1308 |
| 14 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.1239 | 0.1239 |
| 15 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -0.1218 | 0.1218 |
| 16 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1181 | 0.1236 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1181 | 0.1236 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1181 | 0.1232 |
| 19 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1181 | 0.1232 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.1180 | 0.1180 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.1180 | 0.1180 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1057 | 0.1178 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1057 | 0.1178 |
| 24 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.1066 | 0.1066 |
| 25 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1006 | 0.1116 |
| 26 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1006 | 0.1116 |
| 27 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0982 | 0.0982 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0982 | 0.0982 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.0924 | 0.0944 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.0877 | 0.0934 |
| 31 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0871 | 0.0871 |
| 32 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0871 | 0.0871 |
| 33 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0843 | 0.0843 |
| 34 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0842 | 0.0842 |
| 35 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0842 | 0.0842 |
| 36 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.0810 | 0.0874 |
| 37 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0813 | 0.0813 |
| 38 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0785 | 0.0914 |
| 39 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0736 | 0.0999 |
| 40 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0707 | 0.0837 |
| 41 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.0698 | 0.0748 |
| 42 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0687 | 0.0687 |
| 43 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0673 | 0.0673 |
| 44 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.0589 | 0.0757 |
| 45 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0571 | 0.0571 |
| 46 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0571 | 0.0571 |
| 47 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.0534 | 0.0717 |
| 48 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0546 | 0.0546 |
| 49 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0546 | 0.0546 |
| 50 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0526 | 0.0526 |
| 51 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.0465 | 0.0725 |
| 52 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.0463 | 0.0693 |
| 53 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | electron | -0.0482 | 0.0482 |
| 54 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0472 | 0.0472 |
| 55 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0460 | 0.0515 |
| 56 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0466 | 0.0466 |
| 57 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0439 | 0.0472 |
| 58 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0408 | 0.0408 |
| 59 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0406 | 0.0407 |
| 60 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0335 | 0.0531 |
| 61 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0364 | 0.0364 |
| 62 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0364 | 0.0364 |
| 63 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | 0.0321 | 0.0498 |
| 64 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0324 | 0.0324 |
| 65 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0263 | 0.0542 |
| 66 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | electron | 0.0298 | 0.0298 |
| 67 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0239 | 0.0501 |
| 68 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0211 | 0.0472 |
| 69 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | -0.0258 | 0.0258 |
| 70 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | 0.0233 | 0.0357 |
| 71 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0252 | 0.0252 |
| 72 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0252 | 0.0252 |
| 73 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0231 | 0.0231 |
| 74 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0231 | 0.0231 |
| 75 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0212 | 0.0212 |
| 76 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0191 | 0.0191 |
| 77 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0183 | 0.0221 |
| 78 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0139 | 0.0354 |
| 79 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0089 | 0.0469 |
| 80 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | -0.0160 | 0.0182 |
| 81 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0161 | 0.0164 |
| 82 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0126 | 0.0268 |
| 83 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | 0.0122 | 0.0275 |
| 84 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0149 | 0.0149 |
| 85 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0149 | 0.0149 |
| 86 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0144 | 0.0144 |
| 87 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0115 | 0.0232 |
| 88 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0133 | 0.0133 |
| 89 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0065 | 0.0378 |
| 90 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0128 | 0.0128 |
| 91 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0104 | 0.0151 |
| 92 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0014 | 0.0469 |
| 93 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0099 | 0.0099 |
| 94 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | 0.0069 | 0.0173 |
| 95 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0047 | 0.0156 |
| 96 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0047 | 0.0156 |
| 97 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0068 | 0.0069 |
| 98 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0061 | 0.0089 |
| 99 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | neutral_hadron | -0.0043 | 0.0160 |
| 100 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0058 | 0.0099 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
