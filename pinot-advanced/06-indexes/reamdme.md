# Create Pinot Indexes

This folder contains the code for creating a Apache Pinot indexes.

## The Execises

The exercise  include:

- Add Inverted Index
- Add Bloom Filters
- Add Json Index
- more...

## Run the compose file

``` bash
docker-compose up -d
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Excercise 0 - Create tables, Load data

### Dynamic Indexes vs. Sorted Indexes

Most indexes in Pinot are dynamic, unless they are configured to be sorted.  

- Next, we will populate some data in the tables
- Run the following script to ingest data from rawdata

``` bash
cd data
wget https://data.gharchive.org/2021-07-21-{6..9}.json.gz
gunzip *.json.gz
/opt/pinot/bin/pinot-admin.sh LaunchDataIngestionJob -jobSpecFile /scripts/job-spec.yaml
```

- Use the UI to validate that the table was created and data was added.

## Excercise 1 - Using Bloom Filter

Bloom filters help by pruning segments for equity clause.

Let's start with comparing these two queries:

``` SQL
-- without index
SET skipIndexes='commit_author_names=bloomFilter';
select * from github_events where commit_author_names = 'Hoversquid';

-- with index
select * from github_events where commit_author_names = 'Hoversquid'
```

## Excercise 2 - Using Forward Index

Bloom filters help by pruning segments for equity clause.

Let's start with comparing these two queries:

``` SQL
-- without index
SET skipIndexes='commit_author_names=bloomFilter';
select * from github_events where commit_author_names = 'Hoversquid';

-- with index
select * from github_events where commit_author_names = 'Hoversquid'

```



- Refresh Table
- Run Query:

## Validate deployment

Make sure:

- 3 Schemas are created
- 3 Tables are created

## Success

There! You've just created three tables!
