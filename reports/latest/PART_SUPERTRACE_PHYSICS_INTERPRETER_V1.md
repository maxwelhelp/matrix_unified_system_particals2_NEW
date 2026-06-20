# PART_SUPERTRACE_PHYSICS_INTERPRETER_V1

Automatic interpretation of the real-contract ParT Hqql/Tbl attention supertrace.

- summary rows: **1845**
- traced events: **1024**
- pair rows: **327680**
- data_config: `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`
- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`

## Main hypothesis

- B_Hqql_to_Tbl trigger is dominated by lepton-linked attention paths. The Hqql→Tbl confusion likely appears when the ParT representation routes semileptonic H→WW evidence into a top-leptonic-like lepton topology.
- A_Hqql_correct protection also uses lepton-lepton paths, but in different heads/layers. This suggests the same particle roles are used with different routing semantics, not simply presence/absence of leptons.
- Several top paths include pad. Treat pad-linked paths as a detector/sparsity or masking signal until verified by controls; they may still be meaningful because particle multiplicity is physical, but they require a mask-control test.
- The highest trigger concentration is in late ParT blocks: mod.blocks.6.attn(10), mod.blocks.7.attn(6), mod.blocks.5.attn(6), mod.blocks.4.attn(3).
- The highest Hqql-correct protection concentration is in: mod.blocks.6.attn(7), mod.blocks.3.attn(6), mod.blocks.7.attn(4), mod.blocks.2.attn(4).

## Trigger B>A tag counts
| tag | count |
| --- | --- |
| lepton_lepton_correlation | 18 |
| lepton_reads_hadron | 3 |
| lepton_photon_correlation | 2 |
| photon_hadron_topology | 1 |
| hadron_hadron_topology | 1 |

## Hqql-correct A>B tag counts
| tag | count |
| --- | --- |
| lepton_lepton_correlation | 8 |
| lepton_reads_hadron | 5 |
| hadron_hadron_topology | 3 |
| photon_hadron_topology | 3 |
| lepton_photon_correlation | 3 |
| pad_artifact_or_sparse_particle_pattern | 2 |
| hadron_reads_lepton | 1 |

## Anomaly tag counts
| tag | count |
| --- | --- |
| lepton_lepton_correlation | 12 |
| lepton_reads_hadron | 5 |
| photon_hadron_topology | 3 |
| lepton_photon_correlation | 2 |
| pad_artifact_or_sparse_particle_pattern | 1 |
| hadron_reads_lepton | 1 |
| hadron_hadron_topology | 1 |

## Top trigger paths: B_Hqql_to_Tbl stronger than A_Hqql_correct
| module | head | pair_role | tag | A | B | C | B-A |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.7.attn | 4 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.99983 | 0.0 | 0.99983 |
| mod.blocks.6.attn | 0 | electron<-electron | lepton_lepton_correlation | 0.0 | 0.99959 | 0.81136 | 0.99959 |
| mod.blocks.7.attn | 4 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.99689 | 0.0 | 0.99689 |
| mod.blocks.5.attn | 2 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.99519 | 0.8261 | 0.99519 |
| mod.blocks.7.attn | 0 | electron<-electron | lepton_lepton_correlation | 0.0 | 0.99463 | 0.80795 | 0.99463 |
| mod.blocks.7.attn | 6 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.99142 | 0.0 | 0.99142 |
| mod.blocks.6.attn | 4 | electron<-electron | lepton_lepton_correlation | 0.0 | 0.98895 | 0.93771 | 0.98895 |
| mod.blocks.5.attn | 7 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.98828 | 0.94345 | 0.98828 |
| mod.blocks.6.attn | 0 | photon<-neutral_hadron | photon_hadron_topology | 0.0 | 0.98736 | 0.27819 | 0.98736 |
| mod.blocks.6.attn | 0 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.9866 | 0.99476 | 0.9866 |
| mod.blocks.6.attn | 4 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.97966 | 0.98974 | 0.97966 |
| mod.blocks.6.attn | 6 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.97259 | 0.94056 | 0.97259 |
| mod.blocks.4.attn | 5 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.95269 | 0.7399 | 0.95269 |
| mod.blocks.6.attn | 0 | electron<-muon | lepton_lepton_correlation | 0.0 | 0.94817 | 0.83947 | 0.94817 |
| mod.blocks.7.attn | 2 | electron<-electron | lepton_lepton_correlation | 0.0 | 0.94389 | 0.96697 | 0.94389 |
| mod.blocks.5.attn | 6 | muon<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.92837 | 0.84282 | 0.92837 |
| mod.blocks.6.attn | 6 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.92758 | 0.0 | 0.92758 |
| mod.blocks.6.attn | 6 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.92455 | 0.0 | 0.92455 |
| mod.blocks.6.attn | 1 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.91991 | 0.81577 | 0.91991 |
| mod.blocks.5.attn | 6 | muon<-photon | lepton_photon_correlation | 0.0 | 0.91873 | 0.78414 | 0.91873 |

## Top protection/loss paths: A_Hqql_correct stronger than B_Hqql_to_Tbl
| module | head | pair_role | tag | A | B | C | A-B |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.7.attn | 3 | electron<-muon | lepton_lepton_correlation | 0.99912 | 0.0 | 0.92812 | 0.99912 |
| mod.blocks.2.attn | 3 | muon<-muon | lepton_lepton_correlation | 0.99357 | 0.0 | 0.63682 | 0.99357 |
| mod.blocks.6.attn | 5 | electron<-electron | lepton_lepton_correlation | 0.98862 | 0.0 | 0.0 | 0.98862 |
| mod.blocks.6.attn | 6 | muon<-neutral_hadron | lepton_reads_hadron | 0.98815 | 0.0 | 0.0 | 0.98815 |
| mod.blocks.3.attn | 5 | electron<-electron | lepton_lepton_correlation | 0.9877 | 0.0 | 0.59845 | 0.9877 |
| mod.blocks.7.attn | 0 | electron<-muon | lepton_lepton_correlation | 0.9767 | 0.0 | 0.0 | 0.9767 |
| mod.blocks.6.attn | 4 | neutral_hadron<-charged_hadron | hadron_hadron_topology | 0.97475 | 0.0 | 0.57348 | 0.97475 |
| mod.blocks.6.attn | 4 | photon<-neutral_hadron | photon_hadron_topology | 0.95746 | 0.0 | 0.0 | 0.95746 |
| mod.blocks.5.attn | 5 | electron<-electron | lepton_lepton_correlation | 0.95416 | 0.0 | 0.0 | 0.95416 |
| mod.blocks.6.attn | 4 | photon<-charged_hadron | photon_hadron_topology | 0.94236 | 0.0 | 0.66166 | 0.94236 |
| mod.blocks.3.attn | 2 | electron<-neutral_hadron | lepton_reads_hadron | 0.94233 | 0.0 | 0.7996 | 0.94233 |
| mod.blocks.3.attn | 0 | electron<-electron | lepton_lepton_correlation | 0.9396 | 0.0 | 0.9704 | 0.9396 |
| mod.blocks.7.attn | 4 | pad<-charged_hadron | pad_artifact_or_sparse_particle_pattern | 0.93613 | 0.0 | 0.97741 | 0.93613 |
| mod.blocks.2.attn | 5 | electron<-electron | lepton_lepton_correlation | 0.91084 | 0.0 | 0.90462 | 0.91084 |
| mod.blocks.6.attn | 4 | charged_hadron<-neutral_hadron | hadron_hadron_topology | 0.90792 | 0.0 | 0.0 | 0.90792 |
| mod.blocks.5.attn | 7 | photon<-neutral_hadron | photon_hadron_topology | 0.89928 | 0.0 | 0.74939 | 0.89928 |
| mod.blocks.3.attn | 2 | neutral_hadron<-muon | hadron_reads_lepton | 0.89318 | 0.0 | 0.57561 | 0.89318 |
| mod.blocks.3.attn | 7 | electron<-charged_hadron | lepton_reads_hadron | 0.89187 | 0.0 | 0.55298 | 0.89187 |
| mod.blocks.0.attn | 7 | pad<-neutral_hadron | pad_artifact_or_sparse_particle_pattern | 0.87012 | 0.0 | 0.0 | 0.87012 |
| mod.blocks.2.attn | 1 | muon<-photon | lepton_photon_correlation | 0.85991 | 0.0 | 0.97964 | 0.85991 |

## Top anomaly paths
| module | head | pair_role | tag | A | B | C | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.7.attn | 4 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.99983 | 0.0 | 0.99966 |
| mod.blocks.7.attn | 4 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.99689 | 0.0 | 0.99379 |
| mod.blocks.7.attn | 6 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.99142 | 0.0 | 0.98291 |
| mod.blocks.7.attn | 3 | electron<-muon | lepton_lepton_correlation | 0.99912 | 0.0 | 0.92812 | 0.9273 |
| mod.blocks.7.attn | 4 | pad<-charged_hadron | pad_artifact_or_sparse_particle_pattern | 0.93613 | 0.0 | 0.97741 | 0.91498 |
| mod.blocks.3.attn | 0 | electron<-electron | lepton_lepton_correlation | 0.9396 | 0.0 | 0.9704 | 0.91179 |
| mod.blocks.6.attn | 6 | muon<-muon | lepton_lepton_correlation | 0.0 | 0.92758 | 0.0 | 0.8604 |
| mod.blocks.6.attn | 6 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.92455 | 0.0 | 0.85479 |
| mod.blocks.4.attn | 0 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.91851 | 0.0 | 0.84365 |
| mod.blocks.2.attn | 1 | muon<-photon | lepton_photon_correlation | 0.85991 | 0.0 | 0.97964 | 0.8424 |
| mod.blocks.2.attn | 5 | electron<-electron | lepton_lepton_correlation | 0.91084 | 0.0 | 0.90462 | 0.82396 |
| mod.blocks.3.attn | 2 | electron<-neutral_hadron | lepton_reads_hadron | 0.94233 | 0.0 | 0.7996 | 0.75348 |
| mod.blocks.4.attn | 3 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.86759 | 0.0 | 0.75272 |
| mod.blocks.6.attn | 1 | muon<-photon | lepton_photon_correlation | 0.84336 | 0.0 | 0.88111 | 0.7431 |
| mod.blocks.6.attn | 6 | neutral_hadron<-muon | hadron_reads_lepton | 0.82598 | 0.0 | 0.8916 | 0.73645 |
| mod.blocks.2.attn | 5 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.8478 | 0.0 | 0.71877 |
| mod.blocks.6.attn | 0 | photon<-neutral_hadron | photon_hadron_topology | 0.0 | 0.98736 | 0.27819 | 0.70021 |
| mod.blocks.0.attn | 2 | muon<-electron | lepton_lepton_correlation | 0.0 | 0.82742 | 0.0 | 0.68462 |
| mod.blocks.5.attn | 7 | photon<-neutral_hadron | photon_hadron_topology | 0.89928 | 0.0 | 0.74939 | 0.67391 |
| mod.blocks.3.attn | 5 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.82035 | 0.0 | 0.67297 |

## Next tests

1. Mask-control test for pad-linked paths.
2. Lepton-ablation patch on top trigger heads.
3. Compare Hqql/Tbl against WToQQ and TTBar to separate generic lepton routing from top-specific routing.
4. Promote stable top heads into pseudocode rules.

## Validity

This report reads `part_attention_path_summary_real_contract_v1.csv`, which came from real `DataConfig.load(...)` and strict checkpoint loading.
