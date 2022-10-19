from os import getenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', 'k%4!f@&0(c$*h2#6+!t^cpm2=ctsh6k-ld9l-l2zudr$jaenw')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv("POSTGRES_DB", 'photo_service'),
        'USER': getenv("POSTGRES_USER", 'photo_service'),
        'PASSWORD': getenv("POSTGRES_PASSWORD", 'photo_service'),
        'HOST': getenv("POSTGRES_HOST", '127.0.0.1'),
        'PORT': getenv("POSTGRES_PORT", '5432')
    }
}

from .base import *
