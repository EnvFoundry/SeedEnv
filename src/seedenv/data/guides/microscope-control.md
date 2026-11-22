# Microscope acquisition · 显微镜自动采集

Acquire microscope channels, focal planes and time series.

Connect the saved Micro-Manager hardware configuration. Use Acquisition for events and Core for native control. Preserve exposure, pixel size, focal position, channel and acquisition time; focus drift and photobleaching remain experiment-specific.

连接已有 Micro-Manager 配置，确认相机、XY/Z 台和光源的设备标签与单位。Acquisition 编排事件，Core 调用底层能力。保留曝光、像素尺寸、焦面坐标、通道和时间；实验中焦漂与光漂白需要由研究方案处理。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：Pycro-Manager (`python-pycromanager`).

- [Upstream documentation](https://pycro-manager.readthedocs.io/en/latest/setup.html)
