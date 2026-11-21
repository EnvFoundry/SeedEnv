"""Undepleted plane-wave SHG phase-matching factor; illustrative dispersion."""
import json
import numpy as np

# These are illustrative refractive indices, not a material data record.
wavelength_m = 1.064e-6
n_fundamental, n_second_harmonic = 1.50, 1.55
length_m = 1e-3
delta_k = 4 * np.pi * (n_second_harmonic - n_fundamental) / wavelength_m
qpm_period_m = 2 * np.pi / delta_k
factor = lambda mismatch: float(np.sinc(mismatch * length_m / (2 * np.pi)) ** 2)
print(json.dumps({"assumption": "undepleted monochromatic plane waves; illustrative indices",
                  "delta_k_per_m": float(delta_k), "coherence_length_m": float(np.pi / abs(delta_k)),
                  "first_order_qpm_period_m": float(qpm_period_m),
                  "uncompensated_phase_factor": factor(delta_k),
                  "matched_phase_factor": factor(delta_k - 2 * np.pi / qpm_period_m),
                  "note": "Absolute efficiency also needs nonlinear coefficient, pump intensity, overlap and losses."}))
