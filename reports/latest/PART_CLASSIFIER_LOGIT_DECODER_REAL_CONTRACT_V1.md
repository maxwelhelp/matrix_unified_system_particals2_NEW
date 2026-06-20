# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear `W_Tbl-W_Hqql` directions where available. This closes `CLS vector → class logits`.

- events: **128**
- rows: **640**
- summary_rows: **20**
- dim_rows: **272**

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.0511 | 2.5354 | 17.0118 | 0.1768 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.0511 | 2.5354 | 17.0118 | 0.1768 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.1348 | 1.2420 | 5.3029 | 0.4152 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.1348 | 1.2420 | 5.3029 | 0.4152 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 0.9209 | 2.2032 | 15.1223 | 0.1768 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 0.9209 | 2.2032 | 15.1223 | 0.1768 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 0.8371 | 1.1515 | 5.0453 | 0.4152 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 0.8371 | 1.1515 | 5.0453 | 0.4152 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.1997 | 2.3062 | 14.4132 | 0.1768 |
| 10 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.1997 | 2.3062 | 14.4132 | 0.1768 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.1997 | 2.3062 | 14.4132 | 0.1768 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.1997 | 2.3062 | 14.4132 | 0.1768 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.1943 | 2.2545 | 13.6941 | 0.1768 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.1943 | 2.2545 | 13.6941 | 0.1768 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2835 | 0.6556 | 4.1072 | 0.4152 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2835 | 0.6556 | 4.1072 | 0.4152 |
| 17 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2835 | 0.6556 | 4.1072 | 0.4152 |
| 18 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2835 | 0.6556 | 4.1072 | 0.4152 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.1105 | 0.6190 | 3.9818 | 0.4152 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.1105 | 0.6190 | 3.9818 | 0.4152 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 9 | 1.7917 | 1.7917 | 14.3335 | 0.1250 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 9 | 1.7917 | 1.7917 | 14.3335 | 0.1250 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 5 | 1.5515 | 1.5515 | 12.4118 | 0.1250 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 5 | 1.5515 | 1.5515 | 12.4118 | 0.1250 |
| 5 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 9 | 1.2529 | 1.2529 | 10.0234 | 0.1250 |
| 6 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 9 | 1.2529 | 1.2529 | 10.0234 | 0.1250 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 9 | 1.2529 | 1.2529 | 10.0234 | 0.1250 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 9 | 1.2529 | 1.2529 | 10.0234 | 0.1250 |
| 9 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 5 | 1.2244 | 1.2244 | 9.7952 | 0.1250 |
| 10 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 5 | 1.2244 | 1.2244 | 9.7952 | 0.1250 |
| 11 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 5 | -1.0532 | 1.0532 | 8.4258 | -0.1250 |
| 12 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 5 | -1.0532 | 1.0532 | 8.4258 | -0.1250 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 5 | -1.0532 | 1.0532 | 8.4258 | -0.1250 |
| 14 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 5 | -1.0532 | 1.0532 | 8.4258 | -0.1250 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 9 | -1.0301 | 1.0301 | 8.2409 | -0.1250 |
| 16 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 9 | -1.0301 | 1.0301 | 8.2409 | -0.1250 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 5 | -0.7406 | 0.7437 | 5.9250 | -0.1250 |
| 18 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 5 | -0.7406 | 0.7437 | 5.9250 | -0.1250 |
| 19 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 9 | -0.6306 | 0.6517 | 5.0449 | -0.1250 |
| 20 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 9 | -0.6306 | 0.6517 | 5.0449 | -0.1250 |
| 21 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.3767 | 0.3767 | -2.4078 | -0.1564 |
| 22 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.3767 | 0.3767 | -2.4078 | -0.1564 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.2990 | 0.2990 | -1.6909 | -0.1768 |
| 24 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.2990 | 0.2990 | -1.6909 | -0.1768 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.2500 | 0.2662 | 1.5978 | 0.1564 |
| 26 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.2500 | 0.2662 | 1.5978 | 0.1564 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.1712 | 0.2146 | 0.9681 | 0.1768 |
| 28 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.1712 | 0.2146 | 0.9681 | 0.1768 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 54 | 0.1759 | 0.1759 | -0.8295 | -0.2121 |
| 30 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 54 | 0.1759 | 0.1759 | -0.8295 | -0.2121 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.1709 | 0.1709 | -1.0776 | -0.1586 |
| 32 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.1709 | 0.1709 | -1.0776 | -0.1586 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.1507 | 0.1590 | -0.8523 | -0.1768 |
| 34 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.1507 | 0.1590 | -0.8523 | -0.1768 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.1206 | 0.1381 | -0.7706 | -0.1564 |
| 36 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.1206 | 0.1381 | -0.7706 | -0.1564 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | 0.0885 | 0.1037 | 0.5584 | 0.1586 |
| 38 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | 0.0885 | 0.1037 | 0.5584 | 0.1586 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.0863 | 0.0968 | 0.7065 | 0.1222 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.0863 | 0.0968 | 0.7065 | 0.1222 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 54 | 0.0852 | 0.0862 | 0.4020 | 0.2121 |
| 42 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 54 | 0.0852 | 0.0862 | 0.4020 | 0.2121 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.0832 | 0.0832 | 1.4102 | 0.0590 |
| 44 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.0832 | 0.0832 | 1.4102 | 0.0590 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | -0.0661 | 0.1270 | -0.4226 | 0.1564 |
| 46 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | -0.0661 | 0.1270 | -0.4226 | 0.1564 |
| 47 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | -0.0661 | 0.1270 | -0.4226 | 0.1564 |
| 48 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | -0.0661 | 0.1270 | -0.4226 | 0.1564 |
| 49 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.0754 | 0.0782 | -0.4754 | -0.1586 |
| 50 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.0754 | 0.0782 | -0.4754 | -0.1586 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.0754 | 0.0782 | -0.4754 | -0.1586 |
| 52 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.0754 | 0.0782 | -0.4754 | -0.1586 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 54 | 0.0724 | 0.0724 | -0.3414 | -0.2121 |
| 54 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 54 | 0.0724 | 0.0724 | -0.3414 | -0.2121 |
| 55 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 54 | 0.0724 | 0.0724 | -0.3414 | -0.2121 |
| 56 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 54 | 0.0724 | 0.0724 | -0.3414 | -0.2121 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0630 | 0.0645 | 0.5154 | 0.1222 |
| 58 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0630 | 0.0645 | 0.5154 | 0.1222 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0630 | 0.0645 | 0.5154 | 0.1222 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0630 | 0.0645 | 0.5154 | 0.1222 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | 0.0562 | 0.0562 | -2.6322 | -0.0213 |
| 62 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | 0.0562 | 0.0562 | -2.6322 | -0.0213 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0542 | 0.0617 | -0.4436 | -0.1222 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0542 | 0.0617 | -0.4436 | -0.1222 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | -0.0494 | 0.0494 | -2.3142 | 0.0213 |
| 66 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | -0.0494 | 0.0494 | -2.3142 | 0.0213 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | -0.0492 | 0.0492 | -2.3064 | 0.0213 |
| 68 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | -0.0492 | 0.0492 | -2.3064 | 0.0213 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.0488 | 0.0488 | 1.6779 | 0.0291 |
| 70 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.0488 | 0.0488 | 1.6779 | 0.0291 |
| 71 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0412 | 0.0843 | -0.2331 | 0.1768 |
| 72 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0412 | 0.0843 | -0.2331 | 0.1768 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0412 | 0.0843 | -0.2331 | 0.1768 |
| 74 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0412 | 0.0843 | -0.2331 | 0.1768 |
| 75 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0477 | 0.0477 | -2.2351 | -0.0213 |
| 76 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0477 | 0.0477 | -2.2351 | -0.0213 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0477 | 0.0477 | -2.2351 | -0.0213 |
| 78 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0477 | 0.0477 | -2.2351 | -0.0213 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0459 | 0.0459 | 0.7782 | 0.0590 |
| 80 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0459 | 0.0459 | 0.7782 | 0.0590 |
| 81 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0459 | 0.0459 | 0.7782 | 0.0590 |
| 82 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0459 | 0.0459 | 0.7782 | 0.0590 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | -0.0409 | 0.0548 | 0.3344 | -0.1222 |
| 84 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | -0.0409 | 0.0548 | 0.3344 | -0.1222 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.0391 | 0.0393 | -0.8964 | -0.0436 |
| 86 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.0391 | 0.0393 | -0.8964 | -0.0436 |
| 87 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0360 | 0.0426 | 1.2389 | 0.0291 |
| 88 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0360 | 0.0426 | 1.2389 | 0.0291 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0360 | 0.0426 | 1.2389 | 0.0291 |
| 90 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0360 | 0.0426 | 1.2389 | 0.0291 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.0349 | 0.0349 | -0.7999 | -0.0436 |
| 92 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.0349 | 0.0349 | -0.7999 | -0.0436 |
| 93 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.0349 | 0.0349 | -0.7999 | -0.0436 |
| 94 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.0349 | 0.0349 | -0.7999 | -0.0436 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 45 | 0.0309 | 0.0309 | 0.5123 | 0.0603 |
| 96 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 45 | 0.0309 | 0.0309 | 0.5123 | 0.0603 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | -0.0291 | 0.0307 | -0.6667 | 0.0436 |
| 98 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | -0.0291 | 0.0307 | -0.6667 | 0.0436 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | -0.0287 | 0.0289 | -0.6575 | 0.0436 |
| 100 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | -0.0287 | 0.0289 | -0.6575 | 0.0436 |

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
