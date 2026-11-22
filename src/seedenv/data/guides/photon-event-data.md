# Photon event data · 单光子事件数据

Read time-tagged photon files and preserve detector and timing metadata.

Choose the loader for the acquisition format. Retain macrotime, nanotime units, detector IDs and excitation period. Overflow and dead-time treatment matter for lifetime/correlation analysis; file conversion alone does not complete those corrections.

按原始文件类型选择 loader，保留宏时间、微时间、计数单位、探测器编号和激光重复周期。计数器溢出与死时间会影响寿命和关联分析；转换格式不等于完成这些修正。此模块处理实验文件，不安装采集卡驱动。

Software / 软件：phconvert (`python-phconvert`).

- [Upstream documentation](https://phconvert.readthedocs.io/en/latest/)
