# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **270**
- src_label: `label_Hbb`
- tgt_label: `label_Hcc`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.1289 | 1.4592 | 14.5730 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.1289 | 1.4592 | 14.5730 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.0928 | 1.5160 | 5.5365 | 0.4686 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.0928 | 1.5160 | 5.5365 | 0.4686 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.0122 | 1.5842 | 5.3393 | 0.4686 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.0122 | 1.5842 | 5.3393 | 0.4686 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 0.9762 | 1.7325 | 12.6692 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 0.9762 | 1.7325 | 12.6692 | 0.3536 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3813 | 1.2239 | 12.7288 | 0.3536 |
| 10 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3813 | 1.2239 | 12.7288 | 0.3536 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3813 | 1.2239 | 12.7288 | 0.3536 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3813 | 1.2239 | 12.7288 | 0.3536 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.3217 | 1.4718 | 12.8175 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.3217 | 1.4718 | 12.8175 | 0.3536 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.3578 | 0.9408 | 4.4973 | 0.4686 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.3578 | 0.9408 | 4.4973 | 0.4686 |
| 17 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.3452 | 0.9485 | 4.1971 | 0.4686 |
| 18 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.3452 | 0.9485 | 4.1971 | 0.4686 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.3452 | 0.9485 | 4.1971 | 0.4686 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.3452 | 0.9485 | 4.1971 | 0.4686 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 1 | 0.8775 | 0.8775 | 3.5101 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 1 | 0.8775 | 0.8775 | 3.5101 | 0.2500 |
| 7 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | 0.8017 | 0.8017 | 3.2069 | 0.2500 |
| 8 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 2 | 0.8017 | 0.8017 | 3.2069 | 0.2500 |
| 9 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | 0.8017 | 0.8017 | 3.2069 | 0.2500 |
| 10 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 2 | 0.8017 | 0.8017 | 3.2069 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.7107 | 0.7247 | -2.5646 | -0.2771 |
| 12 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.7107 | 0.7247 | -2.5646 | -0.2771 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 2 | -0.5558 | 0.5942 | 2.2232 | -0.2500 |
| 14 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 2 | -0.5558 | 0.5942 | 2.2232 | -0.2500 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | -0.4205 | 0.4222 | 1.6819 | -0.2500 |
| 16 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 1 | -0.4205 | 0.4222 | 1.6819 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | -0.4205 | 0.4222 | 1.6819 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 1 | -0.4205 | 0.4222 | 1.6819 | -0.2500 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.3802 | 0.4801 | 1.3720 | 0.2771 |
| 20 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.3802 | 0.4801 | 1.3720 | 0.2771 |
| 21 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 2 | -0.3553 | 0.4010 | 1.4213 | -0.2500 |
| 22 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 2 | -0.3553 | 0.4010 | 1.4213 | -0.2500 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.3269 | 0.3669 | 1.4828 | 0.2205 |
| 24 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.3269 | 0.3669 | 1.4828 | 0.2205 |
| 25 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.2670 | 0.2770 | -0.9634 | -0.2771 |
| 26 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.2670 | 0.2770 | -0.9634 | -0.2771 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.2670 | 0.2770 | -0.9634 | -0.2771 |
| 28 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.2670 | 0.2770 | -0.9634 | -0.2771 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.2090 | 0.2327 | 0.9480 | 0.2205 |
| 30 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.2090 | 0.2327 | 0.9480 | 0.2205 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.2103 | 0.2156 | -1.2485 | -0.1684 |
| 32 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.2103 | 0.2156 | -1.2485 | -0.1684 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.1486 | 0.1486 | 1.1582 | 0.1283 |
| 34 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.1486 | 0.1486 | 1.1582 | 0.1283 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.1172 | 0.2380 | 0.4230 | 0.2771 |
| 36 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.1172 | 0.2380 | 0.4230 | 0.2771 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.1318 | 0.1318 | 1.4786 | 0.0891 |
| 38 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.1318 | 0.1318 | 1.4786 | 0.0891 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.1193 | 0.1193 | 3.7199 | 0.0321 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.1193 | 0.1193 | 3.7199 | 0.0321 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.0986 | 0.1973 | -0.4474 | -0.2205 |
| 42 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.0986 | 0.1973 | -0.4474 | -0.2205 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | -0.1037 | 0.1037 | 3.2308 | -0.0321 |
| 44 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | -0.1037 | 0.1037 | 3.2308 | -0.0321 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | -0.1030 | 0.1030 | 3.2114 | -0.0321 |
| 46 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | -0.1030 | 0.1030 | 3.2114 | -0.0321 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0707 | 0.2022 | -0.3205 | -0.2205 |
| 48 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0707 | 0.2022 | -0.3205 | -0.2205 |
| 49 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0707 | 0.2022 | -0.3205 | -0.2205 |
| 50 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0707 | 0.2022 | -0.3205 | -0.2205 |
| 51 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0924 | 0.0924 | 0.7197 | 0.1283 |
| 52 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0924 | 0.0924 | 0.7197 | 0.1283 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0924 | 0.0924 | 0.7197 | 0.1283 |
| 54 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0924 | 0.0924 | 0.7197 | 0.1283 |
| 55 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.0913 | 0.0913 | 2.8464 | 0.0321 |
| 56 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.0913 | 0.0913 | 2.8464 | 0.0321 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.0913 | 0.0913 | 2.8464 | 0.0321 |
| 58 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.0913 | 0.0913 | 2.8464 | 0.0321 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | 0.0750 | 0.0750 | 1.9475 | 0.0385 |
| 60 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | 0.0750 | 0.0750 | 1.9475 | 0.0385 |
| 61 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | -0.0668 | 0.0668 | 1.7332 | -0.0385 |
| 62 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | -0.0668 | 0.0668 | 1.7332 | -0.0385 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | -0.0668 | 0.0668 | 1.7332 | -0.0385 |
| 64 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | -0.0668 | 0.0668 | 1.7332 | -0.0385 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | -0.0645 | 0.0781 | 0.7232 | -0.0891 |
| 66 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | -0.0645 | 0.0781 | 0.7232 | -0.0891 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.0655 | 0.0655 | 0.7352 | 0.0891 |
| 68 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.0655 | 0.0655 | 0.7352 | 0.0891 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0642 | 0.0642 | 0.7198 | -0.0891 |
| 70 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0642 | 0.0642 | 0.7198 | -0.0891 |
| 71 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0642 | 0.0642 | 0.7198 | -0.0891 |
| 72 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0642 | 0.0642 | 0.7198 | -0.0891 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | -0.0577 | 0.0830 | 0.4496 | -0.1283 |
| 74 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | -0.0577 | 0.0830 | 0.4496 | -0.1283 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | 0.0584 | 0.0662 | 1.5164 | 0.0385 |
| 76 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | 0.0584 | 0.0662 | 1.5164 | 0.0385 |
| 77 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 1 | -0.0045 | 0.3258 | 0.0180 | -0.2500 |
| 78 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 1 | -0.0045 | 0.3258 | 0.0180 | -0.2500 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | -0.0556 | 0.0578 | 1.4426 | -0.0385 |
| 80 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | -0.0556 | 0.0578 | 1.4426 | -0.0385 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.0442 | 0.0798 | 0.2626 | 0.1684 |
| 82 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.0442 | 0.0798 | 0.2626 | 0.1684 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0369 | 0.0738 | -0.2188 | 0.1684 |
| 84 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0369 | 0.0738 | -0.2188 | 0.1684 |
| 85 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0369 | 0.0738 | -0.2188 | 0.1684 |
| 86 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0369 | 0.0738 | -0.2188 | 0.1684 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.0323 | 0.0707 | -0.1917 | -0.1684 |
| 88 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.0323 | 0.0707 | -0.1917 | -0.1684 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 45 | 0.0348 | 0.0436 | -0.2581 | -0.1348 |
| 90 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 45 | 0.0348 | 0.0436 | -0.2581 | -0.1348 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.0241 | 0.0337 | 0.4460 | 0.0539 |
| 92 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.0241 | 0.0337 | 0.4460 | 0.0539 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 45 | 0.0219 | 0.0252 | -0.1625 | -0.1348 |
| 94 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 45 | 0.0219 | 0.0252 | -0.1625 | -0.1348 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.0223 | 0.0223 | -0.8666 | -0.0257 |
| 96 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.0223 | 0.0223 | -0.8666 | -0.0257 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | -0.0191 | 0.0284 | -0.3849 | 0.0495 |
| 98 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | -0.0191 | 0.0284 | -0.3849 | 0.0495 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.0198 | 0.0227 | -0.3987 | -0.0495 |
| 100 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.0198 | 0.0227 | -0.3987 | -0.0495 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 103 | label_Hbb | label_Hcc | -1.1085 | 0.1443 |
| 2 | mod.fc.0 | 8 | label_Hbb | label_Hcc | -0.8819 | 0.1443 |
| 3 | mod.fc.0 | 121 | label_Hbb | label_Hcc | 0.6736 | 0.1443 |
| 4 | mod.fc.0 | 45 | label_Hbb | label_Hcc | 0.5391 | 0.1443 |
| 5 | mod.fc.0 | 76 | label_Hbb | label_Hcc | 0.5133 | 0.1443 |
| 6 | mod.fc.0 | 57 | label_Hbb | label_Hcc | -0.3565 | 0.1443 |
| 7 | mod.fc.0 | 58 | label_Hbb | label_Hcc | 0.3124 | 0.1443 |
| 8 | mod.fc.0 | 23 | label_Hbb | label_Hcc | 0.2249 | 0.1443 |
| 9 | mod.fc.0 | 3 | label_Hbb | label_Hcc | -0.2157 | 0.1443 |
| 10 | mod.fc.0 | 18 | label_Hbb | label_Hcc | -0.1982 | 0.1443 |
| 11 | mod.fc.0 | 54 | label_Hbb | label_Hcc | -0.1572 | 0.1443 |
| 12 | mod.fc.0 | 34 | label_Hbb | label_Hcc | -0.1541 | 0.1443 |
| 13 | mod.fc.0 | 82 | label_Hbb | label_Hcc | -0.1485 | 0.1443 |
| 14 | mod.fc.0 | 79 | label_Hbb | label_Hcc | 0.1283 | 0.1443 |
| 15 | mod.fc.0 | 124 | label_Hbb | label_Hcc | 0.1225 | 0.1443 |
| 16 | mod.fc.0 | 123 | label_Hbb | label_Hcc | -0.1092 | 0.1443 |
| 17 | mod.fc.0 | 10 | label_Hbb | label_Hcc | -0.1028 | 0.1443 |
| 18 | mod.fc.0 | 66 | label_Hbb | label_Hcc | -0.0750 | 0.1443 |
| 19 | mod.fc.0 | 2 | label_Hbb | label_Hcc | -0.0708 | 0.1443 |
| 20 | mod.fc.0 | 96 | label_Hbb | label_Hcc | 0.0467 | 0.1443 |
| 21 | mod.fc.0 | 91 | label_Hbb | label_Hcc | -0.0307 | 0.1443 |
| 22 | mod.fc.0 | 80 | label_Hbb | label_Hcc | 0.0096 | 0.1443 |
| 23 | mod.fc.0 | 110 | label_Hbb | label_Hcc | -0.0076 | 0.1443 |
| 24 | mod.fc.0 | 6 | label_Hbb | label_Hcc | 0.0016 | 0.1443 |
| 25 | mod.fc.0 | 115 | label_Hbb | label_Hcc | 5.403e-04 | 0.1443 |
| 26 | mod.fc.0 | 78 | label_Hbb | label_Hcc | 6.303e-05 | 0.1443 |
| 27 | mod.fc.0 | 38 | label_Hbb | label_Hcc | -5.013e-05 | 0.1443 |
| 28 | mod.fc.0 | 49 | label_Hbb | label_Hcc | -2.782e-05 | 0.1443 |
| 29 | mod.fc.0 | 81 | label_Hbb | label_Hcc | -2.077e-05 | 0.1443 |
| 30 | mod.fc.0 | 118 | label_Hbb | label_Hcc | -1.910e-05 | 0.1443 |
| 31 | mod.fc.0 | 19 | label_Hbb | label_Hcc | -1.899e-05 | 0.1443 |
| 32 | mod.fc.0 | 20 | label_Hbb | label_Hcc | 1.606e-05 | 0.1443 |
| 33 | mod.fc.0 | 64 | label_Hbb | label_Hcc | -1.547e-05 | 0.1443 |
| 34 | mod.fc.0 | 112 | label_Hbb | label_Hcc | -1.504e-05 | 0.1443 |
| 35 | mod.fc.0 | 89 | label_Hbb | label_Hcc | -1.455e-05 | 0.1443 |
| 36 | mod.fc.0 | 119 | label_Hbb | label_Hcc | 1.406e-05 | 0.1443 |
| 37 | mod.fc.0 | 113 | label_Hbb | label_Hcc | 1.395e-05 | 0.1443 |
| 38 | mod.fc.0 | 46 | label_Hbb | label_Hcc | -1.262e-05 | 0.1443 |
| 39 | mod.fc.0 | 92 | label_Hbb | label_Hcc | 1.224e-05 | 0.1443 |
| 40 | mod.fc.0 | 67 | label_Hbb | label_Hcc | 1.198e-05 | 0.1443 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
