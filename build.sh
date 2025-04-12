#!/usr/bin/env bash
set -o errexit

echo "=== Starting Build Process ==="
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate

if [[ $CREATE_SUPERUSER == "true" ]]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput \
        --email "${DJANGO_SUPERUSER_EMAIL:-admin@example.com}" \
        --username "${DJANGO_SUPERUSER_USERNAME:-admin}"
    echo "Superuser created!"
fi

echo "=== Build Complete ==="