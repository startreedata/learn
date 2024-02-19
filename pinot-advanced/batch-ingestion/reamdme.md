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

In this sections, we will use CLI to ingest data.

- Using docker desktop or docker command, join the pinot-controller shell.
- Run the following command:

``` bash
/opt/pinot/bin/pinot-admin.sh LaunchDataIngestionJob -jobSpecFile /scripts/job-spec-json.yaml
```

## Validate deployment

Make sure:

- the movies table is pupulated following each ingestion

## Success

There! You've just ingested batch data using API, UI & CLI into Pinot!
