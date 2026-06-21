# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear `W_Tbl-W_Hqql` directions where available. This closes `CLS vector → class logits`.

- events: **96**
- rows: **480**
- summary_rows: **20**
- dim_rows: **250**

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 0.5514 | 1.3339 | 12.0215 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 0.5514 | 1.3339 | 12.0215 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 0.3447 | 1.8568 | 11.3397 | 0.3536 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 0.3447 | 1.8568 | 11.3397 | 0.3536 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2704 | 1.8885 | 11.8367 | 0.3536 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2704 | 1.8885 | 11.8367 | 0.3536 |
| 7 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2704 | 1.8885 | 11.8367 | 0.3536 |
| 8 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2704 | 1.8885 | 11.8367 | 0.3536 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 0.4835 | 0.7999 | 4.2812 | 0.5829 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 0.4835 | 0.7999 | 4.2812 | 0.5829 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 0.4126 | 0.7484 | 4.1812 | 0.5829 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 0.4126 | 0.7484 | 4.1812 | 0.5829 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.2384 | 1.4077 | 11.7948 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.2384 | 1.4077 | 11.7948 | 0.3536 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.3383 | 0.7393 | 4.4190 | 0.5829 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.3383 | 0.7393 | 4.4190 | 0.5829 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.3383 | 0.7393 | 4.4190 | 0.5829 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.3383 | 0.7393 | 4.4190 | 0.5829 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.1705 | 0.5441 | 3.8508 | 0.5829 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.1705 | 0.5441 | 3.8508 | 0.5829 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 7 | 1.1007 | 1.1007 | 4.4030 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 7 | 1.1007 | 1.1007 | 4.4030 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 7 | 1.0795 | 1.0795 | 4.3178 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 7 | 1.0795 | 1.0795 | 4.3178 | 0.2500 |
| 5 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 7 | 1.0795 | 1.0795 | 4.3178 | 0.2500 |
| 6 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 7 | 1.0795 | 1.0795 | 4.3178 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 6 | 0.9189 | 0.9189 | 3.6754 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 6 | 0.9189 | 0.9189 | 3.6754 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | -0.8091 | 0.8091 | 3.2363 | -0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 6 | -0.8091 | 0.8091 | 3.2363 | -0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | -0.8091 | 0.8091 | 3.2363 | -0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 6 | -0.8091 | 0.8091 | 3.2363 | -0.2500 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 6 | 0.8066 | 0.8066 | 3.2265 | 0.2500 |
| 14 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 6 | 0.8066 | 0.8066 | 3.2265 | 0.2500 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 6 | -0.7560 | 0.7560 | 3.0242 | -0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 6 | -0.7560 | 0.7560 | 3.0242 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 7 | -0.5682 | 0.6010 | 2.2728 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 7 | -0.5682 | 0.6010 | 2.2728 | -0.2500 |
| 19 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 7 | -0.3675 | 0.4150 | 1.4698 | -0.2500 |
| 20 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 7 | -0.3675 | 0.4150 | 1.4698 | -0.2500 |
| 21 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.2027 | 0.2027 | 0.5555 | 0.3649 |
| 22 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.2027 | 0.2027 | 0.5555 | 0.3649 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.1727 | 0.1737 | -1.0041 | -0.1720 |
| 24 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.1727 | 0.1737 | -1.0041 | -0.1720 |
| 25 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.1635 | 0.1670 | 0.4480 | 0.3649 |
| 26 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.1635 | 0.1670 | 0.4480 | 0.3649 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.1635 | 0.1670 | 0.4480 | 0.3649 |
| 28 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.1635 | 0.1670 | 0.4480 | 0.3649 |
| 29 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.1528 | 0.1755 | -0.8886 | -0.1720 |
| 30 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.1528 | 0.1755 | -0.8886 | -0.1720 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.1528 | 0.1755 | -0.8886 | -0.1720 |
| 32 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.1528 | 0.1755 | -0.8886 | -0.1720 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | 0.1288 | 0.1499 | -0.3531 | -0.3649 |
| 34 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | 0.1288 | 0.1499 | -0.3531 | -0.3649 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | 0.1068 | 0.1100 | -0.4726 | -0.2260 |
| 36 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | 0.1068 | 0.1100 | -0.4726 | -0.2260 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0729 | 0.0860 | -0.8020 | -0.0908 |
| 38 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0729 | 0.0860 | -0.8020 | -0.0908 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.0660 | 0.0675 | 2.0151 | 0.0328 |
| 40 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.0660 | 0.0675 | 2.0151 | 0.0328 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | 0.0601 | 0.0717 | -0.2661 | -0.2260 |
| 42 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | 0.0601 | 0.0717 | -0.2661 | -0.2260 |
| 43 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.0576 | 0.0576 | 1.7586 | -0.0328 |
| 44 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.0576 | 0.0576 | 1.7586 | -0.0328 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.0576 | 0.0576 | 1.7586 | -0.0328 |
| 46 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.0576 | 0.0576 | 1.7586 | -0.0328 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.0553 | 0.0553 | 1.6886 | 0.0328 |
| 48 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.0553 | 0.0553 | 1.6886 | 0.0328 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.0539 | 0.0590 | 0.6869 | 0.0784 |
| 50 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.0539 | 0.0590 | 0.6869 | 0.0784 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | 0.0531 | 0.0580 | 0.6775 | 0.0784 |
| 52 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | 0.0531 | 0.0580 | 0.6775 | 0.0784 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.0509 | 0.0530 | -0.6809 | -0.0747 |
| 54 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.0509 | 0.0530 | -0.6809 | -0.0747 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.0376 | 0.1044 | 0.2187 | 0.1720 |
| 56 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.0376 | 0.1044 | 0.2187 | 0.1720 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.0470 | 0.0529 | 0.5335 | 0.0881 |
| 58 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.0470 | 0.0529 | 0.5335 | 0.0881 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0463 | 0.0463 | -0.6196 | -0.0747 |
| 60 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0463 | 0.0463 | -0.6196 | -0.0747 |
| 61 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0463 | 0.0463 | -0.6196 | -0.0747 |
| 62 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0463 | 0.0463 | -0.6196 | -0.0747 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 82 | 0.0437 | 0.0593 | -0.2555 | -0.1709 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 82 | 0.0437 | 0.0593 | -0.2555 | -0.1709 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | -0.0431 | 0.0464 | 1.3156 | -0.0328 |
| 66 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | -0.0431 | 0.0464 | 1.3156 | -0.0328 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.0414 | 0.0519 | -0.4559 | -0.0908 |
| 68 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.0414 | 0.0519 | -0.4559 | -0.0908 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0381 | 0.0604 | 0.4324 | 0.0881 |
| 70 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0381 | 0.0604 | 0.4324 | 0.0881 |
| 71 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0381 | 0.0604 | 0.4324 | 0.0881 |
| 72 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0381 | 0.0604 | 0.4324 | 0.0881 |
| 73 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | -0.0408 | 0.0441 | 0.5203 | -0.0784 |
| 74 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | -0.0408 | 0.0441 | 0.5203 | -0.0784 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | -0.0408 | 0.0441 | 0.5203 | -0.0784 |
| 76 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | -0.0408 | 0.0441 | 0.5203 | -0.0784 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | -0.0399 | 0.0425 | 0.5092 | -0.0784 |
| 78 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | -0.0399 | 0.0425 | 0.5092 | -0.0784 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | -0.0353 | 0.0412 | -0.3881 | 0.0908 |
| 80 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | -0.0353 | 0.0412 | -0.3881 | 0.0908 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 2 | 0.0343 | 0.0366 | 0.4258 | 0.0807 |
| 82 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 2 | 0.0343 | 0.0366 | 0.4258 | 0.0807 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | -0.0322 | 0.0383 | -0.4309 | 0.0747 |
| 84 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | -0.0322 | 0.0383 | -0.4309 | 0.0747 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0299 | 0.0466 | -0.3289 | 0.0908 |
| 86 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0299 | 0.0466 | -0.3289 | 0.0908 |
| 87 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0299 | 0.0466 | -0.3289 | 0.0908 |
| 88 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0299 | 0.0466 | -0.3289 | 0.0908 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.0286 | 0.0286 | -2.9875 | -0.0096 |
| 90 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.0286 | 0.0286 | -2.9875 | -0.0096 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 82 | 0.0264 | 0.0386 | 0.1548 | 0.1709 |
| 92 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 82 | 0.0264 | 0.0386 | 0.1548 | 0.1709 |
| 93 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0281 | 0.0281 | -2.9404 | -0.0096 |
| 94 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0281 | 0.0281 | -2.9404 | -0.0096 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0281 | 0.0281 | -2.9404 | -0.0096 |
| 96 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0281 | 0.0281 | -2.9404 | -0.0096 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 2 | 0.0264 | 0.0281 | 0.3272 | 0.0807 |
| 98 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 2 | 0.0264 | 0.0281 | 0.3272 | 0.0807 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 58 | 0.0260 | 0.0289 | -0.1486 | -0.1751 |
| 100 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 58 | 0.0260 | 0.0289 | -0.1486 | -0.1751 |

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
