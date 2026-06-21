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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.2374 | 0.7070 | 130.7757 | 0.0015 |
| 2 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.3015 | 0.3960 | 329.9815 | 1.850e-04 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | 0.1715 | 0.6267 | 128.8689 | 0.0011 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.1118 | 0.7491 | 128.6094 | 0.0013 |
| 5 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.1118 | 0.7491 | 135.5131 | 0.0015 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2128 | 0.2128 | 153.6730 | 0.0320 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.1995 | 0.2037 | 144.6764 | 0.0336 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.1437 | 0.4081 | 131.1759 | 0.0014 |
| 9 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.1587 | 0.3268 | 262.8722 | 8.746e-05 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1779 | 0.1816 | 45.6220 | 0.0683 |
| 11 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | 0.0272 | 0.6769 | 108.9801 | 7.364e-04 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.1453 | 0.1467 | 47.8338 | 0.0645 |
| 13 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1004 | 0.3103 | 110.9378 | 0.0013 |
| 14 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0756 | 0.3962 | 129.8082 | 0.0012 |
| 15 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0756 | 0.3962 | 136.7783 | 0.0013 |
| 16 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | 0.0717 | 0.3908 | 130.3340 | 9.962e-04 |
| 17 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0925 | 0.2875 | 102.4834 | 0.0011 |
| 18 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0663 | 0.2744 | 309.6137 | 1.559e-04 |
| 19 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0663 | 0.2744 | 296.8859 | 1.351e-04 |
| 20 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0708 | 0.2380 | 123.5911 | 9.847e-04 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0890 | 0.0890 | 158.1797 | 0.0314 |
| 22 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0348 | 0.2667 | 104.0659 | 0.0011 |
| 23 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0348 | 0.2667 | 100.4124 | 9.430e-04 |
| 24 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -3.985e-05 | 0.4002 | 109.8403 | 6.641e-04 |
| 25 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0277 | 0.2854 | 291.4487 | 1.300e-04 |
| 26 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0487 | 0.2005 | 155.0080 | 7.884e-04 |
| 27 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | 0.0246 | 0.2614 | 109.0722 | 9.065e-04 |
| 28 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0222 | 0.2709 | 88.6964 | 5.348e-04 |
| 29 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0206 | 0.2735 | 91.8748 | 6.064e-04 |
| 30 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0185 | 0.2771 | 115.3753 | 0.0012 |
| 31 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0185 | 0.2771 | 109.1709 | 0.0011 |
| 32 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0301 | 0.2210 | 101.7508 | 4.453e-04 |
| 33 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0149 | 0.2442 | 98.6859 | 8.048e-04 |
| 34 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0204 | 0.2181 | 121.0214 | 7.859e-04 |
| 35 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0204 | 0.2181 | 126.8770 | 8.991e-04 |
| 36 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0539 | 0.0705 | 48.0475 | 0.0601 |
| 37 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0245 | 0.1704 | 161.8836 | 2.180e-04 |
| 38 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | -0.0222 | 0.1616 | 194.9959 | 3.346e-04 |
| 39 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0148 | 0.1680 | 122.9819 | 3.354e-04 |
| 40 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0122 | 0.1684 | 195.8855 | 3.909e-04 |
| 41 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0122 | 0.1684 | 207.7472 | 4.494e-04 |
| 42 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0019 | 0.2068 | 119.7888 | 6.829e-04 |
| 43 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0078 | 0.1826 | 149.5245 | 5.207e-04 |
| 44 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0384 | 0.0563 | 48.4103 | 0.0571 |
| 45 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0384 | 0.0563 | 48.4103 | 0.0571 |
| 46 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0053 | 0.1876 | 159.1189 | 6.908e-04 |
| 47 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0053 | 0.1876 | 150.0254 | 6.013e-04 |
| 48 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0015 | 0.1877 | 205.0604 | 5.230e-04 |
| 49 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0131 | 0.0470 | 160.6269 | 0.0310 |
| 50 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0131 | 0.0470 | 160.6269 | 0.0310 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2128 | 0.2128 | 153.6730 | 0.0320 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.1995 | 0.2037 | 144.6764 | 0.0336 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1779 | 0.1816 | 45.6220 | 0.0683 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.1453 | 0.1467 | 47.8338 | 0.0645 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0890 | 0.0890 | 158.1797 | 0.0314 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0539 | 0.0705 | 48.0475 | 0.0601 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0384 | 0.0563 | 48.4103 | 0.0571 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0384 | 0.0563 | 48.4103 | 0.0571 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0131 | 0.0470 | 160.6269 | 0.0310 |
| 10 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0131 | 0.0470 | 160.6269 | 0.0310 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.2251 | 0.2327 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.2247 | 0.2247 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2128 | 0.2128 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2109 | 0.2109 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2058 | 0.2058 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.1995 | 0.2037 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1910 | 0.1975 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1779 | 0.1816 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.1674 | 0.1674 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.1672 | 0.1672 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.1654 | 0.1654 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1564 | 0.1564 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1543 | 0.1565 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.1453 | 0.1467 |
| 15 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1315 | 0.1315 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.1161 | 0.1161 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0959 | 0.0959 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0890 | 0.0890 |
| 19 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0881 | 0.0881 |
| 20 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | 0.0854 | 0.0854 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0826 | 0.0826 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0752 | 0.0752 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0604 | 0.0604 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0539 | 0.0705 |
| 25 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | 0.0488 | 0.0488 |
| 26 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0404 | 0.0577 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0404 | 0.0577 |
| 28 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0384 | 0.0563 |
| 29 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0384 | 0.0563 |
| 30 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0340 | 0.0531 |
| 31 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0340 | 0.0531 |
| 32 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0282 | 0.0725 |
| 33 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0338 | 0.0490 |
| 34 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0338 | 0.0490 |
| 35 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | 0.0260 | 0.0260 |
| 36 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | 0.0248 | 0.0248 |
| 37 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0209 | 0.0388 |
| 38 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0239 | 0.0239 |
| 39 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | electron | -0.0217 | 0.0217 |
| 40 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0131 | 0.0470 |
| 41 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0131 | 0.0470 |
| 42 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | -0.0192 | 0.0192 |
| 43 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | 0.0176 | 0.0176 |
| 44 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0163 | 0.0163 |
| 45 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0154 | 0.0154 |
| 46 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | -0.0129 | 0.0224 |
| 47 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0141 | 0.0169 |
| 48 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.0130 | 0.0130 |
| 49 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0038 | 0.0460 |
| 50 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0038 | 0.0460 |
| 51 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | -0.0119 | 0.0119 |
| 52 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0118 | 0.0118 |
| 53 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0065 | 0.0277 |
| 54 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0075 | 0.0152 |
| 55 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0087 | 0.0087 |
| 56 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | 0.0085 | 0.0085 |
| 57 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0029 | 0.0275 |
| 58 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0075 | 0.0086 |
| 59 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0073 | 0.0073 |
| 60 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | 0.0072 | 0.0072 |
| 61 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0050 | 0.0147 |
| 62 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0065 | 0.0065 |
| 63 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0065 | 0.0065 |
| 64 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0061 | 0.0061 |
| 65 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | 0.0060 | 0.0060 |
| 66 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | 0.0060 | 0.0060 |
| 67 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | neutral_hadron | 0.0053 | 0.0075 |
| 68 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0057 | 0.0057 |
| 69 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0057 | 0.0057 |
| 70 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | photon | 0.0054 | 0.0054 |
| 71 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | -0.0051 | 0.0063 |
| 72 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0052 | 0.0052 |
| 73 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0052 | 0.0052 |
| 74 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | neutral_hadron | 0.0050 | 0.0051 |
| 75 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | charged_hadron | -0.0049 | 0.0050 |
| 76 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | 0.0048 | 0.0048 |
| 77 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | neutral_hadron | -0.0042 | 0.0072 |
| 78 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | -0.0026 | 0.0133 |
| 79 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0045 | 0.0045 |
| 80 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0045 | 0.0045 |
| 81 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0037 | 0.0064 |
| 82 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0040 | 0.0048 |
| 83 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | 0.0042 | 0.0042 |
| 84 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | 0.0040 | 0.0040 |
| 85 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | charged_hadron | 0.0035 | 0.0045 |
| 86 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | charged_hadron | -0.0028 | 0.0061 |
| 87 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | charged_hadron | -0.0028 | 0.0061 |
| 88 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | 0.0034 | 0.0034 |
| 89 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | photon | -0.0030 | 0.0044 |
| 90 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0030 | 0.0039 |
| 91 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | charged_hadron | -0.0029 | 0.0038 |
| 92 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | -0.0028 | 0.0028 |
| 93 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | neutral_hadron | -0.0022 | 0.0035 |
| 94 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | 0.0024 | 0.0024 |
| 95 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | charged_hadron | -0.0024 | 0.0025 |
| 96 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0013 | 0.0064 |
| 97 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | photon | -0.0021 | 0.0030 |
| 98 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | -0.0017 | 0.0039 |
| 99 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | -0.0017 | 0.0039 |
| 100 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -0.0022 | 0.0022 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
