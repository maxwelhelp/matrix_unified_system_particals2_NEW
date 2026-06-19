# EdgeConv Inner Trace v2

Richer KNN/neighbor route trace for question-ranked pseudo-heads.

## Head route summary
| head | route | p0_top | lead_top | knn_p0 | knn_lead | top4_nb | dR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L2_ch224:256 | core particle + core-neighborhood route | 1.0000 | 1.0000 | 0.8750 | 0.8750 | 0.0703 | 0.2574 |
| L2_ch128:160 | core particle + core-neighborhood route | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0625 | 0.2396 |
| L2_ch0:32 | core particle + core-neighborhood route | 0.7500 | 0.7500 | 0.6250 | 0.6250 | 0.0703 | 0.2635 |
| L2_ch32:64 | core particle + core-neighborhood route | 0.8750 | 0.8750 | 0.7500 | 0.7500 | 0.0703 | 0.2887 |
| L2_ch64:96 | core particle + core-neighborhood route | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0938 | 0.1955 |
| L2_ch160:192 | core particle + core-neighborhood route | 0.8750 | 0.8750 | 0.6250 | 0.6250 | 0.0625 | 0.2540 |
| L1_ch0:16 | context/non-core route | 0.1250 | 0.1250 | 0.1250 | 0.1250 | 0.0625 | 0.0369 |
| L2_ch192:224 | context/non-core route | 0.3750 | 0.3750 | 0.2500 | 0.2500 | 0.0391 | 0.1821 |
| L1_ch112:128 | context/non-core route | 0.2500 | 0.2500 | 0.2500 | 0.2500 | 0.0625 | 0.1542 |
| L0_ch40:48 | context/non-core route | 0.0000 | 0.0000 | 0.2500 | 0.2500 | 0.0234 | 1.6932 |

