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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.2374 | 0.7070 | 105.1566 | 6.983e-04 |
| 2 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.3015 | 0.3960 | 274.1963 | 8.327e-05 |
| 3 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | 0.1715 | 0.6267 | 128.8689 | 0.0011 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | 0.1715 | 0.6267 | 125.8764 | 0.0010 |
| 5 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.1118 | 0.7491 | 135.5131 | 0.0015 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.2128 | 0.2128 | 153.6730 | 0.0320 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.1995 | 0.2037 | 144.6764 | 0.0336 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1437 | 0.4081 | 104.3027 | 6.194e-04 |
| 9 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.1587 | 0.3268 | 299.4730 | 1.721e-04 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.1779 | 0.1816 | 45.6220 | 0.0683 |
| 11 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | 0.0272 | 0.6769 | 133.2286 | 0.0015 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1453 | 0.1467 | 47.8338 | 0.0645 |
| 13 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1004 | 0.3103 | 87.7783 | 5.750e-04 |
| 14 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0756 | 0.3962 | 136.7783 | 0.0013 |
| 15 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.0717 | 0.3908 | 130.3340 | 9.962e-04 |
| 16 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.0717 | 0.3908 | 127.1831 | 9.334e-04 |
| 17 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0925 | 0.2875 | 88.5099 | 5.168e-04 |
| 18 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0663 | 0.2744 | 309.6137 | 1.559e-04 |
| 19 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0708 | 0.2380 | 101.1694 | 4.424e-04 |
| 20 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0890 | 0.0890 | 158.1797 | 0.0314 |
| 21 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0890 | 0.0890 | 158.1797 | 0.0314 |
| 22 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0348 | 0.2667 | 104.0659 | 0.0011 |
| 23 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -3.987e-05 | 0.4002 | 135.6455 | 0.0013 |
| 24 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0277 | 0.2854 | 287.2878 | 1.221e-04 |
| 25 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0277 | 0.2854 | 291.4487 | 1.300e-04 |
| 26 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0487 | 0.2005 | 121.6363 | 3.535e-04 |
| 27 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0246 | 0.2614 | 109.0722 | 9.065e-04 |
| 28 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0246 | 0.2614 | 106.2916 | 8.488e-04 |
| 29 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0222 | 0.2709 | 100.9367 | 0.0011 |
| 30 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0206 | 0.2735 | 112.8805 | 0.0012 |
| 31 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0185 | 0.2771 | 115.3753 | 0.0012 |
| 32 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0301 | 0.2210 | 123.3645 | 8.767e-04 |
| 33 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0149 | 0.2442 | 98.6859 | 8.048e-04 |
| 34 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0149 | 0.2442 | 97.1988 | 7.539e-04 |
| 35 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0204 | 0.2181 | 126.8770 | 8.991e-04 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0539 | 0.0705 | 48.0475 | 0.0601 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0539 | 0.0705 | 48.0475 | 0.0601 |
| 38 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0245 | 0.1704 | 203.4189 | 4.290e-04 |
| 39 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0222 | 0.1616 | 194.9959 | 3.346e-04 |
| 40 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0222 | 0.1616 | 189.6914 | 3.134e-04 |
| 41 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0148 | 0.1680 | 155.1264 | 6.596e-04 |
| 42 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0122 | 0.1684 | 207.7472 | 4.494e-04 |
| 43 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0019 | 0.2068 | 119.7888 | 6.829e-04 |
| 44 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0019 | 0.2068 | 117.2211 | 6.404e-04 |
| 45 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0078 | 0.1826 | 145.3944 | 4.882e-04 |
| 46 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0078 | 0.1826 | 149.5245 | 5.207e-04 |
| 47 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0384 | 0.0563 | 48.4103 | 0.0571 |
| 48 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0053 | 0.1876 | 159.1189 | 6.908e-04 |
| 49 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0015 | 0.1877 | 160.7478 | 2.337e-04 |
| 50 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0131 | 0.0470 | 160.6269 | 0.0310 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.2128 | 0.2128 | 153.6730 | 0.0320 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.1995 | 0.2037 | 144.6764 | 0.0336 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.1779 | 0.1816 | 45.6220 | 0.0683 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1453 | 0.1467 | 47.8338 | 0.0645 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0890 | 0.0890 | 158.1797 | 0.0314 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0890 | 0.0890 | 158.1797 | 0.0314 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0539 | 0.0705 | 48.0475 | 0.0601 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0539 | 0.0705 | 48.0475 | 0.0601 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0384 | 0.0563 | 48.4103 | 0.0571 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0131 | 0.0470 | 160.6269 | 0.0310 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2251 | 0.2327 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.2247 | 0.2247 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.2128 | 0.2128 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.2109 | 0.2109 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.2058 | 0.2058 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.1995 | 0.2037 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1910 | 0.1975 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.1779 | 0.1816 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.1674 | 0.1674 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.1672 | 0.1672 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.1654 | 0.1654 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1564 | 0.1564 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1543 | 0.1565 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1453 | 0.1467 |
| 15 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1315 | 0.1315 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.1161 | 0.1161 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0959 | 0.0959 |
| 18 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0959 | 0.0959 |
| 19 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0890 | 0.0890 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0890 | 0.0890 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0881 | 0.0881 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0881 | 0.0881 |
| 23 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | 0.0854 | 0.0854 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0826 | 0.0826 |
| 25 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0826 | 0.0826 |
| 26 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0752 | 0.0752 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0752 | 0.0752 |
| 28 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0604 | 0.0604 |
| 29 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0604 | 0.0604 |
| 30 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0539 | 0.0705 |
| 31 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0539 | 0.0705 |
| 32 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | 0.0488 | 0.0488 |
| 33 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0404 | 0.0577 |
| 34 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0384 | 0.0563 |
| 35 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0340 | 0.0531 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0282 | 0.0725 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0282 | 0.0725 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0338 | 0.0490 |
| 39 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0260 | 0.0260 |
| 40 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | 0.0248 | 0.0248 |
| 41 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0209 | 0.0388 |
| 42 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0239 | 0.0239 |
| 43 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0239 | 0.0239 |
| 44 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0217 | 0.0217 |
| 45 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0217 | 0.0217 |
| 46 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0131 | 0.0470 |
| 47 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | -0.0192 | 0.0192 |
| 48 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | 0.0176 | 0.0176 |
| 49 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | 0.0163 | 0.0163 |
| 50 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0154 | 0.0154 |
| 51 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0154 | 0.0154 |
| 52 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | -0.0129 | 0.0224 |
| 53 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0141 | 0.0169 |
| 54 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0130 | 0.0130 |
| 55 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0130 | 0.0130 |
| 56 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0038 | 0.0460 |
| 57 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | -0.0119 | 0.0119 |
| 58 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0118 | 0.0118 |
| 59 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0118 | 0.0118 |
| 60 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0065 | 0.0277 |
| 61 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0075 | 0.0152 |
| 62 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0087 | 0.0087 |
| 63 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | 0.0085 | 0.0085 |
| 64 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | 0.0085 | 0.0085 |
| 65 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0029 | 0.0275 |
| 66 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0075 | 0.0086 |
| 67 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0073 | 0.0073 |
| 68 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0073 | 0.0073 |
| 69 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | 0.0072 | 0.0072 |
| 70 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0050 | 0.0147 |
| 71 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0065 | 0.0065 |
| 72 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0061 | 0.0061 |
| 73 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0061 | 0.0061 |
| 74 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | 0.0060 | 0.0060 |
| 75 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0053 | 0.0075 |
| 76 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0053 | 0.0075 |
| 77 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0057 | 0.0057 |
| 78 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | photon | 0.0054 | 0.0054 |
| 79 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0051 | 0.0063 |
| 80 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0051 | 0.0063 |
| 81 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0052 | 0.0052 |
| 82 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | neutral_hadron | 0.0050 | 0.0051 |
| 83 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | charged_hadron | -0.0049 | 0.0050 |
| 84 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | 0.0048 | 0.0048 |
| 85 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | neutral_hadron | -0.0042 | 0.0072 |
| 86 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0026 | 0.0133 |
| 87 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0045 | 0.0045 |
| 88 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0045 | 0.0045 |
| 89 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0045 | 0.0045 |
| 90 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0037 | 0.0064 |
| 91 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0037 | 0.0064 |
| 92 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0040 | 0.0048 |
| 93 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | 0.0042 | 0.0042 |
| 94 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | 0.0040 | 0.0040 |
| 95 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | charged_hadron | 0.0035 | 0.0045 |
| 96 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | charged_hadron | 0.0035 | 0.0045 |
| 97 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | charged_hadron | -0.0028 | 0.0061 |
| 98 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | 0.0034 | 0.0034 |
| 99 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | photon | -0.0030 | 0.0044 |
| 100 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0030 | 0.0039 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
