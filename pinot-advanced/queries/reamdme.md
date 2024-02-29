# Run  Pinot Queries

This folder contains the code for creating a Apache Pinot Tables, and run some queries.

## The Execises

The exercise  include:

- Create Schema
- Create Table
- Ingest Data
- Run Queries

## Run the compose file

``` bash
docker-compose -f docker-compose.yml up
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Excercise 1 - Create Schema, control table, load data

We will use the same schema to create different tables to compare performance

- We will use CLI to create schema & tables, and populate the data
- Using either Docker desktop or docker, log into the pinot controller
- run the following script to create schema and table:

``` bash
/opt/pinot/bin/pinot-admin.sh AddTable -schemaFile /scripts/gitHub_events_schema.json -tableConfigFile /scripts/gitHub_events_offline_table_config.json -exec
```

- Next, we will populate some data in the tables
- Run the following script to ingest data from rawdata

``` bash
/opt/pinot/bin/pinot-admin.sh LaunchDataIngestionJob -jobSpecFile /scripts/job-spec.yaml
```

- Use the UI to validate that the table was created and data was added.

## Excercise 2 - Run Queries

We will be using the API to create these tableswith indexes.

- Navigate to the follwing URL to access the Query Consol: [http://localhost:9000/#/query](http://localhost:9000/#/query)
- Run the following queries:

``` SQL
SELECT * FROM github_events 
SELECT * FROM github_events LIMIT 100
SELECT COUNT(*) FROM github_events 
SELECT MAX(created_at) FROM github_events 
SELECT SUM(label_ids) FROM github_events 
SELECT MIN(label_ids), MAX(label_ids), SUM(label_ids), AVG(label_ids), commit_author_names FROM github_events GROUP BY commit_author_names ORDER BY commit_author_names, MAX(label_ids) DESC 
LIMIT 50

```

- Navigate to the Tables are by going here: [http://localhost:9000/#/tables](http://localhost:9000/#/tables)

## Validate deployment

Make sure:

- All Queries run and are performant

## Success

There! You've just created three tables!
