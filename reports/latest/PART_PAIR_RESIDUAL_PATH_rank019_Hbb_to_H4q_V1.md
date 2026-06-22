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
| 1 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.5248 | 0.6634 | 329.9815 | 2.542e-04 |
| 2 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.5046 | 0.6657 | 265.7897 | 1.381e-04 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.3638 | 1.0217 | 130.7757 | 0.0022 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.3065 | 1.1724 | 102.9025 | 0.0011 |
| 5 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.2511 | 1.2198 | 132.9179 | 0.0030 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.2511 | 1.2198 | 124.7848 | 0.0025 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.4217 | 0.4217 | 128.2821 | 0.0447 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.3494 | 0.3494 | 42.8085 | 0.1045 |
| 9 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.2725 | 0.6064 | 131.1759 | 0.0020 |
| 10 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.2275 | 0.6995 | 102.6035 | 0.0010 |
| 11 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | 0.0596 | 1.1171 | 132.2434 | 0.0028 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.2667 | 0.2708 | 144.6764 | 0.0407 |
| 13 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.1450 | 0.6567 | 132.8509 | 0.0026 |
| 14 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.1450 | 0.6567 | 124.7527 | 0.0022 |
| 15 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1644 | 0.5127 | 88.0831 | 9.319e-04 |
| 16 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1616 | 0.4961 | 292.1937 | 2.230e-04 |
| 17 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1616 | 0.4961 | 307.0545 | 2.704e-04 |
| 18 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.1704 | 0.4580 | 90.8134 | 7.993e-04 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1896 | 0.2077 | 45.6220 | 0.0886 |
| 20 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.1415 | 0.3914 | 100.3251 | 6.582e-04 |
| 21 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1283 | 0.4407 | 110.9378 | 0.0018 |
| 22 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1116 | 0.3974 | 102.4834 | 0.0016 |
| 23 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.1227 | 0.3047 | 159.8869 | 3.161e-04 |
| 24 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.1171 | 0.3244 | 122.1807 | 4.891e-04 |
| 25 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0628 | 0.5094 | 107.4127 | 0.0020 |
| 26 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0628 | 0.5094 | 114.8006 | 0.0024 |
| 27 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0703 | 0.4475 | 303.0085 | 2.635e-04 |
| 28 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | 0.0103 | 0.6673 | 132.6333 | 0.0025 |
| 29 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | 0.0542 | 0.4826 | 112.7432 | 0.0023 |
| 30 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0723 | 0.3665 | 117.1016 | 0.0014 |
| 31 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0723 | 0.3665 | 124.1069 | 0.0017 |
| 32 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0645 | 0.3752 | 122.4333 | 0.0016 |
| 33 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.1223 | 0.1223 | 156.8609 | 0.0390 |
| 34 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0686 | 0.3285 | 123.5911 | 0.0014 |
| 35 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0787 | 0.2675 | 205.0604 | 6.564e-04 |
| 36 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0226 | 0.4375 | 103.2328 | 0.0020 |
| 37 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0226 | 0.4375 | 98.7188 | 0.0017 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1054 | 0.1054 | 47.0544 | 0.0772 |
| 39 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0396 | 0.3066 | 146.5217 | 0.0010 |
| 40 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0396 | 0.3066 | 157.1877 | 0.0012 |
| 41 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0403 | 0.2931 | 155.0080 | 0.0010 |
| 42 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0013 | 0.4180 | 100.9152 | 0.0020 |
| 43 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0383 | 0.2673 | 186.9574 | 6.134e-04 |
| 44 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0383 | 0.2673 | 200.1803 | 7.374e-04 |
| 45 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0193 | 0.2792 | 201.6123 | 7.317e-04 |
| 46 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0129 | 0.2841 | 155.4548 | 0.0012 |
| 47 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0406 | 0.0626 | 158.9065 | 0.0382 |
| 48 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0406 | 0.0626 | 158.9065 | 0.0382 |
| 49 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | -0.0028 | 0.0466 | 47.2781 | 0.0782 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | -0.0028 | 0.0466 | 47.2781 | 0.0782 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.4217 | 0.4217 | 128.2821 | 0.0447 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.3494 | 0.3494 | 42.8085 | 0.1045 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.2667 | 0.2708 | 144.6764 | 0.0407 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1896 | 0.2077 | 45.6220 | 0.0886 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.1223 | 0.1223 | 156.8609 | 0.0390 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1054 | 0.1054 | 47.0544 | 0.0772 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0406 | 0.0626 | 158.9065 | 0.0382 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0406 | 0.0626 | 158.9065 | 0.0382 |
| 9 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | -0.0028 | 0.0466 | 47.2781 | 0.0782 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | -0.0028 | 0.0466 | 47.2781 | 0.0782 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.5366 | 0.5366 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.5039 | 0.5039 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.4566 | 0.4566 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.4549 | 0.4549 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | electron | -0.4327 | 0.4327 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.4217 | 0.4217 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.3922 | 0.3922 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.3782 | 0.3782 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | electron | 0.3526 | 0.3526 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.3494 | 0.3494 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.3210 | 0.3210 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.2667 | 0.2708 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.2632 | 0.2632 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2555 | 0.2555 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.2339 | 0.2502 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.2016 | 0.2016 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1995 | 0.1995 |
| 18 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1954 | 0.2014 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1896 | 0.2077 |
| 20 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1675 | 0.2263 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.1438 | 0.1438 |
| 22 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | 0.1309 | 0.1309 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.1223 | 0.1223 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.1189 | 0.1189 |
| 25 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1079 | 0.1079 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1054 | 0.1054 |
| 27 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.1036 | 0.1036 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.1033 | 0.1033 |
| 29 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0991 | 0.0991 |
| 30 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0880 | 0.0880 |
| 31 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0861 | 0.0861 |
| 32 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0861 | 0.0861 |
| 33 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0760 | 0.0760 |
| 34 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0760 | 0.0760 |
| 35 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0757 | 0.0757 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0676 | 0.0954 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0676 | 0.0954 |
| 38 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | 0.0699 | 0.0699 |
| 39 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0651 | 0.0685 |
| 40 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0615 | 0.0804 |
| 41 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | 0.0612 | 0.0683 |
| 42 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0619 | 0.0619 |
| 43 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0619 | 0.0619 |
| 44 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | -0.0610 | 0.0610 |
| 45 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | 0.0595 | 0.0595 |
| 46 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0542 | 0.0728 |
| 47 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0542 | 0.0568 |
| 48 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0484 | 0.0725 |
| 49 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0481 | 0.0574 |
| 50 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0491 | 0.0527 |
| 51 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | 0.0487 | 0.0487 |
| 52 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0458 | 0.0458 |
| 53 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | 0.0436 | 0.0536 |
| 54 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | 0.0436 | 0.0536 |
| 55 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0406 | 0.0626 |
| 56 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0406 | 0.0626 |
| 57 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0381 | 0.0443 |
| 58 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0367 | 0.0484 |
| 59 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | 0.0385 | 0.0385 |
| 60 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0373 | 0.0416 |
| 61 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0376 | 0.0376 |
| 62 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0376 | 0.0376 |
| 63 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0367 | 0.0367 |
| 64 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0367 | 0.0367 |
| 65 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | 0.0337 | 0.0474 |
| 66 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0248 | 0.0759 |
| 67 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0339 | 0.0385 |
| 68 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0309 | 0.0477 |
| 69 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | -0.0322 | 0.0410 |
| 70 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | 0.0328 | 0.0328 |
| 71 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0307 | 0.0403 |
| 72 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | 0.0298 | 0.0416 |
| 73 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | 0.0286 | 0.0436 |
| 74 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | 0.0283 | 0.0422 |
| 75 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | 0.0266 | 0.0397 |
| 76 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | electron | -0.0282 | 0.0282 |
| 77 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0258 | 0.0380 |
| 78 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0258 | 0.0380 |
| 79 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | 0.0280 | 0.0287 |
| 80 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | 0.0280 | 0.0287 |
| 81 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0244 | 0.0430 |
| 82 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0244 | 0.0430 |
| 83 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0273 | 0.0273 |
| 84 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0273 | 0.0273 |
| 85 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0232 | 0.0413 |
| 86 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0245 | 0.0255 |
| 87 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0245 | 0.0255 |
| 88 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | 0.0214 | 0.0324 |
| 89 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0190 | 0.0389 |
| 90 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | 0.0188 | 0.0341 |
| 91 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0122 | 0.0533 |
| 92 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0122 | 0.0533 |
| 93 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0196 | 0.0196 |
| 94 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | 0.0154 | 0.0282 |
| 95 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | 0.0178 | 0.0178 |
| 96 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0127 | 0.0353 |
| 97 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0127 | 0.0353 |
| 98 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | 0.0151 | 0.0151 |
| 99 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | 0.0151 | 0.0151 |
| 100 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0147 | 0.0154 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
