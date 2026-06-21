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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.0509 | 0.3052 | 109.3575 | 5.819e-04 |
| 2 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0641 | 0.1476 | 110.8567 | 4.651e-04 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.0490 | 0.1909 | 94.5161 | 2.258e-04 |
| 4 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0671 | 0.0985 | 103.5043 | 2.649e-04 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.0730 | 0.0730 | 154.6844 | 0.0134 |
| 6 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0586 | 0.1282 | 92.9688 | 4.073e-04 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.0719 | 0.0719 | 50.8918 | 0.0233 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0496 | 0.1457 | 98.5786 | 2.656e-04 |
| 9 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0496 | 0.1457 | 124.0694 | 6.455e-04 |
| 10 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0148 | 0.2778 | 98.0278 | 3.325e-04 |
| 11 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0148 | 0.2778 | 123.1086 | 8.088e-04 |
| 12 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0497 | 0.1086 | 91.3037 | 3.233e-04 |
| 13 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0535 | 0.0866 | 130.4167 | 2.131e-04 |
| 14 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0425 | 0.0952 | 95.2063 | 1.547e-04 |
| 15 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0425 | 0.0952 | 117.1576 | 3.750e-04 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0518 | 0.0518 | 49.9678 | 0.0243 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0518 | 0.0518 | 150.2727 | 0.0139 |
| 18 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0091 | 0.2107 | 123.3049 | 6.661e-04 |
| 19 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.0307 | 0.1229 | 274.4041 | 9.386e-05 |
| 20 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0403 | 0.0778 | 116.0411 | 1.209e-04 |
| 21 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0403 | 0.0778 | 147.1492 | 2.927e-04 |
| 22 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0271 | 0.1116 | 87.2930 | 1.894e-04 |
| 23 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0271 | 0.1116 | 99.9206 | 4.600e-04 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.0422 | 0.0452 | 149.6900 | 0.0139 |
| 25 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0355 | 0.0613 | 113.9872 | 3.136e-04 |
| 26 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | 0.0293 | 0.0556 | 90.9540 | 1.022e-04 |
| 27 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0130 | 0.1170 | 260.4911 | 5.501e-05 |
| 28 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0130 | 0.1170 | 306.0089 | 1.324e-04 |
| 29 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.0182 | 0.0881 | 94.6646 | 1.758e-04 |
| 30 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0269 | 0.0510 | 146.0381 | 2.507e-04 |
| 31 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0110 | 0.1109 | 82.5500 | 2.316e-04 |
| 32 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0110 | 0.1109 | 104.7446 | 5.633e-04 |
| 33 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0248 | 0.0540 | 192.1471 | 1.717e-04 |
| 34 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0266 | 0.0452 | 146.1505 | 5.672e-05 |
| 35 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0163 | 0.0793 | 301.4136 | 1.132e-04 |
| 36 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.0163 | 0.0741 | 252.6327 | 3.801e-05 |
| 37 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0208 | 0.0500 | 113.3917 | 8.297e-05 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.0225 | 0.0367 | 49.7953 | 0.0284 |
| 39 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | 0.0121 | 0.0783 | 104.3361 | 4.624e-04 |
| 40 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0026 | 0.1002 | 124.6596 | 5.341e-04 |
| 41 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0071 | 0.0734 | 169.9788 | 1.446e-04 |
| 42 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0062 | 0.0619 | 191.5438 | 1.989e-04 |
| 43 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0062 | 0.0619 | 150.8156 | 8.235e-05 |
| 44 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | 0.0021 | 0.0660 | 86.0507 | 1.227e-04 |
| 45 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0026 | 0.0604 | 79.0092 | 1.511e-04 |
| 46 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0022 | 0.0596 | 97.0384 | 3.813e-04 |
| 47 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0097 | 0.0256 | 162.5002 | 0.0128 |
| 48 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0097 | 0.0256 | 162.5002 | 0.0128 |
| 49 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | -0.0030 | 0.0272 | 52.8696 | 0.0245 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | -0.0030 | 0.0272 | 52.8696 | 0.0245 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.0730 | 0.0730 | 154.6844 | 0.0134 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.0719 | 0.0719 | 50.8918 | 0.0233 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0518 | 0.0518 | 49.9678 | 0.0243 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0518 | 0.0518 | 150.2727 | 0.0139 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.0422 | 0.0452 | 149.6900 | 0.0139 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.0225 | 0.0367 | 49.7953 | 0.0284 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0097 | 0.0256 | 162.5002 | 0.0128 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0097 | 0.0256 | 162.5002 | 0.0128 |
| 9 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | -0.0030 | 0.0272 | 52.8696 | 0.0245 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | -0.0030 | 0.0272 | 52.8696 | 0.0245 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.0917 | 0.0917 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.0899 | 0.0899 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.0774 | 0.0774 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.0730 | 0.0730 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.0719 | 0.0719 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.0703 | 0.0703 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.0682 | 0.0682 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.0664 | 0.0664 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.0654 | 0.0654 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0622 | 0.0622 |
| 11 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0619 | 0.0619 |
| 12 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0619 | 0.0619 |
| 13 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0609 | 0.0609 |
| 14 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0609 | 0.0609 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0580 | 0.0580 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0539 | 0.0539 |
| 17 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0533 | 0.0533 |
| 18 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0533 | 0.0533 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0518 | 0.0518 |
| 20 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0518 | 0.0518 |
| 21 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0433 | 0.0530 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0445 | 0.0445 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.0422 | 0.0452 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0422 | 0.0422 |
| 25 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.0417 | 0.0430 |
| 26 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.0403 | 0.0437 |
| 27 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0407 | 0.0407 |
| 28 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0407 | 0.0407 |
| 29 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0368 | 0.0499 |
| 30 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0368 | 0.0499 |
| 31 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.0369 | 0.0420 |
| 32 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0356 | 0.0453 |
| 33 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0350 | 0.0350 |
| 34 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0350 | 0.0350 |
| 35 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0344 | 0.0344 |
| 36 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0344 | 0.0344 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.0320 | 0.0418 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0331 | 0.0331 |
| 39 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0282 | 0.0282 |
| 40 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | 0.0276 | 0.0276 |
| 41 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0271 | 0.0271 |
| 42 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.0206 | 0.0466 |
| 43 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0256 | 0.0256 |
| 44 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0256 | 0.0256 |
| 45 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.0225 | 0.0367 |
| 46 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0245 | 0.0245 |
| 47 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0223 | 0.0299 |
| 48 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0223 | 0.0299 |
| 49 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0237 | 0.0240 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0223 | 0.0244 |
| 51 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0223 | 0.0244 |
| 52 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0222 | 0.0222 |
| 53 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0204 | 0.0204 |
| 54 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0204 | 0.0204 |
| 55 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.0170 | 0.0298 |
| 56 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0161 | 0.0249 |
| 57 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0161 | 0.0249 |
| 58 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0131 | 0.0271 |
| 59 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0131 | 0.0271 |
| 60 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0155 | 0.0155 |
| 61 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0129 | 0.0151 |
| 62 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0131 | 0.0131 |
| 63 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0097 | 0.0256 |
| 64 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0097 | 0.0256 |
| 65 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | 0.0116 | 0.0178 |
| 66 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | 0.0116 | 0.0178 |
| 67 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0123 | 0.0123 |
| 68 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | 0.0121 | 0.0121 |
| 69 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | 0.0121 | 0.0121 |
| 70 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | 0.0114 | 0.0130 |
| 71 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0097 | 0.0190 |
| 72 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0097 | 0.0190 |
| 73 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | -0.0110 | 0.0110 |
| 74 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0070 | 0.0177 |
| 75 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0070 | 0.0177 |
| 76 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | 0.0091 | 0.0091 |
| 77 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0089 | 0.0089 |
| 78 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0045 | 0.0235 |
| 79 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0045 | 0.0235 |
| 80 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0080 | 0.0080 |
| 81 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | -0.0030 | 0.0272 |
| 82 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | -0.0030 | 0.0272 |
| 83 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | 0.0070 | 0.0072 |
| 84 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | -0.0067 | 0.0083 |
| 85 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0066 | 0.0066 |
| 86 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0066 | 0.0066 |
| 87 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0064 | 0.0064 |
| 88 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0064 | 0.0064 |
| 89 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | 0.0062 | 0.0062 |
| 90 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | neutral_hadron | 0.0051 | 0.0093 |
| 91 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | neutral_hadron | -0.0041 | 0.0080 |
| 92 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0035 | 0.0076 |
| 93 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0039 | 0.0039 |
| 94 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0037 | 0.0037 |
| 95 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | -0.0028 | 0.0069 |
| 96 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | -0.0028 | 0.0069 |
| 97 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | -0.0033 | 0.0049 |
| 98 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0032 | 0.0049 |
| 99 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0032 | 0.0042 |
| 100 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | 0.0031 | 0.0042 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
