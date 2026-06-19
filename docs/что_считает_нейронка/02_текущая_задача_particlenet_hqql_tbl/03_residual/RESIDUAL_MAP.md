# Residual / surrogate map

## Residual V2 — true-label surrogate

File:

```text
reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2.md
```

Question:

```text
Can explicit isolation/KNN/missing-pT features classify true Hqql vs true Tbl like ParticleNet?
```

Result:

```text
surrogate_v2_acc_correct_test = 0.6299
ParticleNet_acc_correct_test = 1.0000
surrogate_agreement_with_ParticleNet_on_confused = 0.5452
```

Interpretation:

```text
V2 confirms the direction but does not close the mechanism.
It overpredicts Tbl in all isolation bins.
```

## Residual V2.1 — behavior surrogate

File:

```text
reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2_1_BEHAVIOR.md
```

Question:

```text
Can explicit observables predict ParticleNet behavior on true Hqql events: Hqql->Tbl or not?
```

Result:

```text
n_hqql = 4024
ParticleNet Hqql->Tbl rate test = 0.0364
behavior_surrogate_acc_test = 0.9296
behavior_surrogate_auc_test = 0.5908
```

Interpretation:

```text
Accuracy is high because of imbalance.
AUC=0.5908 means explicit isolation/KNN/missing-pT features are useful but incomplete.
The surrogate captures high-isolation risk but overpredicts the highest bin.
```

## Next residual V3

Needed features:

```text
lepton + b-like candidate angular separation
pairwise charged/neutral geometry
subjet / prong geometry
ECF-like 2-point and 3-point features
tau-like proxies
top-k pair geometry
```

Goal:

```text
Decide whether the remaining residual is b-like/pairwise/subjet geometry or something else.
```
