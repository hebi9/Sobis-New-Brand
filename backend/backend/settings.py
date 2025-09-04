from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
RAIZ_DEL_PROYECTO = BASE_DIR.parent

SECRET_KEY = 'd44vyyh^6p$+a+1zdux3-ubdzn5!k+(md0@q!8du3e7&((1xzx'

import environ

env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

DEBUG = env.bool("DEBUG", default=False)
print("DEBUG:", DEBUG)
if DEBUG:
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
    ]
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]
else:
    ALLOWED_HOSTS = [
        "hebi.pythonanywhere.com",
    ]
    CSRF_TRUSTED_ORIGINS = [
        'http://hebi.pythonanywhere.com',
    ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
]

INSTALLED_APPS += [
    'core',
    'apps.finances',
    'apps.relationship',
    'apps.services',
    'apps.quotes',
    'apps.crm',
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
]



ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR.parent, 'frontend', 'build'),  # Para React compilado
            os.path.join(BASE_DIR, 'core', 'templates'),         # Para las plantillas de Django
        ],
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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    os.path.join(RAIZ_DEL_PROYECTO, 'frontend', 'build', 'static'),
]

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}
