# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **266**
- src_label: `label_Hbb`
- tgt_label: `label_Zqq`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.4152 | 2.1069 | 5.3393 | 0.6454 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.4152 | 2.1069 | 5.3393 | 0.6454 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.3855 | 1.6647 | 12.6692 | 0.3536 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.3855 | 1.6647 | 12.6692 | 0.3536 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.2049 | 1.5064 | 12.2446 | 0.3536 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.2049 | 1.5064 | 12.2446 | 0.3536 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.1752 | 1.6511 | 4.2863 | 0.6454 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.1752 | 1.6511 | 4.2863 | 0.6454 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.3575 | 1.4624 | 4.4385 | 0.6454 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.3575 | 1.4624 | 4.4385 | 0.6454 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.3483 | 1.3633 | 4.2959 | 0.6454 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.3483 | 1.3633 | 4.2959 | 0.6454 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.3483 | 1.3633 | 4.2959 | 0.6454 |
| 14 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.3483 | 1.3633 | 4.2959 | 0.6454 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3780 | 1.1789 | 11.6031 | 0.3536 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3780 | 1.1789 | 11.6031 | 0.3536 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3780 | 1.1789 | 11.6031 | 0.3536 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3780 | 1.1789 | 11.6031 | 0.3536 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.3278 | 1.3022 | 11.4554 | 0.3536 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.3278 | 1.3022 | 11.4554 | 0.3536 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 1 | 0.8150 | 0.8150 | 3.2600 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 1 | 0.8150 | 0.8150 | 3.2600 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | 0.7505 | 0.7505 | 3.0020 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 6 | 0.7505 | 0.7505 | 3.0020 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | 0.7505 | 0.7505 | 3.0020 | 0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 6 | 0.7505 | 0.7505 | 3.0020 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.7102 | 0.7102 | 3.2114 | 0.2212 |
| 12 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.7102 | 0.7102 | 3.2114 | 0.2212 |
| 13 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.7087 | 0.7087 | -2.2187 | -0.3194 |
| 14 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.7087 | 0.7087 | -2.2187 | -0.3194 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 6 | -0.4872 | 0.4872 | 1.9489 | -0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 6 | -0.4872 | 0.4872 | 1.9489 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.4382 | 0.5533 | 1.3720 | 0.3194 |
| 18 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.4382 | 0.5533 | 1.3720 | 0.3194 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | 0.4405 | 0.4405 | 1.9917 | 0.2212 |
| 20 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | 0.4405 | 0.4405 | 1.9917 | 0.2212 |
| 21 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | -0.3725 | 0.4284 | 1.4900 | -0.2500 |
| 22 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 1 | -0.3725 | 0.4284 | 1.4900 | -0.2500 |
| 23 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | -0.3725 | 0.4284 | 1.4900 | -0.2500 |
| 24 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 1 | -0.3725 | 0.4284 | 1.4900 | -0.2500 |
| 25 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.3596 | 0.4235 | -1.1260 | -0.3194 |
| 26 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.3596 | 0.4235 | -1.1260 | -0.3194 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.3596 | 0.4235 | -1.1260 | -0.3194 |
| 28 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.3596 | 0.4235 | -1.1260 | -0.3194 |
| 29 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 1 | 0.2672 | 0.5687 | -1.0689 | -0.2500 |
| 30 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 1 | 0.2672 | 0.5687 | -1.0689 | -0.2500 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.2626 | 0.2626 | 1.4786 | 0.1776 |
| 32 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.2626 | 0.2626 | 1.4786 | 0.1776 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.2573 | 0.2585 | 1.1636 | -0.2212 |
| 34 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.2573 | 0.2585 | 1.1636 | -0.2212 |
| 35 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.2573 | 0.2585 | 1.1636 | -0.2212 |
| 36 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.2573 | 0.2585 | 1.1636 | -0.2212 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.1947 | 0.1947 | 1.0967 | 0.1776 |
| 38 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.1947 | 0.1947 | 1.0967 | 0.1776 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.1885 | 0.1905 | 0.8464 | 0.2228 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.1885 | 0.1905 | 0.8464 | 0.2228 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 66 | 0.1200 | 0.1200 | -0.6128 | -0.1959 |
| 42 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 66 | 0.1200 | 0.1200 | -0.6128 | -0.1959 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.1107 | 0.1417 | -0.6294 | -0.1759 |
| 44 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.1107 | 0.1417 | -0.6294 | -0.1759 |
| 45 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.1107 | 0.1417 | -0.6294 | -0.1759 |
| 46 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.1107 | 0.1417 | -0.6294 | -0.1759 |
| 47 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 6 | 0.0540 | 0.3332 | -0.2161 | -0.2500 |
| 48 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 6 | 0.0540 | 0.3332 | -0.2161 | -0.2500 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | -0.0963 | 0.1051 | -0.4915 | 0.1959 |
| 50 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | -0.0963 | 0.1051 | -0.4915 | 0.1959 |
| 51 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0906 | 0.1114 | 0.5104 | -0.1776 |
| 52 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0906 | 0.1114 | 0.5104 | -0.1776 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0906 | 0.1114 | 0.5104 | -0.1776 |
| 54 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0906 | 0.1114 | 0.5104 | -0.1776 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.0892 | 0.1034 | -0.4005 | -0.2228 |
| 56 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.0892 | 0.1034 | -0.4005 | -0.2228 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 18 | -0.0873 | 0.1025 | -0.4964 | 0.1759 |
| 58 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 18 | -0.0873 | 0.1025 | -0.4964 | 0.1759 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | -0.0760 | 0.0932 | -0.3882 | 0.1959 |
| 60 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | -0.0760 | 0.0932 | -0.3882 | 0.1959 |
| 61 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.0719 | 0.1055 | 0.3230 | 0.2228 |
| 62 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.0719 | 0.1055 | 0.3230 | 0.2228 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.0719 | 0.1055 | 0.3230 | 0.2228 |
| 64 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.0719 | 0.1055 | 0.3230 | 0.2228 |
| 65 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0735 | 0.0735 | -0.3750 | -0.1959 |
| 66 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0735 | 0.0735 | -0.3750 | -0.1959 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0735 | 0.0735 | -0.3750 | -0.1959 |
| 68 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0735 | 0.0735 | -0.3750 | -0.1959 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.0682 | 0.0956 | 0.4460 | 0.1530 |
| 70 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.0682 | 0.0956 | 0.4460 | 0.1530 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | -0.0288 | 0.2871 | -0.0902 | 0.3194 |
| 72 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | -0.0288 | 0.2871 | -0.0902 | 0.3194 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 2 | 0.0691 | 0.0802 | 0.3547 | 0.1949 |
| 74 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 2 | 0.0691 | 0.0802 | 0.3547 | 0.1949 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | -0.0655 | 0.0945 | -0.3720 | 0.1759 |
| 76 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | -0.0655 | 0.0945 | -0.3720 | 0.1759 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.0643 | 0.0781 | -0.3653 | -0.1759 |
| 78 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.0643 | 0.0781 | -0.3653 | -0.1759 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | 0.0449 | 0.0929 | 0.2935 | 0.1530 |
| 80 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | 0.0449 | 0.0929 | 0.2935 | 0.1530 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | -0.0346 | 0.1297 | 0.1565 | -0.2212 |
| 82 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | -0.0346 | 0.1297 | 0.1565 | -0.2212 |
| 83 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | -0.0496 | 0.0496 | 1.8687 | -0.0265 |
| 84 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | -0.0496 | 0.0496 | 1.8687 | -0.0265 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | -0.0496 | 0.0496 | 1.8687 | -0.0265 |
| 86 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | -0.0496 | 0.0496 | 1.8687 | -0.0265 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | 0.0486 | 0.0486 | 1.8322 | 0.0265 |
| 88 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | 0.0486 | 0.0486 | 1.8322 | 0.0265 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0436 | 0.0500 | 0.2239 | 0.1949 |
| 90 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0436 | 0.0500 | 0.2239 | 0.1949 |
| 91 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0436 | 0.0500 | 0.2239 | 0.1949 |
| 92 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0436 | 0.0500 | 0.2239 | 0.1949 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | 0.0439 | 0.0480 | 1.6551 | 0.0265 |
| 94 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | 0.0439 | 0.0480 | 1.6551 | 0.0265 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.0431 | 0.0431 | 2.4176 | 0.0178 |
| 96 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.0431 | 0.0431 | 2.4176 | 0.0178 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.0351 | 0.0776 | -0.2292 | -0.1530 |
| 98 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.0351 | 0.0776 | -0.2292 | -0.1530 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | -0.0415 | 0.0415 | 2.3242 | -0.0178 |
| 100 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | -0.0415 | 0.0415 | 2.3242 | -0.0178 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 103 | label_Hbb | label_Zqq | -1.2776 | 0.1187 |
| 2 | mod.fc.0 | 10 | label_Hbb | label_Zqq | 0.8910 | 0.1187 |
| 3 | mod.fc.0 | 79 | label_Hbb | label_Zqq | -0.8846 | 0.1187 |
| 4 | mod.fc.0 | 66 | label_Hbb | label_Zqq | -0.7835 | 0.1187 |
| 5 | mod.fc.0 | 2 | label_Hbb | label_Zqq | 0.7797 | 0.1187 |
| 6 | mod.fc.0 | 57 | label_Hbb | label_Zqq | -0.7103 | 0.1187 |
| 7 | mod.fc.0 | 18 | label_Hbb | label_Zqq | -0.7038 | 0.1187 |
| 8 | mod.fc.0 | 3 | label_Hbb | label_Zqq | -0.6121 | 0.1187 |
| 9 | mod.fc.0 | 23 | label_Hbb | label_Zqq | 0.5561 | 0.1187 |
| 10 | mod.fc.0 | 82 | label_Hbb | label_Zqq | -0.4513 | 0.1187 |
| 11 | mod.fc.0 | 54 | label_Hbb | label_Zqq | -0.4103 | 0.1187 |
| 12 | mod.fc.0 | 96 | label_Hbb | label_Zqq | 0.2739 | 0.1187 |
| 13 | mod.fc.0 | 91 | label_Hbb | label_Zqq | 0.2269 | 0.1187 |
| 14 | mod.fc.0 | 124 | label_Hbb | label_Zqq | 0.1215 | 0.1187 |
| 15 | mod.fc.0 | 123 | label_Hbb | label_Zqq | 0.1142 | 0.1187 |
| 16 | mod.fc.0 | 34 | label_Hbb | label_Zqq | -0.1061 | 0.1187 |
| 17 | mod.fc.0 | 8 | label_Hbb | label_Zqq | 0.0714 | 0.1187 |
| 18 | mod.fc.0 | 45 | label_Hbb | label_Zqq | -0.0681 | 0.1187 |
| 19 | mod.fc.0 | 121 | label_Hbb | label_Zqq | -0.0314 | 0.1187 |
| 20 | mod.fc.0 | 58 | label_Hbb | label_Zqq | 0.0273 | 0.1187 |
| 21 | mod.fc.0 | 110 | label_Hbb | label_Zqq | -0.0240 | 0.1187 |
| 22 | mod.fc.0 | 6 | label_Hbb | label_Zqq | 0.0198 | 0.1187 |
| 23 | mod.fc.0 | 80 | label_Hbb | label_Zqq | -0.0187 | 0.1187 |
| 24 | mod.fc.0 | 76 | label_Hbb | label_Zqq | 0.0138 | 0.1187 |
| 25 | mod.fc.0 | 78 | label_Hbb | label_Zqq | -3.936e-04 | 0.1187 |
| 26 | mod.fc.0 | 115 | label_Hbb | label_Zqq | 3.338e-04 | 0.1187 |
| 27 | mod.fc.0 | 4 | label_Hbb | label_Zqq | 3.767e-05 | 0.1187 |
| 28 | mod.fc.0 | 11 | label_Hbb | label_Zqq | -3.144e-05 | 0.1187 |
| 29 | mod.fc.0 | 118 | label_Hbb | label_Zqq | -2.909e-05 | 0.1187 |
| 30 | mod.fc.0 | 20 | label_Hbb | label_Zqq | 2.692e-05 | 0.1187 |
| 31 | mod.fc.0 | 109 | label_Hbb | label_Zqq | -2.001e-05 | 0.1187 |
| 32 | mod.fc.0 | 40 | label_Hbb | label_Zqq | -1.810e-05 | 0.1187 |
| 33 | mod.fc.0 | 51 | label_Hbb | label_Zqq | -1.563e-05 | 0.1187 |
| 34 | mod.fc.0 | 52 | label_Hbb | label_Zqq | 1.378e-05 | 0.1187 |
| 35 | mod.fc.0 | 112 | label_Hbb | label_Zqq | -1.159e-05 | 0.1187 |
| 36 | mod.fc.0 | 29 | label_Hbb | label_Zqq | -1.086e-05 | 0.1187 |
| 37 | mod.fc.0 | 49 | label_Hbb | label_Zqq | -1.021e-05 | 0.1187 |
| 38 | mod.fc.0 | 105 | label_Hbb | label_Zqq | -1.009e-05 | 0.1187 |
| 39 | mod.fc.0 | 15 | label_Hbb | label_Zqq | -9.815e-06 | 0.1187 |
| 40 | mod.fc.0 | 71 | label_Hbb | label_Zqq | 8.434e-06 | 0.1187 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
