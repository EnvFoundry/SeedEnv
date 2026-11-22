# Measurement calibration · 测量标定与误差传播

Fit a measurement response from standards and propagate parameter uncertainty.

Keep reference values, raw readings and uncertainties separate. Choose a response model from the measurement mechanism. Errors in the reference require an errors-in-variables treatment. The synthetic example retains slope/intercept covariance for inverse prediction.

将参考值、原始读数与各自不确定度分开保存，选择与仪器机理相符的响应模型。只有观测噪声已给出时才把其当作绝对权重；参考值也有显著误差时采用 errors-in-variables 模型。示例使用合成线性响应，保留斜率与截距的协方差。

Software / 软件：NumPy / SciPy (`python-numerics`).

- [Upstream documentation](https://docs.scipy.org/doc/scipy/)
