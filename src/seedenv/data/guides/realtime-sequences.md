# Real-time sequences · 实时时序实验

Run hardware-timed experiments through an existing ARTIQ host.

Map the core and TTL/DDS channels in device_db.py. Kernels own deterministic timing; host code handles analysis. Account for device latency and RTIO scheduling. Use software matching the existing gateware; environment preparation does not flash equipment.

device_db.py 关联真实 core、TTL、DDS 等通道；内核负责确定时序，主机负责数据处理。实验时间表应反映器件延迟和 RTIO 调度，普通 Python sleep 无法替代。使用与设备 gateware 对应的环境；安装 SeedEnv 不触发烧录。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：ARTIQ (`command-artiq`).

- [Upstream documentation](https://m-labs.hk/artiq/manual/installing.html)
