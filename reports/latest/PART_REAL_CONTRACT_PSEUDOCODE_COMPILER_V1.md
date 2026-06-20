# PART_REAL_CONTRACT_PSEUDOCODE_COMPILER_V1

This report compiles real-contract ParT head/layer traces into readable matrix/pseudocode rules. It is not a standard attention plot.

## Validity base

- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`
- data_config: `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`
- traced events: **1024**
- pair rows: **327680**
- summary rows: **1845**
- compiled rules: **48**
- pad-linked routes: excluded in this compiler v1

## Route type counts

| route_type | count |
| --- | --- |
| LEPTON_LEPTON_ROUTE | 31 |
| LEPTON_READS_HADRON_ROUTE | 8 |
| PHOTON_HADRON_ROUTE | 4 |
| HADRON_HADRON_TOPOLOGY_ROUTE | 2 |
| LEPTON_PHOTON_ROUTE | 2 |
| HADRON_READS_LEPTON_ROUTE | 1 |

## Module concentration

| module | count |
| --- | --- |
| mod.blocks.6.attn | 17 |
| mod.blocks.7.attn | 11 |
| mod.blocks.3.attn | 7 |
| mod.blocks.5.attn | 5 |
| mod.blocks.2.attn | 5 |
| mod.blocks.4.attn | 3 |

## Rules where Hqql becomes Tbl-like

| rule | module | head | route | type | strength | action |
| --- | --- | --- | --- | --- | --- | --- |
| R001_B_to_Tbl | mod.blocks.7.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.99983 | route Hqql event toward Tbl-like evidence |
| R002_B_to_Tbl | mod.blocks.6.attn | 0 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.99959 | route Hqql event toward Tbl-like evidence |
| R003_B_to_Tbl | mod.blocks.7.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.99689 | route Hqql event toward Tbl-like evidence |
| R004_B_to_Tbl | mod.blocks.5.attn | 2 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.99519 | route Hqql event toward Tbl-like evidence |
| R005_B_to_Tbl | mod.blocks.7.attn | 0 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.99463 | route Hqql event toward Tbl-like evidence |
| R006_B_to_Tbl | mod.blocks.7.attn | 6 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.99142 | route Hqql event toward Tbl-like evidence |
| R007_B_to_Tbl | mod.blocks.6.attn | 4 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.98895 | route Hqql event toward Tbl-like evidence |
| R008_B_to_Tbl | mod.blocks.5.attn | 7 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.98828 | route Hqql event toward Tbl-like evidence |
| R009_B_to_Tbl | mod.blocks.6.attn | 0 | photon<-neutral_hadron | PHOTON_HADRON_ROUTE | 0.98736 | route Hqql event toward Tbl-like evidence |
| R010_B_to_Tbl | mod.blocks.6.attn | 0 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.9866 | route Hqql event toward Tbl-like evidence |
| R011_B_to_Tbl | mod.blocks.6.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.97966 | route Hqql event toward Tbl-like evidence |
| R012_B_to_Tbl | mod.blocks.6.attn | 6 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.97259 | route Hqql event toward Tbl-like evidence |
| R013_B_to_Tbl | mod.blocks.4.attn | 5 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.95269 | route Hqql event toward Tbl-like evidence |
| R014_B_to_Tbl | mod.blocks.6.attn | 0 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.94817 | route Hqql event toward Tbl-like evidence |
| R015_B_to_Tbl | mod.blocks.7.attn | 2 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.94389 | route Hqql event toward Tbl-like evidence |
| R016_B_to_Tbl | mod.blocks.5.attn | 6 | muon<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.92837 | route Hqql event toward Tbl-like evidence |
| R017_B_to_Tbl | mod.blocks.6.attn | 6 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.92758 | route Hqql event toward Tbl-like evidence |
| R018_B_to_Tbl | mod.blocks.6.attn | 6 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.92455 | route Hqql event toward Tbl-like evidence |

### R001_B_to_Tbl `mod.blocks.7.attn#h4` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.7.attn][4] reads muon <- muon: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.7.attn, head=4, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.99983 C=0.00000 D=0.00000 strength=0.99983

### R002_B_to_Tbl `mod.blocks.6.attn#h0` `electron<-electron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.6.attn][0] reads electron <- electron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.6.attn, head=0, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.99959 C=0.81136 D=0.81824 strength=0.99959

### R003_B_to_Tbl `mod.blocks.7.attn#h4` `muon<-electron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.7.attn][4] reads muon <- electron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.7.attn, head=4, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.99689 C=0.00000 D=0.00000 strength=0.99689

### R004_B_to_Tbl `mod.blocks.5.attn#h2` `electron<-neutral_hadron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.5.attn][2] reads electron <- neutral_hadron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.5.attn, head=2, electron<-neutral_hadron] := attention_weight * role_gate(electron,neutral_hadron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.99519 C=0.82610 D=0.66386 strength=0.99519

### R005_B_to_Tbl `mod.blocks.7.attn#h0` `electron<-electron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.7.attn][0] reads electron <- electron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.7.attn, head=0, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.99463 C=0.80795 D=0.59530 strength=0.99463

