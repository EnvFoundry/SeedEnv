# CAN devices · CAN 总线设备

Exchange timestamped frames with CAN-connected equipment.

The host selects adapter, channel and bitrate. Interpret identifiers and bytes through the device protocol, preserving timestamps and error state. The included example uses an in-process virtual bus and never transmits to physical equipment.

由宿主指定适配器、通道和 bitrate；报文 ID 与数据字节的物理意义来自设备协议。记录时间戳和错误状态，按设备协议解释多帧结果。附带程序在 virtual 总线上收发，不会连接或发送到真实设备。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：python-can (`python-can`).

- [Upstream documentation](https://python-can.readthedocs.io/en/stable/)
