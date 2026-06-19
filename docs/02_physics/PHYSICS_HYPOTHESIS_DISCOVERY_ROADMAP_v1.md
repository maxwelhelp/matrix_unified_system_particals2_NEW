# Physics Hypothesis / Discovery Roadmap v1

This document explains how to move from an interpretable ParticleNet mechanism to physics hypotheses.

## Current state

We currently have a mechanistic interpretation candidate, not a discovery claim.

The evidence chain so far:

```text
stream/core signal
-> particle0/top-k targeted controls
-> order-control reduced array-index artifact
-> confusion atlas showed structured class collapse
-> known-observable residual v1 found simple surrogate insufficient
-> pseudocode v2/v3 tied heads to code/output/routes
-> EdgeConv inner trace v2 showed L2 core-neighborhood routes
```

## Current safest statement

```text
ParticleNet_kinpid appears to build local/neighbor context in L0/L1 and then perform late class-evidence readout in L2 through particle0/leading-pT core routes. This helps explain Tbl/Hqql/H4q/W/Z/QCD class competition. Simple known-observable surrogate v1 does not reproduce ParticleNet decisions, so a residual mechanism candidate remains.
```

## What we can predict now

Current system can predict and explain:

```text
1. which known class the model will choose
2. which pseudo-heads contribute to the prediction
3. whether prediction is driven by core/particle0/leading-pT route
4. which KNN neighbors feed selected route
5. which class-confusion axis is active, e.g. Hqql->Tbl or signal->QCD
6. whether simple known observables explain the decision poorly
```

Current system cannot yet honestly predict:

```text
1. new particle existence
2. new interaction existence
3. mass peak / resonance
4. cross-section / branching ratio
5. detector-level discovery significance
```

Those need additional data and physics validation.

## Discovery-style hypothesis pipeline

### Stage A — Mechanism hypothesis

Question:

```text
What does the trained network compute?
```

Evidence:

```text
pseudocode v3
EdgeConv inner trace v2
head output trace
class gradients
controls
```

Output:

```text
route-aware mechanism statement
```

Example:

```text
L2_ch128:160 and L2_ch224:256 implement Tbl-like late core-neighborhood readout. Hqql events can trigger this route and collapse toward Tbl.
```

### Stage B — Observable-vs-residual hypothesis

Question:

```text
Is the mechanism just known physics observables?
```

Evidence needed:

```text
known_observable_residual_v2
pair/ECF-like features
tau-like proxies
subjet/top-k pair features
per-file heldout
```

Output:

```text
known proxy / partial residual / strong residual candidate
```

### Stage C — Event-level prediction/explanation

Question:

```text
For this event, what will the network predict and why?
```

Needed tool:

```text
EVENT_FORECAST_EXPLAINER_V1
```

It should output:

```text
predicted class
confidence/logits
active pseudo-head routes
active particles and KNN neighbors
known-observable surrogate prediction
residual score
human-readable explanation
```

### Stage D — Hypothesis generation

Question:

```text
What physical pattern might the residual route represent?
```

Candidate outputs:

```text
unmodeled substructure
heavy-flavor/core-neighborhood relation
specific top-k energy-sharing pattern
wide-angle secondary-prong context
PID/charge-neighborhood motif
simulation shortcut / generator artifact
```

### Stage E — Physics validation

Before any discovery-style claim:

```text
heldout/per-file stability
cross-model agreement: ParticleNet vs ParT vs independent model
simulation/source split
known-observable residual v2/v3
mass/resonance or invariant-feature check if applicable
background-only control
data-vs-simulation sanity checks
systematic uncertainty checks
```

## First concrete hypotheses to test

### H1 — Tbl-like core-neighborhood route

Evidence:

```text
L2_ch224:256 and L2_ch128:160 have high particle0/leading-pT route rates and top Tbl events.
Hqql event can activate Tbl-like route.
```

Hypothesis:

```text
The model recognizes a Tbl-like core-neighborhood motif not captured by simple observables v1.
```

Next tests:

```text
route-specific patch
residual v2
per-file stability
cross-model agreement
```

### H2 — Hqql/Tbl confusion axis

Evidence:

```text
keep_only_particle0 can push Hqql toward Tbl.
L2 core heads are Tbl-heavy.
Residual top events include Hqql/Tbl axis.
```

Hypothesis:

```text
Hqql and Tbl share a core route; secondary context resolves them.
```

Next tests:

```text
remove/patch secondary KNN neighbors
trace L1 context relays feeding L2 core heads
```

### H3 — L0/L1 wide-context builders

Evidence:

```text
L0/L1 heads often activate on non-core particles.
They have context/non-core routes but feed question-ranked L2 readout.
```

Hypothesis:

```text
The network builds class context away from particle0, then L2 reads final evidence through core particle route.
```

Next tests:

```text
edgeconv_inner_trace_v2/v3 neighbor contribution
head-pair synergy patch: L1 context head + L2 readout head
```

## Next tools to build

```text
1. EVENT_FORECAST_EXPLAINER_V1
2. ROUTE_SPECIFIC_PATCH_V1
3. KNOWN_OBSERVABLE_RESIDUAL_V2
4. PER_FILE_MECHANISM_STABILITY_V1
5. CROSS_MODEL_MECHANISM_AGREEMENT_V1
```

## Minimal event-level explanation target

For every interesting event, produce:

```text
input event id
true label / predicted label
model logits
known-observable surrogate prediction
residual score
active L0/L1/L2 pseudo-heads
active particles / KNN route
route-aware pseudocode explanation
hypothesis tag
next validation
```

## Main decision rule

A physics hypothesis becomes strong only if:

```text
mechanism is interpretable
+ route-specific patch changes prediction
+ residual remains after richer known observables
+ heldout/per-file stable
+ cross-model stable
+ physics sanity checks pass
```

Until then, call it:

```text
mechanism candidate / residual route candidate
```

not:

```text
discovery
```
