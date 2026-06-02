from kafka import KafkaProducer
import pandas as pd
import json
import time

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = "stock-market"

print("Starting Kafka Producer...")

# Load dataset
df = pd.read_csv("../data/stock_data.csv")

# Send first 100 rows
for index, row in df.sample(100).iterrows():

    message = {
        "Date": str(row.get("Date", "")),
        "Open": float(row.get("Open", 0)),
        "High": float(row.get("High", 0)),
        "Low": float(row.get("Low", 0)),
        "Close": float(row.get("Close", 0)),
        "Volume": float(row.get("Volume", 0)),
        "Ticker": str(row.get("Ticker", "UNKNOWN"))
    }

    producer.send(topic_name, value=message)

    print(f"Sent: {message}")

    time.sleep(1)

producer.flush()

print("Finished sending data.")