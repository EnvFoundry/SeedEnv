"""Kaplan-Meier estimation on four synthetic observations."""
import json
from lifelines import KaplanMeierFitter

model = KaplanMeierFitter().fit([1, 2, 3, 4], event_observed=[1, 0, 1, 1])
survival = float(model.predict(3))
print(json.dumps({'data':'synthetic', 'survival_at_3':survival,
                  'median_event_time':float(model.median_survival_time_)}))
assert abs(survival - 0.375) < 1e-12
