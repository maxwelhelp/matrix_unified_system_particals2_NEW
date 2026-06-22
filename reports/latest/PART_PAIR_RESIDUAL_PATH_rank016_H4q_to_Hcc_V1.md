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
| 1 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.5307 | 0.6005 | 308.2119 | 4.094e-04 |
| 2 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.3130 | 0.8740 | 105.1566 | 8.017e-04 |
| 3 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.3850 | 0.4610 | 274.1963 | 8.345e-05 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.2595 | 0.7605 | 131.1386 | 0.0023 |
| 5 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.2054 | 0.8068 | 134.1524 | 0.0017 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.2898 | 0.2898 | 124.1126 | 0.0426 |
| 7 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.2032 | 0.4884 | 104.3027 | 7.168e-04 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.1899 | 0.4820 | 132.0454 | 0.0021 |
| 9 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1643 | 0.3216 | 317.3239 | 1.743e-04 |
| 10 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.1322 | 0.4478 | 136.0375 | 0.0016 |
| 11 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1649 | 0.3161 | 104.0169 | 0.0018 |
| 12 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1422 | 0.3532 | 87.7783 | 6.606e-04 |
| 13 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1348 | 0.3200 | 113.4441 | 0.0020 |
| 14 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.1513 | 0.2383 | 156.8574 | 0.0012 |
| 15 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.1181 | 0.3560 | 88.5099 | 5.880e-04 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.1645 | 0.1645 | 144.6764 | 0.0374 |
| 17 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1188 | 0.3239 | 298.5582 | 1.934e-04 |
| 18 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1188 | 0.3239 | 289.9858 | 1.733e-04 |
| 19 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0036 | 0.7323 | 122.8743 | 0.0015 |
| 20 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0036 | 0.7323 | 128.0609 | 0.0017 |
| 21 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.1101 | 0.2858 | 123.2512 | 0.0015 |
| 22 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.1099 | 0.2705 | 206.9739 | 8.345e-04 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1374 | 0.1548 | 39.0524 | 0.1091 |
| 24 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0757 | 0.3422 | 113.5256 | 0.0014 |
| 25 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0936 | 0.2603 | 101.1694 | 4.971e-04 |
| 26 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0354 | 0.4436 | 128.4535 | 0.0015 |
| 27 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0354 | 0.4436 | 122.8354 | 0.0014 |
| 28 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0756 | 0.2457 | 119.2143 | 0.0011 |
| 29 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0756 | 0.2457 | 114.9363 | 9.713e-04 |
| 30 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0732 | 0.2259 | 150.3903 | 8.277e-04 |
| 31 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0732 | 0.2259 | 143.6403 | 7.448e-04 |
| 32 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0461 | 0.3158 | 105.2112 | 0.0013 |
| 33 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0461 | 0.3158 | 109.8352 | 0.0014 |
| 34 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.0885 | 0.1058 | 45.6220 | 0.0734 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0864 | 0.0864 | 153.3764 | 0.0362 |
| 36 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0864 | 0.0864 | 153.3764 | 0.0362 |
| 37 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0311 | 0.2756 | 96.6094 | 0.0011 |
| 38 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0311 | 0.2756 | 99.1125 | 0.0013 |
| 39 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0224 | 0.2771 | 102.4695 | 0.0013 |
| 40 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0716 | 0.0743 | 153.7455 | 0.0360 |
| 41 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0383 | 0.2006 | 208.5625 | 5.054e-04 |
| 42 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0363 | 0.1944 | 160.7478 | 2.418e-04 |
| 43 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0300 | 0.2072 | 157.2104 | 8.077e-04 |
| 44 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0299 | 0.1951 | 195.4355 | 5.244e-04 |
| 45 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0299 | 0.1951 | 186.6688 | 4.708e-04 |
| 46 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0177 | 0.2333 | 121.6363 | 3.855e-04 |
| 47 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0016 | 0.2705 | 124.7977 | 0.0011 |
| 48 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0487 | 0.0657 | 45.1070 | 0.0693 |
| 49 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0487 | 0.0657 | 45.1070 | 0.0693 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0469 | 0.0612 | 45.9582 | 0.0678 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.2898 | 0.2898 | 124.1126 | 0.0426 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.1645 | 0.1645 | 144.6764 | 0.0374 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1374 | 0.1548 | 39.0524 | 0.1091 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.0885 | 0.1058 | 45.6220 | 0.0734 |
| 5 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0864 | 0.0864 | 153.3764 | 0.0362 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0864 | 0.0864 | 153.3764 | 0.0362 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0716 | 0.0743 | 153.7455 | 0.0360 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0487 | 0.0657 | 45.1070 | 0.0693 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0487 | 0.0657 | 45.1070 | 0.0693 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0469 | 0.0612 | 45.9582 | 0.0678 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.3015 | 0.3015 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.2974 | 0.2974 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.2909 | 0.2909 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.2898 | 0.2898 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.2545 | 0.2545 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.2042 | 0.2042 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.1946 | 0.1946 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.1700 | 0.1700 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1607 | 0.1878 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.1645 | 0.1645 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.1519 | 0.1519 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1374 | 0.1548 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1151 | 0.1151 |
| 14 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1151 | 0.1151 |
| 15 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1091 | 0.1091 |
| 16 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.1014 | 0.1014 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.0963 | 0.1031 |
| 18 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.0885 | 0.1058 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.0850 | 0.1158 |
| 20 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0910 | 0.0910 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0888 | 0.0888 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0865 | 0.0865 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0865 | 0.0865 |
| 24 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0864 | 0.0864 |
| 25 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0864 | 0.0864 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0853 | 0.0853 |
| 27 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0853 | 0.0853 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0716 | 0.0743 |
| 29 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.0713 | 0.0713 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0671 | 0.0671 |
| 31 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0671 | 0.0671 |
| 32 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0644 | 0.0674 |
| 33 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | 0.0640 | 0.0640 |
| 34 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0629 | 0.0629 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0600 | 0.0714 |
| 36 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0600 | 0.0714 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0529 | 0.0661 |
| 38 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0527 | 0.0527 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0487 | 0.0657 |
| 40 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0487 | 0.0657 |
| 41 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0469 | 0.0612 |
| 42 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | 0.0495 | 0.0495 |
| 43 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | 0.0456 | 0.0456 |
| 44 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0441 | 0.0441 |
| 45 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0438 | 0.0438 |
| 46 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | 0.0421 | 0.0421 |
| 47 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0413 | 0.0413 |
| 48 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | -0.0337 | 0.0337 |
| 49 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0230 | 0.0702 |
| 50 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | 0.0320 | 0.0320 |
| 51 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0303 | 0.0384 |
| 52 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0303 | 0.0384 |
| 53 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | 0.0292 | 0.0292 |
| 54 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0255 | 0.0317 |
| 55 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0255 | 0.0317 |
| 56 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0252 | 0.0252 |
| 57 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0248 | 0.0248 |
| 58 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0196 | 0.0421 |
| 59 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0233 | 0.0233 |
| 60 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0233 | 0.0233 |
| 61 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0206 | 0.0206 |
| 62 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0130 | 0.0469 |
| 63 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0130 | 0.0469 |
| 64 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0178 | 0.0200 |
| 65 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0176 | 0.0201 |
| 66 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0159 | 0.0222 |
| 67 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0125 | 0.0339 |
| 68 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0125 | 0.0339 |
| 69 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.0163 | 0.0163 |
| 70 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | -0.0155 | 0.0184 |
| 71 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | photon | 0.0153 | 0.0153 |
| 72 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | -0.0147 | 0.0147 |
| 73 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | -0.0138 | 0.0138 |
| 74 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0098 | 0.0275 |
| 75 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | -0.0119 | 0.0167 |
| 76 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0032 | 0.0513 |
| 77 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | neutral_hadron | 0.0116 | 0.0168 |
| 78 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0091 | 0.0245 |
| 79 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0091 | 0.0245 |
| 80 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0118 | 0.0118 |
| 81 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0117 | 0.0124 |
| 82 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | -0.0108 | 0.0141 |
| 83 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0108 | 0.0119 |
| 84 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0108 | 0.0119 |
| 85 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0109 | 0.0109 |
| 86 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0102 | 0.0139 |
| 87 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0106 | 0.0106 |
| 88 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0101 | 0.0116 |
| 89 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | 0.0092 | 0.0146 |
| 90 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0090 | 0.0143 |
| 91 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0090 | 0.0143 |
| 92 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0099 | 0.0099 |
| 93 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0072 | 0.0201 |
| 94 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0072 | 0.0201 |
| 95 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0092 | 0.0092 |
| 96 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0092 | 0.0092 |
| 97 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -1.688e-04 | 0.0442 |
| 98 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -1.687e-04 | 0.0442 |
| 99 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | 0.0080 | 0.0127 |
| 100 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | photon | -0.0084 | 0.0099 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
