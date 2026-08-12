# Telemetry-Log-Anomaly-Detector
The program successfully detects anomalies(problematic) metrics from a set of simulated telemetry logs. 

Main Algorithm:

Part - I (data creation)
1. Created artificial site codes(location) to simulate real telemetry logs.
2. Introduced basic network parameters such as latency, status code, and packet loss percent to start detecting anomalies.
[The data metric count was set to 2000(sample_size).]
3. Using CSV library to write the data to a file, named: "my_network_logs.csv" with headers such as location, latency, packet loss and status code.
4. Set the anomaly generation rate to 2%. Next was setting measurements to differentiate an anomaly and a normal healthy network log.

In normal range:
  - Latency-ms : 10-70
  - Packet_loss : 0.0 - 3.0
  - status-code : 200, 429, 503 with probability of 95, 4, 1.

In anomaly range:
  - Latency-ms : 60-300
  - Packet_loss : 2.0-20.0
  - status-code : 200, 503, 504, 0 with probability of 15, 45, 30, 10.

Part - II (SQL & Database Pipeline)
1. Using sqlite3, used basic queries to create a table with similar headers to the CSV file.
2. Developed an automated ETL (Extract, Transform, Load) pipeline script named net_db_pl.py to open the generated CSV file, parse the telemetry strings, and continuously put the records directly into the SQL database.
3. Implemented standard database cleanup procedures to handle the pipeline's execution state.
Extra: Realized during testing that if the old database file isn't cleared out before a new simulation run, SQL will continuously append data, leading to mixed metrics and false analytical outcomes. Added a step to clear the old table state to ensure a clean 2,000-row structure every run.
5. Wrote an analytics verification script (test_query.py) using structured SQL queries to analyze the imported data.

Part - III (Pandas Integration & Machine Learning)
1. Created the final engine script, network_ai_detector.py, moving away from manually hardcoded SQL logic and switching to programmatic, pattern-based anomaly detection.
2. Utilized the pandas data science library to run an internal query against the SQLite database, converting the static relational table instantly into an in-memory data matrix or a Data-Frame.
3. Extracted the numerical features, specifically "latency_ms" and "packet_loss_percent" to pass directly to the machine learning model.
4. Imported and initialized the Isolation Forest unsupervised machine learning algorithm from scikit-learn to map and isolate anomalous behavior using two critical parameters:
   contamination=0.02: to expect roughly a 2% outlier distribution across the dataset.
   random_state=42: to ensure repeatable results across any system execution.
5. The algorithm successfully flagged 40 distinct anomalies completely on its own without using a single traditional if/else threshold line.
  - It accurately grouped the extreme 503 outages.
  - It caught subtle performance drifts (mild rows sitting at 34ms latency) that a human setting static thresholds would completely miss, proving the adaptive capability of unsupervised learning.
6. The final part of this section compares the results of a normal query with the Forest Isolation Algorithm's script to detect anomalies. Showcases the precision of the Isolation Forest Model compared to a normal query.

Part - IV (Data Visualization Reporting)
1. Integrated the matplotlib charting library to translate the multi-dimensional numeric data frames into visual plot graphs.
2. Programmed a scatter plot utilizing a 4-step execution flow.
3. Blue Cluster: Represents dense, healthy, low-latency background operations across the province's sites.
4. Red Plots: Highlights the 40 distinct, isolated system anomalies flagged entirely by the Isolation Forest model.
