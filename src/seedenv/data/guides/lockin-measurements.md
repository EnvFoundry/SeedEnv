# Lock-in measurements · 锁相测量

Measure in-phase and quadrature signals at a reference frequency.

Read X/Y or amplitude/phase using the model-specific driver. Preserve reference frequency, harmonic, time constant, filter slope and input range. Allow the filter to settle after changes and state the amplitude convention used.

以实际 SR830/SR860 等型号驱动读取 X/Y 或幅值相位，同时保存参考频率、谐波、时间常数、滤波斜率和输入范围。每次改变参数后按滤波响应等待；输出幅值的 RMS/峰值定义与带宽决定实验解释。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：PyMeasure (`python-pymeasure`).

- [Upstream documentation](https://pymeasure.readthedocs.io/en/latest/api/instruments/srs/sr830.html)
