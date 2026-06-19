# Next Control Matrix v1

This is the priority matrix for the next experiments.

## P0 controls

| Control | Why needed | Current blocker | Expected useful output |
|---|---|---|---|
| particle0 removal | tests whether leading particle is necessary | particle0/core dominates stream | class accuracy/logit drop by class |
| keep-only particle0 | tests whether model mostly uses shortcut | particle0 may explain too much alone | shortcut score |
| top-k removal | tests core dependence curve | top particle evidence is core-heavy | k -> class/logit drop curve |
| same-count random removal | baseline for removal controls | need causal contrast | random-vs-targeted delta |
| particle order shuffle | separates sorting index from physics | particle0 may be ordering shortcut | order sensitivity score |
| class-specific gradients | separates global heads from class roles | Hqql/Tbl dominate stream | head-by-class matrix |
| known-observable residual | separates known physics from residual signal | particle0 may proxy pt/mass/tau | residual candidate score |
| per-file heldout | tests stability beyond tiny extracted files | same files can fake stability | file-stability score |

## P1 controls

| Control | Why needed | Output |
|---|---|---|
| route-neighbor trace | tells whether wide particles matter via KNN route | top particle -> neighbor graph |
| head-pair synergy | tests distributed computation | additive/synergistic/redundant heads |
| correct-vs-wrong atlas | tells what heads do on errors | false-class route analysis |
| cross-model agreement | tests architecture-specific artifacts | ParticleNet vs ParT agreement |

## Recommended order

```text
1. particle0/top-k controls
2. particle order shuffle
3. class-specific gradients
4. known-observable residual
5. per-file heldout
6. route-neighbor trace
7. head-pair synergy
8. cross-model agreement
```

## Decision logic

### If particle0 removal collapses Hqql/Tbl

Then:

```text
leading-core is causally important
```

Next:

```text
check if known observables explain it
```

### If keep-only particle0 keeps high performance

Then:

```text
shortcut risk is high
```

Next:

```text
order shuffle + residual test
```

### If particle0 removal barely changes performance

Then:

```text
particle0 dominance in stream may be attribution artifact or redundant evidence
```

Next:

```text
top-k / secondary context / route-neighbor trace
```

### If class-specific gradients show different heads per class

Then:

```text
build class-wise circuit atlas
```

### If residual after known observables remains strong

Then:

```text
residual candidate becomes interesting
```

### If residual disappears

Then:

```text
signal is likely known-observable proxy, still useful but not discovery-like
```
