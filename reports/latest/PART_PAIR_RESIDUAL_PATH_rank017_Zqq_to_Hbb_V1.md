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
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.6011 | 0.6011 | 42.8085 | 0.0766 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.5244 | 0.5244 | 128.2821 | 0.0407 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2900 | 0.2928 | 149.6900 | 0.0348 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.2147 | 0.5771 | 96.9171 | 6.232e-04 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.2716 | 0.2843 | 49.7953 | 0.0665 |
| 6 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.2443 | 0.3440 | 255.3485 | 9.875e-05 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.2398 | 0.2398 | 47.3557 | 0.0683 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.2398 | 0.2398 | 47.3557 | 0.0683 |
| 9 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | 0.1030 | 0.6938 | 131.5680 | 0.0023 |
| 10 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | 0.1030 | 0.6938 | 122.8057 | 0.0019 |
| 11 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1730 | 0.3102 | 323.1997 | 3.669e-04 |
| 12 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.1593 | 0.3112 | 302.6402 | 3.203e-04 |
| 13 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.1593 | 0.3112 | 320.5069 | 3.782e-04 |
| 14 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1766 | 0.1766 | 147.3589 | 0.0362 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1766 | 0.1766 | 147.3589 | 0.0362 |
| 16 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1188 | 0.3329 | 97.6289 | 5.314e-04 |
| 17 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0372 | 0.6556 | 132.5052 | 0.0023 |
| 18 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1079 | 0.2662 | 81.9046 | 4.832e-04 |
| 19 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.1103 | 0.2158 | 117.2430 | 8.922e-04 |
| 20 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.1103 | 0.2158 | 124.7590 | 0.0011 |
| 21 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.1143 | 0.1721 | 148.8833 | 1.796e-04 |
| 22 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0891 | 0.2023 | 124.4124 | 0.0011 |
| 23 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.0263 | 0.4305 | 129.3170 | 0.0012 |
| 24 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0816 | 0.1863 | 146.3777 | 6.957e-04 |
| 25 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0816 | 0.1863 | 157.1609 | 8.673e-04 |
| 26 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0570 | 0.2716 | 104.4463 | 0.0013 |
| 27 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0570 | 0.2716 | 112.6574 | 0.0016 |
| 28 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.0262 | 0.3570 | 124.1259 | 0.0015 |
| 29 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.0262 | 0.3570 | 133.4100 | 0.0019 |
| 30 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0744 | 0.1536 | 208.8924 | 6.054e-04 |
| 31 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0590 | 0.1757 | 206.7696 | 6.088e-04 |
| 32 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0590 | 0.1757 | 192.0901 | 4.939e-04 |
| 33 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | 0.0522 | 0.1935 | 93.6346 | 3.462e-04 |
| 34 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | 0.0102 | 0.3584 | 134.6301 | 0.0019 |
| 35 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0440 | 0.2142 | 85.9040 | 4.117e-04 |
| 36 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0532 | 0.1659 | 159.1804 | 8.722e-04 |
| 37 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0257 | 0.2754 | 114.3159 | 0.0017 |
| 38 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0517 | 0.1704 | 115.1937 | 2.682e-04 |
| 39 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | 0.0461 | 0.1895 | 112.7470 | 8.285e-04 |
| 40 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0564 | 0.1050 | 154.9764 | 0.0342 |
| 41 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | -0.0506 | 0.1227 | 203.8861 | 3.239e-04 |
| 42 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | -0.0303 | 0.1993 | 308.4886 | 1.882e-04 |
| 43 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0252 | 0.2112 | 103.2396 | 0.0014 |
| 44 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0452 | 0.1171 | 155.5532 | 4.670e-04 |
| 45 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0402 | 0.1300 | 123.1559 | 6.051e-04 |
| 46 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -2.623e-04 | 0.2367 | 131.1054 | 9.560e-04 |
| 47 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0046 | 0.2174 | 99.9936 | 0.0011 |
| 48 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0046 | 0.2174 | 104.6476 | 0.0013 |
| 49 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0101 | 0.1634 | 103.5501 | 7.148e-04 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | -0.0070 | 0.1187 | 51.2860 | 0.0625 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.6011 | 0.6011 | 42.8085 | 0.0766 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.5244 | 0.5244 | 128.2821 | 0.0407 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2900 | 0.2928 | 149.6900 | 0.0348 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.2716 | 0.2843 | 49.7953 | 0.0665 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.2398 | 0.2398 | 47.3557 | 0.0683 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.2398 | 0.2398 | 47.3557 | 0.0683 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1766 | 0.1766 | 147.3589 | 0.0362 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1766 | 0.1766 | 147.3589 | 0.0362 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0564 | 0.1050 | 154.9764 | 0.0342 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | -0.0070 | 0.1187 | 51.2860 | 0.0625 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.8000 | 0.8000 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.7276 | 0.7276 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.6518 | 0.6518 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.6331 | 0.6331 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.6331 | 0.6331 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.6011 | 0.6011 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.5263 | 0.5263 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.5244 | 0.5244 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.5145 | 0.5145 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.4684 | 0.4684 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.4375 | 0.4375 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.4259 | 0.4259 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | electron | 0.3885 | 0.3885 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | muon | 0.3101 | 0.3101 |
| 15 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | muon | 0.3101 | 0.3101 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | electron | -0.2962 | 0.2962 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2900 | 0.2928 |
| 18 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.2716 | 0.2843 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.2678 | 0.2678 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.2678 | 0.2678 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.2668 | 0.2668 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.2636 | 0.2636 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.2636 | 0.2636 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2425 | 0.2425 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.2398 | 0.2398 |
| 26 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.2398 | 0.2398 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.2298 | 0.2298 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.2116 | 0.2116 |
| 29 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.2116 | 0.2116 |
| 30 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.2022 | 0.2022 |
| 31 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | electron | -0.1875 | 0.1875 |
| 32 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1822 | 0.1822 |
| 33 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1822 | 0.1822 |
| 34 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1766 | 0.1766 |
| 35 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1766 | 0.1766 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | muon | -0.1666 | 0.1666 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | muon | -0.1666 | 0.1666 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1127 | 0.1127 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1127 | 0.1127 |
| 40 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | -0.1016 | 0.1016 |
| 41 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0987 | 0.0987 |
| 42 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0987 | 0.0987 |
| 43 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0873 | 0.1292 |
| 44 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0664 | 0.0664 |
| 45 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0564 | 0.1050 |
| 46 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | -0.0534 | 0.0930 |
| 47 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | electron | 0.0598 | 0.0598 |
| 48 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0257 | 0.1281 |
| 49 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0460 | 0.0460 |
| 50 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | 0.0320 | 0.0417 |
| 51 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0217 | 0.0697 |
| 52 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0293 | 0.0346 |
| 53 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0293 | 0.0346 |
| 54 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | -0.0070 | 0.1187 |
| 55 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0266 | 0.0331 |
| 56 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0273 | 0.0273 |
| 57 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0106 | 0.0759 |
| 58 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | 0.0229 | 0.0229 |
| 59 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0118 | 0.0595 |
| 60 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | 0.0197 | 0.0253 |
| 61 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | 0.0193 | 0.0225 |
| 62 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | -0.0147 | 0.0391 |
| 63 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | 0.0192 | 0.0192 |
| 64 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0051 | 0.0701 |
| 65 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | 0.0173 | 0.0173 |
| 66 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0148 | 0.0173 |
| 67 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0148 | 0.0173 |
| 68 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0141 | 0.0182 |
| 69 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0145 | 0.0151 |
| 70 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0124 | 0.0232 |
| 71 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0124 | 0.0232 |
| 72 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0134 | 0.0150 |
| 73 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0134 | 0.0150 |
| 74 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | 0.0124 | 0.0174 |
| 75 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0131 | 0.0131 |
| 76 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0043 | 0.0480 |
| 77 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0088 | 0.0283 |
| 78 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0088 | 0.0283 |
| 79 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0125 | 0.0126 |
| 80 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0089 | 0.0250 |
| 81 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0089 | 0.0250 |
| 82 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | 0.0038 | 0.0440 |
| 83 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0113 | 0.0135 |
| 84 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0113 | 0.0135 |
| 85 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | 0.0106 | 0.0162 |
| 86 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0113 | 0.0113 |
| 87 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0104 | 0.0146 |
| 88 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0071 | 0.0268 |
| 89 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0071 | 0.0268 |
| 90 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | -0.0101 | 0.0113 |
| 91 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0099 | 0.0121 |
| 92 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0081 | 0.0186 |
| 93 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | 0.0011 | 0.0457 |
| 94 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | 0.0011 | 0.0457 |
| 95 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0080 | 0.0178 |
| 96 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0029 | 0.0378 |
| 97 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | neutral_hadron | -0.0078 | 0.0171 |
| 98 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0091 | 0.0105 |
| 99 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0091 | 0.0105 |
| 100 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0090 | 0.0090 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
