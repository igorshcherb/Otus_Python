#!/usr/bin/env bash


set -e  # если упадет, то остановится

echo "Apply migrations..."
alembic upgrade head
echo "Done migrations!"

exec "$@"
