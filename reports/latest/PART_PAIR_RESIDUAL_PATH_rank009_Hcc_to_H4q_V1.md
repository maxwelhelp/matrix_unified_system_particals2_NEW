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
| 1 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.5307 | 0.6005 | 256.5644 | 1.306e-04 |
| 2 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.3130 | 0.8740 | 130.7757 | 0.0018 |
| 3 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.3850 | 0.4610 | 329.9815 | 1.852e-04 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.2595 | 0.7605 | 99.4952 | 7.464e-04 |
| 5 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.2054 | 0.8068 | 134.1524 | 0.0017 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.2054 | 0.8068 | 125.5492 | 0.0014 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2898 | 0.2898 | 124.1126 | 0.0426 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.2032 | 0.4884 | 131.1759 | 0.0016 |
| 9 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1899 | 0.4820 | 98.9359 | 6.793e-04 |
| 10 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1643 | 0.3216 | 317.3239 | 1.743e-04 |
| 11 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1643 | 0.3216 | 302.9353 | 1.430e-04 |
| 12 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.1322 | 0.4478 | 136.0375 | 0.0016 |
| 13 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.1322 | 0.4478 | 126.8288 | 0.0013 |
| 14 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.1649 | 0.3161 | 88.8183 | 5.687e-04 |
| 15 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1422 | 0.3532 | 110.9378 | 0.0015 |
| 16 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1348 | 0.3200 | 83.2890 | 6.421e-04 |
| 17 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.1513 | 0.2383 | 117.8791 | 3.884e-04 |
| 18 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1181 | 0.3560 | 102.4834 | 0.0013 |
| 19 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.1645 | 0.1645 | 144.6764 | 0.0374 |
| 20 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1188 | 0.3239 | 298.5582 | 1.934e-04 |
| 21 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0036 | 0.7323 | 128.0609 | 0.0017 |
| 22 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.1101 | 0.2858 | 97.1721 | 4.871e-04 |
| 23 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.1099 | 0.2705 | 154.4873 | 2.670e-04 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.1374 | 0.1548 | 39.0524 | 0.1091 |
| 25 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0757 | 0.3422 | 105.8164 | 0.0012 |
| 26 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0757 | 0.3422 | 113.5256 | 0.0014 |
| 27 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0936 | 0.2603 | 123.5911 | 0.0011 |
| 28 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0354 | 0.4436 | 128.4535 | 0.0015 |
| 29 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0756 | 0.2457 | 119.2143 | 0.0011 |
| 30 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0732 | 0.2259 | 150.3903 | 8.277e-04 |
| 31 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0461 | 0.3158 | 109.8352 | 0.0014 |
| 32 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.0885 | 0.1058 | 45.6220 | 0.0734 |
| 33 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0864 | 0.0864 | 153.3764 | 0.0362 |
| 34 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0311 | 0.2756 | 99.1125 | 0.0013 |
| 35 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0224 | 0.2771 | 102.4695 | 0.0013 |
| 36 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0224 | 0.2771 | 98.3343 | 0.0010 |
| 37 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0716 | 0.0743 | 153.7455 | 0.0360 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0716 | 0.0743 | 153.7455 | 0.0360 |
| 39 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0383 | 0.2006 | 194.3354 | 4.173e-04 |
| 40 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0383 | 0.2006 | 208.5625 | 5.054e-04 |
| 41 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0363 | 0.1944 | 205.0604 | 5.418e-04 |
| 42 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0300 | 0.2072 | 146.9493 | 6.674e-04 |
| 43 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0300 | 0.2072 | 157.2104 | 8.077e-04 |
| 44 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | -0.0299 | 0.1951 | 195.4355 | 5.244e-04 |
| 45 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | 0.0177 | 0.2333 | 155.0080 | 8.610e-04 |
| 46 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0016 | 0.2705 | 117.6640 | 8.673e-04 |
| 47 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0016 | 0.2705 | 124.7977 | 0.0011 |
| 48 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0487 | 0.0657 | 45.1070 | 0.0693 |
| 49 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0469 | 0.0612 | 45.9582 | 0.0678 |
| 50 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0469 | 0.0612 | 45.9582 | 0.0678 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2898 | 0.2898 | 124.1126 | 0.0426 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.1645 | 0.1645 | 144.6764 | 0.0374 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.1374 | 0.1548 | 39.0524 | 0.1091 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.0885 | 0.1058 | 45.6220 | 0.0734 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0864 | 0.0864 | 153.3764 | 0.0362 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0716 | 0.0743 | 153.7455 | 0.0360 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0716 | 0.0743 | 153.7455 | 0.0360 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0487 | 0.0657 | 45.1070 | 0.0693 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0469 | 0.0612 | 45.9582 | 0.0678 |
| 10 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0469 | 0.0612 | 45.9582 | 0.0678 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.3015 | 0.3015 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2974 | 0.2974 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2909 | 0.2909 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2898 | 0.2898 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.2545 | 0.2545 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.2042 | 0.2042 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.1946 | 0.1946 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.1700 | 0.1700 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1607 | 0.1878 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.1645 | 0.1645 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.1519 | 0.1519 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.1374 | 0.1548 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.1151 | 0.1151 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1091 | 0.1091 |
| 15 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.1014 | 0.1014 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.0963 | 0.1031 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.0885 | 0.1058 |
| 18 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.0850 | 0.1158 |
| 19 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0910 | 0.0910 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0888 | 0.0888 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0888 | 0.0888 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0865 | 0.0865 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0864 | 0.0864 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0853 | 0.0853 |
| 25 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0716 | 0.0743 |
| 26 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0716 | 0.0743 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.0713 | 0.0713 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0671 | 0.0671 |
| 29 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0644 | 0.0674 |
| 30 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0644 | 0.0674 |
| 31 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | 0.0640 | 0.0640 |
| 32 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | 0.0629 | 0.0629 |
| 33 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0600 | 0.0714 |
| 34 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0529 | 0.0661 |
| 35 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0529 | 0.0661 |
| 36 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0527 | 0.0527 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0487 | 0.0657 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0469 | 0.0612 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0469 | 0.0612 |
| 40 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | 0.0495 | 0.0495 |
| 41 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | 0.0456 | 0.0456 |
| 42 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0441 | 0.0441 |
| 43 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0438 | 0.0438 |
| 44 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0421 | 0.0421 |
| 45 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0413 | 0.0413 |
| 46 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | -0.0337 | 0.0337 |
| 47 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0230 | 0.0702 |
| 48 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0230 | 0.0702 |
| 49 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | 0.0320 | 0.0320 |
| 50 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0303 | 0.0384 |
| 51 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | 0.0292 | 0.0292 |
| 52 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0255 | 0.0317 |
| 53 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0252 | 0.0252 |
| 54 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0248 | 0.0248 |
| 55 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0196 | 0.0421 |
| 56 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0196 | 0.0421 |
| 57 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0233 | 0.0233 |
| 58 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0206 | 0.0206 |
| 59 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0130 | 0.0469 |
| 60 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0178 | 0.0200 |
| 61 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0176 | 0.0201 |
| 62 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0159 | 0.0222 |
| 63 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.0125 | 0.0339 |
| 64 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.0163 | 0.0163 |
| 65 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | -0.0155 | 0.0184 |
| 66 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | photon | 0.0153 | 0.0153 |
| 67 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | -0.0147 | 0.0147 |
| 68 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0138 | 0.0138 |
| 69 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0138 | 0.0138 |
| 70 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0098 | 0.0275 |
| 71 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0119 | 0.0167 |
| 72 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0032 | 0.0513 |
| 73 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | neutral_hadron | 0.0116 | 0.0168 |
| 74 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0091 | 0.0245 |
| 75 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0118 | 0.0118 |
| 76 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0118 | 0.0118 |
| 77 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0117 | 0.0124 |
| 78 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0108 | 0.0141 |
| 79 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0108 | 0.0141 |
| 80 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0108 | 0.0119 |
| 81 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0109 | 0.0109 |
| 82 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0109 | 0.0109 |
| 83 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0102 | 0.0139 |
| 84 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0106 | 0.0106 |
| 85 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0101 | 0.0116 |
| 86 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | 0.0092 | 0.0146 |
| 87 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0090 | 0.0143 |
| 88 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0099 | 0.0099 |
| 89 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0099 | 0.0099 |
| 90 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | -0.0072 | 0.0201 |
| 91 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0092 | 0.0092 |
| 92 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -1.687e-04 | 0.0442 |
| 93 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | 0.0080 | 0.0127 |
| 94 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | photon | -0.0084 | 0.0099 |
| 95 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | -0.0075 | 0.0123 |
| 96 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | -0.0075 | 0.0123 |
| 97 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | neutral_hadron | -0.0082 | 0.0083 |
| 98 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | -0.0077 | 0.0077 |
| 99 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | neutral_hadron | 0.0071 | 0.0101 |
| 100 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0061 | 0.0126 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
