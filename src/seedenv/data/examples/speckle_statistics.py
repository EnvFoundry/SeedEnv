"""Intensity contrast when independent fully developed speckles are averaged."""
import json
import numpy as np

rng = np.random.default_rng(24)
results = []
for modes in (1, 4, 16):
    field = (rng.normal(size=(modes, 50000)) + 1j * rng.normal(size=(modes, 50000))) / np.sqrt(2)
    intensity = np.mean(np.abs(field) ** 2, axis=0)
    results.append({"independent_modes": modes, "mean_intensity": float(intensity.mean()),
                    "contrast": float(intensity.std() / intensity.mean()), "ideal_contrast": float(1 / np.sqrt(modes))})
print(json.dumps(results))
