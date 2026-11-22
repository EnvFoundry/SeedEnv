# Camera acquisition · 工业相机采集

Use Harvesters with the camera vendor's GenTL producer. Choose a named device and
retain pixel format, exposure, trigger mode and device timestamps with each frame.
Copy data needed after returning an acquisition buffer; record missing frames
and separate sensor time from host arrival time. The GenTL producer must match
the OS and process architecture. Connecting a camera does not calibrate pixel
size, radiometric response or the camera-to-sample coordinate transform.

通过 GenICam/GenTL 连接已有工业相机。

连接与系统和进程架构对应的 GenTL producer，选定设备并保留像素格式、曝光、触发和设备时间戳。归还采集缓冲区前复制需要保留的数据，记录缺帧；像素尺度、响应和样品坐标变换需另行标定。

Software / 软件：Harvesters (`python-harvesters`).

- [Upstream 1](https://github.com/genicam/harvesters)
