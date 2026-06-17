import random
import csv

net_locations = ["Regina_Core_Switch_01", "Saskatoon_Core_Switch_01", "Moose-Jaw_Core_Switch_02"]
numRows = 2000


with open("sasktel_network_logs.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["location", "latency_ms", "packet_loss_percent", "status_code"])

    for _ in range(numRows):
        location = random.choice(net_locations)
        is_anomaly = random.random() < 0.02 #Failure rate.

        #Anomaly range
        if is_anomaly:
            latency = round(random.uniform(300.0, 500.0), 2)
            packet_loss = round(random.uniform(5.0, 20.0), 2)
            status_code = 503
        #Normal Range
        else:
            latency = round(random.uniform(10.0, 35.0), 2)
            packet_loss = round(random.uniform(0.0, 0.5), 2)
            status_code = 200

        writer.writerow([location, latency,  packet_loss, status_code])

