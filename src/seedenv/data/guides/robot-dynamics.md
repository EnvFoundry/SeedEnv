# Robot dynamics simulation · 机器人动力学仿真

Simulate articulated bodies, contacts and actuators with MuJoCo.

Define mass, inertia, joints and actuators in MJCF or an existing asset. Use MjModel, MjData and mj_step directly. Relate model parameters to measured equipment. The included headless pendulum is a simulation, not a physical robot result.

由 MJCF 或已有模型定义质量、惯量、关节和执行器，直接使用 MjModel/MjData 与 mj_step。先建立观测与控制量的单位和时间步；仿真参数需要来自真实系统辨识。附带程序为无图形界面的单摆，结果不是实体机器人的性能。

Software / 软件：MuJoCo (`python-mujoco`).

- [Upstream documentation](https://mujoco.readthedocs.io/en/stable/python.html)
