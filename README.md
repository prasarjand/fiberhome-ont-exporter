
## Fiberhome HG6145D2 Prometheus Exporter

simple script for pulling prometheus metric from fiberhome ONT


## Setup 

Adjust and copy fiberhome-exporter.service to below path

/etc/systemd/system/fiberhome-exporter.service

Run below command
```
sudo systemctl daemon-reload
sudo systemctl start fiberhome-exporter
sudo systemctl enable fiberhome-exporter
```

the program will run at 127.0.0.1:8000


Sample Output
```
# HELP fiberhome_uptime FiberHome Uptime
# TYPE fiberhome_uptime gauge
fiberhome_uptime{device="HG6145D2"} 23564.0
# HELP fiberhome_cpu_usage FiberHome CPU usage
# TYPE fiberhome_cpu_usage gauge
fiberhome_cpu_usage{device="HG6145D2"} 2.0
# HELP fiberhome_mem_total FiberHome total memory
# TYPE fiberhome_mem_total gauge
fiberhome_mem_total{device="HG6145D2"} 524288.0
# HELP fiberhome_mem_free FiberHome free memory
# TYPE fiberhome_mem_free gauge
fiberhome_mem_free{device="HG6145D2"} 366292.0
# HELP fiberhome_rx_power FiberHome optical rxpower
# TYPE fiberhome_rx_power gauge
fiberhome_rx_power{device="HG6145D2"} -23.98
# HELP fiberhome_tx_power FiberHome optical txpower
# TYPE fiberhome_tx_power gauge
fiberhome_tx_power{device="HG6145D2"} 2.15
# HELP fiberhome_ponbytesent FiberHome PON Byte Sent
# TYPE fiberhome_ponbytesent gauge
fiberhome_ponbytesent{device="HG6145D2"} 1.2926440887e+010
# HELP fiberhome_ponbytereceived FiberHome PON Byte Received
# TYPE fiberhome_ponbytereceived gauge
fiberhome_ponbytereceived{device="HG6145D2"} 4.79836708e+08
# HELP fiberhome_ponpacketssent FiberHome PON Packet Sent 
# TYPE fiberhome_ponpacketssent gauge
fiberhome_ponpacketssent{device="HG6145D2"} 1.2885138114e+010
# HELP fiberhome_ponpacketsreveived FiberHome PON Packet Received
# TYPE fiberhome_ponpacketsreveived gauge
fiberhome_ponpacketsreveived{device="HG6145D2"} 5.866389e+06
# HELP fiberhome_supplyvottage FiberHome PON supply voltage 
# TYPE fiberhome_supplyvottage gauge
fiberhome_supplyvottage{device="HG6145D2"} 3.26
# HELP fiberhome_biascurrent FiberHome PON bias Current
# TYPE fiberhome_biascurrent gauge
fiberhome_biascurrent{device="HG6145D2"} 10.08
# HELP fiberhome_transceivertemperature FiberHome PON transceivertemperature
# TYPE fiberhome_transceivertemperature gauge
fiberhome_transceivertemperature{device="HG6145D2"} 44.78

```