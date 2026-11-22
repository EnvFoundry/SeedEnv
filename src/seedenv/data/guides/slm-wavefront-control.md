# SLM wavefront control · 空间光调制与波前整形

Use the hardware backend matching the SLM and camera. Keep display pixels, phase
response at the chosen wavelength and camera coordinates distinct. Save the
phase calibration, coordinate mapping and raw feedback frames with the project.
Hologram optimization can begin in simulation; writing a pattern to a physical
SLM is an explicit experiment operation. Pixel pitch, polarization and optical
alignment affect how the programmed phase maps to the measured field.

SLM 相位、全息图和相机反馈。

把显示像素、SLM 相位响应和相机坐标映射分开。硬件后端由真实型号决定；保存标定映射与原始帧，并用模拟模式先构建程序。

Software / 软件：slmsuite (`python-slmsuite`).

- [Upstream 1](https://github.com/holodyne/slmsuite)
