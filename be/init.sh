#!/bin/bash
set -e  

export APP_PORT="$APP_PORT"
echo "APP PORT: ${APP_PORT}"

uvicorn app.main:app --host 0.0.0.0 --port ${APP_PORT}