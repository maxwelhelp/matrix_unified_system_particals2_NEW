# INTERNAL_ACTIVATION_CONTRAST_V2

Direct internal extractor for the Hqql/Tbl hypothesis.

## Purpose

Answer the question Claude asked:

```text
Is confused high-isolation Hqql actively mapped into Tbl readout,
or does it simply lose Hqql evidence?
```

## Groups

```text
A = protected_highiso
    true=Hqql, pred=Hqql, isolation>0.30

B = confused_highiso
    true=Hqql, pred=Tbl, isolation>0.30

C = Tbl_correct
    true=Tbl, pred=Tbl
```

## What V2 measures

For each pseudo-head/channel slice:

```text
L2_ch128:160
L2_ch160:192
L2_ch224:256
L1_ch32:48
L1_ch80:96
```

and optionally more heads, V2 extracts:

```text
event-level activation mean/norm
approximate classifier-direction projections:
  score_hqql
  score_tbl
particle-level top activation particles
zero-slice ablation contribution:
  contribution_to_Hqql_logit
  contribution_to_Tbl_logit
```

## Diagnosis logic

```text
B ~= C and B has high Tbl score:
  active Tbl readout

B != A but B not ~= C, and Hqql contribution collapses:
  loss of Hqql evidence

Different heads show different modes:
  mixed mechanism
```

## Why ablation is included

The classifier after EdgeConv is not guaranteed to be perfectly linear because of FC nonlinearities. Therefore V2 uses two lenses:

```text
projection lens:
  approximate class-direction score from head slice

ablation lens:
  zero the head slice during forward pass and measure actual Hqql/Tbl logit delta
```

The ablation lens is the safer causal readout.
