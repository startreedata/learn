# Create Tenants

This folder contains the exercise to create tenants in an Apache Pinot cluster.

## The contents

The contents of this cluster include:

- Zookeeper
- Controller
- Broker x 2
- Server x 2

## Run the docker compose file

```bash
docker-compose up
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Validate deployment

Make sure:

- One Controller is running
- Two Brokers are running
- Two Servers are running

## Remove DefaultTenant

To create a tenant, Brokers and servers need to be created without a Tag.  
One quick way we can complete this is by using the ZooKeeper.

- Navigate to the Pinot UI and make sure that `DefaultTenat` has two servers and two brokers.
- Navigate to `ZooKeeper` -> `PinotCluster` -> `CONFIGS` -> `PARTICIPANTS`
- Find one of the brokers, and remove the tag from the TAG_LIST `DefaultTenant_BROKER`.
- Check the main Pinot UI page to confirm that `DefaultTenant` only shows one Broker.
- Navigate to `ZooKeeper` -> `PinotCluster` -> `CONFIGS` -> `PARTICIPANTS`
- Find one of the servers, and remove the tag from TAG_LIST `DefaultTenant_OFFLINE` and `DefaultTenant_REALTIME`
- Check the main Pinot UI page to confirm that DefaultTenant only shows one server.

## Create Tenants using API

Let's create tenants using the API.

- Navigate to the Swagger APIs located at [http://localhost:9000/help](http://localhost:9000/help)
- Find the section Tenant, find the POST - create tenant, and click the button "Try It Out"
- post the following jason code:

```json
{
     "tenantRole" : "BROKER",
     "tenantName" : "BrokerTenant",
     "numberOfInstances" : 1
}
```

- Make sure the result was a success
- repeat the command with the following code:

```json
{
     "tenantRole" : "SERVER",
     "tenantName" : "ServerTenant",
     "offlineInstances" : 1,
     "realtimeInstances" : 1
}
```

## Validate Tenant Creation

Navigate to the Pinot UI main page, and validate that the new Tenant is created

## Create Tenants using CLI

Before we begin, repeat the steps to ensure that at least one broker and one server do not have any tags.

To create a tenant for Server, run the following on the controller container:

```bash
bin/pinot-admin.sh AddTenant \
    -name ServerTenant \
    -role SERVER \
    -instanceCount 0,
    -offlineInstanceCount 1 \
    -realtimeInstanceCount 1 -exec
```

To create a tenant for Broker, run the following on the controller container:

```bash
bin/pinot-admin.sh AddTenant \
    -name BrokerTenant \
    -role BROKER \
    -instanceCount 1,
    -offlineInstanceCount 0 \
    -realtimeInstanceCount 0 -exec
```

## Success

There! 
You've just created some Apache Pinot Tenants!
