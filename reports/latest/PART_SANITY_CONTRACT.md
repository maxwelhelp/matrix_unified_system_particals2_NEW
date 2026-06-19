# PART_SANITY_CONTRACT

- created_at: `2026-06-20T00:07:08`
- network: `external/particle_transformer/networks/example_ParticleTransformer.py`

## Mode contract
| mode | ok | pf_features_n | strict_load | missing | unexpected | errors |
| --- | --- | ---: | --- | ---: | ---: | --- |
| full | True | 17 | True | 0 | 0 |  |
| kinpid | True | 13 | True | 0 | 0 |  |

## Features
### full

- yaml: `external/particle_transformer/data/JetClass/JetClass_full.yaml`
- checkpoint: `external/particle_transformer/models/ParT_full.pt`
- ok: `True`
- pf_features:
  - `part_pt_log`
  - `part_e_log`
  - `part_logptrel`
  - `part_logerel`
  - `part_deltaR`
  - `part_charge`
  - `part_isChargedHadron`
  - `part_isNeutralHadron`
  - `part_isPhoton`
  - `part_isElectron`
  - `part_isMuon`
  - `part_d0`
  - `part_d0err`
  - `part_dz`
  - `part_dzerr`
  - `part_deta`
  - `part_dphi`

### kinpid

- yaml: `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`
- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`
- ok: `True`
- pf_features:
  - `part_pt_log`
  - `part_e_log`
  - `part_logptrel`
  - `part_logerel`
  - `part_deltaR`
  - `part_charge`
  - `part_isChargedHadron`
  - `part_isNeutralHadron`
  - `part_isPhoton`
  - `part_isElectron`
  - `part_isMuon`
  - `part_deta`
  - `part_dphi`

## Supertrace notes

- WARNING: supertrace appears to contain a fake hardcoded 17-feature DataConfig. Use it for attention hooks only until it is migrated to real YAML/DataConfig input construction.
- event_to_arrays exists; verify it uses the same mode/YAML/checkpoint contract before trusting direct-gate predictions.

## Decision

`CONTRACT_OK`: all requested modes strict-load successfully. Next step: validate prediction outputs before interpretation.
