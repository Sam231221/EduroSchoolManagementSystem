from Dpfp.base import *

from .environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

DEBUG = True

SECRET_KEY = env.str("SECRET_KEY")
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
# }

"""
#POSTGRES DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str("DATABASE_NAME"),  
        'USER': env.str("DATABASE_USER"),    
        'PASSWORD': env.str("DATABASE_PASSWORD"),  
        'HOST': env.str("DATABASE_HOST"),
        'PORT': env.str("DATABASE_PORT"),
    }
}

"""


# SMTP CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env.str("Email_Host_User")
EMAIL_HOST_PASSWORD = "qpsy fgsc mdyp dpoe"
