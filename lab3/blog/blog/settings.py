"""
Лабораторные работы №5-7 - Настройки Django проекта

Этот файл содержит все настройки Django приложения.
Django использует эти настройки при запуске сервера.

Важные настройки:
- DEBUG = True - режим разработки (показывает подробные ошибки)
- DATABASES - подключение к базе данных
- INSTALLED_APPS - список всех приложений Django
- STATIC_URL - путь к статическим файлам (CSS, JS, картинки)
"""

from pathlib import Path

# Базовая директория проекта - от неё строятся все остальные пути
# Path(__file__) - путь к этому файлу (settings.py)
# .resolve() - преобразует в абсолютный путь
# .parent.parent - поднимаемся на два уровня вверх (blog/blog/settings.py -> blog/)
BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# НАСТРОЙКИ БЕЗОПАСНОСТИ
# ==========================================

# Секретный ключ - используется для шифрования сессий и токенов
# В продакшене нужно хранить его в переменных окружения!
SECRET_KEY = 'django-insecure-rt155f%8p+8c%tgnid2+$%-$!(_uw$j5l%bu%^bb1%@!0s(e4h'

# DEBUG = True показывает подробные ошибки (только для разработки!)
DEBUG = True

# Список доменов, на которых может работать сайт
# Пустой список = только localhost
ALLOWED_HOSTS = []


# ==========================================
# УСТАНОВЛЕННЫЕ ПРИЛОЖЕНИЯ
# ==========================================

INSTALLED_APPS = [
    # Встроенные приложения Django
    'django.contrib.admin',          # Админ-панель
    'django.contrib.auth',           # Система авторизации
    'django.contrib.contenttypes',   # Типы контента
    'django.contrib.sessions',       # Сессии пользователей
    'django.contrib.messages',       # Сообщения (уведомления)
    'django.contrib.staticfiles',    # Статические файлы
    # Наше приложение
    'articles',                      # Приложение со статьями блога
]

# Middleware - промежуточные обработчики запросов
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',           # Защита от CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'  # Главный файл с URL-маршрутами

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],              # Дополнительные папки с шаблонами
        'APP_DIRS': True,        # Искать шаблоны в папках приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# ==========================================
# БАЗА ДАННЫХ
# ==========================================
# Используем SQLite - простая база данных в одном файле
# Для продакшена лучше использовать PostgreSQL или MySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Движок SQLite
        # Путь к файлу базы данных - общий для всех лабораторных
        'NAME': r'D:\Yandex.Disk\project\p33\shared_db\django_labs.db',
    }
}


# ==========================================
# ВАЛИДАЦИЯ ПАРОЛЕЙ
# ==========================================
# Django проверяет пароли по этим правилам при регистрации

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


# ==========================================
# ЛОКАЛИЗАЦИЯ
# ==========================================

LANGUAGE_CODE = 'en-us'  # Язык интерфейса

TIME_ZONE = 'UTC'        # Часовой пояс

USE_I18N = True          # Включить интернационализацию

USE_TZ = True            # Использовать временные зоны


# ==========================================
# СТАТИЧЕСКИЕ ФАЙЛЫ (CSS, JavaScript, картинки)
# ==========================================

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
