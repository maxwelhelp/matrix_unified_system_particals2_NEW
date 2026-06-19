# EdgeConv Inner Trace v1

Question-driven analyzer tells us which pseudo-heads to inspect. EdgeConv inner trace inspects how those heads are produced inside the real layer.

## Goal

For ranked pseudo-heads, trace:

```text
EdgeConvBlock input
inner conv stack outputs
final EdgeConvBlock output slice
per-particle activation
leading-pT / particle0 match
KNN neighbor indices for top activated particles
raw top-particle features
```

## Why this is needed

Pseudocode v2 says what a pseudo-head likely computes. Output trace says what it writes. Inner trace connects this to the real EdgeConv computation path:

```text
points/features -> KNN neighbors -> edge/conv stack -> channel slice -> pseudo-head output
```

## Main questions

```text
Which neighbors feed the top activated particle?
Do L2 core readouts really read particle0/leading-pT neighborhoods?
Which L0/L1 heads build context away from the leading particle?
Which heads should get ablation/patch next?
```

## Output

```text
reports/latest/EDGE_CONV_INNER_TRACE_V1.md
reports/latest/tables/edgeconv_inner_trace_heads.csv
reports/latest/tables/edgeconv_inner_trace_events.csv
manifests/latest/edgeconv_inner_trace_v1.json
```
