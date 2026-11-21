# Research catalogue · 研究目录

Browse a field, then a direction, then select modules. No field installs all its modules.
先浏览领域和研究方向，再选择具体模块。领域没有整包安装动作。

Modules shared across directions keep the same ID and software components.
跨方向的模块沿用同一个 ID 和软件组件；以下出现次数不代表独立安装次数。

Preparation labels describe the route, not an already installed environment.
准备方式描述可用路径，不表示软件已经在用户机器上安装。

## Optics & photonics · 光学与光子学

14 directions · 54 distinct modules / 14 个方向 · 54 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Geometrical optics · 几何光学 | [Paraxial systems · 近轴光路](../src/seedenv/data/guides/paraxial-optics.md) · `paraxial-optics` | RayTracing | Prepare / 安装 |
| Geometrical optics · 几何光学 | [Lens design · 镜头设计与优化](../src/seedenv/data/guides/lens-design.md) · `lens-design` | Optiland | Prepare / 安装 |
| Geometrical optics · 几何光学 | [Lens prescriptions · 镜头处方与成像分析](../src/seedenv/data/guides/lens-prescriptions.md) · `lens-prescriptions` | RayOptics | Prepare / 安装 |
| Geometrical optics · 几何光学 | [Radiometry · 辐射度与非顺序光线](../src/seedenv/data/guides/radiometry.md) · `radiometry` | Raysect | Bind solver / 连接求解环境 |
| Wave optics & imaging · 波动光学与成像 | [Scalar propagation · 标量衍射与光束传播](../src/seedenv/data/guides/scalar-propagation.md) · `scalar-propagation` | LightPipes | Prepare / 安装 |
| Wave optics & imaging · 波动光学与成像 | [Vector diffraction · 矢量衍射与聚焦](../src/seedenv/data/guides/vector-diffraction.md) · `vector-diffraction` | Diffractio | Prepare / 安装 |
| Wave optics & imaging · 波动光学与成像 | [Fourier imaging · 傅里叶成像与点扩散函数](../src/seedenv/data/guides/fourier-imaging.md) · `fourier-imaging` | POPPY | Prepare / 安装 |
| Wave optics & imaging · 波动光学与成像 | [Wavefront analysis · 波前与成像质量](../src/seedenv/data/guides/wavefront-analysis.md) · `wavefront-analysis` | prysm | Prepare / 安装 |
| Wave optics & imaging · 波动光学与成像 | [Adaptive optics · 自适应光学](../src/seedenv/data/guides/adaptive-optics.md) · `adaptive-optics` | HCIPy | Prepare / 安装 |
| Wave optics & imaging · 波动光学与成像 | [Polarization · 偏振与穆勒矩阵](../src/seedenv/data/guides/polarization.md) · `polarization` | py-pol | Prepare / 安装 |
| Statistical optics · 统计光学 | [Mutual coherence · 经典统计光学与相干性](../src/seedenv/data/guides/mutual-coherence.md) · `mutual-coherence` | NumPy / SciPy | Prepare / 安装 |
| Statistical optics · 统计光学 | [Speckle statistics · 散斑与强度统计](../src/seedenv/data/guides/speckle-statistics.md) · `speckle-statistics` | NumPy / SciPy | Prepare / 安装 |
| Statistical optics · 统计光学 | [Photon correlations · 光子关联与量子统计](../src/seedenv/data/guides/photon-correlations.md) · `photon-correlations` | QuTiP · 量子动力学 | Prepare / 安装 |
| Films & scattering · 薄膜与散射 | [Thin films · 多层薄膜](../src/seedenv/data/guides/thin-films.md) · `thin-films` | tmm | Prepare / 安装 |
| Films & scattering · 薄膜与散射 | [Sphere scattering · 球形颗粒散射](../src/seedenv/data/guides/sphere-scattering.md) · `sphere-scattering` | miepython | Prepare / 安装 |
| Films & scattering · 薄膜与散射 | [Multiple scattering · 多体散射与 T 矩阵](../src/seedenv/data/guides/multiple-scattering.md) · `multiple-scattering` | treams | Prepare / 安装 |
| Films & scattering · 薄膜与散射 | [Particles near layers · 层状介质中的颗粒散射](../src/seedenv/data/guides/layered-particle-scattering.md) · `layered-particle-scattering` | SMUTHI | Bind solver / 连接求解环境 |
| Films & scattering · 薄膜与散射 | [Discrete dipoles · 离散偶极散射](../src/seedenv/data/guides/discrete-dipoles.md) · `discrete-dipoles` | ADDA | Native setup / 原生程序 |
| Nanophotonics · 纳米光子学与电磁场 | [FDTD · 全波时域计算](../src/seedenv/data/guides/fdtd.md) · `fdtd` | Meep / MPB | Bind solver / 连接求解环境 |
| Nanophotonics · 纳米光子学与电磁场 | [Photonic bands · 光子晶体能带与模态](../src/seedenv/data/guides/photonic-bands.md) · `photonic-bands` | Meep / MPB | Bind solver / 连接求解环境 |
| Nanophotonics · 纳米光子学与电磁场 | [Periodic RCWA · 周期光栅与超表面](../src/seedenv/data/guides/periodic-rcwa.md) · `periodic-rcwa` | grcwa | Prepare / 安装 |
| Nanophotonics · 纳米光子学与电磁场 | [Photonic slab modes · 光子晶体薄板模态](../src/seedenv/data/guides/slab-bands.md) · `slab-bands` | Legume | Prepare / 安装 |
| Nanophotonics · 纳米光子学与电磁场 | [Inverse electromagnetics · 电磁逆向设计](../src/seedenv/data/guides/inverse-electromagnetics.md) · `inverse-electromagnetics` | Ceviche | Prepare / 安装 |
| Optoelectronic devices · 光电子器件 | [Semiconductor transport · 半导体载流子与器件输运](../src/seedenv/data/guides/semiconductor-transport.md) · `semiconductor-transport` | DEVSIM | Prepare / 安装 |
| Optoelectronic devices · 光电子器件 | [Photovoltaic devices · 光伏与多结光电器件](../src/seedenv/data/guides/photovoltaic-devices.md) · `photovoltaic-devices` | Solcore | Prepare / 安装 |
| Optoelectronic devices · 光电子器件 | [Semiconductor quantum wells · 半导体量子阱与能带](../src/seedenv/data/guides/quantum-wells.md) · `quantum-wells` | Solcore | Prepare / 安装 |
| Optoelectronic devices · 光电子器件 | [Laser rate equations · 激光速率方程](../src/seedenv/data/guides/laser-rate-equations.md) · `laser-rate-equations` | NumPy / SciPy | Prepare / 安装 |
| Optoelectronic devices · 光电子器件 | [Circuit simulation · 电路模拟](../src/seedenv/data/guides/circuits.md) · `circuits` | ngspice · 电路模拟 | Native setup / 原生程序 |
| Nonlinear & ultrafast · 非线性与超快光学 | [Nonlinear fiber pulses · 光纤非线性脉冲传播](../src/seedenv/data/guides/fiber-pulses.md) · `fiber-pulses` | laserfun | Prepare / 安装 |
| Nonlinear & ultrafast · 非线性与超快光学 | [Broadband pulse propagation · 宽带与超快脉冲](../src/seedenv/data/guides/broadband-pulses.md) · `broadband-pulses` | py-fmas | Prepare / 安装 |
| Nonlinear & ultrafast · 非线性与超快光学 | [Phase matching · 非线性频率转换与相位匹配](../src/seedenv/data/guides/phase-matching.md) · `phase-matching` | NumPy / SciPy | Prepare / 安装 |
| Fibers & lasers · 光纤与激光 | [Nonlinear fiber pulses · 光纤非线性脉冲传播](../src/seedenv/data/guides/fiber-pulses.md) · `fiber-pulses` | laserfun | Prepare / 安装 |
| Fibers & lasers · 光纤与激光 | [Laser rate equations · 激光速率方程](../src/seedenv/data/guides/laser-rate-equations.md) · `laser-rate-equations` | NumPy / SciPy | Prepare / 安装 |
| Fibers & lasers · 光纤与激光 | [Optical resonators · 谐振腔与干涉仪](../src/seedenv/data/guides/optical-resonators.md) · `optical-resonators` | Finesse 3 | Bind solver / 连接求解环境 |
| Fibers & lasers · 光纤与激光 | [Optical communications · 光纤通信与数字信号处理](../src/seedenv/data/guides/fiber-communications.md) · `fiber-communications` | OptiCommPy | Prepare / 安装 |
| Integrated photonics · 集成光子学 | [Photonic layout · 光子芯片器件与布线](../src/seedenv/data/guides/photonic-layout.md) · `photonic-layout` | gdsfactory | Prepare / 安装 |
| Integrated photonics · 集成光子学 | [Mask geometry · 掩模与 GDS/OASIS 几何](../src/seedenv/data/guides/mask-layout.md) · `mask-layout` | KLayout Python API | Prepare / 安装 |
| Integrated photonics · 集成光子学 | [Photonic circuits · 光子集成电路仿真](../src/seedenv/data/guides/photonic-circuits.md) · `photonic-circuits` | SAX | Prepare / 安装 |
| Integrated photonics · 集成光子学 | [Photonic bands · 光子晶体能带与模态](../src/seedenv/data/guides/photonic-bands.md) · `photonic-bands` | Meep / MPB | Bind solver / 连接求解环境 |
| Quantum optics · 量子光学 | [Quantum dynamics · 量子动力学](../src/seedenv/data/guides/quantum.md) · `quantum` | QuTiP · 量子动力学 | Prepare / 安装 |
| Quantum optics · 量子光学 | [Quantum trajectories · 量子轨迹与开放系统](../src/seedenv/data/guides/quantum-trajectories.md) · `quantum-trajectories` | QuTiP · 量子动力学 | Prepare / 安装 |
| Quantum optics · 量子光学 | [Photon correlations · 光子关联与量子统计](../src/seedenv/data/guides/photon-correlations.md) · `photon-correlations` | QuTiP · 量子动力学 | Prepare / 安装 |
| Quantum optics · 量子光学 | [Linear quantum photonics · 线性光学量子电路](../src/seedenv/data/guides/linear-quantum-photonics.md) · `linear-quantum-photonics` | Perceval | Prepare / 安装 |
| Quantum optics · 量子光学 | [Continuous-variable photonics · 连续变量量子光学](../src/seedenv/data/guides/continuous-variable-photonics.md) · `continuous-variable-photonics` | Strawberry Fields | Bind solver / 连接求解环境 |
| Computational & biological imaging · 计算成像与生物光学 | [Digital holography · 数字全息与相位重建](../src/seedenv/data/guides/digital-holography.md) · `digital-holography` | pyDHM | Prepare / 安装 |
| Computational & biological imaging · 计算成像与生物光学 | [Ptychography · 叠层成像与相位恢复](../src/seedenv/data/guides/ptychography.md) · `ptychography` | PtyPy | Bind solver / 连接求解环境 |
| Computational & biological imaging · 计算成像与生物光学 | [Tissue light transport · 组织中的蒙特卡洛光输运](../src/seedenv/data/guides/tissue-light-transport.md) · `tissue-light-transport` | MCX | Bind solver / 连接求解环境 |
| Computational & biological imaging · 计算成像与生物光学 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 | Prepare / 安装 |
| Optical experiments · 光学实验与测量 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 | Prepare / 安装 |
| Optical experiments · 光学实验与测量 | [Camera acquisition · 工业相机采集](../src/seedenv/data/guides/camera-acquisition.md) · `camera-acquisition` | Harvesters | Prepare / 安装 |
| Optical experiments · 光学实验与测量 | [Spectrometer acquisition · 光谱仪采集](../src/seedenv/data/guides/spectrometer-acquisition.md) · `spectrometer-acquisition` | python-seabreeze | Prepare / 安装 |
| Optical experiments · 光学实验与测量 | [SLM wavefront control · 空间光调制与波前整形](../src/seedenv/data/guides/slm-wavefront-control.md) · `slm-wavefront-control` | slmsuite | Prepare / 安装 |
| Optical experiments · 光学实验与测量 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd | Prepare / 安装 |
| X-ray & synchrotron · X 射线与同步辐射 | [Synchrotron wavefronts · 同步辐射波前](../src/seedenv/data/guides/synchrotron-wavefronts.md) · `synchrotron-wavefronts` | SRW | Prepare / 安装 |
| X-ray & synchrotron · X 射线与同步辐射 | [X-ray ray tracing · X 射线束线追迹](../src/seedenv/data/guides/xray-raytracing.md) · `xray-raytracing` | SHADOW4 | Prepare / 安装 |
| Data & specialist tools · 数据与专业环境 | [Optical material data · 光学材料色散数据](../src/seedenv/data/guides/optical-material-data.md) · `optical-material-data` | RefractiveIndex.INFO | Connect data / 连接数据 |
| Data & specialist tools · 数据与专业环境 | [Optics–Photonics AI Lab · 光学专业环境](../src/seedenv/data/guides/optical-lab.md) · `optical-lab` | Optics-Photonics-AI-Lab | Host plugin / 接入插件 |
| Data & specialist tools · 数据与专业环境 | [IOP laboratory · 实验平台](../src/seedenv/data/guides/experimental-lab.md) · `experimental-lab` | IOP · 实验平台 | Host plugin / 接入插件 |

