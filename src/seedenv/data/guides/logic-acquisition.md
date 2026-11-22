# Logic acquisition · 数字信号与协议采集

Acquire digital channels and decode bus protocols with sigrok.

Select channels, voltage threshold, sample rate and trigger for the actual analyzer. Keep raw captures alongside decoded events. Decoders need clock/data mapping and bit order; saved captures can be processed without connected hardware.

根据设备确定通道、阈值、电平、采样率和触发条件，保留原始 capture 与解码结果。协议解码器需要明确时钟、数据线和位序；离线文件可以在无设备的机器处理。GUI 为可选，Agent 可直接调用 sigrok-cli。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：sigrok-cli (`command-sigrok`).

- [Upstream documentation](https://sigrok.org/wiki/Downloads)
