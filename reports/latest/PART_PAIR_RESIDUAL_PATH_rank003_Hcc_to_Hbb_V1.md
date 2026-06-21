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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.3035 | 1.0712 | 129.3170 | 0.0024 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.3846 | 0.3846 | 39.0524 | 0.0711 |
| 3 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.3343 | 0.4976 | 308.4886 | 2.277e-04 |
| 4 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.3155 | 0.4405 | 256.5644 | 9.637e-05 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.3190 | 0.3190 | 42.8085 | 0.0672 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.1999 | 0.7828 | 132.3806 | 0.0021 |
| 7 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.1847 | 0.8133 | 99.4952 | 8.104e-04 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.2120 | 0.6430 | 131.1054 | 0.0021 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2804 | 0.2804 | 124.1126 | 0.0330 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.2506 | 0.2506 | 128.2821 | 0.0312 |
| 11 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1826 | 0.5101 | 98.9359 | 7.166e-04 |
| 12 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1828 | 0.4974 | 112.7470 | 0.0020 |
| 13 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1424 | 0.4425 | 103.5501 | 0.0017 |
| 14 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0315 | 0.8757 | 129.6011 | 0.0021 |
| 15 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0315 | 0.8757 | 123.3446 | 0.0019 |
| 16 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1461 | 0.3519 | 282.9436 | 1.880e-04 |
| 17 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1461 | 0.3519 | 292.0854 | 2.106e-04 |
| 18 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.1157 | 0.4491 | 132.6596 | 0.0019 |
| 19 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1309 | 0.3631 | 317.4253 | 2.315e-04 |
| 20 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.1372 | 0.2827 | 154.4873 | 2.156e-04 |
| 21 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.1283 | 0.3073 | 203.8861 | 5.678e-04 |
| 22 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1185 | 0.3450 | 83.2890 | 6.663e-04 |
| 23 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0949 | 0.3252 | 123.1559 | 0.0013 |
| 24 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0373 | 0.4618 | 130.3783 | 0.0018 |
| 25 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0373 | 0.4618 | 123.1697 | 0.0016 |
| 26 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0636 | 0.3450 | 114.2163 | 0.0017 |
| 27 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0924 | 0.2175 | 117.8791 | 3.545e-04 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1137 | 0.1137 | 42.6181 | 0.0569 |
| 29 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1137 | 0.1137 | 42.6181 | 0.0569 |
| 30 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0659 | 0.2950 | 88.8183 | 5.655e-04 |
| 31 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0740 | 0.2302 | 206.3274 | 5.474e-04 |
| 32 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0759 | 0.2008 | 157.6639 | 9.143e-04 |
| 33 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0554 | 0.2788 | 115.1313 | 9.727e-04 |
| 34 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0554 | 0.2788 | 120.9396 | 0.0011 |
| 35 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0999 | 0.0999 | 139.8983 | 0.0295 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0999 | 0.0999 | 139.8983 | 0.0295 |
| 37 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0556 | 0.2678 | 155.5532 | 9.829e-04 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0865 | 0.0973 | 43.1525 | 0.0570 |
| 39 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0337 | 0.3042 | 103.7723 | 0.0015 |
| 40 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0248 | 0.3204 | 97.9310 | 0.0012 |
| 41 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0248 | 0.3204 | 100.8078 | 0.0014 |
| 42 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0757 | 0.0864 | 142.8148 | 0.0289 |
| 43 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0013 | 0.3246 | 110.4072 | 0.0017 |
| 44 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0013 | 0.3246 | 104.5327 | 0.0015 |
| 45 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0315 | 0.1931 | 184.1699 | 4.383e-04 |
| 46 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0315 | 0.1931 | 195.7695 | 4.915e-04 |
| 47 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | 0.0101 | 0.2389 | 97.1721 | 4.728e-04 |
| 48 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0015 | 0.2451 | 123.8143 | 0.0012 |
| 49 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0077 | 0.2069 | 151.9624 | 8.128e-04 |
| 50 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0077 | 0.2069 | 143.6877 | 7.234e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.3846 | 0.3846 | 39.0524 | 0.0711 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.3190 | 0.3190 | 42.8085 | 0.0672 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2804 | 0.2804 | 124.1126 | 0.0330 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.2506 | 0.2506 | 128.2821 | 0.0312 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1137 | 0.1137 | 42.6181 | 0.0569 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1137 | 0.1137 | 42.6181 | 0.0569 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0999 | 0.0999 | 139.8983 | 0.0295 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0999 | 0.0999 | 139.8983 | 0.0295 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0865 | 0.0973 | 43.1525 | 0.0570 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0757 | 0.0864 | 142.8148 | 0.0289 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.4231 | 0.4231 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.4046 | 0.4046 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | electron | 0.3906 | 0.3906 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.3890 | 0.3890 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.3855 | 0.3855 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.3846 | 0.3846 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.3638 | 0.3638 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.3190 | 0.3190 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | electron | -0.3141 | 0.3141 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.3124 | 0.3124 |
| 11 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.3042 | 0.3042 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.2985 | 0.2985 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2931 | 0.2931 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.2839 | 0.2839 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2804 | 0.2804 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2766 | 0.2766 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.2531 | 0.2531 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.2506 | 0.2506 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | 0.2436 | 0.2436 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | 0.2436 | 0.2436 |
| 21 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.2260 | 0.2260 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.2260 | 0.2260 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.2219 | 0.2219 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.2118 | 0.2118 |
| 25 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | 0.1260 | 0.1260 |
| 26 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | 0.1260 | 0.1260 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.1180 | 0.1180 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1152 | 0.1152 |
| 29 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1152 | 0.1152 |
| 30 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1137 | 0.1137 |
| 31 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1137 | 0.1137 |
| 32 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.1078 | 0.1078 |
| 33 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.1078 | 0.1078 |
| 34 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1037 | 0.1037 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1037 | 0.1037 |
| 36 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1009 | 0.1009 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0999 | 0.0999 |
| 38 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0999 | 0.0999 |
| 39 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.0962 | 0.0962 |
| 40 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0940 | 0.0940 |
| 41 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0940 | 0.0940 |
| 42 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0937 | 0.0937 |
| 43 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0865 | 0.0973 |
| 44 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0868 | 0.0868 |
| 45 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0868 | 0.0868 |
| 46 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0861 | 0.0861 |
| 47 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | 0.0848 | 0.0848 |
| 48 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | 0.0848 | 0.0848 |
| 49 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0831 | 0.0831 |
| 50 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0831 | 0.0831 |
| 51 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0790 | 0.0842 |
| 52 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0773 | 0.0878 |
| 53 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0788 | 0.0812 |
| 54 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0750 | 0.0926 |
| 55 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0784 | 0.0784 |
| 56 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0784 | 0.0784 |
| 57 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0757 | 0.0864 |
| 58 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0672 | 0.0826 |
| 59 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0648 | 0.0648 |
| 60 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0596 | 0.0741 |
| 61 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0600 | 0.0600 |
| 62 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0579 | 0.0579 |
| 63 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0469 | 0.0496 |
| 64 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0470 | 0.0470 |
| 65 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0470 | 0.0470 |
| 66 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0465 | 0.0465 |
| 67 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0443 | 0.0443 |
| 68 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0428 | 0.0438 |
| 69 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0424 | 0.0424 |
| 70 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0424 | 0.0424 |
| 71 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0423 | 0.0423 |
| 72 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | 0.0308 | 0.0840 |
| 73 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0410 | 0.0410 |
| 74 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0394 | 0.0394 |
| 75 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0353 | 0.0543 |
| 76 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0364 | 0.0430 |
| 77 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0364 | 0.0430 |
| 78 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0345 | 0.0490 |
| 79 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0345 | 0.0490 |
| 80 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0289 | 0.0617 |
| 81 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0289 | 0.0617 |
| 82 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0286 | 0.0551 |
| 83 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0335 | 0.0335 |
| 84 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0319 | 0.0323 |
| 85 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0320 | 0.0320 |
| 86 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0289 | 0.0441 |
| 87 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0289 | 0.0441 |
| 88 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0316 | 0.0316 |
| 89 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | -0.0306 | 0.0306 |
| 90 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0300 | 0.0300 |
| 91 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0287 | 0.0303 |
| 92 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0254 | 0.0415 |
| 93 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0230 | 0.0325 |
| 94 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0243 | 0.0243 |
| 95 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0159 | 0.0548 |
| 96 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0236 | 0.0236 |
| 97 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0170 | 0.0492 |
| 98 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0170 | 0.0492 |
| 99 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0212 | 0.0305 |
| 100 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | 0.0227 | 0.0227 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