## Mathematics · 数学

3 directions · 6 distinct modules / 3 个方向 · 6 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Analysis & algebra · 分析与代数 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy | Prepare / 安装 |
| Analysis & algebra · 分析与代数 | [Symbolic mathematics · 符号数学](../src/seedenv/data/guides/symbolic-mathematics.md) · `symbolic-mathematics` | SymPy | Prepare / 安装 |
| Discrete structures · 离散结构 | [Graphs and networks · 图与网络](../src/seedenv/data/guides/networks.md) · `networks` | NetworkX · 图与网络 | Prepare / 安装 |
| Discrete structures · 离散结构 | [Optimization · 优化与运筹](../src/seedenv/data/guides/optimization.md) · `optimization` | CVXPY / HiGHS · 数学优化 | Prepare / 安装 |
| Probability & statistics · 概率与统计 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Probability & statistics · 概率与统计 | [R statistics · R 统计计算](../src/seedenv/data/guides/r-statistics.md) · `r-statistics` | R · 统计计算 | Native setup / 原生程序 |

## AI & computing · AI 与计算

3 directions · 8 distinct modules / 3 个方向 · 8 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Machine learning · 机器学习 | [Machine learning · 机器学习](../src/seedenv/data/guides/machine-learning.md) · `machine-learning` | Scikit-learn · 机器学习 | Prepare / 安装 |
| Machine learning · 机器学习 | [Deep learning · 深度学习运行环境](../src/seedenv/data/guides/deep-learning.md) · `deep-learning` | PyTorch | Bind solver / 连接求解环境 |
| Scientific computing · 科学计算 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy | Prepare / 安装 |
| Scientific computing · 科学计算 | [Differentiable computing · 可微科学计算](../src/seedenv/data/guides/differentiable-computing.md) · `differentiable-computing` | JAX | Bind solver / 连接求解环境 |
| Scientific computing · 科学计算 | [Julia science · Julia 科学计算](../src/seedenv/data/guides/julia-science.md) · `julia-science` | Julia · 科学计算 | Native setup / 原生程序 |
| Data systems · 数据系统 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 | Prepare / 安装 |
| Data systems · 数据系统 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端, PostgreSQL · 研究数据库连接 | Prepare / 安装; Connect data / 连接数据 |
| Data systems · 数据系统 | [Graphs and networks · 图与网络](../src/seedenv/data/guides/networks.md) · `networks` | NetworkX · 图与网络 | Prepare / 安装 |

