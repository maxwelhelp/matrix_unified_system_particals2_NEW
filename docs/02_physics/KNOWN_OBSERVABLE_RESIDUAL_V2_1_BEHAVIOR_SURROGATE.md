# Known Observable Residual v2.1 — Hqql/Tbl behavior surrogate

V2 trained a true-label surrogate and showed that explicit isolation/leptonic-core features do not close the Hqql/Tbl mechanism.

Important V2 result:

```text
surrogate_v2_acc_correct_test = 0.6299
ParticleNet_acc_correct_test  = 1.0000
surrogate_agreement_on_confused = 0.5452
```

The surrogate reproduces the isolation trend direction but overpredicts Tbl in all isolation bins:

```text
low isolation: ParticleNet Hqql->Tbl = 0.0264, surrogate = 0.3476
high isolation: ParticleNet Hqql->Tbl = 0.2558, surrogate = 0.9070
```

Therefore isolation is a strong physical observable, but the mechanism is not fully decoded.

## v2.1 goal

Train a behavior surrogate for true Hqql events:

```text
input: explicit features from Phase 1
label: ParticleNet predicts Tbl or not
```

This asks a cleaner question:

```text
Can explicit isolation/core/KNN observables reproduce ParticleNet's Hqql->Tbl behavior?
```

It reports:

```text
AUC / accuracy / agreement
calibrated Hqql->Tbl rate by isolation bin
feature weights
residual bins where ParticleNet and surrogate disagree
```
