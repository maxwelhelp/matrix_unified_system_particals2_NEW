# Question Driven Stage Analyzer v1

The project now has many evidence layers:

```text
pseudocode v2
layer code alignment
head output trace
class-specific gradients
particle0/top-k controls
order control
confusion atlas
known-observable residual
scope guard
```

The next step is to answer research questions automatically.

## Goal

Instead of reading every report manually, the analyzer should answer questions such as:

```text
Which heads implement the Hqql/Tbl residual axis?
Where is the late core/particle0 readout?
Which heads are early local builders vs late readouts?
Which stages explain the particle0/top-k causal effect?
What remains untested before a physics claim?
Which heads should be traced inside EdgeConv next?
```

## Output

```text
reports/latest/QUESTION_DRIVEN_STAGE_ANALYZER_V1.md
reports/latest/tables/question_driven_stage_answers.csv
reports/latest/tables/question_driven_head_rankings.csv
manifests/latest/question_driven_stage_analyzer_v1.json
```

## Rule

Each answer must cite its evidence stage:

```text
semantic pseudocode
code alignment
output trace
controls
confusion
residual
next test
```

The analyzer must not treat local control deltas as global stream deltas. It must preserve scope labels.
