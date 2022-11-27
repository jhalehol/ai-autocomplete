# /usr/local/bin/bash


./run-tests-with-coverage.sh

IMAGE_NAME="autocomplete"
TAG="latest"

docker build -t "${IMAGE_NAME}:${TAG}" .
