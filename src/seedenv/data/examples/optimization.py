"""Allocate a nonnegative budget to a least-squares target."""
import json
import cvxpy as cp
import numpy as np

x=cp.Variable(3, nonneg=True)
target=np.array([.2,.5,.3])
problem=cp.Problem(cp.Minimize(cp.sum_squares(x-target)),[cp.sum(x)==1])
problem.solve()
print(json.dumps({"state":problem.status, "allocation":x.value.tolist(), "objective":problem.value}))
