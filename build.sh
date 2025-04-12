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
    python manage.py createsuperuser --noinput \
        --email $DJANGO_SUPERUSER_EMAIL \
        --username $DJANGO_SUPERUSER_USERNAME
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').set_password('$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell
fi

echo "=== Build Complete ==="