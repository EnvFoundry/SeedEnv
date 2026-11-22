# Temperature experiments · 温控与热学测量

Read temperature sensors and coordinate settled thermal measurements.

Use the controller-specific driver and sensor calibration. A controller reading is not automatically the sample temperature. The experiment supplies heater range, ramp rate and settling interval. Read the current configuration before changing a running experiment.

对应驱动和传感器曲线决定读数含义；温控器读数不自动等于样品温度。由实验配置提供加热范围、升降温速率、稳定窗口和等待时间，记录传感器通道、设定温度及实际读数。先读现有配置，避免连接时重设已有实验。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：PyMeasure (`python-pymeasure`).

- [Upstream documentation](https://pymeasure.readthedocs.io/en/latest/api/instruments/lakeshore/index.html)
