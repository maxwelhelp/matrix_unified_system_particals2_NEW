# Feature Ranker v1

Automatic contrastive feature ranking for WATCH/ALERT class pairs. No LLM is used.

- input signals: **12**
- candidates: **420**

## Top feature candidates
| pair | feature | score | effect | mono_ratio | direction | n_confused |
| --- | --- | --- | --- | --- | --- | --- |
| label_Hcc->label_Hgg | n_particles | 407.1924 | 1.8377 | 50.0093 | confused_higher | 83 |
| label_Hbb->label_Hgg | n_particles | 310.9361 | 1.3544 | 51.1455 | confused_higher | 88 |
| label_QCD->label_Hgg | pred_conf | 187.3780 | -1.5728 | 28.1373 | correct_higher | 68 |
| label_Hbb->label_Hgg | p0_best_lepton_deltaR | 167.6742 | 1.0718 | 34.8543 | confused_higher | 88 |
| label_H4q->label_Hgg | n_particles | 166.3842 | 1.2492 | 28.9855 | confused_higher | 98 |
| label_Hcc->label_H4q | n_particles | 108.4942 | 1.3454 | 18.4023 | confused_higher | 79 |
| label_Hcc->label_Hgg | pred_conf | 99.9430 | -1.1814 | 19.0931 | correct_higher | 83 |
| label_Wqq->label_Zqq | pred_conf | 76.7596 | -1.0150 | 15.0735 | correct_higher | 150 |
| label_Hbb->label_Hgg | leading_pt_fraction | 69.3179 | -0.7684 | 20.0980 | correct_higher | 88 |
| label_Hbb->label_Hgg | best_lepton_pt | 68.0163 | -0.8763 | 17.2922 | correct_higher | 88 |
| label_Hcc->label_Hgg | knn_pt_mean | 58.9352 | -1.0732 | 12.3938 | correct_higher | 83 |
| label_Hcc->label_Hgg | knn_pt_sum | 58.6218 | -1.0675 | 12.3938 | correct_higher | 83 |
| label_QCD->label_Hgg | leading_pt_fraction | 52.4809 | -1.0279 | 12.0588 | correct_higher | 68 |
| label_H4q->label_Hgg | pred_conf | 48.7019 | -1.3184 | 8.0392 | correct_higher | 98 |
| label_Hbb->label_Hgg | best_lepton_iso_pt_ratio | 45.3038 | -1.1673 | 8.6461 | correct_higher | 88 |
| label_Hcc->label_Hgg | p0_iso_pt_ratio | 40.2960 | 0.6528 | 13.9317 | confused_higher | 83 |
| label_QCD->label_Hgg | p0_iso_pt_ratio | 37.8650 | 0.8425 | 10.6146 | confused_higher | 68 |
| label_QCD->label_Hgg | p0_pt | 36.7514 | -0.9092 | 9.5466 | correct_higher | 68 |
| label_QCD->label_Hgg | leading_pt | 36.7514 | -0.9092 | 9.5466 | correct_higher | 68 |
| label_QCD->label_Hgg | knn_pt_max | 36.7514 | -0.9092 | 9.5466 | correct_higher | 68 |
| label_Hcc->label_Zqq | pred_conf | 34.6708 | -1.0376 | 8.5417 | correct_higher | 49 |
| label_Hcc->label_H4q | pred_conf | 32.5776 | -0.9546 | 7.7880 | correct_higher | 79 |
| label_Hgg->label_Hbb | pred_conf | 31.1755 | -1.0291 | 7.3693 | correct_higher | 60 |
| label_Hbb->label_Hgg | knn_pt_mean | 30.1382 | -0.7033 | 9.5466 | correct_higher | 88 |
| label_QCD->label_Hgg | n_particles | 28.6847 | 1.9174 | 3.5333 | confused_higher | 68 |
| label_QCD->label_Hgg | knn_pt_mean | 28.6086 | -1.2068 | 5.5987 | correct_higher | 68 |
| label_Hcc->label_H4q | knn_pt_mean | 28.2273 | -0.9157 | 7.0343 | correct_higher | 79 |
| label_Hcc->label_H4q | knn_pt_sum | 28.0278 | -0.9137 | 7.0000 | correct_higher | 79 |
| label_QCD->label_Hgg | knn_pt_sum | 26.9351 | -1.1976 | 5.3116 | correct_higher | 68 |
| label_Hbb->label_Hgg | knn_pt_sum | 26.4814 | -0.6907 | 8.5417 | correct_higher | 88 |
| label_Hbb->label_Hgg | has_lepton | 25.7256 | -1.0717 | 5.3477 | correct_higher | 88 |
| label_Hbb->label_Hgg | p0_pt | 25.2200 | -0.6777 | 8.2904 | correct_higher | 88 |
| label_Hbb->label_Hgg | leading_pt | 25.2200 | -0.6777 | 8.2904 | correct_higher | 88 |
| label_Hbb->label_Hgg | knn_pt_max | 25.2200 | -0.6777 | 8.2904 | correct_higher | 88 |
| label_Hbb->label_Hcc | pred_conf | 24.2876 | -1.2176 | 4.1110 | correct_higher | 127 |
| label_Hcc->label_Hgg | best_lepton_pt | 23.5160 | -0.5235 | 10.1374 | correct_higher | 83 |
| label_Hbb->label_Hgg | p0_lepton_aligned | 23.0668 | -0.7380 | 6.9636 | correct_higher | 88 |
| label_Hgg->label_Hbb | n_particles | 19.2568 | -0.7927 | 5.9097 | correct_higher | 60 |
| label_Hbb->label_Hgg | pred_conf | 17.5259 | -1.1774 | 3.3162 | correct_higher | 88 |
| label_Hcc->label_Hgg | leading_pt_fraction | 16.5426 | -0.6556 | 5.6944 | correct_higher | 83 |

