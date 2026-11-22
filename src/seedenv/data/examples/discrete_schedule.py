"""Select indivisible jobs under a small synthetic capacity budget."""
import json
from ortools.sat.python import cp_model

weights, values, capacity = [2, 3, 4], [3, 4, 5], 5
model = cp_model.CpModel()
chosen = [model.new_bool_var(f'job_{i}') for i in range(3)]
model.add(sum(w * x for w, x in zip(weights, chosen)) <= capacity)
model.maximize(sum(v * x for v, x in zip(values, chosen)))
solver = cp_model.CpSolver()
status = solver.solve(model)
assert status == cp_model.OPTIMAL
selection = [i for i, x in enumerate(chosen) if solver.value(x)]
print(json.dumps({'inputs':'synthetic jobs', 'chosen':selection, 'objective':solver.objective_value}))
assert selection == [0, 1] and solver.objective_value == 7
