"""A one-particle harmonic oscillator, using OpenMM's CPU reference platform."""
import json
import openmm as mm
from openmm import unit

system = mm.System()
system.addParticle(1 * unit.dalton)
force = mm.CustomExternalForce('0.5*k*(x*x+y*y+z*z)')
force.addGlobalParameter('k', 100.0)
force.addParticle(0, [])
system.addForce(force)
integrator = mm.VerletIntegrator(0.0001 * unit.picoseconds)
context = mm.Context(system, integrator, mm.Platform.getPlatformByName('Reference'))
context.setPositions([[0.1, 0, 0]] * unit.nanometer)
context.setVelocities([[0, 0, 0]] * unit.nanometer / unit.picosecond)
initial = context.getState(getEnergy=True).getPotentialEnergy().value_in_unit(unit.kilojoule_per_mole)
integrator.step(1000)
state = context.getState(getEnergy=True, getPositions=True)
total = (state.getPotentialEnergy() + state.getKineticEnergy()).value_in_unit(unit.kilojoule_per_mole)
print(json.dumps({'model':'illustrative harmonic oscillator', 'initial_kj_mol':initial,
                  'final_total_kj_mol':total, 'x_nm':state.getPositions().value_in_unit(unit.nanometer)[0].x}))
assert abs(total - initial) < 1e-5
