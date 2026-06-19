# Residual Status Brief v1

## Result

Known-observable residual v1 completed.

```text
status = RESIDUAL_SIGNAL_REMAINS
model_acc_test = 0.7708
known_observable_surrogate_acc = 0.3815
known_observable_agreement_with_model = 0.4102
logit_r2_mean = 0.5676
residual_rel_mean = 0.3845
```

## Interpretation

Simple known observables explain part of the model logits, but not enough to reproduce the model decisions.

Current status:

```text
core/top-k signal is causal,
order-index artifact is reduced,
simple known-observable-only explanation is not enough.
```

## Weak classes for the surrogate

```text
H4q, Wqq, Hqql, Tbl
```

## Next

```text
1. class-specific all-head gradients
2. richer residual v2 with pair/ECF-like features
3. per-file heldout stability
4. cross-model agreement
```