## Physics · 物理

3 directions · 8 distinct modules / 3 个方向 · 8 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Dynamics & fields · 动力学与场 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy | Prepare / 安装 |
| Dynamics & fields · 动力学与场 | [Finite elements · 有限元基础](../src/seedenv/data/guides/finite-elements.md) · `finite-elements` | scikit-fem / meshio · 有限元 | Prepare / 安装 |
| Quantum systems · 量子系统 | [Quantum dynamics · 量子动力学](../src/seedenv/data/guides/quantum.md) · `quantum` | QuTiP · 量子动力学 | Prepare / 安装 |
| Quantum systems · 量子系统 | [Quantum trajectories · 量子轨迹与开放系统](../src/seedenv/data/guides/quantum-trajectories.md) · `quantum-trajectories` | QuTiP · 量子动力学 | Prepare / 安装 |
| Quantum systems · 量子系统 | [Photon correlations · 光子关联与量子统计](../src/seedenv/data/guides/photon-correlations.md) · `photon-correlations` | QuTiP · 量子动力学 | Prepare / 安装 |
| Measurement · 测量 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 | Prepare / 安装 |
| Measurement · 测量 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd | Prepare / 安装 |
| Measurement · 测量 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |

## Chemistry · 化学

3 directions · 7 distinct modules / 3 个方向 · 7 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Molecular informatics · 分子信息学 | [Molecular data · 分子数据](../src/seedenv/data/guides/molecules.md) · `molecules` | RDKit · 分子数据 | Prepare / 安装 |
| Molecular informatics · 分子信息学 | [Reaction informatics · 反应与分子信息学](../src/seedenv/data/guides/reaction-informatics.md) · `reaction-informatics` | RDKit · 分子数据 | Prepare / 安装 |
| Atomistic models · 原子建模 | [Atomistic models · 原子结构与原子模拟](../src/seedenv/data/guides/atomistic-models.md) · `atomistic-models` | ASE | Prepare / 安装 |
| Atomistic models · 原子建模 | [Atomic structure interchange · 原子结构格式互转](../src/seedenv/data/guides/materials.md) · `materials` | ASE / pymatgen · 原子与材料 | Prepare / 安装 |
| Chemical data · 化学数据 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 | Prepare / 安装 |
| Chemical data · 化学数据 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Chemical data · 化学数据 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端, PostgreSQL · 研究数据库连接 | Prepare / 安装; Connect data / 连接数据 |

