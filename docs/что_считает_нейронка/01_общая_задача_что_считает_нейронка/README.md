# 01 — Общая задача: что считает нейронка

Эта папка — родная для старого направления, которым мы занимались раньше: **декомпилировать нейросеть/матрицы/головы в читаемые операции и псевдокод**.

## Главная идея

```text
нейронка / матрица / слой / голова
  -> извлечь вычислительную операцию
  -> описать её как псевдокод / рецепт
  -> проверить causal/functional patch
  -> понять, что именно считается
```

## Старые подзадачи

```text
Program autoencoder
Matrix-to-program
Program-to-matrix
Residual-to-patch
Task-to-recipe
Operator dictionary / primitive categories
```

## Категории этой ветки

```text
method/
  методология декомпиляции матриц, голов, операций, псевдокода

operator_dictionary/
  примитивы и категории операций: local, shift, diff, gate, select, normalize, memory, content, rank, frequency, state, copy, compress, expand, compare, bind, unbind

matrix_programs/
  matrix-to-program, program-to-matrix, product steps, residual-to-patch

head_questions/
  подход “какие вопросы задаёт голова / что она считает”

experiments/
  прогоны, отчёты, диагностика

handoff/
  документы, которые вводят нового агента в курс дела
```

## Где искать старые материалы

Пока старые файлы могут лежать в разных местах репозитория:

```text
docs/
reports/latest/
tools/
scripts/
```

Эта папка фиксирует правильную структуру. Новые документы по общей задаче надо складывать сюда.

## Связь с текущей ParticleNet-задачей

ParticleNet/Hqql-Tbl — это конкретное применение общей задачи:

```text
не просто L2_head -> particle0 -> KNN,
а что физически означает этот route.
```
