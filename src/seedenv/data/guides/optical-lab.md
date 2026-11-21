# Optics–Photonics AI Lab · 光学专业环境

接入已有光学模型、求解器与研究程序。

1. 在宿主中导入上游插件，连接已有计算主机与 OPTICS_HOME。
2. 通过其 prepare/bind 接口选择求解器；专业模型、材料数据与研究程序继续由该环境维护。
3. 保留已安装环境的名称、连接与研究数据；本模块提供发现与接入入口。

查看组件与准备方式：`seedenv show optical-lab`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

上游文档：

- https://github.com/EnvFoundry/Optics-Photonics-AI-Lab
