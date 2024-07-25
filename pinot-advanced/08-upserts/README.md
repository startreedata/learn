# Create Pinot Schema and Table

This folder contains the code for Upserts in Apache Pinot.

## The Exercises

The exercise includes:

- Full Upsert
- Partial Upsert

## Run the docker compose file

```bash
docker-compose up
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Excercise 1 - Full Upsert

In this exercise, we will create a table that suppots full Upserts.

You should see the following files:

- gitHub_events_offline_table_config.json
- gitHub_events_schema.json

Use the following command to create the table

```bash
/opt/pinot/bin/pinot-admin.sh AddTable -schemaFile /scripts/orders_schema.json -tableConfigFile /scripts/orders_full_upserts.json -exec 
```

At this point, you should be able to verify that the Table and schema were created by navigating to <http://localhost:9000> and selecting tables.

Next, let's consume some messages:

```bash
docker exec -it kafka kafka-console-producer.sh --bootstrap-server localhost:9092 --topic orders
```

and paste the following:

```jsonl
{"order_id":1,"customer_id":104,"order_status":"IN_TRANSIT","amount":29.35,"ts":"1632467063"}
{"order_id":2,"customer_id":105,"order_status":"COMPLETED","amount":3.24,"ts":"1618931459"}
{"order_id":3,"customer_id":103,"order_status":"OPEN","amount":9.77,"ts":"1626484196"}
{"order_id":4,"customer_id":104,"order_status":"COMPLETED","amount":90.35,"ts":"1623066325"}
{"order_id":5,"customer_id":105,"order_status":"OPEN","amount":55.52,"ts":"1635543905"}
```

Next, from a query UI [http://localhost:9000/#/query](http://localhost:9000/#/query)
query:

```SQL
select * 
from orders 
limit 10
```

Next, let's try the usert, navigate to the Kafka tab and paste the following:

```json
{"order_id":5,"customer_id":105,"order_status":"CANCELLED","amount":55.52,"ts":"1635543948"}
```

Validate that the record was replaced by re-running the previous query.

## Validate deployment

Make sure:

- Three Schemas are created
- Three Tables are created

## Success

You've just created upserts in Apache Pinot!
