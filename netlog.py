import random
import csv

net_locations = ["Regina_Core_Switch_01", "Saskatoon_Core_Switch_01", "Moose-Jaw_Core_Switch_01",
                  "Prince-Albert_Core_Switch_01", "Lloydminster_Core_Switch_01"]
numRows = 2000


with open("my_network_logs.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["location", "latency_ms", "packet_loss_percent", "status_code"])

    for _ in range(numRows):
        location = random.choice(net_locations)
        is_anomaly = random.random() < 0.02 #Failure rate.
        """

            1. Latency over 150 m/s is considered alarming. (range used: 60-300m/s to offer transition). The latency overlaps the
            normal range making the simulation more realistic.
            2. Same goes for packet_loss. Where there is an overlapping b/w normal and anomaly range.

            #Note, status code: Only used as a representational asset rather than a feature to be used later on.

            Status Code: Explanation:
            1. Code-200 represents healthy connection. Anomaly represents 15% of having a healthy network.
            2. Code-503 server received request but could not process it due to n reasons.
            3. Code-504 taking too long to respond.
            4. Code-0 nothing responded.
            5. Code-429 too many requests.

        """

        if is_anomaly:
            latency = round(random.uniform(60.0, 300.0), 2)
            packet_loss = round(random.uniform(2.0, 20.0), 2)
            status_code = random.choices([200, 503, 504, 0],
                                         weights=[15, 45, 30, 10])[0]
        #Normal Range
        else:
            latency = round(random.uniform(10.0, 70.0), 2)
            packet_loss = round(random.uniform(0.0, 3.0), 2)
            status_code = random.choices([200, 429, 503], weights=[95, 4, 1])[0]

        writer.writerow([location, latency,  packet_loss, status_code])