## Materials · 材料

3 directions · 9 distinct modules / 3 个方向 · 9 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Structures · 结构 | [Crystal analysis · 晶体结构与材料分析](../src/seedenv/data/guides/crystal-analysis.md) · `crystal-analysis` | pymatgen | Prepare / 安装 |
| Structures · 结构 | [Atomistic models · 原子结构与原子模拟](../src/seedenv/data/guides/atomistic-models.md) · `atomistic-models` | ASE | Prepare / 安装 |
| Structures · 结构 | [Atomic structure interchange · 原子结构格式互转](../src/seedenv/data/guides/materials.md) · `materials` | ASE / pymatgen · 原子与材料 | Prepare / 安装 |
| Properties & devices · 性质与器件 | [Semiconductor transport · 半导体载流子与器件输运](../src/seedenv/data/guides/semiconductor-transport.md) · `semiconductor-transport` | DEVSIM | Prepare / 安装 |
| Properties & devices · 性质与器件 | [Thin films · 多层薄膜](../src/seedenv/data/guides/thin-films.md) · `thin-films` | tmm | Prepare / 安装 |
| Properties & devices · 性质与器件 | [Semiconductor quantum wells · 半导体量子阱与能带](../src/seedenv/data/guides/quantum-wells.md) · `quantum-wells` | Solcore | Prepare / 安装 |
| Characterization · 表征 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 | Prepare / 安装 |
| Characterization · 表征 | [Spectrometer acquisition · 光谱仪采集](../src/seedenv/data/guides/spectrometer-acquisition.md) · `spectrometer-acquisition` | python-seabreeze | Prepare / 安装 |
| Characterization · 表征 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |

