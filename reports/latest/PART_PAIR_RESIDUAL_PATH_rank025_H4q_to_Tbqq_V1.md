# PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2

Residual path composition trace with correct CLS-block residual capture. Particle blocks use residual `x`; CLS blocks use residual `x_cls`. Contribution is `dot(block_out - residual_in, dJ/dblock_out)`.

- events: **64**
- rows: **800**
- summary_rows: **50**
- kind_rows: `{'particle': 640, 'cls': 160}`
- missed_rows: **0**

## Top residual block contributions
| rank | objective | module | kind | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | 0.4287 | 1.2159 | 123.6040 | 0.0018 |
| 2 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | 0.4287 | 1.2159 | 128.2694 | 0.0021 |
| 3 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.4968 | 0.5766 | 274.1963 | 1.094e-04 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.3755 | 0.9391 | 105.1566 | 9.085e-04 |
| 5 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.3371 | 0.6255 | 332.9103 | 3.503e-04 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.2436 | 0.9549 | 128.4531 | 0.0020 |
| 7 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | 0.1498 | 1.2447 | 132.6346 | 0.0029 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.3577 | 0.3577 | 127.5447 | 0.0456 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.3189 | 0.3189 | 38.7420 | 0.1306 |
| 10 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.2474 | 0.5705 | 104.3027 | 7.973e-04 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2763 | 0.2763 | 144.6764 | 0.0406 |
| 12 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.2052 | 0.4052 | 306.4897 | 2.257e-04 |
| 13 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.1335 | 0.6370 | 122.4306 | 0.0016 |
| 14 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.1335 | 0.6370 | 127.1936 | 0.0018 |
| 15 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.1910 | 0.2923 | 160.7478 | 2.759e-04 |
| 16 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.1467 | 0.3569 | 155.9810 | 0.0012 |
| 17 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.1048 | 0.5120 | 128.6718 | 0.0017 |
| 18 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.1612 | 0.2514 | 196.4252 | 5.335e-04 |
| 19 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1014 | 0.4775 | 103.9320 | 0.0019 |
| 20 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.1133 | 0.4129 | 124.2668 | 0.0016 |
| 21 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1139 | 0.3610 | 87.7783 | 7.250e-04 |
| 22 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.1029 | 0.3673 | 88.5099 | 6.415e-04 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.1539 | 0.1582 | 45.6220 | 0.0937 |
| 24 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0571 | 0.5199 | 114.1249 | 0.0022 |
| 25 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.1109 | 0.3010 | 144.3360 | 7.355e-04 |
| 26 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.1109 | 0.3010 | 149.9954 | 8.281e-04 |
| 27 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | 0.0203 | 0.6611 | 133.5150 | 0.0025 |
| 28 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.1042 | 0.3035 | 118.8386 | 0.0011 |
| 29 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.1025 | 0.2590 | 198.5050 | 5.129e-04 |
| 30 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.1025 | 0.2590 | 190.7745 | 4.555e-04 |
| 31 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.1003 | 0.2621 | 149.5976 | 8.186e-04 |
| 32 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0564 | 0.4158 | 97.6073 | 0.0012 |
| 33 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0564 | 0.4158 | 100.0924 | 0.0014 |
| 34 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0631 | 0.3574 | 116.7244 | 9.994e-04 |
| 35 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0631 | 0.3574 | 120.2768 | 0.0011 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1190 | 0.1279 | 150.3860 | 0.0403 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1190 | 0.1279 | 150.3860 | 0.0403 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1117 | 0.1148 | 45.5560 | 0.0833 |
| 39 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0621 | 0.2900 | 101.1694 | 5.444e-04 |
| 40 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0182 | 0.4511 | 104.8204 | 0.0014 |
| 41 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0182 | 0.4511 | 108.9611 | 0.0015 |
| 42 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0362 | 0.3689 | 109.3751 | 0.0015 |
| 43 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0964 | 0.1008 | 158.6289 | 0.0383 |
| 44 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.0092 | 0.3975 | 317.2992 | 2.039e-04 |
| 45 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.0092 | 0.3975 | 310.1294 | 1.823e-04 |
| 46 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0243 | 0.3244 | 99.2469 | 0.0013 |
| 47 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0422 | 0.2434 | 121.6363 | 4.235e-04 |
| 48 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0718 | 0.0975 | 42.8363 | 0.0874 |
| 49 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0718 | 0.0975 | 42.8363 | 0.0874 |
| 50 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | -8.503e-04 | 0.3422 | 208.3810 | 7.403e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.3577 | 0.3577 | 127.5447 | 0.0456 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.3189 | 0.3189 | 38.7420 | 0.1306 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2763 | 0.2763 | 144.6764 | 0.0406 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.1539 | 0.1582 | 45.6220 | 0.0937 |
| 5 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1190 | 0.1279 | 150.3860 | 0.0403 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1190 | 0.1279 | 150.3860 | 0.0403 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1117 | 0.1148 | 45.5560 | 0.0833 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0964 | 0.1008 | 158.6289 | 0.0383 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0718 | 0.0975 | 42.8363 | 0.0874 |
| 10 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0718 | 0.0975 | 42.8363 | 0.0874 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.4770 | 0.4770 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.4580 | 0.4580 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.3812 | 0.3812 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.3577 | 0.3577 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.3317 | 0.3317 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.3235 | 0.3235 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.3208 | 0.3208 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.3189 | 0.3189 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.3176 | 0.3176 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.3040 | 0.3040 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.3031 | 0.3031 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.2870 | 0.2870 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2763 | 0.2763 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2531 | 0.2531 |
| 15 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.2028 | 0.2028 |
| 16 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1604 | 0.1604 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1604 | 0.1604 |
| 18 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.1539 | 0.1582 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1479 | 0.1529 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1405 | 0.1405 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1405 | 0.1405 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1307 | 0.1368 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.1267 | 0.1267 |
| 24 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1190 | 0.1279 |
| 25 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1190 | 0.1279 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.1154 | 0.1154 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1117 | 0.1148 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1091 | 0.1091 |
| 29 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1002 | 0.1063 |
| 30 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1002 | 0.1063 |
| 31 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.1005 | 0.1005 |
| 32 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0964 | 0.1008 |
| 33 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0861 | 0.0861 |
| 34 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0861 | 0.0861 |
| 35 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0808 | 0.0933 |
| 36 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0718 | 0.0975 |
| 37 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0718 | 0.0975 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0733 | 0.0911 |
| 39 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0704 | 0.0704 |
| 40 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0694 | 0.0694 |
| 41 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0613 | 0.0791 |
| 42 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0590 | 0.0590 |
| 43 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0590 | 0.0590 |
| 44 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0508 | 0.0641 |
| 45 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0469 | 0.0519 |
| 46 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0469 | 0.0519 |
| 47 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0418 | 0.0725 |
| 48 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0418 | 0.0725 |
| 49 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | 0.0442 | 0.0442 |
| 50 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | 0.0439 | 0.0439 |
| 51 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | 0.0429 | 0.0429 |
| 52 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | -0.0428 | 0.0428 |
| 53 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0424 | 0.0424 |
| 54 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0424 | 0.0424 |
| 55 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0371 | 0.0510 |
| 56 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | 0.0377 | 0.0472 |
| 57 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0390 | 0.0411 |
| 58 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0382 | 0.0382 |
| 59 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0365 | 0.0365 |
| 60 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | 0.0330 | 0.0330 |
| 61 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0320 | 0.0320 |
| 62 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0320 | 0.0320 |
| 63 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0299 | 0.0299 |
| 64 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0299 | 0.0299 |
| 65 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | 0.0289 | 0.0289 |
| 66 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | 0.0288 | 0.0288 |
| 67 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0266 | 0.0375 |
| 68 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0266 | 0.0375 |
| 69 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0270 | 0.0340 |
| 70 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | -0.0200 | 0.0576 |
| 71 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0263 | 0.0322 |
| 72 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | 0.0251 | 0.0299 |
| 73 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | 0.0260 | 0.0260 |
| 74 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | 0.0248 | 0.0248 |
| 75 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0024 | 0.1014 |
| 76 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0124 | 0.0599 |
| 77 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0124 | 0.0599 |
| 78 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0206 | 0.0257 |
| 79 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0206 | 0.0257 |
| 80 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | 0.0213 | 0.0213 |
| 81 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0180 | 0.0180 |
| 82 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0180 | 0.0180 |
| 83 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | -0.0114 | 0.0383 |
| 84 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0087 | 0.0439 |
| 85 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | 0.0126 | 0.0284 |
| 86 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | 0.0143 | 0.0209 |
| 87 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0130 | 0.0231 |
| 88 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0130 | 0.0231 |
| 89 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0094 | 0.0336 |
| 90 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0018 | 0.0619 |
| 91 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0136 | 0.0136 |
| 92 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0116 | 0.0213 |
| 93 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | -0.0084 | 0.0309 |
| 94 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | neutral_hadron | 0.0118 | 0.0169 |
| 95 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0101 | 0.0207 |
| 96 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0101 | 0.0207 |
| 97 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0109 | 0.0119 |
| 98 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0090 | 0.0191 |
| 99 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0098 | 0.0098 |
| 100 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0098 | 0.0098 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
