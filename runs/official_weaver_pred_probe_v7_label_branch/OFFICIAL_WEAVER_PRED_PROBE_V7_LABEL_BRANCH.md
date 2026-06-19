# Official Weaver prediction probe v7 label branch

pred_dir=runs/official_weaver_predict_v5_particlenet_kinpid
n_files=10

## Accuracy by filename mapping

acc=0.766658 label_perm_upper_greedy=0.766658

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

## Accuracy by one-hot label_* branches

acc=0.766658 label_perm_upper_greedy=0.766658

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

## Accuracy by _label_ branch

acc=0.766658 label_perm_upper_greedy=0.766658

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

| file | sample | file-label | entries | acc_file | acc_label_* | acc__label_ | pred_counts | _label_counts | label*_counts |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `pred_HToBB.root` | HToBB | label_Hbb | 100000 | 0.66769 | 0.66769 | 0.66769 | `[1607, 66769, 11871, 8744, 2684, 300, 4758, 606, 2555, 106]` | `[0, 100000, 0, 0, 0, 0, 0, 0, 0, 0]` | `[0, 100000, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_HToCC.root` | HToCC | label_Hcc | 100000 | 0.61341 | 0.61341 | 0.61341 | `[2145, 12027, 61341, 8451, 6490, 221, 5425, 1309, 2512, 79]` | `[0, 0, 100000, 0, 0, 0, 0, 0, 0, 0]` | `[0, 0, 100000, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_HToGG.root` | HToGG | label_Hgg | 100000 | 0.69064 | 0.69064 | 0.69064 | `[3749, 6016, 5963, 69064, 10161, 36, 2444, 819, 1737, 11]` | `[0, 0, 0, 100000, 0, 0, 0, 0, 0, 0]` | `[0, 0, 0, 100000, 0, 0, 0, 0, 0, 0]` |
| `pred_HToWW2Q1L.root` | HToWW2Q1L | label_Hqql | 100000 | 0.94536 | 0.94536 | 0.94536 | `[101, 449, 236, 6, 142, 94536, 443, 521, 166, 3400]` | `[0, 0, 0, 0, 0, 100000, 0, 0, 0, 0]` | `[0, 0, 0, 0, 0, 100000, 0, 0, 0, 0]` |
| `pred_HToWW4Q.root` | HToWW4Q | label_H4q | 100000 | 0.80905 | 0.80905 | 0.80905 | `[928, 1461, 2991, 8391, 80905, 124, 1758, 1140, 2298, 4]` | `[0, 0, 0, 0, 100000, 0, 0, 0, 0, 0]` | `[0, 0, 0, 0, 100000, 0, 0, 0, 0, 0]` |
| `pred_TTBar.root` | TTBar | label_Tbqq | 100000 | 0.91365 | 0.91365 | 0.91365 | `[1673, 1353, 1255, 988, 2569, 80, 275, 372, 91365, 70]` | `[0, 0, 0, 0, 0, 0, 0, 0, 100000, 0]` | `[0, 0, 0, 0, 0, 0, 0, 0, 100000, 0]` |
| `pred_TTBarLep.root` | TTBarLep | label_Tbl | 100000 | 0.95654 | 0.95654 | 0.95654 | `[162, 161, 37, 15, 14, 3776, 51, 36, 94, 95654]` | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 100000]` | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 100000]` |
| `pred_WToQQ.root` | WToQQ | label_Wqq | 100000 | 0.74142 | 0.74142 | 0.74142 | `[5811, 254, 742, 609, 1885, 374, 14279, 74142, 1872, 32]` | `[0, 0, 0, 0, 0, 0, 0, 100000, 0, 0]` | `[0, 0, 0, 0, 0, 0, 0, 100000, 0, 0]` |
| `pred_ZJetsToNuNu.root` | ZJetsToNuNu | label_QCD | 100000 | 0.72447 | 0.72447 | 0.72447 | `[72447, 1593, 2793, 6662, 2484, 99, 4495, 5469, 3828, 130]` | `[100000, 0, 0, 0, 0, 0, 0, 0, 0, 0]` | `[100000, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_ZToQQ.root` | ZToQQ | label_Zqq | 100000 | 0.60435 | 0.60435 | 0.60435 | `[5186, 2890, 2878, 1824, 2473, 357, 60435, 21990, 1907, 60]` | `[0, 0, 0, 0, 0, 0, 100000, 0, 0, 0]` | `[0, 0, 0, 0, 0, 0, 100000, 0, 0, 0]` |

## First output branches

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