## Life sciences · 生命科学

4 directions · 10 distinct modules / 4 个方向 · 10 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Sequences · 序列 | [Biological sequences · 生物序列](../src/seedenv/data/guides/sequences.md) · `sequences` | Biopython · 生物序列 | Prepare / 安装 |
| Sequences · 序列 | [Sequence alignment · 生物序列比对](../src/seedenv/data/guides/sequence-alignment.md) · `sequence-alignment` | Biopython · 生物序列 | Prepare / 安装 |
| Structural data · 结构数据 | [Protein structures · 蛋白质结构数据](../src/seedenv/data/guides/protein-structures.md) · `protein-structures` | Biopython · 生物序列 | Prepare / 安装 |
| Structural data · 结构数据 | [Molecular data · 分子数据](../src/seedenv/data/guides/molecules.md) · `molecules` | RDKit · 分子数据 | Prepare / 安装 |
| Microscopy · 显微成像 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 | Prepare / 安装 |
| Microscopy · 显微成像 | [Camera acquisition · 工业相机采集](../src/seedenv/data/guides/camera-acquisition.md) · `camera-acquisition` | Harvesters | Prepare / 安装 |
| Microscopy · 显微成像 | [Tissue light transport · 组织中的蒙特卡洛光输运](../src/seedenv/data/guides/tissue-light-transport.md) · `tissue-light-transport` | MCX | Bind solver / 连接求解环境 |
| Data & statistics · 数据与统计 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Data & statistics · 数据与统计 | [R statistics · R 统计计算](../src/seedenv/data/guides/r-statistics.md) · `r-statistics` | R · 统计计算 | Native setup / 原生程序 |
| Data & statistics · 数据与统计 | [Graphs and networks · 图与网络](../src/seedenv/data/guides/networks.md) · `networks` | NetworkX · 图与网络 | Prepare / 安装 |

