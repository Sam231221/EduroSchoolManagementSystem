from Dpfp.base import *

from .environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

DEBUG = True
SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = ["*"]

# Order matters
MIDDLEWARE = [
    #'django.middleware.cache.UpdateCacheMiddleware',         #Explict middleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    #'whitenoise.middleware.WhiteNoiseMiddleware',             #Explict middleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    #'django.middleware.cache.FetchFromCacheMiddleware',      #Explict middleware
    # 'csp.middleware.CSPMiddleware',                           #Explict middleware
]

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
}
# Content Security Policy
"""
CSP_DEFAULT_SRC = ('none', )
CSP_BASE_URI = ("'none'", )
CSP_FRAME_ANCESTORS = ("'none'", )
CSP_OBJECT_SRC =('none',)
CSP_STYLE_SRC = ("'self'","'unsafe-inline'", 'cdn.jsdelivr.net' , 'cdnjs.cloudflare.com','fonts.googleapis.com', 'stackpath.bootstrapcdn.com', 'getbootstrap.com')
CSP_SCRIPT_SRC = ("'self'","'unsafe-inline'",'ajax.googleapis.com',  'cdn.jsdelivr.net' ,'cdn.ckeditor.com','stackpath.bootstrapcdn.com', 'code.jquery.com', 'unpkg.com', 'cdnjs.cloudflare.com', 'code.jquery.com', 'getbootstrap.com')
CSP_IMG_SRC = ("'self'", '* data:',  'cdn.jsdelivr.net', 'res.cloudinary.com')
CSP_FONT_SRC = ("'self'",'cdnjs.cloudflare.com', 'cdn.jsdelivr.net' ,'fonts.googleapis.com', 'fonts.gstatic.com')

CSP_FRAME_SRC =("'self'",)
CSP_CONNECT_SRC = ("'self'",
	"http://*.cke-cs.com",
    'https://docx-converter.cke-cs.com', 
    'https://pdf-converter.cke-cs.com',
 )
"""


# CACHE FRAMEWORK
CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 60  # 1 week
CACHE_MIDDLEWARE_KEY_PREFIX = ""

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 15780000  # 6 Months as Recommended
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# CSRF
CSRF_COOKIE_SECURE = True  # to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True  # to avoid transmitting the session cookie over HTTP accidentally.

# REDIRECT HTTP TO HTTPS
SECURE_SSL_REDIRECT = True


"""
import dj_database_url
db_from_env=dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
"""


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# CLOUDINARY STORAGE
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# SMTP CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = env.str("Email_Host_User")
EMAIL_HOST_PASSWORD = env.str("Email_Host_Password")
