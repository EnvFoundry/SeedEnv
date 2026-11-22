# DAQ streams · 连续数据采集

Read multichannel samples with device-provided time domains.

Select a device connection string, inspect signal and domain descriptors, and create a reader. Retain channel units, sample rate, device timestamps and gaps. Packet arrival time is not acquisition time; the reference device is a simulator.

使用设备连接字符串选择采集设备，读取 signal descriptor 和 domain signal 后建立 reader。保留采样率、单位、通道映射、设备时间戳与丢样信息；客户端收到数据的时间不能代替采样时刻。reference device 仅用于软件模拟。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：openDAQ (`python-opendaq`).

- [Upstream documentation](https://opendaq.github.io/opendaq/dev/tutorials/quick_start_setting_up_python.html)
