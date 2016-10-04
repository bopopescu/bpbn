"""
Django settings for bpbn project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e^zzrs@r%xtk@mg4^$+g88a53btkn)1hj@wp63s%s6zzi^f8!r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Settings by David
DATE_INPUT_FORMATS = ('%d.%m.%Y')
DECIMAL_SEPERATOR = ','
USE_THOUSAND_SEPERATOR = True
THOUSAND_SEPARATOR = '.'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'domainmanager.apps.DomainmanagerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lineage',
    'coverage',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bpbn.urls'

TEMPLATES = []

server = os.path.abspath("settings.py")

# D:\\ indicates local development environment
if server.startswith("D:\\"):

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                'D:/Stuff/Django_projects/bpbn_github/bpbn/domainmanager/templates/domainmanager/',
                'D:/Stuff/Django_projects/bpbn_github/bpbn/domainmanager/templates/domainmanager/forms/',
                'D:/Stuff/Django_projects/bpbn_github/bpbn/domainmanager/templates/domainmanager/customTags/'
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.template.context_processors.media',
                ],
            },
        },
    ]

else:

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                '/home/Maunzinator/bpbn/domainmanager/templates/domainmanager/',
                '/home/Maunzinator/bpbn/domainmanager/templates/domainmanager/forms/',
                '/home/Maunzinator/bpbn/domainmanager/templates/domainmanager/customTags/'
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.template.context_processors.media',
                ],
            },
        },
    ]

WSGI_APPLICATION = 'bpbn.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        #        'NAME':'bpbn',
        #        'HOST':'localhost',
        #        'PORT':'3306',
        #        'USER':'developer',
        #        'PASSWORD':'developer'
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'domainmanager',
#        'USER': 'domainmanager_user',
#        'PASSWORD': '\\{!g\\78]45cNbnG',
#        'HOST': '52.59.228.47',
#        'PORT': '5432',
#   }
#}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/Vienna'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

# MEDIA_URL = '/upload/'
MEDIA_URL = '/upload/'

MEDIA_ROOT = os.path.join(BASE_DIR, "domainmanager/upload")

LOGIN_URL = '/admin/login/'
