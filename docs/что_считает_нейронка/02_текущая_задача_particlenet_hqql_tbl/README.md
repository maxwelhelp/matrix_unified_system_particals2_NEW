# 02 — Текущая задача: ParticleNet / Hqql–Tbl / lepton-core isolation

Эта папка — родная для текущей задачи.

## Цель

Понять не только **как** ParticleNet считает, а **что физически** она считает при Hqql/Tbl ambiguity.

Главный вопрос:

```text
В каком кинематическом / топологическом режиме Hqql и Tbl становятся неразличимы,
и что именно сеть использует для их различения?
```

## Текущий главный finding

```text
ParticleNet implicitly uses lepton/core isolation inside jet
as a discriminant for Hqql/Tbl ambiguity.
```

## Evidence chain

```text
Phase 1:
  набрали статистику Hqql_to_Tbl=154, Tbl_to_Hqql=145

Phase 2:
  physical swaps показали, что hadronic context вокруг lepton/core влияет,
  но random control был сильный

Phase 3:
  isolation bins дали чистый observable-signal:
  confusion_rate 0.0264 -> 0.2558 от low isolation к high isolation

Residual V2/V2.1:
  explicit isolation/KNN/missing-pT features подтверждают направление,
  но не полностью воспроизводят ParticleNet behavior
```

## Категории

```text
00_status/
  текущий статус, что доказано, что нет

01_findings/
  законченные findings для paper section

02_phase_experiments/
  Phase 1/2/3: статистика, swaps, controls

03_residual/
  residual/surrogate tests: V2, V2.1, будущий V3

04_methods_and_tools/
  какие tools/scripts запускать

05_reports_map/
  карта исходных отчётов в reports/latest

06_next_steps/
  что делать дальше
```

## Осторожная формулировка

Можно говорить:

```text
ParticleNet uses lepton/core isolation as a mechanistic discriminator for Hqql/Tbl ambiguity.
```

Нельзя пока говорить:

```text
мы открыли новую частицу / новое взаимодействие
```

Пока статус:

```text
mechanistic physics finding + residual candidate
```
