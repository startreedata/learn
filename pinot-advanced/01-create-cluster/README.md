# Create Apache Pinot cluster using Docker Compose

This folder contains the code for creating an Apache Pinot Cluster.

## The contents

The contents of this cluster include:

- Zookeeper
- Controller
- Broker
- Server

## Run the docker compose file

```bash
docker-compose up -d
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Validate deployment

Make sure:

- One Controller is running
- One Broker is running
- One Server is running

Navigate to the ZooKeeper Tab to look at some configurations.

## Teardown

To tear down the cluster, run the docker compose down command as

```bash
docker-compose down
```

## Success

There! You've just stood up an Apache Pinot Cluster!
