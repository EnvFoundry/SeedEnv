# Instrument emulation · 仪器通信模拟

Develop instrument communication against an explicitly simulated VISA backend.

Use @sim or an explicit device-description file with the actual PyVISA API. Exercise commands, termination and readbacks. Simulated replies model only the declared behavior, not physical timing, noise or hardware compatibility.

使用 @sim 或指定模拟设备描述，通过真实 PyVISA API 演练命令、终止符与读回流程。模拟记录只代表声明的设备行为，不代表真实噪声、时序或仪器兼容性。附带程序完成一轮模拟设备通信，之后可替换为项目的设备描述。

Software / 软件：PyVISA-sim (`python-visa-sim`).

- [Upstream documentation](https://pyvisa.readthedocs.io/projects/pyvisa-sim/en/latest/)
