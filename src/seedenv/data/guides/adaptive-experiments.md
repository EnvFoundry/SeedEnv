# Adaptive experiments · 自适应实验采集

Connect measurement, analysis and the next experimental point in an editable loop.

Acquire through Bluesky plans, analyze the observations and choose the next point. Define controllable variables, settling time and stopping conditions. The example optimizes a virtual unimodal detector response and retains every observation; real experiments may be noisy, drifting or multimodal.

通过 Bluesky plan 取得观测，分析程序给出下一点，再由同一设备接口采集。明确可控变量、观测量、范围、等待时间和终止条件；噪声和漂移决定是否需要重复测量。示例寻找虚拟探测器响应峰，保留全部观测，不宣称一般实验都满足单峰假设。

Software / 软件：Bluesky / Ophyd (`python-bluesky`).

- [Upstream documentation](https://github.com/bluesky/bluesky)
