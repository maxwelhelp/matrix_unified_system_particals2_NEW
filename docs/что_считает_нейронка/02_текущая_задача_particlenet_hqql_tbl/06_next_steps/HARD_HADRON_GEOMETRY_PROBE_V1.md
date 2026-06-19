# HARD_HADRON_GEOMETRY_PROBE_V1

## Why this probe exists

V2.1 showed that `L1_ch80:96` in confused Hqql is not directly driven by second leptons.

Instead, hard hadrons are overrepresented in top activations:

```text
L1_ch80:96 hard_hadron top1:
  A protected_highiso  ~= 0.0312
  B confused_highiso   ~= 0.1818
  C Tbl_correct        ~= 0.0391
```

Important correction:

```text
B is not simply like C.
Hard hadrons activate L1_ch80:96 in confused Hqql, but not in true Tbl_correct.
```

Therefore this is likely a topology-confound / imitation mechanism, not a normal Tbl route.

## Matrix-program interpretation

For an L1 EdgeConv pseudo-head:

```python
for particle i:
    nb = KNN(i)
    local_context = concat(
        H[i, source_blocks],
        mean(H[nb, source_blocks]),
        max(H[nb, source_blocks]),
        edge_features(i, nb),
    )
    z_i = W @ local_context
    H_next[i, 80:96] = z_i
```

So the hard hadron may not be important because it is Tbl-like alone. It may be important because it enters the lepton neighborhood and changes the lepton local_context.

## Questions tested

For hard-hadron top activations in `L1_ch80:96`:

```text
Q1. Is the hard hadron inside the best-lepton KNN?
Q2. What is deltaR(hard_hadron, best_lepton)?
Q3. Does the same hard hadron also activate L2_ch128:160?
Q4. Is the geometry in confused Hqql closer to protected Hqql or to true Tbl?
```

## Expected mechanisms

If B hard hadrons are close to best lepton and inside lepton KNN:

```text
hard hadrons enter lepton local_context
-> L1_ch80:96 builds a top-like / Tbl-like route
```

If the same hard hadrons are not top activators in L2_ch128:160:

```text
L2 does not recover correct Hqql evidence from them
-> Hqql evidence stays weak
```

## Output

```text
reports/latest/HARD_HADRON_GEOMETRY_PROBE_V1.md
reports/latest/tables/hard_hadron_geometry_probe_v1_rows.csv
reports/latest/tables/hard_hadron_geometry_probe_v1_summary.csv
manifests/latest/hard_hadron_geometry_probe_v1.json
```
