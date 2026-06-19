# PART_REAL_CONTRACT_PSEUDOCODE_COMPILER_V1

This report compiles real-contract ParT head/layer traces into readable matrix/pseudocode rules. It is not a standard attention plot.

## Validity base

- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`
- data_config: `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`
- traced events: **1024**
- pair rows: **327680**
- summary rows: **1891**
- compiled rules: **48**
- pad-linked routes: excluded in this compiler v1

## Route type counts

| route_type | count |
| --- | --- |
| LEPTON_LEPTON_ROUTE | 31 |
| HADRON_READS_LEPTON_ROUTE | 8 |
| LEPTON_READS_HADRON_ROUTE | 4 |
| LEPTON_PHOTON_ROUTE | 3 |
| HADRON_HADRON_TOPOLOGY_ROUTE | 1 |
| PHOTON_HADRON_ROUTE | 1 |

## Module concentration

| module | count |
| --- | --- |
| mod.blocks.6.attn | 13 |
| mod.blocks.5.attn | 12 |
| mod.blocks.7.attn | 10 |
| mod.blocks.3.attn | 4 |
| mod.blocks.4.attn | 3 |
| mod.blocks.2.attn | 3 |
| mod.blocks.1.attn | 2 |
| mod.blocks.0.attn | 1 |

## Rules where Hqql becomes Tbl-like

| rule | module | head | route | type | strength | action |
| --- | --- | --- | --- | --- | --- | --- |
| R001_B_to_Tbl | mod.blocks.7.attn | 4 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.99492 | route Hqql event toward Tbl-like evidence |
| R002_B_to_Tbl | mod.blocks.6.attn | 4 | muon<-photon | LEPTON_PHOTON_ROUTE | 0.97246 | route Hqql event toward Tbl-like evidence |
| R003_B_to_Tbl | mod.blocks.1.attn | 1 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.95715 | route Hqql event toward Tbl-like evidence |
| R004_B_to_Tbl | mod.blocks.4.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.95476 | route Hqql event toward Tbl-like evidence |
| R005_B_to_Tbl | mod.blocks.7.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.91416 | route Hqql event toward Tbl-like evidence |
| R006_B_to_Tbl | mod.blocks.5.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.84707 | route Hqql event toward Tbl-like evidence |
| R007_B_to_Tbl | mod.blocks.5.attn | 6 | photon<-muon | LEPTON_PHOTON_ROUTE | 0.83968 | route Hqql event toward Tbl-like evidence |
| R008_B_to_Tbl | mod.blocks.6.attn | 6 | neutral_hadron<-neutral_hadron | HADRON_HADRON_TOPOLOGY_ROUTE | 0.8375 | route Hqql event toward Tbl-like evidence |
| R009_B_to_Tbl | mod.blocks.6.attn | 0 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.82479 | route Hqql event toward Tbl-like evidence |
| R010_B_to_Tbl | mod.blocks.4.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.81415 | route Hqql event toward Tbl-like evidence |
| R011_B_to_Tbl | mod.blocks.6.attn | 4 | photon<-charged_hadron | PHOTON_HADRON_ROUTE | 0.79398 | route Hqql event toward Tbl-like evidence |
| R012_B_to_Tbl | mod.blocks.3.attn | 2 | charged_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.77901 | route Hqql event toward Tbl-like evidence |
| R013_B_to_Tbl | mod.blocks.3.attn | 5 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.7758 | route Hqql event toward Tbl-like evidence |
| R014_B_to_Tbl | mod.blocks.5.attn | 7 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.77521 | route Hqql event toward Tbl-like evidence |
| R015_B_to_Tbl | mod.blocks.7.attn | 6 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.77371 | route Hqql event toward Tbl-like evidence |
| R016_B_to_Tbl | mod.blocks.6.attn | 6 | muon<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.76327 | route Hqql event toward Tbl-like evidence |
| R017_B_to_Tbl | mod.blocks.6.attn | 2 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.73291 | route Hqql event toward Tbl-like evidence |
| R018_B_to_Tbl | mod.blocks.6.attn | 7 | electron<-photon | LEPTON_PHOTON_ROUTE | 0.73072 | route Hqql event toward Tbl-like evidence |

### R001_B_to_Tbl `mod.blocks.7.attn#h4` `electron<-muon`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.7.attn][4] reads electron <- muon: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.7.attn, head=4, electron<-muon] := attention_weight * role_gate(electron,muon) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.99492 C=0.99739 D=0.99919 strength=0.99492

