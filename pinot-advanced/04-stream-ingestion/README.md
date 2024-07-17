# Ingest Streaming Data into Apache Pinot

This folder contains the exercises for ingesting streaming data into Apache Pinot Tables.

## The Exercise

The exercises include:

- Ingest using Kafka

### Ingest using Kafka

Notice that in the docker compose file deploys Kafka.
We will use a node application to ingest wikipedia events and send them to kafka.

### Generate data

For this, we need to run a node app to consume data and write to Kafaka
First, we will build the node app:

``` sh
docker build -t pinot-advanced/nodejs-streaming-ingest ./node-app

```

## Run the docker compose file

``` sh
docker-compose up -d
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

- It takes a few minutes for Pinot to start
- Make sure that the wikievents table is created by navigating to  [http://localhost:9000/#/query](http://localhost:9000/#/query)

## Start Consumer

``` sh
docker start pinot-node-consumer
```

## Stop Consumer

``` sh
docker stop pinot-node-consumer
```

## Validate deployment

- the wikipedia events table is pupulated by navigating to: [http://localhost:9000/#/query?query=select+*+from+wikievents+limit+10&tracing=false&useMSE=false](http://localhost:9000/#/query?query=select+*+from+wikievents+limit+10&tracing=false&useMSE=false)

## Teardown

``` sh
docker-compose down
```

## Success

There!
You've just ingested batch data using API, UI & CLI into Pinot!
