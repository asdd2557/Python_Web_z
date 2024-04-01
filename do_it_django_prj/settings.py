"""
Django settings for do_it_django_prj project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from asyncio.constants import ACCEPT_RETRY_DELAY
import os # 미디어 파일을 쓰겠다.

from pathlib import Path
from telnetlib import LOGOUT
from django.shortcuts import render

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','b@zg(te-o5db8m^+9a((nd(fs2k224=zlp^s#g+6skpmhb=-3d')

# SECURITY WARNING: don't run with debug turned on in production!

#DEBUG = int(os.environ.get('DEBUG',1))#인터넷 에러 메세지를 보여줄까에 대한 여부
DEBUG = True
if os.environ.get('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
else:
    ALLOWED_HOSTS = []



# Application definition

_STATIC = [
    BASE_DIR / "static",
]



CSRF_TRUSTED_ORIGINS = ['https://*.promicing.com', 'https://*.3.39.18.230']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_extensions',



    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'crispy_forms', ## 폼 이쁘게 꾸미기
    'markdownx',
    'blog',
    'single_pages',

    'ckeditor',#게시물 이미지 넣는 거
    'ckeditor_uploader',
    'ckeditor_static_add', #ckeditor 전용 static
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'allauth.account.middleware.AccountMiddleware',
   # 'allauth.account.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'do_it_django_prj.urls'

SITE_NAME = 'Promicing' #사이트 이름

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

WSGI_APPLICATION = 'do_it_django_prj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE','django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE',BASE_DIR / 'db.sqlite3'),
        'USER': os.environ.get('SQL_USER','user'),
        'PASSWORD':os.environ.get('SQL_PASSWORD', 'password'),
        'HOST':os.environ.get('SQL_HOST','localhost'),
        'PORT': os.environ.get('SQL_PORT','5432')
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/' #URL이 static으로 오는경우에 미디어 파일로 접근하는 로직
STATIC_ROOT = os.path.join(BASE_DIR, '_static')
MEDIA_URL = '/media/' #URL이 media로 오는경우에 미디어파일에 접근하는것이다.
MEDIA_ROOT = os.path.join(BASE_DIR, '_media') #파일이 저장되는곳을 지정해주는로직

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = 'bootstrap4' ## 폼 이쁘게 꾸미기

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]
SITE_ID = 5

ACCOUNT_EMAIL_REQUIRED = True ## 이메일 관리를 할것이냐
ACCOUNT_EMAIL_VERIFICATION = 'none' ## 회원가입을하면 그 이메일을 보내서 회원가입 할것이냐 물어보는것

LOGIN_REDIRECT_URL = '/' ## 로그아웃하였을경우 블로그홈페이지로 감
LOGOUT_REDIRECT_URL = '/blog/' ## 로그아웃하였을경우 블로그홈페이지로 감


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'PROMPT': 'select_account',
    },
}
# settings.py

SOCIALACCOUNT_ADAPTER = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

CKEDITOR_UPLOAD_PATH = 'uploads/'  # 이미지 저장할 경로

CKEDITOR_CONFIGS = {
    'default': {
        'extraPlugins': 'codesnippet,timestamp,tooltip,englishauto',  # 추가된 플러그인 이름들
        'toolbar': 'full',
        'allowedContent': True,
    },
}