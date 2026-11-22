# Synchronized streams · 多设备数据流同步

Combine sensor streams and event markers using Lab Streaming Layer.

Record source IDs, channel labels, units, rates and clock origin. Put event markers in a separate stream and retain original timestamps alongside clock correction. Stream synchronization does not replace hardware triggering or remove sensor latency.

为每个流记录 source_id、通道名、单位、采样率和时钟来源，事件标记使用单独流。用时间修正处理主机时钟偏差，并保留原始时间。LSL 传输同步不代替硬件触发，也不保证传感器自身没有固定延迟。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：Lab Streaming Layer · 同步数据流 (`python-pylsl`).

- [Upstream documentation](https://github.com/labstreaminglayer/pylsl)
