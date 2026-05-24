# 📈 Yahoo Finance Market Stock
## End-of-Semester Project — Big Data Processing
---

# Table of Contents

1. Executive Summary
2. Introduction
3. Project Background
4. System Objectives
5. Architecture Diagram
6. System Architecture Explanation
7. Problem Statement
8. Business Questions
9. Dataset Explanation
10. Technology Stack
11. Project Structure
12. End-to-End Pipeline Workflow
13. Detailed Component Explanation
14. Distributed Processing Concepts
15. Real-Time Streaming Concepts
16. Batch Processing Concepts
17. Dashboard Visualization System
18. How To Run
19. Expected Output
20. Dashboard Features
21. Batch Analysis Findings
22. Streaming Analysis Findings
23. Technical Challenges Faced
24. Learning Outcomes
25. System Limitations
26. Future Improvements
27. Conclusion

---

# Executive Summary

Yahoo Market Stock is a distributed real-time financial analytics platform designed to simulate how modern big data systems process, analyze, and visualize stock market activity.

This project combines:

* Apache Kafka,
* Apache Spark Structured Streaming,
* Docker Compose,
* Python,
* and Streamlit

to build a complete end-to-end big data processing pipeline capable of supporting both:

* historical batch analysis,
* and real-time streaming analytics.

The system continuously streams stock market records into Kafka using a custom Python producer. Apache Spark Structured Streaming consumes the incoming stock market events and performs distributed financial analytics such as:

* volume aggregation,
* stock activity analysis,
* market fluctuation monitoring,
* and streaming event processing.

Simultaneously, Spark batch processing analyzes historical market activity to identify:

* dominant companies,
* historical price ranges,
* highest trading volumes,
* and long-term financial patterns.

The analytics results are visualized through an interactive Streamlit dashboard designed using a modern fintech-inspired interface.

This project demonstrates how distributed technologies can work together to build scalable, reproducible, and efficient financial analytics systems.

---

# Introduction

Modern industries generate massive amounts of data every second. Financial markets are among the largest producers of continuously changing real-time information.

Every stock transaction generates:

* market activity,
* trading volume,
* price movement,
* and financial indicators.

As financial markets grow increasingly data-driven, companies require systems capable of:

* handling high-throughput streaming data,
* processing analytics with low latency,
* and visualizing insights in real time.

Traditional systems often struggle with:

* scalability limitations,
* inefficient data processing,
* delayed analytics,
* and infrastructure bottlenecks.

To solve these problems, modern financial systems rely heavily on distributed technologies such as:

* Apache Kafka,
* Apache Spark,
* distributed streaming platforms,
* and scalable visualization systems.

This project was developed to simulate a modern distributed financial analytics architecture capable of:

* streaming stock market events,
* processing financial analytics,
* and visualizing real-time market intelligence.

The project demonstrates practical implementations of:

* real-time data engineering,
* distributed analytics,
* stream processing,
* and containerized big data infrastructures.

---

# Project Background

The financial sector increasingly depends on real-time analytics systems for:

* stock monitoring,
* market intelligence,
* fraud detection,
* algorithmic trading,
* and investment decision-making.

Modern financial systems must continuously process:

* millions of events,
* large-scale transactions,
* and rapidly changing market activity.

As data volume grows, traditional monolithic systems become insufficient due to:

* limited scalability,
* slow processing performance,
* and centralized bottlenecks.

Distributed technologies provide solutions by enabling:

* scalable event streaming,
* distributed processing,
* parallel computation,
* and real-time analytics generation.

This project was inspired by how financial companies use:

* Kafka for streaming infrastructure,
* Spark for distributed analytics,
* and interactive dashboards for real-time visualization.

The project demonstrates how these technologies can be integrated into a simplified but realistic financial analytics platform.

---

# System Objectives

The primary objective of this project is to develop a distributed big data pipeline capable of handling:

* historical financial analysis,
* real-time stock market event processing,
* and interactive visualization.

The project aims to:

* simulate stock market streaming activity,
* process financial analytics using distributed systems,
* generate both batch and streaming insights,
* and visualize analytics interactively.

Additional objectives include:

* demonstrating Kafka event streaming,
* implementing Spark Structured Streaming,
* applying distributed batch analytics,
* and building a containerized analytics infrastructure.

---

# Architecture Diagram

The following architecture illustrates the complete end-to-end data pipeline used in this project.

<img width="1536" height="1024" alt="YahooMarketArchitectureDiagram" src="https://github.com/user-attachments/assets/cecf448c-782b-4f46-9c7e-a23132ab793f" />

---

# System Architecture Explanation

