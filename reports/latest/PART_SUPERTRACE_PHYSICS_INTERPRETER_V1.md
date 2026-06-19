# PART_SUPERTRACE_PHYSICS_INTERPRETER_V1

Automatic interpretation of the real-contract ParT Hqql/Tbl attention supertrace.

- summary rows: **1891**
- traced events: **1024**
- pair rows: **327680**
- data_config: `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`
- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`

## Main hypothesis

- B_Hqql_to_Tbl trigger is dominated by lepton-linked attention paths. The Hqql→Tbl confusion likely appears when the ParT representation routes semileptonic H→WW evidence into a top-leptonic-like lepton topology.
- A_Hqql_correct protection also uses lepton-lepton paths, but in different heads/layers. This suggests the same particle roles are used with different routing semantics, not simply presence/absence of leptons.
- Several top paths include pad. Treat pad-linked paths as a detector/sparsity or masking signal until verified by controls; they may still be meaningful because particle multiplicity is physical, but they require a mask-control test.
- The highest trigger concentration is in late ParT blocks: mod.blocks.6.attn(9), mod.blocks.7.attn(4), mod.blocks.3.attn(4), mod.blocks.4.attn(3).
- The highest Hqql-correct protection concentration is in: mod.blocks.5.attn(6), mod.blocks.7.attn(5), mod.blocks.2.attn(5), mod.blocks.6.attn(4).

## Trigger B>A tag counts
| tag | count |
| --- | --- |
| lepton_lepton_correlation | 12 |
| lepton_photon_correlation | 3 |
| pad_artifact_or_sparse_particle_pattern | 3 |
| hadron_reads_lepton | 3 |
| photon_hadron_topology | 2 |
| hadron_hadron_topology | 1 |
| lepton_reads_hadron | 1 |

## Hqql-correct A>B tag counts
| tag | count |
| --- | --- |
| lepton_lepton_correlation | 15 |
| hadron_reads_lepton | 4 |
| pad_artifact_or_sparse_particle_pattern | 3 |
| lepton_reads_hadron | 2 |
| hadron_hadron_topology | 1 |

## Anomaly tag counts
| tag | count |
| --- | --- |
| lepton_lepton_correlation | 12 |
| hadron_reads_lepton | 5 |
| pad_artifact_or_sparse_particle_pattern | 3 |
| lepton_reads_hadron | 2 |
| lepton_photon_correlation | 2 |
| hadron_hadron_topology | 1 |

## Top trigger paths: B_Hqql_to_Tbl stronger than A_Hqql_correct
| module | head | pair_role | tag | A | B | C | B-A |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.7.attn | 4 | electron<-muon | lepton_lepton_correlation | 0.0 | 0.99492 | 0.99739 | 0.99492 |
| mod.blocks.6.attn | 4 | muon<-photon | lepton_photon_correlation | 0.0 | 0.97246 | 0.74121 | 0.97246 |
| mod.blocks.1.attn | 1 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.95715 | 0.9439 | 0.95715 |
| mod.blocks.4.attn | 4 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.95476 | 0.0 | 0.95476 |
| mod.blocks.7.attn | 5 | electron<-electron | lepton_lepton_correlation | 0.0 | 0.91416 | 0.41317 | 0.91416 |
| mod.blocks.6.attn | 0 | pad<-neutral_hadron | pad_artifact_or_sparse_particle_pattern | 0.0 | 0.90578 | 0.0 | 0.90578 |
| mod.blocks.3.attn | 6 | pad<-charged_hadron | pad_artifact_or_sparse_particle_pattern | 0.0 | 0.85074 | 0.63239 | 0.85074 |
| mod.blocks.5.attn | 4 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.84707 | 0.0 | 0.84707 |
| mod.blocks.5.attn | 6 | photon<-muon | lepton_photon_correlation | 0.0 | 0.83968 | 0.95644 | 0.83968 |
| mod.blocks.6.attn | 6 | neutral_hadron<-neutral_hadron | hadron_hadron_topology | 0.0 | 0.8375 | 0.85019 | 0.8375 |
| mod.blocks.6.attn | 0 | electron<-muon | lepton_lepton_correlation | 0.0 | 0.82479 | 0.78712 | 0.82479 |
| mod.blocks.4.attn | 4 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.81415 | 0.66542 | 0.81415 |
| mod.blocks.6.attn | 4 | photon<-charged_hadron | photon_hadron_topology | 0.0 | 0.79398 | 0.63594 | 0.79398 |
| mod.blocks.3.attn | 2 | charged_hadron<-muon | hadron_reads_lepton | 0.0 | 0.77901 | 0.64003 | 0.77901 |
| mod.blocks.3.attn | 5 | neutral_hadron<-muon | hadron_reads_lepton | 0.0 | 0.7758 | 0.0 | 0.7758 |
| mod.blocks.5.attn | 7 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.77521 | 0.84613 | 0.77521 |
| mod.blocks.7.attn | 6 | neutral_hadron<-muon | hadron_reads_lepton | 0.0 | 0.77371 | 0.0 | 0.77371 |
| mod.blocks.6.attn | 6 | muon<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.76327 | 0.0 | 0.76327 |
| mod.blocks.2.attn | 6 | pad<-photon | pad_artifact_or_sparse_particle_pattern | 0.0 | 0.75595 | 0.34616 | 0.75595 |
| mod.blocks.6.attn | 2 | electron<-electron | lepton_lepton_correlation | 0.0 | 0.73291 | 0.64568 | 0.73291 |

## Top protection/loss paths: A_Hqql_correct stronger than B_Hqql_to_Tbl
| module | head | pair_role | tag | A | B | C | A-B |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.5.attn | 1 | electron<-electron | lepton_lepton_correlation | 0.99932 | 0.0 | 0.91066 | 0.99932 |
| mod.blocks.7.attn | 2 | pad<-electron | pad_artifact_or_sparse_particle_pattern | 0.97871 | 0.0 | 0.67414 | 0.97871 |
| mod.blocks.7.attn | 1 | muon<-muon | lepton_lepton_correlation | 0.97833 | 0.0 | 0.9046 | 0.97833 |
| mod.blocks.7.attn | 5 | muon<-electron | lepton_lepton_correlation | 0.97671 | 0.0 | 0.0 | 0.97671 |
| mod.blocks.7.attn | 4 | electron<-electron | lepton_lepton_correlation | 0.96647 | 0.0 | 0.99711 | 0.96647 |
| mod.blocks.4.attn | 4 | pad<-electron | pad_artifact_or_sparse_particle_pattern | 0.94351 | 0.0 | 0.0 | 0.94351 |
| mod.blocks.6.attn | 4 | muon<-muon | lepton_lepton_correlation | 0.93515 | 0.0 | 0.90974 | 0.93515 |
| mod.blocks.6.attn | 4 | pad<-electron | pad_artifact_or_sparse_particle_pattern | 0.91212 | 0.0 | 0.0 | 0.91212 |
| mod.blocks.5.attn | 5 | muon<-electron | lepton_lepton_correlation | 0.90792 | 0.0 | 0.0 | 0.90792 |
| mod.blocks.7.attn | 5 | electron<-muon | lepton_lepton_correlation | 0.88279 | 0.0 | 0.0 | 0.88279 |
| mod.blocks.5.attn | 6 | charged_hadron<-muon | hadron_reads_lepton | 0.87231 | 0.0 | 0.66925 | 0.87231 |
| mod.blocks.6.attn | 5 | muon<-electron | lepton_lepton_correlation | 0.8719 | 0.0 | 0.62484 | 0.8719 |
| mod.blocks.6.attn | 6 | electron<-neutral_hadron | lepton_reads_hadron | 0.86733 | 0.0 | 0.7873 | 0.86733 |
| mod.blocks.5.attn | 6 | charged_hadron<-electron | hadron_reads_lepton | 0.85955 | 0.0 | 0.63717 | 0.85955 |
| mod.blocks.0.attn | 6 | muon<-charged_hadron | lepton_reads_hadron | 0.84918 | 0.0 | 0.44765 | 0.84918 |
| mod.blocks.2.attn | 3 | neutral_hadron<-electron | hadron_reads_lepton | 0.82581 | 0.0 | 0.60567 | 0.82581 |
| mod.blocks.2.attn | 4 | muon<-electron | lepton_lepton_correlation | 0.81026 | 0.0 | 0.7175 | 0.81026 |
| mod.blocks.2.attn | 0 | electron<-electron | lepton_lepton_correlation | 0.785 | 0.0 | 0.22663 | 0.785 |
| mod.blocks.1.attn | 4 | muon<-muon | lepton_lepton_correlation | 0.78356 | 0.0 | 0.45438 | 0.78356 |
| mod.blocks.5.attn | 1 | muon<-muon | lepton_lepton_correlation | 0.78001 | 0.0 | 0.92331 | 0.78001 |

## Top anomaly paths
| module | head | pair_role | tag | A | B | C | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.7.attn | 4 | electron<-electron | lepton_lepton_correlation | 0.96647 | 0.0 | 0.99711 | 0.96368 |
| mod.blocks.4.attn | 4 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.95476 | 0.0 | 0.91156 |
| mod.blocks.5.attn | 1 | electron<-electron | lepton_lepton_correlation | 0.99932 | 0.0 | 0.91066 | 0.91004 |
| mod.blocks.7.attn | 1 | muon<-muon | lepton_lepton_correlation | 0.97833 | 0.0 | 0.9046 | 0.88499 |
| mod.blocks.6.attn | 4 | muon<-muon | lepton_lepton_correlation | 0.93515 | 0.0 | 0.90974 | 0.85074 |
| mod.blocks.6.attn | 0 | pad<-neutral_hadron | pad_artifact_or_sparse_particle_pattern | 0.0 | 0.90578 | 0.0 | 0.82045 |
| mod.blocks.5.attn | 1 | muon<-muon | lepton_lepton_correlation | 0.78001 | 0.0 | 0.92331 | 0.72019 |
| mod.blocks.5.attn | 4 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.84707 | 0.0 | 0.71753 |
| mod.blocks.6.attn | 6 | electron<-neutral_hadron | lepton_reads_hadron | 0.86733 | 0.0 | 0.7873 | 0.68285 |
| mod.blocks.5.attn | 7 | muon<-muon | lepton_lepton_correlation | 0.75266 | 0.0 | 0.88239 | 0.66414 |
| mod.blocks.7.attn | 2 | pad<-electron | pad_artifact_or_sparse_particle_pattern | 0.97871 | 0.0 | 0.67414 | 0.65979 |
| mod.blocks.6.attn | 6 | muon<-muon | lepton_lepton_correlation | 0.66232 | 0.0 | 0.95609 | 0.63324 |
| mod.blocks.3.attn | 5 | neutral_hadron<-muon | hadron_reads_lepton | 0.0 | 0.7758 | 0.0 | 0.60186 |
| mod.blocks.7.attn | 6 | neutral_hadron<-muon | hadron_reads_lepton | 0.0 | 0.77371 | 0.0 | 0.59862 |
| mod.blocks.5.attn | 6 | charged_hadron<-muon | hadron_reads_lepton | 0.87231 | 0.0 | 0.66925 | 0.58379 |
| mod.blocks.6.attn | 6 | muon<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.76327 | 0.0 | 0.58258 |
| mod.blocks.2.attn | 4 | muon<-electron | lepton_lepton_correlation | 0.81026 | 0.0 | 0.7175 | 0.58136 |
| mod.blocks.5.attn | 6 | charged_hadron<-electron | hadron_reads_lepton | 0.85955 | 0.0 | 0.63717 | 0.54768 |
| mod.blocks.6.attn | 5 | muon<-electron | lepton_lepton_correlation | 0.8719 | 0.0 | 0.62484 | 0.54479 |
| mod.blocks.3.attn | 2 | electron<-electron | lepton_lepton_correlation | 0.71602 | 0.0 | 0.7411 | 0.53064 |

## Next tests

1. Mask-control test for pad-linked paths.
2. Lepton-ablation patch on top trigger heads.
3. Compare Hqql/Tbl against WToQQ and TTBar to separate generic lepton routing from top-specific routing.
4. Promote stable top heads into pseudocode rules.

## Validity

This report reads `part_attention_path_summary_real_contract_v1.csv`, which came from real `DataConfig.load(...)` and strict checkpoint loading.
