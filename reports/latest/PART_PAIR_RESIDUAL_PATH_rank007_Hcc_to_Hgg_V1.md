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
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.3973 | 0.3973 | 39.0524 | 0.0850 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.3647 | 0.3647 | 124.1126 | 0.0389 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0832 | 0.8534 | 131.4352 | 0.0017 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.0994 | 0.7339 | 99.4952 | 6.993e-04 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.2139 | 0.2139 | 153.6730 | 0.0316 |
| 6 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.1855 | 0.3047 | 299.4730 | 1.582e-04 |
| 7 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.1688 | 0.3540 | 256.5644 | 1.037e-04 |
| 8 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.0732 | 0.7161 | 133.2286 | 0.0014 |
| 9 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1444 | 0.3266 | 282.4639 | 1.495e-04 |
| 10 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1444 | 0.3266 | 288.8622 | 1.672e-04 |
| 11 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0385 | 0.7319 | 125.0754 | 0.0013 |
| 12 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0385 | 0.7319 | 130.5200 | 0.0014 |
| 13 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.0849 | 0.4298 | 98.9359 | 6.279e-04 |
| 14 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0809 | 0.4184 | 132.0445 | 0.0015 |
| 15 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0672 | 0.3965 | 135.6455 | 0.0013 |
| 16 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0885 | 0.2818 | 88.8183 | 5.145e-04 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1253 | 0.1296 | 47.8338 | 0.0615 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1241 | 0.1267 | 154.2962 | 0.0316 |
| 19 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1241 | 0.1267 | 154.2962 | 0.0316 |
| 20 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0796 | 0.2988 | 83.2890 | 5.962e-04 |
| 21 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0717 | 0.2996 | 111.2343 | 0.0013 |
| 22 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0952 | 0.2008 | 117.8791 | 3.206e-04 |
| 23 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0296 | 0.4093 | 126.4518 | 0.0011 |
| 24 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0296 | 0.4093 | 132.0595 | 0.0013 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1029 | 0.1029 | 44.8754 | 0.0599 |
| 26 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0756 | 0.1713 | 186.9599 | 3.205e-04 |
| 27 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0756 | 0.1713 | 196.0397 | 3.611e-04 |
| 28 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0483 | 0.2616 | 97.1721 | 4.240e-04 |
| 29 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0518 | 0.2190 | 154.4873 | 2.037e-04 |
| 30 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0402 | 0.2647 | 112.8805 | 0.0012 |
| 31 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0593 | 0.1745 | 152.4296 | 6.358e-04 |
| 32 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0619 | 0.1545 | 203.4189 | 3.429e-04 |
| 33 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0220 | 0.2894 | 106.0217 | 0.0011 |
| 34 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0220 | 0.2894 | 110.8742 | 0.0012 |
| 35 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0257 | 0.2718 | 298.0052 | 1.830e-04 |
| 36 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0200 | 0.2942 | 99.7638 | 0.0010 |
| 37 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0200 | 0.2942 | 97.0879 | 9.031e-04 |
| 38 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0350 | 0.2318 | 120.5559 | 8.879e-04 |
| 39 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0732 | 0.0736 | 152.0112 | 0.0325 |
| 40 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0446 | 0.1820 | 145.0695 | 5.308e-04 |
| 41 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0446 | 0.1820 | 152.1832 | 5.988e-04 |
| 42 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0283 | 0.2240 | 116.2196 | 7.223e-04 |
| 43 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0283 | 0.2240 | 120.8415 | 8.144e-04 |
| 44 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0163 | 0.2699 | 100.9367 | 0.0010 |
| 45 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | 0.0383 | 0.1725 | 155.1264 | 5.741e-04 |
| 46 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0548 | 0.0811 | 47.1044 | 0.0600 |
| 47 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0548 | 0.0811 | 47.1044 | 0.0600 |
| 48 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | 0.0202 | 0.2069 | 123.3645 | 7.855e-04 |
| 49 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0029 | 0.2676 | 100.4949 | 0.0011 |
| 50 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | -0.0074 | 0.1684 | 198.8910 | 3.856e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.3973 | 0.3973 | 39.0524 | 0.0850 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.3647 | 0.3647 | 124.1126 | 0.0389 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.2139 | 0.2139 | 153.6730 | 0.0316 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1253 | 0.1296 | 47.8338 | 0.0615 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1241 | 0.1267 | 154.2962 | 0.0316 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1241 | 0.1267 | 154.2962 | 0.0316 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1029 | 0.1029 | 44.8754 | 0.0599 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0732 | 0.0736 | 152.0112 | 0.0325 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0548 | 0.0811 | 47.1044 | 0.0600 |
| 10 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0548 | 0.0811 | 47.1044 | 0.0600 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.4188 | 0.4188 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.3973 | 0.3973 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.3965 | 0.3965 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.3797 | 0.3797 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.3731 | 0.3731 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.3698 | 0.3698 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.3647 | 0.3647 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.3450 | 0.3450 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.3410 | 0.3410 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.3208 | 0.3208 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.2369 | 0.2369 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.2164 | 0.2164 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.2139 | 0.2139 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.1894 | 0.1894 |
| 15 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1415 | 0.1415 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1415 | 0.1415 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1296 | 0.1360 |
| 18 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1253 | 0.1296 |
| 19 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1241 | 0.1267 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1241 | 0.1267 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1183 | 0.1217 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1183 | 0.1217 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.1186 | 0.1186 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1162 | 0.1162 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.1147 | 0.1147 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.1036 | 0.1036 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1029 | 0.1029 |
| 28 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0882 | 0.0882 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0838 | 0.0838 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0782 | 0.0782 |
| 31 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0732 | 0.0736 |
| 32 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0710 | 0.0710 |
| 33 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0576 | 0.0772 |
| 34 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0576 | 0.0772 |
| 35 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0548 | 0.0811 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0548 | 0.0811 |
| 37 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0597 | 0.0597 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0539 | 0.0824 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0539 | 0.0824 |
| 40 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0526 | 0.0543 |
| 41 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0411 | 0.0411 |
| 42 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0378 | 0.0378 |
| 43 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0366 | 0.0366 |
| 44 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0358 | 0.0358 |
| 45 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0339 | 0.0339 |
| 46 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0339 | 0.0339 |
| 47 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0309 | 0.0309 |
| 48 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0309 | 0.0309 |
| 49 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0294 | 0.0294 |
| 50 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0278 | 0.0278 |
| 51 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0264 | 0.0264 |
| 52 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0264 | 0.0264 |
| 53 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0252 | 0.0252 |
| 54 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0246 | 0.0246 |
| 55 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0216 | 0.0216 |
| 56 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0216 | 0.0216 |
| 57 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0204 | 0.0204 |
| 58 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0203 | 0.0203 |
| 59 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0203 | 0.0203 |
| 60 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0203 | 0.0203 |
| 61 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0191 | 0.0201 |
| 62 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0183 | 0.0183 |
| 63 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0183 | 0.0183 |
| 64 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0175 | 0.0175 |
| 65 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0173 | 0.0173 |
| 66 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0153 | 0.0153 |
| 67 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0150 | 0.0150 |
| 68 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | 0.0150 | 0.0150 |
| 69 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | 0.0148 | 0.0148 |
| 70 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | neutral_hadron | 0.0134 | 0.0160 |
| 71 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0125 | 0.0125 |
| 72 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | 0.0123 | 0.0123 |
| 73 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0120 | 0.0120 |
| 74 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0104 | 0.0104 |
| 75 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | 0.0101 | 0.0101 |
| 76 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0088 | 0.0088 |
| 77 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0050 | 0.0188 |
| 78 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0075 | 0.0085 |
| 79 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0072 | 0.0073 |
| 80 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | electron | 0.0072 | 0.0072 |
| 81 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | 0.0070 | 0.0070 |
| 82 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0039 | 0.0157 |
| 83 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | -0.0054 | 0.0077 |
| 84 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | -0.0031 | 0.0157 |
| 85 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | neutral_hadron | -0.0048 | 0.0067 |
| 86 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | 0.0050 | 0.0050 |
| 87 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0045 | 0.0055 |
| 88 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0043 | 0.0043 |
| 89 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | 0.0015 | 0.0156 |
| 90 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | 0.0017 | 0.0145 |
| 91 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0029 | 0.0089 |
| 92 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0040 | 0.0040 |
| 93 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | photon | 0.0036 | 0.0055 |
| 94 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | charged_hadron | -0.0033 | 0.0064 |
| 95 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | neutral_hadron | 0.0029 | 0.0080 |
| 96 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | 0.0032 | 0.0066 |
| 97 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | charged_hadron | -0.0035 | 0.0036 |
| 98 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | 0.0035 | 0.0035 |
| 99 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | charged_hadron | -0.0032 | 0.0047 |
| 100 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0034 | 0.0034 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
