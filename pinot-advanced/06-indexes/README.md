# Create Pinot Indexes

This folder contains the code for creating an Apache Pinot indexes.

## The Exercises

The exercise includes:

- Add Inverted Index
- Add Bloom Filters
- Add Json Index
- more...

## Run the docker compose file

```bash
docker-compose up
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Exercise 0 - Create Schema, control table, load data

We will use the same schema to create different tables to compare performance

- We will use CLI to create schema & tables, and populate the data
- Using either Docker desktop or docker, log into the pinot controller
- run the following script to create schema and table:

```bash
/opt/pinot/bin/pinot-admin.sh AddTable -schemaFile /scripts/gitHub_events_schema.json -tableConfigFile /scripts/gitHub_events_offline_table_config.json -exec 
```

- Next, we will populate some data in the tables
- Run the following script to ingest data from rawdata

```bash
gunzip /scripts/rawdata/*.json.gz
/opt/pinot/bin/pinot-admin.sh LaunchDataIngestionJob -jobSpecFile /scripts/job-spec.yaml
```

- Use the UI to validate that the table was created and data was added.

## Exercise 1 - Inverted Index

We will be using the API to create these tables with indexes.

- Navigate to the following URL to access the API: [http://localhost:9000/#/help](http://localhost:9000/#/help)
- add stuff
- Navigate to the Tables by going here: [http://localhost:9000/#/tables](http://localhost:9000/#/tables)

## Validate deployment

Make sure:

- Three Schemas are created
- Three Tables are created

## Success

There! You've just created three tables!
