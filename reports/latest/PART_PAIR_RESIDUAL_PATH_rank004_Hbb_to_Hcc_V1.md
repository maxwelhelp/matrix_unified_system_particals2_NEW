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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.3035 | 1.0712 | 102.9025 | 0.0010 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.3846 | 0.3846 | 39.0524 | 0.0711 |
| 3 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.3343 | 0.4976 | 265.7897 | 9.902e-05 |
| 4 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.3155 | 0.4405 | 308.2119 | 3.003e-04 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.3190 | 0.3190 | 42.8085 | 0.0672 |
| 6 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.1999 | 0.7828 | 132.3806 | 0.0021 |
| 7 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.1999 | 0.7828 | 125.2337 | 0.0019 |
| 8 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.1847 | 0.8133 | 131.1386 | 0.0025 |
| 9 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.2120 | 0.6430 | 102.6035 | 9.259e-04 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.2804 | 0.2804 | 124.1126 | 0.0330 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2506 | 0.2506 | 128.2821 | 0.0312 |
| 12 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.1826 | 0.5101 | 132.0454 | 0.0022 |
| 13 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1828 | 0.4974 | 88.0831 | 8.700e-04 |
| 14 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.1424 | 0.4425 | 90.8134 | 7.351e-04 |
| 15 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0315 | 0.8757 | 129.6011 | 0.0021 |
| 16 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1461 | 0.3519 | 292.0854 | 2.106e-04 |
| 17 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.1157 | 0.4491 | 124.9753 | 0.0017 |
| 18 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.1157 | 0.4491 | 132.6596 | 0.0019 |
| 19 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1309 | 0.3631 | 317.4253 | 2.315e-04 |
| 20 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1309 | 0.3631 | 302.5776 | 2.027e-04 |
| 21 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.1372 | 0.2827 | 206.9739 | 6.770e-04 |
| 22 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.1283 | 0.3073 | 159.8869 | 2.466e-04 |
| 23 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1185 | 0.3450 | 113.4441 | 0.0021 |
| 24 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0949 | 0.3252 | 100.3251 | 5.824e-04 |
| 25 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0373 | 0.4618 | 130.3783 | 0.0018 |
| 26 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0636 | 0.3450 | 107.2521 | 0.0015 |
| 27 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0636 | 0.3450 | 114.2163 | 0.0017 |
| 28 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0924 | 0.2175 | 156.8574 | 0.0011 |
| 29 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1137 | 0.1137 | 42.6181 | 0.0569 |
| 30 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0659 | 0.2950 | 104.0169 | 0.0018 |
| 31 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0740 | 0.2302 | 206.3274 | 5.474e-04 |
| 32 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0740 | 0.2302 | 193.1919 | 4.821e-04 |
| 33 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0759 | 0.2008 | 148.2018 | 8.094e-04 |
| 34 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0759 | 0.2008 | 157.6639 | 9.143e-04 |
| 35 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0554 | 0.2788 | 120.9396 | 0.0011 |
| 36 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0999 | 0.0999 | 139.8983 | 0.0295 |
| 37 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0556 | 0.2678 | 122.1807 | 4.253e-04 |
| 38 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0865 | 0.0973 | 43.1525 | 0.0570 |
| 39 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0865 | 0.0973 | 43.1525 | 0.0570 |
| 40 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0337 | 0.3042 | 99.8773 | 0.0013 |
| 41 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0337 | 0.3042 | 103.7723 | 0.0015 |
| 42 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0248 | 0.3204 | 100.8078 | 0.0014 |
| 43 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0757 | 0.0864 | 142.8148 | 0.0289 |
| 44 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0757 | 0.0864 | 142.8148 | 0.0289 |
| 45 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | 0.0013 | 0.3246 | 110.4072 | 0.0017 |
| 46 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0315 | 0.1931 | 195.7695 | 4.915e-04 |
| 47 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | 0.0101 | 0.2389 | 123.2512 | 0.0015 |
| 48 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0015 | 0.2451 | 123.8143 | 0.0012 |
| 49 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0015 | 0.2451 | 117.2345 | 0.0011 |
| 50 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0077 | 0.2069 | 151.9624 | 8.128e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.3846 | 0.3846 | 39.0524 | 0.0711 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.3190 | 0.3190 | 42.8085 | 0.0672 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.2804 | 0.2804 | 124.1126 | 0.0330 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2506 | 0.2506 | 128.2821 | 0.0312 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1137 | 0.1137 | 42.6181 | 0.0569 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0999 | 0.0999 | 139.8983 | 0.0295 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0865 | 0.0973 | 43.1525 | 0.0570 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0865 | 0.0973 | 43.1525 | 0.0570 |
| 9 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0757 | 0.0864 | 142.8148 | 0.0289 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0757 | 0.0864 | 142.8148 | 0.0289 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.4231 | 0.4231 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.4046 | 0.4046 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | electron | 0.3906 | 0.3906 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.3890 | 0.3890 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.3855 | 0.3855 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.3846 | 0.3846 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.3638 | 0.3638 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.3190 | 0.3190 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | electron | -0.3141 | 0.3141 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.3124 | 0.3124 |
| 11 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.3042 | 0.3042 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2985 | 0.2985 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.2931 | 0.2931 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.2839 | 0.2839 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.2804 | 0.2804 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.2766 | 0.2766 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.2531 | 0.2531 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2506 | 0.2506 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | electron | 0.2436 | 0.2436 |
| 20 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | electron | -0.2260 | 0.2260 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.2219 | 0.2219 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.2118 | 0.2118 |
| 23 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | 0.1260 | 0.1260 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.1180 | 0.1180 |
| 25 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.1180 | 0.1180 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.1152 | 0.1152 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1137 | 0.1137 |
| 28 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.1078 | 0.1078 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.1037 | 0.1037 |
| 30 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1009 | 0.1009 |
| 31 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0999 | 0.0999 |
| 32 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.0962 | 0.0962 |
| 33 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0940 | 0.0940 |
| 34 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0937 | 0.0937 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0937 | 0.0937 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0865 | 0.0973 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0865 | 0.0973 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0868 | 0.0868 |
| 39 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0861 | 0.0861 |
| 40 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | 0.0848 | 0.0848 |
| 41 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0831 | 0.0831 |
| 42 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0790 | 0.0842 |
| 43 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0790 | 0.0842 |
| 44 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0773 | 0.0878 |
| 45 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0773 | 0.0878 |
| 46 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0788 | 0.0812 |
| 47 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0750 | 0.0926 |
| 48 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0750 | 0.0926 |
| 49 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0784 | 0.0784 |
| 50 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0757 | 0.0864 |
| 51 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0757 | 0.0864 |
| 52 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0672 | 0.0826 |
| 53 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0672 | 0.0826 |
| 54 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0648 | 0.0648 |
| 55 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0648 | 0.0648 |
| 56 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0596 | 0.0741 |
| 57 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0600 | 0.0600 |
| 58 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | 0.0579 | 0.0579 |
| 59 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0469 | 0.0496 |
| 60 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0470 | 0.0470 |
| 61 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0465 | 0.0465 |
| 62 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | 0.0443 | 0.0443 |
| 63 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0428 | 0.0438 |
| 64 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | 0.0424 | 0.0424 |
| 65 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0423 | 0.0423 |
| 66 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | 0.0308 | 0.0840 |
| 67 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0410 | 0.0410 |
| 68 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0394 | 0.0394 |
| 69 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0353 | 0.0543 |
| 70 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0364 | 0.0430 |
| 71 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0345 | 0.0490 |
| 72 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0289 | 0.0617 |
| 73 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0286 | 0.0551 |
| 74 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0335 | 0.0335 |
| 75 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0319 | 0.0323 |
| 76 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0320 | 0.0320 |
| 77 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0320 | 0.0320 |
| 78 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0289 | 0.0441 |
| 79 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0316 | 0.0316 |
| 80 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0316 | 0.0316 |
| 81 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0306 | 0.0306 |
| 82 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0300 | 0.0300 |
| 83 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0287 | 0.0303 |
| 84 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0254 | 0.0415 |
| 85 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0230 | 0.0325 |
| 86 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0243 | 0.0243 |
| 87 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0243 | 0.0243 |
| 88 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0159 | 0.0548 |
| 89 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0236 | 0.0236 |
| 90 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0236 | 0.0236 |
| 91 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | 0.0170 | 0.0492 |
| 92 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0212 | 0.0305 |
| 93 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0212 | 0.0305 |
| 94 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | 0.0227 | 0.0227 |
| 95 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0218 | 0.0244 |
| 96 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0218 | 0.0244 |
| 97 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | -0.0196 | 0.0301 |
| 98 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0200 | 0.0200 |
| 99 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0200 | 0.0200 |
| 100 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0195 | 0.0218 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
