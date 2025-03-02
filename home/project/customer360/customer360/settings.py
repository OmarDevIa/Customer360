"""
Paramètres Django pour le projet customer360.

Généré par 'django-admin startproject' utilisant Django 4.2.4.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/4.2/topics/settings/

Pour la liste complète des paramètres et de leurs valeurs, voir
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Construire des chemins à l'intérieur du projet comme ceci : BASE_DIR / 'sous-dossier'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Paramètres de développement rapide - inadaptés pour la production
# Voir https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# AVERTISSEMENT DE SÉCURITÉ : gardez la clé secrète utilisée en production secrète !
SECRET_KEY = 'django-insecure-mxj20imb1j!8hz2!kqt*qh5^=y3q3^hyknmj**bpi9v2vuhr!p'

# AVERTISSEMENT DE SÉCURITÉ : ne pas exécuter avec le débogage activé en production !
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ['https://*.cognitiveclass.ai']

# Définition de l'application

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customer360'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'customer360.urls'

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

WSGI_APPLICATION = 'customer360.wsgi.application'


# Base de données
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validation des mots de passe
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalisation
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Fichiers statiques (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static/"),
)

# Type de champ clé primaire par défaut
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'