The architecture consists of several interconnected distributed components responsible for:

* event ingestion,
* stream processing,
* distributed analytics,
* and visualization.

Each layer has a specific responsibility within the pipeline.

---

# 1️. Historical Dataset Layer

The pipeline begins with a historical stock market dataset stored in CSV format (`stock_data.csv`).

The dataset contains:

* opening prices,
* closing prices,
* highest prices,
* lowest prices,
* trading volume,
* and company information.

This dataset acts as the primary data source for:

* historical batch analytics,
* and simulated real-time stock event streaming.

The dataset provides realistic financial market activity used throughout the system.

---

# 2️. Kafka Producer Layer

The Kafka producer is implemented using Python.

The producer continuously:

* reads stock market records,
* transforms rows into streaming events,
* serializes stock information,
* and streams messages into Apache Kafka.

Instead of sending all records simultaneously, the producer streams data gradually to simulate:

* live stock activity,
* real-time event flow,
* and continuous market movement.

This creates a realistic streaming environment similar to actual financial infrastructures.

---

# 3️. Apache Kafka Streaming Layer

Apache Kafka acts as the distributed event streaming platform.

Kafka is responsible for:

* receiving stock market events,
* storing streaming messages,
* and distributing events to downstream consumers.

Kafka enables:

* asynchronous communication,
* high-throughput event ingestion,
* scalability,
* fault tolerance,
* and distributed event handling.

Within this project, Kafka serves as the communication bridge between:

* the producer,
* and Spark Structured Streaming.

Kafka allows stock events to be processed continuously without tight coupling between services.

---

# 4️. Spark Structured Streaming Layer

Apache Spark Structured Streaming functions as the distributed stream processing engine.

Spark continuously consumes stock market events from Kafka and performs:

* real-time aggregation,
* distributed analytics,
* market activity monitoring,
* and streaming financial calculations.

Spark processes streaming data using:

* distributed computation,
* micro-batch execution,
* and parallel analytics processing.

The streaming layer enables:

* low-latency analytics,
* scalable processing,
* and continuous financial event monitoring.

This demonstrates how modern distributed processing systems analyze continuously incoming data streams efficiently.

---

# 5️. Batch Processing Layer

In addition to streaming analytics, Spark also performs historical batch analysis.

The batch processing job analyzes:

* average stock prices,
* highest trading volumes,
* historical market fluctuations,
* and company performance trends.

Batch processing demonstrates Spark’s ability to:

* process large historical datasets,
* perform distributed computation,
* and generate long-term analytical insights.

This layer complements the streaming pipeline by providing historical financial intelligence.

---

# 6️. Dashboard Visualization Layer

The Streamlit dashboard acts as the visualization and presentation layer.

The dashboard visualizes:

* financial KPIs,
* stock activity,
* streaming analytics,
* market movement,
* interactive charts,
* and financial insights.

The dashboard was designed using a modern fintech-inspired interface to simulate professional financial analytics platforms.

The visualization layer transforms complex streaming data into:

* understandable insights,
* interactive analytics,
* and user-friendly financial dashboards.

---

# Problem Statement

Financial institutions require systems capable of:

* processing continuously incoming market events,
* analyzing large-scale historical data,
* and visualizing analytics in real time.

Traditional systems often struggle with:

* delayed analytics,
* scalability limitations,
* infrastructure bottlenecks,
* and inefficient data processing pipelines.

This project addresses these challenges by implementing a distributed financial analytics system capable of:

* ingesting stock events in real time,
* processing distributed analytics,
* generating streaming insights,
* and visualizing market intelligence interactively.

The project demonstrates how distributed technologies can support scalable financial analytics infrastructures.

---

# Business Questions

The project was designed to answer several analytical business questions.

---

# Historical Batch Analytics Questions

Which companies:

* generate the highest trading volumes?
* demonstrate the highest average closing prices?
* show the widest historical price fluctuations?
* dominate long-term market activity?

---

# Real-Time Streaming Analytics Questions

Which stocks are currently:

* experiencing abnormal activity?
* generating unusual volume spikes?
* showing rapid price movement?
* dominating streaming analytics?

---

# Dataset Explanation

## Dataset Name

`stock_data.csv`
---

## Dataset Domain

Financial Market Analytics

---

## Dataset Description

The dataset contains historical stock market trading records from multiple publicly traded companies.

Each row represents:

* one company,
* on one trading day,
* with corresponding financial activity.

The dataset includes:

* opening prices,
* highest prices,
* lowest prices,
* closing prices,
* trading volumes,
* and company identifiers.

---

## Dataset Fields

