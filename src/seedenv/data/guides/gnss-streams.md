# GNSS field data · GNSS 与野外定位数据

Parse receiver streams and associate field measurements with position and time.

Read saved files or an explicit receiver stream. Preserve fix type, datum, time scale and quality fields. Latitude/longitude/height are not local Cartesian coordinates. Account for sensor timing and antenna offsets when joining field observations.

从已保存文件或指定串口读取 UBX/NMEA/RTCM 消息，保留定位类型、坐标基准、时间尺度和质量字段。经纬高不是局部直角坐标；组合其他传感器时处理时钟偏差、天线偏置与缺失定位。读取保存数据不需要在线设备。

Software / 软件：pyubx2 (`python-pyubx2`).

- [Upstream documentation](https://github.com/semuconsulting/pyubx2)
