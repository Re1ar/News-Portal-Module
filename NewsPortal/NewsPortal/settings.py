"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Постройте пути внутри проекта следующим образом: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v)!*+z++1n=g=g)9d9+o628rae)7k5dj=!x*v_74ary2tgjh5j'

# SECURITY WARNING: don't run with debug turned on in production!
# Включает режим отладки. Важно! При запуске реального проекта в работу
# нужно отключать, прописав "False"
DEBUG = True

# Локальный адрес проекта
ALLOWED_HOSTS = ['127.0.0.1']


# Application definition
# Список установленных(подключенных) приложений
# Каждый раз, при создании(использовании) нового(существующего) приложения, его нужно прописывать здесь
# иначе джанго не обнаружит созданное(используемое) приложение

INSTALLED_APPS = [
    # Список приложений созданных по умолчанию
    'django.contrib.admin',
    'django.contrib.auth',  # приложение поддержки авторизации
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # управление сессиями.
    # В обработке каждого запроса (переменная request) вы можете получить доступ к данным сессии
    # (которые хранятся на сервере) и каким-то образом манипулировать ими.

    'django.contrib.messages',
    'django.contrib.staticfiles',  # приложение для работы с "статическими файлами"(CSS, Java и т.д)

    # Список пользовательских приложений, создается разработчиком
    'django.contrib.sites',
    'django.contrib.flatpages',
    # news - основное приложение новостного портала
    'news.apps.NewsConfig',

    # приложение для идентификации, аутентификации и авторизации
    'sign',
    'protect',
    # приложение для подключения фильтров
    'django_filters',
    # подключение приложений из "allauth"
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    # Необходимо для реализации регистрации через провайдер "Google"
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]

DEFAULT_FROM_EMAIL = 'rolan@yandex.ru'  # здесь указываем ПОЛНУЮ почту, с которой будут отправляться письма

# Идентификатор (целое число) текущего сайта в таблице базы данных django_site .
# Может использоваться приложениями для связывания своих данных с определенными сайтами и,
# таким образом, для управления контентом нескольких сайтов в единой базе данных.
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

# Настройка шаблонов
# параметр "DIRS" - настраивает путь к папке шаблона
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Задаем путь к папке с шаблонами, где джанго будет их искать
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',  # контекстный процессор, нужен для allauth.
            ],
        },
    },
]

# Добавляем бэкенды аутентификации:
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    # встроенный бэкенд Django, реализующий аутентификацию по username
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    # бэкенд аутентификации, предоставленный пакетом allauth
    'allauth.account.auth_backends.AuthenticationBackend',
    # нам нужно «включить» аутентификацию как по username, так и специфичную по email или сервис-провайдеру.
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'Asia/Vladivostok'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# URL, указывающий на каталог со статическими файлами
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройка STATICFILES_DIRS указывает каталоги, которые проверяются на наличие статических файлов.
STATICFILES_DIRS = [
    BASE_DIR/"static"
]

LOGIN_URL = '/account/login/'  # страница аутентификации
# LOGIN_REDIRECT_URL = '/'  # страница, на которую перенаправляется пользователь после успешного входа на сайт,

# регистрация по электронной почте.
# В файл настроек проекта мы должны внести дополнительные параметры:
# (1)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

# Модуль Д6 - настройка отправки почты
EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же всегда
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый всегда
EMAIL_HOST_USER = 'rolan'  # имя пользователя, например, если почта user@yandex.ru, то надо
# писать user, иными словами, это всё то что идёт до собачки (@)
EMAIL_HOST_PASSWORD = 'Rfkjifff21541' # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, включать обязательно, защита от хакеров

SERVER_EMAIL = 'rolan@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке

# Модуль 6.3 - подтверждение регистрации через почту
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTIFICTION_METHOD = 'email'

# Модуль 6.5 - действия по расписанию
# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше,
# но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


CELERY_BROKER_URL = 'redis://localhost:6379'  # указывает на URL брокера сообщений (Redis).
                                              # По умолчанию он находится на порту 6379.
CELERY_RESULT_BACKEND = 'redis://localhost:6379'  # указывает на хранилище результатов выполнения задач.
CELERY_ACCEPT_CONTENT = ['application/json']  # допустимый формат данных.
CELERY_TASK_SERIALIZER = 'json'  # метод сериализации задач.
CELERY_RESULT_SERIALIZER = 'json'  # метод сериализации результатов.





# (1)
# Первые два указывают на то, что поле email является обязательным и уникальным, а третий, наоборот, говорит,
# что username теперь необязательный. Следующий параметр указывает, что аутентификация будет происходить
# посредством электронной почты. Напоследок мы указываем, что верификация почты отсутствует. Обычно на почту
# отправляется подтверждение аккаунта, после подтверждения которого восстанавливается полная функциональность
# учетной записи. Для тестового примера нам не обязательно это делать.