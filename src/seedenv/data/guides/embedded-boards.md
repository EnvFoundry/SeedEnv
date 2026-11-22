# Embedded measurement boards · 嵌入式测量板

Run board-side measurement programs on an existing MicroPython device.

Select an explicit board ID or serial port. Board code owns pin mapping, voltage conventions, ADC calibration and hardware timing; the host stores results. mpremote actions can interrupt the current board program, so use the intended experiment state.

使用明确的板卡序列号或串口，不使用自动连接第一台设备。板端程序处理引脚、电压、ADC 标定及硬件定时；主机收集结果并标记重启和缺口。mpremote 执行动作可能打断板上当前程序，运行前先确认本次实验的板端状态。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：MicroPython mpremote (`python-mpremote`).

- [Upstream documentation](https://docs.micropython.org/en/latest/reference/mpremote.html)
