# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear `W_Tbl-W_Hqql` directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **268**

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.1289 | 1.4592 | 14.5730 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.1289 | 1.4592 | 14.5730 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.0928 | 1.5160 | 5.5365 | 0.4686 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.0928 | 1.5160 | 5.5365 | 0.4686 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.0122 | 1.5842 | 5.3393 | 0.4686 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.0122 | 1.5842 | 5.3393 | 0.4686 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 0.9762 | 1.7325 | 12.6692 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 0.9762 | 1.7325 | 12.6692 | 0.3536 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.3813 | 1.2239 | 12.7288 | 0.3536 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.3813 | 1.2239 | 12.7288 | 0.3536 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3217 | 1.4718 | 12.8175 | 0.3536 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3217 | 1.4718 | 12.8175 | 0.3536 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3217 | 1.4718 | 12.8175 | 0.3536 |
| 14 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3217 | 1.4718 | 12.8175 | 0.3536 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.3578 | 0.9408 | 4.4973 | 0.4686 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.3578 | 0.9408 | 4.4973 | 0.4686 |
| 17 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.3578 | 0.9408 | 4.4973 | 0.4686 |
| 18 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.3578 | 0.9408 | 4.4973 | 0.4686 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.3452 | 0.9485 | 4.1971 | 0.4686 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.3452 | 0.9485 | 4.1971 | 0.4686 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | 0.8775 | 0.8775 | 3.5101 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 1 | 0.8775 | 0.8775 | 3.5101 | 0.2500 |
| 7 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | 0.8775 | 0.8775 | 3.5101 | 0.2500 |
| 8 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 1 | 0.8775 | 0.8775 | 3.5101 | 0.2500 |
| 9 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 2 | 0.8017 | 0.8017 | 3.2069 | 0.2500 |
| 10 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 2 | 0.8017 | 0.8017 | 3.2069 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.7107 | 0.7247 | -2.5646 | -0.2771 |
| 12 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.7107 | 0.7247 | -2.5646 | -0.2771 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | -0.5558 | 0.5942 | 2.2232 | -0.2500 |
| 14 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 2 | -0.5558 | 0.5942 | 2.2232 | -0.2500 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | -0.5558 | 0.5942 | 2.2232 | -0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 2 | -0.5558 | 0.5942 | 2.2232 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 1 | -0.4205 | 0.4222 | 1.6819 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 1 | -0.4205 | 0.4222 | 1.6819 | -0.2500 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.3802 | 0.4801 | 1.3720 | 0.2771 |
| 20 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.3802 | 0.4801 | 1.3720 | 0.2771 |
| 21 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 2 | -0.3553 | 0.4010 | 1.4213 | -0.2500 |
| 22 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 2 | -0.3553 | 0.4010 | 1.4213 | -0.2500 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.3269 | 0.3669 | 1.4828 | 0.2205 |
| 24 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.3269 | 0.3669 | 1.4828 | 0.2205 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.2670 | 0.2770 | -0.9634 | -0.2771 |
| 26 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.2670 | 0.2770 | -0.9634 | -0.2771 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.2090 | 0.2327 | 0.9480 | 0.2205 |
| 28 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.2090 | 0.2327 | 0.9480 | 0.2205 |
| 29 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.2090 | 0.2327 | 0.9480 | 0.2205 |
| 30 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.2090 | 0.2327 | 0.9480 | 0.2205 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.2103 | 0.2156 | -1.2485 | -0.1684 |
| 32 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.2103 | 0.2156 | -1.2485 | -0.1684 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.1486 | 0.1486 | 1.1582 | 0.1283 |
| 34 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.1486 | 0.1486 | 1.1582 | 0.1283 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.1172 | 0.2380 | 0.4230 | 0.2771 |
| 36 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.1172 | 0.2380 | 0.4230 | 0.2771 |
| 37 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.1172 | 0.2380 | 0.4230 | 0.2771 |
| 38 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.1172 | 0.2380 | 0.4230 | 0.2771 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.1318 | 0.1318 | 1.4786 | 0.0891 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.1318 | 0.1318 | 1.4786 | 0.0891 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.1193 | 0.1193 | 3.7199 | 0.0321 |
| 42 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.1193 | 0.1193 | 3.7199 | 0.0321 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.0986 | 0.1973 | -0.4474 | -0.2205 |
| 44 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.0986 | 0.1973 | -0.4474 | -0.2205 |
| 45 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.1037 | 0.1037 | 3.2308 | -0.0321 |
| 46 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.1037 | 0.1037 | 3.2308 | -0.0321 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.1037 | 0.1037 | 3.2308 | -0.0321 |
| 48 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.1037 | 0.1037 | 3.2308 | -0.0321 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | -0.1030 | 0.1030 | 3.2114 | -0.0321 |
| 50 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | -0.1030 | 0.1030 | 3.2114 | -0.0321 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.0707 | 0.2022 | -0.3205 | -0.2205 |
| 52 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.0707 | 0.2022 | -0.3205 | -0.2205 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.0924 | 0.0924 | 0.7197 | 0.1283 |
| 54 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.0924 | 0.0924 | 0.7197 | 0.1283 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | 0.0913 | 0.0913 | 2.8464 | 0.0321 |
| 56 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | 0.0913 | 0.0913 | 2.8464 | 0.0321 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0750 | 0.0750 | 1.9475 | 0.0385 |
| 58 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0750 | 0.0750 | 1.9475 | 0.0385 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0750 | 0.0750 | 1.9475 | 0.0385 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0750 | 0.0750 | 1.9475 | 0.0385 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | -0.0668 | 0.0668 | 1.7332 | -0.0385 |
| 62 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | -0.0668 | 0.0668 | 1.7332 | -0.0385 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | -0.0645 | 0.0781 | 0.7232 | -0.0891 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | -0.0645 | 0.0781 | 0.7232 | -0.0891 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0655 | 0.0655 | 0.7352 | 0.0891 |
| 66 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0655 | 0.0655 | 0.7352 | 0.0891 |
| 67 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0655 | 0.0655 | 0.7352 | 0.0891 |
| 68 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0655 | 0.0655 | 0.7352 | 0.0891 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | -0.0642 | 0.0642 | 0.7198 | -0.0891 |
| 70 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | -0.0642 | 0.0642 | 0.7198 | -0.0891 |
| 71 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0577 | 0.0830 | 0.4496 | -0.1283 |
| 72 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0577 | 0.0830 | 0.4496 | -0.1283 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0577 | 0.0830 | 0.4496 | -0.1283 |
| 74 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0577 | 0.0830 | 0.4496 | -0.1283 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | 0.0584 | 0.0662 | 1.5164 | 0.0385 |
| 76 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | 0.0584 | 0.0662 | 1.5164 | 0.0385 |
| 77 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 1 | -0.0045 | 0.3258 | 0.0180 | -0.2500 |
| 78 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 1 | -0.0045 | 0.3258 | 0.0180 | -0.2500 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | -0.0556 | 0.0578 | 1.4426 | -0.0385 |
| 80 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | -0.0556 | 0.0578 | 1.4426 | -0.0385 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0442 | 0.0798 | 0.2626 | 0.1684 |
| 82 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0442 | 0.0798 | 0.2626 | 0.1684 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | -0.0369 | 0.0738 | -0.2188 | 0.1684 |
| 84 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | -0.0369 | 0.0738 | -0.2188 | 0.1684 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0323 | 0.0707 | -0.1917 | -0.1684 |
| 86 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0323 | 0.0707 | -0.1917 | -0.1684 |
| 87 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0323 | 0.0707 | -0.1917 | -0.1684 |
| 88 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0323 | 0.0707 | -0.1917 | -0.1684 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 45 | 0.0348 | 0.0436 | -0.2581 | -0.1348 |
| 90 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 45 | 0.0348 | 0.0436 | -0.2581 | -0.1348 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.0241 | 0.0337 | 0.4460 | 0.0539 |
| 92 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.0241 | 0.0337 | 0.4460 | 0.0539 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 45 | 0.0219 | 0.0252 | -0.1625 | -0.1348 |
| 94 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 45 | 0.0219 | 0.0252 | -0.1625 | -0.1348 |
| 95 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 45 | 0.0219 | 0.0252 | -0.1625 | -0.1348 |
| 96 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 45 | 0.0219 | 0.0252 | -0.1625 | -0.1348 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.0223 | 0.0223 | -0.8666 | -0.0257 |
| 98 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.0223 | 0.0223 | -0.8666 | -0.0257 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | -0.0191 | 0.0284 | -0.3849 | 0.0495 |
| 100 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | -0.0191 | 0.0284 | -0.3849 | 0.0495 |

