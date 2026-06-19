# Feature Ranker V1

Second component after `CONFUSION_MONITOR_V1`.

## Goal

For each WATCH/ALERT class pair from `signal_board_v1.csv`, automatically answer:

```text
What explicit event features distinguish A_correct from A_to_B?
```

## Input

```text
reports/latest/tables/signal_board_v1.csv
model checkpoint
data directory
```

## Groups for A->B

```text
A_correct = true A, pred A
A_to_B    = true A, pred B
B_correct = true B, pred B
B_to_A    = true B, pred A
```

## Feature families V1

```text
basic counts / missing-pT / confidence
particle0/core PID, pT, isolation
leading particle PID, pT, isolation
KNN PID fractions around particle0
KNN pT sums around particle0
best lepton presence/isolation
core-lepton alignment proxy
```

## Scores

```text
contrastive effect = standardized difference between A_correct and A_to_B
monotonic ratio = max_bin_rate / min_bin_rate for A->B over feature bins
rank_score = abs(effect) * monotonic_ratio * log1p(n_A_to_B)
```

## Output

```text
reports/latest/FEATURE_RANKER_V1.md
reports/latest/tables/feature_ranker_v1_candidates.csv
reports/latest/tables/feature_ranker_v1_bins.csv
reports/latest/tables/signal_board_v1_feature_candidates.csv
manifests/latest/feature_ranker_v1.json
```

## Next

Only candidates with strong score should go to Deep Probe / patch / residual.
