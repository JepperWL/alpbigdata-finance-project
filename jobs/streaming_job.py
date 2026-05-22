from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Spark Session
spark = SparkSession.builder \
    .appName("StockMarketStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Schema
schema = StructType([
    StructField("Date", StringType(), True),
    StructField("Open", DoubleType(), True),
    StructField("High", DoubleType(), True),
    StructField("Low", DoubleType(), True),
    StructField("Close", DoubleType(), True),
    StructField("Volume", DoubleType(), True),
    StructField("Ticker", StringType(), True)
])

# Read stream from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "stock-market") \
    .option("startingOffsets", "earliest") \
    .load()

# Convert Kafka value to JSON
json_df = df.selectExpr("CAST(value AS STRING)")

parsed_df = json_df.select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

# Aggregation
agg_df = parsed_df.groupBy("Ticker").agg(
    avg("Close").alias("Average_Close"),
    max("Volume").alias("Max_Volume")
)

# Output to console
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()