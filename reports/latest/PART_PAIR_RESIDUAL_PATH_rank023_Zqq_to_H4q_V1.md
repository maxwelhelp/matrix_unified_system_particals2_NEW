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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.3564 | 1.0226 | 130.7757 | 0.0021 |
| 2 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.3477 | 0.4353 | 255.3485 | 1.209e-04 |
| 3 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.3282 | 0.4614 | 329.9815 | 2.733e-04 |
| 4 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.2663 | 0.5727 | 131.1759 | 0.0018 |
| 5 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.2235 | 0.6593 | 96.9171 | 6.693e-04 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2898 | 0.2898 | 149.6900 | 0.0401 |
| 7 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.1265 | 0.8401 | 120.8026 | 0.0017 |
| 8 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.1265 | 0.8401 | 128.8138 | 0.0021 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.2374 | 0.2374 | 144.6764 | 0.0421 |
| 10 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1565 | 0.3870 | 110.9378 | 0.0016 |
| 11 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1996 | 0.2029 | 45.6220 | 0.0893 |
| 12 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1245 | 0.3582 | 102.4834 | 0.0014 |
| 13 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.1337 | 0.2901 | 123.5911 | 0.0012 |
| 14 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0010 | 0.8127 | 131.4528 | 0.0023 |
| 15 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0926 | 0.4430 | 121.2518 | 0.0015 |
| 16 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0926 | 0.4430 | 129.1286 | 0.0017 |
| 17 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1126 | 0.3601 | 97.6289 | 5.888e-04 |
| 18 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1178 | 0.3094 | 318.1224 | 3.207e-04 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.1504 | 0.1590 | 49.7953 | 0.0879 |
| 20 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.1503 | 0.1503 | 166.1179 | 0.0371 |
| 21 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1024 | 0.2887 | 81.9046 | 5.530e-04 |
| 22 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | 0.0568 | 0.4589 | 133.3510 | 0.0020 |
| 23 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0969 | 0.1996 | 148.8833 | 2.356e-04 |
| 24 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0615 | 0.2589 | 85.9040 | 4.841e-04 |
| 25 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0411 | 0.2730 | 97.5640 | 0.0011 |
| 26 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0411 | 0.2730 | 101.4841 | 0.0013 |
| 27 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0304 | 0.2667 | 114.0390 | 9.276e-04 |
| 28 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0304 | 0.2667 | 120.7818 | 0.0011 |
| 29 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0498 | 0.1883 | 204.7952 | 6.459e-04 |
| 30 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.0090 | 0.3275 | 311.4129 | 2.865e-04 |
| 31 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.0090 | 0.3275 | 297.2621 | 2.377e-04 |
| 32 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0323 | 0.2232 | 93.6346 | 4.232e-04 |
| 33 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0668 | 0.0794 | 52.3365 | 0.0737 |
| 34 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0240 | 0.2487 | 155.0080 | 9.303e-04 |
| 35 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0041 | 0.3199 | 103.1872 | 0.0013 |
| 36 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0041 | 0.3199 | 110.1915 | 0.0015 |
| 37 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0044 | 0.3179 | 112.3551 | 0.0018 |
| 38 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0082 | 0.2747 | 102.9587 | 0.0015 |
| 39 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0200 | 0.2268 | 142.9345 | 7.127e-04 |
| 40 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0200 | 0.2268 | 152.7932 | 8.474e-04 |
| 41 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0187 | 0.2119 | 115.1937 | 3.406e-04 |
| 42 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0513 | 0.0802 | 49.7706 | 0.0788 |
| 43 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0513 | 0.0802 | 49.7706 | 0.0788 |
| 44 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0199 | 0.2012 | 198.0765 | 5.679e-04 |
| 45 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0199 | 0.2012 | 185.4231 | 4.745e-04 |
| 46 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0130 | 0.2177 | 156.2505 | 9.662e-04 |
| 47 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0048 | 0.2337 | 122.5041 | 0.0013 |
| 48 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0031 | 0.2331 | 205.0604 | 6.032e-04 |
| 49 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0295 | 0.0732 | 161.3226 | 0.0388 |
| 50 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0295 | 0.0732 | 161.3227 | 0.0388 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2898 | 0.2898 | 149.6900 | 0.0401 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.2374 | 0.2374 | 144.6764 | 0.0421 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1996 | 0.2029 | 45.6220 | 0.0893 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.1504 | 0.1590 | 49.7953 | 0.0879 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.1503 | 0.1503 | 166.1179 | 0.0371 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0668 | 0.0794 | 52.3365 | 0.0737 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0513 | 0.0802 | 49.7706 | 0.0788 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0513 | 0.0802 | 49.7706 | 0.0788 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0295 | 0.0732 | 161.3226 | 0.0388 |
| 10 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0295 | 0.0732 | 161.3227 | 0.0388 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.4155 | 0.4155 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.3186 | 0.3186 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2898 | 0.2898 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2818 | 0.2818 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.2580 | 0.2580 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.2498 | 0.2498 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.2418 | 0.2418 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.2374 | 0.2374 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.2366 | 0.2366 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.2179 | 0.2179 |
| 11 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.2112 | 0.2112 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.2106 | 0.2106 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.2009 | 0.2187 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1996 | 0.2029 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.1866 | 0.1866 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1739 | 0.1739 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.1504 | 0.1590 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.1503 | 0.1503 |
| 19 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | 0.1475 | 0.1475 |
| 20 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1457 | 0.1457 |
| 21 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.1335 | 0.1335 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.1077 | 0.1307 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.1113 | 0.1113 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1033 | 0.1033 |
| 25 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0981 | 0.0981 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0766 | 0.1083 |
| 27 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0766 | 0.1083 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0742 | 0.0948 |
| 29 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0764 | 0.0764 |
| 30 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | 0.0746 | 0.0746 |
| 31 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | -0.0741 | 0.0741 |
| 32 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0668 | 0.0794 |
| 33 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0649 | 0.0649 |
| 34 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0649 | 0.0649 |
| 35 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0627 | 0.0627 |
| 36 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0616 | 0.0616 |
| 37 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0574 | 0.0574 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0513 | 0.0802 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0513 | 0.0802 |
| 40 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | 0.0567 | 0.0567 |
| 41 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.0555 | 0.0555 |
| 42 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0531 | 0.0531 |
| 43 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0531 | 0.0531 |
| 44 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0411 | 0.1003 |
| 45 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0411 | 0.1003 |
| 46 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0484 | 0.0638 |
| 47 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | 0.0469 | 0.0469 |
| 48 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0427 | 0.0427 |
| 49 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0410 | 0.0410 |
| 50 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -0.0385 | 0.0385 |
| 51 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0295 | 0.0732 |
| 52 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0295 | 0.0732 |
| 53 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | 0.0378 | 0.0378 |
| 54 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0358 | 0.0358 |
| 55 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0320 | 0.0320 |
| 56 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0320 | 0.0320 |
| 57 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0301 | 0.0302 |
| 58 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0292 | 0.0293 |
| 59 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0222 | 0.0266 |
| 60 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0230 | 0.0230 |
| 61 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0230 | 0.0230 |
| 62 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0171 | 0.0393 |
| 63 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0171 | 0.0393 |
| 64 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0210 | 0.0227 |
| 65 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | 0.0212 | 0.0212 |
| 66 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0155 | 0.0379 |
| 67 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0129 | 0.0472 |
| 68 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0130 | 0.0395 |
| 69 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0130 | 0.0395 |
| 70 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0168 | 0.0168 |
| 71 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0168 | 0.0168 |
| 72 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | -0.0161 | 0.0161 |
| 73 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0160 | 0.0160 |
| 74 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0129 | 0.0282 |
| 75 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | -0.0150 | 0.0191 |
| 76 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0149 | 0.0172 |
| 77 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0148 | 0.0151 |
| 78 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0136 | 0.0159 |
| 79 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0137 | 0.0137 |
| 80 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | 0.0113 | 0.0157 |
| 81 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0118 | 0.0125 |
| 82 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | photon | 0.0117 | 0.0124 |
| 83 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0110 | 0.0140 |
| 84 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0106 | 0.0140 |
| 85 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | 0.0111 | 0.0111 |
| 86 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0096 | 0.0168 |
| 87 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0095 | 0.0165 |
| 88 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | -0.0102 | 0.0117 |
| 89 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0105 | 0.0105 |
| 90 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0105 | 0.0105 |
| 91 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0089 | 0.0095 |
| 92 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | electron | 0.0086 | 0.0100 |
| 93 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0089 | 0.0089 |
| 94 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0088 | 0.0088 |
| 95 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0088 | 0.0088 |
| 96 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | 0.0087 | 0.0087 |
| 97 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | neutral_hadron | -0.0074 | 0.0128 |
| 98 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0079 | 0.0104 |
| 99 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0079 | 0.0104 |
| 100 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0050 | 0.0223 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
