# Strategy backtesting · 策略回测

用历史或自备行情研究策略与交易成本。

1. 输入明确的 OHLC 数据，统一时区、复权方式与交易日历。信号只能使用当时已可获得的数据。
2. 写出成交时点、佣金与滑点假设，保留持仓和逐笔交易，再比较不同时段。
3. 行情账户和实盘交易连接由用户独立选择；这个起步模块运行离线回测。

查看组件与准备方式：`seedenv show backtesting`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example backtesting --output backtest.py`，然后运行 `seedenv run python-backtesting -- backtest.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://kernc.github.io/backtesting.py/
