# PART_ATTENTION_SUPERTRACE_V1

Full ParT top-K attention-pair supertrace over A/B/C/D groups. Saves top-K pairs per attention module/head/event, then ranks trigger/loss/anomaly paths.

- events traced: **14000**
- pair rows: **8960000**
- summary rows: **2017**
- topk per head: **8**

## Input counts
| group | available/selected |
| --- | --- |
| A_Hqql_correct | 25694 |
| B_Hqql_to_Tbl | 4577 |
| C_Tbl_correct | 14533 |
| D_Tbl_to_Hqql | 6443 |

## Top B>A trigger paths
| module | head | pair_role | A | B | C | B-A |
| --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.6.attn | 0 | muon<-electron | 0.0 | 0.66189 | 0.63061 | 0.66189 |
| mod.blocks.1.attn | 0 | muon<-muon | 0.0 | 0.64012 | 0.755 | 0.64012 |
| mod.blocks.1.attn | 6 | electron<-muon | 0.0 | 0.56519 | 0.43575 | 0.56519 |
| mod.blocks.5.attn | 6 | electron<-neutral_hadron | 0.0 | 0.54112 | 0.48447 | 0.54112 |
| mod.blocks.7.attn | 4 | electron<-muon | 0.0 | 0.52242 | 0.61052 | 0.52242 |
| mod.blocks.1.attn | 6 | muon<-electron | 0.0 | 0.46381 | 0.41307 | 0.46381 |
| mod.blocks.0.attn | 5 | pad<-charged_hadron | 0.0 | 0.43156 | 0.31358 | 0.43156 |
| mod.blocks.1.attn | 2 | muon<-muon | 0.41268 | 0.84122 | 0.65964 | 0.42854 |
| mod.blocks.0.attn | 2 | pad<-muon | 0.0 | 0.4173 | 0.0 | 0.4173 |
| mod.blocks.0.attn | 0 | pad<-charged_hadron | 0.0 | 0.34482 | 0.0 | 0.34482 |
| mod.blocks.5.attn | 3 | electron<-neutral_hadron | 0.24497 | 0.58473 | 0.0 | 0.33976 |
| mod.blocks.0.attn | 7 | pad<-charged_hadron | 0.0 | 0.32755 | 0.0 | 0.32755 |
| mod.blocks.0.attn | 1 | pad<-neutral_hadron | 0.0 | 0.31444 | 0.0 | 0.31444 |
| mod.blocks.0.attn | 7 | pad<-neutral_hadron | 0.0 | 0.30848 | 0.0 | 0.30848 |
| mod.blocks.0.attn | 6 | pad<-photon | 0.0 | 0.30534 | 0.0 | 0.30534 |
| mod.blocks.6.attn | 3 | muon<-electron | 0.41588 | 0.71686 | 0.91447 | 0.30098 |
| mod.blocks.0.attn | 1 | pad<-photon | 0.0 | 0.29816 | 0.2062 | 0.29816 |
| mod.blocks.0.attn | 7 | pad<-photon | 0.0 | 0.29089 | 0.0 | 0.29089 |
| mod.blocks.4.attn | 3 | electron<-neutral_hadron | 0.34968 | 0.6249 | 0.0 | 0.27522 |
| mod.blocks.2.attn | 2 | muon<-muon | 0.64333 | 0.91676 | 0.89485 | 0.27343 |

