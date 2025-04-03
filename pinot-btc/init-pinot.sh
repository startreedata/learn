#!/usr/bin/env bash

echo "Creating Pinot tables ..."
curl -s -F schemaName=@tables/001-ticker/ticker_schema.json localhost:9000/schemas
curl -s -XPOST -H 'Content-Type: application/json' -d @tables/001-ticker/ticker_table.json localhost:9000/tables
curl -s -F schemaName=@tables/002-portfolio/portfolio_schema.json localhost:9000/schemas
curl -s -XPOST -H 'Content-Type: application/json' -d @tables/002-portfolio/portfolio_table.json localhost:9000/tables

echo "Loading CSV data into Pinot ..."
docker compose exec pinot-controller bin/pinot-admin.sh LaunchDataIngestionJob -jobSpecFile /tmp/files/job_spec.yaml
