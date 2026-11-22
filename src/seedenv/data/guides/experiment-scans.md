# Experiment scans · 实验扫描与数据流

Describe readable and settable signals through Ophyd and compose native Bluesky
plans. Preserve start/descriptor/event/stop documents so each observation keeps
its coordinates, units and timestamps. Real devices and EPICS connections come
from the laboratory host; simulated Ophyd devices support offline development.
Choose settling and trigger behavior from the experiment. Hardware-timed loops
belong to their controllers rather than a Python scheduling interval.

设备、扫描计划和事件数据流。

由 Ophyd 设备接口描述可读写信号，再用 Bluesky 编排扫描。示例可用模拟设备；实际仪器驱动、EPICS 等连接单独配置。

Software / 软件：Bluesky / Ophyd (`python-bluesky`).

- [Upstream 1](https://github.com/bluesky/bluesky)
