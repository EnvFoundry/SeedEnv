# Instrument procedures · 仪器测量程序

Build editable measurement procedures with instrument drivers and result records.

Choose the instrument class and adapter for the actual model. Define Procedure parameters and its startup, execution and shutdown operations. Record setpoints, readbacks, units and time together; acquisition cadence is independent of GUI refresh.

先选择实际型号的 Instrument 类和适配器，再定义 Procedure 的参数、启动、采样和结束操作。每条数据同时保留设定值、读回值、单位和时间。硬件步进与 GUI 显示频率分开；退出程序时按实验要求结束输出。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：PyMeasure (`python-pymeasure`).

- [Upstream documentation](https://pymeasure.readthedocs.io/en/latest/tutorial/procedure.html)
