#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# Create superuser if enabled
if [[ $CREATE_SUPERUSER == "true" ]]; then
    echo "Creating superuser..."

    # First create without password to avoid interactive prompt
    python manage.py createsuperuser \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --email "$DJANGO_SUPERUSER_EMAIL" \
        --noinput || true

    # Now set the password properly
    echo "from django.contrib.auth import get_user_model; \
          User = get_user_model(); \
          user = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME'); \
          user.set_password('$DJANGO_SUPERUSER_PASSWORD'); \
          user.save()" | python manage.py shell

    echo "Superuser created successfully!"
fi