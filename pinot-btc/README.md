# Pinot Bitcoin Portfolio  

This repository contains a sample application that streams the Bitcoin ticker information into Apache Pinot. It is a companion 
repository to the blog series that introduces the reader to the basics of Apache Pinot.

## Running the Code  

Run the following Docker command to bring up the containers.  

```shell
docker compose up -d
```

Next, run the init script to create the schemas and tables in Pinot.  

```shell
./init-pinot.sh
```

You can then navigate to the Pinot query console on http://localhost:9000 to view the Pinot UI and query the data.

Next, run the init script to initialize Superset

```shell
./init-supreset.sh
```

You can then navigate to http://localhost:8088 to view the Superset UI.