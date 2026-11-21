# Instrument connections · 仪器连接

通过已有 VISA 后端连接仪器。

1. 确认设备、地址及其编程手册，选择本机已有 VISA 或 pyvisa-py 后端。
2. 先读取设备身份与状态，再按实验需要发送命令；设备驱动与总线支持取决于实际硬件。
3. 多设备共享、持续实验和平台编排通过 IOP 连接，保留既有设备会话。

查看组件与准备方式：`seedenv show instruments`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

上游文档：

- https://pyvisa.readthedocs.io/en/latest/introduction/getting.html
