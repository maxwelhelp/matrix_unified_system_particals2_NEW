# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear `W_Tbl-W_Hqql` directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **250**

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 0.5794 | 1.3553 | 12.2446 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 0.5794 | 1.3553 | 12.2446 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 0.3369 | 1.8673 | 11.5856 | 0.3536 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 0.3369 | 1.8673 | 11.5856 | 0.3536 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 0.5115 | 0.8502 | 4.2863 | 0.5829 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 0.5115 | 0.8502 | 4.2863 | 0.5829 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2100 | 1.8773 | 12.1384 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2100 | 1.8773 | 12.1384 | 0.3536 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2100 | 1.8773 | 12.1384 | 0.3536 |
| 10 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2100 | 1.8773 | 12.1384 | 0.3536 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 0.4048 | 0.7445 | 4.2159 | 0.5829 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 0.4048 | 0.7445 | 4.2159 | 0.5829 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.2605 | 1.4244 | 11.6518 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.2605 | 1.4244 | 11.6518 | 0.3536 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2779 | 0.7122 | 4.5138 | 0.5829 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2779 | 0.7122 | 4.5138 | 0.5829 |
| 17 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2779 | 0.7122 | 4.5138 | 0.5829 |
| 18 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2779 | 0.7122 | 4.5138 | 0.5829 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.1926 | 0.5634 | 3.8751 | 0.5829 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.1926 | 0.5634 | 3.8751 | 0.5829 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 7 | 1.1021 | 1.1021 | 4.4085 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 7 | 1.1021 | 1.1021 | 4.4085 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 7 | 1.0436 | 1.0436 | 4.1744 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 7 | 1.0436 | 1.0436 | 4.1744 | 0.2500 |
| 5 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 7 | 1.0436 | 1.0436 | 4.1744 | 0.2500 |
| 6 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 7 | 1.0436 | 1.0436 | 4.1744 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | -0.8337 | 0.8337 | 3.3346 | -0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 6 | -0.8337 | 0.8337 | 3.3346 | -0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | -0.8337 | 0.8337 | 3.3346 | -0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 6 | -0.8337 | 0.8337 | 3.3346 | -0.2500 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 6 | 0.8178 | 0.8178 | 3.2712 | 0.2500 |
| 14 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 6 | 0.8178 | 0.8178 | 3.2712 | 0.2500 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 6 | -0.7652 | 0.7652 | 3.0607 | -0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 6 | -0.7652 | 0.7652 | 3.0607 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 7 | -0.5573 | 0.6066 | 2.2292 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 7 | -0.5573 | 0.6066 | 2.2292 | -0.2500 |
| 19 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 7 | -0.3583 | 0.4176 | 1.4330 | -0.2500 |
| 20 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 7 | -0.3583 | 0.4176 | 1.4330 | -0.2500 |
| 21 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.2009 | 0.2009 | 0.5504 | 0.3649 |
| 22 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.2009 | 0.2009 | 0.5504 | 0.3649 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.1628 | 0.1643 | -0.9463 | -0.1720 |
| 24 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.1628 | 0.1643 | -0.9463 | -0.1720 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | 0.1385 | 0.1385 | -0.6128 | -0.2260 |
| 26 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | 0.1385 | 0.1385 | -0.6128 | -0.2260 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | 0.1333 | 0.1620 | -0.3653 | -0.3649 |
| 28 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | 0.1333 | 0.1620 | -0.3653 | -0.3649 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.1357 | 0.1410 | 0.3717 | 0.3649 |
| 30 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.1357 | 0.1410 | 0.3717 | 0.3649 |
| 31 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.1357 | 0.1410 | 0.3717 | 0.3649 |
| 32 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.1357 | 0.1410 | 0.3717 | 0.3649 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.1294 | 0.1642 | -0.7525 | -0.1720 |
| 34 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.1294 | 0.1642 | -0.7525 | -0.1720 |
| 35 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.1294 | 0.1642 | -0.7525 | -0.1720 |
| 36 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.1294 | 0.1642 | -0.7525 | -0.1720 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.0753 | 0.0753 | 2.2970 | 0.0328 |
| 38 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.0753 | 0.0753 | 2.2970 | 0.0328 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.0715 | 0.0715 | 0.9115 | 0.0784 |
| 40 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.0715 | 0.0715 | 0.9115 | 0.0784 |
| 41 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.0660 | 0.0660 | 2.0132 | -0.0328 |
| 42 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.0660 | 0.0660 | 2.0132 | -0.0328 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.0660 | 0.0660 | 2.0132 | -0.0328 |
| 44 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.0660 | 0.0660 | 2.0132 | -0.0328 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | 0.0574 | 0.0755 | -0.2537 | -0.2260 |
| 46 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | 0.0574 | 0.0755 | -0.2537 | -0.2260 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0563 | 0.0760 | -0.6199 | -0.0908 |
| 48 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0563 | 0.0760 | -0.6199 | -0.0908 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.0560 | 0.0560 | 1.7082 | 0.0328 |
| 50 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.0560 | 0.0560 | 1.7082 | 0.0328 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.0544 | 0.0544 | 0.6174 | 0.0881 |
| 52 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.0544 | 0.0544 | 0.6174 | 0.0881 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 82 | 0.0511 | 0.0677 | -0.2988 | -0.1709 |
| 54 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 82 | 0.0511 | 0.0677 | -0.2988 | -0.1709 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | 0.0518 | 0.0591 | 0.6609 | 0.0784 |
| 56 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | 0.0518 | 0.0591 | 0.6609 | 0.0784 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0518 | 0.0518 | -0.6927 | -0.0747 |
| 58 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0518 | 0.0518 | -0.6927 | -0.0747 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0518 | 0.0518 | -0.6927 | -0.0747 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0518 | 0.0518 | -0.6927 | -0.0747 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0454 | 0.0639 | 0.5152 | 0.0881 |
| 62 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0454 | 0.0639 | 0.5152 | 0.0881 |
| 63 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0454 | 0.0639 | 0.5152 | 0.0881 |
| 64 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0454 | 0.0639 | 0.5152 | 0.0881 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | -0.0457 | 0.0472 | 1.3930 | -0.0328 |
| 66 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | -0.0457 | 0.0472 | 1.3930 | -0.0328 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.0438 | 0.0469 | -0.5862 | -0.0747 |
| 68 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.0438 | 0.0469 | -0.5862 | -0.0747 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.0400 | 0.0544 | -0.4404 | -0.0908 |
| 70 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.0400 | 0.0544 | -0.4404 | -0.0908 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.0293 | 0.1069 | 0.1704 | 0.1720 |
| 72 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.0293 | 0.1069 | 0.1704 | 0.1720 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | -0.0396 | 0.0433 | 0.5055 | -0.0784 |
| 74 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | -0.0396 | 0.0433 | 0.5055 | -0.0784 |
| 75 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | -0.0389 | 0.0437 | 0.4957 | -0.0784 |
| 76 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | -0.0389 | 0.0437 | 0.4957 | -0.0784 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | -0.0389 | 0.0437 | 0.4957 | -0.0784 |
| 78 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | -0.0389 | 0.0437 | 0.4957 | -0.0784 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 18 | 0.0304 | 0.0817 | -0.0834 | -0.3649 |
| 80 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 18 | 0.0304 | 0.0817 | -0.0834 | -0.3649 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | -0.0375 | 0.0426 | -0.4127 | 0.0908 |
| 82 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | -0.0375 | 0.0426 | -0.4127 | 0.0908 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 2 | 0.0343 | 0.0378 | 0.4251 | 0.0807 |
| 84 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 2 | 0.0343 | 0.0378 | 0.4251 | 0.0807 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | -0.0304 | 0.0400 | -0.4062 | 0.0747 |
| 86 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | -0.0304 | 0.0400 | -0.4062 | 0.0747 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 82 | 0.0295 | 0.0425 | 0.1728 | 0.1709 |
| 88 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 82 | 0.0295 | 0.0425 | 0.1728 | 0.1709 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0264 | 0.0434 | -0.2902 | 0.0908 |
| 90 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0264 | 0.0434 | -0.2902 | 0.0908 |
| 91 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0264 | 0.0434 | -0.2902 | 0.0908 |
| 92 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0264 | 0.0434 | -0.2902 | 0.0908 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.0292 | 0.0292 | -3.0478 | -0.0096 |
| 94 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.0292 | 0.0292 | -3.0478 | -0.0096 |
| 95 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0276 | 0.0276 | -2.8872 | -0.0096 |
| 96 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0276 | 0.0276 | -2.8872 | -0.0096 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0276 | 0.0276 | -2.8872 | -0.0096 |
| 98 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0276 | 0.0276 | -2.8872 | -0.0096 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 2 | 0.0264 | 0.0289 | 0.3276 | 0.0807 |
| 100 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 2 | 0.0264 | 0.0289 | 0.3276 | 0.0807 |

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
