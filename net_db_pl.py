import sqlite3
import csv

connection = sqlite3.connect("sasktel_network.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS network_logs (
            location VARCHAR(50),
            latency_ms DECIMAL(5, 2),
            packet_loss_percent DECIMAL(5, 2),
            status_code INT
                                            );

""")

with open("sasktel_network_logs.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""

    INSERT INTO network_logs (location, latency_ms, packet_loss_percent, status_code)
    VALUES(?, ?, ?, ?)""",

    (row["location"],
     float(row["latency_ms"]),
     float(row["packet_loss_percent"]),
     int(row["status_code"])

    ))

connection.commit()
connection.close()
