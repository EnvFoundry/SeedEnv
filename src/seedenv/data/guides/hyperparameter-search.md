# Hyperparameter search · 超参数搜索

Explore a defined model or algorithm search space.

Make the objective, budget and data split explicit. Conditional parameters should follow the actual model family; retain completed trials so a restarted study does not repeat finished work.

搜索明确的模型或算法配置空间。

明确目标函数、预算与数据划分。条件参数应符合模型结构；保留已完成试验，使重启后的搜索可以接续。

Software / 软件：Optuna (`python-optuna`).

Use `seedenv context hyperparameter-search` for software entries and setup on this host.

- https://optuna.readthedocs.io/en/stable/
