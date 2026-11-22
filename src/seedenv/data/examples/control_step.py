"""Unit-step response of an illustrative stable first-order system."""
import json
import numpy as np
import control as ct

system = ct.tf([1], [1, 1])
t, y = ct.step_response(system, T=np.linspace(0, 10, 501))
error = float(np.max(np.abs(y - (1 - np.exp(-t)))))
print(json.dumps({'system':'1/(s+1)', 'final_output':float(y[-1]), 'analytic_max_error':error}))
assert error < 1e-10
