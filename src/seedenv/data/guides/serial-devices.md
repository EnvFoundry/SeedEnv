# Serial devices · 串口设备连接

Communicate with serial instruments and controllers.

Use the instrument protocol for baud rate, framing, terminators and timing. Parse complete replies and keep command-response pairing; opening a port does not establish that the attached device is the intended instrument.

连接串口仪器与控制器。

按设备协议设置波特率、帧、终止符和时序。解析完整响应并保持命令对应；打开串口本身不能确定设备身份。

Software / 软件：pySerial (`python-serial`).

Use `seedenv context serial-devices` for software entries and setup on this host.

- https://pyserial.readthedocs.io/en/latest/
