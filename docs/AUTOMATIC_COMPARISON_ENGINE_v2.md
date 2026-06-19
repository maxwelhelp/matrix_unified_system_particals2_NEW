# Automatic Comparison Engine v2

v1 automated the first useful human comparisons:

```text
particle0/core relation vs missing controls
wide context vs route-neighbor trace
patch evidence vs all-head gradient
head stability vs heldout need
class signature vs class-specific gradients
negative gates vs suppressive-head interpretation
```

v2 adds the comparisons needed before running a much larger stream.

## New comparisons added in v2

### C7 — Sample-size scaling

Human reasoning:

```text
A signal that appears at 640 events but disappears at 2560+ events is probably unstable.
A signal that keeps rank/shape across larger samples is more meaningful.
```

Automatic comparison:

```text
signal/rank/history vs n_events / SAMPLES_PER_FILE
```

Output:

```text
scales_with_data / unstable_with_scale / needs_more_large_runs
```

---

### C8 — Class concentration vs class imbalance

Human reasoning:

```text
If Hqql/Tbl dominate the stream, this can be real class signature or sampling/class imbalance.
```

Automatic comparison:

```text
class particle signal vs class counts / balanced-vs-natural setup
```

Output:

```text
class signature needs class-balanced and natural-distribution comparison
```

---

### C9 — Correct-vs-wrong split

Human reasoning:

```text
A useful mechanism should be compared on correct predictions and errors.
On errors, heads may answer the predicted class instead of the true class.
```

Automatic comparison:

```text
head/particle signal in correct examples vs misclassified examples
```

Output:

```text
needs error atlas / false-class route analysis
```

---

### C10 — Known-observable residual

Human reasoning:

```text
For physics discovery, a signal is interesting only if it survives after known observables:
mass, pt, tau variables, nparticles, charge/PID proxies.
```

Automatic comparison:

```text
head/particle/hypothesis signal vs residual after known observables
```

Output:

```text
residual_candidate / shortcut_explained_by_known_observables / missing_residual_test
```

---

### C11 — Head-pair synergy

Human reasoning:

```text
The network can use multiple heads together. Single-head patch and gradient do not reveal synergy.
```

Automatic comparison:

```text
single-head effect + single-head effect vs pair patch effect
```

Output:

```text
additive / synergistic / redundant / compensating
```

---

### C12 — Cross-model / checkpoint agreement

Human reasoning:

```text
If ParticleNet_kinpid and ParT_kinpid find the same pattern, it is more likely to be physics-like.
If only one checkpoint finds it, it may be architecture-specific.
```

Automatic comparison:

```text
hypothesis signal across models: ParticleNet_kin, ParticleNet_kinpid, ParT_kinpid, ParT_full
```

Output:

```text
cross_model_supported / architecture_specific / needs_cross_model_test
```

---

### C13 — Per-file / heldout stability

Human reasoning:

```text
A relation should survive across different ROOT files and tar parts.
```

Automatic comparison:

```text
relation/head/class signal per ROOT file / per tar part / heldout files
```

Output:

```text
heldout_stable / file_specific / needs_heldout
```

---

### C14 — Ordering-vs-physics coordinate check

Human reasoning:

```text
particle0 dominance can be sorting/order, not physics.
Need order shuffle or coordinate-based controls.
```

Automatic comparison:

```text
particle index signal vs pt/deltaR/feature signal vs shuffled order control
```

Output:

```text
order_shortcut_candidate / physical_coordinate_candidate / needs_shuffle_control
```

---

### C15 — Discovery readiness score

Human reasoning:

```text
A hypothesis becomes discovery-relevant only after it survives controls, heldout, residual, and cross-model checks.
```

Automatic comparison:

```text
controls_passed + heldout + residual + cross-model + causal evidence
```

Output:

```text
method_debug / known_physics / residual_candidate / anomaly_candidate / discovery_candidate
```

---

### C16 — Big-stream readiness

Human reasoning:

```text
Before running much larger data, the stream must know what to save, what to drop, and what to summarize.
```

Automatic comparison:

```text
current stream rows/size/missing tests vs planned larger run
```

Output:

```text
ready_for_large_stream / needs_controls_first / run_sampled_large_stream
```

## Why v2 matters

v2 is the first step toward an automatic analyst that behaves like a careful scientist:

```text
signal -> alternative explanation -> missing control -> next experiment -> training row
```

It should not say “discovery” from correlation. It should rank which comparisons are mature enough to run at larger scale.
