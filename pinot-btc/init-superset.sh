#!/usr/bin/env bash

docker compose exec -it superset superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin
docker compose exec -it superset superset db upgrade
docker compose exec -it superset superset init