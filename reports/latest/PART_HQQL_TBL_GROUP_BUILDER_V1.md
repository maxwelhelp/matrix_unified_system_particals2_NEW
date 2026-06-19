# PART_HQQL_TBL_GROUP_BUILDER_V1

Builds A/B/C groups for ParT attention tracing from Weaver prediction ROOT outputs.

## Counts
| group | total_available | selected_limit |
| --- | --- | --- |
| A_Hqql_correct | 25694 | 5000 |
| B_Hqql_to_Tbl | 4577 | 2000 |
| C_Tbl_correct | 14533 | 5000 |
| D_Tbl_to_Hqql | 6443 | 2000 |

## Selected preview
| group | source_group | entry | true | pred | score_Hqql | score_Tbl | margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A_Hqql_correct | HToWW2Q1L | 34951 | label_Hqql | label_Hqql | 0.99957 | 0.0003 | 0.99927 |
| A_Hqql_correct | HToWW2Q1L | 15150 | label_Hqql | label_Hqql | 0.99928 | 0.00031 | 0.99898 |
| A_Hqql_correct | HToWW2Q1L | 60939 | label_Hqql | label_Hqql | 0.99915 | 0.0002 | 0.99895 |
| A_Hqql_correct | HToWW2Q1L | 96198 | label_Hqql | label_Hqql | 0.9991 | 0.00024 | 0.99886 |
| A_Hqql_correct | HToWW2Q1L | 57869 | label_Hqql | label_Hqql | 0.99927 | 0.00047 | 0.9988 |
| A_Hqql_correct | HToWW2Q1L | 89959 | label_Hqql | label_Hqql | 0.99899 | 0.00028 | 0.99871 |
| A_Hqql_correct | HToWW2Q1L | 14964 | label_Hqql | label_Hqql | 0.99885 | 0.00025 | 0.9986 |
| A_Hqql_correct | HToWW2Q1L | 12465 | label_Hqql | label_Hqql | 0.9988 | 0.00027 | 0.99853 |
| A_Hqql_correct | HToWW2Q1L | 17147 | label_Hqql | label_Hqql | 0.99919 | 0.00068 | 0.99851 |
| A_Hqql_correct | HToWW2Q1L | 1342 | label_Hqql | label_Hqql | 0.99901 | 0.00052 | 0.99849 |
| A_Hqql_correct | HToWW2Q1L | 45097 | label_Hqql | label_Hqql | 0.9987 | 0.0003 | 0.9984 |
| A_Hqql_correct | HToWW2Q1L | 27827 | label_Hqql | label_Hqql | 0.99898 | 0.00061 | 0.99836 |
| A_Hqql_correct | HToWW2Q1L | 49427 | label_Hqql | label_Hqql | 0.99873 | 0.00038 | 0.99835 |
| A_Hqql_correct | HToWW2Q1L | 33312 | label_Hqql | label_Hqql | 0.99888 | 0.00066 | 0.99822 |
| A_Hqql_correct | HToWW2Q1L | 8309 | label_Hqql | label_Hqql | 0.99844 | 0.00033 | 0.99811 |
| A_Hqql_correct | HToWW2Q1L | 62762 | label_Hqql | label_Hqql | 0.9989 | 0.00083 | 0.99807 |
| A_Hqql_correct | HToWW2Q1L | 98274 | label_Hqql | label_Hqql | 0.99813 | 6e-05 | 0.99807 |
| A_Hqql_correct | HToWW2Q1L | 63781 | label_Hqql | label_Hqql | 0.99828 | 0.00021 | 0.99806 |
| A_Hqql_correct | HToWW2Q1L | 51694 | label_Hqql | label_Hqql | 0.99815 | 0.00026 | 0.99789 |
| A_Hqql_correct | HToWW2Q1L | 76752 | label_Hqql | label_Hqql | 0.99806 | 0.00017 | 0.99789 |
| A_Hqql_correct | HToWW2Q1L | 15180 | label_Hqql | label_Hqql | 0.99789 | 0.00021 | 0.99768 |
| A_Hqql_correct | HToWW2Q1L | 6729 | label_Hqql | label_Hqql | 0.9983 | 0.00074 | 0.99756 |
| A_Hqql_correct | HToWW2Q1L | 58735 | label_Hqql | label_Hqql | 0.99812 | 0.00056 | 0.99756 |
| A_Hqql_correct | HToWW2Q1L | 84215 | label_Hqql | label_Hqql | 0.99832 | 0.00083 | 0.99749 |
| A_Hqql_correct | HToWW2Q1L | 25815 | label_Hqql | label_Hqql | 0.99839 | 0.00092 | 0.99747 |
| A_Hqql_correct | HToWW2Q1L | 12502 | label_Hqql | label_Hqql | 0.99855 | 0.00117 | 0.99738 |
| A_Hqql_correct | HToWW2Q1L | 99241 | label_Hqql | label_Hqql | 0.99843 | 0.00114 | 0.99729 |
| A_Hqql_correct | HToWW2Q1L | 15156 | label_Hqql | label_Hqql | 0.99785 | 0.00059 | 0.99725 |
| A_Hqql_correct | HToWW2Q1L | 5299 | label_Hqql | label_Hqql | 0.99808 | 0.00084 | 0.99724 |
| A_Hqql_correct | HToWW2Q1L | 56222 | label_Hqql | label_Hqql | 0.99797 | 0.00074 | 0.99723 |
| A_Hqql_correct | HToWW2Q1L | 97151 | label_Hqql | label_Hqql | 0.9979 | 0.0007 | 0.9972 |
| A_Hqql_correct | HToWW2Q1L | 41510 | label_Hqql | label_Hqql | 0.9973 | 0.00016 | 0.99713 |
| A_Hqql_correct | HToWW2Q1L | 97675 | label_Hqql | label_Hqql | 0.99784 | 0.00087 | 0.99697 |
| A_Hqql_correct | HToWW2Q1L | 43419 | label_Hqql | label_Hqql | 0.99792 | 0.00097 | 0.99695 |
| A_Hqql_correct | HToWW2Q1L | 33654 | label_Hqql | label_Hqql | 0.99773 | 0.00084 | 0.99689 |
| A_Hqql_correct | HToWW2Q1L | 1567 | label_Hqql | label_Hqql | 0.99761 | 0.00078 | 0.99683 |
| A_Hqql_correct | HToWW2Q1L | 21757 | label_Hqql | label_Hqql | 0.9974 | 0.00061 | 0.99679 |
| A_Hqql_correct | HToWW2Q1L | 85683 | label_Hqql | label_Hqql | 0.99764 | 0.00088 | 0.99676 |
| A_Hqql_correct | HToWW2Q1L | 21402 | label_Hqql | label_Hqql | 0.99695 | 0.0002 | 0.99675 |
| A_Hqql_correct | HToWW2Q1L | 75279 | label_Hqql | label_Hqql | 0.99701 | 0.00036 | 0.99665 |

## Next
Use `part_hqql_tbl_groups_v1.csv` as the event index list for `PART_ATTENTION_TRACE_V1`.
