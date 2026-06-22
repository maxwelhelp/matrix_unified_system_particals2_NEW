# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **252**
- src_label: `label_Hgg`
- tgt_label: `label_Hcc`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.3692 | 1.5585 | 14.5730 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.3692 | 1.5585 | 14.5730 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.3213 | 1.7022 | 5.5365 | 0.5914 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.3213 | 1.7022 | 5.5365 | 0.5914 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 0.8541 | 1.2124 | 3.8859 | 0.5914 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 0.8541 | 1.2124 | 3.8859 | 0.5914 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 0.8062 | 1.3508 | 12.3908 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 0.8062 | 1.3508 | 12.3908 | 0.3536 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.4850 | 1.3253 | 12.8843 | 0.3536 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.4850 | 1.3253 | 12.8843 | 0.3536 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.5330 | 0.9990 | 3.9187 | 0.5914 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.5330 | 0.9990 | 3.9187 | 0.5914 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2198 | 1.1832 | 12.8881 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2198 | 1.1832 | 12.8881 | 0.3536 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2198 | 1.1832 | 12.8881 | 0.3536 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2198 | 1.1832 | 12.8881 | 0.3536 |
| 17 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.1719 | 0.7913 | 3.9388 | 0.5914 |
| 18 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.1719 | 0.7913 | 3.9388 | 0.5914 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.1719 | 0.7913 | 3.9388 | 0.5914 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.1719 | 0.7913 | 3.9388 | 0.5914 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 3 | 1.0697 | 1.0697 | 4.2789 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 3 | 1.0697 | 1.0697 | 4.2789 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 3 | 0.9052 | 0.9052 | 3.6207 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 3 | 0.9052 | 0.9052 | 3.6207 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | 0.6999 | 0.6999 | 2.7994 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 2 | 0.6999 | 0.6999 | 2.7994 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | 0.6999 | 0.6999 | 2.7994 | 0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 2 | 0.6999 | 0.6999 | 2.7994 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.6302 | 0.6426 | -2.5646 | -0.2457 |
| 12 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.6302 | 0.6426 | -2.5646 | -0.2457 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 3 | -0.4801 | 0.4833 | 1.9202 | -0.2500 |
| 14 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 3 | -0.4801 | 0.4833 | 1.9202 | -0.2500 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 3 | -0.4801 | 0.4833 | 1.9202 | -0.2500 |
| 16 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 3 | -0.4801 | 0.4833 | 1.9202 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 2 | -0.4201 | 0.4201 | 1.6805 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 2 | -0.4201 | 0.4201 | 1.6805 | -0.2500 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.3488 | 0.3488 | -1.0786 | -0.3234 |
| 20 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.3488 | 0.3488 | -1.0786 | -0.3234 |
| 21 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.2853 | 0.2853 | 1.1582 | 0.2464 |
| 22 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.2853 | 0.2853 | 1.1582 | 0.2464 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.2654 | 0.2804 | 1.0801 | 0.2457 |
| 24 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.2654 | 0.2804 | 1.0801 | 0.2457 |
| 25 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 3 | 0.2358 | 0.4251 | -0.9432 | -0.2500 |
| 26 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 3 | 0.2358 | 0.4251 | -0.9432 | -0.2500 |
| 27 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 2 | -0.2636 | 0.2811 | 1.0543 | -0.2500 |
| 28 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 2 | -0.2636 | 0.2811 | 1.0543 | -0.2500 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.2418 | 0.2418 | -0.7478 | -0.3234 |
| 30 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.2418 | 0.2418 | -0.7478 | -0.3234 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.2199 | 0.2660 | 0.6800 | 0.3234 |
| 32 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.2199 | 0.2660 | 0.6800 | 0.3234 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.1521 | 0.2161 | 0.6190 | 0.2457 |
| 34 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.1521 | 0.2161 | 0.6190 | 0.2457 |
| 35 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.1296 | 0.1479 | -0.5274 | -0.2457 |
| 36 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.1296 | 0.1479 | -0.5274 | -0.2457 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.1296 | 0.1479 | -0.5274 | -0.2457 |
| 38 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.1296 | 0.1479 | -0.5274 | -0.2457 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.1248 | 0.1248 | 3.7199 | 0.0335 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.1248 | 0.1248 | 3.7199 | 0.0335 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.1066 | 0.1066 | 1.0332 | 0.1031 |
| 42 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.1066 | 0.1066 | 1.0332 | 0.1031 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.0961 | 0.0961 | 2.8634 | 0.0335 |
| 44 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.0961 | 0.0961 | 2.8634 | 0.0335 |
| 45 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.0961 | 0.0961 | 2.8634 | 0.0335 |
| 46 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.0961 | 0.0961 | 2.8634 | 0.0335 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.0864 | 0.0864 | 0.8381 | 0.1031 |
| 48 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.0864 | 0.0864 | 0.8381 | 0.1031 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | -0.0841 | 0.0841 | 2.5077 | -0.0335 |
| 50 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | -0.0841 | 0.0841 | 2.5077 | -0.0335 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | -0.0832 | 0.0832 | 2.4801 | -0.0335 |
| 52 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | -0.0832 | 0.0832 | 2.4801 | -0.0335 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.0796 | 0.0997 | -0.4279 | -0.1860 |
| 54 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.0796 | 0.0997 | -0.4279 | -0.1860 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0645 | 0.1067 | -0.1995 | 0.3234 |
| 56 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0645 | 0.1067 | -0.1995 | 0.3234 |
| 57 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0645 | 0.1067 | -0.1995 | 0.3234 |
| 58 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0645 | 0.1067 | -0.1995 | 0.3234 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0651 | 0.0805 | -0.6354 | -0.1024 |
| 60 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0651 | 0.0805 | -0.6354 | -0.1024 |
| 61 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0651 | 0.0805 | -0.6354 | -0.1024 |
| 62 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0651 | 0.0805 | -0.6354 | -0.1024 |
| 63 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0609 | 0.0955 | 0.2473 | 0.2464 |
| 64 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0609 | 0.0955 | 0.2473 | 0.2464 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0609 | 0.0955 | 0.2473 | 0.2464 |
| 66 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0609 | 0.0955 | 0.2473 | 0.2464 |
| 67 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0513 | 0.0644 | 0.4972 | -0.1031 |
| 68 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0513 | 0.0644 | 0.4972 | -0.1031 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0513 | 0.0644 | 0.4972 | -0.1031 |
| 70 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0513 | 0.0644 | 0.4972 | -0.1031 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.0458 | 0.0917 | -0.4474 | -0.1024 |
| 72 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.0458 | 0.0917 | -0.4474 | -0.1024 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.0357 | 0.0981 | -0.1449 | -0.2464 |
| 74 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.0357 | 0.0981 | -0.1449 | -0.2464 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.0398 | 0.0687 | -0.1617 | -0.2464 |
| 76 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.0398 | 0.0687 | -0.1617 | -0.2464 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.0439 | 0.0439 | -0.8666 | -0.0507 |
| 78 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.0439 | 0.0439 | -0.8666 | -0.0507 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | -0.0259 | 0.0855 | -0.2529 | 0.1024 |
| 80 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | -0.0259 | 0.0855 | -0.2529 | 0.1024 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | -0.0306 | 0.0541 | 0.2970 | -0.1031 |
| 82 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | -0.0306 | 0.0541 | 0.2970 | -0.1031 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | -0.0252 | 0.0782 | -0.1355 | 0.1860 |
| 84 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | -0.0252 | 0.0782 | -0.1355 | 0.1860 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 45 | 0.0329 | 0.0329 | -0.2004 | -0.1643 |
| 86 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 45 | 0.0329 | 0.0329 | -0.2004 | -0.1643 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 82 | 0.0296 | 0.0296 | 0.3180 | 0.0930 |
| 88 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 82 | 0.0296 | 0.0296 | 0.3180 | 0.0930 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 66 | 0.0263 | 0.0451 | -0.2352 | -0.1118 |
| 90 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 66 | 0.0263 | 0.0451 | -0.2352 | -0.1118 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 45 | 0.0283 | 0.0283 | -0.1723 | -0.1643 |
| 92 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 45 | 0.0283 | 0.0283 | -0.1723 | -0.1643 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 82 | 0.0278 | 0.0278 | 0.2994 | 0.0930 |
| 94 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 82 | 0.0278 | 0.0278 | 0.2994 | 0.0930 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | 0.0173 | 0.0785 | -0.0927 | -0.1860 |
| 96 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | 0.0173 | 0.0785 | -0.0927 | -0.1860 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | 0.0266 | 0.0279 | 0.2381 | 0.1118 |
| 98 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | 0.0266 | 0.0279 | 0.2381 | 0.1118 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | 0.0239 | 0.0239 | 2.0409 | 0.0117 |
| 100 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | 0.0239 | 0.0239 | 2.0409 | 0.0117 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 57 | label_Hgg | label_Hcc | 1.2936 | 0.1917 |
| 2 | mod.fc.0 | 76 | label_Hgg | label_Hcc | 0.9855 | 0.1917 |
| 3 | mod.fc.0 | 103 | label_Hgg | label_Hcc | -0.9829 | 0.1917 |
| 4 | mod.fc.0 | 3 | label_Hgg | label_Hcc | 0.7442 | 0.1917 |
| 5 | mod.fc.0 | 45 | label_Hgg | label_Hcc | 0.6574 | 0.1917 |
| 6 | mod.fc.0 | 66 | label_Hgg | label_Hcc | -0.4471 | 0.1917 |
| 7 | mod.fc.0 | 121 | label_Hgg | label_Hcc | -0.4126 | 0.1917 |
| 8 | mod.fc.0 | 8 | label_Hgg | label_Hcc | -0.4096 | 0.1917 |
| 9 | mod.fc.0 | 2 | label_Hgg | label_Hcc | -0.3781 | 0.1917 |
| 10 | mod.fc.0 | 82 | label_Hgg | label_Hcc | -0.3718 | 0.1917 |
| 11 | mod.fc.0 | 123 | label_Hgg | label_Hcc | -0.2567 | 0.1917 |
| 12 | mod.fc.0 | 10 | label_Hgg | label_Hcc | -0.2028 | 0.1917 |
| 13 | mod.fc.0 | 23 | label_Hgg | label_Hcc | -0.1416 | 0.1917 |
| 14 | mod.fc.0 | 79 | label_Hgg | label_Hcc | 0.1342 | 0.1917 |
| 15 | mod.fc.0 | 18 | label_Hgg | label_Hcc | 0.1319 | 0.1917 |
| 16 | mod.fc.0 | 58 | label_Hgg | label_Hcc | 0.0848 | 0.1917 |
| 17 | mod.fc.0 | 124 | label_Hgg | label_Hcc | 0.0595 | 0.1917 |
| 18 | mod.fc.0 | 34 | label_Hgg | label_Hcc | -0.0469 | 0.1917 |
| 19 | mod.fc.0 | 54 | label_Hgg | label_Hcc | 0.0459 | 0.1917 |
| 20 | mod.fc.0 | 6 | label_Hgg | label_Hcc | 0.0421 | 0.1917 |
| 21 | mod.fc.0 | 96 | label_Hgg | label_Hcc | -0.0285 | 0.1917 |
| 22 | mod.fc.0 | 80 | label_Hgg | label_Hcc | -0.0076 | 0.1917 |
| 23 | mod.fc.0 | 110 | label_Hgg | label_Hcc | 0.0028 | 0.1917 |
| 24 | mod.fc.0 | 91 | label_Hgg | label_Hcc | -0.0022 | 0.1917 |
| 25 | mod.fc.0 | 78 | label_Hgg | label_Hcc | -2.614e-04 | 0.1917 |
| 26 | mod.fc.0 | 115 | label_Hgg | label_Hcc | -1.136e-04 | 0.1917 |
| 27 | mod.fc.0 | 4 | label_Hgg | label_Hcc | -4.869e-05 | 0.1917 |
| 28 | mod.fc.0 | 38 | label_Hgg | label_Hcc | -4.084e-05 | 0.1917 |
| 29 | mod.fc.0 | 11 | label_Hgg | label_Hcc | 3.249e-05 | 0.1917 |
| 30 | mod.fc.0 | 89 | label_Hgg | label_Hcc | -1.982e-05 | 0.1917 |
| 31 | mod.fc.0 | 20 | label_Hgg | label_Hcc | 1.801e-05 | 0.1917 |
| 32 | mod.fc.0 | 81 | label_Hgg | label_Hcc | -1.441e-05 | 0.1917 |
| 33 | mod.fc.0 | 64 | label_Hgg | label_Hcc | -1.361e-05 | 0.1917 |
| 34 | mod.fc.0 | 113 | label_Hgg | label_Hcc | 1.336e-05 | 0.1917 |
| 35 | mod.fc.0 | 31 | label_Hgg | label_Hcc | 1.325e-05 | 0.1917 |
| 36 | mod.fc.0 | 119 | label_Hgg | label_Hcc | 1.308e-05 | 0.1917 |
| 37 | mod.fc.0 | 48 | label_Hgg | label_Hcc | 1.223e-05 | 0.1917 |
| 38 | mod.fc.0 | 87 | label_Hgg | label_Hcc | 1.184e-05 | 0.1917 |
| 39 | mod.fc.0 | 118 | label_Hgg | label_Hcc | 1.170e-05 | 0.1917 |
| 40 | mod.fc.0 | 127 | label_Hgg | label_Hcc | -1.130e-05 | 0.1917 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
