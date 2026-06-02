from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, sum

# Create Spark Session
spark = SparkSession.builder \
    .appName("YahooMarketStockBatchAnalysis") \
    .getOrCreate()

# Load Dataset from HDFS
df = spark.read.csv(
    "hdfs://namenode:9000/stock-data/stock_data.csv",
    header=True,
    inferSchema=True
)

# Show Data
print("\n==============================")
print(" Historical Stock Data Preview ")
print("==============================")

df.show(5)

# Average Close Price
print("\n==============================")
print(" Average Close Price ")
print("==============================")

avg_close = df.groupBy("Ticker").agg(
    avg("Close").alias("Average_Close")
)

avg_close.orderBy(
    "Average_Close",
    ascending=False
).show()

# Highest Trading Volume
print("\n==============================")
print(" Highest Trading Volume ")
print("==============================")

volume_analysis = df.groupBy("Ticker").agg(
    sum("Volume").alias("Total_Volume")
)

volume_analysis.orderBy(
    "Total_Volume",
    ascending=False
).show()

# Price Range Analysis
print("\n==============================")
print(" Price Range Analysis ")
print("==============================")

price_range = df.groupBy("Ticker").agg(
    max("High").alias("Highest_Price"),
    min("Low").alias("Lowest_Price")
)

price_range.show()

# Stop Session
spark.stop()