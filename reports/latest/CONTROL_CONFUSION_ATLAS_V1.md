# Control Confusion Atlas v1

Shows where predictions move under particle0/top-k controls. This answers: when a class collapses, what class wins instead?

n_events=2560 mode=kinpid

## Control summary
| control | acc | flip | mean_abs_logit_diff | delta_base_pred_logit |
| --- | --- | --- | --- | --- |
| baseline | 0.7574 | 0.0000 | 0.0000 | 0.0000 |
| remove_particle0 | 0.5633 | 0.3160 | 2.4906 | -3.5645 |
| keep_only_particle0 | 0.2027 | 0.7941 | 32.8198 | -26.5106 |
| remove_top1 | 0.5633 | 0.3160 | 2.4906 | -3.5645 |
| keep_top1 | 0.2027 | 0.7941 | 32.8198 | -26.5106 |
| random_remove1 | 0.7449 | 0.0609 | 0.4545 | -0.2199 |
| remove_top2 | 0.4566 | 0.4664 | 3.5341 | -5.5531 |
| keep_top2 | 0.2430 | 0.7477 | 18.9785 | -16.7977 |
| random_remove2 | 0.7195 | 0.0934 | 0.7154 | -0.3821 |
| remove_top4 | 0.3492 | 0.5922 | 5.0245 | -8.2648 |
| keep_top4 | 0.2922 | 0.7004 | 12.5859 | -12.2420 |
| random_remove4 | 0.6871 | 0.1727 | 1.2817 | -0.9011 |
| remove_top8 | 0.2691 | 0.6844 | 6.8715 | -11.2240 |
| keep_top8 | 0.3773 | 0.6055 | 7.0017 | -6.4296 |
| random_remove8 | 0.5855 | 0.3090 | 2.4352 | -2.5122 |
| remove_top16 | 0.1980 | 0.7871 | 9.1754 | -14.7724 |
| keep_top16 | 0.5391 | 0.4051 | 2.8349 | -1.7016 |
| random_remove16 | 0.3793 | 0.5664 | 5.1972 | -6.9018 |

## Top baseline-pred -> control-pred transitions

### remove_particle0
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_H4q | 94 | 0.3686 |
| label_Tbl | label_QCD | 79 | 0.3123 |
| label_Hcc | label_H4q | 45 | 0.2045 |
| label_Tbl | label_Hbb | 50 | 0.1976 |
| label_Zqq | label_H4q | 45 | 0.1793 |
| label_Wqq | label_Zqq | 35 | 0.1296 |
| label_Zqq | label_Wqq | 28 | 0.1116 |
| label_Tbl | label_Tbqq | 28 | 0.1107 |
| label_Hqql | label_Wqq | 27 | 0.1059 |
| label_Hgg | label_H4q | 23 | 0.0821 |
| label_Wqq | label_H4q | 21 | 0.0778 |
| label_Hqql | label_Zqq | 18 | 0.0706 |

### keep_only_particle0
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_Tbl | 197 | 0.7725 |
| label_H4q | label_Wqq | 129 | 0.4708 |
| label_Hgg | label_Wqq | 112 | 0.4000 |
| label_Hcc | label_Wqq | 81 | 0.3682 |
| label_Zqq | label_Wqq | 87 | 0.3466 |
| label_Hbb | label_Wqq | 75 | 0.3086 |
| label_Tbqq | label_Wqq | 84 | 0.3077 |
| label_Hbb | label_Tbl | 67 | 0.2757 |
| label_Tbqq | label_H4q | 72 | 0.2637 |
| label_Zqq | label_QCD | 63 | 0.2510 |
| label_Hcc | label_Tbl | 55 | 0.2500 |
| label_Wqq | label_QCD | 67 | 0.2481 |

### remove_top1
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_H4q | 94 | 0.3686 |
| label_Tbl | label_QCD | 79 | 0.3123 |
| label_Hcc | label_H4q | 45 | 0.2045 |
| label_Tbl | label_Hbb | 50 | 0.1976 |
| label_Zqq | label_H4q | 45 | 0.1793 |
| label_Wqq | label_Zqq | 35 | 0.1296 |
| label_Zqq | label_Wqq | 28 | 0.1116 |
| label_Tbl | label_Tbqq | 28 | 0.1107 |
| label_Hqql | label_Wqq | 27 | 0.1059 |
| label_Hgg | label_H4q | 23 | 0.0821 |
| label_Wqq | label_H4q | 21 | 0.0778 |
| label_Hqql | label_Zqq | 18 | 0.0706 |

### keep_top1
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_Tbl | 197 | 0.7725 |
| label_H4q | label_Wqq | 129 | 0.4708 |
| label_Hgg | label_Wqq | 112 | 0.4000 |
| label_Hcc | label_Wqq | 81 | 0.3682 |
| label_Zqq | label_Wqq | 87 | 0.3466 |
| label_Hbb | label_Wqq | 75 | 0.3086 |
| label_Tbqq | label_Wqq | 84 | 0.3077 |
| label_Hbb | label_Tbl | 67 | 0.2757 |
| label_Tbqq | label_H4q | 72 | 0.2637 |
| label_Zqq | label_QCD | 63 | 0.2510 |
| label_Hcc | label_Tbl | 55 | 0.2500 |
| label_Wqq | label_QCD | 67 | 0.2481 |

