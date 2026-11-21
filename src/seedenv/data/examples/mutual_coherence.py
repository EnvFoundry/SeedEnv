"""Propagate a partially coherent two-mode field through a lossless mixer."""
import json
import numpy as np

intensities = np.array([1.0, 0.6])
degree = 0.4 * np.exp(0.3j)
cross = degree * np.sqrt(np.prod(intensities))
coherence = np.array([[intensities[0], cross], [cross.conjugate(), intensities[1]]])
mixer = np.array([[1, 1j], [1j, 1]]) / np.sqrt(2)
output = mixer @ coherence @ mixer.conj().T
weights = np.linalg.eigvalsh(coherence)
print(json.dumps({"input_intensity": intensities.tolist(),
                  "output_intensity": output.diagonal().real.tolist(),
                  "coherent_mode_weights": weights.tolist(),
                  "input_power": float(np.trace(coherence).real),
                  "output_power": float(np.trace(output).real)}))
