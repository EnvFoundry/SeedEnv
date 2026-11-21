# Geospatial and remote sensing · 地理与遥感

矢量、栅格与多维时空数据。

1. 先读取坐标参考系、空间分辨率、时间坐标和缺失值。经纬度不能直接作为米制距离。
2. GeoPandas 处理矢量，Rasterio 读写栅格，xarray 组织带坐标的多维数组。
3. 叠加前统一坐标系统；大范围任务按窗口或分块处理。

查看组件与准备方式：`seedenv show geospatial`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example geospatial --output geospatial.py`，然后运行 `seedenv run python-geospatial -- geospatial.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://geopandas.org/en/stable/getting_started/install.html
