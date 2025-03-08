"""
Django settings for project_name.

Updated for Django 5.0 compatibility.

For more information, see:
https://docs.djangoproject.com/en/5.0/topics/settings/
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os

# Environment Configuration
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
IS_PRODUCTION = ENVIRONMENT == "production"

# Security Settings
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
DEBUG_TOOLBAR = os.environ.get("DEBUG_TOOLBAR", "False").lower() == "true"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Allowed Hosts (Flexible for Development & Production)
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Application definition

DEPENDENCIES_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'main',
]

ADDONS = [
    # Uncomment if needed
    # 'webpack_loader',
    # 'rest_framework',
    # 'push_notifications',
]

INSTALLED_APPS = DEPENDENCIES_APPS + ADDONS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_name.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project_name.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Static Files Configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email Config
EMAIL_SUBJECT_PREFIX = '[project_name] '
DEFAULT_FROM_EMAIL = 'No Reply <no-reply@project_name.com>'
SERVER_EMAIL = 'Server <server@project_name.com>'
# ADMINS = [('Admin', 'admin@project_name.com')]
# MANAGERS = [('Admin', 'admin@project_name.com')]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True

# Secure Headers (Disable only in local development)
SECURE_CROSS_ORIGIN_OPENER_POLICY = None if DEBUG else "same-origin"
