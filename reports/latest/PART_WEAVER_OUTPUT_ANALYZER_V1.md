# PART_WEAVER_OUTPUT_ANALYZER_V1

- glob: `reports/latest/part_weaver_predict_smoke_v3_*.root`
- files: **10**

## Summary
| file | n | accuracy | labels | scores | prefix | error |
| --- | --- | --- | --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | 500000 | 0.000378 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | 500000 | 0.037204 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | 500000 | 0.0 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | 500000 | 0.255976 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | 500000 | 0.000174 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | 500000 | 0.0 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | 500000 | 0.145936 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_WToQQ.root | 500000 | 0.0001 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZJetsToNuNu.root | 500000 | 0.71229 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZToQQ.root | 500000 | 0.078674 | 10 | 10 | score_ |  |

## Top confusion pairs
| file | true | pred | n |
| --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Zqq | 245491 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_QCD | 185859 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hcc | 26583 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hqql | 22137 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Tbl | 19530 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hbb | 189 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Wqq | 94 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_H4q | 69 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hgg | 48 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Zqq | 228587 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hqql | 93812 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_QCD | 85562 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Tbl | 71963 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hcc | 18602 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hbb | 989 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_H4q | 428 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Wqq | 51 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hgg | 6 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Zqq | 303399 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_QCD | 142281 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hqql | 30517 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Tbl | 12183 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hcc | 11205 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hbb | 340 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_H4q | 67 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Wqq | 8 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_QCD | 189140 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hqql | 127988 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hcc | 111079 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Zqq | 45669 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Tbl | 22925 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_H4q | 3091 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Wqq | 62 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hgg | 25 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hbb | 21 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Zqq | 296173 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_QCD | 110595 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hqql | 66472 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hcc | 17085 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Tbl | 9469 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hbb | 102 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_H4q | 87 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Wqq | 17 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Zqq | 443625 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_QCD | 22770 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Tbl | 17245 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hqql | 15390 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hcc | 546 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hbb | 287 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Wqq | 132 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_H4q | 4 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hgg | 1 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_QCD | 177568 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Zqq | 111460 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hcc | 104240 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Tbl | 72968 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hqql | 31773 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_H4q | 1087 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hgg | 544 |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | label_Tbl | label_Hbb | 195 |
