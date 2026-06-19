# REASONING FRAMEWORK V1

## Принципы анализа, которые привели к Hqql/Tbl finding

Этот документ надо держать на самом видном месте. Он описывает не конкретный отчёт, а **метод мышления**, который переводит нас от “как сеть считает” к “что она считает”.

---

## Главный принцип — “Что” важнее “Как”

```text
БЫЛО:  Как сеть считает?  -> route -> head -> activation
СТАЛО: Что она считает?   -> физический смысл -> observable -> hypothesis
```

Если отчёт описывает только head/route/activation, но не отвечает на вопрос “что это означает в терминах данных или физики”, значит анализ застрял на уровне “как”.

---

## Принцип 1 — Аномалия как вход, а не выход

Не ищи паттерн во всех данных. Начинай с систематической ошибки модели.

```text
confusion matrix
  -> high confusion pair
  -> почему именно эти классы физически похожи?
```

В нашей задаче:

```text
Hqql -> Tbl confusion не случайна.
Оба класса связаны с W->lν topology.
```

Правило автоматизации:

```text
TRIGGER: confusion_rate(A->B) > 2x среднего
ACTION: задать вопрос “что физически общего между A и B?”
```

---

## Принцип 2 — Contrastive analysis вместо absolute analysis

Нельзя смотреть только confused events. Всегда сравнивать с правильными событиями.

```text
Hqql_correct vs Hqql_to_Tbl
Tbl_correct  vs Tbl_to_Hqql
```

Правило автоматизации:

```text
для каждого feature:
  mean(feature | group_A) vs mean(feature | group_B)
  ratio или standardized_diff
  если большой разрыв -> candidate discriminant
```

---

## Принцип 3 — Монотонность как доказательство

Если continuous feature монотонно связан с outcome, это сильнее, чем разница средних.

В нашей задаче:

```text
particle0 isolation -> Hqql->Tbl confusion_rate
0.00-0.10 : 0.0264
0.10-0.15 : 0.0243
0.15-0.20 : 0.0340
0.20-0.30 : 0.0724
0.30+     : 0.2558
```

Это дало finding:

```text
lepton/core isolation inside jet is a physical discriminant.
```

Правило автоматизации:

```text
bin continuous feature into 5 bins
compute outcome_rate per bin
if Spearman high and max/min rate > 5 -> strong observable candidate
```

---

## Принцип 4 — Causal patch как проверка направления

Корреляция не доказывает причинность. Нужен patch и matched/random контроль.

```text
targeted_patch_effect >> random_same_count_effect
```

В нашей задаче route-specific patch показал, что L2 core/KNN route causally holds prediction на выбранных событиях.

Правило автоматизации:

```text
targeted_patch
random_same_count_patch
null_patch
signal = targeted_flip_rate / random_flip_rate
если signal > 3 -> causal evidence
```

---

## Принцип 5 — Surrogate для измерения residual

Построй простую явную модель на найденных features.

```text
surrogate explains model -> mechanism mostly decoded
surrogate fails / overpredicts -> residual mechanism remains
```

В нашей задаче:

```text
V2.1 behavior surrogate AUC = 0.5908
surrogate overpredicts high-isolation bin
```

Значит isolation важен, но не полный механизм.

---

## Принцип 6 — Инверсия вопроса при residual

Если surrogate переоценивает, надо сменить вопрос.

```text
Не: почему Hqql уходит в Tbl?
А: почему большинство high-isolation Hqql НЕ уходит в Tbl?
```

В нашей задаче:

```text
high-isolation bin:
ParticleNet Hqql->Tbl rate = 0.2558
surrogate rate             = 0.8140
```

Значит есть **veto mechanism**: что-то спасает примерно 74% high-isolation Hqql от Tbl-readout.

Правило автоматизации:

```text
TRIGGER: surrogate_rate >> model_rate in a bin
ACTION:
  protected = high-risk events model classified correctly
  actual_confused = high-risk events model confused
  compare protected vs actual_confused
  find veto features
```

---

## Общий алгоритм автоматического анализа

```python
def analyze_report(report):
    confusion_pairs = find_high_confusion_pairs(report.confusion_matrix)

    for pair in confusion_pairs:
        ask_physical_question(pair)
        groups = build_contrastive_groups(pair)
        candidates = compare_features(groups)
        strong = monotonicity_check(candidates)
        causal = causal_patch(strong)
        surrogate = train_surrogate(causal)
        residual = compare_model_vs_surrogate_by_bins(surrogate)

        if surrogate_overpredicts(residual):
            find_veto_mechanism(residual)
        if surrogate_underpredicts(residual):
            find_additional_trigger(residual)
```

---

## Checklist для каждого нового отчёта

```text
□ Где модель ошибается систематически?
□ Почему эти классы похожи физически / логически?
□ Чем confused отличается от correct?
□ Есть ли монотонная зависимость по bins?
□ Targeted patch сильнее random?
□ Surrogate закрывает residual?
□ Если нет — что защищает correct cases или что добавляет trigger?
```

---

## Уровни claim

```text
Level 1 — Observable candidate:
  monotonicity by bins, ratio > 5x

Level 2 — Mechanistic candidate:
  + targeted patch >> random patch

Level 3 — Physics hypothesis:
  + surrogate partially closes residual
  + stable by files/subsamples

Level 4 — Cross-model claim:
  + same behavior on another architecture
```

Нельзя говорить “новая частица / новое взаимодействие”, пока нет внешней физической валидации.

---

## Применение сейчас

Следующий вопрос после V2.1:

```text
Что спасает high-isolation Hqql_correct от ложного Tbl-readout?
```

Нужный эксперимент:

```text
VETO_SEARCH_V1
```

Сравнить:

```text
Hqql_correct_highiso vs Hqql_to_Tbl_highiso
```

и найти veto features в KNN hadronic/leptonic/pair geometry.
