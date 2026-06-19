# Hqql/Tbl Physical Confusion Frame v1

Claude's critique is correct: the project has been answering mostly **how the network computes**, but the physics question is **what the route physically represents**.

## New central question

```text
For Hqql events predicted as Tbl, what is particle0 / leading-core physically?
```

Not enough:

```text
L2 head -> particle0 -> KNN neighbors
```

Needed:

```text
Is particle0 a lepton?
Is it a charged hadron / photon / neutral hadron?
What is its pT rank and isolation?
What are its KNN neighbors physically?
How do confused Hqql->Tbl events differ from correct Hqql and correct Tbl?
```

## Correct pipeline shift

Old pipeline:

```text
route -> causal patch -> residual -> hypothesis
```

New pipeline:

```text
confusion regime -> physical observable -> ambiguity reason -> route -> patch
```

## First concrete target

Compare groups:

```text
Hqql_correct: true Hqql, pred Hqql
Hqql_to_Tbl:  true Hqql, pred Tbl
Tbl_correct:  true Tbl,  pred Tbl
Tbl_to_Hqql:  true Tbl,  pred Hqql if present
```

For each group, measure:

```text
particle0 PID / charge / pT rank / isolation proxy
leading particle PID / charge / isolation proxy
L2 route-top particle PID / charge / isolation proxy
KNN neighbor PID composition
lepton isolation proxy
missing-pT / momentum imbalance proxy
lepton-core deltaR proxies
```

## Why this matters

If Hqql_to_Tbl events systematically have a lepton-like or Tbl-like core route, then the network confusion is physically meaningful, not just a neural artifact.

## Next tools

```text
tools/hqql_tbl_confusion_physics_regime_v1.py
scripts/RUN_HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.sh
```

Then:

```text
ROUTE_SPECIFIC_PATCH_V1 should patch physical routes selected from this confusion regime, not only generic L2 heads.
KNOWN_OBSERVABLE_RESIDUAL_V2 should include leptonic-W and core-neighborhood observables.
```
