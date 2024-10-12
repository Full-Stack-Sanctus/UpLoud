#import django 
#django.setup() 
#from rest_framework_simplejwt.authentication import JWTAuthentication  
#import rest_framework_simplejwt
#import corsheaders
from decouple import config
import dj_database_url
"""
Django settings for NaijaTrans project.
Generated by 'django-admin startproject' using Django 5.1.1.
For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q&3j9a4q6%!u-*!3ursgx-q$qax)2eu*om-+92@svm13*#x*6s'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Application definition
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party apps
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    # My app
    'naijatrans',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]
ROOT_URLCONF = 'NaijaTrans.urls'
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
WSGI_APPLICATION = 'NaijaTrans.wsgi.application'
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
ALLOWED_HOSTS = ['https://empire-djangob.onrender.com', 'empire-djangob.onrender.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.sqlite3', etc.
        'NAME': config('DB_NAME'),  # Specify your database name
        'USER': config('DB_USER'),  # Specify your database user
        'PASSWORD': config('DB_PASSWORD'),  # Specify your database password
        'HOST': config('DB_HOST', default='localhost'),  # Specify your database host
        'PORT': config('DB_PORT', default='5432'),  # Specify your database port
    }
}


LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/auth/profile/'


AUTHENTICATION_BACKENDS = [
    'naijatrans.EmailAuth.EmailAuthBackend',  # Custom email backend
    'django.contrib.auth.backends.ModelBackend',  # Default backend
]


AUTH_USER_MODEL = 'naijatrans.UserLogin'  # Assuming your app is named naijatrans
