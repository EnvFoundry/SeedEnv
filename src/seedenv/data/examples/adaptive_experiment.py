"""Measure a virtual detector, choose the next point and retain observations."""
import json
import math
from bluesky import RunEngine
from bluesky import plans
from ophyd.sim import SynAxis, SynSignal
from scipy.optimize import minimize_scalar

motor = SynAxis(name='position')
detector = SynSignal(name='intensity', func=lambda: math.exp(-((motor.position-.7)/.45)**2))
engine = RunEngine({})
observations = []

def record(name, document):
    if name == 'event':
        observations.append({'position': document['data']['position'],
                             'intensity': document['data']['intensity'],
                             'time': document['time']})

engine.subscribe(record)

def objective(position):
    engine(plans.list_scan([detector], motor, [float(position)]))
    return -observations[-1]['intensity']

result = minimize_scalar(objective, bounds=(-2, 2), method='bounded',
                         options={'xatol': 1e-4, 'maxiter': 40})
assert result.success and abs(result.x - .7) < 1e-3
print(json.dumps({'mode': 'virtual_devices', 'optimum': result.x,
                  'observations': observations}))
