import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

con = sqlite3.connect("sasktel_network.db")
query = "SELECT location, latency_ms, packet_loss_percent, status_code FROM network_logs;" #Setting table variables.
df = pd.read_sql_query(query, con) #Uses the query(columns), and connection variable to save data into the dataframe.
con.close() #Closes the connection.

features = df[["latency_ms", "packet_loss_percent"]]
#Separating the actual parameters that the AI will need for its analysis.

#Setting similar anomaly detection rate in contamination.
#Setting a construct random_state for similar results on every run.
mod = IsolationForest(contamination = 0.02, random_state = 42)

#Training the AI on recognizing baseline and anomaly data.
#here, 1 is for normal data, and -1 for anomaly.
df["ai_prediction"] = mod.fit_predict(features)

#Filter out the anomaly data.
ai_anomalies = df[df["ai_prediction"] == -1]

#now, printing the data.

print("AI Anomaly Detection Successful.")
print(f"The anomaly count flagged by AI out of the 2000 rows is: {len(ai_anomalies)}")
print("\nBelow are the first few anomalies detected from data pattern:")
anom_data = ai_anomalies[["location","latency_ms", "packet_loss_percent", "status_code"]].head()
print(anom_data)



# Create a scatter plot of the network metrics
plt.figure(figsize=(10, 6))

# Plot normal points in blue
normal = df[df["ai_prediction"] == 1]
plt.scatter(normal["latency_ms"], normal["packet_loss_percent"], c="blue", label="Normal Operations", alpha=0.5)

# Plot AI-detected anomalies in red
anomalies = df[df["ai_prediction"] == -1]
plt.scatter(anomalies["latency_ms"], anomalies["packet_loss_percent"], c="red", label="AI Detected Anomalies", edgecolors="black", s=100)

# Add chart details
plt.title("SaskTel Core Network Infrastructure - AI Anomaly Detection", fontsize=14)
plt.xlabel("Latency (ms)", fontsize=12)
plt.ylabel("Packet Loss (%)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Save the plot as an image file in your folder
plt.savefig("sasktel_ai_report.png")
print("\n[SUCCESS] Visual report saved as 'sasktel_ai_report.png'!")
