# PART_PAD_CONTROL_V1

Pad-control check for real-contract ParT Hqql/Tbl supertrace. This removes all paths where query or key role is `pad`, then re-ranks the strongest trigger/protection/anomaly paths.

- summary rows: **1845**
- pad-linked rows: **334**
- non-pad rows: **1511**

## Conclusion

- PASS: after removing pad-linked paths, the Hqql->Tbl trigger remains lepton-dominated.
- Pad paths are present but not dominant in top trigger paths.

## Top trigger tag counts before pad removal
| tag | count |
| --- | --- |
| lepton_lepton | 18 |
| lepton_reads_hadron | 3 |
| lepton_photon | 2 |
| photon_other | 1 |
| hadron_hadron | 1 |

## Top trigger tag counts after pad removal
| tag | count |
| --- | --- |
| lepton_lepton | 18 |
| lepton_reads_hadron | 3 |
| lepton_photon | 2 |
| photon_other | 1 |
| hadron_hadron | 1 |

## Top non-pad B>A trigger paths
| module | head | pair_role | tag | A | B | C | B-A |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.7.attn | 4 | muon<-muon | lepton_lepton | 0.0 | 0.99983 | 0.0 | 0.99983 |
| mod.blocks.6.attn | 0 | electron<-electron | lepton_lepton | 0.0 | 0.99959 | 0.81136 | 0.99959 |
| mod.blocks.7.attn | 4 | muon<-electron | lepton_lepton | 0.0 | 0.99689 | 0.0 | 0.99689 |
| mod.blocks.5.attn | 2 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.99519 | 0.8261 | 0.99519 |
| mod.blocks.7.attn | 0 | electron<-electron | lepton_lepton | 0.0 | 0.99463 | 0.80795 | 0.99463 |
| mod.blocks.7.attn | 6 | muon<-muon | lepton_lepton | 0.0 | 0.99142 | 0.0 | 0.99142 |
| mod.blocks.6.attn | 4 | electron<-electron | lepton_lepton | 0.0 | 0.98895 | 0.93771 | 0.98895 |
| mod.blocks.5.attn | 7 | muon<-muon | lepton_lepton | 0.0 | 0.98828 | 0.94345 | 0.98828 |
| mod.blocks.6.attn | 0 | photon<-neutral_hadron | photon_other | 0.0 | 0.98736 | 0.27819 | 0.98736 |
| mod.blocks.6.attn | 0 | muon<-electron | lepton_lepton | 0.0 | 0.9866 | 0.99476 | 0.9866 |
| mod.blocks.6.attn | 4 | muon<-muon | lepton_lepton | 0.0 | 0.97966 | 0.98974 | 0.97966 |
| mod.blocks.6.attn | 6 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.97259 | 0.94056 | 0.97259 |
| mod.blocks.4.attn | 5 | muon<-muon | lepton_lepton | 0.0 | 0.95269 | 0.7399 | 0.95269 |
| mod.blocks.6.attn | 0 | electron<-muon | lepton_lepton | 0.0 | 0.94817 | 0.83947 | 0.94817 |
| mod.blocks.7.attn | 2 | electron<-electron | lepton_lepton | 0.0 | 0.94389 | 0.96697 | 0.94389 |
| mod.blocks.5.attn | 6 | muon<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.92837 | 0.84282 | 0.92837 |
| mod.blocks.6.attn | 6 | muon<-muon | lepton_lepton | 0.0 | 0.92758 | 0.0 | 0.92758 |
| mod.blocks.6.attn | 6 | muon<-electron | lepton_lepton | 0.0 | 0.92455 | 0.0 | 0.92455 |
| mod.blocks.6.attn | 1 | muon<-muon | lepton_lepton | 0.0 | 0.91991 | 0.81577 | 0.91991 |
| mod.blocks.5.attn | 6 | muon<-photon | lepton_photon | 0.0 | 0.91873 | 0.78414 | 0.91873 |

