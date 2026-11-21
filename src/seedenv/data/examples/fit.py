"""Fit a measured relationship; replace x and y with your own observations."""
import json
import numpy as np
from scipy.optimize import curve_fit

x = np.linspace(0, 3, 31)
y = 2.5 * np.exp(-0.7 * x) + 0.01 * np.sin(4 * x)
parameters, covariance = curve_fit(lambda t, a, rate: a * np.exp(-rate * t), x, y)
print(json.dumps({"amplitude": parameters[0], "decay_rate": parameters[1],
                  "standard_errors": np.sqrt(np.diag(covariance)).tolist()}))
