# Flow experiments · 流量与气路实验

Read mass-flow controllers together with pressure and temperature conditions.

Select a port and unit address, then read gas, control mode and configured units. Retain measured mass/volume flow, pressure and temperature. Standard volumetric flow depends on reference conditions; connection alone should not change setpoints.

选择明确端口和 unit 地址。读取已配置气体、控制模式和流量单位，记录实际质量流量、体积流量、压力与温度。标准体积流量依赖参考状态；设定流量与出口实际流量并不相同，连接过程不改写设定值。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：Alicat flow controller driver (`python-alicat`).

- [Upstream documentation](https://github.com/numat/alicat)