## Medicine · 医学研究

2 directions · 7 distinct modules / 2 个方向 · 7 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Image data · 影像数据 | [DICOM data · DICOM 图像与元数据](../src/seedenv/data/guides/dicom-data.md) · `dicom-data` | pydicom | Prepare / 安装 |
| Image data · 影像数据 | [Neuroimaging arrays · NIfTI 与神经影像数组](../src/seedenv/data/guides/neuroimaging-data.md) · `neuroimaging-data` | NiBabel | Prepare / 安装 |
| Image data · 影像数据 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 | Prepare / 安装 |
| Research data · 研究数据 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Research data · 研究数据 | [R statistics · R 统计计算](../src/seedenv/data/guides/r-statistics.md) · `r-statistics` | R · 统计计算 | Native setup / 原生程序 |
| Research data · 研究数据 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 | Prepare / 安装 |
| Research data · 研究数据 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端, PostgreSQL · 研究数据库连接 | Prepare / 安装; Connect data / 连接数据 |

## Pharmaceutical research · 医药研究

3 directions · 7 distinct modules / 3 个方向 · 7 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Molecules & reactions · 分子与反应 | [Molecular data · 分子数据](../src/seedenv/data/guides/molecules.md) · `molecules` | RDKit · 分子数据 | Prepare / 安装 |
| Molecules & reactions · 分子与反应 | [Reaction informatics · 反应与分子信息学](../src/seedenv/data/guides/reaction-informatics.md) · `reaction-informatics` | RDKit · 分子数据 | Prepare / 安装 |
| Biological structures · 生物结构 | [Protein structures · 蛋白质结构数据](../src/seedenv/data/guides/protein-structures.md) · `protein-structures` | Biopython · 生物序列 | Prepare / 安装 |
| Biological structures · 生物结构 | [Sequence alignment · 生物序列比对](../src/seedenv/data/guides/sequence-alignment.md) · `sequence-alignment` | Biopython · 生物序列 | Prepare / 安装 |
| Experimental data · 实验数据 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Experimental data · 实验数据 | [Optimization · 优化与运筹](../src/seedenv/data/guides/optimization.md) · `optimization` | CVXPY / HiGHS · 数学优化 | Prepare / 安装 |
| Experimental data · 实验数据 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端, PostgreSQL · 研究数据库连接 | Prepare / 安装; Connect data / 连接数据 |

## Mechanical engineering · 机械工程

3 directions · 6 distinct modules / 3 个方向 · 6 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Geometry & manufacturing · 几何与制造 | [Parametric geometry · 参数化几何](../src/seedenv/data/guides/cad.md) · `cad` | CadQuery · 参数化几何 | Prepare / 安装 |
| Continuum models · 连续介质建模 | [Finite elements · 有限元基础](../src/seedenv/data/guides/finite-elements.md) · `finite-elements` | scikit-fem / meshio · 有限元 | Prepare / 安装 |
| Continuum models · 连续介质建模 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy | Prepare / 安装 |
| Experiments · 实验 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 | Prepare / 安装 |
| Experiments · 实验 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd | Prepare / 安装 |
| Experiments · 实验 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 | Prepare / 安装 |

## Electronics · 电子