## Signal board candidates
| pair | feature | score | reason | next |
| --- | --- | --- | --- | --- |
| label_Hcc->label_Hgg | n_particles | 407.1924 | feature=n_particles, effect=1.838, monotonic_ratio=50.009 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_Hgg | pred_conf | 99.9430 | feature=pred_conf, effect=-1.181, monotonic_ratio=19.093 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_Hgg | knn_pt_mean | 58.9352 | feature=knn_pt_mean, effect=-1.073, monotonic_ratio=12.394 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_Hgg | knn_pt_sum | 58.6218 | feature=knn_pt_sum, effect=-1.068, monotonic_ratio=12.394 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_Hgg | p0_iso_pt_ratio | 40.2960 | feature=p0_iso_pt_ratio, effect=0.653, monotonic_ratio=13.932 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_Hgg | best_lepton_pt | 23.5160 | feature=best_lepton_pt, effect=-0.524, monotonic_ratio=10.137 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_Hgg | leading_pt_fraction | 16.5426 | feature=leading_pt_fraction, effect=-0.656, monotonic_ratio=5.694 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_Hgg | best_lepton_iso_pt_ratio | 11.9798 | feature=best_lepton_iso_pt_ratio, effect=-0.547, monotonic_ratio=4.944 | run deep probe / patch if physics meaning is plausible |
| label_Hbb->label_Hgg | n_particles | 310.9361 | feature=n_particles, effect=1.354, monotonic_ratio=51.145 | run deep probe / patch if physics meaning is plausible |
| label_Hbb->label_Hgg | p0_best_lepton_deltaR | 167.6742 | feature=p0_best_lepton_deltaR, effect=1.072, monotonic_ratio=34.854 | run deep probe / patch if physics meaning is plausible |
| label_Hbb->label_Hgg | leading_pt_fraction | 69.3179 | feature=leading_pt_fraction, effect=-0.768, monotonic_ratio=20.098 | run deep probe / patch if physics meaning is plausible |
| label_Hbb->label_Hgg | best_lepton_pt | 68.0163 | feature=best_lepton_pt, effect=-0.876, monotonic_ratio=17.292 | run deep probe / patch if physics meaning is plausible |
| label_Hbb->label_Hgg | best_lepton_iso_pt_ratio | 45.3038 | feature=best_lepton_iso_pt_ratio, effect=-1.167, monotonic_ratio=8.646 | run deep probe / patch if physics meaning is plausible |
| label_Hbb->label_Hgg | knn_pt_mean | 30.1382 | feature=knn_pt_mean, effect=-0.703, monotonic_ratio=9.547 | run deep probe / patch if physics meaning is plausible |
| label_Hbb->label_Hgg | knn_pt_sum | 26.4814 | feature=knn_pt_sum, effect=-0.691, monotonic_ratio=8.542 | run deep probe / patch if physics meaning is plausible |
| label_Hbb->label_Hgg | has_lepton | 25.7256 | feature=has_lepton, effect=-1.072, monotonic_ratio=5.348 | run deep probe / patch if physics meaning is plausible |
| label_QCD->label_Hgg | pred_conf | 187.3780 | feature=pred_conf, effect=-1.573, monotonic_ratio=28.137 | run deep probe / patch if physics meaning is plausible |
| label_QCD->label_Hgg | leading_pt_fraction | 52.4809 | feature=leading_pt_fraction, effect=-1.028, monotonic_ratio=12.059 | run deep probe / patch if physics meaning is plausible |
| label_QCD->label_Hgg | p0_iso_pt_ratio | 37.8650 | feature=p0_iso_pt_ratio, effect=0.843, monotonic_ratio=10.615 | run deep probe / patch if physics meaning is plausible |
| label_QCD->label_Hgg | p0_pt | 36.7514 | feature=p0_pt, effect=-0.909, monotonic_ratio=9.547 | run deep probe / patch if physics meaning is plausible |
| label_QCD->label_Hgg | leading_pt | 36.7514 | feature=leading_pt, effect=-0.909, monotonic_ratio=9.547 | run deep probe / patch if physics meaning is plausible |
| label_QCD->label_Hgg | knn_pt_max | 36.7514 | feature=knn_pt_max, effect=-0.909, monotonic_ratio=9.547 | run deep probe / patch if physics meaning is plausible |
| label_QCD->label_Hgg | n_particles | 28.6847 | feature=n_particles, effect=1.917, monotonic_ratio=3.533 | run deep probe / patch if physics meaning is plausible |
| label_QCD->label_Hgg | knn_pt_mean | 28.6086 | feature=knn_pt_mean, effect=-1.207, monotonic_ratio=5.599 | run deep probe / patch if physics meaning is plausible |
| label_H4q->label_Hgg | n_particles | 166.3842 | feature=n_particles, effect=1.249, monotonic_ratio=28.986 | run deep probe / patch if physics meaning is plausible |
| label_H4q->label_Hgg | pred_conf | 48.7019 | feature=pred_conf, effect=-1.318, monotonic_ratio=8.039 | run deep probe / patch if physics meaning is plausible |
| label_H4q->label_Hgg | knn_pt_mean | 12.7226 | feature=knn_pt_mean, effect=-0.603, monotonic_ratio=4.594 | run deep probe / patch if physics meaning is plausible |
| label_H4q->label_Hgg | knn_pt_sum | 11.6749 | feature=knn_pt_sum, effect=-0.574, monotonic_ratio=4.429 | run deep probe / patch if physics meaning is plausible |
| label_H4q->label_Hgg | leading_pt_fraction | 11.6740 | feature=leading_pt_fraction, effect=-0.484, monotonic_ratio=5.248 | run deep probe / patch if physics meaning is plausible |
| label_H4q->label_Hgg | p0_pt | 8.7788 | feature=p0_pt, effect=-0.428, monotonic_ratio=4.466 | run deep probe / patch if physics meaning is plausible |
| label_H4q->label_Hgg | leading_pt | 8.7788 | feature=leading_pt, effect=-0.428, monotonic_ratio=4.466 | run deep probe / patch if physics meaning is plausible |
| label_H4q->label_Hgg | knn_pt_max | 8.7788 | feature=knn_pt_max, effect=-0.428, monotonic_ratio=4.466 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_H4q | n_particles | 108.4942 | feature=n_particles, effect=1.345, monotonic_ratio=18.402 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_H4q | pred_conf | 32.5776 | feature=pred_conf, effect=-0.955, monotonic_ratio=7.788 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_H4q | knn_pt_mean | 28.2273 | feature=knn_pt_mean, effect=-0.916, monotonic_ratio=7.034 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_H4q | knn_pt_sum | 28.0278 | feature=knn_pt_sum, effect=-0.914, monotonic_ratio=7.000 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_H4q | p0_iso_pt_ratio | 8.6957 | feature=p0_iso_pt_ratio, effect=0.537, monotonic_ratio=3.696 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_H4q | p0_pt | 8.3504 | feature=p0_pt, effect=-0.531, monotonic_ratio=3.589 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_H4q | leading_pt | 8.3504 | feature=leading_pt, effect=-0.531, monotonic_ratio=3.589 | run deep probe / patch if physics meaning is plausible |
| label_Hcc->label_H4q | knn_pt_max | 8.3504 | feature=knn_pt_max, effect=-0.531, monotonic_ratio=3.589 | run deep probe / patch if physics meaning is plausible |

## Interpretation

Top rows are observable candidates. They are not physics claims yet. The next stage should run only for candidates that have plausible semantics and enough counts.
