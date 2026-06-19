# Research Dynamics v1

This report compares evidence graph snapshots across runs.

- Graph snapshots: **15**
- Real dynamics available: **True**

## Runs
| run | generated | baseline_acc | n_events | nodes | edges | heads | particles |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-06-16T04:05:30.121747+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 1 | 2026-06-16T04:10:17.558878+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 2 | 2026-06-16T04:12:40.863052+00:00 | 0.7719 | 640 | 814 | 966 | 24 | 710 |
| 3 | 2026-06-16T04:24:36.833330+00:00 | 0.7719 | 640 | 814 | 966 | 24 | 710 |
| 4 | 2026-06-16T04:24:47.422420+00:00 | 0.7719 | 640 | 814 | 966 | 24 | 710 |
| 5 | 2026-06-16T04:25:12.140529+00:00 | 0.7719 | 640 | 1076 | 1246 | 24 | 950 |
| 6 | 2026-06-16T04:26:01.675182+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 7 | 2026-06-16T04:29:01.473693+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 8 | 2026-06-16T04:30:31.493657+00:00 | 0.7574 | 2560 | 1080 | 1255 | 24 | 959 |
| 9 | 2026-06-16T05:06:52.665592+00:00 | 0.7574 | 2560 | 2027 | 2241 | 24 | 1865 |
| 10 | 2026-06-16T05:11:25.686042+00:00 | 0.7602 | 5120 | 2056 | 2269 | 24 | 1893 |
| 11 | 2026-06-16T05:24:57.640226+00:00 | 0.7662 | 10240 | 2056 | 2270 | 24 | 1894 |
| 12 | 2026-06-16T05:28:42.780658+00:00 | 0.7662 | 10240 | 2056 | 2270 | 24 | 1894 |
| 13 | 2026-06-16T05:31:03.047143+00:00 | 0.7662 | 10240 | 2056 | 2270 | 24 | 1894 |
| 14 | 2026-06-16T06:43:00.041263+00:00 | 0.7662 | 10240 | 2056 | 2270 | 24 | 1894 |

## Latest top heads
| rank | head | gate_abs | delta_gate | delta_rank | patch_drop | role |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | L1_ch112:128 | 0.8689 | 0.0000 | 0 | 0.0000 | middle learned-neighborhood / route-composition head |
| 2 | L1_ch16:32 | 0.7480 | 0.0000 | 0 | 0.0000 | middle learned-neighborhood / route-composition head |
| 3 | L0_ch40:48 | 0.7156 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 4 | L2_ch224:256 | 0.7083 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 5 | L0_ch48:56 | 0.3769 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 6 | L0_ch8:16 | 0.3577 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |
| 7 | L2_ch128:160 | 0.3421 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 8 | L2_ch64:96 | 0.3056 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 9 | L2_ch0:32 | 0.2611 | 0.0000 | 0 | 0.0000 | late aggregation / class-evidence head |
| 10 | L0_ch24:32 | 0.2271 | 0.0000 | 0 | 0.0000 | early feature/geometry/PID reader |

## Latest class particle patterns
| class | n | mean_score | mean_pt | mean_deltaR | particle0_fraction | charged_fraction |
| --- | --- | --- | --- | --- | --- | --- |
| label_Zqq | 32 | 3.2203 | 23.8471 | 0.1093 | 0.0625 | 0.5312 |
| label_QCD | 16 | 3.0393 | 21.2429 | 0.0465 | 0.0625 | 0.3750 |
| label_Wqq | 16 | 2.7462 | 21.9049 | 0.1449 | 0.0625 | 0.6250 |
| label_Tbl | 264 | 2.6393 | 40.0952 | 0.2991 | 0.0644 | 0.4167 |
| label_Hqql | 1566 | 2.5816 | 36.4443 | 0.2075 | 0.0632 | 0.4547 |

## Output files

- JSON: `manifests/latest/research_dynamics_v1.json`
- Head dynamics: `reports/latest/tables/dynamics_head_ranks.csv`
- Particle dynamics: `reports/latest/tables/dynamics_particle_patterns.csv`
- Hypothesis dynamics: `reports/latest/tables/dynamics_hypotheses.csv`
