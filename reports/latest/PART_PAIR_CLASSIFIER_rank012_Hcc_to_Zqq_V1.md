# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **270**
- src_label: `label_Hcc`
- tgt_label: `label_Zqq`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.3119 | 2.0415 | 5.5365 | 0.6299 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.3119 | 2.0415 | 5.5365 | 0.6299 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.3183 | 1.3917 | 14.5730 | 0.3536 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.3183 | 1.3917 | 14.5730 | 0.3536 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.0842 | 1.5656 | 4.2863 | 0.6299 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.0842 | 1.5656 | 4.2863 | 0.6299 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.0778 | 1.1183 | 12.2446 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.0778 | 1.1183 | 12.2446 | 0.3536 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.4991 | 1.5345 | 4.4599 | 0.6299 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.4991 | 1.5345 | 4.4599 | 0.6299 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.5510 | 1.2249 | 4.4652 | 0.6299 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.5510 | 1.2249 | 4.4652 | 0.6299 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.5510 | 1.2249 | 4.4652 | 0.6299 |
| 14 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.5510 | 1.2249 | 4.4652 | 0.6299 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.5446 | 1.0860 | 13.0464 | 0.3536 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.5446 | 1.0860 | 13.0464 | 0.3536 |
| 17 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.5446 | 1.0860 | 13.0464 | 0.3536 |
| 18 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.5446 | 1.0860 | 13.0464 | 0.3536 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.5055 | 0.9392 | 13.7337 | 0.3536 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.5055 | 0.9392 | 13.7337 | 0.3536 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.9420 | 0.9420 | 3.7199 | 0.2532 |
| 4 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.9420 | 0.9420 | 3.7199 | 0.2532 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | 0.8121 | 0.8121 | 3.2484 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 6 | 0.8121 | 0.8121 | 3.2484 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | 0.8121 | 0.8121 | 3.2484 | 0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 6 | 0.8121 | 0.8121 | 3.2484 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 2 | 0.6819 | 0.6819 | 2.7277 | 0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 2 | 0.6819 | 0.6819 | 2.7277 | 0.2500 |
| 13 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | 0.6140 | 0.6140 | 2.4244 | 0.2532 |
| 14 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | 0.6140 | 0.6140 | 2.4244 | 0.2532 |
| 15 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.4302 | 0.4537 | 1.8053 | 0.2383 |
| 16 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.4302 | 0.4537 | 1.8053 | 0.2383 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | -0.2675 | 0.2739 | 1.0702 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 2 | -0.2675 | 0.2739 | 1.0702 | -0.2500 |
| 19 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | -0.2675 | 0.2739 | 1.0702 | -0.2500 |
| 20 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 2 | -0.2675 | 0.2739 | 1.0702 | -0.2500 |
| 21 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.2555 | 0.2719 | 1.0722 | 0.2383 |
| 22 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.2555 | 0.2719 | 1.0722 | 0.2383 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.2555 | 0.2719 | 1.0722 | 0.2383 |
| 24 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.2555 | 0.2719 | 1.0722 | 0.2383 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.2103 | 0.2125 | 0.8464 | 0.2484 |
| 26 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.2103 | 0.2125 | 0.8464 | 0.2484 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.1992 | 0.2136 | 0.7867 | -0.2532 |
| 28 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.1992 | 0.2136 | 0.7867 | -0.2532 |
| 29 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.1992 | 0.2136 | 0.7867 | -0.2532 |
| 30 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.1992 | 0.2136 | 0.7867 | -0.2532 |
| 31 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 6 | 0.1849 | 0.2583 | -0.7395 | -0.2500 |
| 32 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 6 | 0.1849 | 0.2583 | -0.7395 | -0.2500 |
| 33 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 6 | -0.1764 | 0.2573 | 0.7056 | -0.2500 |
| 34 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 6 | -0.1764 | 0.2573 | 0.7056 | -0.2500 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.1877 | 0.1911 | -0.7554 | -0.2484 |
| 36 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.1877 | 0.1911 | -0.7554 | -0.2484 |
| 37 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 2 | 0.1402 | 0.1807 | -0.5607 | -0.2500 |
| 38 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 2 | 0.1402 | 0.1807 | -0.5607 | -0.2500 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.1446 | 0.1446 | 1.1582 | 0.1249 |
| 40 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.1446 | 0.1446 | 1.1582 | 0.1249 |
| 41 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.1413 | 0.1413 | -3.3425 | -0.0423 |
| 42 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.1413 | 0.1413 | -3.3425 | -0.0423 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.1413 | 0.1413 | -3.3425 | -0.0423 |
| 44 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.1413 | 0.1413 | -3.3425 | -0.0423 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.1066 | 0.2133 | -0.4474 | -0.2383 |
| 46 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.1066 | 0.2133 | -0.4474 | -0.2383 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | -0.0966 | 0.2115 | 0.4055 | -0.2383 |
| 48 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | -0.0966 | 0.2115 | 0.4055 | -0.2383 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.1093 | 0.1475 | -0.6199 | -0.1763 |
| 50 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.1093 | 0.1475 | -0.6199 | -0.1763 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.1124 | 0.1161 | 0.9000 | 0.1249 |
| 52 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.1124 | 0.1161 | 0.9000 | 0.1249 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | -0.1084 | 0.1106 | -2.5646 | 0.0423 |
| 54 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | -0.1084 | 0.1106 | -2.5646 | 0.0423 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 66 | 0.1085 | 0.1085 | -0.6128 | -0.1771 |
| 56 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 66 | 0.1085 | 0.1085 | -0.6128 | -0.1771 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0951 | 0.1171 | -0.5398 | -0.1763 |
| 58 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0951 | 0.1171 | -0.5398 | -0.1763 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0951 | 0.1171 | -0.5398 | -0.1763 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0951 | 0.1171 | -0.5398 | -0.1763 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | -0.0970 | 0.0970 | -2.2938 | 0.0423 |
| 62 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | -0.0970 | 0.0970 | -2.2938 | 0.0423 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.0938 | 0.0938 | -2.2187 | -0.0423 |
| 64 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.0938 | 0.0938 | -2.2187 | -0.0423 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 2 | 0.0904 | 0.0997 | 0.4251 | 0.2126 |
| 66 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 2 | 0.0904 | 0.0997 | 0.4251 | 0.2126 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.0699 | 0.0824 | 0.7902 | 0.0884 |
| 68 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.0699 | 0.0824 | 0.7902 | 0.0884 |
| 69 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0692 | 0.0692 | 0.3257 | 0.2126 |
| 70 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0692 | 0.0692 | 0.3257 | 0.2126 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0692 | 0.0692 | 0.3257 | 0.2126 |
| 72 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0692 | 0.0692 | 0.3257 | 0.2126 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.0612 | 0.0750 | 0.6923 | 0.0884 |
| 74 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.0612 | 0.0750 | 0.6923 | 0.0884 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | -0.0597 | 0.0791 | -0.3369 | 0.1771 |
| 76 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | -0.0597 | 0.0791 | -0.3369 | 0.1771 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | -0.0431 | 0.1575 | 0.1704 | -0.2532 |
| 78 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | -0.0431 | 0.1575 | 0.1704 | -0.2532 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.0503 | 0.1105 | 0.2025 | 0.2484 |
| 80 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.0503 | 0.1105 | 0.2025 | 0.2484 |
| 81 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.0503 | 0.1105 | 0.2025 | 0.2484 |
| 82 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.0503 | 0.1105 | 0.2025 | 0.2484 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.0527 | 0.0637 | -0.4173 | -0.1264 |
| 84 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.0527 | 0.0637 | -0.4173 | -0.1264 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0478 | 0.0874 | 0.2709 | 0.1763 |
| 86 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0478 | 0.0874 | 0.2709 | 0.1763 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0506 | 0.0593 | -0.2855 | -0.1771 |
| 88 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0506 | 0.0593 | -0.2855 | -0.1771 |
| 89 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0506 | 0.0593 | -0.2855 | -0.1771 |
| 90 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0506 | 0.0593 | -0.2855 | -0.1771 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 2 | 0.0500 | 0.0546 | -0.2352 | -0.2126 |
| 92 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 2 | 0.0500 | 0.0546 | -0.2352 | -0.2126 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | -0.0480 | 0.0550 | -0.3798 | 0.1264 |
| 94 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | -0.0480 | 0.0550 | -0.3798 | 0.1264 |
| 95 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.0472 | 0.0552 | -0.3734 | -0.1264 |
| 96 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.0472 | 0.0552 | -0.3734 | -0.1264 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.0472 | 0.0552 | -0.3734 | -0.1264 |
| 98 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.0472 | 0.0552 | -0.3734 | -0.1264 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | 0.0356 | 0.1111 | -0.1434 | -0.2484 |
| 100 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | 0.0356 | 0.1111 | -0.1434 | -0.2484 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 79 | label_Hcc | label_Zqq | -1.0130 | -0.0256 |
| 2 | mod.fc.0 | 10 | label_Hcc | label_Zqq | 0.9938 | -0.0256 |
| 3 | mod.fc.0 | 8 | label_Hcc | label_Zqq | 0.9532 | -0.0256 |
| 4 | mod.fc.0 | 2 | label_Hcc | label_Zqq | 0.8505 | -0.0256 |
| 5 | mod.fc.0 | 66 | label_Hcc | label_Zqq | -0.7085 | -0.0256 |
| 6 | mod.fc.0 | 121 | label_Hcc | label_Zqq | -0.7051 | -0.0256 |
| 7 | mod.fc.0 | 45 | label_Hcc | label_Zqq | -0.6072 | -0.0256 |
| 8 | mod.fc.0 | 18 | label_Hcc | label_Zqq | -0.5056 | -0.0256 |
| 9 | mod.fc.0 | 76 | label_Hcc | label_Zqq | -0.4996 | -0.0256 |
| 10 | mod.fc.0 | 3 | label_Hcc | label_Zqq | -0.3963 | -0.0256 |
| 11 | mod.fc.0 | 57 | label_Hcc | label_Zqq | -0.3537 | -0.0256 |
| 12 | mod.fc.0 | 23 | label_Hcc | label_Zqq | 0.3312 | -0.0256 |
| 13 | mod.fc.0 | 82 | label_Hcc | label_Zqq | -0.3028 | -0.0256 |
| 14 | mod.fc.0 | 58 | label_Hcc | label_Zqq | -0.2851 | -0.0256 |
| 15 | mod.fc.0 | 91 | label_Hcc | label_Zqq | 0.2576 | -0.0256 |
| 16 | mod.fc.0 | 54 | label_Hcc | label_Zqq | -0.2532 | -0.0256 |
| 17 | mod.fc.0 | 96 | label_Hcc | label_Zqq | 0.2272 | -0.0256 |
| 18 | mod.fc.0 | 123 | label_Hcc | label_Zqq | 0.2234 | -0.0256 |
| 19 | mod.fc.0 | 103 | label_Hcc | label_Zqq | -0.1691 | -0.0256 |
| 20 | mod.fc.0 | 34 | label_Hcc | label_Zqq | 0.0480 | -0.0256 |
| 21 | mod.fc.0 | 80 | label_Hcc | label_Zqq | -0.0283 | -0.0256 |
| 22 | mod.fc.0 | 6 | label_Hcc | label_Zqq | 0.0183 | -0.0256 |
| 23 | mod.fc.0 | 110 | label_Hcc | label_Zqq | -0.0164 | -0.0256 |
| 24 | mod.fc.0 | 124 | label_Hcc | label_Zqq | -9.467e-04 | -0.0256 |
| 25 | mod.fc.0 | 78 | label_Hcc | label_Zqq | -4.566e-04 | -0.0256 |
| 26 | mod.fc.0 | 115 | label_Hcc | label_Zqq | -2.064e-04 | -0.0256 |
| 27 | mod.fc.0 | 38 | label_Hcc | label_Zqq | 5.127e-05 | -0.0256 |
| 28 | mod.fc.0 | 4 | label_Hcc | label_Zqq | 3.719e-05 | -0.0256 |
| 29 | mod.fc.0 | 11 | label_Hcc | label_Zqq | -2.544e-05 | -0.0256 |
| 30 | mod.fc.0 | 51 | label_Hcc | label_Zqq | -2.382e-05 | -0.0256 |
| 31 | mod.fc.0 | 81 | label_Hcc | label_Zqq | 2.149e-05 | -0.0256 |
| 32 | mod.fc.0 | 89 | label_Hcc | label_Zqq | 1.828e-05 | -0.0256 |
| 33 | mod.fc.0 | 64 | label_Hcc | label_Zqq | 1.778e-05 | -0.0256 |
| 34 | mod.fc.0 | 49 | label_Hcc | label_Zqq | 1.761e-05 | -0.0256 |
| 35 | mod.fc.0 | 119 | label_Hcc | label_Zqq | -1.549e-05 | -0.0256 |
| 36 | mod.fc.0 | 105 | label_Hcc | label_Zqq | -1.425e-05 | -0.0256 |
| 37 | mod.fc.0 | 40 | label_Hcc | label_Zqq | -1.424e-05 | -0.0256 |
| 38 | mod.fc.0 | 19 | label_Hcc | label_Zqq | 1.333e-05 | -0.0256 |
| 39 | mod.fc.0 | 46 | label_Hcc | label_Zqq | 1.320e-05 | -0.0256 |
| 40 | mod.fc.0 | 127 | label_Hcc | label_Zqq | 1.287e-05 | -0.0256 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
