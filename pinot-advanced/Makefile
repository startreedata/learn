# Define the list of directories
DIRS := 01-create-cluster 03-batch-ingestion 05-queries 07-transform 09-minion 02-add-table 04-stream-ingestion 06-indexes 08-upserts 10-create-tenant

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
pull_images:
	@for dir in $(DIRS); do \
		echo "Pulling Docker images in \033[1m$$dir\033[0m..."; \
		(cd $$dir && docker compose pull); \
		echo "Completed pulling images in \033[1m$$dir\033[0m."; \
	done

.PHONY: all pull_images stop_containers 