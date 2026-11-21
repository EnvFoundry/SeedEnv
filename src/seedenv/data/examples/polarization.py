"""Malus' law for a normalized horizontal Jones state and a 45-degree polarizer."""
import json
from math import pi
from py_pol.jones_vector import Jones_vector
from py_pol.jones_matrix import Jones_matrix

incident = Jones_vector('incident')
incident.linear_light(azimuth=0)
polarizer = Jones_matrix('polarizer')
polarizer.diattenuator_perfect(azimuth=pi / 4)
intensity = (polarizer * incident).parameters.intensity()
print(json.dumps({"transmitted_fraction": float(intensity.item()), "ideal_fraction": 0.5}))
