# Research catalogue · 研究目录

Fields and directions are navigation. Select individual tasks; shared software is prepared once.
领域和方向用于导航。按任务选装，跨领域共享同一软件；关联资源单独展示。

198 distinct task modules · 8 related resources / 198 个不同任务模块 · 8 个关联资源

| Entry / 入口 | Group / 类型 | Directions / 方向 | Distinct tasks / 不同任务 | Related resources / 关联资源 |
| --- | --- | ---: | ---: | ---: |
| Optics & photonics · 光学与光子学 | Research / 研究领域 | 13 | 63 | 3 |
| Mathematics · 数学 | Research / 研究领域 | 4 | 15 | 0 |
| AI & computing · AI 与计算 | Research / 研究领域 | 5 | 20 | 1 |
| Physics · 物理 | Research / 研究领域 | 5 | 29 | 1 |
| Chemistry · 化学 | Research / 研究领域 | 6 | 20 | 1 |
| Materials · 材料 | Research / 研究领域 | 5 | 23 | 1 |
| Life sciences · 生命科学 | Research / 研究领域 | 7 | 31 | 1 |
| Medicine · 医学研究 | Research / 研究领域 | 5 | 20 | 1 |
| Pharmaceutical research · 医药研究 | Research / 研究领域 | 5 | 21 | 2 |
| Mechanical engineering · 机械工程 | Research / 研究领域 | 6 | 26 | 0 |
| Electronics · 电子 | Research / 研究领域 | 6 | 23 | 0 |
| Earth & environment · 地球与环境 | Research / 研究领域 | 6 | 22 | 0 |
| Astronomy & space · 天文与空间 | Research / 研究领域 | 5 | 18 | 1 |
| Economics & finance · 经济与金融 | Research / 研究领域 | 5 | 16 | 1 |
| Experimental science · 实验科学 | Shared / 公共能力 | 7 | 42 | 1 |
| Research essentials · 通用研究工具 | Shared / 公共能力 | 4 | 14 | 1 |

Counts within a field deduplicate repeated tasks. A task can appear in several fields, so field counts do not sum to the global total.
领域内按不同模块计数；同一模块可出现在多个领域，不能把各行相加作为全局模块数。

“Prepare” identifies an installation route, not a claim that every platform has been exercised. Conda routes use an existing micromamba, mamba or conda. Native executables, accelerator runtimes and accounts retain their explicit connection steps.
“安装”表示已有准备方式，不表示所有平台都已逐项运行。Conda 配方使用已有管理器；原生程序、加速运行环境与账户保留明确的连接步骤。

