# Phase 3 Hqql/Tbl Isolation Controls v1

## 3C Isolation bins
| bin | n_hqql | n_hqql_to_tbl | confusion_rate | p0_lepton | missing_pt |
| --- | --- | --- | --- | --- | --- |
| 0.00-0.10 | 492 | 13 | 0.0264 | 0.5000 | 623.1096 |
| 0.10-0.15 | 1442 | 35 | 0.0243 | 0.5929 | 611.5750 |
| 0.15-0.20 | 1384 | 47 | 0.0340 | 0.7782 | 613.7278 |
| 0.20-0.30 | 663 | 48 | 0.0724 | 0.8748 | 626.5158 |
| 0.30+ | 43 | 11 | 0.2558 | 0.9535 | 655.0747 |

## 3A matched controls
| test | n | success | flip | delta_margin |
| --- | --- | --- | --- | --- |
| 3A_real_hqql_hadron | 150 | 0.6200 | 0.6667 | 1.9644 |
| 3A_control_qcd_hadron | 150 | 0.5333 | 0.8200 | 2.0360 |

## 3B hadron fraction sweep
| fraction | n | success | flip | delta_margin |
| --- | --- | --- | --- | --- |
| 0.0 | 150 | 0.0000 | 0.0000 | 0.0000 |
| 0.2 | 150 | 0.6533 | 0.6667 | 2.1165 |
| 0.4 | 150 | 0.6467 | 0.6733 | 2.1417 |
| 0.6 | 150 | 0.6067 | 0.6533 | 1.8051 |
| 0.8 | 150 | 0.6267 | 0.6733 | 1.8431 |
| 1.0 | 150 | 0.6200 | 0.6667 | 1.9644 |

## Interpretation

3C is the cleanest observable test. If confusion_rate increases with isolation, isolation is a real physical discriminator. 3A checks whether Hqql-specific hadronic context beats QCD-matched hadrons. 3B checks whether the effect has a monotonic density curve.