## Top non-pad A>B protection paths
| module | head | pair_role | tag | A | B | C | A-B |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.7.attn | 3 | electron<-muon | lepton_lepton | 0.99912 | 0.0 | 0.92812 | 0.99912 |
| mod.blocks.2.attn | 3 | muon<-muon | lepton_lepton | 0.99357 | 0.0 | 0.63682 | 0.99357 |
| mod.blocks.6.attn | 5 | electron<-electron | lepton_lepton | 0.98862 | 0.0 | 0.0 | 0.98862 |
| mod.blocks.6.attn | 6 | muon<-neutral_hadron | lepton_reads_hadron | 0.98815 | 0.0 | 0.0 | 0.98815 |
| mod.blocks.3.attn | 5 | electron<-electron | lepton_lepton | 0.9877 | 0.0 | 0.59845 | 0.9877 |
| mod.blocks.7.attn | 0 | electron<-muon | lepton_lepton | 0.9767 | 0.0 | 0.0 | 0.9767 |
| mod.blocks.6.attn | 4 | neutral_hadron<-charged_hadron | hadron_hadron | 0.97475 | 0.0 | 0.57348 | 0.97475 |
| mod.blocks.6.attn | 4 | photon<-neutral_hadron | photon_other | 0.95746 | 0.0 | 0.0 | 0.95746 |
| mod.blocks.5.attn | 5 | electron<-electron | lepton_lepton | 0.95416 | 0.0 | 0.0 | 0.95416 |
| mod.blocks.6.attn | 4 | photon<-charged_hadron | photon_other | 0.94236 | 0.0 | 0.66166 | 0.94236 |
| mod.blocks.3.attn | 2 | electron<-neutral_hadron | lepton_reads_hadron | 0.94233 | 0.0 | 0.7996 | 0.94233 |
| mod.blocks.3.attn | 0 | electron<-electron | lepton_lepton | 0.9396 | 0.0 | 0.9704 | 0.9396 |
| mod.blocks.2.attn | 5 | electron<-electron | lepton_lepton | 0.91084 | 0.0 | 0.90462 | 0.91084 |
| mod.blocks.6.attn | 4 | charged_hadron<-neutral_hadron | hadron_hadron | 0.90792 | 0.0 | 0.0 | 0.90792 |
| mod.blocks.5.attn | 7 | photon<-neutral_hadron | photon_other | 0.89928 | 0.0 | 0.74939 | 0.89928 |
| mod.blocks.3.attn | 2 | neutral_hadron<-muon | hadron_reads_lepton | 0.89318 | 0.0 | 0.57561 | 0.89318 |
| mod.blocks.3.attn | 7 | electron<-charged_hadron | lepton_reads_hadron | 0.89187 | 0.0 | 0.55298 | 0.89187 |
| mod.blocks.2.attn | 1 | muon<-photon | lepton_photon | 0.85991 | 0.0 | 0.97964 | 0.85991 |
| mod.blocks.6.attn | 1 | muon<-photon | lepton_photon | 0.84336 | 0.0 | 0.88111 | 0.84336 |
| mod.blocks.2.attn | 1 | electron<-photon | lepton_photon | 0.84336 | 0.0 | 0.0 | 0.84336 |

## Top non-pad anomaly paths
| module | head | pair_role | tag | A | B | C | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.7.attn | 4 | muon<-muon | lepton_lepton | 0.0 | 0.99983 | 0.0 | 0.99966 |
| mod.blocks.7.attn | 4 | muon<-electron | lepton_lepton | 0.0 | 0.99689 | 0.0 | 0.99379 |
| mod.blocks.7.attn | 6 | muon<-muon | lepton_lepton | 0.0 | 0.99142 | 0.0 | 0.98291 |
| mod.blocks.7.attn | 3 | electron<-muon | lepton_lepton | 0.99912 | 0.0 | 0.92812 | 0.9273 |
| mod.blocks.3.attn | 0 | electron<-electron | lepton_lepton | 0.9396 | 0.0 | 0.9704 | 0.91179 |
| mod.blocks.6.attn | 6 | muon<-muon | lepton_lepton | 0.0 | 0.92758 | 0.0 | 0.8604 |
| mod.blocks.6.attn | 6 | muon<-electron | lepton_lepton | 0.0 | 0.92455 | 0.0 | 0.85479 |
| mod.blocks.4.attn | 0 | muon<-electron | lepton_lepton | 0.0 | 0.91851 | 0.0 | 0.84365 |
| mod.blocks.2.attn | 1 | muon<-photon | lepton_photon | 0.85991 | 0.0 | 0.97964 | 0.8424 |
| mod.blocks.2.attn | 5 | electron<-electron | lepton_lepton | 0.91084 | 0.0 | 0.90462 | 0.82396 |
| mod.blocks.3.attn | 2 | electron<-neutral_hadron | lepton_reads_hadron | 0.94233 | 0.0 | 0.7996 | 0.75348 |
| mod.blocks.4.attn | 3 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.86759 | 0.0 | 0.75272 |
| mod.blocks.6.attn | 1 | muon<-photon | lepton_photon | 0.84336 | 0.0 | 0.88111 | 0.7431 |
| mod.blocks.6.attn | 6 | neutral_hadron<-muon | hadron_reads_lepton | 0.82598 | 0.0 | 0.8916 | 0.73645 |
| mod.blocks.2.attn | 5 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.8478 | 0.0 | 0.71877 |
| mod.blocks.6.attn | 0 | photon<-neutral_hadron | photon_other | 0.0 | 0.98736 | 0.27819 | 0.70021 |
| mod.blocks.0.attn | 2 | muon<-electron | lepton_lepton | 0.0 | 0.82742 | 0.0 | 0.68462 |
| mod.blocks.5.attn | 7 | photon<-neutral_hadron | photon_other | 0.89928 | 0.0 | 0.74939 | 0.67391 |
| mod.blocks.3.attn | 5 | electron<-neutral_hadron | lepton_reads_hadron | 0.0 | 0.82035 | 0.0 | 0.67297 |
| mod.blocks.6.attn | 2 | electron<-neutral_hadron | lepton_reads_hadron | 0.72718 | 0.0 | 0.87937 | 0.63947 |

