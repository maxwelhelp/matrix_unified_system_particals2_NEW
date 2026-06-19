# Route Specific Patch v1

Goal: move from event-level explanation to causal route test.

`EVENT_FORECAST_EXPLAINER_V1` shows which heads/routes are active. But raw activation ranking can put L0/L1 context builders above L2 class readouts because early activations have larger scale. Therefore we need a targeted patch:

```text
baseline event prediction
-> remove/zero selected route particles for selected L2 readout heads
-> compare logits/prediction/confidence
-> compare with random same-count patch
```

Primary target heads:

```text
L2_ch224:256
L2_ch128:160
L2_ch32:64
L2_ch0:32
```

Patch modes:

```text
remove_top_particle
remove_knn_neighbors
remove_top_plus_knn
random_same_count
```

Outputs:

```text
reports/latest/ROUTE_SPECIFIC_PATCH_V1.md
reports/latest/tables/route_specific_patch_results.csv
manifests/latest/route_specific_patch_v1.json
```

Interpretation:

If removing the L2 route top particle / KNN route flips or strongly reduces the target logit while random same-count does not, then the route-aware pseudocode is causally supported.
