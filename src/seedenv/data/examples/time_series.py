"""Forecast a synthetic AR(1) sequence using only its training prefix."""
import json
import numpy as np
from statsmodels.tsa.ar_model import AutoReg

rng = np.random.default_rng(19)
y = np.zeros(240)
for t in range(1, len(y)):
    y[t] = 0.7 * y[t-1] + rng.normal(scale=0.2)
model = AutoReg(y[:200], lags=1).fit()
prediction = model.predict(200, 239)
print(json.dumps({"train_samples": 200, "forecast_samples": 40,
                  "ar_coefficient": float(model.params[1]),
                  "forecast_mae": float(np.mean(abs(prediction-y[200:])))}))