## Optics & photonics · 光学与光子学

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Geometrical optics · 几何光学 | [Paraxial systems · 近轴光路](../src/seedenv/data/guides/paraxial-optics.md) · `paraxial-optics` | RayTracing (pip) |
| Geometrical optics · 几何光学 | [Lens design · 镜头设计与优化](../src/seedenv/data/guides/lens-design.md) · `lens-design` | Optiland (pip) |
| Geometrical optics · 几何光学 | [Lens prescriptions · 镜头处方与成像分析](../src/seedenv/data/guides/lens-prescriptions.md) · `lens-prescriptions` | RayOptics (pip) |
| Geometrical optics · 几何光学 | [Radiometry · 辐射度与非顺序光线](../src/seedenv/data/guides/radiometry.md) · `radiometry` | Raysect (bind interpreter / 连接解释器) |
| Wave optics & imaging · 波动光学与成像 | [Scalar propagation · 标量衍射与光束传播](../src/seedenv/data/guides/scalar-propagation.md) · `scalar-propagation` | LightPipes (pip) |
| Wave optics & imaging · 波动光学与成像 | [Vector diffraction · 矢量衍射与聚焦](../src/seedenv/data/guides/vector-diffraction.md) · `vector-diffraction` | Diffractio (pip) |
| Wave optics & imaging · 波动光学与成像 | [Fourier imaging · 傅里叶成像与点扩散函数](../src/seedenv/data/guides/fourier-imaging.md) · `fourier-imaging` | POPPY (pip) |
| Wave optics & imaging · 波动光学与成像 | [Wavefront analysis · 波前与成像质量](../src/seedenv/data/guides/wavefront-analysis.md) · `wavefront-analysis` | prysm (pip) |
| Wave optics & imaging · 波动光学与成像 | [Adaptive optics · 自适应光学](../src/seedenv/data/guides/adaptive-optics.md) · `adaptive-optics` | HCIPy (pip) |
| Wave optics & imaging · 波动光学与成像 | [Polarization · 偏振与穆勒矩阵](../src/seedenv/data/guides/polarization.md) · `polarization` | py-pol (pip) |
| Statistical optics · 统计光学 | [Mutual coherence · 经典统计光学与相干性](../src/seedenv/data/guides/mutual-coherence.md) · `mutual-coherence` | NumPy / SciPy (pip) |
| Statistical optics · 统计光学 | [Speckle statistics · 散斑与强度统计](../src/seedenv/data/guides/speckle-statistics.md) · `speckle-statistics` | NumPy / SciPy (pip) |
| Statistical optics · 统计光学 | [Photon correlations · 光子关联与量子统计](../src/seedenv/data/guides/photon-correlations.md) · `photon-correlations` | QuTiP · 量子动力学 (pip) |
| Films & scattering · 薄膜与散射 | [Thin films · 多层薄膜](../src/seedenv/data/guides/thin-films.md) · `thin-films` | tmm (pip) |
| Films & scattering · 薄膜与散射 | [Sphere scattering · 球形颗粒散射](../src/seedenv/data/guides/sphere-scattering.md) · `sphere-scattering` | miepython (pip) |
| Films & scattering · 薄膜与散射 | [Multiple scattering · 多体散射与 T 矩阵](../src/seedenv/data/guides/multiple-scattering.md) · `multiple-scattering` | treams (pip) |
| Films & scattering · 薄膜与散射 | [Particles near layers · 层状介质中的颗粒散射](../src/seedenv/data/guides/layered-particle-scattering.md) · `layered-particle-scattering` | SMUTHI (bind interpreter / 连接解释器) |
| Films & scattering · 薄膜与散射 | [Discrete dipoles · 离散偶极散射](../src/seedenv/data/guides/discrete-dipoles.md) · `discrete-dipoles` | ADDA (connect command / 连接程序) |
| Nanophotonics · 纳米光子学与电磁场 | [FDTD · 全波时域计算](../src/seedenv/data/guides/fdtd.md) · `fdtd` | Meep / MPB (conda / bind) |
| Nanophotonics · 纳米光子学与电磁场 | [Photonic bands · 光子晶体能带与模态](../src/seedenv/data/guides/photonic-bands.md) · `photonic-bands` | Meep / MPB (conda / bind) |
| Nanophotonics · 纳米光子学与电磁场 | [Periodic RCWA · 周期光栅与超表面](../src/seedenv/data/guides/periodic-rcwa.md) · `periodic-rcwa` | grcwa (pip) |
| Nanophotonics · 纳米光子学与电磁场 | [Photonic slab modes · 光子晶体薄板模态](../src/seedenv/data/guides/slab-bands.md) · `slab-bands` | Legume (pip) |
| Nanophotonics · 纳米光子学与电磁场 | [Inverse electromagnetics · 电磁逆向设计](../src/seedenv/data/guides/inverse-electromagnetics.md) · `inverse-electromagnetics` | Ceviche (pip) |
| Optoelectronic devices · 光电子器件 | [Semiconductor transport · 半导体载流子与器件输运](../src/seedenv/data/guides/semiconductor-transport.md) · `semiconductor-transport` | DEVSIM (pip) |
| Optoelectronic devices · 光电子器件 | [Photovoltaic devices · 光伏与多结光电器件](../src/seedenv/data/guides/photovoltaic-devices.md) · `photovoltaic-devices` | Solcore (pip) |
| Optoelectronic devices · 光电子器件 | [Semiconductor quantum wells · 半导体量子阱与能带](../src/seedenv/data/guides/quantum-wells.md) · `quantum-wells` | Solcore (pip) |
| Optoelectronic devices · 光电子器件 | [Laser rate equations · 激光速率方程](../src/seedenv/data/guides/laser-rate-equations.md) · `laser-rate-equations` | NumPy / SciPy (pip) |
| Optoelectronic devices · 光电子器件 | [Circuit simulation · 电路模拟](../src/seedenv/data/guides/circuits.md) · `circuits` | ngspice · 电路模拟 (connect command / 连接程序) |
| Optoelectronic devices · 光电子器件 | [Source-measure sweeps · 源表与器件电学扫描](../src/seedenv/data/guides/source-measure-sweeps.md) · `source-measure-sweeps` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optoelectronic devices · 光电子器件 | [Temperature experiments · 温控与热学测量](../src/seedenv/data/guides/temperature-control.md) · `temperature-control` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Nonlinear & ultrafast · 非线性与超快光学 | [Nonlinear fiber pulses · 光纤非线性脉冲传播](../src/seedenv/data/guides/fiber-pulses.md) · `fiber-pulses` | laserfun (pip) |
| Nonlinear & ultrafast · 非线性与超快光学 | [Broadband pulse propagation · 宽带与超快脉冲](../src/seedenv/data/guides/broadband-pulses.md) · `broadband-pulses` | py-fmas (pip) |
| Nonlinear & ultrafast · 非线性与超快光学 | [Phase matching · 非线性频率转换与相位匹配](../src/seedenv/data/guides/phase-matching.md) · `phase-matching` | NumPy / SciPy (pip) |
| Fibers & lasers · 光纤与激光 | [Nonlinear fiber pulses · 光纤非线性脉冲传播](../src/seedenv/data/guides/fiber-pulses.md) · `fiber-pulses` | laserfun (pip) |
| Fibers & lasers · 光纤与激光 | [Laser rate equations · 激光速率方程](../src/seedenv/data/guides/laser-rate-equations.md) · `laser-rate-equations` | NumPy / SciPy (pip) |
| Fibers & lasers · 光纤与激光 | [Optical resonators · 谐振腔与干涉仪](../src/seedenv/data/guides/optical-resonators.md) · `optical-resonators` | Finesse 3 (bind interpreter / 连接解释器) |
| Fibers & lasers · 光纤与激光 | [Optical communications · 光纤通信与数字信号处理](../src/seedenv/data/guides/fiber-communications.md) · `fiber-communications` | OptiCommPy (pip) |
| Integrated photonics · 集成光子学 | [Photonic layout · 光子芯片器件与布线](../src/seedenv/data/guides/photonic-layout.md) · `photonic-layout` | gdsfactory (pip) |
| Integrated photonics · 集成光子学 | [Mask geometry · 掩模与 GDS/OASIS 几何](../src/seedenv/data/guides/mask-layout.md) · `mask-layout` | KLayout Python API (pip) |
| Integrated photonics · 集成光子学 | [Photonic circuits · 光子集成电路仿真](../src/seedenv/data/guides/photonic-circuits.md) · `photonic-circuits` | SAX (pip) |
| Integrated photonics · 集成光子学 | [Photonic bands · 光子晶体能带与模态](../src/seedenv/data/guides/photonic-bands.md) · `photonic-bands` | Meep / MPB (conda / bind) |
| Quantum optics · 量子光学 | [Quantum dynamics · 量子动力学](../src/seedenv/data/guides/quantum.md) · `quantum` | QuTiP · 量子动力学 (pip) |
| Quantum optics · 量子光学 | [Quantum trajectories · 量子轨迹与开放系统](../src/seedenv/data/guides/quantum-trajectories.md) · `quantum-trajectories` | QuTiP · 量子动力学 (pip) |
| Quantum optics · 量子光学 | [Photon correlations · 光子关联与量子统计](../src/seedenv/data/guides/photon-correlations.md) · `photon-correlations` | QuTiP · 量子动力学 (pip) |
| Quantum optics · 量子光学 | [Linear quantum photonics · 线性光学量子电路](../src/seedenv/data/guides/linear-quantum-photonics.md) · `linear-quantum-photonics` | Perceval (pip) |
| Quantum optics · 量子光学 | [Continuous-variable photonics · 连续变量量子光学](../src/seedenv/data/guides/continuous-variable-photonics.md) · `continuous-variable-photonics` | Strawberry Fields (bind interpreter / 连接解释器) |
| Quantum optics · 量子光学 | [Photon event data · 单光子事件数据](../src/seedenv/data/guides/photon-event-data.md) · `photon-event-data` | phconvert (pip) |
| Quantum optics · 量子光学 | [Real-time sequences · 实时时序实验](../src/seedenv/data/guides/realtime-sequences.md) · `realtime-sequences` | ARTIQ (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Quantum optics · 量子光学 | [Triggered experiment sequences · 触发与实验序列](../src/seedenv/data/guides/triggered-sequences.md) · `triggered-sequences` | labscript suite (bind interpreter / 连接解释器); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Computational & biological imaging · 计算成像与生物光学 | [Digital holography · 数字全息与相位重建](../src/seedenv/data/guides/digital-holography.md) · `digital-holography` | pyDHM (pip) |
| Computational & biological imaging · 计算成像与生物光学 | [Ptychography · 叠层成像与相位恢复](../src/seedenv/data/guides/ptychography.md) · `ptychography` | PtyPy (bind interpreter / 连接解释器) |
| Computational & biological imaging · 计算成像与生物光学 | [Tissue light transport · 组织中的蒙特卡洛光输运](../src/seedenv/data/guides/tissue-light-transport.md) · `tissue-light-transport` | MCX (bind interpreter / 连接解释器) |
| Computational & biological imaging · 计算成像与生物光学 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 (pip) |
| Optical experiments · 光学实验与测量 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical experiments · 光学实验与测量 | [Camera acquisition · 工业相机采集](../src/seedenv/data/guides/camera-acquisition.md) · `camera-acquisition` | Harvesters (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical experiments · 光学实验与测量 | [Spectrometer acquisition · 光谱仪采集](../src/seedenv/data/guides/spectrometer-acquisition.md) · `spectrometer-acquisition` | python-seabreeze (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical experiments · 光学实验与测量 | [SLM wavefront control · 空间光调制与波前整形](../src/seedenv/data/guides/slm-wavefront-control.md) · `slm-wavefront-control` | slmsuite (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical experiments · 光学实验与测量 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd (pip) |
| Optical experiments · 光学实验与测量 | [Motion control · 位移台与运动控制](../src/seedenv/data/guides/motion-control.md) · `motion-control` | pylablib (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical experiments · 光学实验与测量 | [DAQ streams · 连续数据采集](../src/seedenv/data/guides/daq-streams.md) · `daq-streams` | openDAQ (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical experiments · 光学实验与测量 | [Lock-in measurements · 锁相测量](../src/seedenv/data/guides/lockin-measurements.md) · `lockin-measurements` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical experiments · 光学实验与测量 | [Oscilloscope acquisition · 示波器波形采集](../src/seedenv/data/guides/oscilloscope-acquisition.md) · `oscilloscope-acquisition` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical experiments · 光学实验与测量 | [Measurement calibration · 测量标定与误差传播](../src/seedenv/data/guides/measurement-calibration.md) · `measurement-calibration` | NumPy / SciPy (pip) |
| Optical experiments · 光学实验与测量 | [Adaptive experiments · 自适应实验采集](../src/seedenv/data/guides/adaptive-experiments.md) · `adaptive-experiments` | Bluesky / Ophyd (pip) |
| Optical experiments · 光学实验与测量 | [Microscope acquisition · 显微镜自动采集](../src/seedenv/data/guides/microscope-control.md) · `microscope-control` | Pycro-Manager (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| X-ray & synchrotron · X 射线与同步辐射 | [Synchrotron wavefronts · 同步辐射波前](../src/seedenv/data/guides/synchrotron-wavefronts.md) · `synchrotron-wavefronts` | SRW (pip) |
| X-ray & synchrotron · X 射线与同步辐射 | [X-ray ray tracing · X 射线束线追迹](../src/seedenv/data/guides/xray-raytracing.md) · `xray-raytracing` | SHADOW4 (pip) |

Related resources / 关联资源：

- [Optical material data · 光学材料色散数据](../src/seedenv/data/guides/optical-material-data.md) · `optical-material-data` — RefractiveIndex.INFO (connect service / 连接服务)
- [Optics–Photonics AI Lab · 光学专业环境](../src/seedenv/data/guides/optical-lab.md) · `optical-lab` — Optics-Photonics-AI-Lab (connect plugin / 连接插件)
- [IOP laboratory · 实验平台](../src/seedenv/data/guides/experimental-lab.md) · `experimental-lab` — IOP · 实验平台 (connect plugin / 连接插件)

## Mathematics · 数学

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Analysis & algebra · 分析与代数 | [Symbolic mathematics · 符号数学](../src/seedenv/data/guides/symbolic-mathematics.md) · `symbolic-mathematics` | SymPy (pip) |
| Analysis & algebra · 分析与代数 | [Computer algebra · 计算代数与数论](../src/seedenv/data/guides/sage-mathematics.md) · `sage-mathematics` | SageMath (conda / bind) |
| Analysis & algebra · 分析与代数 | [Arbitrary precision · 任意精度计算](../src/seedenv/data/guides/arbitrary-precision.md) · `arbitrary-precision` | mpmath (pip) |
| Numerical methods · 数值方法 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy (pip) |
| Numerical methods · 数值方法 | [Differential equations · 常微分与边值问题](../src/seedenv/data/guides/differential-equations.md) · `differential-equations` | NumPy / SciPy (pip) |
| Numerical methods · 数值方法 | [Sparse linear algebra · 稀疏线性代数](../src/seedenv/data/guides/sparse-linear-algebra.md) · `sparse-linear-algebra` | NumPy / SciPy (pip) |
| Numerical methods · 数值方法 | [Computational geometry · 计算几何](../src/seedenv/data/guides/computational-geometry.md) · `computational-geometry` | NumPy / SciPy (pip) |
| Discrete structures & optimization · 离散结构与优化 | [Graphs and networks · 图与网络](../src/seedenv/data/guides/networks.md) · `networks` | NetworkX · 图与网络 (pip) |
| Discrete structures & optimization · 离散结构与优化 | [Optimization · 优化与运筹](../src/seedenv/data/guides/optimization.md) · `optimization` | CVXPY / HiGHS · 数学优化 (pip) |
| Discrete structures & optimization · 离散结构与优化 | [Discrete optimization · 离散优化与调度](../src/seedenv/data/guides/discrete-optimization.md) · `discrete-optimization` | OR-Tools (pip) |
| Probability & inference · 概率与推断 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 (pip) |
| Probability & inference · 概率与推断 | [R statistics · R 统计计算](../src/seedenv/data/guides/r-statistics.md) · `r-statistics` | R · 统计计算 (connect command / 连接程序) |
| Probability & inference · 概率与推断 | [Bayesian models · 贝叶斯建模](../src/seedenv/data/guides/bayesian-models.md) · `bayesian-models` | PyMC / ArviZ (pip) |
| Probability & inference · 概率与推断 | [Uncertainty propagation · 不确定度传播](../src/seedenv/data/guides/uncertainty-propagation.md) · `uncertainty-propagation` | uncertainties (pip) |
| Probability & inference · 概率与推断 | [Causal models · 因果建模](../src/seedenv/data/guides/causal-models.md) · `causal-models` | DoWhy (pip) |

## AI & computing · AI 与计算

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Machine learning · 机器学习 | [Machine learning · 机器学习](../src/seedenv/data/guides/machine-learning.md) · `machine-learning` | Scikit-learn · 机器学习 (pip) |
| Machine learning · 机器学习 | [Gradient boosting · 梯度提升与表格学习](../src/seedenv/data/guides/gradient-boosting.md) · `gradient-boosting` | XGBoost (pip) |
| Machine learning · 机器学习 | [Hyperparameter search · 超参数搜索](../src/seedenv/data/guides/hyperparameter-search.md) · `hyperparameter-search` | Optuna (pip) |
| Deep learning · 深度学习 | [Deep learning · 深度学习运行环境](../src/seedenv/data/guides/deep-learning.md) · `deep-learning` | PyTorch (bind interpreter / 连接解释器) |
| Deep learning · 深度学习 | [Differentiable computing · 可微科学计算](../src/seedenv/data/guides/differentiable-computing.md) · `differentiable-computing` | JAX (bind interpreter / 连接解释器) |
| Deep learning · 深度学习 | [Transformer models · Transformer 模型使用](../src/seedenv/data/guides/transformer-models.md) · `transformer-models` | Transformers / PyTorch (bind interpreter / 连接解释器) |
| Deep learning · 深度学习 | [Graph learning · 图机器学习](../src/seedenv/data/guides/graph-learning.md) · `graph-learning` | PyTorch Geometric (bind interpreter / 连接解释器) |
| Data & numerical computing · 数据与数值计算 | [Model datasets · 模型数据集处理](../src/seedenv/data/guides/model-datasets.md) · `model-datasets` | Hugging Face Datasets (pip) |
| Data & numerical computing · 数据与数值计算 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 (pip) |
| Data & numerical computing · 数据与数值计算 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端 (pip); PostgreSQL · 研究数据库连接 (connect service / 连接服务) |
| Data & numerical computing · 数据与数值计算 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy (pip) |
| Data & numerical computing · 数据与数值计算 | [Distributed arrays · 分块与分布式数据计算](../src/seedenv/data/guides/distributed-arrays.md) · `distributed-arrays` | Dask (pip) |
| Data & numerical computing · 数据与数值计算 | [Julia science · Julia 科学计算](../src/seedenv/data/guides/julia-science.md) · `julia-science` | Julia · 科学计算 (connect command / 连接程序) |
| Graphs & retrieval · 图与检索 | [Graphs and networks · 图与网络](../src/seedenv/data/guides/networks.md) · `networks` | NetworkX · 图与网络 (pip) |
| Graphs & retrieval · 图与检索 | [Vector search · 向量近邻检索](../src/seedenv/data/guides/vector-search.md) · `vector-search` | Faiss CPU (conda / bind) |
| Physical AI · 物理交互与具身智能 | [Robot dynamics simulation · 机器人动力学仿真](../src/seedenv/data/guides/robot-dynamics.md) · `robot-dynamics` | MuJoCo (pip) |
| Physical AI · 物理交互与具身智能 | [Robot and sensor frames · 机器人与传感器坐标系](../src/seedenv/data/guides/robot-geometry.md) · `robot-geometry` | pytransform3d (pip) |
| Physical AI · 物理交互与具身智能 | [Robot connections · 机器人与 ROS 2](../src/seedenv/data/guides/robot-connections.md) · `robot-connections` | ROS 2 (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Physical AI · 物理交互与具身智能 | [Adaptive experiments · 自适应实验采集](../src/seedenv/data/guides/adaptive-experiments.md) · `adaptive-experiments` | Bluesky / Ophyd (pip) |
| Physical AI · 物理交互与具身智能 | [Synchronized streams · 多设备数据流同步](../src/seedenv/data/guides/synchronized-streams.md) · `synchronized-streams` | Lab Streaming Layer · 同步数据流 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |

Related resources / 关联资源：

- [Experiment tracking · 实验记录服务连接](../src/seedenv/data/guides/experiment-tracking.md) · `experiment-tracking` — MLflow tracking (connect service / 连接服务)

## Physics · 物理

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Dynamics & fields · 动力学与场 | [Differential equations · 常微分与边值问题](../src/seedenv/data/guides/differential-equations.md) · `differential-equations` | NumPy / SciPy (pip) |
| Dynamics & fields · 动力学与场 | [Finite elements · 有限元基础](../src/seedenv/data/guides/finite-elements.md) · `finite-elements` | scikit-fem / meshio · 有限元 (pip) |
| Dynamics & fields · 动力学与场 | [Variational PDEs · 变分形式偏微分方程](../src/seedenv/data/guides/variational-pdes.md) · `variational-pdes` | FEniCSx (conda / bind) |
| Dynamics & fields · 动力学与场 | [Control systems · 控制系统分析](../src/seedenv/data/guides/control-systems.md) · `control-systems` | python-control (pip) |
| Quantum & many-body systems · 量子与多体系统 | [Quantum dynamics · 量子动力学](../src/seedenv/data/guides/quantum.md) · `quantum` | QuTiP · 量子动力学 (pip) |
| Quantum & many-body systems · 量子与多体系统 | [Quantum trajectories · 量子轨迹与开放系统](../src/seedenv/data/guides/quantum-trajectories.md) · `quantum-trajectories` | QuTiP · 量子动力学 (pip) |
| Quantum & many-body systems · 量子与多体系统 | [Tensor networks · 张量网络](../src/seedenv/data/guides/tensor-networks.md) · `tensor-networks` | quimb (pip) |
| Quantum & many-body systems · 量子与多体系统 | [Molecular electronic structure · 分子电子结构](../src/seedenv/data/guides/electronic-molecules.md) · `electronic-molecules` | PySCF (pip) |
| Quantum & many-body systems · 量子与多体系统 | [Photon correlations · 光子关联与量子统计](../src/seedenv/data/guides/photon-correlations.md) · `photon-correlations` | QuTiP · 量子动力学 (pip) |
| Matter & collective behavior · 物质与集体行为 | [Many-particle dynamics · 多粒子动力学](../src/seedenv/data/guides/many-particle-dynamics.md) · `many-particle-dynamics` | HOOMD-blue (conda / bind) |
| Matter & collective behavior · 物质与集体行为 | [Atomistic dynamics · 原子尺度动力学](../src/seedenv/data/guides/atomistic-dynamics.md) · `atomistic-dynamics` | LAMMPS (connect command / 连接程序) |
| Matter & collective behavior · 物质与集体行为 | [Micromagnetics · 微磁学](../src/seedenv/data/guides/micromagnetics.md) · `micromagnetics` | MuMax3 (connect command / 连接程序) |
| Matter & collective behavior · 物质与集体行为 | [Lattice dynamics · 晶格动力学与声子](../src/seedenv/data/guides/phonons.md) · `phonons` | Phonopy (conda / bind) |
| Plasma & particle physics · 等离子体与粒子物理 | [Plasma models · 等离子体计算](../src/seedenv/data/guides/plasma-models.md) · `plasma-models` | PlasmaPy (pip) |
| Plasma & particle physics · 等离子体与粒子物理 | [Particle event data · 粒子物理事件数据](../src/seedenv/data/guides/particle-event-data.md) · `particle-event-data` | ROOT (conda / bind) |
| Measurement & signals · 测量与信号 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Measurement & signals · 测量与信号 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd (pip) |
| Measurement & signals · 测量与信号 | [Signal processing · 信号处理](../src/seedenv/data/guides/signal-processing.md) · `signal-processing` | NumPy / SciPy (pip) |
| Measurement & signals · 测量与信号 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 (pip) |
| Measurement & signals · 测量与信号 | [Uncertainty propagation · 不确定度传播](../src/seedenv/data/guides/uncertainty-propagation.md) · `uncertainty-propagation` | uncertainties (pip) |
| Measurement & signals · 测量与信号 | [Parameter measurements · 参数测量与实验数据集](../src/seedenv/data/guides/laboratory-measurements.md) · `laboratory-measurements` | QCoDeS (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Measurement & signals · 测量与信号 | [Lock-in measurements · 锁相测量](../src/seedenv/data/guides/lockin-measurements.md) · `lockin-measurements` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Measurement & signals · 测量与信号 | [Temperature experiments · 温控与热学测量](../src/seedenv/data/guides/temperature-control.md) · `temperature-control` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Measurement & signals · 测量与信号 | [DAQ streams · 连续数据采集](../src/seedenv/data/guides/daq-streams.md) · `daq-streams` | openDAQ (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Measurement & signals · 测量与信号 | [Real-time sequences · 实时时序实验](../src/seedenv/data/guides/realtime-sequences.md) · `realtime-sequences` | ARTIQ (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Measurement & signals · 测量与信号 | [Triggered experiment sequences · 触发与实验序列](../src/seedenv/data/guides/triggered-sequences.md) · `triggered-sequences` | labscript suite (bind interpreter / 连接解释器); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Measurement & signals · 测量与信号 | [Photon event data · 单光子事件数据](../src/seedenv/data/guides/photon-event-data.md) · `photon-event-data` | phconvert (pip) |
| Measurement & signals · 测量与信号 | [Adaptive experiments · 自适应实验采集](../src/seedenv/data/guides/adaptive-experiments.md) · `adaptive-experiments` | Bluesky / Ophyd (pip) |
| Measurement & signals · 测量与信号 | [Measurement calibration · 测量标定与误差传播](../src/seedenv/data/guides/measurement-calibration.md) · `measurement-calibration` | NumPy / SciPy (pip) |

Related resources / 关联资源：

- [IOP laboratory · 实验平台](../src/seedenv/data/guides/experimental-lab.md) · `experimental-lab` — IOP · 实验平台 (connect plugin / 连接插件)

## Chemistry · 化学

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Molecular informatics · 分子信息学 | [Molecular data · 分子数据](../src/seedenv/data/guides/molecules.md) · `molecules` | RDKit · 分子数据 (pip) |
| Molecular informatics · 分子信息学 | [Reaction informatics · 反应与分子信息学](../src/seedenv/data/guides/reaction-informatics.md) · `reaction-informatics` | RDKit · 分子数据 (pip) |
| Molecular informatics · 分子信息学 | [Conformer search · 分子构象生成](../src/seedenv/data/guides/conformer-search.md) · `conformer-search` | RDKit · 分子数据 (pip) |
| Electronic structure · 电子结构 | [Molecular electronic structure · 分子电子结构](../src/seedenv/data/guides/electronic-molecules.md) · `electronic-molecules` | PySCF (pip) |
| Electronic structure · 电子结构 | [Atomistic models · 原子结构与原子模拟](../src/seedenv/data/guides/atomistic-models.md) · `atomistic-models` | ASE (pip) |
| Molecular simulation · 分子模拟 | [Molecular dynamics · 分子动力学](../src/seedenv/data/guides/molecular-dynamics.md) · `molecular-dynamics` | OpenMM (pip) |
| Molecular simulation · 分子模拟 | [Trajectory analysis · 分子轨迹分析](../src/seedenv/data/guides/trajectory-analysis.md) · `trajectory-analysis` | MDAnalysis (pip) |
| Molecular simulation · 分子模拟 | [Molecular force-field parameters · 分子力场参数化](../src/seedenv/data/guides/molecular-parameters.md) · `molecular-parameters` | OpenFF Toolkit (conda / bind) |
| Reactions & thermodynamics · 反应与热力学 | [Reaction kinetics · 反应动力学](../src/seedenv/data/guides/reaction-kinetics.md) · `reaction-kinetics` | Cantera (pip) |
| Reactions & thermodynamics · 反应与热力学 | [Fluid thermodynamics · 流体热力学](../src/seedenv/data/guides/fluid-thermodynamics.md) · `fluid-thermodynamics` | thermo (pip) |
| Reactions & thermodynamics · 反应与热力学 | [Aqueous geochemistry · 水溶液地球化学](../src/seedenv/data/guides/aqueous-geochemistry.md) · `aqueous-geochemistry` | PHREEQC (connect command / 连接程序) |
| Spectroscopy & measurements · 光谱与测量 | [Spectral fitting · 光谱与峰形拟合](../src/seedenv/data/guides/molecular-spectra.md) · `molecular-spectra` | lmfit (pip) |
| Spectroscopy & measurements · 光谱与测量 | [Assay curve models · 实验响应曲线建模](../src/seedenv/data/guides/binding-assays.md) · `binding-assays` | lmfit (pip) |
| Spectroscopy & measurements · 光谱与测量 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 (pip) |
| Laboratory automation · 实验自动化 | [Liquid handling · 液体处理与实验板操作](../src/seedenv/data/guides/liquid-handling.md) · `liquid-handling` | PyLabRobot (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Flow experiments · 流量与气路实验](../src/seedenv/data/guides/flow-control.md) · `flow-control` | Alicat flow controller driver (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Temperature experiments · 温控与热学测量](../src/seedenv/data/guides/temperature-control.md) · `temperature-control` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Instrument procedures · 仪器测量程序](../src/seedenv/data/guides/instrument-procedures.md) · `instrument-procedures` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Parameter measurements · 参数测量与实验数据集](../src/seedenv/data/guides/laboratory-measurements.md) · `laboratory-measurements` | QCoDeS (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Adaptive experiments · 自适应实验采集](../src/seedenv/data/guides/adaptive-experiments.md) · `adaptive-experiments` | Bluesky / Ophyd (pip) |

Related resources / 关联资源：

- [Chemical database access · 化学数据库连接](../src/seedenv/data/guides/chemical-data.md) · `chemical-data` — PubChem PUG REST (connect service / 连接服务)

## Materials · 材料

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Structures & composition · 结构与成分 | [Crystal analysis · 晶体结构与材料分析](../src/seedenv/data/guides/crystal-analysis.md) · `crystal-analysis` | pymatgen (pip) |
| Structures & composition · 结构与成分 | [Atomistic models · 原子结构与原子模拟](../src/seedenv/data/guides/atomistic-models.md) · `atomistic-models` | ASE (pip) |
| Structures & composition · 结构与成分 | [Atomic structure interchange · 原子结构格式互转](../src/seedenv/data/guides/materials.md) · `materials` | ASE / pymatgen · 原子与材料 (pip) |
| Structures & composition · 结构与成分 | [Materials features · 材料特征与数据建模](../src/seedenv/data/guides/materials-features.md) · `materials-features` | matminer (pip) |
| Electronic structure · 电子结构 | [Plane-wave electronic structure · 平面波电子结构](../src/seedenv/data/guides/plane-wave-dft.md) · `plane-wave-dft` | Quantum ESPRESSO (connect command / 连接程序) |
| Electronic structure · 电子结构 | [Molecular electronic structure · 分子电子结构](../src/seedenv/data/guides/electronic-molecules.md) · `electronic-molecules` | PySCF (pip) |
| Atomic & lattice dynamics · 原子与晶格动力学 | [Atomistic dynamics · 原子尺度动力学](../src/seedenv/data/guides/atomistic-dynamics.md) · `atomistic-dynamics` | LAMMPS (connect command / 连接程序) |
| Atomic & lattice dynamics · 原子与晶格动力学 | [Many-particle dynamics · 多粒子动力学](../src/seedenv/data/guides/many-particle-dynamics.md) · `many-particle-dynamics` | HOOMD-blue (conda / bind) |
| Atomic & lattice dynamics · 原子与晶格动力学 | [Lattice dynamics · 晶格动力学与声子](../src/seedenv/data/guides/phonons.md) · `phonons` | Phonopy (conda / bind) |
| Atomic & lattice dynamics · 原子与晶格动力学 | [Trajectory analysis · 分子轨迹分析](../src/seedenv/data/guides/trajectory-analysis.md) · `trajectory-analysis` | MDAnalysis (pip) |
| Devices & functional materials · 器件与功能材料 | [Semiconductor transport · 半导体载流子与器件输运](../src/seedenv/data/guides/semiconductor-transport.md) · `semiconductor-transport` | DEVSIM (pip) |
| Devices & functional materials · 器件与功能材料 | [Thin films · 多层薄膜](../src/seedenv/data/guides/thin-films.md) · `thin-films` | tmm (pip) |
| Devices & functional materials · 器件与功能材料 | [Semiconductor quantum wells · 半导体量子阱与能带](../src/seedenv/data/guides/quantum-wells.md) · `quantum-wells` | Solcore (pip) |
| Devices & functional materials · 器件与功能材料 | [Micromagnetics · 微磁学](../src/seedenv/data/guides/micromagnetics.md) · `micromagnetics` | MuMax3 (connect command / 连接程序) |
| Characterization · 表征 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 (pip) |
| Characterization · 表征 | [Spectral fitting · 光谱与峰形拟合](../src/seedenv/data/guides/molecular-spectra.md) · `molecular-spectra` | lmfit (pip) |
| Characterization · 表征 | [Spectrometer acquisition · 光谱仪采集](../src/seedenv/data/guides/spectrometer-acquisition.md) · `spectrometer-acquisition` | python-seabreeze (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Characterization · 表征 | [Source-measure sweeps · 源表与器件电学扫描](../src/seedenv/data/guides/source-measure-sweeps.md) · `source-measure-sweeps` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Characterization · 表征 | [Temperature experiments · 温控与热学测量](../src/seedenv/data/guides/temperature-control.md) · `temperature-control` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Characterization · 表征 | [Lock-in measurements · 锁相测量](../src/seedenv/data/guides/lockin-measurements.md) · `lockin-measurements` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Characterization · 表征 | [Motion control · 位移台与运动控制](../src/seedenv/data/guides/motion-control.md) · `motion-control` | pylablib (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Characterization · 表征 | [Parameter measurements · 参数测量与实验数据集](../src/seedenv/data/guides/laboratory-measurements.md) · `laboratory-measurements` | QCoDeS (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Characterization · 表征 | [Measurement calibration · 测量标定与误差传播](../src/seedenv/data/guides/measurement-calibration.md) · `measurement-calibration` | NumPy / SciPy (pip) |

Related resources / 关联资源：

- [Optical material data · 光学材料色散数据](../src/seedenv/data/guides/optical-material-data.md) · `optical-material-data` — RefractiveIndex.INFO (connect service / 连接服务)

## Life sciences · 生命科学

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Sequences & reads · 序列与读段 | [Biological sequences · 生物序列](../src/seedenv/data/guides/sequences.md) · `sequences` | Biopython · 生物序列 (pip) |
| Sequences & reads · 序列与读段 | [Sequence alignment · 生物序列比对](../src/seedenv/data/guides/sequence-alignment.md) · `sequence-alignment` | Biopython · 生物序列 (pip) |
| Sequences & reads · 序列与读段 | [Read preprocessing · 测序读段预处理](../src/seedenv/data/guides/read-quality.md) · `read-quality` | fastp (connect command / 连接程序) |
| Sequences & reads · 序列与读段 | [Sequence read mapping · 测序读段映射](../src/seedenv/data/guides/read-mapping.md) · `read-mapping` | minimap2 (connect command / 连接程序) |
| Sequences & reads · 序列与读段 | [Genomic alignment files · 基因组比对文件](../src/seedenv/data/guides/genomic-alignments.md) · `genomic-alignments` | pysam (pip) |
| Molecular structures · 分子结构 | [Protein structures · 蛋白质结构数据](../src/seedenv/data/guides/protein-structures.md) · `protein-structures` | Biopython · 生物序列 (pip) |
| Molecular structures · 分子结构 | [Molecular data · 分子数据](../src/seedenv/data/guides/molecules.md) · `molecules` | RDKit · 分子数据 (pip) |
| Molecular structures · 分子结构 | [Conformer search · 分子构象生成](../src/seedenv/data/guides/conformer-search.md) · `conformer-search` | RDKit · 分子数据 (pip) |
| Molecular structures · 分子结构 | [Molecular dynamics · 分子动力学](../src/seedenv/data/guides/molecular-dynamics.md) · `molecular-dynamics` | OpenMM (pip) |
| Molecular structures · 分子结构 | [Trajectory analysis · 分子轨迹分析](../src/seedenv/data/guides/trajectory-analysis.md) · `trajectory-analysis` | MDAnalysis (pip) |
| Cellular & spatial omics · 细胞与空间组学 | [Single-cell analysis · 单细胞分析](../src/seedenv/data/guides/single-cell.md) · `single-cell` | Scanpy (pip) |
| Cellular & spatial omics · 细胞与空间组学 | [Spatial omics · 空间组学](../src/seedenv/data/guides/spatial-omics.md) · `spatial-omics` | Squidpy (pip) |
| Cellular & spatial omics · 细胞与空间组学 | [Proteomics data · 蛋白质组学数据](../src/seedenv/data/guides/proteomics.md) · `proteomics` | Pyteomics (pip) |
| Systems & evolution · 系统与进化 | [Metabolic networks · 代谢网络](../src/seedenv/data/guides/metabolic-networks.md) · `metabolic-networks` | COBRApy (pip) |
| Systems & evolution · 系统与进化 | [Phylogenetic structures · 系统发育结构](../src/seedenv/data/guides/phylogenetics.md) · `phylogenetics` | DendroPy (pip) |
| Systems & evolution · 系统与进化 | [Graphs and networks · 图与网络](../src/seedenv/data/guides/networks.md) · `networks` | NetworkX · 图与网络 (pip) |
| Microscopy · 显微成像 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 (pip) |
| Microscopy · 显微成像 | [Camera acquisition · 工业相机采集](../src/seedenv/data/guides/camera-acquisition.md) · `camera-acquisition` | Harvesters (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Microscopy · 显微成像 | [Tissue light transport · 组织中的蒙特卡洛光输运](../src/seedenv/data/guides/tissue-light-transport.md) · `tissue-light-transport` | MCX (bind interpreter / 连接解释器) |
| Microscopy · 显微成像 | [Volume processing · 三维医学影像处理](../src/seedenv/data/guides/volume-processing.md) · `volume-processing` | SimpleITK (pip) |
| Microscopy · 显微成像 | [Microscope acquisition · 显微镜自动采集](../src/seedenv/data/guides/microscope-control.md) · `microscope-control` | Pycro-Manager (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Microscopy · 显微成像 | [Motion control · 位移台与运动控制](../src/seedenv/data/guides/motion-control.md) · `motion-control` | pylablib (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Microscopy · 显微成像 | [Photon event data · 单光子事件数据](../src/seedenv/data/guides/photon-event-data.md) · `photon-event-data` | phconvert (pip) |
| Biological inference · 生物数据推断 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 (pip) |
| Biological inference · 生物数据推断 | [Bayesian models · 贝叶斯建模](../src/seedenv/data/guides/bayesian-models.md) · `bayesian-models` | PyMC / ArviZ (pip) |
| Biological inference · 生物数据推断 | [R statistics · R 统计计算](../src/seedenv/data/guides/r-statistics.md) · `r-statistics` | R · 统计计算 (connect command / 连接程序) |
| Laboratory automation · 实验自动化 | [Liquid handling · 液体处理与实验板操作](../src/seedenv/data/guides/liquid-handling.md) · `liquid-handling` | PyLabRobot (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Flow experiments · 流量与气路实验](../src/seedenv/data/guides/flow-control.md) · `flow-control` | Alicat flow controller driver (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Instrument procedures · 仪器测量程序](../src/seedenv/data/guides/instrument-procedures.md) · `instrument-procedures` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Synchronized streams · 多设备数据流同步](../src/seedenv/data/guides/synchronized-streams.md) · `synchronized-streams` | Lab Streaming Layer · 同步数据流 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory automation · 实验自动化 | [Adaptive experiments · 自适应实验采集](../src/seedenv/data/guides/adaptive-experiments.md) · `adaptive-experiments` | Bluesky / Ophyd (pip) |

Related resources / 关联资源：

- [Protein structure access · 蛋白质结构数据库连接](../src/seedenv/data/guides/protein-database.md) · `protein-database` — RCSB PDB (connect service / 连接服务)

## Medicine · 医学研究

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Image data · 影像数据 | [DICOM data · DICOM 图像与元数据](../src/seedenv/data/guides/dicom-data.md) · `dicom-data` | pydicom (pip) |
| Image data · 影像数据 | [Neuroimaging arrays · NIfTI 与神经影像数组](../src/seedenv/data/guides/neuroimaging-data.md) · `neuroimaging-data` | NiBabel (pip) |
| Image data · 影像数据 | [Volume processing · 三维医学影像处理](../src/seedenv/data/guides/volume-processing.md) · `volume-processing` | SimpleITK (pip) |
| Image analysis & learning · 影像分析与学习 | [Image registration · 影像配准](../src/seedenv/data/guides/image-registration.md) · `image-registration` | ANTsPy (pip) |
| Image analysis & learning · 影像分析与学习 | [Radiomic features · 影像组学特征](../src/seedenv/data/guides/radiomics.md) · `radiomics` | PyRadiomics (bind interpreter / 连接解释器) |
| Image analysis & learning · 影像分析与学习 | [Medical image learning · 医学影像学习](../src/seedenv/data/guides/medical-learning.md) · `medical-learning` | MONAI / PyTorch (bind interpreter / 连接解释器) |
| Image analysis & learning · 影像分析与学习 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 (pip) |
| Physiological signals · 生理信号 | [Electrophysiology · 电生理信号分析](../src/seedenv/data/guides/electrophysiology.md) · `electrophysiology` | MNE-Python (pip) |
| Physiological signals · 生理信号 | [Signal processing · 信号处理](../src/seedenv/data/guides/signal-processing.md) · `signal-processing` | NumPy / SciPy (pip) |
| Physiological signals · 生理信号 | [Time series and econometrics · 时间序列与计量](../src/seedenv/data/guides/time-series.md) · `time-series` | Statsmodels · 统计与时序 (pip) |
| Physiological signals · 生理信号 | [Synchronized streams · 多设备数据流同步](../src/seedenv/data/guides/synchronized-streams.md) · `synchronized-streams` | Lab Streaming Layer · 同步数据流 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Physiological signals · 生理信号 | [DAQ streams · 连续数据采集](../src/seedenv/data/guides/daq-streams.md) · `daq-streams` | openDAQ (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Physiological signals · 生理信号 | [Measurement calibration · 测量标定与误差传播](../src/seedenv/data/guides/measurement-calibration.md) · `measurement-calibration` | NumPy / SciPy (pip) |
| Population & event data · 人群与事件数据 | [Survival analysis · 生存与事件时间分析](../src/seedenv/data/guides/survival-analysis.md) · `survival-analysis` | lifelines (pip) |
| Population & event data · 人群与事件数据 | [Causal models · 因果建模](../src/seedenv/data/guides/causal-models.md) · `causal-models` | DoWhy (pip) |
| Population & event data · 人群与事件数据 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 (pip) |
| Population & event data · 人群与事件数据 | [R statistics · R 统计计算](../src/seedenv/data/guides/r-statistics.md) · `r-statistics` | R · 统计计算 (connect command / 连接程序) |
| Research data · 研究数据 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 (pip) |
| Research data · 研究数据 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端 (pip); PostgreSQL · 研究数据库连接 (connect service / 连接服务) |
| Research data · 研究数据 | [HDF5 data · HDF5 数据](../src/seedenv/data/guides/hdf5-data.md) · `hdf5-data` | h5py (pip) |

Related resources / 关联资源：

- [Research dataset access · 医学研究数据连接](../src/seedenv/data/guides/clinical-datasets.md) · `clinical-datasets` — PhysioNet (connect service / 连接服务)

## Pharmaceutical research · 医药研究

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Molecules & reactions · 分子与反应 | [Molecular data · 分子数据](../src/seedenv/data/guides/molecules.md) · `molecules` | RDKit · 分子数据 (pip) |
| Molecules & reactions · 分子与反应 | [Reaction informatics · 反应与分子信息学](../src/seedenv/data/guides/reaction-informatics.md) · `reaction-informatics` | RDKit · 分子数据 (pip) |
| Molecules & reactions · 分子与反应 | [Conformer search · 分子构象生成](../src/seedenv/data/guides/conformer-search.md) · `conformer-search` | RDKit · 分子数据 (pip) |
| Structure & interactions · 结构与相互作用 | [Protein structures · 蛋白质结构数据](../src/seedenv/data/guides/protein-structures.md) · `protein-structures` | Biopython · 生物序列 (pip) |
| Structure & interactions · 结构与相互作用 | [Molecular docking · 分子对接](../src/seedenv/data/guides/docking.md) · `docking` | AutoDock Vina (connect command / 连接程序) |
| Structure & interactions · 结构与相互作用 | [Molecular force-field parameters · 分子力场参数化](../src/seedenv/data/guides/molecular-parameters.md) · `molecular-parameters` | OpenFF Toolkit (conda / bind) |
| Molecular simulation · 分子模拟 | [Molecular dynamics · 分子动力学](../src/seedenv/data/guides/molecular-dynamics.md) · `molecular-dynamics` | OpenMM (pip) |
| Molecular simulation · 分子模拟 | [Trajectory analysis · 分子轨迹分析](../src/seedenv/data/guides/trajectory-analysis.md) · `trajectory-analysis` | MDAnalysis (pip) |
| Molecular simulation · 分子模拟 | [Molecular electronic structure · 分子电子结构](../src/seedenv/data/guides/electronic-molecules.md) · `electronic-molecules` | PySCF (pip) |
| Assays & kinetics · 实验响应与动力学 | [Assay curve models · 实验响应曲线建模](../src/seedenv/data/guides/binding-assays.md) · `binding-assays` | lmfit (pip) |
| Assays & kinetics · 实验响应与动力学 | [Compartment dynamics · 房室动力学](../src/seedenv/data/guides/compartment-models.md) · `compartment-models` | NumPy / SciPy (pip) |
| Assays & kinetics · 实验响应与动力学 | [Reaction kinetics · 反应动力学](../src/seedenv/data/guides/reaction-kinetics.md) · `reaction-kinetics` | Cantera (pip) |
| Assays & kinetics · 实验响应与动力学 | [Liquid handling · 液体处理与实验板操作](../src/seedenv/data/guides/liquid-handling.md) · `liquid-handling` | PyLabRobot (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Assays & kinetics · 实验响应与动力学 | [Microscope acquisition · 显微镜自动采集](../src/seedenv/data/guides/microscope-control.md) · `microscope-control` | Pycro-Manager (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Assays & kinetics · 实验响应与动力学 | [Instrument procedures · 仪器测量程序](../src/seedenv/data/guides/instrument-procedures.md) · `instrument-procedures` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Assays & kinetics · 实验响应与动力学 | [Parameter measurements · 参数测量与实验数据集](../src/seedenv/data/guides/laboratory-measurements.md) · `laboratory-measurements` | QCoDeS (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Assays & kinetics · 实验响应与动力学 | [Adaptive experiments · 自适应实验采集](../src/seedenv/data/guides/adaptive-experiments.md) · `adaptive-experiments` | Bluesky / Ophyd (pip) |
| Data & inference · 数据与推断 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 (pip) |
| Data & inference · 数据与推断 | [Bayesian models · 贝叶斯建模](../src/seedenv/data/guides/bayesian-models.md) · `bayesian-models` | PyMC / ArviZ (pip) |
| Data & inference · 数据与推断 | [Survival analysis · 生存与事件时间分析](../src/seedenv/data/guides/survival-analysis.md) · `survival-analysis` | lifelines (pip) |
| Data & inference · 数据与推断 | [Optimization · 优化与运筹](../src/seedenv/data/guides/optimization.md) · `optimization` | CVXPY / HiGHS · 数学优化 (pip) |

Related resources / 关联资源：

- [Chemical database access · 化学数据库连接](../src/seedenv/data/guides/chemical-data.md) · `chemical-data` — PubChem PUG REST (connect service / 连接服务)
- [Protein structure access · 蛋白质结构数据库连接](../src/seedenv/data/guides/protein-database.md) · `protein-database` — RCSB PDB (connect service / 连接服务)

## Mechanical engineering · 机械工程

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Geometry & meshes · 几何与网格 | [Parametric geometry · 参数化几何](../src/seedenv/data/guides/cad.md) · `cad` | CadQuery · 参数化几何 (pip) |
| Geometry & meshes · 几何与网格 | [Mesh generation · 网格生成](../src/seedenv/data/guides/mesh-generation.md) · `mesh-generation` | Gmsh Python (conda / bind) |
| Geometry & meshes · 几何与网格 | [Mesh exchange · 网格与场数据互转](../src/seedenv/data/guides/mesh-exchange.md) · `mesh-exchange` | meshio (pip) |
| Continuum & fluid models · 连续介质与流体 | [Finite elements · 有限元基础](../src/seedenv/data/guides/finite-elements.md) · `finite-elements` | scikit-fem / meshio · 有限元 (pip) |
| Continuum & fluid models · 连续介质与流体 | [Variational PDEs · 变分形式偏微分方程](../src/seedenv/data/guides/variational-pdes.md) · `variational-pdes` | FEniCSx (conda / bind) |
| Continuum & fluid models · 连续介质与流体 | [Computational fluid dynamics · 计算流体动力学](../src/seedenv/data/guides/fluid-dynamics.md) · `fluid-dynamics` | OpenFOAM (connect command / 连接程序) |
| Dynamics & control · 动力学与控制 | [Differential equations · 常微分与边值问题](../src/seedenv/data/guides/differential-equations.md) · `differential-equations` | NumPy / SciPy (pip) |
| Dynamics & control · 动力学与控制 | [Control systems · 控制系统分析](../src/seedenv/data/guides/control-systems.md) · `control-systems` | python-control (pip) |
| Dynamics & control · 动力学与控制 | [Signal processing · 信号处理](../src/seedenv/data/guides/signal-processing.md) · `signal-processing` | NumPy / SciPy (pip) |
| Processes & scheduling · 过程与调度 | [Discrete-event simulation · 离散事件仿真](../src/seedenv/data/guides/discrete-events.md) · `discrete-events` | SimPy (pip) |
| Processes & scheduling · 过程与调度 | [Discrete optimization · 离散优化与调度](../src/seedenv/data/guides/discrete-optimization.md) · `discrete-optimization` | OR-Tools (pip) |
| Processes & scheduling · 过程与调度 | [Optimization · 优化与运筹](../src/seedenv/data/guides/optimization.md) · `optimization` | CVXPY / HiGHS · 数学优化 (pip) |
| Experiments · 实验 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experiments · 实验 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd (pip) |
| Experiments · 实验 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 (pip) |
| Experiments · 实验 | [Serial devices · 串口设备连接](../src/seedenv/data/guides/serial-devices.md) · `serial-devices` | pySerial (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experiments · 实验 | [Motion control · 位移台与运动控制](../src/seedenv/data/guides/motion-control.md) · `motion-control` | pylablib (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experiments · 实验 | [DAQ streams · 连续数据采集](../src/seedenv/data/guides/daq-streams.md) · `daq-streams` | openDAQ (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experiments · 实验 | [CAN devices · CAN 总线设备](../src/seedenv/data/guides/can-devices.md) · `can-devices` | python-can (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experiments · 实验 | [Modbus devices · 工业与实验传感器](../src/seedenv/data/guides/modbus-devices.md) · `modbus-devices` | PyModbus (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experiments · 实验 | [Measurement calibration · 测量标定与误差传播](../src/seedenv/data/guides/measurement-calibration.md) · `measurement-calibration` | NumPy / SciPy (pip) |
| Robotics · 机器人 | [Robot connections · 机器人与 ROS 2](../src/seedenv/data/guides/robot-connections.md) · `robot-connections` | ROS 2 (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Robotics · 机器人 | [Robot and sensor frames · 机器人与传感器坐标系](../src/seedenv/data/guides/robot-geometry.md) · `robot-geometry` | pytransform3d (pip) |
| Robotics · 机器人 | [Robot dynamics simulation · 机器人动力学仿真](../src/seedenv/data/guides/robot-dynamics.md) · `robot-dynamics` | MuJoCo (pip) |
| Robotics · 机器人 | [Embedded measurement boards · 嵌入式测量板](../src/seedenv/data/guides/embedded-boards.md) · `embedded-boards` | MicroPython mpremote (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Robotics · 机器人 | [Synchronized streams · 多设备数据流同步](../src/seedenv/data/guides/synchronized-streams.md) · `synchronized-streams` | Lab Streaming Layer · 同步数据流 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |

## Electronics · 电子

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Circuit simulation · 电路仿真 | [Circuit simulation · 电路模拟](../src/seedenv/data/guides/circuits.md) · `circuits` | ngspice · 电路模拟 (connect command / 连接程序) |
| Circuit simulation · 电路仿真 | [RF networks · 射频网络分析](../src/seedenv/data/guides/rf-networks.md) · `rf-networks` | scikit-rf (pip) |
| Digital design · 数字设计 | [Digital HDL simulation · 数字 HDL 仿真](../src/seedenv/data/guides/digital-hdl.md) · `digital-hdl` | Icarus Verilog (connect command / 连接程序) |
| Digital design · 数字设计 | [PCB project tools · PCB 工程工具](../src/seedenv/data/guides/pcb-design.md) · `pcb-design` | KiCad (connect command / 连接程序) |
| Semiconductor devices · 半导体器件 | [Semiconductor transport · 半导体载流子与器件输运](../src/seedenv/data/guides/semiconductor-transport.md) · `semiconductor-transport` | DEVSIM (pip) |
| Semiconductor devices · 半导体器件 | [Photovoltaic devices · 光伏与多结光电器件](../src/seedenv/data/guides/photovoltaic-devices.md) · `photovoltaic-devices` | Solcore (pip) |
| Semiconductor devices · 半导体器件 | [Semiconductor quantum wells · 半导体量子阱与能带](../src/seedenv/data/guides/quantum-wells.md) · `quantum-wells` | Solcore (pip) |
| Signals & control · 信号与控制 | [Signal processing · 信号处理](../src/seedenv/data/guides/signal-processing.md) · `signal-processing` | NumPy / SciPy (pip) |
| Signals & control · 信号与控制 | [Control systems · 控制系统分析](../src/seedenv/data/guides/control-systems.md) · `control-systems` | python-control (pip) |
| Signals & control · 信号与控制 | [Time series and econometrics · 时间序列与计量](../src/seedenv/data/guides/time-series.md) · `time-series` | Statsmodels · 统计与时序 (pip) |
| Acquisition & interfaces · 采集与接口 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & interfaces · 采集与接口 | [Serial devices · 串口设备连接](../src/seedenv/data/guides/serial-devices.md) · `serial-devices` | pySerial (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & interfaces · 采集与接口 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd (pip) |
| Acquisition & interfaces · 采集与接口 | [Source-measure sweeps · 源表与器件电学扫描](../src/seedenv/data/guides/source-measure-sweeps.md) · `source-measure-sweeps` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & interfaces · 采集与接口 | [Oscilloscope acquisition · 示波器波形采集](../src/seedenv/data/guides/oscilloscope-acquisition.md) · `oscilloscope-acquisition` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & interfaces · 采集与接口 | [Lock-in measurements · 锁相测量](../src/seedenv/data/guides/lockin-measurements.md) · `lockin-measurements` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & interfaces · 采集与接口 | [Logic acquisition · 数字信号与协议采集](../src/seedenv/data/guides/logic-acquisition.md) · `logic-acquisition` | sigrok-cli (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & interfaces · 采集与接口 | [Radio signal acquisition · 射频信号采集](../src/seedenv/data/guides/radio-acquisition.md) · `radio-acquisition` | SoapySDR (bind interpreter / 连接解释器); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & interfaces · 采集与接口 | [DAQ streams · 连续数据采集](../src/seedenv/data/guides/daq-streams.md) · `daq-streams` | openDAQ (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Embedded systems · 嵌入式系统 | [Embedded measurement boards · 嵌入式测量板](../src/seedenv/data/guides/embedded-boards.md) · `embedded-boards` | MicroPython mpremote (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Embedded systems · 嵌入式系统 | [CAN devices · CAN 总线设备](../src/seedenv/data/guides/can-devices.md) · `can-devices` | python-can (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Embedded systems · 嵌入式系统 | [Modbus devices · 工业与实验传感器](../src/seedenv/data/guides/modbus-devices.md) · `modbus-devices` | PyModbus (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Embedded systems · 嵌入式系统 | [Real-time sequences · 实时时序实验](../src/seedenv/data/guides/realtime-sequences.md) · `realtime-sequences` | ARTIQ (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |

## Earth & environment · 地球与环境

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Geospatial data · 地理空间数据 | [Vector geodata · 地理矢量数据](../src/seedenv/data/guides/vector-geodata.md) · `vector-geodata` | geopandas (pip) |
| Geospatial data · 地理空间数据 | [Raster geodata · 遥感栅格数据](../src/seedenv/data/guides/raster-geodata.md) · `raster-geodata` | rasterio (pip) |
| Geospatial data · 地理空间数据 | [Raster remote sensing · 栅格遥感处理](../src/seedenv/data/guides/remote-sensing.md) · `remote-sensing` | rioxarray (pip) |
| Weather & climate · 天气与气候 | [Climate arrays · 气候与多维时空数据](../src/seedenv/data/guides/climate-arrays.md) · `climate-arrays` | xarray (pip) |
| Weather & climate · 天气与气候 | [Meteorological calculations · 气象数据计算](../src/seedenv/data/guides/weather-data.md) · `weather-data` | MetPy (pip) |
| Weather & climate · 天气与气候 | [Climate indicators · 气候指标](../src/seedenv/data/guides/climate-indicators.md) · `climate-indicators` | xclim (pip) |
| Weather & climate · 天气与气候 | [Time series and econometrics · 时间序列与计量](../src/seedenv/data/guides/time-series.md) · `time-series` | Statsmodels · 统计与时序 (pip) |
| Geophysics · 地球物理 | [Seismology · 地震学信号分析](../src/seedenv/data/guides/seismology.md) · `seismology` | ObsPy (pip) |
| Geophysics · 地球物理 | [Geophysical inversion · 地球物理反演](../src/seedenv/data/guides/geophysical-inversion.md) · `geophysical-inversion` | SimPEG (pip) |
| Geochemistry & transport · 地球化学与输运 | [Aqueous geochemistry · 水溶液地球化学](../src/seedenv/data/guides/aqueous-geochemistry.md) · `aqueous-geochemistry` | PHREEQC (connect command / 连接程序) |
| Geochemistry & transport · 地球化学与输运 | [Fluid thermodynamics · 流体热力学](../src/seedenv/data/guides/fluid-thermodynamics.md) · `fluid-thermodynamics` | thermo (pip) |
| Geochemistry & transport · 地球化学与输运 | [Variational PDEs · 变分形式偏微分方程](../src/seedenv/data/guides/variational-pdes.md) · `variational-pdes` | FEniCSx (conda / bind) |
| Spatial models & uncertainty · 空间模型与不确定度 | [Computational geometry · 计算几何](../src/seedenv/data/guides/computational-geometry.md) · `computational-geometry` | NumPy / SciPy (pip) |
| Spatial models & uncertainty · 空间模型与不确定度 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 (pip) |
| Spatial models & uncertainty · 空间模型与不确定度 | [Bayesian models · 贝叶斯建模](../src/seedenv/data/guides/bayesian-models.md) · `bayesian-models` | PyMC / ArviZ (pip) |
| Field instruments · 野外观测设备 | [GNSS field data · GNSS 与野外定位数据](../src/seedenv/data/guides/gnss-streams.md) · `gnss-streams` | pyubx2 (pip) |
| Field instruments · 野外观测设备 | [Modbus devices · 工业与实验传感器](../src/seedenv/data/guides/modbus-devices.md) · `modbus-devices` | PyModbus (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Field instruments · 野外观测设备 | [MQTT streams · MQTT 数据流](../src/seedenv/data/guides/mqtt-streams.md) · `mqtt-streams` | Eclipse Paho MQTT (pip) |
| Field instruments · 野外观测设备 | [Embedded measurement boards · 嵌入式测量板](../src/seedenv/data/guides/embedded-boards.md) · `embedded-boards` | MicroPython mpremote (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Field instruments · 野外观测设备 | [Synchronized streams · 多设备数据流同步](../src/seedenv/data/guides/synchronized-streams.md) · `synchronized-streams` | Lab Streaming Layer · 同步数据流 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Field instruments · 野外观测设备 | [DAQ streams · 连续数据采集](../src/seedenv/data/guides/daq-streams.md) · `daq-streams` | openDAQ (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Field instruments · 野外观测设备 | [Measurement calibration · 测量标定与误差传播](../src/seedenv/data/guides/measurement-calibration.md) · `measurement-calibration` | NumPy / SciPy (pip) |

## Astronomy & space · 天文与空间

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Coordinates & ephemerides · 坐标与星历 | [Astronomy · 天文计算](../src/seedenv/data/guides/astronomy.md) · `astronomy` | Astropy · 天文与物理量 (pip) |
| Coordinates & ephemerides · 坐标与星历 | [Ephemerides and observers · 星历与观测位置](../src/seedenv/data/guides/orbit-ephemerides.md) · `orbit-ephemerides` | Skyfield (pip) |
| Orbital dynamics · 轨道动力学 | [N-body orbits · 引力多体轨道](../src/seedenv/data/guides/n-body-orbits.md) · `n-body-orbits` | REBOUND (pip) |
| Orbital dynamics · 轨道动力学 | [Differential equations · 常微分与边值问题](../src/seedenv/data/guides/differential-equations.md) · `differential-equations` | NumPy / SciPy (pip) |
| Spectra & time series · 光谱与时序 | [Astronomical spectra · 天文光谱分析](../src/seedenv/data/guides/astronomical-spectra.md) · `astronomical-spectra` | specutils (pip) |
| Spectra & time series · 光谱与时序 | [Light curves · 天文光变曲线](../src/seedenv/data/guides/light-curves.md) · `light-curves` | Lightkurve (pip) |
| Spectra & time series · 光谱与时序 | [Time series and econometrics · 时间序列与计量](../src/seedenv/data/guides/time-series.md) · `time-series` | Statsmodels · 统计与时序 (pip) |
| Solar physics · 太阳物理 | [Solar data · 太阳物理数据](../src/seedenv/data/guides/solar-physics.md) · `solar-physics` | SunPy (pip) |
| Solar physics · 太阳物理 | [Plasma models · 等离子体计算](../src/seedenv/data/guides/plasma-models.md) · `plasma-models` | PlasmaPy (pip) |
| Optical instruments · 光学仪器 | [Fourier imaging · 傅里叶成像与点扩散函数](../src/seedenv/data/guides/fourier-imaging.md) · `fourier-imaging` | POPPY (pip) |
| Optical instruments · 光学仪器 | [Adaptive optics · 自适应光学](../src/seedenv/data/guides/adaptive-optics.md) · `adaptive-optics` | HCIPy (pip) |
| Optical instruments · 光学仪器 | [Wavefront analysis · 波前与成像质量](../src/seedenv/data/guides/wavefront-analysis.md) · `wavefront-analysis` | prysm (pip) |
| Optical instruments · 光学仪器 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 (pip) |
| Optical instruments · 光学仪器 | [Camera acquisition · 工业相机采集](../src/seedenv/data/guides/camera-acquisition.md) · `camera-acquisition` | Harvesters (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical instruments · 光学仪器 | [Motion control · 位移台与运动控制](../src/seedenv/data/guides/motion-control.md) · `motion-control` | pylablib (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical instruments · 光学仪器 | [Radio signal acquisition · 射频信号采集](../src/seedenv/data/guides/radio-acquisition.md) · `radio-acquisition` | SoapySDR (bind interpreter / 连接解释器); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical instruments · 光学仪器 | [Synchronized streams · 多设备数据流同步](../src/seedenv/data/guides/synchronized-streams.md) · `synchronized-streams` | Lab Streaming Layer · 同步数据流 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Optical instruments · 光学仪器 | [Measurement calibration · 测量标定与误差传播](../src/seedenv/data/guides/measurement-calibration.md) · `measurement-calibration` | NumPy / SciPy (pip) |

Related resources / 关联资源：

- [Optics–Photonics AI Lab · 光学专业环境](../src/seedenv/data/guides/optical-lab.md) · `optical-lab` — Optics-Photonics-AI-Lab (connect plugin / 连接插件)

## Economics & finance · 经济与金融

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Econometrics · 计量经济 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 (pip) |
| Econometrics · 计量经济 | [Panel econometrics · 面板计量](../src/seedenv/data/guides/panel-econometrics.md) · `panel-econometrics` | linearmodels (pip) |
| Econometrics · 计量经济 | [Causal models · 因果建模](../src/seedenv/data/guides/causal-models.md) · `causal-models` | DoWhy (pip) |
| Econometrics · 计量经济 | [R statistics · R 统计计算](../src/seedenv/data/guides/r-statistics.md) · `r-statistics` | R · 统计计算 (connect command / 连接程序) |
| Time series · 时间序列 | [Time series and econometrics · 时间序列与计量](../src/seedenv/data/guides/time-series.md) · `time-series` | Statsmodels · 统计与时序 (pip) |
| Time series · 时间序列 | [Volatility models · 波动率建模](../src/seedenv/data/guides/volatility-models.md) · `volatility-models` | ARCH (pip) |
| Time series · 时间序列 | [Bayesian models · 贝叶斯建模](../src/seedenv/data/guides/bayesian-models.md) · `bayesian-models` | PyMC / ArviZ (pip) |
| Valuation & allocation · 估值与配置 | [Derivative valuation · 衍生品估值](../src/seedenv/data/guides/derivatives-pricing.md) · `derivatives-pricing` | QuantLib (pip) |
| Valuation & allocation · 估值与配置 | [Portfolio allocation · 投资组合配置研究](../src/seedenv/data/guides/portfolio-allocation.md) · `portfolio-allocation` | PyPortfolioOpt (pip) |
| Valuation & allocation · 估值与配置 | [Optimization · 优化与运筹](../src/seedenv/data/guides/optimization.md) · `optimization` | CVXPY / HiGHS · 数学优化 (pip) |
| Strategy research · 策略研究 | [Strategy backtesting · 策略回测](../src/seedenv/data/guides/backtesting.md) · `backtesting` | Statsmodels · 统计与时序 (pip); Backtesting.py · 策略回测 (pip) |
| Strategy research · 策略研究 | [Exchange market data · 交易所市场数据](../src/seedenv/data/guides/market-data.md) · `market-data` | CCXT (pip) |
| Strategy research · 策略研究 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 (pip) |
| Economic systems · 经济系统 | [Agent-based simulation · 经济主体仿真](../src/seedenv/data/guides/agent-based-economics.md) · `agent-based-economics` | Mesa (pip) |
| Economic systems · 经济系统 | [Graphs and networks · 图与网络](../src/seedenv/data/guides/networks.md) · `networks` | NetworkX · 图与网络 (pip) |
| Economic systems · 经济系统 | [Discrete-event simulation · 离散事件仿真](../src/seedenv/data/guides/discrete-events.md) · `discrete-events` | SimPy (pip) |

Related resources / 关联资源：

- [Economic series access · 经济时间序列连接](../src/seedenv/data/guides/economic-data.md) · `economic-data` — FRED / ALFRED (connect service / 连接服务)

## Experimental science · 实验科学

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Device connections · 设备连接 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Device connections · 设备连接 | [Serial devices · 串口设备连接](../src/seedenv/data/guides/serial-devices.md) · `serial-devices` | pySerial (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Device connections · 设备连接 | [Camera acquisition · 工业相机采集](../src/seedenv/data/guides/camera-acquisition.md) · `camera-acquisition` | Harvesters (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Device connections · 设备连接 | [Spectrometer acquisition · 光谱仪采集](../src/seedenv/data/guides/spectrometer-acquisition.md) · `spectrometer-acquisition` | python-seabreeze (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Device connections · 设备连接 | [Instrument procedures · 仪器测量程序](../src/seedenv/data/guides/instrument-procedures.md) · `instrument-procedures` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Device connections · 设备连接 | [Parameter measurements · 参数测量与实验数据集](../src/seedenv/data/guides/laboratory-measurements.md) · `laboratory-measurements` | QCoDeS (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Device connections · 设备连接 | [Instrument emulation · 仪器通信模拟](../src/seedenv/data/guides/device-emulation.md) · `device-emulation` | PyVISA-sim (pip) |
| Laboratory connections · 实验室系统连接 | [OPC UA connections · OPC UA 连接](../src/seedenv/data/guides/opc-ua.md) · `opc-ua` | asyncua (pip) |
| Laboratory connections · 实验室系统连接 | [MQTT streams · MQTT 数据流](../src/seedenv/data/guides/mqtt-streams.md) · `mqtt-streams` | Eclipse Paho MQTT (pip) |
| Laboratory connections · 实验室系统连接 | [EPICS process variables · EPICS 过程变量](../src/seedenv/data/guides/epics-controls.md) · `epics-controls` | PyEPICS (bind interpreter / 连接解释器); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory connections · 实验室系统连接 | [Modbus devices · 工业与实验传感器](../src/seedenv/data/guides/modbus-devices.md) · `modbus-devices` | PyModbus (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory connections · 实验室系统连接 | [CAN devices · CAN 总线设备](../src/seedenv/data/guides/can-devices.md) · `can-devices` | python-can (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory connections · 实验室系统连接 | [Embedded measurement boards · 嵌入式测量板](../src/seedenv/data/guides/embedded-boards.md) · `embedded-boards` | MicroPython mpremote (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory connections · 实验室系统连接 | [Flow experiments · 流量与气路实验](../src/seedenv/data/guides/flow-control.md) · `flow-control` | Alicat flow controller driver (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Laboratory connections · 实验室系统连接 | [Temperature experiments · 温控与热学测量](../src/seedenv/data/guides/temperature-control.md) · `temperature-control` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & control · 采集与控制 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd (pip) |
| Acquisition & control · 采集与控制 | [Control systems · 控制系统分析](../src/seedenv/data/guides/control-systems.md) · `control-systems` | python-control (pip) |
| Acquisition & control · 采集与控制 | [HDF5 data · HDF5 数据](../src/seedenv/data/guides/hdf5-data.md) · `hdf5-data` | h5py (pip) |
| Acquisition & control · 采集与控制 | [DAQ streams · 连续数据采集](../src/seedenv/data/guides/daq-streams.md) · `daq-streams` | openDAQ (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & control · 采集与控制 | [Microscope acquisition · 显微镜自动采集](../src/seedenv/data/guides/microscope-control.md) · `microscope-control` | Pycro-Manager (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & control · 采集与控制 | [Source-measure sweeps · 源表与器件电学扫描](../src/seedenv/data/guides/source-measure-sweeps.md) · `source-measure-sweeps` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & control · 采集与控制 | [Lock-in measurements · 锁相测量](../src/seedenv/data/guides/lockin-measurements.md) · `lockin-measurements` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & control · 采集与控制 | [Oscilloscope acquisition · 示波器波形采集](../src/seedenv/data/guides/oscilloscope-acquisition.md) · `oscilloscope-acquisition` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & control · 采集与控制 | [Logic acquisition · 数字信号与协议采集](../src/seedenv/data/guides/logic-acquisition.md) · `logic-acquisition` | sigrok-cli (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & control · 采集与控制 | [Radio signal acquisition · 射频信号采集](../src/seedenv/data/guides/radio-acquisition.md) · `radio-acquisition` | SoapySDR (bind interpreter / 连接解释器); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Acquisition & control · 采集与控制 | [GNSS field data · GNSS 与野外定位数据](../src/seedenv/data/guides/gnss-streams.md) · `gnss-streams` | pyubx2 (pip) |
| Measurement processing · 测量处理 | [Signal processing · 信号处理](../src/seedenv/data/guides/signal-processing.md) · `signal-processing` | NumPy / SciPy (pip) |
| Measurement processing · 测量处理 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 (pip) |
| Measurement processing · 测量处理 | [Spectral fitting · 光谱与峰形拟合](../src/seedenv/data/guides/molecular-spectra.md) · `molecular-spectra` | lmfit (pip) |
| Measurement processing · 测量处理 | [Uncertainty propagation · 不确定度传播](../src/seedenv/data/guides/uncertainty-propagation.md) · `uncertainty-propagation` | uncertainties (pip) |
| Measurement processing · 测量处理 | [Physical units · 物理单位计算](../src/seedenv/data/guides/physical-units.md) · `physical-units` | Pint (pip) |
| Measurement processing · 测量处理 | [Measurement calibration · 测量标定与误差传播](../src/seedenv/data/guides/measurement-calibration.md) · `measurement-calibration` | NumPy / SciPy (pip) |
| Measurement processing · 测量处理 | [Photon event data · 单光子事件数据](../src/seedenv/data/guides/photon-event-data.md) · `photon-event-data` | phconvert (pip) |
| Motion and robotics · 运动与机器人 | [Motion control · 位移台与运动控制](../src/seedenv/data/guides/motion-control.md) · `motion-control` | pylablib (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Motion and robotics · 运动与机器人 | [Robot connections · 机器人与 ROS 2](../src/seedenv/data/guides/robot-connections.md) · `robot-connections` | ROS 2 (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Motion and robotics · 运动与机器人 | [Robot and sensor frames · 机器人与传感器坐标系](../src/seedenv/data/guides/robot-geometry.md) · `robot-geometry` | pytransform3d (pip) |
| Motion and robotics · 运动与机器人 | [Robot dynamics simulation · 机器人动力学仿真](../src/seedenv/data/guides/robot-dynamics.md) · `robot-dynamics` | MuJoCo (pip) |
| Timing and synchronization · 时序与同步 | [Synchronized streams · 多设备数据流同步](../src/seedenv/data/guides/synchronized-streams.md) · `synchronized-streams` | Lab Streaming Layer · 同步数据流 (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Timing and synchronization · 时序与同步 | [Real-time sequences · 实时时序实验](../src/seedenv/data/guides/realtime-sequences.md) · `realtime-sequences` | ARTIQ (connect command / 连接程序); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Timing and synchronization · 时序与同步 | [Triggered experiment sequences · 触发与实验序列](../src/seedenv/data/guides/triggered-sequences.md) · `triggered-sequences` | labscript suite (bind interpreter / 连接解释器); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experimental procedures · 实验程序 | [Adaptive experiments · 自适应实验采集](../src/seedenv/data/guides/adaptive-experiments.md) · `adaptive-experiments` | Bluesky / Ophyd (pip) |
| Experimental procedures · 实验程序 | [Liquid handling · 液体处理与实验板操作](../src/seedenv/data/guides/liquid-handling.md) · `liquid-handling` | PyLabRobot (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experimental procedures · 实验程序 | [Instrument procedures · 仪器测量程序](../src/seedenv/data/guides/instrument-procedures.md) · `instrument-procedures` | PyMeasure (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |
| Experimental procedures · 实验程序 | [Parameter measurements · 参数测量与实验数据集](../src/seedenv/data/guides/laboratory-measurements.md) · `laboratory-measurements` | QCoDeS (pip); Laboratory device connections · 实验设备连接 (connect service / 连接服务) |

Related resources / 关联资源：

- [IOP laboratory · 实验平台](../src/seedenv/data/guides/experimental-lab.md) · `experimental-lab` — IOP · 实验平台 (connect plugin / 连接插件)

## Research essentials · 通用研究工具

| Direction / 方向 | Task / 任务 | Software / 软件 |
| --- | --- | --- |
| Computing · 计算 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy (pip) |
| Computing · 计算 | [Symbolic mathematics · 符号数学](../src/seedenv/data/guides/symbolic-mathematics.md) · `symbolic-mathematics` | SymPy (pip) |
| Computing · 计算 | [Julia science · Julia 科学计算](../src/seedenv/data/guides/julia-science.md) · `julia-science` | Julia · 科学计算 (connect command / 连接程序) |
| Computing · 计算 | [Physical units · 物理单位计算](../src/seedenv/data/guides/physical-units.md) · `physical-units` | Pint (pip) |
| Data & storage · 数据与存储 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 (pip) |
| Data & storage · 数据与存储 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端 (pip); PostgreSQL · 研究数据库连接 (connect service / 连接服务) |
| Data & storage · 数据与存储 | [HDF5 data · HDF5 数据](../src/seedenv/data/guides/hdf5-data.md) · `hdf5-data` | h5py (pip) |
| Data & storage · 数据与存储 | [Chunked array storage · Zarr 分块数组](../src/seedenv/data/guides/zarr-data.md) · `zarr-data` | Zarr (pip) |
| Interactive research · 交互式研究 | [Interactive notebooks · 交互式研究笔记本](../src/seedenv/data/guides/notebooks.md) · `notebooks` | JupyterLab (pip) |
| Interactive research · 交互式研究 | [Parameterized notebooks · 参数化笔记本运行](../src/seedenv/data/guides/parameterized-notebooks.md) · `parameterized-notebooks` | Papermill (pip) |
| Writing & figures · 写作与图表 | [Research writing · 研究写作](../src/seedenv/data/guides/writing.md) · `writing` | LaTeX · 论文编译 (connect command / 连接程序) |
| Writing & figures · 写作与图表 | [Literature metadata · 文献元数据](../src/seedenv/data/guides/references.md) · `references` | HTTP APIs · 数据接口 (pip); Crossref · 文献元数据 (connect service / 连接服务) |
| Writing & figures · 写作与图表 | [Scientific plotting · 科学绘图](../src/seedenv/data/guides/scientific-plotting.md) · `scientific-plotting` | Matplotlib (pip) |
| Writing & figures · 写作与图表 | [Research media tools · 研究音视频工具](../src/seedenv/data/guides/media-tools.md) · `media-tools` | FFmpeg (connect command / 连接程序) |

Related resources / 关联资源：

- [Experiment tracking · 实验记录服务连接](../src/seedenv/data/guides/experiment-tracking.md) · `experiment-tracking` — MLflow tracking (connect service / 连接服务)
