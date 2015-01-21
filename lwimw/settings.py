import os
import socket
from django.contrib.messages import constants as message_constants
import private

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
HOSTNAME = socket.gethostname()

SECRET_KEY = private.SECRET_KEY

ADMINS = (
    ('David Colgan', 'dvcolgan@gmail.com'),
)
MANAGERS = ADMINS

# Settings that are different on prod, testing, and local dev.
# The only production location for this site is lookwhatimadeweekend.com;
# any other install is local dev.
if HOSTNAME == 'luffy':
    ALLOWED_HOSTS = ['lookwhatimadeweekend.com', 'lwimw.lessboring.com']
    DEBUG = False
    SITE_DOMAIN = 'lookwhatimadeweekend.com'
    SERVER = 'testing'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    ALLOWED_HOSTS = []
    DEBUG = True
    SITE_DOMAIN = 'lwimw.egg'
    SERVER = 'local'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lwimw.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


ROOT_URLCONF = 'lwimw.urls'
WSGI_APPLICATION = 'lwimw.wsgi.application'

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = False
USE_L10N = True
USE_TZ = True

EMAIL_PORT = 25
EMAIL_HOST_USER = private.POSTMARK_API_KEY
EMAIL_HOST_PASSWORD = private.POSTMARK_API_KEY
EMAIL_USE_TLS = True

SERVER_EMAIL = 'david@lessboring.com'
EMAIL_HOST = 'smtp.postmarkapp.com'
ADMIN_EMAIL_SENDER = SERVER_EMAIL
DEFAULT_FROM_EMAIL = SERVER_EMAIL

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'site-static')
STATIC_URL = '/static/'

INTERNAL_IPS = ('127.0.0.1',)

LOGIN_REDIRECT_URL = '/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django_extensions',
    'rest_framework',
    'widget_tweaks',
    'bootstrapform',
    'registration',
    'contests',
    'blog',
    'comments',
    'uploadedimages',
    'util',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'contests.middleware.CurrentContestMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert-info',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: 'alert-warning',
    message_constants.ERROR: 'alert-danger',
}

import django.conf.global_settings as DEFAULT_SETTINGS
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
ACCOUNT_ACTIVATION_DAYS = 7
