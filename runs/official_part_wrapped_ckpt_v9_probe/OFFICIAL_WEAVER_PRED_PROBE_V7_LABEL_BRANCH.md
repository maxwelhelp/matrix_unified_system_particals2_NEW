# Official Weaver prediction probe v7 label branch

pred_dir=/home/maxwelhelp/Рабочий стол/matrix_unified_system_particals/runs/official_part_wrapped_ckpt_v9_kinpid
n_files=10

## Accuracy by filename mapping

acc=0.101229 label_perm_upper_greedy=0.151608

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

## Accuracy by one-hot label_* branches

acc=0.101229 label_perm_upper_greedy=0.151608

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

## Accuracy by _label_ branch

acc=0.101229 label_perm_upper_greedy=0.151608

true_counts=`[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]`

| file | sample | file-label | entries | acc_file | acc_label_* | acc__label_ | pred_counts | _label_counts | label*_counts |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `pred_HToBB.root` | HToBB | label_Hbb | 100000 | 0.00279 | 0.00279 | 0.00279 | `[81008, 279, 998, 110, 1164, 81, 13138, 2668, 21, 533]` | `[0, 100000, 0, 0, 0, 0, 0, 0, 0, 0]` | `[0, 100000, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_HToCC.root` | HToCC | label_Hcc | 100000 | 0.00907 | 0.00907 | 0.00907 | `[76987, 292, 907, 63, 824, 20, 17137, 3632, 9, 129]` | `[0, 0, 100000, 0, 0, 0, 0, 0, 0, 0]` | `[0, 0, 100000, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_HToGG.root` | HToGG | label_Hgg | 100000 | 0.00011 | 0.00011 | 0.00011 | `[81302, 36, 2969, 11, 3882, 2, 11362, 395, 31, 10]` | `[0, 0, 0, 100000, 0, 0, 0, 0, 0, 0]` | `[0, 0, 0, 100000, 0, 0, 0, 0, 0, 0]` |
| `pred_HToWW2Q1L.root` | HToWW2Q1L | label_Hqql | 100000 | 0.00427 | 0.00427 | 0.00427 | `[40158, 3384, 8171, 258, 1024, 427, 44729, 1102, 52, 695]` | `[0, 0, 0, 0, 0, 100000, 0, 0, 0, 0]` | `[0, 0, 0, 0, 0, 100000, 0, 0, 0, 0]` |
| `pred_HToWW4Q.root` | HToWW4Q | label_H4q | 100000 | 0.0395 | 0.0395 | 0.0395 | `[82089, 37, 3062, 44, 3950, 1, 10329, 469, 7, 12]` | `[0, 0, 0, 0, 100000, 0, 0, 0, 0, 0]` | `[0, 0, 0, 0, 100000, 0, 0, 0, 0, 0]` |
| `pred_TTBar.root` | TTBar | label_Tbqq | 100000 | 1e-05 | 1e-05 | 1e-05 | `[98005, 11, 65, 6, 357, 4, 1117, 426, 1, 8]` | `[0, 0, 0, 0, 0, 0, 0, 0, 100000, 0]` | `[0, 0, 0, 0, 0, 0, 0, 0, 100000, 0]` |
| `pred_TTBarLep.root` | TTBarLep | label_Tbl | 100000 | 0.03248 | 0.03248 | 0.03248 | `[52040, 9528, 8886, 245, 250, 1839, 20360, 3555, 49, 3248]` | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 100000]` | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 100000]` |
| `pred_WToQQ.root` | WToQQ | label_Wqq | 100000 | 0.00421 | 0.00421 | 0.00421 | `[29815, 1172, 7615, 162, 509, 7, 60062, 421, 69, 168]` | `[0, 0, 0, 0, 0, 0, 0, 100000, 0, 0]` | `[0, 0, 0, 0, 0, 0, 0, 100000, 0, 0]` |
| `pred_ZJetsToNuNu.root` | ZJetsToNuNu | label_QCD | 100000 | 0.37526 | 0.37526 | 0.37526 | `[37526, 270, 3047, 260, 1486, 21, 55993, 800, 475, 122]` | `[100000, 0, 0, 0, 0, 0, 0, 0, 0, 0]` | `[100000, 0, 0, 0, 0, 0, 0, 0, 0, 0]` |
| `pred_ZToQQ.root` | ZToQQ | label_Zqq | 100000 | 0.54459 | 0.54459 | 0.54459 | `[37335, 731, 5424, 101, 552, 27, 54459, 893, 46, 432]` | `[0, 0, 0, 0, 0, 0, 100000, 0, 0, 0]` | `[0, 0, 0, 0, 0, 0, 100000, 0, 0, 0]` |

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
