"""
Django settings for broomtrade project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cldnguyafqc#-d&=xd5$(q(2hm8qq)f8m2+*wycp6%joi*d5aj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # обеспечивает поддержку нескольких сайтов одной копией Django, без нее не работают комменты
    'django.contrib.comments',
    'easy_thumbnails',
    'taggit',
    'precise_bbcode',
    'main',
    'guestbook',
    'news',
    'imagepool',
    'categories',
    'goods',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'broomtrade.urls'

WSGI_APPLICATION = 'broomtrade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/site.dat'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'  # префикс, который будет добавлятся к интернет-адресу каждого статичного файла

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR,  'static'),)

MEDIA_ROOT = os.path.join(BASE_DIR,  'uploads')  # папка для хранения выгруженных файлов
MEDIA_URL = '/media/'  # префикс интернет-адреса для выгруженных выйлов

LOGIN_URL = 'login'  # имя привязки для страницы входа
LOGOUT_URL = 'logout'  # имя привязки для страницы выхода

SITE_ID = 1  # указываем, поскольку включенна поддержка нескольких сайтов одной копией Django

THUMBNAIL_BASEDIR = 'thumbnails'
# THUMBNAIL_DEFAULT_OPTIONS = {'detail': True}
THUMBNAIL_ALIASES = {'goods.Good.image': {'base': {'size': (200, 100), 'base': True}}}  # задаем единственный псевдоним 'base', содержащий параметры для миниатюр товаров, которые будут выводиться в списке


MANAGERS = (('admin', 'admin@someserver.ru'),)  # параметры рассылки уведомлений о вновь добавленных комментариях
EMAIL_HOST = 'someserver'
EMAIL_HOST_USER = 'user'
EMAIL_HOST_PASSWORD = '1234567890'
# EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'mailer@someserver.ru'

LOGIN_REDIRECT_URL = 'main'  # перенаправляет на главную страницу после входа
