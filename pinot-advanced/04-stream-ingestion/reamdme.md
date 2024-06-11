# Ingest Streaming Data into Apache Pinot

This folder contains the exercises for ingesting streaming data into Apache Pinot Tables.

## The Exercise

The exercises include:

- Ingest using Kafaka

## Run the compose file

``` bash
docker-compose up -d
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

### Ingest using Kafka

Notice that in the docker compose file deploys Kafka.
We will use a node application to ingest wikipedia events and send them to kafka.

### Generate data

For this, we need to run a node app to consume data and write to Kafaka

``` sh

```

- Check the wikievents.js code under scripts folder on how to connect to kafka
- Run the done script wikievents.js
- Check the wikipedia_events_schema.json file to inspect the schema
- check the wikipedia_events_realtime_table_congig.json to inspect the table design
- Navigate to [http://localhost:9000/#/query](http://localhost:9000/#/query) to validate that the table exists
- Run the sample select query to validate data
- Stop the wikievents.js

## Validate deployment

Make sure:

- the wikipedia events table is pupulated

## Teardwon

To tear down the cluster, run the docker compose down command as

``` bash
docker-compose down
```

## Success

There! You've just ingested batch data using API, UI & CLI into Pinot!
