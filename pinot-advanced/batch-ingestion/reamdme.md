# Ingest Batch Data into Apache Pinot

This folder contains the exercises for ingesting batch data into Apache Pinot Tables.

## The Exercise

The exercises include:

- Ingest using UI
- Ingest using API
- Ingest using CLI

## Run the compose file

``` bash
docker-compose -f docker-compose.yml up
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

### Ingest using UI

- Navigate to the Query Consol [http://localhost:9000/#/query](http://localhost:9000/#/query)
- Select movies table
- Enter the following code to import data using UI:

``` sql
SET taskName = 'URL-Read';
SET input.fs.className = 'org.apache.pinot.plugin.filesystem.S3PinotFS';
SET input.fs.prop.region = 'us-east-2';
INSERT INTO "movies"
FROM FILE 's3://bhdemo/movies.csv'

```

- Make sure the recods were ingested.

### Ingest using API



### Ingest using CLI



## Validate deployment

Make sure:

- 1 Controller is running
- 1 Broker is running
- 1 Server is running

Navigate to the ZooKeeper Tab to look at some configurations.

## Success

There! You've just stood up a Apache Pinot Cluster!
