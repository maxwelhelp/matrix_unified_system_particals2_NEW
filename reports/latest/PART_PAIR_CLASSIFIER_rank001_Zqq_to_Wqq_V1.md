# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **250**
- src_label: `label_Zqq`
- tgt_label: `label_Wqq`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 0.2897 | 0.6776 | 12.2446 | 0.1768 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 0.2897 | 0.6776 | 12.2446 | 0.1768 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 0.1685 | 0.9337 | 11.5856 | 0.1768 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 0.1685 | 0.9337 | 11.5856 | 0.1768 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 0.2557 | 0.4251 | 4.2863 | 0.2915 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 0.2557 | 0.4251 | 4.2863 | 0.2915 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.1050 | 0.9386 | 12.1384 | 0.1768 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.1050 | 0.9386 | 12.1384 | 0.1768 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.1050 | 0.9386 | 12.1384 | 0.1768 |
| 10 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.1050 | 0.9386 | 12.1384 | 0.1768 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 0.2024 | 0.3722 | 4.2159 | 0.2915 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 0.2024 | 0.3722 | 4.2159 | 0.2915 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.1302 | 0.7122 | 11.6518 | 0.1768 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.1302 | 0.7122 | 11.6518 | 0.1768 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.1389 | 0.3561 | 4.5138 | 0.2915 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.1389 | 0.3561 | 4.5138 | 0.2915 |
| 17 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.1389 | 0.3561 | 4.5138 | 0.2915 |
| 18 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.1389 | 0.3561 | 4.5138 | 0.2915 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.0963 | 0.2817 | 3.8751 | 0.2915 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.0963 | 0.2817 | 3.8751 | 0.2915 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 7 | 0.5511 | 0.5511 | 4.4085 | 0.1250 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 7 | 0.5511 | 0.5511 | 4.4085 | 0.1250 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 7 | 0.5218 | 0.5218 | 4.1744 | 0.1250 |
| 4 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 7 | 0.5218 | 0.5218 | 4.1744 | 0.1250 |
| 5 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 7 | 0.5218 | 0.5218 | 4.1744 | 0.1250 |
| 6 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 7 | 0.5218 | 0.5218 | 4.1744 | 0.1250 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 6 | 0.4688 | 0.4688 | 3.7507 | 0.1250 |
| 8 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 6 | 0.4688 | 0.4688 | 3.7507 | 0.1250 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | -0.4168 | 0.4168 | 3.3346 | -0.1250 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 6 | -0.4168 | 0.4168 | 3.3346 | -0.1250 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | -0.4168 | 0.4168 | 3.3346 | -0.1250 |
| 12 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 6 | -0.4168 | 0.4168 | 3.3346 | -0.1250 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 6 | 0.4089 | 0.4089 | 3.2712 | 0.1250 |
| 14 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 6 | 0.4089 | 0.4089 | 3.2712 | 0.1250 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 6 | -0.3826 | 0.3826 | 3.0607 | -0.1250 |
| 16 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 6 | -0.3826 | 0.3826 | 3.0607 | -0.1250 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 7 | -0.2787 | 0.3033 | 2.2292 | -0.1250 |
| 18 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 7 | -0.2787 | 0.3033 | 2.2292 | -0.1250 |
| 19 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 7 | -0.1791 | 0.2088 | 1.4330 | -0.1250 |
| 20 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 7 | -0.1791 | 0.2088 | 1.4330 | -0.1250 |
| 21 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.1004 | 0.1004 | 0.5504 | 0.1825 |
| 22 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.1004 | 0.1004 | 0.5504 | 0.1825 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.0814 | 0.0821 | -0.9463 | -0.0860 |
| 24 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.0814 | 0.0821 | -0.9463 | -0.0860 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | 0.0693 | 0.0693 | -0.6128 | -0.1130 |
| 26 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | 0.0693 | 0.0693 | -0.6128 | -0.1130 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | 0.0667 | 0.0810 | -0.3653 | -0.1825 |
| 28 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | 0.0667 | 0.0810 | -0.3653 | -0.1825 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.0678 | 0.0705 | 0.3717 | 0.1825 |
| 30 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.0678 | 0.0705 | 0.3717 | 0.1825 |
| 31 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.0678 | 0.0705 | 0.3717 | 0.1825 |
| 32 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.0678 | 0.0705 | 0.3717 | 0.1825 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.0647 | 0.0821 | -0.7525 | -0.0860 |
| 34 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.0647 | 0.0821 | -0.7525 | -0.0860 |
| 35 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.0647 | 0.0821 | -0.7525 | -0.0860 |
| 36 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.0647 | 0.0821 | -0.7525 | -0.0860 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.0376 | 0.0376 | 2.2970 | 0.0164 |
| 38 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.0376 | 0.0376 | 2.2970 | 0.0164 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.0357 | 0.0357 | 0.9115 | 0.0392 |
| 40 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.0357 | 0.0357 | 0.9115 | 0.0392 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.0330 | 0.0330 | 2.0132 | -0.0164 |
| 42 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.0330 | 0.0330 | 2.0132 | -0.0164 |
| 43 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.0330 | 0.0330 | 2.0132 | -0.0164 |
| 44 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.0330 | 0.0330 | 2.0132 | -0.0164 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | 0.0287 | 0.0377 | -0.2537 | -0.1130 |
| 46 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | 0.0287 | 0.0377 | -0.2537 | -0.1130 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0282 | 0.0380 | -0.6199 | -0.0454 |
| 48 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0282 | 0.0380 | -0.6199 | -0.0454 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.0280 | 0.0280 | 1.7082 | 0.0164 |
| 50 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.0280 | 0.0280 | 1.7082 | 0.0164 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.0272 | 0.0272 | 0.6174 | 0.0440 |
| 52 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.0272 | 0.0272 | 0.6174 | 0.0440 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 82 | 0.0255 | 0.0338 | -0.2988 | -0.0854 |
| 54 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 82 | 0.0255 | 0.0338 | -0.2988 | -0.0854 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | 0.0259 | 0.0295 | 0.6609 | 0.0392 |
| 56 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | 0.0259 | 0.0295 | 0.6609 | 0.0392 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0259 | 0.0259 | -0.6927 | -0.0374 |
| 58 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0259 | 0.0259 | -0.6927 | -0.0374 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0259 | 0.0259 | -0.6927 | -0.0374 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0259 | 0.0259 | -0.6927 | -0.0374 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0227 | 0.0320 | 0.5152 | 0.0440 |
| 62 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0227 | 0.0320 | 0.5152 | 0.0440 |
| 63 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0227 | 0.0320 | 0.5152 | 0.0440 |
| 64 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0227 | 0.0320 | 0.5152 | 0.0440 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | -0.0228 | 0.0236 | 1.3930 | -0.0164 |
| 66 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | -0.0228 | 0.0236 | 1.3930 | -0.0164 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.0219 | 0.0235 | -0.5862 | -0.0374 |
| 68 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.0219 | 0.0235 | -0.5862 | -0.0374 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.0200 | 0.0272 | -0.4404 | -0.0454 |
| 70 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.0200 | 0.0272 | -0.4404 | -0.0454 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.0146 | 0.0535 | 0.1704 | 0.0860 |
| 72 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.0146 | 0.0535 | 0.1704 | 0.0860 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | -0.0198 | 0.0216 | 0.5055 | -0.0392 |
| 74 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | -0.0198 | 0.0216 | 0.5055 | -0.0392 |
| 75 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | -0.0194 | 0.0218 | 0.4957 | -0.0392 |
| 76 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | -0.0194 | 0.0218 | 0.4957 | -0.0392 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | -0.0194 | 0.0218 | 0.4957 | -0.0392 |
| 78 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | -0.0194 | 0.0218 | 0.4957 | -0.0392 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 18 | 0.0152 | 0.0408 | -0.0834 | -0.1825 |
| 80 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 18 | 0.0152 | 0.0408 | -0.0834 | -0.1825 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | -0.0187 | 0.0213 | -0.4127 | 0.0454 |
| 82 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | -0.0187 | 0.0213 | -0.4127 | 0.0454 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 2 | 0.0171 | 0.0189 | 0.4251 | 0.0403 |
| 84 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 2 | 0.0171 | 0.0189 | 0.4251 | 0.0403 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | -0.0152 | 0.0200 | -0.4062 | 0.0374 |
| 86 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | -0.0152 | 0.0200 | -0.4062 | 0.0374 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 82 | 0.0148 | 0.0213 | 0.1728 | 0.0854 |
| 88 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 82 | 0.0148 | 0.0213 | 0.1728 | 0.0854 |
| 89 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0132 | 0.0217 | -0.2902 | 0.0454 |
| 90 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0132 | 0.0217 | -0.2902 | 0.0454 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0132 | 0.0217 | -0.2902 | 0.0454 |
| 92 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0132 | 0.0217 | -0.2902 | 0.0454 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.0146 | 0.0146 | -3.0478 | -0.0048 |
| 94 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.0146 | 0.0146 | -3.0478 | -0.0048 |
| 95 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0138 | 0.0138 | -2.8872 | -0.0048 |
| 96 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0138 | 0.0138 | -2.8872 | -0.0048 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0138 | 0.0138 | -2.8872 | -0.0048 |
| 98 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0138 | 0.0138 | -2.8872 | -0.0048 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 2 | 0.0132 | 0.0144 | 0.3276 | 0.0403 |
| 100 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 2 | 0.0132 | 0.0144 | 0.3276 | 0.0403 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 18 | label_Zqq | label_Wqq | 1.4597 | -0.2717 |
| 2 | mod.fc.0 | 66 | label_Zqq | label_Wqq | 0.9041 | -0.2717 |
| 3 | mod.fc.0 | 58 | label_Zqq | label_Wqq | 0.7005 | -0.2717 |
| 4 | mod.fc.0 | 79 | label_Zqq | label_Wqq | -0.6879 | -0.2717 |
| 5 | mod.fc.0 | 82 | label_Zqq | label_Wqq | 0.6835 | -0.2717 |
| 6 | mod.fc.0 | 96 | label_Zqq | label_Wqq | -0.6741 | -0.2717 |
| 7 | mod.fc.0 | 121 | label_Zqq | label_Wqq | 0.3634 | -0.2717 |
| 8 | mod.fc.0 | 76 | label_Zqq | label_Wqq | 0.3524 | -0.2717 |
| 9 | mod.fc.0 | 2 | label_Zqq | label_Wqq | -0.3226 | -0.2717 |
| 10 | mod.fc.0 | 10 | label_Zqq | label_Wqq | -0.3137 | -0.2717 |
| 11 | mod.fc.0 | 3 | label_Zqq | label_Wqq | -0.2989 | -0.2717 |
| 12 | mod.fc.0 | 8 | label_Zqq | label_Wqq | -0.1311 | -0.2717 |
| 13 | mod.fc.0 | 124 | label_Zqq | label_Wqq | -0.1244 | -0.2717 |
| 14 | mod.fc.0 | 23 | label_Zqq | label_Wqq | -0.0845 | -0.2717 |
| 15 | mod.fc.0 | 54 | label_Zqq | label_Wqq | 0.0786 | -0.2717 |
| 16 | mod.fc.0 | 57 | label_Zqq | label_Wqq | 0.0668 | -0.2717 |
| 17 | mod.fc.0 | 91 | label_Zqq | label_Wqq | -0.0419 | -0.2717 |
| 18 | mod.fc.0 | 103 | label_Zqq | label_Wqq | -0.0383 | -0.2717 |
| 19 | mod.fc.0 | 34 | label_Zqq | label_Wqq | 0.0295 | -0.2717 |
| 20 | mod.fc.0 | 45 | label_Zqq | label_Wqq | -0.0148 | -0.2717 |
| 21 | mod.fc.0 | 123 | label_Zqq | label_Wqq | 0.0117 | -0.2717 |
| 22 | mod.fc.0 | 80 | label_Zqq | label_Wqq | -0.0095 | -0.2717 |
| 23 | mod.fc.0 | 110 | label_Zqq | label_Wqq | -0.0027 | -0.2717 |
| 24 | mod.fc.0 | 6 | label_Zqq | label_Wqq | 0.0026 | -0.2717 |
| 25 | mod.fc.0 | 115 | label_Zqq | label_Wqq | 3.350e-04 | -0.2717 |
| 26 | mod.fc.0 | 78 | label_Zqq | label_Wqq | 7.588e-05 | -0.2717 |
| 27 | mod.fc.0 | 38 | label_Zqq | label_Wqq | -4.922e-05 | -0.2717 |
| 28 | mod.fc.0 | 11 | label_Zqq | label_Wqq | 3.402e-05 | -0.2717 |
| 29 | mod.fc.0 | 118 | label_Zqq | label_Wqq | 3.106e-05 | -0.2717 |
| 30 | mod.fc.0 | 20 | label_Zqq | label_Wqq | -1.930e-05 | -0.2717 |
| 31 | mod.fc.0 | 109 | label_Zqq | label_Wqq | 1.693e-05 | -0.2717 |
| 32 | mod.fc.0 | 51 | label_Zqq | label_Wqq | 1.577e-05 | -0.2717 |
| 33 | mod.fc.0 | 49 | label_Zqq | label_Wqq | -1.272e-05 | -0.2717 |
| 34 | mod.fc.0 | 40 | label_Zqq | label_Wqq | 1.138e-05 | -0.2717 |
| 35 | mod.fc.0 | 127 | label_Zqq | label_Wqq | -1.062e-05 | -0.2717 |
| 36 | mod.fc.0 | 52 | label_Zqq | label_Wqq | -1.041e-05 | -0.2717 |
| 37 | mod.fc.0 | 46 | label_Zqq | label_Wqq | -9.766e-06 | -0.2717 |
| 38 | mod.fc.0 | 29 | label_Zqq | label_Wqq | 8.084e-06 | -0.2717 |
| 39 | mod.fc.0 | 117 | label_Zqq | label_Wqq | 8.062e-06 | -0.2717 |
| 40 | mod.fc.0 | 98 | label_Zqq | label_Wqq | 7.758e-06 | -0.2717 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
