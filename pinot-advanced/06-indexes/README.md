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

## Exercise 0 - Create table, load data

We will use the same schema to create different tables to compare performance

- We will use CLI to create schema & tables, and populate the data
- Using either Docker desktop or docker, log into the pinot controller
- run the following script to create schema and table:

```bash
docker exec -it pinot-controller sh
/opt/pinot/bin/pinot-admin.sh AddTable -schemaFile /scripts/gitHub_events_schema.json -tableConfigFile /scripts/gitHub_events_offline_table_config.json -exec
```

- Next, we will populate some data in the tables
- Run the following script to ingest data from rawdata

```bash
cd data
wget https://data.gharchive.org/2021-07-21-9.json.gz
wget https://data.gharchive.org/2021-07-21-10.json.gz
wget https://data.gharchive.org/2021-07-21-11.json.gz
wget https://data.gharchive.org/2021-07-21-12.json.gz
gunzip *.gz
/opt/pinot/bin/pinot-admin.sh LaunchDataIngestionJob -jobSpecFile /scripts/job-spec.yaml
```

- Use the UI to validate that the table was created and data was added.

## Excercise 1 - Adding Index

To add an index, you can ecdit the Table Config file.

Edit the github_events_offlien_table_config.jason and add a bloom filter to the column 'commit_author_names' in the tableIndexConfig section:

``` json
"bloomFilterColumns": [
      "id",
      "commit_author_names",
      "label_ids"
    ],
```
Note: that you can do this using the UI, or by editing the config directly.

## Excercise 2 - Using Indexes

We can run queries with and without indexes.  In this example, we will se the Bloom Filter. Bloom filters help by pruning segments for equity clause.

Let's start with comparing these two queries:

``` SQL
-- without index
SET skipIndexes='commit_author_names=bloomFilter';
select * from github_events where commit_author_names = 'Hoversquid';

-- with index
select * from github_events where commit_author_names = 'Hoversquid'
```

## Validate deployment

Make sure:

- The Schemas are created
- The Tables are created
- Data is loaded
- You can see the indexes using the UI

## Success

There! You've just created and used Indexes!
