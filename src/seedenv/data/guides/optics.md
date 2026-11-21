# Optics basics · 光学基础

多层膜与球形颗粒散射的计算起点。

1. 明确波长、复折射率、入射角、偏振与长度单位。薄膜层顺序和半无限介质应与软件约定一致。
2. tmm 用于平面多层膜，miepython 用于球形颗粒。选择算法先看模型几何与假设。
3. 需要材料库、参数研究、全波仿真或完整研究流程时，选择 optical-lab 模块接入现有专业环境。

查看组件与准备方式：`seedenv show optics`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example optics --output thin_film.py`，然后运行 `seedenv run python-optics -- thin_film.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://github.com/sbyrnes321/tmm
