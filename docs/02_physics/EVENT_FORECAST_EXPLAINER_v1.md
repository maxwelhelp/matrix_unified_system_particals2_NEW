# Event Forecast Explainer v1

Goal: explain individual JetClass events like token-level explanations in text models.

For each event, output:

```text
true label
predicted label
logits / confidence
active pseudo-head routes
active top particles and KNN neighbors
route-aware pseudocode explanation
known-observable/residual context when available
hypothesis tag
next validation
```

This is not a discovery claim. It is event-level mechanistic forecasting:

```text
what the network predicts
which particle route caused it
why this may correspond to Tbl/Hqql/H4q/QCD/WZ class competition
what remains to validate physically
```

Outputs:

```text
reports/latest/EVENT_FORECAST_EXPLAINER_V1.md
reports/latest/tables/event_forecast_explanations.csv
reports/latest/tables/event_forecast_active_routes.csv
manifests/latest/event_forecast_explainer_v1.json
```
