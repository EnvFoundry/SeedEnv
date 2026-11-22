# Robot connections · 机器人与 ROS 2

Connect existing robot nodes, sensor topics and action interfaces.

Run the native ROS 2 interface on its activated worker. Preserve domain, namespace, QoS and frame conventions. Read the existing state before invoking task-specific actions. Robot drivers and controllers retain responsibility for trajectories, timing and stop behavior.

在已激活 ROS 工作空间的执行主机上使用完整 ros2 接口；保留 domain、namespace、QoS 和坐标系约定。先读取已有节点与状态，再由具体任务调用 action 或控制器。机器人驱动、控制频率、轨迹和停止机制属于该机器人系统，不由通用提示词替代。

Software preparation leaves the laboratory connection with the host. Use the named device selected for this task; keep acquisition data in the project.
软件准备后，由宿主连接本任务选定的设备；采集数据保存在研究项目内。

Software / 软件：ROS 2 (`command-ros2`).

- [Upstream documentation](https://github.com/ros2/ros2_documentation)
