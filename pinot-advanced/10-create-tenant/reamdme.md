# Create Tenants

This folder contains the excercise to create tenants in a Apache Pinot cluster.

## The contents

The contents of this cluster include:

- Zookeeper
- Controller
- Broker x 2
- Server x 2

## Run the compose file

``` bash
docker-compose -f docker-compose.yml up
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Validate deployment

Make sure:

- 1 Controller is running
- 2 Brokers are running
- 2 Servers are running

## Remove DefaultTenant

In order to create a tenant, Brokers and servers need to be created without a Tag.  One quick way we can accomplish this is by using the ZooKeeper.

- Navigate to the Pinot UI and make sure that DefaultTenat has 2 servers and 2 brokers.
- Navigate to ZooKeeper -> PinotCluster -> CONFIGS -> PARTICIPANTS
- Find one of the brokers, and remove the tag from the TAG_LIST "DefaultTenant_BROKER".
- Check the main Pinot UI page to confirm that DefaultTenant only shows 1 Broker.
- Navigate to ZooKeeper -> PinotCluster -> CONFIGS -> PARTICIPANTS
- Find one of the servers, and remove the tag from TAG_LIST "DefaultTenant_OFFLINE" & "DefaultTenant_REALTIME"
- Check the main Pinot UI page to confirm that DefaultTenant only shows 1 server.

## Crete Tenants using API

Let's create tenants using the API.

- Navigate to the Swagger APIs located at [http://localhost:9000/help](http://localhost:9000/help)
- Find the section Tenant, find the POST - create tenant, and click the button "Try It Out"
- post the following jason code:

``` json

{
     "tenantRole" : "BROKER",
     "tenantName" : "BrokerTenant",
     "numberOfInstances" : 1
}

```

- Make sure the result was a success
- repeat the command with the following code:

``` json
{
     "tenantRole" : "SERVER",
     "tenantName" : "ServerTenant",
     "offlineInstances" : 1,
     "realtimeInstances" : 1
}

```

## Validate Tenant Creation

Navigate to the Pinot UI main page, and validate that the new Tenant is created

## Create Tenats using CLI

Before we begin, repeat the steps to ensure that atleast one broker and one server do not have any tags.

To create a tenant for Server, run the following on the controller container:

``` bash
bin/pinot-admin.sh AddTenant \
    -name ServerTenant \
    -role SERVER \
    -instanceCount 0,
    -offlineInstanceCount 1 \
    -realtimeInstanceCount 1 -exec

```

To create a tenant for Broker, run the following on the controller container:

``` bash
bin/pinot-admin.sh AddTenant \
    -name BrokerTenant \
    -role BROKER \
    -instanceCount 1,
    -offlineInstanceCount 0 \
    -realtimeInstanceCount 0 -exec

```

## Teardwon

To tear down the cluster, run the docker compose down command as

``` bash
docker-compose down
```

## Success

There! You've just created some Apache Pinot Tenants!
