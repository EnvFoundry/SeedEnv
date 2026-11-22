# Parameter measurements · 参数测量与实验数据集

Associate instrument parameters, scan coordinates and measured datasets.

Use Station for existing instruments, Measurement for parameters and setpoints, and DataSaver for a project-local database. Keep instrument configuration and sample context with the data. Reuse existing QCoDeS experiments and full driver APIs.

以 Station 组织已连接仪器，Measurement 声明参数与 setpoints，DataSaver 写入研究项目的数据库。保存仪器配置和样品说明；区分可控制的参数与只能读取的结果。已有 QCoDeS 实验直接连接，不另建一套扫描框架。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：QCoDeS (`python-qcodes`).

- [Upstream documentation](https://microsoft.github.io/Qcodes/)
