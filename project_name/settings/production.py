from .common import *
from .partials.util import get_secret

DEBUG = False

# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

ALLOWED_HOSTS = ['.project_name.com']
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

if get_secret('DATABASE_URL'):
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    POSTGRES_USER = get_secret('POSTGRES_USER')
    POSTGRES_PASSWORD = get_secret('POSTGRES_PASSWORD')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'project_name',
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': 'db',
            'PORT': 5432,
        }
    }

# Email Config
"""
EMAIL_PASSWORD = get_secret('EMAIL_PASSWORD')
EMAIL_HOST = 'smtp.project_name.com'
EMAIL_HOST_USER = 'project_name'
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
"""
