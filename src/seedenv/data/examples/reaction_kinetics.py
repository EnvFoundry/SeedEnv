"""Adiabatic equilibrium for an illustrative methane/air mixture."""
import json
import cantera as ct

gas = ct.Solution('gri30.yaml')
gas.TP = 300.0, ct.one_atm
gas.set_equivalence_ratio(1.0, 'CH4', 'O2:1, N2:3.76')
initial_h = gas.enthalpy_mass
gas.equilibrate('HP')
relative_change = abs(gas.enthalpy_mass - initial_h) / max(1.0, abs(initial_h))
print(json.dumps({'mechanism':'gri30.yaml', 'constraint':'constant enthalpy and pressure',
                  'equilibrium_temperature_K':gas.T, 'enthalpy_relative_change':relative_change}))
assert 1500 < gas.T < 3000 and relative_change < 1e-6
