import os
from pathlib import Path
import crispy_forms

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-)$hrhngd0d!5(*-r2h1vi)_=gb3p95dd&hi@d1*(^$a$05^y#0"

DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['.vercel.app', '.now.sh', '127.0.0.1', 'localhost']


INSTALLED_APPS = [
    'daphne',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "user",
    'bootstrap4',
    'ventes',
    'channels',
    'chatapp',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = ['bootstrap5', 'bootstrap4', 'uni_form']

CRISPY_TEMPLATE_PREFIX = 'bootstrap5/uni_form'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Paramètres d'e-mail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.example.com'  # Remplacez par l'hôte SMTP de votre serveur de messagerie
# EMAIL_PORT = 587  # Port SMTP
# EMAIL_HOST_USER = 'your-email@example.com'  # Votre adresse e-mail
# EMAIL_HOST_PASSWORD = 'your-email-password'  # Votre mot de passe e-mail
# EMAIL_USE_TLS = True  # Utiliser TLS pour la connexion sécurisée

# Autres paramètres d'e-mail facultatifs
# EMAIL_USE_SSL = True  # Utiliser SSL pour la connexion sécurisée
# DEFAULT_FROM_EMAIL = 'your-email@example.com'  # Adresse e-mail par défaut
# EMAIL_TIMEOUT = None  # Durée d'attente pour la connexion SMTP (en secondes)

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME":"railway",
        "USER":"postgres",
        "PASSWORD":"ObamQVEbE5VQJI0fAywS",
        "HOST":"containers-us-west-94.railway.app",
        "PORT":"5693",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"

ADMIN_URL = "admin/"

ACCOUNT_FORMS = {
    'signup': 'user.forms.SpyBookSignupForm',
    # Autres clés de formulaire...
}

LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = ""

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

ASGI_APPLICATION = 'core.asgi.application' 

