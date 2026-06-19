# Known Observable Residual v1

This report asks whether ParticleNet logits are mostly explainable by simple known observables, or whether a residual model signal remains.

n_events=2560 train=1792 test=768 status=RESIDUAL_SIGNAL_REMAINS

## Summary
| metric | value |
| --- | --- |
| model_acc_test | 0.7708 |
| known_observable_surrogate_acc | 0.3815 |
| known_observable_agreement_with_model | 0.4102 |
| observable_label_acc | 0.4128 |
| logit_r2_mean | 0.5676 |
| logit_r2_min | 0.3019 |
| residual_rel_mean | 0.3845 |
| n_features | 57 |

## Per-class surrogate/residual
| class | n | model_acc | surrogate_acc | agreement | logit_r2 | residual_norm |
| --- | --- | --- | --- | --- | --- | --- |
| label_QCD | 85 | 0.6588 | 0.4353 | 0.5529 | 0.6922 | 8.2601 |
| label_Hbb | 70 | 0.6571 | 0.2714 | 0.3429 | 0.5239 | 9.0267 |
| label_Hcc | 69 | 0.6812 | 0.4348 | 0.4928 | 0.5424 | 7.9392 |
| label_Hgg | 83 | 0.6627 | 0.6265 | 0.5301 | 0.6940 | 6.0044 |
| label_H4q | 84 | 0.7857 | 0.0119 | 0.0952 | 0.5321 | 7.0216 |
| label_Hqql | 67 | 0.9851 | 0.4030 | 0.4030 | 0.3019 | 12.7107 |
| label_Zqq | 77 | 0.5844 | 0.4156 | 0.3766 | 0.5523 | 6.7982 |
| label_Wqq | 69 | 0.7971 | 0.1159 | 0.2174 | 0.5165 | 6.7924 |
| label_Tbqq | 80 | 0.9125 | 0.4750 | 0.4625 | 0.6849 | 8.5394 |
| label_Tbl | 84 | 0.9881 | 0.5833 | 0.5952 | 0.6357 | 15.0818 |

## Top known-observable coefficients
| rank | feature | coef_norm |
| --- | --- | --- |
| 1 | feat4_ptw | 123.3347 |
| 2 | pt_weighted_deltaR | 62.0109 |
| 3 | pt_weighted_dR1 | 62.0109 |
| 4 | log_jet_energy | 28.5204 |
| 5 | feat1_ptw | 27.4110 |
| 6 | feat3_ptw | 26.1671 |
| 7 | feat2_ptw | 22.4453 |
| 8 | feat1_mean | 22.3517 |
| 9 | feat0_ptw | 18.9321 |
| 10 | feat3_mean | 17.2607 |
| 11 | mean_deltaR | 13.0874 |
| 12 | feat4_mean | 12.9449 |
| 13 | pt_weighted_dR2 | 12.0782 |
| 14 | lead_pt_frac | 9.3803 |
| 15 | lead_e_frac | 8.2212 |
| 16 | log_jet_mass | 7.2121 |
| 17 | pt2_concentration | 6.2155 |
| 18 | log_nparticles | 5.7955 |
| 19 | pt_weighted_dR3 | 5.1827 |
| 20 | log_jet_pt | 4.9100 |
| 21 | feat0_mean | 4.6300 |
| 22 | feat2_mean | 4.4940 |
| 23 | top16_pt_frac | 3.0718 |
| 24 | top8_pt_frac | 2.8837 |
| 25 | charge_abs_sum | 2.6287 |
| 26 | top4_pt_frac | 2.4639 |
| 27 | pid_pt_frac_electron | 2.3542 |
| 28 | feat9_ptw | 2.3542 |
| 29 | feat10_ptw | 2.3353 |
| 30 | pid_pt_frac_muon | 2.3353 |

## Top residual events
| rank | event | true | model_pred | surrogate_pred | residual_norm | residual_rel |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1410 | label_Tbl | label_Tbl | label_Tbl | 80.5424 | 0.6635 |
| 2 | 1494 | label_Tbl | label_Tbl | label_Hqql | 51.3550 | 0.6583 |
| 3 | 1316 | label_Tbl | label_Tbl | label_Hqql | 40.4979 | 0.5551 |
| 4 | 996 | label_Hqql | label_Hqql | label_Tbl | 38.6770 | 0.7740 |
| 5 | 1338 | label_Tbl | label_Tbl | label_Tbl | 38.3642 | 0.5381 |
| 6 | 1391 | label_Tbl | label_Tbl | label_Hqql | 34.5709 | 0.5131 |
| 7 | 1426 | label_Tbl | label_Tbl | label_Tbl | 34.0842 | 0.4806 |
| 8 | 1423 | label_Tbl | label_Tbl | label_Tbl | 33.0620 | 0.4381 |
| 9 | 873 | label_Hqql | label_Hqql | label_Tbl | 29.8975 | 0.9058 |
| 10 | 850 | label_Hqql | label_Hqql | label_Tbl | 29.2385 | 0.9781 |
| 11 | 1346 | label_Tbl | label_Tbl | label_Tbl | 29.2247 | 0.4401 |
| 12 | 1322 | label_Tbl | label_Tbl | label_Hqql | 27.6508 | 0.4579 |
| 13 | 1505 | label_Tbl | label_Tbl | label_Tbl | 26.2348 | 1.1674 |
| 14 | 1323 | label_Tbl | label_Tbl | label_Tbl | 26.2241 | 0.4395 |
| 15 | 920 | label_Hqql | label_Hqql | label_Tbl | 25.8093 | 1.0722 |
| 16 | 1307 | label_Tbl | label_Tbl | label_Hqql | 25.0628 | 0.4884 |
| 17 | 170 | label_Hbb | label_Hbb | label_Tbl | 25.0480 | 0.5154 |
| 18 | 1425 | label_Tbl | label_Tbl | label_Hgg | 23.9663 | 0.6596 |
| 19 | 201 | label_Hbb | label_Hbb | label_QCD | 22.1572 | 0.5611 |
| 20 | 494 | label_Hcc | label_Hcc | label_Hqql | 21.5708 | 1.4551 |
| 21 | 1944 | label_Wqq | label_QCD | label_Zqq | 21.4281 | 0.6152 |
| 22 | 1522 | label_Tbl | label_Tbl | label_Tbl | 21.3368 | 0.4608 |
| 23 | 2157 | label_QCD | label_Tbqq | label_Tbqq | 21.1214 | 0.5955 |
| 24 | 1465 | label_Tbl | label_Tbl | label_Hbb | 20.9514 | 0.5590 |
| 25 | 2070 | label_QCD | label_QCD | label_QCD | 20.6433 | 0.5635 |

## Interpretation

- If agreement/R2 are high, the particle0/top-k mechanism may mostly be a known-observable proxy.
- If residual remains high, the model contains signal not captured by this simple observable set.
- This v1 is a first-pass linear/ridge surrogate, not final physics proof. Next steps: richer ECF/EFP-like features and heldout/per-file stability.
