# Create Apache Pinot cluster using Docker Compose

This folder contains the code for creating a Apache Pinot Cluster.

## The contents

The contents of this cluster include:

- Zookeeper
- Controller
- Broker
- Server

## Run the compose file

``` bash
docker-compose -f docker-compose.yml up
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Validate deployment

Make sure:

- 1 Controller is running
- 1 Broker is running
- 1 Server is running

Navigate to the ZooKeeper Tab to look at some configurations.

## Success

There! You've just stood up a Apache Pinot Cluster!