## Top A>B Hqql-loss paths
| module | head | pair_role | A | B | C | A-B |
| --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.6.attn | 4 | electron<-muon | 0.88124 | 0.0 | 0.85836 | 0.88124 |
| mod.blocks.4.attn | 4 | electron<-muon | 0.84285 | 0.0 | 0.74255 | 0.84285 |
| mod.blocks.7.attn | 5 | electron<-muon | 0.78312 | 0.0 | 0.0 | 0.78312 |
| mod.blocks.2.attn | 4 | muon<-electron | 0.78027 | 0.0 | 0.75396 | 0.78027 |
| mod.blocks.6.attn | 5 | muon<-muon | 0.77841 | 0.0 | 0.6549 | 0.77841 |
| mod.blocks.4.attn | 4 | muon<-electron | 0.77323 | 0.0 | 0.75152 | 0.77323 |
| mod.blocks.7.attn | 4 | muon<-electron | 0.69534 | 0.0 | 0.61652 | 0.69534 |
| mod.cls_blocks.1.attn | 3 | CLS<-CLS | 0.69467 | 0.0 | 0.0 | 0.69467 |
| mod.blocks.7.attn | 4 | muon<-muon | 0.69134 | 0.0 | 0.5741 | 0.69134 |
| mod.blocks.6.attn | 6 | muon<-muon | 0.67817 | 0.0 | 0.92329 | 0.67817 |
| mod.blocks.4.attn | 5 | electron<-muon | 0.66592 | 0.0 | 0.51727 | 0.66592 |
| mod.blocks.5.attn | 4 | muon<-muon | 0.66397 | 0.0 | 0.66821 | 0.66397 |
| mod.blocks.5.attn | 5 | muon<-muon | 0.66248 | 0.0 | 0.66238 | 0.66248 |
| mod.blocks.5.attn | 6 | muon<-neutral_hadron | 0.64652 | 0.0 | 0.52423 | 0.64652 |
| mod.blocks.1.attn | 2 | electron<-muon | 0.63276 | 0.0 | 0.66463 | 0.63276 |
| mod.blocks.1.attn | 6 | muon<-muon | 0.62775 | 0.0 | 0.53168 | 0.62775 |
| mod.cls_blocks.1.attn | 6 | CLS<-CLS | 0.61499 | 0.0 | 0.0 | 0.61499 |
| mod.cls_blocks.1.attn | 5 | CLS<-CLS | 0.60456 | 0.0 | 0.0 | 0.60456 |
| mod.blocks.0.attn | 5 | muon<-electron | 0.60371 | 0.0 | 0.68627 | 0.60371 |
| mod.blocks.4.attn | 7 | muon<-muon | 0.59707 | 0.0 | 0.75415 | 0.59707 |

## Top anomaly paths B!=A and B!=C
| module | head | pair_role | A | B | C | score |
| --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.6.attn | 4 | electron<-muon | 0.88124 | 0.0 | 0.85836 | 0.75641 |
| mod.blocks.6.attn | 6 | muon<-muon | 0.67817 | 0.0 | 0.92329 | 0.62615 |
| mod.blocks.4.attn | 4 | electron<-muon | 0.84285 | 0.0 | 0.74255 | 0.62586 |
| mod.blocks.2.attn | 4 | muon<-electron | 0.78027 | 0.0 | 0.75396 | 0.58829 |
| mod.blocks.4.attn | 4 | muon<-electron | 0.77323 | 0.0 | 0.75152 | 0.58109 |
| mod.blocks.6.attn | 5 | muon<-muon | 0.77841 | 0.0 | 0.6549 | 0.50978 |
| mod.blocks.6.attn | 2 | muon<-muon | 0.58676 | 0.0 | 0.83306 | 0.4888 |
| mod.blocks.4.attn | 7 | muon<-muon | 0.59707 | 0.0 | 0.75415 | 0.45028 |
| mod.blocks.5.attn | 4 | muon<-muon | 0.66397 | 0.0 | 0.66821 | 0.44367 |
| mod.blocks.5.attn | 5 | muon<-muon | 0.66248 | 0.0 | 0.66238 | 0.43881 |
| mod.blocks.7.attn | 4 | muon<-electron | 0.69534 | 0.0 | 0.61652 | 0.42869 |
| mod.blocks.1.attn | 2 | electron<-muon | 0.63276 | 0.0 | 0.66463 | 0.42055 |
| mod.blocks.0.attn | 5 | muon<-electron | 0.60371 | 0.0 | 0.68627 | 0.4143 |
| mod.blocks.5.attn | 5 | muon<-electron | 0.58722 | 0.0 | 0.68995 | 0.40515 |
| mod.blocks.7.attn | 4 | muon<-muon | 0.69134 | 0.0 | 0.5741 | 0.3969 |
| mod.blocks.0.attn | 2 | muon<-electron | 0.58142 | 0.0 | 0.68024 | 0.3955 |
| mod.blocks.6.attn | 0 | muon<-muon | 0.56635 | 0.0 | 0.65504 | 0.37098 |
| mod.blocks.4.attn | 5 | electron<-muon | 0.66592 | 0.0 | 0.51727 | 0.34446 |
| mod.blocks.5.attn | 6 | muon<-neutral_hadron | 0.64652 | 0.0 | 0.52423 | 0.33893 |
| mod.blocks.2.attn | 6 | muon<-muon | 0.50384 | 0.0 | 0.66613 | 0.33562 |

## Next
Use `part_attention_path_summary_v1.csv` for automatic physics-regime interpretation and ParticleNet-vs-ParT comparison.
