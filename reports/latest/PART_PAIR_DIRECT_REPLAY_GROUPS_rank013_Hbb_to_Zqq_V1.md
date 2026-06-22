# PART_PAIR_DIRECT_REPLAY_GROUPS_rank013_Hbb_to_Zqq_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **13**
- src_label: `label_Hbb` / src_group: `HToBB`
- tgt_label: `label_Zqq` / tgt_group: `ZToQQ`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank013_Hbb_to_Zqq_v1.csv`

## Group counts
| group | selected |
| --- | --- |
| A_src_correct | 256 |
| B_src_to_tgt | 256 |
| C_tgt_correct | 256 |
| D_tgt_to_src | 256 |

## Source scan counts
| source_group | scanned | pred_counts |
| --- | --- | --- |
| HToBB | 20000 | {'label_Hcc': 1888, 'label_Tbqq': 376, 'label_Hbb': 14361, 'label_Hgg': 1668, 'label_Hqql': 43, 'label_Zqq': 851, 'label_Wqq': 117, 'label_QCD': 296, 'label_H4q': 381, 'label_Tbl': 19} |
| ZToQQ | 9344 | {'label_Zqq': 5860, 'label_Wqq': 1902, 'label_QCD': 470, 'label_H4q': 196, 'label_Tbqq': 126, 'label_Hgg': 200, 'label_Hcc': 291, 'label_Hbb': 257, 'label_Hqql': 37, 'label_Tbl': 5} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
