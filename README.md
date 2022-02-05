# Aiven Kafka Quickstart Producer with Python and Json

## Description

In this project, we will showcase how to leverage Aiven's Kafka managed services in order to produce and consume weather data in Json format, by having a full integartion suite from source (Weather Web APIs or local data sets) to sink (Time series database in InfluxDB or any other type of consumer), as well as visualisation and dashboard options with Graphana.

The documnet is intended to be simple in order to help people who are fresh starters with Kafka and Aiven to quickly get a hold on a working real-life example.

### What is Kafka?

[Source: wikipedia]
Apache Kafka is a framework implementation of a software bus using stream-processing. It is an open-source software platform developed by the Apache Software Foundation written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.

### How It Works?

[Source: wikipedia]
Kafka stores key-value messages that come from arbitrarily many processes called producers. The data can be partitioned into different "partitions" within different "topics". Within a partition, messages are strictly ordered by their offsets (the position of a message within a partition), and indexed and stored together with a timestamp. Other processes called "consumers" can read messages from partitions.

<p align="center">
<img src="images/kafka1.png" width="66%">
</p>

### What is Aiven Kafka?

[Source: aiven.io]
Aiven for Apache Kafka® is a fully managed streaming platform, deployable in the cloud of your choice. Snap it into your existing workflows with the click of a button, automate away the mundane tasks, and focus on building your core apps.

## Prerequisites

### Python

Install Python on local machine. Install kafka-python and other dependencies using pip. Example:

```bash
pip3 install kafka-python
```

### Kafka & Zookeper (optional)

For quick testing and troubleshooting purposes, it may be useful to install Kafka on the local machine. We will not go into the details of this process.

start kafka and zookeper on standart ports, Start by creating a new topic, example:

```bash
kafka-topics --bootstrap-server localhost:9092 --topic my_first_topic --create --partitions 3 --replication-factor 1
```

Example of listening to new incoming messages:

```bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic my_first_topic
```
