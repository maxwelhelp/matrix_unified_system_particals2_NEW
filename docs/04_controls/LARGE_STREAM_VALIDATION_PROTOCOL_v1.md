# Large Stream Validation Protocol v1

This protocol describes how to run larger data without losing scientific discipline.

## Current state

The staged large run already reached:

```text
n_events = 5120
stream snapshots = 11
stream events = 4871
```

It confirmed:

```text
stable head mixture
particle0/core dominance
Hqql/Tbl concentration
```

But it did not resolve:

```text
physics vs shortcut
known-observable proxy vs residual signal
heldout stability
cross-model agreement
```

## Do not run everything blindly

Running more data without controls can amplify the strongest shortcut.

The correct protocol is staged:

```text
1. smoke / medium / large stream
2. controls
3. residual tests
4. heldout/cross-model
5. larger file/tar expansion
```

## Stage plan

### Stage 1 — current completed stage

```text
medium: SAMPLES_PER_FILE=256
large: SAMPLES_PER_FILE=512
```

Status:

```text
completed enough for next controls
```

### Stage 2 — controls before more scale

Run:

```text
particle0/top-k controls
order shuffle
class-specific gradients
known-observable residual
```

### Stage 3 — xlarge sampled

Only after Stage 2 starts:

```bash
STAGE=xlarge MICRO_BATCH=8 bash scripts/RUN_LARGE_STREAM_STAGE_V1.sh
```

### Stage 4 — more ROOT files / tar parts

Only after per-file tracking exists.

Required output:

```text
per-file heldout stability report
class distribution report
stream size report
```

## What to record per run

Each run should store:

```text
stage
sample size
file list
classes present
n_events
baseline accuracy
top heads
top particle patterns
watcher task states
relation signals
comparison statuses
```

## Stop conditions

Stop scaling and run controls if:

```text
particle0/core dominance remains HIGH
class dominance Hqql/Tbl remains HIGH
comparison engine says METHOD_DEBUG_NOT_DISCOVERY_READY
known-observable residual is missing
```

Current project state satisfies these stop conditions, so the next step is controls, not more blind scaling.
