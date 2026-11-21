# Medical image data · 医学图像数据

NIfTI、DICOM 与体数据的读取和组织。

1. 保留体素间距、方向和仿射变换；数组索引与物理坐标分开处理。
2. NiBabel 操作 NIfTI，pydicom 读取 DICOM 元数据与数据；压缩像素可能需要相应解码库。
3. 重采样与图像处理时记录坐标变换，输出图像继续保留空间信息。

查看组件与准备方式：`seedenv show medical-imaging`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example medical-imaging --output medical_images.py`，然后运行 `seedenv run python-medical-images -- medical_images.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://nipy.org/nibabel/installation.html
