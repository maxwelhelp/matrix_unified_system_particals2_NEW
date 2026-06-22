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
| 1 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.4709 | 0.6265 | 332.9103 | 2.786e-04 |
| 2 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.4649 | 0.5621 | 265.7897 | 1.357e-04 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.3889 | 0.4003 | 38.7420 | 0.1065 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.2112 | 0.8547 | 102.9025 | 9.365e-04 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.3310 | 0.3344 | 127.5447 | 0.0445 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.1245 | 1.0935 | 132.6346 | 0.0025 |
| 7 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.1261 | 1.0837 | 129.8747 | 0.0023 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.3153 | 0.3153 | 128.2821 | 0.0435 |
| 9 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.2353 | 0.4677 | 321.1511 | 2.547e-04 |
| 10 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0570 | 1.1642 | 126.7027 | 0.0023 |
| 11 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0570 | 1.1642 | 131.5431 | 0.0025 |
| 12 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1558 | 0.5328 | 102.6035 | 8.118e-04 |
| 13 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.1210 | 0.6000 | 133.5150 | 0.0022 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.2074 | 0.2096 | 42.8085 | 0.1084 |
| 15 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.1696 | 0.3078 | 159.8869 | 2.875e-04 |
| 16 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1359 | 0.4348 | 103.9320 | 0.0017 |
| 17 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1320 | 0.3880 | 88.0831 | 7.448e-04 |
| 18 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.1266 | 0.4013 | 124.2668 | 0.0015 |
| 19 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0623 | 0.6206 | 130.5544 | 0.0020 |
| 20 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.1322 | 0.3113 | 203.0070 | 6.319e-04 |
| 21 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.1246 | 0.3292 | 155.9810 | 0.0011 |
| 22 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0777 | 0.4484 | 114.1249 | 0.0019 |
| 23 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0767 | 0.4385 | 111.6639 | 0.0018 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1489 | 0.1489 | 44.2736 | 0.0862 |
| 25 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0158 | 0.6501 | 127.3505 | 0.0019 |
| 26 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0158 | 0.6501 | 132.0635 | 0.0022 |
| 27 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.1021 | 0.2880 | 203.5704 | 6.089e-04 |
| 28 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.1021 | 0.2880 | 195.9488 | 5.522e-04 |
| 29 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0816 | 0.3642 | 90.8134 | 6.657e-04 |
| 30 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0874 | 0.3262 | 155.4918 | 9.789e-04 |
| 31 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0874 | 0.3262 | 149.7463 | 8.867e-04 |
| 32 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.1336 | 0.1336 | 140.9990 | 0.0415 |
| 33 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0457 | 0.4782 | 114.1341 | 0.0019 |
| 34 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0457 | 0.4782 | 109.7153 | 0.0017 |
| 35 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0489 | 0.4504 | 101.5469 | 0.0015 |
| 36 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0489 | 0.4504 | 103.6475 | 0.0017 |
| 37 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0777 | 0.2659 | 122.1807 | 4.294e-04 |
| 38 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0389 | 0.4016 | 102.5737 | 0.0016 |
| 39 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0211 | 0.3719 | 123.5013 | 0.0013 |
| 40 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0211 | 0.3719 | 120.0757 | 0.0012 |
| 41 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0327 | 0.2988 | 153.5558 | 0.0010 |
| 42 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.0081 | 0.3872 | 328.2527 | 2.629e-04 |
| 43 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.0081 | 0.3872 | 320.8513 | 2.415e-04 |
| 44 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0070 | 0.3792 | 123.1596 | 0.0013 |
| 45 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0050 | 0.2993 | 100.3251 | 5.629e-04 |
| 46 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 1.019e-04 | 0.3111 | 208.3810 | 6.607e-04 |
| 47 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0404 | 0.0764 | 139.0508 | 0.0423 |
| 48 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0404 | 0.0764 | 139.0508 | 0.0423 |
| 49 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0334 | 0.0734 | 41.0827 | 0.0924 |
| 50 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0334 | 0.0734 | 41.0827 | 0.0924 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.3889 | 0.4003 | 38.7420 | 0.1065 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.3310 | 0.3344 | 127.5447 | 0.0445 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.3153 | 0.3153 | 128.2821 | 0.0435 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.2074 | 0.2096 | 42.8085 | 0.1084 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1489 | 0.1489 | 44.2736 | 0.0862 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.1336 | 0.1336 | 140.9990 | 0.0415 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0404 | 0.0764 | 139.0508 | 0.0423 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0404 | 0.0764 | 139.0508 | 0.0423 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0334 | 0.0734 | 41.0827 | 0.0924 |
| 10 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0334 | 0.0734 | 41.0827 | 0.0924 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.4640 | 0.4640 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.3894 | 0.4097 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.3928 | 0.3928 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.3889 | 0.4003 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.3898 | 0.3898 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | electron | -0.3728 | 0.3728 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.3682 | 0.3682 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.3659 | 0.3659 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.3310 | 0.3344 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.3186 | 0.3186 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.3160 | 0.3160 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.3153 | 0.3153 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.3094 | 0.3156 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | electron | 0.2951 | 0.2951 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2578 | 0.2578 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.2368 | 0.2368 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.2167 | 0.2167 |
| 18 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.2118 | 0.2189 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.2074 | 0.2096 |
| 20 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.1906 | 0.1906 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | electron | 0.1816 | 0.1816 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.1717 | 0.1717 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.1676 | 0.1676 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1594 | 0.1594 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1489 | 0.1489 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.1477 | 0.1477 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.1358 | 0.1358 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.1336 | 0.1336 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1188 | 0.1188 |
| 30 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.1156 | 0.1156 |
| 31 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.1127 | 0.1127 |
| 32 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | electron | -0.1106 | 0.1106 |
| 33 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0820 | 0.1076 |
| 34 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0820 | 0.1076 |
| 35 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0557 | 0.0563 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0547 | 0.0547 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0547 | 0.0547 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0432 | 0.0926 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0432 | 0.0926 |
| 40 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0404 | 0.0764 |
| 41 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0404 | 0.0764 |
| 42 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0334 | 0.0734 |
| 43 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0334 | 0.0734 |
| 44 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0372 | 0.0460 |
| 45 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0372 | 0.0460 |
| 46 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0362 | 0.0362 |
| 47 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0276 | 0.0549 |
| 48 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0234 | 0.0686 |
| 49 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0234 | 0.0686 |
| 50 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | -0.0293 | 0.0354 |
| 51 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0214 | 0.0447 |
| 52 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0249 | 0.0281 |
| 53 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0222 | 0.0344 |
| 54 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0244 | 0.0253 |
| 55 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0142 | 0.0536 |
| 56 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.0187 | 0.0315 |
| 57 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0190 | 0.0247 |
| 58 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0199 | 0.0204 |
| 59 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -0.0161 | 0.0287 |
| 60 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0181 | 0.0207 |
| 61 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | 0.0113 | 0.0402 |
| 62 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | -0.0150 | 0.0231 |
| 63 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0160 | 0.0176 |
| 64 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0143 | 0.0241 |
| 65 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0117 | 0.0338 |
| 66 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0150 | 0.0197 |
| 67 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0098 | 0.0373 |
| 68 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0098 | 0.0373 |
| 69 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0140 | 0.0194 |
| 70 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0145 | 0.0169 |
| 71 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0147 | 0.0147 |
| 72 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0131 | 0.0182 |
| 73 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0131 | 0.0182 |
| 74 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | 0.0125 | 0.0171 |
| 75 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | 0.0098 | 0.0268 |
| 76 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0013 | 0.0588 |
| 77 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0013 | 0.0588 |
| 78 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | 0.0104 | 0.0211 |
| 79 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0114 | 0.0165 |
| 80 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | 0.0120 | 0.0125 |
| 81 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0115 | 0.0126 |
| 82 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0078 | 0.0257 |
| 83 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0111 | 0.0113 |
| 84 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0111 | 0.0113 |
| 85 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | 0.0073 | 0.0261 |
| 86 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | photon | 0.0109 | 0.0114 |
| 87 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0090 | 0.0133 |
| 88 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | 0.0045 | 0.0295 |
| 89 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | 0.0045 | 0.0295 |
| 90 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0085 | 0.0134 |
| 91 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0085 | 0.0134 |
| 92 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0042 | 0.0304 |
| 93 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0042 | 0.0304 |
| 94 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0075 | 0.0162 |
| 95 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0075 | 0.0162 |
| 96 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0071 | 0.0167 |
| 97 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | electron | -0.0065 | 0.0163 |
| 98 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | neutral_hadron | 0.0084 | 0.0085 |
| 99 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0027 | 0.0308 |
| 100 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0075 | 0.0116 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