## Exact final linear Tbl-Hqql direction
| rank | module | dim | W_Tbl_minus_Hqql | bias_Tbl_minus_Hqql |
| --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 54 | -1.6964 | -0.6703 |
| 2 | mod.fc.0 | 76 | 1.4146 | -0.6703 |
| 3 | mod.fc.0 | 18 | -1.2686 | -0.6703 |
| 4 | mod.fc.0 | 103 | 1.2515 | -0.6703 |
| 5 | mod.fc.0 | 121 | 0.9775 | -0.6703 |
| 6 | mod.fc.0 | 96 | -0.7730 | -0.6703 |
| 7 | mod.fc.0 | 58 | 0.5745 | -0.6703 |
| 8 | mod.fc.0 | 23 | 0.5696 | -0.6703 |
| 9 | mod.fc.0 | 45 | -0.4822 | -0.6703 |
| 10 | mod.fc.0 | 57 | 0.4719 | -0.6703 |
| 11 | mod.fc.0 | 10 | -0.3489 | -0.6703 |
| 12 | mod.fc.0 | 8 | 0.2327 | -0.6703 |
| 13 | mod.fc.0 | 2 | 0.2039 | -0.6703 |
| 14 | mod.fc.0 | 91 | 0.1842 | -0.6703 |
| 15 | mod.fc.0 | 34 | -0.1708 | -0.6703 |
| 16 | mod.fc.0 | 79 | -0.1077 | -0.6703 |
| 17 | mod.fc.0 | 6 | 0.0887 | -0.6703 |
| 18 | mod.fc.0 | 66 | 0.0838 | -0.6703 |
| 19 | mod.fc.0 | 3 | 0.0658 | -0.6703 |
| 20 | mod.fc.0 | 80 | -0.0510 | -0.6703 |
| 21 | mod.fc.0 | 110 | -0.0399 | -0.6703 |
| 22 | mod.fc.0 | 123 | 0.0129 | -0.6703 |
| 23 | mod.fc.0 | 124 | 0.0039 | -0.6703 |
| 24 | mod.fc.0 | 82 | 0.0031 | -0.6703 |
| 25 | mod.fc.0 | 78 | -0.0022 | -0.6703 |
| 26 | mod.fc.0 | 115 | -3.447e-04 | -0.6703 |
| 27 | mod.fc.0 | 49 | -2.977e-05 | -0.6703 |
| 28 | mod.fc.0 | 118 | 2.434e-05 | -0.6703 |
| 29 | mod.fc.0 | 87 | 2.198e-05 | -0.6703 |
| 30 | mod.fc.0 | 74 | -1.706e-05 | -0.6703 |
| 31 | mod.fc.0 | 125 | 1.705e-05 | -0.6703 |
| 32 | mod.fc.0 | 111 | 1.638e-05 | -0.6703 |
| 33 | mod.fc.0 | 70 | -1.551e-05 | -0.6703 |
| 34 | mod.fc.0 | 50 | 1.345e-05 | -0.6703 |
| 35 | mod.fc.0 | 15 | -1.341e-05 | -0.6703 |
| 36 | mod.fc.0 | 81 | -1.294e-05 | -0.6703 |
| 37 | mod.fc.0 | 38 | -1.277e-05 | -0.6703 |
| 38 | mod.fc.0 | 108 | 1.259e-05 | -0.6703 |
| 39 | mod.fc.0 | 29 | 1.211e-05 | -0.6703 |
| 40 | mod.fc.0 | 61 | 1.161e-05 | -0.6703 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[Tbl,dim] - W[Hqql,dim]
positive supports J = Tbl-Hqql; negative resists it.
```
