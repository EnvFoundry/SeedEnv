# Spectrometer acquisition · 光谱仪采集

Select the supported spectrometer and USB backend through python-seabreeze. Read
its identity and wavelength mapping, then use the experiment's integration time
and trigger mode. Preserve raw counts, dark measurements and acquisition settings.
Radiometric units require response calibration; clipping, detector nonlinearity
and stray light are not removed merely by subtracting a background. The Python
interface and OS-specific USB access are separate preparation steps.

连接受支持光谱仪并读取光谱。

先读设备身份与波长映射，再设置积分时间与触发。保存原始计数、暗背景和设备设置；计数转辐射量需配套响应数据。

Software / 软件：python-seabreeze (`python-seabreeze`).

- [Upstream 1](https://github.com/ap--/python-seabreeze)
