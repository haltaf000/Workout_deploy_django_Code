#!/usr/bin/env bash
set -o errexit

# Create persistent SQLite directory
mkdir -p /var/lib/sqlite
chmod 777 /var/lib/sqlite

# Regular build commands
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# Superuser creation
if [[ $CREATE_SUPERUSER == "true" ]]; then
    python manage.py createsuperuser --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').set_password('$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell
fi