# Automatic Reasoning Pipeline V1

Goal: automate the Claude-style reasoning framework at scale.

## Core idea

Most of the pipeline can be automated. Human/LLM reasoning is needed only at controlled interpretation gates.

```text
large data stream
-> confusion/anomaly mining
-> contrastive group builder
-> feature library extraction
-> monotonic bin tests
-> patch/control proposal
-> surrogate/residual comparison
-> inversion/veto search
-> ranked hypotheses
-> human/LLM review only for physics meaning and next-feature design
```

## What can be fully automatic

### 1. Anomaly mining

Input:

```text
true labels, predicted labels, logits, event ids, file ids
```

Automatic outputs:

```text
confusion matrix
high-confusion pairs
per-file stability of each confusion pair
class-pair priority score
```

Score:

```text
priority = confusion_rate * n_events * stability_score * confidence_score
```

### 2. Contrastive group generation

For each pair A/B:

```text
A_correct = true A, pred A
A_to_B    = true A, pred B
B_correct = true B, pred B
B_to_A    = true B, pred A
```

Also generate conditional groups:

```text
high_feature protected vs confused
surrogate_overpredict protected vs actual confused
route-active vs route-inactive
```

### 3. Feature extraction

Automatic feature families:

```text
basic kinematics
PID composition
leading/core identity
KNN PID fractions
KNN pT sums
isolation proxies
missing-pT proxies
pairwise deltaR geometry
hard-neighbor counts
subjet/prong proxies
route/head activation summaries
patch sensitivity summaries
```

### 4. Contrastive ranking

For each feature and group pair:

```text
mean difference
ratio
standardized effect
AUC
mutual information approximation
stability by file
```

Output:

```text
candidate discriminants
candidate veto features
candidate trigger features
```

### 5. Monotonicity / bin tests

For every continuous candidate:

```text
bin feature into 5-10 bins
compute confusion/outcome rate per bin
Spearman trend
max/min rate ratio
stability across files
```

Strong observable candidate if:

```text
trend_score high
rate ratio high
enough events per bin
stable across files
```

### 6. Patch/control proposal

Given a feature type, automatically propose controls:

```text
isolation feature -> neighbor injection/removal/sweep
PID feature       -> same-pT PID matched swap
KNN pT feature    -> hard-neighbor patch
geometry feature  -> pairwise geometry swap / nearest-neighbor patch
route feature     -> route-specific mask/replace
```

Every patch must include:

```text
targeted_patch
random_same_count
same_pid_same_pt_control
same_event_nonKNN_control when possible
null baseline
```

### 7. Surrogate + residual

Train explicit surrogate models:

```text
true-label surrogate
model-behavior surrogate
class-pair behavior surrogate
bin-calibrated surrogate
```

Compare:

```text
model rate vs surrogate rate by bins
agreement
AUC
calibration
residual groups
```

### 8. Residual inversion / veto search

If surrogate overpredicts:

```text
protected = high-risk events where model stays correct
actual_confused = high-risk events where model follows surrogate/confuses
find veto features
```

If surrogate underpredicts:

```text
unexpected_confused = events model confuses but surrogate says low-risk
find additional trigger features
```

## Where human/LLM thinking is still needed

### Gate A — physical meaning of class pair

Example:

```text
Hqql and Tbl both include leptonic W-like topology.
```

This is not always recoverable from data alone. It needs domain knowledge or LLM/domain expert.

### Gate B — feature semantics

The system can rank `particle0_iso_pt_ratio`, but human/LLM names it:

```text
lepton/core isolation inside jet
```

### Gate C — patch validity

The system can propose swaps, but human/LLM must check:

```text
Does this patch preserve physical plausibility?
Is random control fair?
Does it create distribution shift?
```

### Gate D — residual interpretation

The system can say surrogate overpredicts high-isolation bin. Human/LLM asks the important question:

```text
What saves the protected high-isolation events?
```

## Big-volume strategy

Use staged automation:

```text
Stage 0 quick scan:  small sample, all class pairs
Stage 1 medium:      top class pairs, all feature families
Stage 2 large/full:  top hypotheses, per-file stability
Stage 3 patch:       only strongest candidates
Stage 4 surrogate:   explicit feature models
Stage 5 veto search: residual inversion groups
```

Do not run expensive patch tests on everything. Run them only after automatic ranking.

## Output schema for automatic reports

Every auto-analysis should write:

```text
hypothesis_id
class_pair
question
contrast_groups
candidate_feature
feature_family
evidence_type: contrastive / monotonic / patch / surrogate / veto
score
stability_score
sample_counts
recommended_next_action
claim_level
```

Claim levels:

```text
0 = weak pattern
1 = observable candidate
2 = mechanistic candidate
3 = physics hypothesis candidate
4 = cross-model claim
```

## Current application to ParticleNet Hqql/Tbl

Already discovered automatically/manually:

```text
confusion pair: Hqql/Tbl
observable: lepton/core isolation
monotonic ratio: ~9.7x
surrogate residual: high-isolation overprediction
inversion question: what protects high-isolation Hqql?
next tool: VETO_SEARCH_V2_FULL_KNN_GEOMETRY
```

## Next implementation target

Build:

```text
tools/auto_reasoning_engine_v1.py
```

It should consume current report tables and produce:

```text
reports/latest/AUTO_REASONING_ENGINE_V1.md
reports/latest/tables/auto_reasoning_hypotheses.csv
manifests/latest/auto_reasoning_engine_v1.json
```

Minimum V1 scope:

```text
class-pair confusion mining
contrastive feature ranking
monotonic bin tests
surrogate residual inversion suggestions
next-experiment recommendations
```
