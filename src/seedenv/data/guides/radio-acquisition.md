# Radio signal acquisition · 射频信号采集

Acquire complex radio samples through a native SoapySDR driver.

Choose receiver/channel, center frequency, sample rate, gain, antenna and clock. Preserve I/Q samples, timestamps and overflow information. Absolute power requires receive-chain calibration. This task starts with reception; transmission is a separate experiment.

选择明确的接收设备和通道，记录中心频率、采样率、增益、天线与时钟源。使用接收流获取 I/Q，并保留溢出和时间戳信息；数值幅度需要经过接收链标定才能解释为绝对功率。发射不是采集模块的默认操作。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：SoapySDR (`environment-soapysdr`).

- [Upstream documentation](https://github.com/pothosware/SoapySDR/wiki)
