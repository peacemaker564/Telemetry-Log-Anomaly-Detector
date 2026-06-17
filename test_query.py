import sqlite3

conn = sqlite3.connect("sasktel_network.db") #Connection
cur = conn.cursor()

cur.execute("""
            SELECT * FROM network_logs
            WHERE latency_ms > 100;

            """)
high_latency_logs = cur.fetchall()


for logs in high_latency_logs:
    print(logs)


print(f"Alert found: {len(high_latency_logs)}!")
