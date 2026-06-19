# MATRIX_PROGRAM_HEAD_ANALYSIS_PRINCIPLE_V1

## Главный принцип

Каждую pseudo-head / channel group надо анализировать не как абстрактный feature importance, а как **матричную программу**.

То есть для каждой головы надо отвечать не только:

```text
эта голова важна или нет?
```

а:

```text
что она читает?
из каких предыдущих channel programs?
какие частицы / соседства активируют её?
какую проекцию она пишет дальше?
какую class-direction она усиливает или теряет?
какой физический observable соответствует этой программе?
```

## Почему это важно

Внешние методы дают физическую гипотезу:

```text
confusion bins
patches
surrogates
feature ranker
```

Но они не показывают, где именно внутри сети живёт механизм.

Матричная программа головы показывает:

```text
local particle evidence
-> learned projection
-> channel slice / pseudo-head
-> next route/composition layer
-> class-evidence direction
```

Это превращает интерпретацию из:

```text
модель почему-то путает A и B
```

в:

```text
эта L1-программа строит B-like route,
а эта L2-программа теряет A evidence,
поэтому classifier выбирает B.
```

## Универсальный шаблон анализа головы

Для каждой головы / channel group:

```text
1. Static identity
   layer, channel slice, head_id

2. Patch lens
   что меняется при zero/patch этой головы?
   acc_drop, logit_drop, class_drop

3. Weight/source lens
   какие предыдущие channel blocks её кормят?
   какие output blocks она пишет?

4. Matrix-program pseudocode
   read particle state
   read KNN neighbors
   read edge differences
   project through W
   aggregate / route / write

5. Class-direction lens
   score_Hqql, score_Tbl, score_other
   logit contribution when zeroed

6. A/B/C activation contrast
   A = correct protected
   B = confused target
   C = correct predicted-class reference

7. Particle attribution
   top particles by activation:
   particle0, best_lepton, second_lepton, hard_hadron, nearest_hadron, other

8. Diagnosis
   active target-class readout?
   loss of source-class evidence?
   mixed route/class failure?
```

## Required output for every head

```text
head_id
layer
channels
matrix_program_role
source_blocks
output_blocks
class_effects
A_activation
B_activation
C_activation
B_minus_A_effect
B_closer_to_C_score
top_particle_roles_A
top_particle_roles_B
top_particle_roles_C
diagnosis
physical_interpretation
next_test
```

## Diagnosis types

### 1. Active target-class readout

```text
B becomes closer to C than A
B target-class contribution rises
```

Meaning:

```text
the head actively constructs target-class evidence
```

### 2. Loss of source-class evidence

```text
B source-class contribution drops
B target-class contribution does not rise cleanly
```

Meaning:

```text
the head fails to preserve the correct-class signal
```

### 3. Mixed mechanism

```text
one head builds target-like route
a later head loses source-class evidence
```

Meaning:

```text
the model confuses because different stages fail differently
```

This is usually the most interesting case.

## Example: Hqql -> Tbl confusion

External analysis found:

```text
high lepton/core isolation -> Tbl-risk
spread lepton-centered geometry -> suspicious
second-lepton ambiguity -> suspicious
```

Direct internal contrast showed a stronger mechanism.

### L1 route/composition stage

```text
L1_ch80:96
  B_confused_highiso has active Tbl-like route contribution
  B-A hqql_contrib ~= -0.1101
  B-A tbl_contrib  ~= +1.1220

L1_ch32:48
  weaker but same direction
  B-A hqql_contrib ~= -0.2127
  B-A tbl_contrib  ~= +0.3607
```

Interpretation:

```text
Tbl-like composition appears already at L1 route level.
Something in local particle-neighborhood evidence is routed as Tbl-like before final class readout.
```

### L2 class-evidence stage

```text
L2_ch128:160
  B-A hqql_contrib ~= -0.2256
  B-A tbl_contrib  ~= -0.0576
```

Interpretation:

```text
L2_ch128:160 does not become a clean Tbl head.
It mainly loses Hqql evidence.
```

### Complete mechanism from this example

```text
Step 1 — L1 route trigger:
  local particle-neighborhood ambiguity activates Tbl-like route/composition.

Step 2 — L2 evidence failure:
  correct Hqql evidence is not accumulated strongly.

Step 3 — classifier result:
  residual/early Tbl-like signal + weak Hqql evidence -> pred Tbl.
```

This is stronger than saying:

```text
high isolation correlates with confusion
```

because it says:

```text
where inside the network the wrong route appears,
where the correct evidence is lost,
and which particle roles likely trigger the transition.
```

## What this opens

This method opens three things.

### 1. Mechanistic interpretability

We can explain not only what feature correlates with errors, but where the network represents it.

```text
observable -> pseudo-head -> matrix program -> class direction
```

### 2. Discovery of implicit observables

If a head consistently reads a particle-neighborhood structure that is not in standard observables, we can extract it as a new explicit candidate observable.

Example:

```text
compactness / spread of lepton-centered KNN context
second-lepton-like route trigger
```

### 3. Automated analysis of all heads

The same process should run for every head and every important class pair:

```text
Confusion Monitor -> Feature Ranker -> Matrix Program Head Analysis -> Direct Activation Contrast -> Particle Role Attribution
```

The output is a catalog:

```text
which heads read raw physics
which heads build routes
which heads accumulate class evidence
which heads fail during confusion
which particles trigger each failure
```

## Rule for future work

Do not stop at:

```text
feature is important
head is important
patch changes output
```

Always continue to:

```text
what matrix program does this head implement?
what does it read?
what does it write?
which class direction does it change?
which particles cause it in A/B/C?
```

That is the core of this project.
