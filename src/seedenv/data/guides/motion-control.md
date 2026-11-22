# Motion control · 位移台与运动控制

Connect motion controllers and read actual stage positions.

Select the controller backend and define axes, physical units, origin and travel limits. Homing is a movement, not a connection step. Acquire after motion completion and retain readback position and approach direction. Map sample/camera frames through calibration.

先确认控制器型号、轴映射、步数与物理单位、零点和软限位，再执行实验所需移动。回零会真实移动，不应作为连接操作。等待运动完成后采样，记录读回位置及回程方向；跨相机和样品坐标使用独立标定。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：pylablib (`python-pylablib`).

- [Upstream documentation](https://pylablib.readthedocs.io/en/stable/devices/stages_root.html)