### R002_B_to_Tbl `mod.blocks.6.attn#h4` `muon<-photon`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.6.attn][4] reads muon <- photon: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.6.attn, head=4, muon<-photon] := attention_weight * role_gate(muon,photon) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.97246 C=0.74121 D=0.75982 strength=0.97246

### R003_B_to_Tbl `mod.blocks.1.attn#h1` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.1.attn][1] reads muon <- muon: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.1.attn, head=1, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.95715 C=0.94390 D=0.90858 strength=0.95715

### R004_B_to_Tbl `mod.blocks.4.attn#h4` `muon<-electron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.4.attn][4] reads muon <- electron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.4.attn, head=4, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.95476 C=0.00000 D=0.97434 strength=0.95476

### R005_B_to_Tbl `mod.blocks.7.attn#h5` `electron<-electron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.7.attn][5] reads electron <- electron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.7.attn, head=5, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.91416 C=0.41317 D=0.60410 strength=0.91416

### R006_B_to_Tbl `mod.blocks.5.attn#h4` `muon<-electron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.5.attn][4] reads muon <- electron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.5.attn, head=4, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.84707 C=0.00000 D=0.00000 strength=0.84707

### R007_B_to_Tbl `mod.blocks.5.attn#h6` `photon<-muon`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.5.attn][6] reads photon <- muon: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.5.attn, head=6, photon<-muon] := attention_weight * role_gate(photon,muon) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.83968 C=0.95644 D=0.88518 strength=0.83968

### R008_B_to_Tbl `mod.blocks.6.attn#h6` `neutral_hadron<-neutral_hadron`

```text
IF group == B_Hqql_to_Tbl AND HEAD[mod.blocks.6.attn][6] reads neutral_hadron <- neutral_hadron: route Hqql event toward Tbl-like evidence
ROUTE[mod.blocks.6.attn, head=6, neutral_hadron<-neutral_hadron] := attention_weight * role_gate(neutral_hadron,neutral_hadron) * class_regime(B_Hqql_to_Tbl)
```
- meaning: route is stronger in Hqql→Tbl mistakes than in correct Hqql
- A=0.00000 B=0.83750 C=0.85019 D=0.82503 strength=0.83750

## Rules where Hqql is protected

