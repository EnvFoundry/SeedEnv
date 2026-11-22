# MQTT streams · MQTT 数据流

Read instrument and telemetry topic streams.

Define topic, payload schema, QoS and retained-message handling. Timestamp messages at the source when possible and distinguish a repeated delivery from a new physical observation.

读取仪器与遥测主题数据流。

明确主题、载荷结构、QoS 与保留消息处理。尽可能使用源时间戳，区分重复投递与新的物理观测。

Software / 软件：Eclipse Paho MQTT (`python-mqtt`).

Use `seedenv context mqtt-streams` for software entries and setup on this host.

- https://eclipse.dev/paho/files/paho.mqtt.python/html/