3 directions · 7 distinct modules / 3 个方向 · 7 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Circuits · 电路 | [Circuit simulation · 电路模拟](../src/seedenv/data/guides/circuits.md) · `circuits` | ngspice · 电路模拟 | Native setup / 原生程序 |
| Semiconductor devices · 半导体器件 | [Semiconductor transport · 半导体载流子与器件输运](../src/seedenv/data/guides/semiconductor-transport.md) · `semiconductor-transport` | DEVSIM | Prepare / 安装 |
| Semiconductor devices · 半导体器件 | [Photovoltaic devices · 光伏与多结光电器件](../src/seedenv/data/guides/photovoltaic-devices.md) · `photovoltaic-devices` | Solcore | Prepare / 安装 |
| Semiconductor devices · 半导体器件 | [Semiconductor quantum wells · 半导体量子阱与能带](../src/seedenv/data/guides/quantum-wells.md) · `quantum-wells` | Solcore | Prepare / 安装 |
| Signals & acquisition · 信号与采集 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy | Prepare / 安装 |
| Signals & acquisition · 信号与采集 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 | Prepare / 安装 |
| Signals & acquisition · 信号与采集 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd | Prepare / 安装 |

## Earth & environment · 地球与环境

3 directions · 7 distinct modules / 3 个方向 · 7 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Geospatial data · 地理数据 | [Vector geodata · 地理矢量数据](../src/seedenv/data/guides/vector-geodata.md) · `vector-geodata` | geopandas | Prepare / 安装 |
| Geospatial data · 地理数据 | [Raster geodata · 遥感栅格数据](../src/seedenv/data/guides/raster-geodata.md) · `raster-geodata` | rasterio | Prepare / 安装 |
| Climate & time series · 气候与时序 | [Climate arrays · 气候与多维时空数据](../src/seedenv/data/guides/climate-arrays.md) · `climate-arrays` | xarray | Prepare / 安装 |
| Climate & time series · 气候与时序 | [Time series and econometrics · 时间序列与计量](../src/seedenv/data/guides/time-series.md) · `time-series` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Spatial analysis · 空间分析 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 | Prepare / 安装 |
| Spatial analysis · 空间分析 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Spatial analysis · 空间分析 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端, PostgreSQL · 研究数据库连接 | Prepare / 安装; Connect data / 连接数据 |

## Astronomy & space · 天文与空间

3 directions · 7 distinct modules / 3 个方向 · 7 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Coordinates & data · 坐标与数据 | [Astronomy · 天文计算](../src/seedenv/data/guides/astronomy.md) · `astronomy` | Astropy · 天文与物理量 | Prepare / 安装 |
| Optical instruments · 光学仪器 | [Fourier imaging · 傅里叶成像与点扩散函数](../src/seedenv/data/guides/fourier-imaging.md) · `fourier-imaging` | POPPY | Prepare / 安装 |
| Optical instruments · 光学仪器 | [Adaptive optics · 自适应光学](../src/seedenv/data/guides/adaptive-optics.md) · `adaptive-optics` | HCIPy | Prepare / 安装 |
| Optical instruments · 光学仪器 | [Wavefront analysis · 波前与成像质量](../src/seedenv/data/guides/wavefront-analysis.md) · `wavefront-analysis` | prysm | Prepare / 安装 |
| Signals & images · 信号与图像 | [Time series and econometrics · 时间序列与计量](../src/seedenv/data/guides/time-series.md) · `time-series` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Signals & images · 信号与图像 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 | Prepare / 安装 |
| Signals & images · 信号与图像 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |

## Economics & finance · 经济与金融

3 directions · 8 distinct modules / 3 个方向 · 8 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Econometrics · 计量经济 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Econometrics · 计量经济 | [Time series and econometrics · 时间序列与计量](../src/seedenv/data/guides/time-series.md) · `time-series` | Statsmodels · 统计与时序 | Prepare / 安装 |
| Econometrics · 计量经济 | [R statistics · R 统计计算](../src/seedenv/data/guides/r-statistics.md) · `r-statistics` | R · 统计计算 | Native setup / 原生程序 |
| Strategy research · 交易策略研究 | [Strategy backtesting · 策略回测](../src/seedenv/data/guides/backtesting.md) · `backtesting` | Backtesting.py · 策略回测 | Prepare / 安装 |
| Strategy research · 交易策略研究 | [Optimization · 优化与运筹](../src/seedenv/data/guides/optimization.md) · `optimization` | CVXPY / HiGHS · 数学优化 | Prepare / 安装 |
| Market & economic data · 市场与经济数据 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 | Prepare / 安装 |
| Market & economic data · 市场与经济数据 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端, PostgreSQL · 研究数据库连接 | Prepare / 安装; Connect data / 连接数据 |
| Market & economic data · 市场与经济数据 | [Graphs and networks · 图与网络](../src/seedenv/data/guides/networks.md) · `networks` | NetworkX · 图与网络 | Prepare / 安装 |

