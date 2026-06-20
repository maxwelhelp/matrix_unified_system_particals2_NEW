# PART_REPLAY_PARITY_REAL_CONTRACT_V1

Checks whether direct reconstructed ParT forward reproduces prediction ROOT labels for the same selected events.

## Summary

| group | n | root/direct pred match | root pred counts | direct pred counts | mean direct Tbl-Hqql |
| --- | ---: | ---: | --- | --- | ---: |
| A_Hqql_correct | 64 | 0.9531 | `{'label_Hqql': 64}` | `{'label_Hqql': 61, 'label_Tbl': 3}` | -7.100395 |
| B_Hqql_to_Tbl | 64 | 0.0469 | `{'label_Tbl': 64}` | `{'label_Hqql': 60, 'label_Tbl': 3, 'label_Hbb': 1}` | -6.448471 |
| C_Tbl_correct | 64 | 0.9688 | `{'label_Tbl': 64}` | `{'label_Tbl': 62, 'label_Hqql': 2}` | 7.271353 |
| D_Tbl_to_Hqql | 64 | 0.0000 | `{'label_Hqql': 64}` | `{'label_Tbl': 63, 'label_QCD': 1}` | 8.320596 |

## Decision

`REPLAY_PARITY_FAIL`: exact route patch is only a margin-sensitivity probe until reconstruction/prediction parity is fixed.
