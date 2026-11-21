# Machine learning · 机器学习

表格学习、特征变换和模型比较。

1. 根据真实使用情境划分样本，保留实体、时间或组别关系。预处理与模型组成同一 Pipeline。
2. 先实现能解释输入输出的基线，再选择模型和评价量。保存用于复现预测的完整 pipeline。
3. 需要深度学习时连接已有 PyTorch/JAX 环境，按目标硬件选择上游安装方式；本模块覆盖 scikit-learn。

查看组件与准备方式：`seedenv show machine-learning`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example machine-learning --output learning.py`，然后运行 `seedenv run python-ml -- learning.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://scikit-learn.org/stable/install.html
