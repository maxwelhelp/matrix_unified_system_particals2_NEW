# Research Stream Index v1

This is the first thing to read before deep logs. It converts evidence graphs into queryable stream events.

- Snapshots: **15**
- Stream events: **6795**
- Latest run index: **14**

## Main cards
| priority | title | value | drilldown |
| --- | --- | --- | --- |
| P0 | Stream state | 15 snapshots, 6795 events | manifests/latest/research_stream_index_v1.json |
| P0 | Top current all-head gate | L1_ch112:128 rank 1 gate_abs=0.8689 | python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 10 |
| P0 | Top current particle evidence | event 3653 particle 0 label_Hqql score=5.1967 | python tools/query_research_stream_v1.py --event-type PARTICLE_TOP --top 20 |
| P0 | particle0/core dominance in top particle stream | run particle0 removal / top-k controls | reports/latest/tables/research_stream_alerts.csv |
| P1 | negative/suppressive head gates exist | compare positive vs negative gates; add suppressive-head analysis | reports/latest/tables/research_stream_alerts.csv |

## Alerts
| severity | title | score | next_action |
| --- | --- | --- | --- |
| HIGH | particle0/core dominance in top particle stream | 1.0000 | run particle0 removal / top-k controls |
| MEDIUM | negative/suppressive head gates exist | 5.0000 | compare positive vs negative gates; add suppressive-head analysis |

## Top current heads
| rank | title | score | summary |
| --- | --- | --- | --- |
| 1 | L1_ch112:128 rank 1 gate_abs=0.8689 | 0.8689 | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? |
| 2 | L1_ch16:32 rank 2 gate_abs=0.7480 | 0.7480 | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? |
| 3 | L0_ch40:48 rank 3 gate_abs=0.7156 | 0.7156 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 4 | L2_ch224:256 rank 4 gate_abs=0.7083 | 0.7083 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 5 | L0_ch48:56 rank 5 gate_abs=0.3769 | 0.3769 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 6 | L0_ch8:16 rank 6 gate_abs=0.3577 | 0.3577 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |
| 7 | L2_ch128:160 rank 7 gate_abs=0.3421 | 0.3421 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 8 | L2_ch64:96 rank 8 gate_abs=0.3056 | 0.3056 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 9 | L2_ch0:32 rank 9 gate_abs=0.2611 | 0.2611 | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? |
| 10 | L0_ch24:32 rank 10 gate_abs=0.2271 | 0.2271 | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? |

## Top current particles
| rank | title | score | summary | tags |
| --- | --- | --- | --- | --- |
| 1 | event 3653 particle 0 label_Hqql score=5.1967 | 5.1967 | pt=351.8683 dR=0.0731 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 2 | event 3458 particle 0 label_Hqql score=5.1648 | 5.1648 | pt=493.3960 dR=0.0331 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 3 | event 4073 particle 0 label_Hqql score=5.1471 | 5.1471 | pt=441.5128 dR=0.0147 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 4 | event 3346 particle 0 label_Hqql score=5.1411 | 5.1411 | pt=288.1587 dR=0.0467 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 5 | event 3282 particle 0 label_Hqql score=5.1176 | 5.1176 | pt=379.5849 dR=0.0690 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 6 | event 3477 particle 0 label_Hqql score=5.0932 | 5.0932 | pt=596.0616 dR=0.0393 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 7 | event 3931 particle 0 label_Hqql score=5.0865 | 5.0865 | pt=408.1933 dR=0.0199 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 8 | event 3525 particle 0 label_Hqql score=5.0709 | 5.0709 | pt=437.4170 dR=0.0272 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 9 | event 3375 particle 0 label_Hqql score=5.0370 | 5.0370 | pt=444.0590 dR=0.0185 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 10 | event 3192 particle 0 label_Hqql score=5.0365 | 5.0365 | pt=427.5177 dR=0.0538 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 11 | event 7974 particle 0 label_Wqq score=5.0278 | 5.0278 | pt=201.7087 dR=0.0590 charge=0.0000 | particle,label_Wqq,particle_0,particle0,core_high_pt |
| 12 | event 3329 particle 0 label_Hqql score=5.0219 | 5.0219 | pt=557.3921 dR=0.0414 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 13 | event 3101 particle 0 label_Hqql score=5.0098 | 5.0098 | pt=423.7215 dR=0.0287 charge=1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 14 | event 3330 particle 0 label_Hqql score=4.9895 | 4.9895 | pt=441.8409 dR=0.0349 charge=-1.0000 | particle,label_Hqql,particle_0,particle0,core_high_pt,charged |
| 15 | event 5121 particle 0 label_Tbl score=4.9885 | 4.9885 | pt=498.7116 dR=0.1038 charge=1.0000 | particle,label_Tbl,particle_0,particle0,core_high_pt,charged |

## Next actions
- Run particle0/top-k controls and rebuild stream index.
- Run class-specific all-head gradients for Hqql/Tbl/Tbqq/Wqq/Zqq.
- Run route-neighbor trace for top all-head particles.
- Create more distinct snapshots with HISTORY_COPY=1 for real dynamics.
- Move large stream history to SQLite/DuckDB when Git files get too large.

## Drilldown examples

```bash
python tools/query_research_stream_v1.py --query particle0 --top 20
python tools/query_research_stream_v1.py --head L1_ch112:128
python tools/query_research_stream_v1.py --class-label label_Hqql
python tools/query_research_stream_v1.py --hypothesis AH1
python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 20
```
