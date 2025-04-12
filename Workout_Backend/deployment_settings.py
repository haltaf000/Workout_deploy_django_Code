import os
from pathlib import Path
from .settings import *
from .settings import BASE_DIR

# Security
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')

# Hosts
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
ALLOWED_HOSTS = [
    RENDER_EXTERNAL_HOSTNAME,
    'workout-frontend-e4vi.onrender.com',
    'workoutgenerator-5hjc.onrender.com',
    '127.0.0.1'
] if RENDER_EXTERNAL_HOSTNAME else [
    'workout-frontend-e4vi.onrender.com',
    'workoutgenerator-5hjc.onrender.com',
    '127.0.0.1'
]

CSRF_TRUSTED_ORIGINS = [
    f'https://{host}' for host in ALLOWED_HOSTS if host and not host.startswith('127.')
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# CORS
CORS_ALLOWED_ORIGINS = [
    'https://workout-frontend-e4vi.onrender.com',
    'http://localhost:3000'
]