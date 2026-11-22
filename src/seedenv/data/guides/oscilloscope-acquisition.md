# Oscilloscope acquisition · 示波器波形采集

Acquire triggered waveforms with their scaling and time axes.

Read waveform blocks and preambles through the supported model driver. Reconstruct units and time axes from scale, offset and sample interval; retain probe attenuation, bandwidth and trigger settings. A screen image does not contain the original waveform samples.

用真实型号支持的波形接口读取二进制块及其 preamble。按照仪器给出的增益、偏移和时间步长还原波形，保留探头衰减、带宽、采样率及触发条件。显示截图不能代替原始波形；不同通道的延迟需按实验处理。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：PyMeasure (`python-pymeasure`).

- [Upstream documentation](https://pymeasure.readthedocs.io/en/stable/api/instruments/keysight/keysightDSOX1102G.html)
