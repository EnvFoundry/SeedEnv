"""Synthetic linear sensor calibration and an inverse prediction in kelvin."""
import json
import numpy as np
from scipy.optimize import curve_fit

# Reference values are treated as exact in this example. Observed voltage has
# known independent 0.05 V standard uncertainty; real standards may need ODR.
reference_K = np.arange(6, dtype=float)
reading_V = 1.7 * reference_K + 0.12 + np.array([.02, -.03, .01, -.02, .03, -.01])
parameters, covariance = curve_fit(lambda x, a, b: a*x+b, reference_K, reading_V,
                                  sigma=np.full(6, .05), absolute_sigma=True)
slope, offset = parameters
new_reading_V, reading_sigma_V = 4.4, .05
estimate_K = (new_reading_V - offset) / slope
gradient = np.array([-estimate_K / slope, -1 / slope])
sigma_K = np.sqrt((reading_sigma_V / slope)**2 + gradient @ covariance @ gradient)
assert abs(estimate_K - (4.4-.12)/1.7) < .05 and sigma_K > 0
print(json.dumps({'mode': 'synthetic_standards', 'slope_V_per_K': slope,
                  'offset_V': offset, 'covariance': covariance.tolist(),
                  'estimate_K': estimate_K, 'standard_uncertainty_K': sigma_K}))
