# EPICS process variables · EPICS 过程变量

Connect to laboratory EPICS process variables.

Read units, limits and timestamps with each process variable. Use the laboratory naming and connection configuration; asynchronous callbacks should not block acquisition or silently replace newer readings.

连接实验室 EPICS 过程变量。

读取过程变量时保留单位、限制和时间戳。采用实验室命名与连接配置，异步回调避免阻塞采集或覆盖更新观测。

Software / 软件：PyEPICS (`environment-epics`).

Use `seedenv context epics-controls` for software entries and setup on this host.

- https://pyepics.github.io/pyepics/installation.html