### remove_top4
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_H4q | 174 | 0.6824 |
| label_Zqq | label_H4q | 167 | 0.6653 |
| label_Wqq | label_H4q | 166 | 0.6148 |
| label_Hcc | label_H4q | 135 | 0.6136 |
| label_Tbl | label_QCD | 88 | 0.3478 |
| label_Hbb | label_H4q | 77 | 0.3169 |
| label_Tbqq | label_H4q | 56 | 0.2051 |
| label_Tbl | label_H4q | 48 | 0.1897 |
| label_Tbl | label_Hbb | 40 | 0.1581 |
| label_Hcc | label_Tbqq | 30 | 0.1364 |
| label_Hbb | label_Tbqq | 32 | 0.1317 |
| label_H4q | label_Hgg | 35 | 0.1277 |

### keep_top4
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Tbqq | label_H4q | 165 | 0.6044 |
| label_Tbl | label_Hqql | 152 | 0.6008 |
| label_Hgg | label_H4q | 125 | 0.4464 |
| label_Hgg | label_Wqq | 108 | 0.3857 |
| label_Zqq | label_Wqq | 90 | 0.3586 |
| label_Zqq | label_QCD | 88 | 0.3506 |
| label_Wqq | label_QCD | 88 | 0.3259 |
| label_Hcc | label_H4q | 65 | 0.2955 |
| label_Hbb | label_Wqq | 69 | 0.2840 |
| label_Hcc | label_Wqq | 60 | 0.2727 |
| label_Hbb | label_H4q | 64 | 0.2634 |
| label_H4q | label_Wqq | 69 | 0.2518 |

### remove_top16
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Tbl | label_QCD | 223 | 0.8814 |
| label_Hqql | label_QCD | 204 | 0.8000 |
| label_Wqq | label_QCD | 189 | 0.7000 |
| label_Zqq | label_QCD | 169 | 0.6733 |
| label_Hcc | label_QCD | 121 | 0.5500 |
| label_Hbb | label_H4q | 107 | 0.4403 |
| label_Tbqq | label_QCD | 104 | 0.3810 |
| label_Tbqq | label_H4q | 103 | 0.3773 |
| label_Hbb | label_QCD | 85 | 0.3498 |
| label_Hcc | label_H4q | 71 | 0.3227 |
| label_H4q | label_Hgg | 87 | 0.3175 |
| label_H4q | label_QCD | 79 | 0.2883 |

### keep_top16
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hgg | label_H4q | 135 | 0.4821 |
| label_Tbqq | label_H4q | 123 | 0.4505 |
| label_Zqq | label_Wqq | 113 | 0.4502 |
| label_Hbb | label_Hcc | 56 | 0.2305 |
| label_Hgg | label_Wqq | 63 | 0.2250 |
| label_Hcc | label_Zqq | 46 | 0.2091 |
| label_Hbb | label_Zqq | 46 | 0.1893 |
| label_Hgg | label_Zqq | 46 | 0.1643 |
| label_Hbb | label_H4q | 39 | 0.1605 |
| label_QCD | label_Wqq | 36 | 0.1494 |
| label_Tbl | label_Hqql | 36 | 0.1423 |
| label_H4q | label_Wqq | 37 | 0.1350 |

## Top true-class -> control-pred transitions

### remove_particle0
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_H4q | 92 | 0.3594 |
| label_Tbl | label_QCD | 76 | 0.2969 |
| label_Hcc | label_H4q | 53 | 0.2070 |
| label_Zqq | label_Wqq | 50 | 0.1953 |
| label_Tbl | label_Hbb | 50 | 0.1953 |
| label_Zqq | label_H4q | 46 | 0.1797 |
| label_Wqq | label_Zqq | 41 | 0.1602 |
| label_Hgg | label_H4q | 38 | 0.1484 |
| label_Hcc | label_Hgg | 33 | 0.1289 |
| label_Hbb | label_Hgg | 32 | 0.1250 |
| label_Tbl | label_Tbqq | 28 | 0.1094 |
| label_Hqql | label_Wqq | 27 | 0.1055 |

### keep_only_particle0
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_Tbl | 195 | 0.7617 |
| label_H4q | label_Wqq | 119 | 0.4648 |
| label_Hgg | label_Wqq | 104 | 0.4062 |
| label_Hcc | label_Wqq | 100 | 0.3906 |
| label_Zqq | label_Wqq | 88 | 0.3438 |
| label_Hbb | label_Wqq | 78 | 0.3047 |
| label_Tbqq | label_Wqq | 77 | 0.3008 |
| label_Hbb | label_Tbl | 69 | 0.2695 |
| label_Tbqq | label_H4q | 65 | 0.2539 |
| label_Wqq | label_QCD | 63 | 0.2461 |
| label_Hcc | label_Tbl | 56 | 0.2188 |
| label_Zqq | label_QCD | 56 | 0.2188 |

