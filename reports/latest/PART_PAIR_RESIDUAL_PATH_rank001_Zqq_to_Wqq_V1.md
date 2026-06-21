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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.0509 | 0.3052 | 96.9171 | 3.485e-04 |
| 2 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.0641 | 0.1476 | 97.6289 | 2.781e-04 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.0490 | 0.1909 | 109.6585 | 4.683e-04 |
| 4 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0671 | 0.0985 | 93.6346 | 1.585e-04 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.0730 | 0.0730 | 154.6844 | 0.0134 |
| 6 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0586 | 0.1282 | 81.9046 | 2.428e-04 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.0719 | 0.0719 | 50.8918 | 0.0233 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0496 | 0.1457 | 124.0694 | 6.455e-04 |
| 9 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0148 | 0.2778 | 123.1086 | 8.088e-04 |
| 10 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0497 | 0.1086 | 85.9040 | 1.939e-04 |
| 11 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0535 | 0.0866 | 115.1937 | 1.266e-04 |
| 12 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0425 | 0.0952 | 117.1576 | 3.750e-04 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0518 | 0.0518 | 49.9678 | 0.0243 |
| 14 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0518 | 0.0518 | 49.9678 | 0.0243 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0518 | 0.0518 | 150.2727 | 0.0139 |
| 16 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0518 | 0.0518 | 150.2727 | 0.0139 |
| 17 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0091 | 0.2107 | 123.3049 | 6.661e-04 |
| 18 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0091 | 0.2107 | 95.6847 | 2.238e-04 |
| 19 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.0307 | 0.1229 | 255.3485 | 5.768e-05 |
| 20 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0403 | 0.0778 | 147.1492 | 2.927e-04 |
| 21 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0271 | 0.1116 | 99.9206 | 4.600e-04 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.0422 | 0.0452 | 149.6900 | 0.0139 |
| 23 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0355 | 0.0613 | 90.4747 | 1.059e-04 |
| 24 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0355 | 0.0613 | 113.9872 | 3.136e-04 |
| 25 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | 0.0293 | 0.0556 | 104.1436 | 2.127e-04 |
| 26 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0130 | 0.1170 | 306.0089 | 1.324e-04 |
| 27 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0182 | 0.0881 | 110.1591 | 3.631e-04 |
| 28 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0269 | 0.0510 | 146.0381 | 2.507e-04 |
| 29 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0269 | 0.0510 | 112.4233 | 8.478e-05 |
| 30 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0110 | 0.1109 | 104.7446 | 5.633e-04 |
| 31 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0248 | 0.0540 | 192.1471 | 1.717e-04 |
| 32 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0248 | 0.0540 | 145.2558 | 5.828e-05 |
| 33 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0266 | 0.0452 | 170.6172 | 1.188e-04 |
| 34 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0163 | 0.0793 | 301.4136 | 1.132e-04 |
| 35 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0163 | 0.0793 | 253.2079 | 3.870e-05 |
| 36 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.0163 | 0.0741 | 277.6694 | 7.953e-05 |
| 37 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | 0.0208 | 0.0500 | 131.9218 | 1.740e-04 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.0225 | 0.0367 | 49.7953 | 0.0284 |
| 39 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0121 | 0.0783 | 104.3361 | 4.624e-04 |
| 40 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0121 | 0.0783 | 79.1737 | 1.556e-04 |
| 41 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0026 | 0.1002 | 124.6596 | 5.341e-04 |
| 42 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0026 | 0.1002 | 95.5170 | 1.796e-04 |
| 43 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0071 | 0.0734 | 148.8833 | 8.668e-05 |
| 44 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | -0.0062 | 0.0619 | 191.5438 | 1.989e-04 |
| 45 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | 0.0021 | 0.0660 | 93.7459 | 2.517e-04 |
| 46 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0026 | 0.0604 | 93.7209 | 3.075e-04 |
| 47 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0022 | 0.0596 | 83.7074 | 1.285e-04 |
| 48 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0022 | 0.0596 | 97.0384 | 3.813e-04 |
| 49 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0097 | 0.0256 | 162.5002 | 0.0128 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | -0.0030 | 0.0272 | 52.8696 | 0.0245 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.0730 | 0.0730 | 154.6844 | 0.0134 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.0719 | 0.0719 | 50.8918 | 0.0233 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0518 | 0.0518 | 49.9678 | 0.0243 |
| 4 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0518 | 0.0518 | 49.9678 | 0.0243 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0518 | 0.0518 | 150.2727 | 0.0139 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0518 | 0.0518 | 150.2727 | 0.0139 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.0422 | 0.0452 | 149.6900 | 0.0139 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.0225 | 0.0367 | 49.7953 | 0.0284 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0097 | 0.0256 | 162.5002 | 0.0128 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | -0.0030 | 0.0272 | 52.8696 | 0.0245 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.0917 | 0.0917 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.0899 | 0.0899 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.0774 | 0.0774 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.0730 | 0.0730 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.0719 | 0.0719 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.0703 | 0.0703 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.0682 | 0.0682 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.0664 | 0.0664 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.0654 | 0.0654 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0622 | 0.0622 |
| 11 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0622 | 0.0622 |
| 12 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.0619 | 0.0619 |
| 13 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -0.0609 | 0.0609 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0580 | 0.0580 |
| 15 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0580 | 0.0580 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0539 | 0.0539 |
| 17 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0539 | 0.0539 |
| 18 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0533 | 0.0533 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0518 | 0.0518 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0518 | 0.0518 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0518 | 0.0518 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0518 | 0.0518 |
| 23 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0433 | 0.0530 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0445 | 0.0445 |
| 25 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0445 | 0.0445 |
| 26 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.0422 | 0.0452 |
| 27 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0422 | 0.0422 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0422 | 0.0422 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.0417 | 0.0430 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.0403 | 0.0437 |
| 31 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0407 | 0.0407 |
| 32 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0368 | 0.0499 |
| 33 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.0369 | 0.0420 |
| 34 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0356 | 0.0453 |
| 35 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0350 | 0.0350 |
| 36 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0344 | 0.0344 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.0320 | 0.0418 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0331 | 0.0331 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0331 | 0.0331 |
| 40 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0282 | 0.0282 |
| 41 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0276 | 0.0276 |
| 42 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0271 | 0.0271 |
| 43 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.0206 | 0.0466 |
| 44 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | -0.0256 | 0.0256 |
| 45 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.0225 | 0.0367 |
| 46 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0245 | 0.0245 |
| 47 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0223 | 0.0299 |
| 48 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0237 | 0.0240 |
| 49 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0223 | 0.0244 |
| 50 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0222 | 0.0222 |
| 51 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0204 | 0.0204 |
| 52 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.0170 | 0.0298 |
| 53 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | 0.0161 | 0.0249 |
| 54 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0131 | 0.0271 |
| 55 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0155 | 0.0155 |
| 56 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0129 | 0.0151 |
| 57 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0131 | 0.0131 |
| 58 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0131 | 0.0131 |
| 59 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0097 | 0.0256 |
| 60 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | 0.0116 | 0.0178 |
| 61 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0123 | 0.0123 |
| 62 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | 0.0121 | 0.0121 |
| 63 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | 0.0114 | 0.0130 |
| 64 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0097 | 0.0190 |
| 65 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0110 | 0.0110 |
| 66 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0070 | 0.0177 |
| 67 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0091 | 0.0091 |
| 68 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0091 | 0.0091 |
| 69 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | 0.0089 | 0.0089 |
| 70 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0045 | 0.0235 |
| 71 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0080 | 0.0080 |
| 72 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | -0.0030 | 0.0272 |
| 73 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0070 | 0.0072 |
| 74 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0070 | 0.0072 |
| 75 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | -0.0067 | 0.0083 |
| 76 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | -0.0067 | 0.0083 |
| 77 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0066 | 0.0066 |
| 78 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0064 | 0.0064 |
| 79 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0062 | 0.0062 |
| 80 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0051 | 0.0093 |
| 81 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0051 | 0.0093 |
| 82 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | neutral_hadron | -0.0041 | 0.0080 |
| 83 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0035 | 0.0076 |
| 84 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0039 | 0.0039 |
| 85 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0037 | 0.0037 |
| 86 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0037 | 0.0037 |
| 87 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | neutral_hadron | -0.0028 | 0.0069 |
| 88 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | -0.0033 | 0.0049 |
| 89 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0032 | 0.0049 |
| 90 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0032 | 0.0049 |
| 91 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0032 | 0.0042 |
| 92 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | 0.0031 | 0.0042 |
| 93 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | 4.253e-04 | 0.0142 |
| 94 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | photon | -0.0031 | 0.0032 |
| 95 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0030 | 0.0030 |
| 96 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | charged_hadron | -0.0028 | 0.0029 |
| 97 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0025 | 0.0037 |
| 98 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0025 | 0.0037 |
| 99 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | 0.0027 | 0.0027 |
| 100 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | 0.0027 | 0.0027 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
