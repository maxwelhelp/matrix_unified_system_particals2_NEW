# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **276**
- src_label: `label_Hgg`
- tgt_label: `label_Hbb`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.3369 | 1.7548 | 12.6692 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.3369 | 1.7548 | 12.6692 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.3250 | 1.6051 | 5.3393 | 0.6111 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.3250 | 1.6051 | 5.3393 | 0.6111 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 0.7653 | 1.4194 | 12.3908 | 0.3536 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 0.7653 | 1.4194 | 12.3908 | 0.3536 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 0.7771 | 1.1423 | 3.8859 | 0.6111 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 0.7771 | 1.1423 | 3.8859 | 0.6111 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.4023 | 1.6597 | 12.8884 | 0.3536 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.4023 | 1.6597 | 12.8884 | 0.3536 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.4142 | 0.8213 | 4.2420 | 0.6111 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.4142 | 0.8213 | 4.2420 | 0.6111 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2687 | 1.4424 | 11.7633 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2687 | 1.4424 | 11.7633 | 0.3536 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2687 | 1.4424 | 11.7633 | 0.3536 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2687 | 1.4424 | 11.7633 | 0.3536 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2569 | 0.6411 | 4.1101 | 0.6111 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2569 | 0.6411 | 4.1101 | 0.6111 |
| 19 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2569 | 0.6411 | 4.1101 | 0.6111 |
| 20 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2569 | 0.6411 | 4.1101 | 0.6111 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 3 | 1.0697 | 1.0697 | 4.2789 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 3 | 1.0697 | 1.0697 | 4.2789 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 3 | 1.0246 | 1.0246 | 4.0984 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 3 | 1.0246 | 1.0246 | 4.0984 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | 0.8556 | 0.8556 | 3.4223 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 1 | 0.8556 | 0.8556 | 3.4223 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | 0.8556 | 0.8556 | 3.4223 | 0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 1 | 0.8556 | 0.8556 | 3.4223 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 1 | -0.6223 | 0.6351 | 2.4891 | -0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 1 | -0.6223 | 0.6351 | 2.4891 | -0.2500 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 3 | -0.5868 | 0.5868 | 2.3474 | -0.2500 |
| 14 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 3 | -0.5868 | 0.5868 | 2.3474 | -0.2500 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 3 | -0.5868 | 0.5868 | 2.3474 | -0.2500 |
| 16 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 3 | -0.5868 | 0.5868 | 2.3474 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.5723 | 0.5723 | 1.3874 | 0.4125 |
| 18 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.5723 | 0.5723 | 1.3874 | 0.4125 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.4449 | 0.4449 | -1.0786 | -0.4125 |
| 20 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.4449 | 0.4449 | -1.0786 | -0.4125 |
| 21 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.3390 | 0.3476 | -1.2485 | -0.2716 |
| 22 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.3390 | 0.3476 | -1.2485 | -0.2716 |
| 23 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 1 | -0.3045 | 0.3497 | 1.2178 | -0.2500 |
| 24 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 1 | -0.3045 | 0.3497 | 1.2178 | -0.2500 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.2806 | 0.2806 | 1.0332 | 0.2716 |
| 26 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.2806 | 0.2806 | 1.0332 | 0.2716 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.2601 | 0.2625 | -0.6306 | -0.4125 |
| 28 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.2601 | 0.2625 | -0.6306 | -0.4125 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.1871 | 0.2092 | 1.5847 | 0.1181 |
| 30 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.1871 | 0.2092 | 1.5847 | 0.1181 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.1808 | 0.1808 | 0.6658 | 0.2716 |
| 32 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.1808 | 0.1808 | 0.6658 | 0.2716 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.1070 | 0.1500 | 0.4460 | 0.2400 |
| 34 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.1070 | 0.1500 | 0.4460 | 0.2400 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.1027 | 0.1286 | -0.4279 | -0.2400 |
| 36 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.1027 | 0.1286 | -0.4279 | -0.2400 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0845 | 0.1014 | 0.7156 | 0.1181 |
| 38 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0845 | 0.1014 | 0.7156 | 0.1181 |
| 39 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0845 | 0.1014 | 0.7156 | 0.1181 |
| 40 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0845 | 0.1014 | 0.7156 | 0.1181 |
| 41 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0790 | 0.1209 | 0.1916 | 0.4125 |
| 42 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0790 | 0.1209 | 0.1916 | 0.4125 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0790 | 0.1209 | 0.1916 | 0.4125 |
| 44 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0790 | 0.1209 | 0.1916 | 0.4125 |
| 45 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 3 | 0.0054 | 0.4233 | -0.0216 | -0.2500 |
| 46 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 3 | 0.0054 | 0.4233 | -0.0216 | -0.2500 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | -0.0478 | 0.0913 | 0.4050 | -0.1181 |
| 48 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | -0.0478 | 0.0913 | 0.4050 | -0.1181 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | -0.0502 | 0.0502 | 1.8719 | -0.0268 |
| 50 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | -0.0502 | 0.0502 | 1.8719 | -0.0268 |
| 51 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0501 | 0.0501 | 1.8675 | 0.0268 |
| 52 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0501 | 0.0501 | 1.8675 | 0.0268 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0501 | 0.0501 | 1.8675 | 0.0268 |
| 54 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0501 | 0.0501 | 1.8675 | 0.0268 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | -0.0494 | 0.0494 | 1.8421 | -0.0268 |
| 56 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | -0.0494 | 0.0494 | 1.8421 | -0.0268 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.0456 | 0.0577 | 1.4511 | 0.0314 |
| 58 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.0456 | 0.0577 | 1.4511 | 0.0314 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | 0.0418 | 0.0645 | -0.1743 | -0.2400 |
| 60 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | 0.0418 | 0.0645 | -0.1743 | -0.2400 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0452 | 0.0471 | 1.4406 | 0.0314 |
| 62 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0452 | 0.0471 | 1.4406 | 0.0314 |
| 63 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0452 | 0.0471 | 1.4406 | 0.0314 |
| 64 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0452 | 0.0471 | 1.4406 | 0.0314 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | 0.0444 | 0.0486 | 1.6551 | 0.0268 |
| 66 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | 0.0444 | 0.0486 | 1.6551 | 0.0268 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | -0.0446 | 0.0446 | 1.4192 | -0.0314 |
| 68 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | -0.0446 | 0.0446 | 1.4192 | -0.0314 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 66 | 0.0413 | 0.0502 | -0.4436 | -0.0930 |
| 70 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 66 | 0.0413 | 0.0502 | -0.4436 | -0.0930 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | -0.0365 | 0.0380 | 1.1607 | -0.0314 |
| 72 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | -0.0365 | 0.0380 | 1.1607 | -0.0314 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0236 | 0.0892 | -0.0868 | -0.2716 |
| 74 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0236 | 0.0892 | -0.0868 | -0.2716 |
| 75 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0236 | 0.0892 | -0.0868 | -0.2716 |
| 76 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0236 | 0.0892 | -0.0868 | -0.2716 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | -0.0307 | 0.0443 | -0.3720 | 0.0825 |
| 78 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | -0.0307 | 0.0443 | -0.3720 | 0.0825 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.0289 | 0.0396 | -0.2447 | -0.1180 |
| 80 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.0289 | 0.0396 | -0.2447 | -0.1180 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | -0.0278 | 0.0298 | -0.3367 | 0.0825 |
| 82 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | -0.0278 | 0.0298 | -0.3367 | 0.0825 |
| 83 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | -0.0278 | 0.0298 | -0.3367 | 0.0825 |
| 84 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | -0.0278 | 0.0298 | -0.3367 | 0.0825 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.0221 | 0.0221 | -0.8848 | -0.0250 |
| 86 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.0221 | 0.0221 | -0.8848 | -0.0250 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.0171 | 0.0470 | -0.1449 | -0.1180 |
| 88 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.0171 | 0.0470 | -0.1449 | -0.1180 |
| 89 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0078 | 0.0912 | 0.0327 | 0.2400 |
| 90 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0078 | 0.0912 | 0.0327 | 0.2400 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0078 | 0.0912 | 0.0327 | 0.2400 |
| 92 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0078 | 0.0912 | 0.0327 | 0.2400 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 18 | 0.0197 | 0.0266 | -0.2383 | -0.0825 |
| 94 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 18 | 0.0197 | 0.0266 | -0.2383 | -0.0825 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | -0.0077 | 0.0817 | 0.0649 | -0.1181 |
| 96 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | -0.0077 | 0.0817 | 0.0649 | -0.1181 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | 0.0179 | 0.0277 | 0.1924 | 0.0930 |
| 98 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | 0.0179 | 0.0277 | 0.1924 | 0.0930 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 82 | 0.0172 | 0.0172 | 0.3086 | 0.0558 |
| 100 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 82 | 0.0172 | 0.0172 | 0.3086 | 0.0558 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 57 | label_Hgg | label_Hbb | 1.6501 | 0.0474 |
| 2 | mod.fc.0 | 121 | label_Hgg | label_Hbb | -1.0862 | 0.0474 |
| 3 | mod.fc.0 | 3 | label_Hgg | label_Hbb | 0.9599 | 0.0474 |
| 4 | mod.fc.0 | 8 | label_Hgg | label_Hbb | 0.4723 | 0.0474 |
| 5 | mod.fc.0 | 76 | label_Hgg | label_Hbb | 0.4722 | 0.0474 |
| 6 | mod.fc.0 | 66 | label_Hgg | label_Hbb | -0.3721 | 0.0474 |
| 7 | mod.fc.0 | 23 | label_Hgg | label_Hbb | -0.3665 | 0.0474 |
| 8 | mod.fc.0 | 18 | label_Hgg | label_Hbb | 0.3300 | 0.0474 |
| 9 | mod.fc.0 | 2 | label_Hgg | label_Hbb | -0.3073 | 0.0474 |
| 10 | mod.fc.0 | 58 | label_Hgg | label_Hbb | -0.2277 | 0.0474 |
| 11 | mod.fc.0 | 82 | label_Hgg | label_Hbb | -0.2233 | 0.0474 |
| 12 | mod.fc.0 | 54 | label_Hgg | label_Hbb | 0.2030 | 0.0474 |
| 13 | mod.fc.0 | 123 | label_Hgg | label_Hbb | -0.1475 | 0.0474 |
| 14 | mod.fc.0 | 103 | label_Hgg | label_Hbb | 0.1256 | 0.0474 |
| 15 | mod.fc.0 | 45 | label_Hgg | label_Hbb | 0.1183 | 0.0474 |
| 16 | mod.fc.0 | 34 | label_Hgg | label_Hbb | 0.1072 | 0.0474 |
| 17 | mod.fc.0 | 10 | label_Hgg | label_Hbb | -0.1000 | 0.0474 |
| 18 | mod.fc.0 | 96 | label_Hgg | label_Hbb | -0.0752 | 0.0474 |
| 19 | mod.fc.0 | 124 | label_Hgg | label_Hbb | -0.0630 | 0.0474 |
| 20 | mod.fc.0 | 6 | label_Hgg | label_Hbb | 0.0406 | 0.0474 |
| 21 | mod.fc.0 | 91 | label_Hgg | label_Hbb | 0.0285 | 0.0474 |
| 22 | mod.fc.0 | 80 | label_Hgg | label_Hbb | -0.0172 | 0.0474 |
| 23 | mod.fc.0 | 110 | label_Hgg | label_Hbb | 0.0104 | 0.0474 |
| 24 | mod.fc.0 | 79 | label_Hgg | label_Hbb | 0.0058 | 0.0474 |
| 25 | mod.fc.0 | 115 | label_Hgg | label_Hbb | -6.538e-04 | 0.0474 |
| 26 | mod.fc.0 | 78 | label_Hgg | label_Hbb | -3.245e-04 | 0.0474 |
| 27 | mod.fc.0 | 4 | label_Hgg | label_Hbb | -4.918e-05 | 0.0474 |
| 28 | mod.fc.0 | 11 | label_Hgg | label_Hbb | 3.849e-05 | 0.0474 |
| 29 | mod.fc.0 | 118 | label_Hgg | label_Hbb | 3.079e-05 | 0.0474 |
| 30 | mod.fc.0 | 109 | label_Hgg | label_Hbb | 2.011e-05 | 0.0474 |
| 31 | mod.fc.0 | 49 | label_Hgg | label_Hbb | 1.841e-05 | 0.0474 |
| 32 | mod.fc.0 | 15 | label_Hgg | label_Hbb | 1.347e-05 | 0.0474 |
| 33 | mod.fc.0 | 88 | label_Hgg | label_Hbb | 1.273e-05 | 0.0474 |
| 34 | mod.fc.0 | 77 | label_Hgg | label_Hbb | -1.204e-05 | 0.0474 |
| 35 | mod.fc.0 | 19 | label_Hgg | label_Hbb | 1.094e-05 | 0.0474 |
| 36 | mod.fc.0 | 106 | label_Hgg | label_Hbb | -1.068e-05 | 0.0474 |
| 37 | mod.fc.0 | 29 | label_Hgg | label_Hbb | 9.635e-06 | 0.0474 |
| 38 | mod.fc.0 | 38 | label_Hgg | label_Hbb | 9.291e-06 | 0.0474 |
| 39 | mod.fc.0 | 112 | label_Hgg | label_Hbb | 8.853e-06 | 0.0474 |
| 40 | mod.fc.0 | 31 | label_Hgg | label_Hbb | 8.442e-06 | 0.0474 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