## Event route examples
| head | rank | event | true | pred | top | lead | score | knn_p0 | knn_lead | nb_top4 | nb_dR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L2_ch224:256 | 1 | 369 | label_Tbl | label_Tbl | 0 | 0 | 0.6458 | 1 | 1 | 0.0625 | 0.2548 |
| L2_ch224:256 | 2 | 332 | label_Tbl | label_Tbl | 0 | 0 | 0.5683 | 0 | 0 | 0.1250 | 0.2847 |
| L2_ch224:256 | 3 | 355 | label_Tbl | label_Tbl | 0 | 0 | 0.5429 | 1 | 1 | 0.0625 | 0.2881 |
| L2_ch224:256 | 4 | 323 | label_Tbl | label_Tbl | 0 | 0 | 0.5153 | 1 | 1 | 0.0625 | 0.3361 |
| L2_ch224:256 | 5 | 334 | label_Tbl | label_Tbl | 0 | 0 | 0.5128 | 1 | 1 | 0.0625 | 0.2095 |
| L2_ch224:256 | 6 | 340 | label_Tbl | label_Tbl | 0 | 0 | 0.4992 | 1 | 1 | 0.0625 | 0.2980 |
| L2_ch224:256 | 7 | 337 | label_Tbl | label_Tbl | 0 | 0 | 0.4978 | 1 | 1 | 0.0625 | 0.3087 |
| L2_ch224:256 | 8 | 197 | label_Hqql | label_Tbl | 0 | 0 | 0.4960 | 1 | 1 | 0.0625 | 0.0789 |
| L2_ch128:160 | 1 | 327 | label_Tbl | label_Tbl | 0 | 0 | 0.6819 | 1 | 1 | 0.0625 | 0.2529 |
| L2_ch128:160 | 2 | 376 | label_Tbl | label_Tbl | 0 | 0 | 0.6815 | 1 | 1 | 0.0625 | 0.2787 |
| L2_ch128:160 | 3 | 362 | label_Tbl | label_Tbl | 0 | 0 | 0.6496 | 1 | 1 | 0.0625 | 0.3023 |
| L2_ch128:160 | 4 | 373 | label_Tbl | label_Tbl | 0 | 0 | 0.6484 | 1 | 1 | 0.0625 | 0.1563 |
| L2_ch128:160 | 5 | 356 | label_Tbl | label_Tbl | 0 | 0 | 0.6449 | 1 | 1 | 0.0625 | 0.1316 |
| L2_ch128:160 | 6 | 342 | label_Tbl | label_Tbl | 0 | 0 | 0.6404 | 1 | 1 | 0.0625 | 0.2390 |
| L2_ch128:160 | 7 | 365 | label_Tbl | label_Tbl | 0 | 0 | 0.6011 | 1 | 1 | 0.0625 | 0.3081 |
| L2_ch128:160 | 8 | 379 | label_Tbl | label_Tbl | 0 | 0 | 0.5979 | 1 | 1 | 0.0625 | 0.2477 |
| L2_ch0:32 | 1 | 369 | label_Tbl | label_Tbl | 0 | 0 | 0.4082 | 1 | 1 | 0.0625 | 0.2548 |
| L2_ch0:32 | 2 | 332 | label_Tbl | label_Tbl | 0 | 0 | 0.3955 | 0 | 0 | 0.1250 | 0.2847 |
| L2_ch0:32 | 3 | 351 | label_Tbl | label_Tbl | 0 | 0 | 0.3941 | 1 | 1 | 0.1250 | 0.3332 |
| L2_ch0:32 | 4 | 341 | label_Tbl | label_Tbl | 0 | 0 | 0.3858 | 1 | 1 | 0.0625 | 0.3755 |
| L2_ch0:32 | 5 | 340 | label_Tbl | label_Tbl | 0 | 0 | 0.3713 | 1 | 1 | 0.0625 | 0.2980 |
| L2_ch0:32 | 6 | 365 | label_Tbl | label_Tbl | 0 | 0 | 0.3634 | 1 | 1 | 0.0625 | 0.3081 |
| L2_ch0:32 | 7 | 434 | label_Tbqq | label_Tbqq | 3 | 0 | 0.3565 | 0 | 0 | 0.0625 | 0.1667 |
| L2_ch0:32 | 8 | 445 | label_Tbqq | label_Tbqq | 4 | 0 | 0.3338 | 0 | 0 | 0.0000 | 0.0873 |
| L2_ch32:64 | 1 | 351 | label_Tbl | label_Tbl | 0 | 0 | 0.7287 | 1 | 1 | 0.1250 | 0.3332 |
| L2_ch32:64 | 2 | 369 | label_Tbl | label_Tbl | 0 | 0 | 0.7211 | 1 | 1 | 0.0625 | 0.2548 |
| L2_ch32:64 | 3 | 332 | label_Tbl | label_Tbl | 0 | 0 | 0.6587 | 0 | 0 | 0.1250 | 0.2847 |
| L2_ch32:64 | 4 | 340 | label_Tbl | label_Tbl | 0 | 0 | 0.6397 | 1 | 1 | 0.0625 | 0.2980 |
| L2_ch32:64 | 5 | 400 | label_Tbqq | label_Tbqq | 2 | 0 | 0.5830 | 0 | 0 | 0.0000 | 0.1520 |
| L2_ch32:64 | 6 | 383 | label_Tbl | label_Tbl | 0 | 0 | 0.5593 | 1 | 1 | 0.0625 | 0.4315 |
| L2_ch32:64 | 7 | 365 | label_Tbl | label_Tbl | 0 | 0 | 0.5556 | 1 | 1 | 0.0625 | 0.3081 |
| L2_ch32:64 | 8 | 379 | label_Tbl | label_Tbl | 0 | 0 | 0.5550 | 1 | 1 | 0.0625 | 0.2477 |
| L2_ch64:96 | 1 | 198 | label_Hqql | label_Hqql | 0 | 0 | 0.3590 | 1 | 1 | 0.0625 | 0.0382 |
| L2_ch64:96 | 2 | 337 | label_Tbl | label_Tbl | 0 | 0 | 0.3299 | 1 | 1 | 0.0625 | 0.3087 |
| L2_ch64:96 | 3 | 379 | label_Tbl | label_Tbl | 0 | 0 | 0.3216 | 1 | 1 | 0.0625 | 0.2477 |
| L2_ch64:96 | 4 | 217 | label_Hqql | label_Hqql | 0 | 0 | 0.3145 | 1 | 1 | 0.2500 | 0.0249 |
| L2_ch64:96 | 5 | 351 | label_Tbl | label_Tbl | 0 | 0 | 0.3093 | 1 | 1 | 0.1250 | 0.3332 |
| L2_ch64:96 | 6 | 353 | label_Tbl | label_Tbl | 0 | 0 | 0.3082 | 1 | 1 | 0.0625 | 0.2705 |
| L2_ch64:96 | 7 | 356 | label_Tbl | label_Tbl | 0 | 0 | 0.2884 | 1 | 1 | 0.0625 | 0.1316 |
| L2_ch64:96 | 8 | 334 | label_Tbl | label_Tbl | 0 | 0 | 0.2880 | 1 | 1 | 0.0625 | 0.2095 |
| L2_ch160:192 | 1 | 351 | label_Tbl | label_Tbl | 0 | 0 | 0.7933 | 1 | 1 | 0.1250 | 0.3332 |
| L2_ch160:192 | 2 | 379 | label_Tbl | label_Tbl | 0 | 0 | 0.7500 | 1 | 1 | 0.0625 | 0.2477 |
| L2_ch160:192 | 3 | 365 | label_Tbl | label_Tbl | 0 | 0 | 0.6882 | 1 | 1 | 0.0625 | 0.3081 |
| L2_ch160:192 | 4 | 370 | label_Tbl | label_Tbl | 0 | 0 | 0.6369 | 0 | 0 | 0.0000 | 0.2151 |
| L2_ch160:192 | 5 | 415 | label_Tbqq | label_Tbqq | 1 | 0 | 0.5975 | 0 | 0 | 0.0000 | 0.2327 |
| L2_ch160:192 | 6 | 332 | label_Tbl | label_Tbl | 0 | 0 | 0.5925 | 0 | 0 | 0.1250 | 0.2847 |
| L2_ch160:192 | 7 | 376 | label_Tbl | label_Tbl | 0 | 0 | 0.5447 | 1 | 1 | 0.0625 | 0.2787 |
| L2_ch160:192 | 8 | 356 | label_Tbl | label_Tbl | 0 | 0 | 0.5051 | 1 | 1 | 0.0625 | 0.1316 |
| L1_ch0:16 | 1 | 383 | label_Tbl | label_Tbl | 1 | 0 | 7.2508 | 0 | 0 | 0.1250 | 0.0369 |
| L1_ch0:16 | 2 | 76 | label_Hcc | label_Hcc | 3 | 0 | 7.2441 | 0 | 0 | 0.0625 | 0.0207 |
| L1_ch0:16 | 3 | 369 | label_Tbl | label_Tbl | 2 | 0 | 6.7681 | 0 | 0 | 0.0625 | 0.0134 |
| L1_ch0:16 | 4 | 565 | label_QCD | label_QCD | 2 | 0 | 6.7588 | 0 | 0 | 0.1250 | 0.0313 |
| L1_ch0:16 | 5 | 332 | label_Tbl | label_Tbl | 4 | 0 | 6.4890 | 0 | 0 | 0.0000 | 0.0366 |
| L1_ch0:16 | 6 | 517 | label_QCD | label_QCD | 0 | 0 | 6.4161 | 1 | 1 | 0.0625 | 0.0418 |
| L1_ch0:16 | 7 | 416 | label_Tbqq | label_Tbqq | 13 | 0 | 6.3927 | 0 | 0 | 0.0000 | 0.1109 |
| L1_ch0:16 | 8 | 320 | label_Tbl | label_Tbl | 16 | 0 | 6.2390 | 0 | 0 | 0.0625 | 0.0036 |
| L2_ch192:224 | 1 | 332 | label_Tbl | label_Tbl | 0 | 0 | 0.4874 | 0 | 0 | 0.1250 | 0.2847 |
| L2_ch192:224 | 2 | 400 | label_Tbqq | label_Tbqq | 2 | 0 | 0.4061 | 0 | 0 | 0.0000 | 0.1520 |
| L2_ch192:224 | 3 | 379 | label_Tbl | label_Tbl | 0 | 0 | 0.3873 | 1 | 1 | 0.0625 | 0.2477 |
| L2_ch192:224 | 4 | 415 | label_Tbqq | label_Tbqq | 1 | 0 | 0.3588 | 0 | 0 | 0.0000 | 0.2327 |
| L2_ch192:224 | 5 | 398 | label_Tbqq | label_Tbqq | 7 | 0 | 0.3385 | 0 | 0 | 0.0000 | 0.0721 |
| L2_ch192:224 | 6 | 389 | label_Tbqq | label_Tbqq | 9 | 0 | 0.3325 | 0 | 0 | 0.0000 | 0.0490 |
| L2_ch192:224 | 7 | 351 | label_Tbl | label_Tbl | 0 | 0 | 0.2955 | 1 | 1 | 0.1250 | 0.3332 |
| L2_ch192:224 | 8 | 392 | label_Tbqq | label_Tbqq | 4 | 0 | 0.2817 | 0 | 0 | 0.0000 | 0.0853 |
| L1_ch112:128 | 1 | 106 | label_Hcc | label_Hcc | 19 | 0 | 6.0516 | 0 | 0 | 0.0625 | 0.1398 |
| L1_ch112:128 | 2 | 464 | label_Wqq | label_Wqq | 17 | 0 | 5.8654 | 0 | 0 | 0.0625 | 0.1365 |
| L1_ch112:128 | 3 | 134 | label_Hgg | label_Hgg | 31 | 0 | 5.8620 | 0 | 0 | 0.0625 | 0.2059 |
| L1_ch112:128 | 4 | 355 | label_Tbl | label_Tbl | 0 | 0 | 5.8467 | 1 | 1 | 0.0625 | 0.2881 |
| L1_ch112:128 | 5 | 442 | label_Tbqq | label_Tbqq | 33 | 0 | 5.7272 | 0 | 0 | 0.0000 | 0.1914 |
| L1_ch112:128 | 6 | 623 | label_Zqq | label_Zqq | 3 | 0 | 5.6757 | 0 | 0 | 0.1250 | 0.0280 |
| L1_ch112:128 | 7 | 351 | label_Tbl | label_Tbl | 29 | 0 | 5.6099 | 0 | 0 | 0.0625 | 0.2146 |
| L1_ch112:128 | 8 | 88 | label_Hcc | label_Hcc | 0 | 0 | 5.5992 | 1 | 1 | 0.0625 | 0.0292 |
| L0_ch40:48 | 1 | 86 | label_Hcc | label_Hcc | 36 | 0 | 13.9624 | 0 | 0 | 0.0000 | 1.9702 |
| L0_ch40:48 | 2 | 523 | label_QCD | label_Tbqq | 52 | 0 | 13.6218 | 0 | 0 | 0.0000 | 1.6840 |
| L0_ch40:48 | 3 | 138 | label_Hgg | label_Hcc | 36 | 0 | 13.3192 | 0 | 0 | 0.0000 | 1.7102 |
| L0_ch40:48 | 4 | 490 | label_Wqq | label_H4q | 52 | 0 | 12.5176 | 0 | 0 | 0.0000 | 2.1075 |
| L0_ch40:48 | 5 | 397 | label_Tbqq | label_Tbqq | 49 | 0 | 12.3968 | 0 | 0 | 0.0000 | 1.2667 |
| L0_ch40:48 | 6 | 284 | label_H4q | label_H4q | 49 | 0 | 11.9891 | 0 | 0 | 0.0625 | 1.9370 |
| L0_ch40:48 | 7 | 133 | label_Hgg | label_Hgg | 52 | 0 | 11.9696 | 1 | 1 | 0.0625 | 1.2444 |
| L0_ch40:48 | 8 | 342 | label_Tbl | label_Tbl | 31 | 0 | 11.8864 | 1 | 1 | 0.0625 | 1.6252 |

## Interpretation

Use `route_pattern` and neighbor statistics to refine pseudocode v3/v4. Core L2 readouts should have high top particle0/leading rates; context builders may have lower top particle0 but can still include core in KNN route.
