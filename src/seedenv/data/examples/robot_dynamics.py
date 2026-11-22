"""Headless damped pendulum with native MuJoCo, not a physical robot."""
import json
import numpy as np
import mujoco

model = mujoco.MjModel.from_xml_string('''
<mujoco>
  <option timestep="0.001" gravity="0 0 -9.81">
    <flag energy="enable"/>
  </option>
  <worldbody>
    <body>
      <joint name="pivot" type="hinge" axis="0 1 0" damping="0.1"/>
      <geom type="sphere" pos="0 0 -1" size="0.05" mass="1"/>
    </body>
  </worldbody>
</mujoco>''')
state = mujoco.MjData(model)
state.qpos[0] = 0.3
mujoco.mj_forward(model, state)
initial_energy = float(sum(state.energy))
for _ in range(2000):
    mujoco.mj_step(model, state)
mujoco.mj_forward(model, state)
final_energy = float(sum(state.energy))
assert np.isfinite(state.qpos).all() and final_energy < initial_energy
print(json.dumps({'mode': 'simulation', 'duration_s': float(state.time),
                  'angle_rad': float(state.qpos[0]), 'initial_energy_J': initial_energy,
                  'final_energy_J': final_energy}))
