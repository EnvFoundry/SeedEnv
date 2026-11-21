# SeedEnv

[English](README.md)

**按研究需要准备工具，安装后跨会话复用。**

用户在 Origo 首次设置或日后的“研究环境”页面选择需要的模块。SeedEnv
准备软件、连接已有安装，并提供实际调用入口、简明工作说明和起步程序。
光学光子学 AI 实验室、IOP 等专业环境继续维护自己的研究方法和专业积累。

## 开始使用

需要 Python 3.11 或更新版本。在项目目录执行：

```sh
python -m pip install .
seedenv search 光学
seedenv plan optics molecules writing
seedenv prepare optics molecules
seedenv example optics --output thin_film.py
seedenv run python-optics -- thin_film.py
```

默认软件位置是 `~/.seedenv`。可通过 `SEEDENV_HOME`，或命令前的
`seedenv --home PATH ...` 指定持久目录。研究程序和数据放在研究空间。
环境准备与 Agent 对其他目录的读写范围分别管理。

示例可以改写为自己的完整程序；`seedenv entry COMPONENT` 返回真实解释器或
可执行程序，后续计算使用上游完整接口。

## 可组合的内容

第一批提供 **27 个模块**，覆盖科学计算、表格数据、统计与金融回测、机器学习、
优化、化学分子、材料结构、生物序列、医学影像、地理、图像、有限元、CAD、
电路、光学、量子、天文、仪器、网络、论文写作、R、Julia、文献和数据库连接，
以及现有专业环境的接入。具体模块和软件见 [英文首页的对应表](README.md#modules)。

每个模块包含软件引用、适用任务、工作说明和上游文档，适合时再附起步程序。
组合引用同一组件，不重复维护。引导围绕模型选择、输入含义、单位、时间关系、
数据接口和结果解释展开，避免把泛泛的“专家角色”提示词作为专业能力。

Python 组件可以自动安装。LaTeX、R、Julia、ngspice 连接已有程序；其中 LaTeX
也可交给 Origo 已有的 `research-tex` 准备流程。独立命令目前不负责系统包安装。
插件激活、数据服务账户和仪器连接由产品已有的连接管理完成。
找到可执行文件代表可以登记入口，额外字体、驱动和后端仍取决于实际安装。

## 长期使用

```sh
seedenv discover science --python /已有环境/bin/python
seedenv bind python-science -- /已有环境/bin/python
seedenv installed
seedenv prepare optics --background
seedenv status JOB_ID
seedenv cancel JOB_ID
```

重复准备会复用已完成的组件；新增模块只准备缺少的组件。依赖需要改变时创建
新目录，保留旧目录供正在运行的程序使用。某个组件准备失败，不影响已完成的部分。
后台准备需要所在机器和进程持续运行。

Windows、macOS、Linux 使用相同接口，但具体软件遵循上游的平台要求。
服务器或 WSL 上的环境在对应执行位置准备，产品通过已有远程通道调用。
本项目不假定所有求解器原生支持所有系统。

## 产品接入

```sh
seedenv connect origo --output ./seedenv-origo
seedenv connect mcp --output ./seedenv-mcp
seedenv plan optics writing --host origo
```

Origo 导出包包含可独立运行的 MCP 和一份短 Skill，随后在产品插件管理中导入、
启用。通用 MCP 导出包也包含服务代码，配置使用当前 Python。
Agent 按需读取模块说明，取得解释器后编写和运行自己的研究程序。

TypeScript 提供调用客户端和可嵌入的模块选择组件；Rust 提供原生产品调用端；
Python 负责组合和准备；SQLite 保存实际软件位置与准备进度。
科学软件已有的 C/C++ 等内核直接复用。

这些接入组件已在本项目实现。**它们尚未随某个 Origo 发布版本上线**；具体页面
接线与插件启用见 [接入说明](docs/integration.md)。

扩展新领域主要是添加模块内容，见 [模块说明](docs/modules.md)。实际运行情况见
[实现说明](docs/implementation.md)。SeedEnv 使用 MIT 许可证，上游软件遵循各自许可证。
