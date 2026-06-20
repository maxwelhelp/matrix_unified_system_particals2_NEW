# PART_REPLAY_PARITY_REAL_CONTRACT_V1

Checks whether direct reconstructed ParT forward reproduces prediction ROOT labels for the same selected events.

## Summary

| group | n | root/direct pred match | root pred counts | direct pred counts | mean direct Tbl-Hqql |
| --- | ---: | ---: | --- | --- | ---: |
| A_Hqql_correct | 64 | 0.0000 | `{'label_Hqql': 64}` | `{'label_Zqq': 31, 'label_QCD': 29, 'label_Hcc': 2, 'label_Wqq': 1, 'label_Hbb': 1}` | -0.972998 |
| B_Hqql_to_Tbl | 64 | 0.0000 | `{'label_Tbl': 64}` | `{'label_Zqq': 30, 'label_QCD': 22, 'label_Hcc': 6, 'label_H4q': 3, 'label_Hbb': 1, 'label_Wqq': 1, 'label_Hqql': 1}` | -1.520804 |
| C_Tbl_correct | 64 | 0.0156 | `{'label_Tbl': 64}` | `{'label_QCD': 33, 'label_Zqq': 16, 'label_Hbb': 10, 'label_Wqq': 3, 'label_Tbl': 1, 'label_Hgg': 1}` | -1.421699 |
| D_Tbl_to_Hqql | 64 | 0.0312 | `{'label_Hqql': 64}` | `{'label_QCD': 27, 'label_Hbb': 12, 'label_Zqq': 13, 'label_Hqql': 2, 'label_Tbl': 5, 'label_Hcc': 3, 'label_Wqq': 2}` | -1.117456 |

## Decision

`REPLAY_PARITY_FAIL`: exact route patch is only a margin-sensitivity probe until reconstruction/prediction parity is fixed.
