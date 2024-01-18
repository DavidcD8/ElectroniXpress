from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
    "8001-davidcd8-electronixpress-twqcrugx1c.us2.codeanyapp.com",
    "127.0.0.1",
    "8000-davidcd8-electronixpress-twqcrugx1c.us2.codeanyapp.com",
    "8000-davidcd8-electronixpress-ay7zuhy2l0.us2.codeanyapp.com",
    "8000-davidcd8-electronixpress-j30mzjfann.us2.codeanyapp.com",
    "localhost",
    "8000-davidcd8-electronixpress-j30mzjfann.us2.codeanyapp.com",
    "onlineshopfirst-9d7d819c65b1.herokuapp.com",  
     'https://8000-davidcd8-electronixpress-2sbslal7d5.us2.codeanyapp.com',
     '8000-davidcd8-electronixpress-2sbslal7d5.us2.codeanyapp.com',
     "127.0.0.1",
    "localhost",
    "8000-davidcd8-electronixpress-2sbslal7d5.us2.codeanyapp.com",
    "onlineshopfirst-9d7d819c65b1.herokuapp.com", '8000-davidcd8-electronixpress-t8cw2ni2o3.us2.codeanyapp.com'
    ,]

CSRF_USE_SESSIONS = True
CSRF_COOKIE_SECURE = True
FREE_DELIVERY_THRESHOLD = 100
STANDARD_DELIVERY_PERCENTAGE = 5

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "bag",
    "checkout",
    "onlineshop",
    "crispy_forms",
    "whitenoise",
    "crispy_bootstrap4",
    "django.contrib.sitemaps",
]


CRISPY_TEMPLATE_PACK = "bootstrap4"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]


ROOT_URLCONF = "geekygizmos.urls"


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
                "bag.contexts.bag_contents",
            ],
        },
    },
]


SITE_ID = 1

ESMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_SIGNUP_URL = "/accounts/signup/"
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
WSGI_APPLICATION = "geekygizmos.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(
        os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


if "USE_AWS" in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = "onlineshopfirst"
    AWS_S3_REGION_NAME = "eu-west-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # Static and media files
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    MEDIAFILES_LOCATION = "media"

    # Override static and media URLs in production
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"

WHITENOISE_USE_FINDERS = True
STATIC_URL = "static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
STRIPE_CURRENCY = "EUR"
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", "")


if "DEVELOPMENT" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "codeinstitutetest@example.com"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS")
    DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CSRF_TRUSTED_ORIGINS = [
    "https://8000-davidcd8-electronixpress-twqcrugx1c.us2.codeanyapp.com/admin/login/?next=/admin/",
    
    'http://127.0.0.1:8000/',
    'https://8000-davidcd8-electronixpress-2sbslal7d5.us2.codeanyapp.com',
    'https://8000-davidcd8-electronixpress-2sbslal7d5.us2.codeanyapp.com',
    'https://8000-davidcd8-electronixpress-t8cw2ni2o3.us2.codeanyapp.com',
    
    "https://8000-davidcd8-electronixpress-twqcrugx1c.us2.codeanyapp.com",
    "http://127.0.0.1:8000/",
    "https://8000-davidcd8-electronixpress-2sbslal7d5.us2.codeanyapp.com",
    "https://8000-davidcd8-electronixpress-t8cw2ni2o3.us2.codeanyapp.com",
    # Add other valid origins as needed
]

AUTHENTICATION_BACKENDS = {
    # to login username in django admin, regardless of allauth
    "django.contrib.auth.backends.ModelBackend",
    # allauth specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
}
