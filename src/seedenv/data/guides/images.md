# Image processing · 图像处理

图像读写、滤波、分割与定量分析。

1. 明确像素尺寸、位深、通道次序和强度范围，保留原始图像。
2. 先选择需要测量的量，再组织预处理、分割或特征提取；每步保留对后续量的影响。
3. 使用完整 scikit-image 和 Pillow 接口；批处理脚本保持文件名与输出关联。

查看组件与准备方式：`seedenv show images`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example images --output images.py`，然后运行 `seedenv run python-images -- images.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://scikit-image.org/docs/stable/user_guide/install.html
