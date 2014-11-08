import os
import socket
from django.contrib.messages import constants as message_constants

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from private import SECRET_KEY, POSTMARK_API_KEY

ADMINS = (
    ('David Colgan', 'dvcolgan@gmail.com'),
)
SERVER_EMAIL = 'david@lessboring.com'
EMAIL_HOST = 'smtp.postmarkapp.com'

MANAGERS = ADMINS

HOSTNAME = socket.gethostname()
FILEPATH = os.path.abspath(__file__)

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


# Override prod settings here using your dev host name
if HOSTNAME == 'fire-star' or HOSTNAME == 'boa-hancock':
    DEBUG = True
    SITE_DOMAIN = 'lwimw.egg'
    SERVER = 'local'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
elif HOSTNAME == 'luffy':
    ALLOWED_HOSTS = ['lookwhatimadeweekend.com', 'lwimw.lessboring.com']
    DEBUG = False
    SITE_DOMAIN = 'lookwhatimadeweekend.com'
    SERVER = 'testing'

TEMPLATE_DEBUG = DEBUG

EMAIL_PORT = 25
EMAIL_HOST_USER = POSTMARK_API_KEY
EMAIL_HOST_PASSWORD = POSTMARK_API_KEY
EMAIL_USE_TLS = True

ADMIN_EMAIL_SENDER = SERVER_EMAIL
DEFAULT_FROM_EMAIL = SERVER_EMAIL

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = False
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'site-static')
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'contests.middleware.CurrentContestMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'lwimw.urls'

WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
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

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'widget_tweaks',
    'bootstrapform',
    'registration',
    'contests',
    'util',
    'themevoting',
    'blog',
    #'debug_toolbar',
)
ACCOUNT_ACTIVATION_DAYS = 7

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