| rule | module | head | route | type | strength | action |
| --- | --- | --- | --- | --- | --- | --- |
| R001_A_protect | mod.blocks.5.attn | 1 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.99932 | preserve Hqql evidence and resist Tbl-like confusion |
| R002_A_protect | mod.blocks.7.attn | 1 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.97833 | preserve Hqql evidence and resist Tbl-like confusion |
| R003_A_protect | mod.blocks.7.attn | 5 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.97671 | preserve Hqql evidence and resist Tbl-like confusion |
| R004_A_protect | mod.blocks.7.attn | 4 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.96647 | preserve Hqql evidence and resist Tbl-like confusion |
| R005_A_protect | mod.blocks.6.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.93515 | preserve Hqql evidence and resist Tbl-like confusion |
| R006_A_protect | mod.blocks.5.attn | 5 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.90792 | preserve Hqql evidence and resist Tbl-like confusion |
| R007_A_protect | mod.blocks.7.attn | 5 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.88279 | preserve Hqql evidence and resist Tbl-like confusion |
| R008_A_protect | mod.blocks.5.attn | 6 | charged_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.87231 | preserve Hqql evidence and resist Tbl-like confusion |
| R009_A_protect | mod.blocks.6.attn | 5 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.8719 | preserve Hqql evidence and resist Tbl-like confusion |
| R010_A_protect | mod.blocks.6.attn | 6 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.86733 | preserve Hqql evidence and resist Tbl-like confusion |
| R011_A_protect | mod.blocks.5.attn | 6 | charged_hadron<-electron | HADRON_READS_LEPTON_ROUTE | 0.85955 | preserve Hqql evidence and resist Tbl-like confusion |
| R012_A_protect | mod.blocks.0.attn | 6 | muon<-charged_hadron | LEPTON_READS_HADRON_ROUTE | 0.84918 | preserve Hqql evidence and resist Tbl-like confusion |
| R013_A_protect | mod.blocks.2.attn | 3 | neutral_hadron<-electron | HADRON_READS_LEPTON_ROUTE | 0.82581 | preserve Hqql evidence and resist Tbl-like confusion |
| R014_A_protect | mod.blocks.2.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.81026 | preserve Hqql evidence and resist Tbl-like confusion |
| R015_A_protect | mod.blocks.2.attn | 0 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.785 | preserve Hqql evidence and resist Tbl-like confusion |
| R016_A_protect | mod.blocks.1.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.78356 | preserve Hqql evidence and resist Tbl-like confusion |
| R017_A_protect | mod.blocks.5.attn | 1 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.78001 | preserve Hqql evidence and resist Tbl-like confusion |
| R018_A_protect | mod.blocks.3.attn | 1 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.7618 | preserve Hqql evidence and resist Tbl-like confusion |

### R001_A_protect `mod.blocks.5.attn#h1` `electron<-electron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.5.attn][1] reads electron <- electron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.5.attn, head=1, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.99932 B=0.00000 C=0.91066 D=0.85996 strength=0.99932

### R002_A_protect `mod.blocks.7.attn#h1` `muon<-muon`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.7.attn][1] reads muon <- muon: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.7.attn, head=1, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.97833 B=0.00000 C=0.90460 D=0.90545 strength=0.97833

### R003_A_protect `mod.blocks.7.attn#h5` `muon<-electron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.7.attn][5] reads muon <- electron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.7.attn, head=5, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.97671 B=0.00000 C=0.00000 D=0.51909 strength=0.97671

### R004_A_protect `mod.blocks.7.attn#h4` `electron<-electron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.7.attn][4] reads electron <- electron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.7.attn, head=4, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.96647 B=0.00000 C=0.99711 D=0.99259 strength=0.96647

### R005_A_protect `mod.blocks.6.attn#h4` `muon<-muon`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.6.attn][4] reads muon <- muon: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.6.attn, head=4, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.93515 B=0.00000 C=0.90974 D=0.83554 strength=0.93515

### R006_A_protect `mod.blocks.5.attn#h5` `muon<-electron`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.5.attn][5] reads muon <- electron: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.5.attn, head=5, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.90792 B=0.00000 C=0.00000 D=0.00000 strength=0.90792

### R007_A_protect `mod.blocks.7.attn#h5` `electron<-muon`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.7.attn][5] reads electron <- muon: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.7.attn, head=5, electron<-muon] := attention_weight * role_gate(electron,muon) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.88279 B=0.00000 C=0.00000 D=0.78840 strength=0.88279

### R008_A_protect `mod.blocks.5.attn#h6` `charged_hadron<-muon`

```text
IF group == A_Hqql_correct AND HEAD[mod.blocks.5.attn][6] reads charged_hadron <- muon: preserve Hqql evidence and resist Tbl-like confusion
ROUTE[mod.blocks.5.attn, head=6, charged_hadron<-muon] := attention_weight * role_gate(charged_hadron,muon) * class_regime(A_Hqql_correct)
```
- meaning: route is stronger in correct Hqql than in Hqql→Tbl mistakes
- A=0.87231 B=0.00000 C=0.66925 D=0.58538 strength=0.87231

## Anomaly rules

