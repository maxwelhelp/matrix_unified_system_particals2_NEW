# Stream Architecture V1 — no LLM first

This is the practical streaming architecture for automatic discovery-style analysis.

## Principle

The signal must surface by itself.

```text
ROOT/events stream
  -> Confusion Monitor
  -> Feature Ranker
  -> Deep Probe only for top signals
  -> Signal Board
  -> human/assistant review
```

No LLM is needed in V1. The system writes structured signals, and the assistant/human interprets them later.

## Component 1 — Confusion Monitor

Goal:

```text
detect class-pair confusion shifts automatically
```

Input:

```text
model checkpoint
data directory
samples/files stage
baseline confusion json from previous run
```

Output:

```text
reports/latest/CONFUSION_MONITOR_V1.md
reports/latest/tables/confusion_monitor_v1_pairs.csv
reports/latest/tables/confusion_monitor_v1_matrix.csv
reports/latest/tables/signal_board_v1.csv
manifests/latest/confusion_monitor_v1.json
```

Status logic:

```text
ALERT if confusion_rate or delta_vs_baseline is high
WATCH if moderate
OK otherwise
```

## Component 2 — Feature Ranker

Runs only for WATCH/ALERT class pairs.

For each pair A/B:

```text
A_correct
A_to_B
B_correct
B_to_A
```

Compute contrastive features and monotonic bins.

## Component 3 — Deep Probe

Runs only for top ranked feature candidates.

```text
patch/control
surrogate
residual inversion
veto/trigger search
```

## Signal Board

A row is a candidate hypothesis or alert:

```text
signal_id
source
class_pair
status
score
reason
next_action
```

The assistant should review only the signal board, not all raw events.
