# GEOMETRY_VETO_PATCH_V1

Purpose: test the two candidate mechanisms found by VETO_SEARCH_V2.

## Starting point

High-isolation Hqql events split into:

```text
protected_highiso: true=Hqql, pred=Hqql
actual_confused_highiso: true=Hqql, pred=Tbl
```

VETO_SEARCH_V2 suggests two effects:

```text
A. geometry veto:
   protected has more compact / energetic lepton-centered KNN context

B. second-lepton trigger:
   confused has much higher second_lepton_present
```

## Patches

### G1 compact KNN injection

For highiso Hqql_to_Tbl targets:

```text
keep target event and best lepton
replace KNN neighbors around target lepton
with KNN neighbors around matched protected_highiso lepton
```

Control:

```text
same-PID / pT-matched random neighbor replacement
```

### G2 second lepton removal

For highiso Hqql_to_Tbl targets with second lepton:

```text
remove second lepton-like object
```

Control:

```text
remove random non-best-lepton particle
```

### G3 combined

```text
G1 compact KNN injection + G2 second lepton removal
```

Interpretation:

```text
G3 >> G1 and G2: additive / interacting mechanisms
G3 ~= max(G1,G2): one mechanism dominates
```

## Metrics

```text
success_to_Hqql_rate
flip_rate
delta_margin_Hqql_minus_Tbl
random/control comparison
```

Strong support:

```text
targeted success / control success > 3x
and targeted delta_margin > control delta_margin
```