### R006_B_to_Tbl `mod.blocks.7.attn#h6` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.7.attn][6] reads muon <- muon: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.7.attn, head=6, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.99142 C=0.00000 D=0.00000 strength=0.99142

### R007_B_to_Tbl `mod.blocks.6.attn#h4` `electron<-electron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.6.attn][4] reads electron <- electron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.6.attn, head=4, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.98895 C=0.93771 D=0.91624 strength=0.98895

### R008_B_to_Tbl `mod.blocks.5.attn#h7` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.5.attn][7] reads muon <- muon: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.5.attn, head=7, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.98828 C=0.94345 D=0.00000 strength=0.98828

## Rules where Hqql is protected

| rule | module | head | route | type | strength | action |
| --- | --- | --- | --- | --- | --- | --- |
| R001_A_protect | mod.blocks.7.attn | 3 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.99912 | preserve Hqql evidence and resist Tbl-like confusion |
| R002_A_protect | mod.blocks.2.attn | 3 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.99357 | preserve Hqql evidence and resist Tbl-like confusion |
| R003_A_protect | mod.blocks.6.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.98862 | preserve Hqql evidence and resist Tbl-like confusion |
| R004_A_protect | mod.blocks.6.attn | 6 | muon<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.98815 | preserve Hqql evidence and resist Tbl-like confusion |
| R005_A_protect | mod.blocks.3.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.9877 | preserve Hqql evidence and resist Tbl-like confusion |
| R006_A_protect | mod.blocks.7.attn | 0 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.9767 | preserve Hqql evidence and resist Tbl-like confusion |
| R007_A_protect | mod.blocks.6.attn | 4 | neutral_hadron<-charged_hadron | HADRON_HADRON_TOPOLOGY_ROUTE | 0.97475 | preserve Hqql evidence and resist Tbl-like confusion |
| R008_A_protect | mod.blocks.6.attn | 4 | photon<-neutral_hadron | PHOTON_HADRON_ROUTE | 0.95746 | preserve Hqql evidence and resist Tbl-like confusion |
| R009_A_protect | mod.blocks.5.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.95416 | preserve Hqql evidence and resist Tbl-like confusion |
| R010_A_protect | mod.blocks.6.attn | 4 | photon<-charged_hadron | PHOTON_HADRON_ROUTE | 0.94236 | preserve Hqql evidence and resist Tbl-like confusion |
| R011_A_protect | mod.blocks.3.attn | 2 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.94233 | preserve Hqql evidence and resist Tbl-like confusion |
| R012_A_protect | mod.blocks.3.attn | 0 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.9396 | preserve Hqql evidence and resist Tbl-like confusion |
| R013_A_protect | mod.blocks.2.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.91084 | preserve Hqql evidence and resist Tbl-like confusion |
| R014_A_protect | mod.blocks.6.attn | 4 | charged_hadron<-neutral_hadron | HADRON_HADRON_TOPOLOGY_ROUTE | 0.90792 | preserve Hqql evidence and resist Tbl-like confusion |
| R015_A_protect | mod.blocks.5.attn | 7 | photon<-neutral_hadron | PHOTON_HADRON_ROUTE | 0.89928 | preserve Hqql evidence and resist Tbl-like confusion |
| R016_A_protect | mod.blocks.3.attn | 2 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.89318 | preserve Hqql evidence and resist Tbl-like confusion |
| R017_A_protect | mod.blocks.3.attn | 7 | electron<-charged_hadron | LEPTON_READS_HADRON_ROUTE | 0.89187 | preserve Hqql evidence and resist Tbl-like confusion |
| R018_A_protect | mod.blocks.2.attn | 1 | muon<-photon | LEPTON_PHOTON_ROUTE | 0.85991 | preserve Hqql evidence and resist Tbl-like confusion |

### R001_A_protect `mod.blocks.7.attn#h3` `electron<-muon`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.7.attn][3] reads electron <- muon: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.7.attn, head=3, electron<-muon] := attention_weight * role_gate(electron,muon) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.99912 B=0.00000 C=0.92812 D=0.87833 strength=0.99912

### R002_A_protect `mod.blocks.2.attn#h3` `muon<-muon`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.2.attn][3] reads muon <- muon: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.2.attn, head=3, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.99357 B=0.00000 C=0.63682 D=0.98051 strength=0.99357

### R003_A_protect `mod.blocks.6.attn#h5` `electron<-electron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.6.attn][5] reads electron <- electron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.6.attn, head=5, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.98862 B=0.00000 C=0.00000 D=0.91956 strength=0.98862

### R004_A_protect `mod.blocks.6.attn#h6` `muon<-neutral_hadron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.6.attn][6] reads muon <- neutral_hadron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.6.attn, head=6, muon<-neutral_hadron] := attention_weight * role_gate(muon,neutral_hadron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.98815 B=0.00000 C=0.00000 D=0.78898 strength=0.98815

### R005_A_protect `mod.blocks.3.attn#h5` `electron<-electron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.3.attn][5] reads electron <- electron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.3.attn, head=5, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.98770 B=0.00000 C=0.59845 D=0.00000 strength=0.98770

