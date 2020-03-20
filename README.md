# Kafka Tutorial 


## What is Kafka?

- Open Source Stream Processing Software Platform
- Handles real time data feeds
- Essentially a big commit log where data is stored in sequence as it happens. 
- Core Concepts:
  - Topics: Stream of records, can be subdivided into partitions and each record can be assigned an offset. 
  - Producers: Logs data into the Kafka System. 
  - Consumers: Gets subscribed to a topic and consumes the data from there
  - Broker: An instance of the Kafka system that is responsible for the message exchange. A kafka cluster is a set of brokers.
  - Zookeeper: Synchronization service and manages all brokers 

## Create a Simple Notification Service using Kafka

This exploratory notebook creates two Kafka producers and Kafka Consumers each on a single Broker.

Step1: The parser fetches raw markups for individual recipes from the following URL ['https://www.allrecipes.com/recipes/96/salad/'].

Step2: `Producer1` then logs these raw markups in the `raw_recipes` topic

Step3: `Consumer1` feeds on the said topic and processes them to create nice json-like objects out of the recipe markups.

Step4: `Producer2` then logs these processed JSON objects in the `parsed_recipes` topic

Step5: `Consumer2` then feeds on the said topic and creates an alert whenever a salad is above a certain calorie count.
