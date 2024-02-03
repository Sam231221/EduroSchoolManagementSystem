import os
from pathlib import Path
import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
EXPLICT_APPS = [
    #'django.contrib.sites',
    'MAuthentication.apps.MAuthenticationConfig',
    'MEhub',
    "MManagement",
    "MOthers",
    "ckeditor",
    "ckeditor_uploader",
       'rest_framework',
    'corsheaders',
]
THIRDPARTY_PLUGIN = [
    #'whitenoise'
]

AUTH_USER_MODEL = "MAuthentication.User"

ROOT_URLCONF = "Dpfp.urls"
INSTALLED_APPS = DEFAULT_APPS + EXPLICT_APPS + THIRDPARTY_PLUGIN

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',  
                'MAuthentication.context_processors.forms',
            ],
        },
    },
]

WSGI_APPLICATION = "Dpfp.wsgi.application"

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

CKEDITOR_UPLOAD_PATH = "Sms/uploads/"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "uiColor": "#FFFFFF",
        "height": 500,
        "toolbar_Custom": [
            ["Styles", "Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker", "Undo", "Redo"],
            ["Link", "Unlink", "Anchor"],
            ["Image", "Flash", "Table", "HorizontalRule"],
            ["TextColor", "BGColor"],
            ["Smiley", "SpecialChar"],
            ["Source"],
        ],
    },
    "sourcecode": {
        "skin": "moono",
        # 'skin': 'office2013',
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {"name": "document", "items": ["Source", "-", "Save", "NewPage", "Preview", "Print", "-", "Templates"]},
            {
                "name": "clipboard",
                "items": ["Cut", "Copy", "Paste", "PasteText", "PasteFromWord", "-", "Undo", "Redo"],
            },
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            {
                "name": "insert",
                "items": ["Image", "Flash", "Table", "HorizontalRule", "Smiley", "SpecialChar", "PageBreak", "Iframe"],
            },
            "/",
            {
                "name": "basicstyles",
                "items": ["Bold", "Italic", "Underline", "Strike", "Subscript", "Superscript", "-", "RemoveFormat"],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "CreateDiv",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "BidiLtr",
                    "BidiRtl",
                    "Language",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            "\t",
            {
                "name": "tools",
                "items": [
                    "CodeSnippet",
                    "youtube",
                    "clipboard",
                    "ShowBlocks",
                    "Preview",
                    "Maximize",
                ],
            },
            "/",  # put this to force next toolbar on new line
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        "toolbarGroups": [{"name": "document", "groups": ["mode", "document", "doctools"]}],
        "width": "100%",
        "removePlugins": "stylesheetparser",
        "toolbarCanCollapse": True,
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                "codesnippet",
                "widget",
                "lineutils",
                "clipboard",
                "elementspath",
            ]
        ),
    },
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
CORS_ALLOW_ALL_ORIGINS=True
SOCIAL_AUTH_FACEBOOK_KEY = '605352750442305'
SOCIAL_AUTH_FACEBOOK_SECRET = '9b701b2223914aeda73111b89cc295c4'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '848686387472-1cmojobb1oqs50591bglb73fc9rbac6e.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'FYOLzOHwhZv_GkDONcoYN3nQ'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LdaeUAfAAAAAM9bU8TxfRTky-ok_qnhsF6gq-za'

LOGIN_URL = "/accounts/login/"

'''
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

'''

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kathmandu"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/staticfiles/"



STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "staticfiles/mediafiles")
MEDIA_URL = "/mediafiles/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
