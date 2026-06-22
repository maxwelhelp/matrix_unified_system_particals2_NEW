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
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.3973 | 0.3973 | 39.0524 | 0.0850 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.3647 | 0.3647 | 124.1126 | 0.0389 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0832 | 0.8534 | 124.2740 | 0.0016 |
| 4 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0832 | 0.8534 | 131.4352 | 0.0017 |
| 5 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.0994 | 0.7339 | 131.1386 | 0.0022 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2139 | 0.2139 | 153.6730 | 0.0316 |
| 7 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.1855 | 0.3047 | 262.8722 | 8.057e-05 |
| 8 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.1688 | 0.3540 | 308.2119 | 3.235e-04 |
| 9 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.0732 | 0.7161 | 108.9801 | 7.237e-04 |
| 10 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1444 | 0.3266 | 288.8622 | 1.672e-04 |
| 11 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0385 | 0.7319 | 130.5200 | 0.0014 |
| 12 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0849 | 0.4298 | 132.0454 | 0.0019 |
| 13 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0809 | 0.4184 | 124.4872 | 0.0013 |
| 14 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0809 | 0.4184 | 132.0445 | 0.0015 |
| 15 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.0672 | 0.3965 | 109.8403 | 6.404e-04 |
| 16 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0885 | 0.2818 | 104.0169 | 0.0016 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.1253 | 0.1296 | 47.8338 | 0.0615 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.1241 | 0.1267 | 154.2962 | 0.0316 |
| 19 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0796 | 0.2988 | 113.4441 | 0.0018 |
| 20 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0717 | 0.2996 | 105.0147 | 0.0012 |
| 21 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0717 | 0.2996 | 111.2343 | 0.0013 |
| 22 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0952 | 0.2008 | 156.8574 | 9.939e-04 |
| 23 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0296 | 0.4093 | 132.0595 | 0.0013 |
| 24 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1029 | 0.1029 | 44.8754 | 0.0599 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1029 | 0.1029 | 44.8754 | 0.0599 |
| 26 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0756 | 0.1713 | 196.0397 | 3.611e-04 |
| 27 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0483 | 0.2616 | 123.2512 | 0.0013 |
| 28 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0518 | 0.2190 | 206.9739 | 6.361e-04 |
| 29 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0402 | 0.2647 | 91.8748 | 5.930e-04 |
| 30 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0593 | 0.1745 | 143.8280 | 5.482e-04 |
| 31 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0593 | 0.1745 | 152.4296 | 6.358e-04 |
| 32 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0619 | 0.1545 | 161.8836 | 1.744e-04 |
| 33 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0220 | 0.2894 | 110.8742 | 0.0012 |
| 34 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0257 | 0.2718 | 298.0052 | 1.830e-04 |
| 35 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0257 | 0.2718 | 286.5959 | 1.596e-04 |
| 36 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0200 | 0.2942 | 99.7638 | 0.0010 |
| 37 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0350 | 0.2318 | 115.0230 | 7.713e-04 |
| 38 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0350 | 0.2318 | 120.5559 | 8.879e-04 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0732 | 0.0736 | 152.0112 | 0.0325 |
| 40 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0732 | 0.0736 | 152.0112 | 0.0325 |
| 41 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0446 | 0.1820 | 152.1832 | 5.988e-04 |
| 42 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0283 | 0.2240 | 120.8415 | 8.144e-04 |
| 43 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0163 | 0.2699 | 88.6964 | 5.054e-04 |
| 44 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0383 | 0.1725 | 122.9819 | 2.910e-04 |
| 45 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0548 | 0.0811 | 47.1044 | 0.0600 |
| 46 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | 0.0202 | 0.2069 | 101.7508 | 3.969e-04 |
| 47 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0029 | 0.2676 | 97.6660 | 9.594e-04 |
| 48 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0029 | 0.2676 | 100.4949 | 0.0011 |
| 49 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0074 | 0.1684 | 186.9479 | 3.322e-04 |
| 50 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0074 | 0.1684 | 198.8910 | 3.856e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.3973 | 0.3973 | 39.0524 | 0.0850 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.3647 | 0.3647 | 124.1126 | 0.0389 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2139 | 0.2139 | 153.6730 | 0.0316 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.1253 | 0.1296 | 47.8338 | 0.0615 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.1241 | 0.1267 | 154.2962 | 0.0316 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1029 | 0.1029 | 44.8754 | 0.0599 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1029 | 0.1029 | 44.8754 | 0.0599 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0732 | 0.0736 | 152.0112 | 0.0325 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0732 | 0.0736 | 152.0112 | 0.0325 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0548 | 0.0811 | 47.1044 | 0.0600 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.4188 | 0.4188 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.3973 | 0.3973 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.3965 | 0.3965 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.3797 | 0.3797 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.3731 | 0.3731 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.3698 | 0.3698 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.3647 | 0.3647 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.3450 | 0.3450 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.3410 | 0.3410 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.3209 | 0.3209 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2369 | 0.2369 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2164 | 0.2164 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2139 | 0.2139 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.1894 | 0.1894 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.1415 | 0.1415 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1296 | 0.1360 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.1253 | 0.1296 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.1241 | 0.1267 |
| 19 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1183 | 0.1217 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1186 | 0.1186 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1186 | 0.1186 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1162 | 0.1162 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.1147 | 0.1147 |
| 24 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1036 | 0.1036 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1036 | 0.1036 |
| 26 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1029 | 0.1029 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1029 | 0.1029 |
| 28 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0882 | 0.0882 |
| 29 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0838 | 0.0838 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0838 | 0.0838 |
| 31 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0782 | 0.0782 |
| 32 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0782 | 0.0782 |
| 33 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0732 | 0.0736 |
| 34 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0732 | 0.0736 |
| 35 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0710 | 0.0710 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0710 | 0.0710 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0576 | 0.0772 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0548 | 0.0811 |
| 39 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0597 | 0.0597 |
| 40 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0539 | 0.0824 |
| 41 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0526 | 0.0543 |
| 42 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0526 | 0.0543 |
| 43 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0411 | 0.0411 |
| 44 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0378 | 0.0378 |
| 45 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0366 | 0.0366 |
| 46 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0366 | 0.0366 |
| 47 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0358 | 0.0358 |
| 48 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.0339 | 0.0339 |
| 49 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0309 | 0.0309 |
| 50 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0294 | 0.0294 |
| 51 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0278 | 0.0278 |
| 52 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0264 | 0.0264 |
| 53 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | 0.0252 | 0.0252 |
| 54 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0246 | 0.0246 |
| 55 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0216 | 0.0216 |
| 56 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0204 | 0.0204 |
| 57 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0203 | 0.0203 |
| 58 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -0.0203 | 0.0203 |
| 59 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0191 | 0.0201 |
| 60 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0191 | 0.0201 |
| 61 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0183 | 0.0183 |
| 62 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0175 | 0.0175 |
| 63 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0175 | 0.0175 |
| 64 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0173 | 0.0173 |
| 65 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | -0.0153 | 0.0153 |
| 66 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0150 | 0.0150 |
| 67 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0148 | 0.0148 |
| 68 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | neutral_hadron | 0.0134 | 0.0160 |
| 69 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0125 | 0.0125 |
| 70 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0125 | 0.0125 |
| 71 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | 0.0123 | 0.0123 |
| 72 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0120 | 0.0120 |
| 73 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0104 | 0.0104 |
| 74 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0104 | 0.0104 |
| 75 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | 0.0101 | 0.0101 |
| 76 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0088 | 0.0088 |
| 77 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0088 | 0.0088 |
| 78 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0050 | 0.0188 |
| 79 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0050 | 0.0188 |
| 80 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0075 | 0.0085 |
| 81 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0072 | 0.0073 |
| 82 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | 0.0072 | 0.0072 |
| 83 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | 0.0072 | 0.0072 |
| 84 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | 0.0070 | 0.0070 |
| 85 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0039 | 0.0157 |
| 86 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0039 | 0.0157 |
| 87 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0054 | 0.0077 |
| 88 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0054 | 0.0077 |
| 89 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0031 | 0.0157 |
| 90 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0031 | 0.0157 |
| 91 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | neutral_hadron | -0.0048 | 0.0067 |
| 92 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | 0.0050 | 0.0050 |
| 93 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0045 | 0.0055 |
| 94 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0045 | 0.0055 |
| 95 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0043 | 0.0043 |
| 96 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | 0.0015 | 0.0156 |
| 97 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0017 | 0.0145 |
| 98 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0017 | 0.0145 |
| 99 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0029 | 0.0089 |
| 100 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0040 | 0.0040 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
