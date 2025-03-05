# KDP - Kafka - Flink - Pinot

This repo is designed to get the user introduced to the KDP stack.

## Abstract

In today’s fast-paced digital landscape, businesses demand real-time insights to stay competitive. This workshop demonstrates the seamless integration of Apache Kafka, Apache Flink, and Apache Pinot to build a robust, scalable, and high-performance real-time data pipeline. Participants will explore how Kafka serves as the backbone for event streaming, Flink powers sophisticated stream processing, and Pinot delivers lightning-fast analytics—all working together to transform raw data into actionable insights instantly. Through a hands-on demo, we’ll simulate a real-world use case (a gaming company with player stats), showcasing how these open-source technologies handle data ingestion, processing, and querying at scale. Attendees will leave with a clear understanding of each tool’s role, practical implementation tips, and the ability to architect similar systems for their own applications. Whether you’re a data engineer, analyst, or developer, this session will empower you to harness the full potential of real-time data ecosystems.

 **Apache Kafka** is a distributed event streaming platform designed for high-throughput, fault-tolerant, and scalable data ingestion and storage. It acts as a central nervous system for real-time data pipelines, enabling producers to publish events to topics and consumers to subscribe and process them. Kafka’s key strengths include its durable commit log, which ensures data persistence, and its ability to handle millions of events per second with low latency. In this workshop, Kafka will serve as the ingestion layer, streaming raw data (e.g., user actions or sensor readings) to downstream systems like Flink and Pinot, providing a reliable foundation for real-time processing and analytics.

**Apache Flink** is an open-source stream processing framework renowned for its ability to perform stateful computations over both unbounded (streaming) and bounded (batch) data with low latency and exactly-once guarantees. Flink excels at real-time data transformation, aggregation, and enrichment, making it ideal for complex event processing tasks. Its unified architecture and rich APIs (including SQL, DataStream, and Table) offer flexibility for developers and analysts alike. In the demo, Flink will process Kafka streams—filtering, aggregating, or joining data in real time—before feeding the results to Pinot, showcasing its power in turning raw events into meaningful, processed datasets.

**Apache Pinot** is a real-time distributed OLAP (Online Analytical Processing) datastore built for ultra-low-latency analytics on large-scale streaming and batch data. It ingests data directly from Kafka topics, organizes it into columnar segments, and enables sub-second query responses even under high throughput. Pinot’s strengths lie in its ability to handle real-time ingestion, support complex SQL queries, and scale horizontally across clusters. In this workshop, Pinot will act as the analytics layer, consuming processed data from Flink and Kafka to power interactive dashboards or ad-hoc queries, demonstrating its capability to deliver instant insights to end users.

### Build

``` sh
docker-compose build
```
### Start 

```sh
docker-compose up -d
```
### Create Kafka Topics

``` sh
docker exec kafka kafka-topics.sh \
		--bootstrap-server localhost:9092 \
		--create \
		--topic games

docker exec kafka kafka-topics.sh \
		--bootstrap-server localhost:9092 \
		--create \
		--topic players

docker exec kafka kafka-topics.sh \
		--bootstrap-server localhost:9092 \
		--create \
		--topic player_scores

docker exec kafka kafka-topics.sh \
		--bootstrap-server localhost:9092 \
		--create \
		--topic player_scores_enhanced
```

### Create Tables in Pinot

``` sh
docker exec pinot-controller ./bin/pinot-admin.sh \
		AddTable \
		-tableConfigFile /tmp/pinot/config/games.table.json \
		-schemaFile /tmp/pinot/config/games.schema.json \
		-exec

docker exec pinot-controller ./bin/pinot-admin.sh \
		AddTable \
		-tableConfigFile /tmp/pinot/config/players.table.json \
		-schemaFile /tmp/pinot/config/players.schema.json \
		-exec

docker exec pinot-controller ./bin/pinot-admin.sh \
		AddTable \
		-tableConfigFile /tmp/pinot/config/playerscores.table.json \
		-schemaFile /tmp/pinot/config/playerscores.schema.json \
		-exec

docker exec pinot-controller ./bin/pinot-admin.sh \
		AddTable \
		-tableConfigFile /tmp/pinot/config/playerscoresenhanced.table.json \
		-schemaFile /tmp/pinot/config/playerscoresenhanced.schema.json \
		-exec
```

### Flink

### Validate

## Tear Down

``` sh
docker exec kafka kafka-topics.sh \
		--bootstrap-server localhost:9092 \
		--create \
		--topic games

docker exec kafka kafka-topics.sh \
		--bootstrap-server localhost:9092 \
		--create \
		--topic players

docker exec kafka kafka-topics.sh \
		--bootstrap-server localhost:9092 \
		--create \
		--topic player_scores

docker exec kafka kafka-topics.sh \
		--bootstrap-server localhost:9092 \
		--create \
		--topic player_score_enhanced
```