### remove_top1
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_H4q | 92 | 0.3594 |
| label_Tbl | label_QCD | 76 | 0.2969 |
| label_Hcc | label_H4q | 53 | 0.2070 |
| label_Zqq | label_Wqq | 50 | 0.1953 |
| label_Tbl | label_Hbb | 50 | 0.1953 |
| label_Zqq | label_H4q | 46 | 0.1797 |
| label_Wqq | label_Zqq | 41 | 0.1602 |
| label_Hgg | label_H4q | 38 | 0.1484 |
| label_Hcc | label_Hgg | 33 | 0.1289 |
| label_Hbb | label_Hgg | 32 | 0.1250 |
| label_Tbl | label_Tbqq | 28 | 0.1094 |
| label_Hqql | label_Wqq | 27 | 0.1055 |

### keep_top1
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_Tbl | 195 | 0.7617 |
| label_H4q | label_Wqq | 119 | 0.4648 |
| label_Hgg | label_Wqq | 104 | 0.4062 |
| label_Hcc | label_Wqq | 100 | 0.3906 |
| label_Zqq | label_Wqq | 88 | 0.3438 |
| label_Hbb | label_Wqq | 78 | 0.3047 |
| label_Tbqq | label_Wqq | 77 | 0.3008 |
| label_Hbb | label_Tbl | 69 | 0.2695 |
| label_Tbqq | label_H4q | 65 | 0.2539 |
| label_Wqq | label_QCD | 63 | 0.2461 |
| label_Hcc | label_Tbl | 56 | 0.2188 |
| label_Zqq | label_QCD | 56 | 0.2188 |

### remove_top4
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Hqql | label_H4q | 175 | 0.6836 |
| label_Zqq | label_H4q | 162 | 0.6328 |
| label_Wqq | label_H4q | 154 | 0.6016 |
| label_Hcc | label_H4q | 147 | 0.5742 |
| label_Tbl | label_QCD | 88 | 0.3438 |
| label_Hbb | label_H4q | 83 | 0.3242 |
| label_Tbqq | label_H4q | 53 | 0.2070 |
| label_QCD | label_H4q | 52 | 0.2031 |
| label_Tbl | label_H4q | 50 | 0.1953 |
| label_Hgg | label_H4q | 47 | 0.1836 |
| label_H4q | label_Hgg | 41 | 0.1602 |
| label_Tbl | label_Hbb | 39 | 0.1523 |

### keep_top4
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Tbl | label_Hqql | 156 | 0.6094 |
| label_Tbqq | label_H4q | 151 | 0.5898 |
| label_Hgg | label_H4q | 101 | 0.3945 |
| label_Hgg | label_Wqq | 91 | 0.3555 |
| label_Zqq | label_QCD | 90 | 0.3516 |
| label_Zqq | label_Wqq | 88 | 0.3438 |
| label_Hcc | label_H4q | 87 | 0.3398 |
| label_Wqq | label_QCD | 83 | 0.3242 |
| label_Hbb | label_Wqq | 77 | 0.3008 |
| label_Hbb | label_H4q | 69 | 0.2695 |
| label_Hcc | label_Wqq | 65 | 0.2539 |
| label_H4q | label_Wqq | 64 | 0.2500 |

### remove_top16
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Tbl | label_QCD | 224 | 0.8750 |
| label_Hqql | label_QCD | 205 | 0.8008 |
| label_Wqq | label_QCD | 183 | 0.7148 |
| label_Zqq | label_QCD | 170 | 0.6641 |
| label_Hcc | label_QCD | 134 | 0.5234 |
| label_Hbb | label_H4q | 111 | 0.4336 |
| label_Tbqq | label_H4q | 103 | 0.4023 |
| label_Tbqq | label_QCD | 98 | 0.3828 |
| label_Hbb | label_QCD | 85 | 0.3320 |
| label_H4q | label_QCD | 79 | 0.3086 |
| label_H4q | label_Hgg | 78 | 0.3047 |
| label_Hcc | label_H4q | 75 | 0.2930 |

### keep_top16
| from | to | n | rate |
| --- | --- | --- | --- |
| label_Zqq | label_Wqq | 132 | 0.5156 |
| label_Hgg | label_H4q | 117 | 0.4570 |
| label_Tbqq | label_H4q | 112 | 0.4375 |
| label_Hbb | label_Hcc | 58 | 0.2266 |
| label_Hgg | label_Wqq | 55 | 0.2148 |
| label_Hcc | label_H4q | 51 | 0.1992 |
| label_QCD | label_Wqq | 49 | 0.1914 |
| label_Hbb | label_Zqq | 47 | 0.1836 |
| label_Hgg | label_Zqq | 46 | 0.1797 |
| label_Hbb | label_H4q | 45 | 0.1758 |
| label_Hcc | label_Zqq | 45 | 0.1758 |
| label_Tbl | label_Hqql | 43 | 0.1680 |

## Interpretation

- Use `baseline_pred_to_control_pred` to see model-decision competition after a control.
- Use `true_class_to_control_pred` to see which real classes become confused.
- Tbl/Hqql transitions after `remove_particle0` are the first place to inspect for class-local shortcuts/proxies.