| Column  | Description         |
| ------- | ------------------- |
| Date    | Trading date        |
| Open    | Opening stock price |
| High    | Highest stock price |
| Low     | Lowest stock price  |
| Close   | Closing stock price |
| Volume  | Trading volume      |
| Company | Company name        |

---

## Dataset Usage

The dataset is utilized for:

* Kafka event streaming,
* Spark streaming analytics,
* batch processing,
* dashboard visualization,
* and financial insight generation.

---

# Technology Stack

| Technology     | Purpose                      |
| -------------- | ---------------------------- |
| Python         | Core programming language    |
| Apache Kafka   | Real-time event streaming    |
| Apache Spark   | Distributed analytics engine |
| PySpark        | Batch & streaming processing |
| Docker Compose | Container orchestration      |
| Streamlit      | Interactive dashboard        |
| Pandas         | Data manipulation            |
| Plotly         | Interactive visualization    |

---

# Project Structure

```bash id="f6i6h4"
alpbigdata-finance-project/
│
├── docker-compose.yml
├── README.md
│
├── producer/
│   ├── producer.py
│   └── requirements.txt
│
├── jobs/
│   ├── batch_analysis.py
│   └── streaming_job.py
│
├── dashboard/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
│
└── data/
    └── stock_data.csv
```

---

# End-to-End Pipeline Workflow

The project follows the workflow below:

1. Historical stock market data is loaded from CSV.
2. The Python producer streams stock events into Kafka.
3. Kafka stores and distributes streaming messages.
4. Spark Structured Streaming consumes stock events.
5. Spark performs distributed analytics processing.
6. Batch jobs analyze historical financial activity.
7. Streamlit visualizes streaming analytics interactively.

---

# Detailed Component Explanation

## Kafka Producer

Responsible for:

* event generation,
* real-time simulation,
* and message streaming.

---

## Kafka Broker

Responsible for:

* event ingestion,
* asynchronous communication,
* and distributed message handling.

---

## Spark Streaming

Responsible for:

* distributed analytics,
* stream aggregation,
* and real-time processing.

---

## Batch Processing

Responsible for:

* historical insight generation,
* large-scale analysis,
* and long-term financial analytics.

---

## Streamlit Dashboard

Responsible for:

* interactive visualization,
* financial KPI presentation,
* and real-time dashboard rendering.

---

# Distributed Processing Concepts

The project demonstrates distributed computing concepts such as:

* parallel analytics,
* distributed execution,
* scalable processing,
* and fault-tolerant architectures.

Apache Spark distributes computations across processing tasks to improve:

* performance,
* scalability,
* and analytics efficiency.

---

# Real-Time Streaming Concepts

The streaming pipeline demonstrates:

* continuous event processing,
* asynchronous communication,
* low-latency analytics,
* and live market monitoring.

Kafka and Spark work together to create a scalable streaming infrastructure capable of handling continuously incoming financial events.

---

# Batch Processing Concepts

Batch processing enables the system to:

* analyze historical financial trends,
* process large datasets efficiently,
* and generate long-term market intelligence.

Spark batch analytics calculate:

* average prices,
* market activity,
* trading volume,
* and historical price fluctuations.

---

# Dashboard Visualization System

The dashboard was designed using:

* Streamlit,
* Plotly,
* and interactive financial visualization techniques.

The dashboard includes:

* KPI cards,
* donut charts,
* volume analytics,
* interactive market charts,
* and real-time stock activity monitoring.

The design was inspired by modern:

* fintech dashboards,
* trading platforms,
* and financial intelligence systems.

---

# How To Run

## Step 1 — Clone Repository

```bash id="abpjxv"
git clone <repository-url>
cd alpbigdata-finance-project
```

---

## Step 2 — Start Docker Containers

```bash id="1v7pn9"
docker compose up -d
```

---

## Step 3 — Verify Containers

```bash id="8q8f96"
docker ps
```

Expected running containers:

* zookeeper
* kafka
* spark
* streamlit

---

## Step 4 — Create Kafka Topic

```bash id="hm7mkf"
docker exec -it kafka bash
```

Inside Kafka container:

```bash id="8qog3k"
/opt/kafka/bin/kafka-topics.sh \
--create \
--topic stock-market \
--bootstrap-server localhost:9092
```

---

## Step 5 — Run Kafka Producer

Open new terminal:

```bash id="8z94bq"
cd producer
python producer.py
```

---

## Step 6 — Run Spark Streaming Job

```bash id="6g8xv4"
docker exec -it spark bash
```

Inside Spark container:

```bash id="3guhja"
spark-submit /home/jovyan/work/jobs/streaming_job.py
```