### R006_A_protect `mod.blocks.7.attn#h0` `electron<-muon`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.7.attn][0] reads electron <- muon: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.7.attn, head=0, electron<-muon] := attention_weight * role_gate(electron,muon) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.97670 B=0.00000 C=0.00000 D=0.00000 strength=0.97670

### R007_A_protect `mod.blocks.6.attn#h4` `neutral_hadron<-charged_hadron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.6.attn][4] reads neutral_hadron <- charged_hadron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.6.attn, head=4, neutral_hadron<-charged_hadron] := attention_weight * role_gate(neutral_hadron,charged_hadron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.97475 B=0.00000 C=0.57348 D=0.00000 strength=0.97475

### R008_A_protect `mod.blocks.6.attn#h4` `photon<-neutral_hadron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.6.attn][4] reads photon <- neutral_hadron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.6.attn, head=4, photon<-neutral_hadron] := attention_weight * role_gate(photon,neutral_hadron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.95746 B=0.00000 C=0.00000 D=0.00000 strength=0.95746

## Anomaly rules

| rule | module | head | route | type | strength | action |
| --- | --- | --- | --- | --- | --- | --- |
| R001_anomaly | mod.blocks.7.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.99966 | mark nonstandard transition route |
| R002_anomaly | mod.blocks.7.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.99379 | mark nonstandard transition route |
| R003_anomaly | mod.blocks.7.attn | 6 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.98291 | mark nonstandard transition route |
| R004_anomaly | mod.blocks.7.attn | 3 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.9273 | mark nonstandard transition route |
| R005_anomaly | mod.blocks.3.attn | 0 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.91179 | mark nonstandard transition route |
| R006_anomaly | mod.blocks.6.attn | 6 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.8604 | mark nonstandard transition route |
| R007_anomaly | mod.blocks.6.attn | 6 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.85479 | mark nonstandard transition route |
| R008_anomaly | mod.blocks.4.attn | 0 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.84365 | mark nonstandard transition route |
| R009_anomaly | mod.blocks.2.attn | 1 | muon<-photon | LEPTON_PHOTON_ROUTE | 0.8424 | mark nonstandard transition route |
| R010_anomaly | mod.blocks.2.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.82396 | mark nonstandard transition route |
| R011_anomaly | mod.blocks.3.attn | 2 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.75348 | mark nonstandard transition route |
| R012_anomaly | mod.blocks.4.attn | 3 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.75272 | mark nonstandard transition route |

### R001_anomaly `mod.blocks.7.attn#h4` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.7.attn][4] reads muon <- muon: mark nonstandard transition route
ROUTE[mod.blocks.7.attn, head=4, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.00000 B=0.99983 C=0.00000 D=0.00000 strength=0.99966

### R002_anomaly `mod.blocks.7.attn#h4` `muon<-electron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.7.attn][4] reads muon <- electron: mark nonstandard transition route
ROUTE[mod.blocks.7.attn, head=4, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.00000 B=0.99689 C=0.00000 D=0.00000 strength=0.99379

### R003_anomaly `mod.blocks.7.attn#h6` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.7.attn][6] reads muon <- muon: mark nonstandard transition route
ROUTE[mod.blocks.7.attn, head=6, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.00000 B=0.99142 C=0.00000 D=0.00000 strength=0.98291

### R004_anomaly `mod.blocks.7.attn#h3` `electron<-muon`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.7.attn][3] reads electron <- muon: mark nonstandard transition route
ROUTE[mod.blocks.7.attn, head=3, electron<-muon] := attention_weight * role_gate(electron,muon) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.99912 B=0.00000 C=0.92812 D=0.87833 strength=0.92730

### R005_anomaly `mod.blocks.3.attn#h0` `electron<-electron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.3.attn][0] reads electron <- electron: mark nonstandard transition route
ROUTE[mod.blocks.3.attn, head=0, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.93960 B=0.00000 C=0.97040 D=0.00000 strength=0.91179

### R006_anomaly `mod.blocks.6.attn#h6` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.6.attn][6] reads muon <- muon: mark nonstandard transition route
ROUTE[mod.blocks.6.attn, head=6, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.00000 B=0.92758 C=0.00000 D=0.00000 strength=0.86040

### R007_anomaly `mod.blocks.6.attn#h6` `muon<-electron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.6.attn][6] reads muon <- electron: mark nonstandard transition route
ROUTE[mod.blocks.6.attn, head=6, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.00000 B=0.92455 C=0.00000 D=0.00000 strength=0.85479

### R008_anomaly `mod.blocks.4.attn#h0` `muon<-electron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.4.attn][0] reads muon <- electron: mark nonstandard transition route
ROUTE[mod.blocks.4.attn, head=0, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.00000 B=0.91851 C=0.00000 D=0.76188 strength=0.84365

## What this preserves

- head/layer provenance
- role-to-role route
- class-regime difference
- matrix-route form
- pseudocode form
- real-contract source trace

## Next validation

1. run pad-control report
2. test top rules by head/route drop-control
3. compare against WToQQ and TTBar regimes
4. promote stable rules into operation dictionary

