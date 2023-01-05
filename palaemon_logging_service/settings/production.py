from .settings import *
import os

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.environ.get("POSTGRES_ADMIN_PASSWORD"),
        'HOST': 'db',
        'PORT': '5432',
    }
}