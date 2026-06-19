# Stream Cycle Workflow v1

This workflow turns the project into a repeatable evidence stream.

## Why the stream index is fast

`RUN_RESEARCH_STREAM_INDEX_V1.sh` does not run ParticleNet. It only reads existing JSON/CSV evidence graphs and builds a stream index.

Heavy step:

```text
ParticleNet / ROOT / gradients / particles
```

Fast steps:

```text
evidence graph indexing
dynamics comparison
stream indexing
querying
```

## Full stream cycle

Use:

```bash
bash scripts/RUN_STREAM_CYCLE_V1.sh
```

This runs:

1. all-head supertrace, unless `RUN_MODEL=0`;
2. evidence graph with history copy;
3. dynamics;
4. stream index.

## Examples

### Rebuild only index from current data

```bash
RUN_MODEL=0 bash scripts/RUN_STREAM_CYCLE_V1.sh
```

### New short stream snapshot

```bash
SAMPLES_PER_FILE=64 MICRO_BATCH=32 RUN_MODEL=1 bash scripts/RUN_STREAM_CYCLE_V1.sh
```

### New main stream snapshot

```bash
SAMPLES_PER_FILE=256 MICRO_BATCH=32 RUN_MODEL=1 bash scripts/RUN_STREAM_CYCLE_V1.sh
```

### Safer low-memory run

```bash
SAMPLES_PER_FILE=256 MICRO_BATCH=16 RUN_MODEL=1 bash scripts/RUN_STREAM_CYCLE_V1.sh
```

## After the cycle

Read first:

```text
reports/latest/RESEARCH_STREAM_INDEX_V1.md
manifests/latest/research_stream_index_v1.json
```

Then drill down:

```bash
python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 20
python tools/query_research_stream_v1.py --query particle0 --top 30
python tools/query_research_stream_v1.py --class-label label_Hqql --top 30
python tools/query_research_stream_v1.py --hypothesis AH1 --top 30
```

## Current P0 stream alert

The current stream reports strong particle0/core dominance. Next model-side experiment should test:

```text
remove particle0
keep only particle0
remove top-k particles
same-count random controls
```
