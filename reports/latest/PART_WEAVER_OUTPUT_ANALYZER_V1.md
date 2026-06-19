# PART_WEAVER_OUTPUT_ANALYZER_V1

- glob: `reports/latest/part_weaver_predict_smoke_v3_*.root`
- files: **10**

## Summary
| file | n | accuracy | labels | scores | prefix | error |
| --- | --- | --- | --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | 100000 | 0.66769 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | 100000 | 0.61341 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | 100000 | 0.69064 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | 100000 | 0.94536 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | 100000 | 0.80905 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | 100000 | 0.91365 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root | 100000 | 0.95654 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_WToQQ.root | 100000 | 0.74142 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZJetsToNuNu.root | 100000 | 0.72447 | 10 | 10 | score_ |  |
| reports/latest/part_weaver_predict_smoke_v3_ZToQQ.root | 100000 | 0.60435 | 10 | 10 | score_ |  |

## Top confusion pairs
| file | true | pred | n |
| --- | --- | --- | --- |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hbb | 66769 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hcc | 11871 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hgg | 8744 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Zqq | 4758 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_H4q | 2684 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Tbqq | 2555 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_QCD | 1607 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Wqq | 606 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Hqql | 300 |
| reports/latest/part_weaver_predict_smoke_v3_HToBB.root | label_Hbb | label_Tbl | 106 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hcc | 61341 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hbb | 12027 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hgg | 8451 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_H4q | 6490 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Zqq | 5425 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Tbqq | 2512 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_QCD | 2145 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Wqq | 1309 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Hqql | 221 |
| reports/latest/part_weaver_predict_smoke_v3_HToCC.root | label_Hcc | label_Tbl | 79 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hgg | 69064 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_H4q | 10161 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hbb | 6016 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hcc | 5963 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_QCD | 3749 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Zqq | 2444 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Tbqq | 1737 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Wqq | 819 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Hqql | 36 |
| reports/latest/part_weaver_predict_smoke_v3_HToGG.root | label_Hgg | label_Tbl | 11 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hqql | 94536 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Tbl | 3400 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Wqq | 521 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hbb | 449 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Zqq | 443 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hcc | 236 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Tbqq | 166 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_H4q | 142 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_QCD | 101 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root | label_Hqql | label_Hgg | 6 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_H4q | 80905 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hgg | 8391 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hcc | 2991 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Tbqq | 2298 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Zqq | 1758 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hbb | 1461 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Wqq | 1140 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_QCD | 928 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Hqql | 124 |
| reports/latest/part_weaver_predict_smoke_v3_HToWW4Q.root | label_H4q | label_Tbl | 4 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Tbqq | 91365 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_H4q | 2569 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_QCD | 1673 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hbb | 1353 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hcc | 1255 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hgg | 988 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Wqq | 372 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Zqq | 275 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Hqql | 80 |
| reports/latest/part_weaver_predict_smoke_v3_TTBar.root | label_Tbqq | label_Tbl | 70 |
