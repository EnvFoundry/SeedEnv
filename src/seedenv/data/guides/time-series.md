# Time series and econometrics · 时间序列与计量

时间索引、回归、时序模型和预测误差。

1. 明确时间戳、频率、时区及一个记录何时实际可获得。按时间先后划分拟合区间和后续区间。
2. 先比较简单基线，再选择回归或时序模型。保留趋势、季节性和外生变量的含义。
3. 估计、预测和策略收益属于不同计算；用独立输出说明各自结果。

查看组件与准备方式：`seedenv show time-series`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example time-series --output time_series.py`，然后运行 `seedenv run python-statistics -- time_series.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://www.statsmodels.org/stable/install.html
