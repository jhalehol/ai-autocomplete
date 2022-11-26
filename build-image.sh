# /usr/local/bin/bash

IMAGE_NAME="autocomplete"
TAG="latest"

docker build -t "${IMAGE_NAME}:${TAG}" .
