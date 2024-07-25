# Define the list of directories
DIRS := 01-create-cluster 02-add-table 03-batch-ingestion 04-stream-ingestion 05-queries  06-indexes 07-transform 08-upserts 09-minion 10-create-tenant
.ONESHELL:

# Default target
all: pull_images

# Target to stop all containers in each directory
stop_containers:
	@for dir in $(DIRS); do \
		echo "Stopping all containers in \033[1m$$dir\033[0m..."; \
		(cd $$dir && docker compose down -v); \
		echo "All containers in \033[1m$$dir\033[0m have been stopped and volumes removed."; \
	done

# Target to pull images in each directory
pull_images: build
	@for dir in $(DIRS); do \
		echo "Pulling Docker images in \033[1m$$dir\033[0m..."; \
		(cd $$dir && docker compose pull); \
		echo "Completed pulling images in \033[1m$$dir\033[0m."; \
	done

#  Smoke test to run all containers
start_all: 
	@for dir in $(DIRS); do \
		echo "Starting containers in \033[1m$$dir\033[0m..."; \
		(cd $$dir && docker compose up -d); \
		echo "Done with containers in \033[1m$$dir\033[0m."; \
		(cd $$dir && docker compose down -v); \
		echo "All containers in \033[1m$$dir\033[0m have been stopped and volumes removed."; \
	done

DIR4=04-stream-ingestion
build:
	cd $(DIR4) && docker-compose build -q 

.PHONY: all pull_images stop_containers 