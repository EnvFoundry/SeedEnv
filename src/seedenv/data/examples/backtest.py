"""A synthetic market illustrates the API; it is not a market-performance claim."""
import json
import numpy as np
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

class MovingAverage(Strategy):
    def init(self):
        self.fast = self.I(lambda x: pd.Series(x).rolling(10).mean(), self.data.Close)
        self.slow = self.I(lambda x: pd.Series(x).rolling(30).mean(), self.data.Close)
    def next(self):
        if crossover(self.fast, self.slow):
            self.buy(size=1)
        elif crossover(self.slow, self.fast):
            self.position.close()

price = 100 * np.exp(np.cumsum(np.random.default_rng(7).normal(0.0005, 0.01, 400)))
data = pd.DataFrame({"Open":price, "High":price*1.01, "Low":price*.99, "Close":price, "Volume":1000},
                    index=pd.date_range("2020-01-01", periods=len(price), freq="B"))
result = Backtest(data, MovingAverage, cash=10000, commission=.002, exclusive_orders=True).run()
print(json.dumps({"data":"synthetic", "trades":int(result["# Trades"]), "return_percent":float(result["Return [%]"])}))
