import os
from pathlib import Path
from .settings import *
from .settings import BASE_DIR

render_hostname = [os.environ.get("RENDER_EXTERNAL_HOSTNAME")]

ALLOWED_HOSTS = [render_hostname, 'workout-frontend-e4vi.onrender.com', 'workoutgenerator-5hjc.onrender.com', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = [f"https://{render_hostname}"]

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Uncomment and customize CORS_ALLOWED_ORIGINS if needed
# CORS_ALLOWED_ORIGINS = ['http://localhost:3000']

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    }
}

# Switch to using SQLite instead of PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
