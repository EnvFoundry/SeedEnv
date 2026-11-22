# Source-measure sweeps · 源表与器件电学扫描

Acquire device current–voltage sweeps and source-measure readbacks.

Select the model-specific SMU driver. Supply wiring mode, source mode, ranges, compliance, integration time and settling time. Store measured voltage and current alongside setpoints; distinguish hysteresis, contact resistance and self-heating from device response.

使用对应型号的源表驱动，例如 Keithley 2400。实验配置给出接线方式、源模式、量程、compliance、积分时间和每点等待时间。保存命令值与实际电流电压；扫描顺序、迟滞、接触电阻和自热都可能改变曲线。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：PyMeasure (`python-pymeasure`).

- [Upstream documentation](https://pymeasure.readthedocs.io/en/latest/api/instruments/keithley/keithley2400.html)
