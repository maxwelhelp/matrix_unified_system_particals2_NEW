# PART_ALL_CLASS_ATLAS_PLANNER_V1

All-class atlas planner. It scans available prediction ROOT files, infers true/predicted class transitions, ranks class-pairs, and marks which pairs have enough source ROOT mapping for direct replay / full program graph decoding.

- prediction_files: **10**
- sources: **10**
- candidate_pairs: **90**
- ready_pairs: **72**
- min_error: **4**

## Top class-pair candidates
| rank | src | tgt | errors | src_total | err_rate | mean_margin | src_groups | tgt_groups | ready |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | label_Zqq | label_Wqq | 21990 | 100000 | 0.2199 | 0.3693 | ZToQQ | WToQQ | 1 |
| 2 | label_Wqq | label_Zqq | 14279 | 100000 | 0.1428 | 0.3258 | WToQQ | ZToQQ | 1 |
| 3 | label_Hcc | label_Hbb | 12027 | 100000 | 0.1203 | 0.3503 | HToCC | HToBB | 1 |
| 4 | label_Hbb | label_Hcc | 11871 | 100000 | 0.1187 | 0.3491 | HToBB | HToCC | 1 |
| 5 | label_Hgg | label_H4q | 10161 | 100000 | 0.1016 | 0.3988 | HToGG | HToWW4Q | 1 |
| 6 | label_Hbb | label_Hgg | 8744 | 100000 | 0.0874 | 0.3974 | HToBB | HToGG | 1 |
| 7 | label_Hcc | label_Hgg | 8451 | 100000 | 0.0845 | 0.3919 | HToCC | HToGG | 1 |
| 8 | label_H4q | label_Hgg | 8391 | 100000 | 0.0839 | 0.3494 | HToWW4Q | HToGG | 1 |
| 9 | label_Hcc | label_H4q | 6490 | 100000 | 0.0649 | 0.4426 | HToCC | HToWW4Q | 1 |
| 10 | label_Hgg | label_Hbb | 6016 | 100000 | 0.0602 | 0.3526 | HToGG | HToBB | 1 |
| 11 | label_Hgg | label_Hcc | 5963 | 100000 | 0.0596 | 0.3461 | HToGG | HToCC | 1 |
| 12 | label_Hcc | label_Zqq | 5425 | 100000 | 0.0542 | 0.4183 | HToCC | ZToQQ | 1 |
| 13 | label_Hbb | label_Zqq | 4758 | 100000 | 0.0476 | 0.3921 | HToBB | ZToQQ | 1 |
| 14 | label_Tbl | label_Hqql | 3776 | 100000 | 0.0378 | 0.4975 | TTBarLep | HToWW2Q1L | 1 |
| 15 | label_Hqql | label_Tbl | 3400 | 100000 | 0.0340 | 0.4791 | HToWW2Q1L | TTBarLep | 1 |
| 16 | label_H4q | label_Hcc | 2991 | 100000 | 0.0299 | 0.3052 | HToWW4Q | HToCC | 1 |
| 17 | label_Zqq | label_Hbb | 2890 | 100000 | 0.0289 | 0.3816 | ZToQQ | HToBB | 1 |
| 18 | label_Zqq | label_Hcc | 2878 | 100000 | 0.0288 | 0.3860 | ZToQQ | HToCC | 1 |
| 19 | label_Hbb | label_H4q | 2684 | 100000 | 0.0268 | 0.4345 | HToBB | HToWW4Q | 1 |
| 20 | label_Tbqq | label_H4q | 2569 | 100000 | 0.0257 | 0.4169 | TTBar | HToWW4Q | 1 |
| 21 | label_Hbb | label_Tbqq | 2555 | 100000 | 0.0255 | 0.4920 | HToBB | TTBar | 1 |
| 22 | label_Hcc | label_Tbqq | 2512 | 100000 | 0.0251 | 0.4784 | HToCC | TTBar | 1 |
| 23 | label_Zqq | label_H4q | 2473 | 100000 | 0.0247 | 0.4099 | ZToQQ | HToWW4Q | 1 |
| 24 | label_Hgg | label_Zqq | 2444 | 100000 | 0.0244 | 0.3596 | HToGG | ZToQQ | 1 |
| 25 | label_H4q | label_Tbqq | 2298 | 100000 | 0.0230 | 0.4054 | HToWW4Q | TTBar | 1 |
| 26 | label_Zqq | label_Tbqq | 1907 | 100000 | 0.0191 | 0.5582 | ZToQQ | TTBar | 1 |
| 27 | label_Wqq | label_H4q | 1885 | 100000 | 0.0188 | 0.4480 | WToQQ | HToWW4Q | 1 |
| 28 | label_Wqq | label_Tbqq | 1872 | 100000 | 0.0187 | 0.5623 | WToQQ | TTBar | 1 |
| 29 | label_Zqq | label_Hgg | 1824 | 100000 | 0.0182 | 0.3369 | ZToQQ | HToGG | 1 |
| 30 | label_H4q | label_Zqq | 1758 | 100000 | 0.0176 | 0.3327 | HToWW4Q | ZToQQ | 1 |

## Available sources
| group | label | events | source_root_available | prediction_root |
| --- | --- | --- | --- | --- |
| HToBB | label_Hbb | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_HToBB.root |
| HToCC | label_Hcc | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_HToCC.root |
| HToGG | label_Hgg | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_HToGG.root |
| HToWW2Q1L | label_Hqql | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root |
| HToWW4Q | label_H4q | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root |
| TTBar | label_Tbqq | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_TTBar.root |
| TTBarLep | label_Tbl | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root |
| WToQQ | label_Wqq | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_WToQQ.root |
| ZJetsToNuNu |  | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_ZJetsToNuNu.root |
| ZToQQ | label_Zqq | 100000 | 1 | reports/latest/part_weaver_predict_smoke_v3_ZToQQ.root |

## Decision

`ATLAS_PLANNER_OK`: at least one pair has both source and target source roots; next step can build direct replay pair groups.
