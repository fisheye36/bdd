.DEFAULT_GOAL := help

all: build run  ## Build and run the container in one go

prepare-env-file:  ## Prepare local .env file with secrets based on the template
	@bin/prepare-env-file.sh

build: prepare-env-file  ## Build the container
	docker build -t bdd .

run:  ## Run the container, providing new OTP beforehand
	@bin/update-otp.sh
	docker run -t -v "$$PWD/bdd/.env:/app/.env" bdd

enter:  ## Enter the container, directly into /app directory
	docker run -it -v "$$PWD/bdd/.env:/app/.env" bdd /bin/bash

status:  ## Show status of running containers
	docker ps

clean-docker:  ## Clean all Docker resources, cached images, etc.
	docker system prune --all --volumes

help:  ## See this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: help
