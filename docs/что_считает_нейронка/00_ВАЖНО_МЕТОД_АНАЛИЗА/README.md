# 00 — ВАЖНО: метод анализа

Это самая важная папка направления **«что считает нейронка»**.

Её надо читать первой, до любых отдельных отчётов.

## Почему она важна

Главная ошибка, которую мы уже совершали:

```text
смотреть только route/head/activation и забывать спросить:
что это физически или логически означает?
```

Вторая ошибка, которую мы только что зафиксировали:

```text
когда физическая гипотеза уже сформулирована,
продолжать дебажить модель только внешними patches/surrogates,
хотя у нас есть доступ к внутренним активациям.
```

Третья ключевая ошибка, которую теперь запрещаем:

```text
смотреть на голову как на “важный канал”,
но не читать её как матричную программу:
что она читает, куда пишет, какую class-direction двигает,
и какие частицы включают эту программу.
```

Четвёртая ошибка:

```text
анализировать по одной голове вручную,
когда нужен полный граф particle_role -> head -> class по всем головам.
```

Правильный порядок:

```text
1. найти систематическую ошибку / аномалию
2. понять физический/данный смысл классов
3. сравнить confused vs correct
4. найти monotonic observable
5. проверить patch/control
6. построить surrogate
7. если surrogate ошибается — искать veto/additional trigger
8. когда гипотеза стала конкретной — проверить её напрямую во внутренних активациях
9. каждую важную голову читать как матричную программу: read -> project -> route/write -> class direction -> particle roles
10. строить полный граф путей particle_role -> head -> class и ранжировать triggers/loss/anomalies автоматически
```

## Главные документы

Читать в таком порядке:

```text
REASONING_FRAMEWORK_V1.md
  Базовая логика анализа: confusion -> physical question -> contrastive groups -> monotonicity -> patch -> surrogate -> residual inversion.

DIRECT_INTERNAL_ACTIVATION_PROBE_V1.md
  Новый важный разворот: после появления конкретной физической гипотезы идти внутрь сети и сравнивать activation space, а не только делать внешние patches.

MATRIX_PROGRAM_HEAD_ANALYSIS_PRINCIPLE_V1.md
  Главный принцип чтения голов: каждая pseudo-head = матричная программа. Надо анализировать read/source blocks, projection, route/write, class-direction и top-particle roles.

MATRIX_PROGRAM_FULL_TRACE_V1.md
  Полный автоматический trace: particle_role -> head -> class, ranked paths, triggers, source-evidence loss, anomalous third-topology mechanisms.

CLASS_PAIR_PHYSICS_PLAYBOOK_V1.md
  Что делать, когда Confusion Monitor нашёл новую пару классов. Примеры: Zqq/Wqq, Hbb/Hcc, Hgg/H4q.

STREAM_ARCHITECTURE_V1.md
  Как превратить метод в поток: monitor -> ranker -> deep probe -> signal board.

AUTOMATIC_REASONING_PIPELINE_V1.md
  Полная автоматизация reasoning pipeline и claim levels.

FEATURE_RANKER_V1.md
  Как ранжировать features после WATCH/ALERT пары.
```

Этот framework создан из логики, которая привела нас от head/route tracing к реальному finding:

```text
ParticleNet uses lepton/core isolation inside jet for Hqql/Tbl ambiguity.
```

Теперь тот же метод применяется автоматически к новым парам, которые поднимает Confusion Monitor:

```text
Zqq <-> Wqq
Hbb <-> Hcc
Hgg <-> H4q
...
```

## Запомнить

```text
Не “какая голова активна?”
А “какой физический/логический observable она считает?”
```

И второе:

```text
Когда observable уже найден — не гадать только внешними патчами.
Надо смотреть, где он живёт во внутренних активациях.
```

И третье:

```text
Когда найдена важная голова — не останавливаться на importance.
Надо восстановить её матричную программу:
какие source blocks она читает,
какие частицы активируют её,
какую class-direction она двигает,
и где в цепочке возникает route / failure / readout.
```

И четвёртое:

```text
После отдельных голов надо строить полный граф всех путей:
particle_role -> pseudo-head -> class.
Так видны сразу trigger paths, loss paths и anomalous third-topology paths.
```

## Автоматизация

Все будущие анализаторы отчётов должны следовать этому framework:

```text
confusion -> contrastive groups -> bins/monotonicity -> patch -> surrogate -> residual inversion -> direct activation contrast -> matrix-program head analysis -> full path trace
```

Новая практическая схема:

```text
CONFUSION_MONITOR_V1
  -> signal_board_v1.csv

FEATURE_RANKER_V1
  -> top observable candidates

DIRECT_INTERNAL_ACTIVATION_PROBE
  -> A/B/C activation contrast when hypothesis is concrete

MATRIX_PROGRAM_HEAD_ANALYSIS
  -> read/source blocks -> projection -> class-direction -> particle roles

MATRIX_PROGRAM_FULL_TRACE
  -> particle_role -> head -> class ranked mechanisms

DEEP_PROBE
  -> patch/control/surrogate only for top candidates or after activation evidence
```

## Пороги для Feature Ranker

Главное число после monitor:

```text
monotonic_ratio = max_bin_confusion_rate / min_bin_confusion_rate
```

Интерпретация:

```text
> 5x  -> сильный observable candidate
> 3x  -> средний, копать если физически осмысленно
< 2x  -> обычно шум или слабый эффект
```
