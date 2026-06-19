# Official Weaver prediction probe v6

pred_dir=runs/official_weaver_predict_v5_kinpid
n_files=10
acc_from_filename=0.1015

| file | sample | true | entries | acc | score branches | pred_counts |
| --- | --- | --- | ---: | ---: | --- | --- |
| `pred_HToBB.root` | HToBB | label_Hbb | 100000 | 0.00276 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[80713, 276, 981, 113, 1134, 80, 13399, 2760, 20, 524]` |
| `pred_HToCC.root` | HToCC | label_Hcc | 100000 | 0.00886 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[76651, 281, 886, 65, 805, 19, 17414, 3740, 9, 130]` |
| `pred_HToGG.root` | HToGG | label_Hgg | 100000 | 0.00011 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[81099, 35, 2952, 11, 3825, 2, 11637, 399, 30, 10]` |
| `pred_HToWW2Q1L.root` | HToWW2Q1L | label_Hqql | 100000 | 0.00421 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[39761, 3318, 8025, 258, 1013, 421, 45343, 1132, 48, 681]` |
| `pred_HToWW4Q.root` | HToWW4Q | label_H4q | 100000 | 0.039 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[81814, 40, 3047, 46, 3900, 1, 10629, 505, 6, 12]` |
| `pred_TTBar.root` | TTBar | label_Tbqq | 100000 | 1e-05 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[97969, 12, 65, 5, 350, 4, 1147, 439, 1, 8]` |
| `pred_TTBarLep.root` | TTBarLep | label_Tbl | 100000 | 0.03241 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[51609, 9487, 8832, 252, 245, 1827, 20837, 3623, 47, 3241]` |
| `pred_WToQQ.root` | WToQQ | label_Wqq | 100000 | 0.00421 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[29388, 1120, 7370, 167, 490, 5, 60806, 421, 66, 167]` |
| `pred_ZJetsToNuNu.root` | ZJetsToNuNu | label_QCD | 100000 | 0.37151 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[37151, 261, 2947, 267, 1457, 20, 56511, 810, 458, 118]` |
| `pred_ZToQQ.root` | ZToQQ | label_Zqq | 100000 | 0.55195 | `['score_label_QCD', 'score_label_Hbb', 'score_label_Hcc', 'score_label_Hgg', 'score_label_H4q', 'score_label_Hqql', 'score_label_Zqq', 'score_label_Wqq', 'score_label_Tbqq', 'score_label_Tbl']` | `[36769, 714, 5254, 103, 537, 26, 55195, 922, 46, 434]` |

## First file branches

```json
[
  "label_QCD",
  "score_label_QCD",
  "label_Hbb",
  "score_label_Hbb",
  "label_Hcc",
  "score_label_Hcc",
  "label_Hgg",
  "score_label_Hgg",
  "label_H4q",
  "score_label_H4q",
  "label_Hqql",
  "score_label_Hqql",
  "label_Zqq",
  "score_label_Zqq",
  "label_Wqq",
  "score_label_Wqq",
  "label_Tbqq",
  "score_label_Tbqq",
  "label_Tbl",
  "score_label_Tbl",
  "_label_",
  "jet_pt",
  "jet_eta",
  "jet_phi",
  "jet_energy",
  "jet_nparticles",
  "jet_sdmass",
  "jet_tau1",
  "jet_tau2",
  "jet_tau3",
  "jet_tau4"
]
```
