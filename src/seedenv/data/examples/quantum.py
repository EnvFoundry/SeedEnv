"""Two-level coherent evolution with hbar=1."""
import json
import numpy as np
from qutip import basis, sigmax, sigmaz, sesolve

t=np.linspace(0,2*np.pi,101)
result=sesolve(sigmax()/2,basis(2,0),t,e_ops=[sigmaz()])
print(json.dumps({"samples":len(t), "max_error_against_cos":float(np.max(abs(result.expect[0]-np.cos(t))))}))
