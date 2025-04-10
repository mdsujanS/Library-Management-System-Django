from pathlib import Path
import os
import environ
import dj_database_url

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Security Settings
SECRET_KEY = "django-insecure-!ahgtm#y5qulkxe*ubf7n12n!$e457fh=13_0)j=iz(55vx=j#"
DEBUG = True
ALLOWED_HOSTS = ["*"]



# Application Definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "books",
    "accounts",
    "users",
    "authors",
    "categories",
    "user_borrow_book",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "library_management_system.urls"
CORS_ALLOWED_ORIGINS = [
    'https://our-library-management-system.onrender.com'
]
CSRF_TRUSTED_ORIGINS = [ 'https://our-library-management-system.onrender.com']
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "library_management_system.wsgi.application"

# Email Configuration


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("sksujon404319@gmail.com")
EMAIL_HOST_PASSWORD = os.environ.get("vgtsyymesxnwuqdl")
# Database Configuration
# DATABASES = {
#     "default": dj_database_url.config(
#         default=env("DATABASE_URL"),
#     )
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
