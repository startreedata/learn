# Create Pinot Schema and Table

This folder contains the code for creating an Apache Pinot Cluster and adding schema and tables.

## The Exercises

The exercise includes:

- Add schema and table using API
- Add schema and table using CLI
- Add schema and table using UI
- Add real-time and offline tables

## Run the docker compose file

``` bash
docker-compose up -d
```

## Launching the UI

Once that's run, you can navigate the Pinot UI - [http://localhost:9000](http://localhost:9000)

## Exercise 1 - API

In this exercise, we will create a schema and an offline table using API.

- Navigate to the Swagger APIs located at [http://localhost:9000/help](http://localhost:9000/help)
- Find the "Schema" section in the APIs.  
- Find the POST - create schema, and click the button "Try It Out"
- Paste the following code and hit Enter:

``` json
{
    "metricFieldSpecs": [
    ],
    "dimensionFieldSpecs": [
      {
        "dataType": "INT",
        "name": "ActualElapsedTime"
      },
      {
        "dataType": "INT",
        "name": "AirTime"
      },
      {
        "dataType": "INT",
        "name": "AirlineID"
      },
      {
        "dataType": "INT",
        "name": "ArrDel15"
      },
      {
        "dataType": "INT",
        "name": "ArrDelay"
      },
      {
        "dataType": "INT",
        "name": "ArrDelayMinutes"
      },
      {
        "dataType": "INT",
        "name": "ArrTime"
      },
      {
        "dataType": "STRING",
        "name": "ArrTimeBlk"
      },
      {
        "dataType": "INT",
        "name": "ArrivalDelayGroups"
      },
      {
        "dataType": "INT",
        "name": "CRSArrTime"
      },
      {
        "dataType": "INT",
        "name": "CRSDepTime"
      },
      {
        "dataType": "INT",
        "name": "CRSElapsedTime"
      },
      {
        "dataType": "STRING",
        "name": "CancellationCode"
      },
      {
        "dataType": "INT",
        "name": "Cancelled"
      },
      {
        "dataType": "STRING",
        "name": "Carrier"
      },
      {
        "dataType": "INT",
        "name": "CarrierDelay"
      },
      {
        "dataType": "INT",
        "name": "DayOfWeek"
      },
      {
        "dataType": "INT",
        "name": "DayofMonth"
      },
      {
        "dataType": "INT",
        "name": "DepDel15"
      },
      {
        "dataType": "INT",
        "name": "DepDelay"
      },
      {
        "dataType": "INT",
        "name": "DepDelayMinutes"
      },
      {
        "dataType": "INT",
        "name": "DepTime"
      },
      {
        "dataType": "STRING",
        "name": "DepTimeBlk"
      },
      {
        "dataType": "INT",
        "name": "DepartureDelayGroups"
      },
      {
        "dataType": "STRING",
        "name": "Dest"
      },
      {
        "dataType": "INT",
        "name": "DestAirportID"
      },
      {
        "dataType": "INT",
        "name": "DestAirportSeqID"
      },
      {
        "dataType": "INT",
        "name": "DestCityMarketID"
      },
      {
        "dataType": "STRING",
        "name": "DestCityName"
      },
      {
        "dataType": "STRING",
        "name": "DestState"
      },
      {
        "dataType": "INT",
        "name": "DestStateFips"
      },
      {
        "dataType": "STRING",
        "name": "DestStateName"
      },
      {
        "dataType": "INT",
        "name": "DestWac"
      },
      {
        "dataType": "INT",
        "name": "Distance"
      },
      {
        "dataType": "INT",
        "name": "DistanceGroup"
      },
      {
        "dataType": "INT",
        "name": "DivActualElapsedTime"
      },
      {
        "dataType": "INT",
        "name": "DivAirportIDs",
        "singleValueField": false
      },
      {
        "dataType": "INT",
        "name": "DivAirportLandings"
      },
      {
        "dataType": "INT",
        "name": "DivAirportSeqIDs",
        "singleValueField": false
      },
      {
        "dataType": "STRING",
        "name": "DivAirports",
        "singleValueField": false
      },
      {
        "dataType": "INT",
        "name": "DivArrDelay"
      },
      {
        "dataType": "INT",
        "name": "DivDistance"
      },
      {
        "dataType": "INT",
        "name": "DivLongestGTimes",
        "singleValueField": false
      },
      {
        "dataType": "INT",
        "name": "DivReachedDest"
      },
      {
        "dataType": "STRING",
        "name": "DivTailNums",
        "singleValueField": false
      },
      {
        "dataType": "INT",
        "name": "DivTotalGTimes",
        "singleValueField": false
      },
      {
        "dataType": "INT",
        "name": "DivWheelsOffs",
        "singleValueField": false
      },
      {
        "dataType": "INT",
        "name": "DivWheelsOns",
        "singleValueField": false
      },
      {
        "dataType": "INT",
        "name": "Diverted"
      },
      {
        "dataType": "INT",
        "name": "FirstDepTime"
      },
      {
        "dataType": "STRING",
        "name": "FlightDate"
      },
      {
        "dataType": "INT",
        "name": "FlightNum"
      },
      {
        "dataType": "INT",
        "name": "Flights"
      },
      {
        "dataType": "INT",
        "name": "LateAircraftDelay"
      },
      {
        "dataType": "INT",
        "name": "LongestAddGTime"
      },
      {
        "dataType": "INT",
        "name": "Month"
      },
      {
        "dataType": "INT",
        "name": "NASDelay"
      },
      {
        "dataType": "STRING",
        "name": "Origin"
      },
      {
        "dataType": "INT",
        "name": "OriginAirportID"
      },
      {
        "dataType": "INT",
        "name": "OriginAirportSeqID"
      },
      {
        "dataType": "INT",
        "name": "OriginCityMarketID"
      },
      {
        "dataType": "STRING",
        "name": "OriginCityName"
      },
      {
        "dataType": "STRING",
        "name": "OriginState"
      },
      {
        "dataType": "INT",
        "name": "OriginStateFips"
      },
      {
        "dataType": "STRING",
        "name": "OriginStateName"
      },
      {
        "dataType": "INT",
        "name": "OriginWac"
      },
      {
        "dataType": "INT",
        "name": "Quarter"
      },
      {
        "dataType": "STRING",
        "name": "RandomAirports",
        "singleValueField": false
      },
      {
        "dataType": "INT",
        "name": "SecurityDelay"
      },
      {
        "dataType": "STRING",
        "name": "TailNum"
      },
      {
        "dataType": "INT",
        "name": "TaxiIn"
      },
      {
        "dataType": "INT",
        "name": "TaxiOut"
      },
      {
        "dataType": "INT",
        "name": "Year"
      },
      {
        "dataType": "INT",
        "name": "WheelsOn"
      },
      {
        "dataType": "INT",
        "name": "WheelsOff"
      },
      {
        "dataType": "INT",
        "name": "WeatherDelay"
      },
      {
        "dataType": "STRING",
        "name": "UniqueCarrier"
      },
      {
        "dataType": "INT",
        "name": "TotalAddGTime"
      }
    ],
    "dateTimeFieldSpecs": [
      {
        "name": "DaysSinceEpoch",
        "dataType": "INT",
        "format": "1:DAYS:EPOCH",
        "granularity": "1:DAYS"
      },
      {
        "name": "ts",
        "dataType": "TIMESTAMP",
        "format": "1:MILLISECONDS:TIMESTAMP",
        "granularity": "1:SECONDS"
      },
      {
        "name": "tsRaw",
        "dataType": "TIMESTAMP",
        "format": "1:MILLISECONDS:TIMESTAMP",
        "granularity": "1:SECONDS"
      }
    ],
    "schemaName": "airlineStats"
  }
  
```

- You can validate that the schema got created by checking the UI.
- Navigate to the Swagger APIs located at [http://localhost:9000/help](http://localhost:9000/help)
- Find the "Table" section in the APIs.  
- Find the POST - create table, and click the button "Try It Out"
- Paste the following code and hit Enter:

``` json
{
    "tableName": "airlineStats",
    "tableType": "OFFLINE",
    "segmentsConfig": {
      "timeColumnName": "DaysSinceEpoch",
      "timeType": "DAYS",
      "segmentPushType": "APPEND",
      "segmentAssignmentStrategy": "BalanceNumSegmentAssignmentStrategy",
      "replication": "1"
    },
    "tenants": {},
    "fieldConfigList": [
      {
        "name": "ts",
        "encodingType": "DICTIONARY",
        "indexTypes": [
          "TIMESTAMP"
        ],
        "timestampConfig": {
          "granularities": [
            "DAY",
            "WEEK",
            "MONTH"
          ]
        }
      },
      {
        "name": "ArrTimeBlk",
        "encodingType": "DICTIONARY",
        "indexes": {
          "inverted": {
            "enabled": "true"
          }
        },
        "tierOverwrites": {
          "hotTier": {
            "encodingType": "DICTIONARY",
            "indexes": {
              "bloom": {
                "enabled": "true"
              }
            }
          },
          "coldTier": {
            "encodingType": "RAW",
            "indexes": {
              "text": {
                "enabled": "true"
              }
            }
          }
        }
      }
    ],
    "tableIndexConfig": {
      "starTreeIndexConfigs": [
        {
          "dimensionsSplitOrder": [
            "AirlineID",
            "Origin",
            "Dest"
          ],
          "skipStarNodeCreationForDimensions": [],
          "functionColumnPairs": [
            "COUNT__*",
            "MAX__ArrDelay"
          ],
          "maxLeafRecords": 10
        }
      ],
      "enableDynamicStarTreeCreation": true,
      "loadMode": "MMAP",
      "tierOverwrites": {
        "hotTier": {
          "starTreeIndexConfigs": [
            {
              "dimensionsSplitOrder": [
                "Carrier",
                "CancellationCode",
                "Origin",
                "Dest"
              ],
              "skipStarNodeCreationForDimensions": [],
              "functionColumnPairs": [
                "MAX__CarrierDelay",
                "AVG__CarrierDelay"
              ],
              "maxLeafRecords": 10
            }
          ]
        },
        "coldTier": {
          "starTreeIndexConfigs": []
        }
      }
    },
    "metadata": {
      "customConfigs": {}
    },
    "ingestionConfig": {
      "transformConfigs": [
        {
          "columnName": "ts",
          "transformFunction": "fromEpochDays(DaysSinceEpoch)"
        },
        {
          "columnName": "tsRaw",
          "transformFunction": "fromEpochDays(DaysSinceEpoch)"
        }
      ]
    },
    "tierConfigs": [
      {
        "name": "hotTier",
        "segmentSelectorType": "time",
        "segmentAge": "3130d",
        "storageType": "pinot_server",
        "serverTag": "DefaultTenant_OFFLINE"
      },
      {
        "name": "coldTier",
        "segmentSelectorType": "time",
        "segmentAge": "3140d",
        "storageType": "pinot_server",
        "serverTag": "DefaultTenant_OFFLINE"
      }
    ]
  }
```

- Validate that the table got creat by checking the UI under Tables.

## Exercise 2 - CLI

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

## Exercise 3 - UI

In this exercise, we will create a schema and table using the Pinot UI.

- Navigate to the Tables by going here: [http://localhost:9000/#/tables](http://localhost:9000/#/tables)
- Select the Add Schema button
- Use the UI to create a schema using the following name & fields:
- Schema Name: fineFoodReviews
- ProductId: Dimension, STRING
- UserId: Dimension,STRING
- Score: Dimension,INT
- Summary: Dimension,STRING
- Text: Dimension,STRING
- n_tokens: Dimension,INT
- embedding: Dimension,FLOAT (`multivalueField` true)
- select SAVE

Next, we will create the offline table.

- Select the Add Offline Table button
- In our case, we will accept defaults for all other fields
- Select SAVE

## Validate deployment

Make sure:

- Three Schemas are created
- Three Tables are created

## Teardown

To tear down the cluster, run the docker compose down command as

```bash
docker-compose down
```

## Success

There! You've just created three tables in a Pinot Cluster!
