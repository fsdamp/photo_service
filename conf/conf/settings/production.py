from os import getenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', 'django-insecure-o0lv(_-h*@oe3m&6q&0r1m475nfu+=#ke%(8x=@eu-3@w6%ev)')

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
