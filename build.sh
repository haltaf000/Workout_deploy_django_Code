#!/usr/bin/env bash
set -o errexit

echo "=== Starting Build Process ==="
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate



echo "=== Build Complete ==="