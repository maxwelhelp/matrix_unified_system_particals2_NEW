# CLASS_PAIR_PHYSICS_PLAYBOOK_V1

This document explains what to do after `CONFUSION_MONITOR_V1` finds a new strong class-pair signal.

It turns a raw stream alert into the same reasoning framework that worked for Hqql/Tbl.

---

## Why this matters

The stream monitor proved the pipeline works:

```text
Old manual path:
  Hqql/Tbl was selected by hand and took a long manual loop.

Stream path:
  one run surfaced stronger signals automatically:
    Zqq -> Wqq  rate ~= 0.21
    Wqq -> Zqq  rate ~= 0.14
    Hbb <-> Hcc rate ~= 0.11
    Hgg -> H4q rate ~= 0.10
```

Therefore the goal is not to manually inspect every pair. The goal is:

```text
confusion monitor -> feature ranker -> only top candidates -> deep probe
```

---

## Standard class-pair loop

For every `A -> B` signal:

```text
1. State the physical/logical question.
2. Build groups:
   A_correct = true A, pred A
   A_to_B    = true A, pred B
   B_correct = true B, pred B
   B_to_A    = true B, pred A
3. Run Feature Ranker.
4. Look at monotonic_ratio and contrastive effect.
5. Pick top feature with plausible physical meaning.
6. Run Deep Probe only for that feature.
7. If surrogate overpredicts or underpredicts, run VETO/TRIGGER search.
```

---

## Feature Ranker decision thresholds

The first number to check is:

```text
monotonic_ratio = max_bin_confusion_rate / min_bin_confusion_rate
```

Interpretation:

```text
> 5x  -> strong observable candidate, like Hqql/Tbl isolation ~= 9.7x
> 3x  -> medium signal, worth probing if physically meaningful
< 2x  -> usually noise or weak effect, skip unless counts are huge
```

Also require:

```text
enough events in bins
stable direction across files/subsamples if possible
feature has physical/logical semantics
```

---

## Deep Probe rule

Deep Probe is expensive. Do not run it for everything.

Run it only when:

```text
class pair is WATCH/ALERT
feature has high monotonic_ratio
contrastive effect is nontrivial
feature has plausible physical meaning
```

Deep Probe should include:

```text
bin scan
single-feature or small-feature surrogate
targeted patch
random_same_count control
same-pid/same-pt control when applicable
residual inversion if surrogate fails
```

---

## Example 1 — Zqq <-> Wqq

### Monitor signal

```text
Zqq -> Wqq is the strongest current signal.
Wqq -> Zqq is also strong.
```

### Physical question

```text
Z -> qq and W -> qq are both two-prong hadronic decays.
The key difference is charge/isospin/flavor composition, not leptons.
```

### First hypothesis before Feature Ranker

```text
The network confuses Zqq and Wqq when local charge/PID composition is ambiguous.
```

### Features to prioritize

```text
KNN charge fraction
charged-hadron fraction
neutral-hadron fraction
photon fraction
particle0/leading charge
total charged pT around core
charge asymmetry between prongs
```

### Expected Deep Probe if top feature passes threshold

```text
charge/PID neighborhood patch:
  replace charged/neutral KNN composition with matched W-like or Z-like context
  compare targeted patch vs same-count random
```

### Possible claim if supported

```text
ParticleNet uses local charge/PID neighborhood composition as an implicit W/Z hadronic discriminator.
```

---

## Example 2 — Hbb <-> Hcc

### Monitor signal

```text
Hcc -> Hbb and Hbb -> Hcc are both high-rate signals.
```

### Physical question

```text
Both are Higgs -> heavy-flavor qq decays.
The difference is b vs c flavor.
```

### First hypothesis before Feature Ranker

```text
The model uses heavy-flavor proxy features: displaced-track/impact-like information, charged multiplicity, secondary-vertex-like patterns, or b/c PID proxies if present.
```

### Features to prioritize

```text
charged-hadron fraction
track/charge composition
impact/displacement-like channels if full mode exists
KNN hard charged count
leading charged pT fraction
secondary-prong geometry
```

### Expected Deep Probe

```text
heavy-flavor proxy patch:
  swap/mask hard charged neighbors or displacement-like channels if available
  compare Hbb-like vs Hcc-like local context
```

### Possible claim if supported

```text
ParticleNet uses local heavy-flavor proxy structure, not just global mass/pt, for Hbb/Hcc separation.
```

---

## Example 3 — Hgg <-> H4q

### Monitor signal

```text
Hgg -> H4q and H4q -> Hgg are strong signals.
```

### Physical question

```text
Hgg is gluon-rich and often softer/broader.
H4q is four-quark/prong-like and can have different multiplicity/substructure.
```

### First hypothesis before Feature Ranker

```text
The model confuses them when multiplicity, pT spread, or prong geometry becomes ambiguous.
```

### Features to prioritize

```text
n_particles
KNN pT spread
KNN max/mean/sum pT
pairwise deltaR spread
hard-neighbor count
subjet/prong proxies
tau-like or ECF-like features
```

### Expected Deep Probe

```text
substructure patch:
  alter hard-neighbor density or pairwise geometry around core/prongs
  compare targeted geometry patch vs random same-count
```

### Possible claim if supported

```text
ParticleNet uses local multiplicity/prong geometry as an implicit Hgg/H4q discriminator.
```

---

## How this connects to the Hqql/Tbl result

Hqql/Tbl taught the template:

```text
confusion pair -> physical question -> contrastive groups -> monotonic observable -> patch -> surrogate -> residual inversion
```

For Hqql/Tbl:

```text
observable: lepton/core isolation
monotonic ratio: ~= 9.7x
residual inversion: what protects high-isolation Hqql?
next: core/lepton alignment and KNN veto search
```

For every new pair, repeat the same template.

---

## Minimum automatic output for every pair

The system should write one row per candidate:

```text
class_pair
physical_question_hint
top_feature
feature_family
monotonic_ratio
contrastive_effect
counts
recommended_deep_probe
claim_level
```

Claim levels:

```text
0 = raw confusion signal
1 = observable candidate
2 = mechanistic candidate after patch/control
3 = physics-hypothesis candidate after surrogate/residual/stability
4 = cross-model claim
```

---

## Important warning

A strong confusion pair is not automatically an interesting physics discovery.

It becomes interesting only if:

```text
feature has physical meaning
monotonic/bin relation is strong
patch/control supports the mechanism
surrogate explains part of model behavior
residual analysis yields a new trigger/veto question
```
