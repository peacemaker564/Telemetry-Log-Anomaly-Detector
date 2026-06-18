# Telemetry-Log-Anomaly-Detector
The program successfully detects anomalies(problematic) metrics from a set of simulated telemetry logs. 

Main Algorithm:
Part - I (data creation)
1. Created artificial site codes(location) to simulate real telemetry logs.
2. Introduced basic network parameters such as latency, status code, and packet loss percent to start detecting anomalies.
[The data metric count was set to 2000(sample_size).]
3. Using CSV library to write the data to a file, named: "sasktel_network_logs.csv"(sasktel was chosen due to its high visibility in saskatchewan specific regions) with headers such as location, latency, packet loss and status code.
4. Set the anomaly generation rate to 2%. Next was setting measurements to differentiate an anomaly and a normal healthy network log.
  In normal range:
  - Latency-ms : 10-35
  - Packet_loss : 0.0 - 0.5
  - status-code : 200

  In anomaly range:
  - Latency-ms : 300-500
  - Packet_loss : 5.0-20.0
  - status-code : 503

