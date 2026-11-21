# Astronomy · 天文计算

物理单位、坐标、时间与天文数据格式。

1. 使用带单位的物理量，明确参考坐标系和时间尺度。
2. Astropy 提供 FITS、坐标变换与常见计算；数据选择与具体模型另按研究任务组织。
3. 保存结果的单位与坐标元数据，避免裸数值在跨程序传递中丢失含义。

查看组件与准备方式：`seedenv show astronomy`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example astronomy --output astronomy.py`，然后运行 `seedenv run python-astronomy -- astronomy.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://docs.astropy.org/en/stable/install.html
