#!/bin/bash

source .env

echo "running ${LOCAL_REPO}/${IMAGE_NAME}:latest"

# docker run --env-file .env \
#     -p "$HOST_PORT":"$APP_PORT" \
#     -e PYTHONUNBUFFERED=1 \
#     ${LOCAL_REPO}/${IMAGE_NAME}:latest

docker run --rm --env-file .env \
    -p "$HOST_PORT":"$APP_PORT" \
    -e API_NAME="$API_NAME" \
    -e API_VERSION="$API_VERSION" \
    -e API_KEY="$API_KEY" \
    -e AI_API_KEY="$AI_API_KEY" \
    -e AI_API_ENDPOINT="$AI_API_ENDPOINT" \
    -e MAX_GENERATED_SUM="$MAX_GENERATED_SUM" \
    -e SYSTEM_PROMPT="$SYSTEM_PROMPT" \
    -e ALLOWED_ORIGINS="$ALLOWED_ORIGINS" \
    -e ALLOWED_CREDENTIALS="$ALLOWED_CREDENTIALS" \
    -e ALLOWED_METHODS="$ALLOWED_METHODS" \
    -e ALLOWED_HEADERS="$ALLOWED_HEADERS" \
    -e MAX_LEN_SCRAPER="$MAX_LEN_SCRAPER" \
    -e HOST_PORT="$HOST_PORT" \
    -e APP_PORT="$APP_PORT" \
    -e PYTHONUNBUFFERED=1 \
    ${LOCAL_REPO}/${IMAGE_NAME}:latest