# Create Pinot Schema and Table

This folder contains the code for examining transform functions in Apache Pinot.

## The Exercises

The exercise includes:

- Add schema and table using CLI
- Examine Transform functions used
- Use transform funtions in queries

## Run the docker compose file

``` bash
docker-compose up
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Exercise 1 - Deplaoy Table and schema using CLI

In this exercise, we will use the CLI to create a schema and table.

First, using either the Docker Desktop or docker command line, join the pinot-controller shell.

Navigate to the `scripts` folder:

```sh
cd scripts
```

You should see the following files:

- `gitHub_events_offline_table_config.json`
- `gitHub_events_schema.json`

Use the following command to create the table

``` bash
/opt/pinot/bin/pinot-admin.sh AddTable -schemaFile /scripts/gitHub_events_schema.json -tableConfigFile /scripts/gitHub_events_offline_table_config.json -exec 
```

At this point, you should be able to verify that the Table and schema were created by navigating to <http://localhost:9000> and selecting tables.

## Exercise 2 - Examine native transfform funtions

In this exercise, we will createlook at the Json transform funtions used in the ingestion process.

- Navigate to the Tables by going here: [http://localhost:9000/#/tenants/table/github_events_OFFLINE](http://localhost:9000/#/tenants/table/github_events_OFFLINE)
- Look at the table config.  You will notice the folliwing transform funtions:

``` json

"transformConfigs": [
        {
          "columnName": "repo_name",
          "transformFunction": "jsonPathString(repo, '$.name', 'null')"
        },
        {
          "columnName": "repo_name_fst",
          "transformFunction": "jsonPathString(repo, '$.name', 'null')"
        },
        {
          "columnName": "actor_json",
          "transformFunction": "jsonFormat(actor)"
        },
        {
          "columnName": "payload_commits",
          "transformFunction": "jsonPathString(payload, '$.commits', 'null')"
        },
        {
          "columnName": "payload_pull_request",
          "transformFunction": "jsonPathString(payload, '$.pull_request', 'null')"
        },
        {
          "columnName": "commit_author_names",
          "transformFunction": "jsonPathArrayDefaultEmpty(payload, '$.commits[*].author.name')"
        },
        {
          "columnName": "label_ids",
          "transformFunction": "jsonPathArrayDefaultEmpty(payload, '$.pull_request.labels[*].id')"
        }
      ],

```

Notice the use of jsonPathString, jsonFormat and jsonPathArrayDefaultEmpty functions to transform the original json to columns.

## Exercise 3 - Groovy Transform

Navigate to the Table Config here: [http://localhost:9000/#/tenants/table/github_events_OFFLINE](http://localhost:9000/#/tenants/table/github_events_OFFLINE)

- Notice that the Groovy Function is turned on.
- Next, we will use groovy functions i the query. Navigate to the query console: [http://localhost:9000/#/query](http://localhost:9000/#/query)

``` SQL
-- Use groovy function in query
SELECT groovy('{"returnType":"STRING","isSingleValue":true}', 'def x = 0; arg0.eachWithIndex{item, idx -> if (item.startsWith("Y")) { x = item }}; return x', commit_author_names) AS teammate,
       commit_author_names
FROM github_events
WHERE commit_author_names = 'Gun1Yun'
ORDER BY teammate;
```

## Validate deployment

Make sure:

- Three Schemas are created
- Three Tables are created
- Native Transform functions were used
- Groovy Transform Functions were used.

## Success

There!
You've just used Transform functions in Pinot!
