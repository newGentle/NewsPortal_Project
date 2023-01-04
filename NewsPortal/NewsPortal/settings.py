"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from dotenv import load_dotenv

import os
from pathlib import Path

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    # 'accounts',
    'django_filters',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates'), os.path.join(BASE_DIR / 'templates', 'allauth',)],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'news_db',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGES = [
    ('ru', 'Russian'),
    ('en', 'English')
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

LOGIN_REDIRECT_URL = 'posts_list'
LOGOUT_REDIRECT_URL = '/accounts/login'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignUpForm'}

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('ACC_LOGIN')
EMAIL_HOST_PASSWORD = os.getenv('ACC_PASSWORD')
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_OF_ADMIN')

SERVER_EMAIL = os.getenv('EMAIL_OF_ADMIN')
ADMINS = [
    ('Admin'),(os.getenv('EMAIL_OF_ADMIN')),
    ]

# из за спамов был добавлен отладочный вариант отправки почты
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_URL = 'http://127.0.0.1:8000'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        }
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
    
#     'formatters': {
#         'console_DEBUG': {
#             'format': '{asctime} {levelname} {message}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
    
#         'console_WARNING': {
#             'format': '{asctime} {levelname} {message} {pathname}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
    
#         'console_ERROR': {
#             'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#         'file_INFO': {
#             'format': '{asctime} {levelname} {module} {message}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#     },
    
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#     },
#     'handlers': {
#         'console_D': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_DEBUG',
#         },
#         'console_W': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_WARNING',
#         },
#         'console_E': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_ERROR',
#         },
#         'file_I': {
#             'level': 'INFO',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'filename': 'general.log',
#             'formatter': 'file_INFO',
#         },
#         'file_E': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'errors.log',
#             'formatter': 'console_ERROR',
#         },
#         'file_S': {
#             'class': 'logging.FileHandler',
#             'filename': 'security.log',
#             'formatter': 'file_INFO',
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#             'formatter': 'console_WARNING',
#         },
#     },
    
#     'loggers': {
#         'django': {
#             'level': 'DEBUG',
#             'handlers': ['console_D', 'console_W', 'console_E', 'file_I'],
#             'propagate': True,
#         },
#         'django.request': {
#             'level': 'ERROR',
#             'handlers': ['file_I', 'mail_admins'],
#             'propagate': True,
#         },
#         'django.server': {
#             'level': 'ERROR',
#             'handlers': ['file_I', 'mail_admins'],
#             'propagate': True,
#         },
#         'django.template': {
#             'level': 'ERROR',
#             'handlers': ['file_I'],
#             'propagate': True,
#         },
#         'django.db.backends': {
#             'level': 'ERROR',
#             'handlers': ['file_I'],
#             'propagate': True,
#         },
#         'django.security': {
#             'handlers': ['file_S'],
#             'propagate': True,
#         },
#     },
# }