## Experimental science · 实验科学

3 directions · 8 distinct modules / 3 个方向 · 8 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Device connections · 设备连接 | [Instrument connections · 仪器连接](../src/seedenv/data/guides/instruments.md) · `instruments` | PyVISA · 仪器连接 | Prepare / 安装 |
| Device connections · 设备连接 | [Camera acquisition · 工业相机采集](../src/seedenv/data/guides/camera-acquisition.md) · `camera-acquisition` | Harvesters | Prepare / 安装 |
| Device connections · 设备连接 | [Spectrometer acquisition · 光谱仪采集](../src/seedenv/data/guides/spectrometer-acquisition.md) · `spectrometer-acquisition` | python-seabreeze | Prepare / 安装 |
| Acquisition & workflows · 采集与流程 | [Experiment scans · 实验扫描与数据流](../src/seedenv/data/guides/experiment-scans.md) · `experiment-scans` | Bluesky / Ophyd | Prepare / 安装 |
| Acquisition & workflows · 采集与流程 | [IOP laboratory · 实验平台](../src/seedenv/data/guides/experimental-lab.md) · `experimental-lab` | IOP · 实验平台 | Host plugin / 接入插件 |
| Measurement processing · 测量处理 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy | Prepare / 安装 |
| Measurement processing · 测量处理 | [Image processing · 图像处理](../src/seedenv/data/guides/images.md) · `images` | scikit-image / Pillow · 图像处理 | Prepare / 安装 |
| Measurement processing · 测量处理 | [Statistical models · 统计建模与推断](../src/seedenv/data/guides/statistical-models.md) · `statistical-models` | Statsmodels · 统计与时序 | Prepare / 安装 |

## Research essentials · 通用研究工具

3 directions · 9 distinct modules / 3 个方向 · 9 个不同模块

| Direction / 方向 | Module / 模块 | Software / 软件 | Preparation / 准备 |
| --- | --- | --- | --- |
| Computing · 计算 | [Scientific computing · 科学计算](../src/seedenv/data/guides/science.md) · `science` | Scientific Python · 科学计算 | Prepare / 安装 |
| Computing · 计算 | [Numerical computing · 数值计算](../src/seedenv/data/guides/numerical-computing.md) · `numerical-computing` | NumPy / SciPy | Prepare / 安装 |
| Computing · 计算 | [Symbolic mathematics · 符号数学](../src/seedenv/data/guides/symbolic-mathematics.md) · `symbolic-mathematics` | SymPy | Prepare / 安装 |
| Computing · 计算 | [Julia science · Julia 科学计算](../src/seedenv/data/guides/julia-science.md) · `julia-science` | Julia · 科学计算 | Native setup / 原生程序 |
| Data · 数据 | [Tables and local data · 表格与本地数据](../src/seedenv/data/guides/tables.md) · `tables` | Polars / DuckDB / Arrow · 表格与数据 | Prepare / 安装 |
| Data · 数据 | [Research databases · 研究数据库](../src/seedenv/data/guides/databases.md) · `databases` | SQLAlchemy / psycopg · 数据库客户端, PostgreSQL · 研究数据库连接 | Prepare / 安装; Connect data / 连接数据 |
| Writing & figures · 写作与图表 | [Research writing · 研究写作](../src/seedenv/data/guides/writing.md) · `writing` | LaTeX · 论文编译 | Native setup / 原生程序 |
| Writing & figures · 写作与图表 | [Literature metadata · 文献元数据](../src/seedenv/data/guides/references.md) · `references` | HTTP APIs · 数据接口, Crossref · 文献元数据 | Prepare / 安装; Connect data / 连接数据 |
| Writing & figures · 写作与图表 | [Scientific plotting · 科学绘图](../src/seedenv/data/guides/scientific-plotting.md) · `scientific-plotting` | Matplotlib | Prepare / 安装 |
