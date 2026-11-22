# Modbus devices · 工业与实验传感器

Read laboratory or industrial registers over Modbus TCP or serial.

Build the register map from the device manual: address, offset, word order, signedness, scale and units. Serialize requests per client. Distinguish transport timeouts from device exceptions; writes belong to the specific experiment.

从设备手册建立寄存器表：设备地址、寄存器偏移、字节序、符号、缩放和单位。保持客户端请求串行；timeout 与设备返回的异常分别处理。先读取明确选定的寄存器，写寄存器应由具体实验指定。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：PyModbus (`python-pymodbus`).

- [Upstream documentation](https://pymodbus.readthedocs.io/en/stable/source/client.html)