| rule | module | head | route | type | strength | action |
| --- | --- | --- | --- | --- | --- | --- |
| R001_anomaly | mod.blocks.7.attn | 4 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.96368 | mark nonstandard transition route |
| R002_anomaly | mod.blocks.4.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.91156 | mark nonstandard transition route |
| R003_anomaly | mod.blocks.5.attn | 1 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.91004 | mark nonstandard transition route |
| R004_anomaly | mod.blocks.7.attn | 1 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.88499 | mark nonstandard transition route |
| R005_anomaly | mod.blocks.6.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.85074 | mark nonstandard transition route |
| R006_anomaly | mod.blocks.5.attn | 1 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.72019 | mark nonstandard transition route |
| R007_anomaly | mod.blocks.5.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.71753 | mark nonstandard transition route |
| R008_anomaly | mod.blocks.6.attn | 6 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.68285 | mark nonstandard transition route |
| R009_anomaly | mod.blocks.5.attn | 7 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.66414 | mark nonstandard transition route |
| R010_anomaly | mod.blocks.6.attn | 6 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.63324 | mark nonstandard transition route |
| R011_anomaly | mod.blocks.3.attn | 5 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.60186 | mark nonstandard transition route |
| R012_anomaly | mod.blocks.7.attn | 6 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.59862 | mark nonstandard transition route |

### R001_anomaly `mod.blocks.7.attn#h4` `electron<-electron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.7.attn][4] reads electron <- electron: mark nonstandard transition route
ROUTE[mod.blocks.7.attn, head=4, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.96647 B=0.00000 C=0.99711 D=0.99259 strength=0.96368

### R002_anomaly `mod.blocks.4.attn#h4` `muon<-electron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.4.attn][4] reads muon <- electron: mark nonstandard transition route
ROUTE[mod.blocks.4.attn, head=4, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.00000 B=0.95476 C=0.00000 D=0.97434 strength=0.91156

### R003_anomaly `mod.blocks.5.attn#h1` `electron<-electron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.5.attn][1] reads electron <- electron: mark nonstandard transition route
ROUTE[mod.blocks.5.attn, head=1, electron<-electron] := attention_weight * role_gate(electron,electron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.99932 B=0.00000 C=0.91066 D=0.85996 strength=0.91004

### R004_anomaly `mod.blocks.7.attn#h1` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.7.attn][1] reads muon <- muon: mark nonstandard transition route
ROUTE[mod.blocks.7.attn, head=1, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.97833 B=0.00000 C=0.90460 D=0.90545 strength=0.88499

### R005_anomaly `mod.blocks.6.attn#h4` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.6.attn][4] reads muon <- muon: mark nonstandard transition route
ROUTE[mod.blocks.6.attn, head=4, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.93515 B=0.00000 C=0.90974 D=0.83554 strength=0.85074

### R006_anomaly `mod.blocks.5.attn#h1` `muon<-muon`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.5.attn][1] reads muon <- muon: mark nonstandard transition route
ROUTE[mod.blocks.5.attn, head=1, muon<-muon] := attention_weight * role_gate(muon,muon) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.78001 B=0.00000 C=0.92331 D=0.93508 strength=0.72019

### R007_anomaly `mod.blocks.5.attn#h4` `muon<-electron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.5.attn][4] reads muon <- electron: mark nonstandard transition route
ROUTE[mod.blocks.5.attn, head=4, muon<-electron] := attention_weight * role_gate(muon,electron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.00000 B=0.84707 C=0.00000 D=0.00000 strength=0.71753

### R008_anomaly `mod.blocks.6.attn#h6` `electron<-neutral_hadron`

```text
IF group == B_Hqql_to_Tbl_anomaly AND HEAD[mod.blocks.6.attn][6] reads electron <- neutral_hadron: mark nonstandard transition route
ROUTE[mod.blocks.6.attn, head=6, electron<-neutral_hadron] := attention_weight * role_gate(electron,neutral_hadron) * class_regime(B_Hqql_to_Tbl_anomaly)
```
- meaning: route separates mistake regime from both correct regimes
- A=0.86733 B=0.00000 C=0.78730 D=0.74315 strength=0.68285

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

