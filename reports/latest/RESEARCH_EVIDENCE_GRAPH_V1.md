# Research Evidence Graph v1

This is the compact structured evidence graph for agent/neural analysis.

- Nodes: **2056**
- Edges: **2270**
- Head vectors: **24**
- Particle vectors: **1894**
- Baseline acc: **0.7662109136581421**

## Main updated hypotheses

- AH1: distributed core-anchor + secondary-context mechanism.
- AH2: Hqql/Tbl high-confidence head-system signature.
- AH3: single-head and all-head evidence differ.
- AH4: head-system mixture across L0/L1/L2.

## Files

- JSON graph: `manifests/latest/research_evidence_graph_v1.json`
- Head vectors: `reports/latest/tables/evidence_head_vectors.csv`
- Particle vectors: `reports/latest/tables/evidence_particle_vectors.csv`
- Edges: `reports/latest/tables/evidence_edges.csv`

## Next use

This graph can be loaded by an agent, a notebook, Redis cache, SQLite/DuckDB, or a future neural hypothesis generator.
