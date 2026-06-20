# PART_ENTRY_MAPPING_PROBE_V1

Compares prediction ROOT scores at the selected entry_idx with direct legacy-wrapper replay probabilities for the same source entry.

| group | n | same pred rate | mean score L2 | root pred counts | direct pred counts |
| --- | ---: | ---: | ---: | --- | --- |
| A_Hqql_correct | 256 | 0.9688 | 0.079958 | `{'label_Hqql': 256}` | `{'label_Hqql': 248, 'label_Tbl': 5, 'label_Wqq': 1, 'label_Zqq': 1, 'label_H4q': 1}` |
| B_Hqql_to_Tbl | 256 | 0.0391 | 1.304014 | `{'label_Tbl': 256}` | `{'label_Hqql': 239, 'label_Tbl': 10, 'label_Hbb': 3, 'label_Zqq': 1, 'label_Wqq': 2, 'label_Tbqq': 1}` |
| C_Tbl_correct | 256 | 0.9609 | 0.070545 | `{'label_Tbl': 256}` | `{'label_Tbl': 246, 'label_Hqql': 8, 'label_QCD': 1, 'label_Hbb': 1}` |
| D_Tbl_to_Hqql | 256 | 0.0234 | 1.334405 | `{'label_Hqql': 256}` | `{'label_Tbl': 246, 'label_QCD': 2, 'label_Hqql': 6, 'label_Wqq': 1, 'label_Hcc': 1}` |

## Decision

`ENTRY_MAPPING_OR_SCORE_PARITY_FAIL`: prediction ROOT selected rows are not reliably the same replayed source events/scores. Do not use error groups for causal claims yet.
