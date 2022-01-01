from .base import *
from decouple import config
import os

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'django-insecure-#ozpdv!r#6e*2m=&#rg(txzy2+vnkgi9k-g6-4z399&i@$zty!'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
