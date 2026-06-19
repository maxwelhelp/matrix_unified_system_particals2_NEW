# Large Stream Run Plan v1

The large stream should not start by running the whole downloaded JetClass data blindly.

## Why not everything at once

The current strongest signal is particle0/core dominance. If this is a shortcut, a larger run will only make the shortcut look more confident.

So the right order is:

```text
1. staged larger stream
2. evidence graph + dynamics + stream + watcher + relation + comparison
3. particle0/top-k controls
4. class-specific gradients
5. route-neighbor trace
6. then expand to more files/tar parts
```

## Stages

### Stage A — smoke stream

```text
SAMPLES_PER_FILE=64
MICRO_BATCH=32
```

Purpose:

```text
check pipeline works after code changes
```

### Stage B — medium stream

```text
SAMPLES_PER_FILE=256
MICRO_BATCH=32
```

Purpose:

```text
current baseline scale
```

### Stage C — large sampled stream

```text
SAMPLES_PER_FILE=512
MICRO_BATCH=16
```

Purpose:

```text
larger evidence without OOM
```

### Stage D — bigger sampled stream

```text
SAMPLES_PER_FILE=1024
MICRO_BATCH=8 or 16
```

Purpose:

```text
stress test stability
```

## Expected outputs after each stage

```text
all-head supertrace
evidence graph history
dynamics
stream index
task watcher
relation signal graph
automatic comparison engine v2
```

## Important rule

After Stage B or C, do not just keep scaling. Run controls:

```text
particle0/top-k controls
class-specific gradients
route-neighbor trace
```

Otherwise the stream mostly tells us that particle0/core dominates, but not whether that is physics or shortcut.
