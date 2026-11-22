# SeedEnv

[English](README.md)

**按领域找到方向，按研究任务选择模块，准备后跨会话使用。**

SeedEnv 为 Origo 首次设置和日常环境管理提供同一套软件选择、准备与连接能力。
模块可以包含软件、环境、数据连接、插件和简短工作说明。深入的研究方法、知识库
和实验流程继续由光学光子学 AI 实验室、IOP 等专业环境提供。

## 选择研究环境

浏览顺序是 **领域 → 研究方向 → 具体模块**。领域和方向只用于导航，默认不勾选
模块。也可以直接搜索任务或软件，跨领域组合所需内容。

当前有 **14 个研究领域、2 个公共能力入口**，合计 85 个方向与分组、
**171 个不同任务模块、8 个关联资源**。光学与光子学有 13 个研究方向、51 个任务模块；
数据来源与专业实验室作为关联资源单独展示。完整对应关系见 [研究目录](docs/catalogue.md)。
这些是可以选择的研究起点，覆盖范围仍可按实际需要扩展。

| 研究工作 | 可选模块 | 直接准备的软件 |
| --- | --- | --- |
| 多层膜反射透射 | `thin-films` | tmm、NumPy |
| 分子电子结构 | `electronic-molecules` | PySCF |
| 分子动力学 | `molecular-dynamics` | OpenMM |
| 晶格振动 | `phonons` | Phonopy |
| 单细胞分析 | `single-cell` | Scanpy |
| 医学体数据处理 | `volume-processing` | SimpleITK |
| 衍生品定价 | `derivatives-pricing` | QuantLib |
| 控制与系统响应 | `control-systems` | python-control |

同一个模块可以出现在多个方向，实际软件只引用一份。

## 开始使用

需要 Python 3.11 或更新版本。在项目目录执行：

```sh
python -m pip install .
seedenv browse
seedenv browse --field optics
seedenv search --field optics --direction optoelectronic-devices
seedenv --research-space /path/to/user-space plan thin-films writing
seedenv --research-space /path/to/user-space prepare thin-films
seedenv --research-space /path/to/user-space context thin-films
seedenv --research-space /path/to/user-space example thin-films --output thin_film.py
seedenv --research-space /path/to/user-space run python-tmm -- thin_film.py
```

`--research-space` 指向**用户层级的研究空间**。软件与登记信息放在其中的
`system/seedenv`，研究代码、数据和输出留在各自项目中。各会话传入同一个用户
空间即可复用环境，不要传入每次会话的临时目录。也可设置 `SEEDENV_RESEARCH_SPACE`。

已有的 `--home` / `SEEDENV_HOME` 仍直接指定环境目录；没有位置配置的独立命令
继续使用 `~/.seedenv`。已有软件不会被迁移或删除。

## 软件体积与长期使用

浏览只读取小型目录，说明按需加载。允许一个模块都不选，此时不创建软件目录或
后台任务。只有所选模块进入准备计划，计划显示新增软件、可复用
环境和保存位置。下载量与新增磁盘量目前没有逐平台的解析估计，接口用空值表示，
界面明确显示尚无估计，不把未知体积当成零。

同一组件只准备一次。兼容的大环境也可供小模块使用，不受选择先后顺序影响。
不同依赖的软件可以保留独立环境，因此组件去重不代表所有
底层依赖都只占一份空间。大型数据、模型权重、GPU 后端和硬件驱动单独选择或连接。

旧 `python-optics` 环境可供拆分后的薄膜、球形散射模块复用。`optics` 现在是领域，
旧命令应改选 `thin-films`、`sphere-scattering`；原组合仍可通过
`thin-film-and-scattering` 显式访问。

```sh
seedenv discover thin-films --python /existing/environment/bin/python
seedenv bind python-tmm -- /existing/environment/bin/python
seedenv installed
seedenv prepare thin-films --background
seedenv status JOB_ID
seedenv cancel JOB_ID
```

后续命令继续使用相同的位置参数或环境变量。环境不随会话结束删除；失败的新增
安装不替换已有环境。后台准备要求执行机器持续运行。

Python 配方可自动准备；Meep、Phonopy 等 Conda 配方使用机器上已有的
micromamba、mamba 或 conda，在同一用户空间下创建独立环境。已有求解环境可以
登记实际解释器。原生程序、
设备驱动、插件和数据连接保留各自配置步骤。各系统使用同一入口，软件运行位置
遵循上游支持情况，服务器和 WSL 通过产品已有通道接入。

## 产品与 Agent 接入

```sh
seedenv --research-space /path/to/user-space connect origo --output ./seedenv-origo
seedenv connect mcp --modules thin-films molecular-dynamics --output ./seedenv-mcp
seedenv --research-space /path/to/user-space plan thin-films writing --host origo
```

TypeScript 提供客户端和领域、方向、模块选择界面；Rust 提供原生客户端；
Python 负责组合与准备；SQLite 保存安装位置与进度；直接复用上游的 C/C++ 等内核。

导出包包含所选模块的目录、说明和示例，也会包含本地扩展内容。复制 MCP 包到另一台
电脑后，在包内运行 `python configure.py --research-space /path/to/user-space`，
再把生成的 `mcp.json` 接入自己的 Agent。研究软件在接收端实际运行的机器上准备。

Agent 先浏览或搜索，再通过 `context` 取得所选模块的说明与实际调用入口，编写完整研究程序。
示例可以改写，模块不限制上游 API。安装路径不会改变 Agent 的文件访问范围。

这些组件已在本仓库实现。Origo 发布版本的页面接线与用户空间映射仍需产品接入，
见 [接入说明](docs/integration.md)。扩展方法见 [模块说明](docs/modules.md)，
实际运行范围见 [实现说明](docs/implementation.md)。

开发时运行 `python -m unittest discover -s tests -v`；TypeScript 客户端在
`clients/typescript` 下执行 `npm ci`、`npm run build`、`npm test`，Rust 客户端在
仓库根目录执行 `cargo test --manifest-path clients/rust/Cargo.toml`。
`scripts/run_examples.py --home PATH` 运行已准备软件的示例，也可追加模块名限定范围，
该脚本不会安装软件。

SeedEnv 使用 MIT 许可证，上游软件遵循各自许可证。
