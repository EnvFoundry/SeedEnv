"""A dimensionless class-B laser model above threshold, with a small seed."""
import json
import numpy as np
from scipy.integrate import solve_ivp

pump, lifetime_ratio = 1.5, 50.0
def rates(time, state):
    inversion, photons = state
    return [(pump - inversion - inversion * photons) / lifetime_ratio,
            (inversion - 1) * photons]

solution = solve_ivp(rates, (0, 3000), [pump, 1e-4], rtol=1e-8, atol=1e-10,
                     t_eval=np.linspace(0, 3000, 3001))
if not solution.success:
    raise RuntimeError(solution.message)
print(json.dumps({"model": "dimensionless class-B laser; time in photon lifetimes",
                  "pump": pump, "final_inversion": float(solution.y[0, -1]),
                  "final_photons": float(solution.y[1, -1]),
                  "stationary_inversion": 1.0, "stationary_photons": pump - 1,
                  "peak_photons": float(solution.y[1].max())}))
