# Triggered experiment sequences · 触发与实验序列

Compile experiment timelines and coordinate labscript/BLACS shots.

The connection table represents actual wiring, channels and clocks. Compile timelines into shots and execute through BLACS device workers. Configure the apparatus profile and trigger relationships first. Dummy devices support offline compilation, not claims of physical execution.

connection table 对应实际连线、通道和时钟；labscript 将时间表编译为 shot，BLACS 按设备驱动执行。先配置 apparatus profile 和触发关系，再与已有分析程序衔接。dummy devices 适用于离线编译，不能表示真实设备已完成执行。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：labscript suite (`environment-labscript`).

- [Upstream documentation](https://docs.labscriptsuite.org/en/latest/installation/)