---

## Step 7 — Run Batch Analysis

Inside Spark container:

```bash id="j6v5z0"
spark-submit /home/jovyan/work/jobs/batch_analysis.py
```

---

## Step 8 — Open Dashboard

Open browser:

```bash id="nl4l7m"
http://localhost:8501
```

---

# Expected Output

## Kafka Producer Output

The producer continuously streams stock events into Kafka.

Example:

```bash id="o9rq8k"
Sent: {'Company': 'AAPL', 'Close': 194.5, 'Volume': 1200000}
```

---

## Spark Streaming Output

Spark continuously processes stock events and generates:

* streaming analytics,
* real-time aggregation,
* and market activity monitoring.

---

## Batch Processing Output

Spark batch jobs generate:

* average closing price analysis,
* highest trading volume analysis,
* and historical market insights.

---

## Dashboard Output

The dashboard visualizes:

* real-time stock analytics,
* KPI metrics,
* volume distribution,
* streaming activity,
* and financial charts.

---

# Dashboard Features

The dashboard includes:

* Interactive KPI cards
* Donut charts
* Volume analytics
* Market share visualization
* Live streaming feed
* Financial charts
* Modern fintech-inspired UI
* Real-time auto-refresh analytics
* Streaming activity monitoring

---

# Batch Analysis Findings

The historical analysis revealed several important financial insights.

## Key Findings

* TSLA and AAPL generated extremely high trading volumes.
* Technology companies dominated overall market activity.
* Historical stock volatility varied significantly between companies.
* High-volume companies consistently demonstrated strong market influence.
* Several companies exhibited significant historical price fluctuations.

The batch analysis demonstrates Spark’s ability to process large historical datasets efficiently using distributed analytics.

---

# Streaming Analysis Findings

The streaming pipeline successfully simulated real-time financial analytics.

Observed behaviors include:

* continuous event ingestion,
* real-time analytics generation,
* dynamic market activity,
* and low-latency streaming.

Kafka and Spark successfully demonstrated:

* scalable event streaming,
* distributed stream processing,
* and real-time market intelligence generation.

---

# Technical Challenges Faced

Several technical challenges were encountered during development.

## Main Challenges

* Kafka topic configuration
* Docker volume mounting issues
* Spark path configuration
* Kafka producer connectivity
* Streaming synchronization debugging
* Streamlit dependency setup
* Spark Kafka integration
* Distributed processing troubleshooting

These challenges provided valuable practical experience in:

* big data engineering,
* distributed systems debugging,
* and real-time analytics infrastructures.

---

# Learning Outcomes

Through this project, several important technical concepts were implemented and learned.

## Technical Skills Acquired

* Apache Kafka event streaming
* Spark Structured Streaming
* Distributed analytics processing
* Docker container orchestration
* Financial dashboard development
* Big data pipeline architecture
* Real-time event handling
* Stream processing systems
* Financial analytics visualization
* Distributed systems debugging

The project provided practical experience similar to real-world financial data engineering systems.

---

# System Limitations

Although the system successfully demonstrates a complete big data workflow, several limitations remain.

## Current Limitations

* Historical CSV data is used instead of live APIs
* Kafka operates using a single broker configuration
* Spark processing runs locally instead of distributed clusters
* No cloud deployment has been implemented
* Dashboard analytics remain simplified
* No persistent database storage exists
* Real-time alert systems are not implemented

---

# Future Improvements

Several improvements could enhance the system further.

## Potential Enhancements

* Integration with live Yahoo Finance APIs
* Distributed Spark cluster deployment
* Cloud deployment using AWS or Google Cloud
* Machine learning stock prediction models
* Real-time anomaly detection
* Advanced dashboard filtering
* Multi-broker Kafka architecture
* Real-time notification systems
* Persistent historical storage
* User authentication system

---

# Conclusion

Yahoo Market Stock successfully demonstrates the implementation of a distributed end-to-end financial analytics pipeline using modern big data technologies.

By integrating:

* Apache Kafka,
* Apache Spark Structured Streaming,
* Docker Compose,
* Python,
* and Streamlit,

the system was able to:

* ingest streaming financial events,
* process distributed analytics,
* perform historical batch analysis,
* and visualize financial intelligence interactively.

The project demonstrates how distributed technologies can work together to create scalable, reproducible, and efficient financial analytics systems.

In addition to fulfilling academic requirements, this project also provided practical experience in:

* distributed systems,
* stream processing,
* financial analytics engineering,
* and big data infrastructure deployment.

---

## Project Submission Branch
This project was submitted for Big Data Processing Class A — Group 5.
