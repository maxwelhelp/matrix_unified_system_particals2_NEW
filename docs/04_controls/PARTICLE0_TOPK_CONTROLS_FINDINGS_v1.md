# Particle0 / Top-k Controls Findings v1

This document records the interpretation of the first successful KNN-safe particle0/top-k control run.

## Run state

```text
model: ParticleNet_kinpid.pt
mode: kinpid
n_events: 2560
baseline_acc: 0.7574
```

## Main global result

### Remove particle0

```text
remove_particle0 acc: 0.5633
acc_drop: 0.1941
flip_rate: 0.3160
delta_base_pred_logit: -3.5645
```

Random same-count baseline:

```text
random_remove1 acc_drop_mean: 0.0146
random_remove1 flip_mean: 0.0624
random_remove1 delta_logit_mean: -0.2061
```

Interpretation:

```text
particle0 is specifically causal, not just one random particle.
```

Approx ratios:

```text
acc_drop(remove_particle0) / acc_drop(random_remove1) ~= 13.3x
flip(remove_particle0) / flip(random_remove1) ~= 5.1x
logit_drop(remove_particle0) / logit_drop(random_remove1) ~= 17.3x
```

## Important non-shortcut result

### Keep only particle0

```text
keep_only_particle0 acc: 0.2027
acc_drop: 0.5547
flip_rate: 0.7941
delta_base_pred_logit: -26.5106
```

Interpretation:

```text
particle0 alone is not enough for the full model.
```

So the current best interpretation is **not**:

```text
model only uses particle0 shortcut
```

Better interpretation:

```text
leading/core particle is a necessary anchor,
but the model also needs secondary/top-k context.
```

## Top-k curve

```text
remove_top1  acc_drop 0.1941
remove_top2  acc_drop 0.3008
remove_top4  acc_drop 0.4082
remove_top8  acc_drop 0.4883
remove_top16 acc_drop 0.5594
```

Random baselines:

```text
random_remove1  acc_drop 0.0146
random_remove2  acc_drop 0.0340
random_remove4  acc_drop 0.0732
random_remove8  acc_drop 0.1724
random_remove16 acc_drop 0.3746
```

Interpretation:

```text
top-k removal is consistently more destructive than random same-count removal.
```

The ratio shrinks as k grows because random removal of 16 particles is already destructive.

## Keep top-k curve

```text
keep_top1  acc 0.2027
keep_top2  acc 0.2430
keep_top4  acc 0.2922
keep_top8  acc 0.3773
keep_top16 acc 0.5391
```

Interpretation:

```text
top-16 particles retain substantial information,
but not all information.
```

This supports:

```text
core/top-k carries much class evidence,
but full event context still matters.
```

## Class-specific result

Classes most damaged by removing particle0:

```text
Tbl:  acc 0.9688 -> 0.2031, drop 0.7656
Hqql: acc 0.9570 -> 0.2813, drop 0.6758
Hcc:  acc 0.5820 -> 0.4141, drop 0.1680
Zqq:  acc 0.6094 -> 0.4453, drop 0.1641
```

Classes barely harmed or even improved:

```text
Hgg:  acc 0.6914 -> 0.6953, drop -0.0039
H4q:  acc 0.7813 -> 0.8047, drop -0.0234
QCD:  acc 0.6992 -> 0.6719, drop 0.0273
Tbqq: acc 0.9063 -> 0.8828, drop 0.0234
```

Interpretation:

```text
particle0/core anchor is highly class-specific.
It is especially important for Hqql and Tbl.
```

## Key class examples

### Hqql

```text
baseline acc: 0.9570
remove_particle0 acc: 0.2813
keep_top8 acc: 0.9219
keep_top16 acc: 0.9570
```

Interpretation:

```text
Hqql is mostly encoded in the top-k core set.
Top-8 is almost enough; top-16 fully recovers baseline accuracy.
```

### Tbl

```text
baseline acc: 0.9688
remove_particle0 acc: 0.2031
keep_top1 acc: 0.8711
keep_top2 acc: 0.5273
keep_top4 acc: 0.3789
keep_top8 acc: 0.5352
keep_top16 acc: 0.8320
```

Interpretation:

```text
Tbl is extremely particle0-sensitive,
but the keep-top-k curve is non-monotonic enough that we should inspect confusion / routing.
```

Possible explanation:

```text
particle0 alone creates a strong Tbl shortcut,
but adding only a few core particles changes class competition;
fuller top-16 context partially restores it.
```

## Updated hypothesis status

### AH1 — distributed core-anchor + secondary-context mechanism

Status update:

```text
from OBSERVED_NEEDS_CONTROL
to SUPPORTED_BY_TARGETED_REMOVAL_BUT_NEEDS_ORDER_RESIDUAL_TEST
```

Reason:

```text
remove_particle0 is much worse than random_remove1,
so particle0/core is causally important.
```

Remaining risks:

```text
particle ordering / sorting shortcut
known observable proxy: pt/mass/tau/nparticles
class-specific bias Hqql/Tbl
```

### AH2 — Hqql/Tbl high-confidence head-system signature

Status update:

```text
SUPPORTED_BY_CONTROL
```

Reason:

```text
Hqql/Tbl collapse hardest under particle0 removal.
```

### Shortcut-only hypothesis

Status:

```text
REJECT_AS_GLOBAL_EXPLANATION
```

Reason:

```text
keep_only_particle0 global acc is only 0.2027.
```

But:

```text
Tbl has strong keep_top1 accuracy 0.8711,
so a class-local shortcut remains possible for Tbl.
```

## Next required tests

### P0. Particle order / sorting control

Question:

```text
Is particle0 important because of physical leading-pT information or because of index/order?
```

Run:

```text
particle order shuffle
sort by alternative order
coordinate/feature-only comparison
```

### P0. Known-observable residual

Question:

```text
Is particle0/top-k evidence already explained by known jet observables?
```

Compare against:

```text
jet mass
jet pT
nparticles
tau21/tau32
energy correlators / EFPs
charge/PID summaries
```

### P0. Class-specific gradients

Question:

```text
Which heads carry Hqql and Tbl core-anchor dependence?
```

Run:

```text
class-specific all-head gradients for Hqql, Tbl, Zqq, Wqq, Hbb/Hcc/Hgg
```

### P1. Confusion analysis under controls

Question:

```text
When Hqql/Tbl collapse, where do predictions go?
```

Need:

```text
control confusion matrices
class transition table: baseline_pred -> control_pred
```

## Short conclusion

The result is strong and useful:

```text
The model does not merely have an attribution artifact.
The leading/core particle is causally important, especially for Hqql/Tbl.
But particle0 alone is not enough globally, so the mechanism is core-anchor + context, not pure particle0-only shortcut.
```

This is now a stronger mechanistic hypothesis, but not yet a physics-discovery claim.
