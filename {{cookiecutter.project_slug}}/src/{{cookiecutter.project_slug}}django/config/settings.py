"""
Django settings for {{cookiecutter.project_slug}}django project.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import sys
from pathlib import Path
import os
import logging

import ldap
from django.db import DatabaseError
from django_auth_ldap.config import (
    LDAPSearch,
    GroupOfNamesType,
    LDAPSearchUnion,
    LDAPGroupQuery,
)

import oracledb


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-(*b5_%3-$%9n4((5_8y%%nl1rug206z#&dk=4onh6+!h!bh8#@"
SECRET_KEY = os.getenv("SECRET_KEY")

# Environment
ENV = os.getenv("ENV")

if ENV is None:
    ENV = "DD"

assert ENV in (
    "DD",
    "TO",
    "TC",
    "PP",
), "ENV needs to be one of the following values: DD, TO, TC or PP"

if ENV == "DD":
    DEBUG = True
else:
    DEBUG = False

TAG_VERSION = os.getenv("TAG_VERSION")

logging.info(os.getenv("ALLOWED_HOSTS"))

ALLOWED_HOSTS = ["localhost", "0.0.0.0", os.getenv("ALLOWED_HOSTS")]

# Application definition

INSTALLED_APPS = [
    "{{cookiecutter.project_slug}}django",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "rest_framework_datatables",
    "django_filters",
    "graphene_django",
]

GRAPHENE = {"SCHEMA": "config.schema.schema"}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# set oracledb -> cx_oracle
# sys.modules["cx_Oracle"] = oracledb

if ENV in ["DD", "TO", "TC"]:
    DATABASE_DSN = (
        f"(DESCRIPTION = (ADDRESS_LIST =  "
        f"(ADDRESS = (PROTOCOL = TCP)(HOST = {os.getenv('{{cookiecutter.project_slug.upper()}}_DB_HOST')})(PORT = {os.getenv('{{cookiecutter.project_slug.upper()}}_DB_PORT')})) ) "
        f"(CONNECT_DATA = (SERVICE_NAME = {os.getenv('{{cookiecutter.project_slug.upper()}}_DB_SERVICE')}) ) )"
    )
elif ENV == "PP":
    DATABASE_DSN = (
        f"(DESCRIPTION_LIST= (LOAD_BALANCE=off) (FAILOVER=on) (DESCRIPTION= (CONNECT_TIMEOUT=5) (TRANSPORT_CONNECT_TIMEOUT=3) (RETRY_COUNT=3) "
        f"(ADDRESS_LIST= (LOAD_BALANCE=on) (ADDRESS= (PROTOCOL=TCP) (HOST={os.getenv('{{cookiecutter.project_slug.upper()}}_DB_HOST')}) (PORT={os.getenv('{{cookiecutter.project_slug.upper()}}_DB_PORT')}) ) ) "
        f"(CONNECT_DATA=(SERVICE_NAME={os.getenv('{{cookiecutter.project_slug.upper()}}_DB_SERVICE')})) ) "
        f"(DESCRIPTION= (CONNECT_TIMEOUT=5) (TRANSPORT_CONNECT_TIMEOUT=3) (RETRY_COUNT=3) (ADDRESS_LIST= (LOAD_BALANCE=on) "
        f"(ADDRESS=(PROTOCOL=TCP)(HOST={os.getenv('{{cookiecutter.project_slug.upper()}}_DB_HOST_FAILOVER')})(PORT={os.getenv('{{cookiecutter.project_slug.upper()}}_DB_PORT')})) ) "
        f"(CONNECT_DATA=(SERVICE_NAME={os.getenv('{{cookiecutter.project_slug.upper()}}_DB_SERVICE')})) ) )"
    )
else:
    DATABASE_DSN = "+++ not set +++"


DATABASE_DSN = (
    f"(DESCRIPTION = (ADDRESS_LIST =  "
    f"(ADDRESS = (PROTOCOL = TCP)(HOST = {os.getenv('{{cookiecutter.project_slug.upper()}}_DB_HOST')})(PORT = {os.getenv('{{cookiecutter.project_slug.upper()}}_DB_PORT')})) ) "
    f"(CONNECT_DATA = (SERVICE_NAME = {os.getenv('{{cookiecutter.project_slug.upper()}}_DB_SERVICE')}) ) )"
)

# logging.info("DATABASE_DSN: " + DATABASE_DSN)

DATABASES = {
    # "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "SqliteLocal"}
    "default": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": DATABASE_DSN,
        "USER": os.getenv("{{cookiecutter.project_slug.upper()}}_DB_USER"),
        "PASSWORD": os.getenv("{{cookiecutter.project_slug.upper()}}_DB_PASSWORD"),
        "LIB_DIR": os.getenv("DIR_ORACLE_LIB"),
        "TEST": {
            # "NAME": DATABASE_TEST_DSN,
            # "USER": os.getenv("{{cookiecutter.project_slug.upper()}}_DB_TEST_USER"),
            # "PASSWORD": os.getenv("{{cookiecutter.project_slug.upper()}}_DB_TEST_PASSWORD"),
            # "CREATE_DB": False,
            # "CREATE_USER": False,
            "MIRROR": "default"  # Do not create a test database
        },
        # "OPTIONS": {
        #     "threaded": True,
        # },
    },
    # "mysql": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "OPTIONS": {
    #         "read_default_file": os.path.join(BASE_DIR, "mysql.cnf"),
    #     },
    # },
    # "{{cookiecutter.project_slug}}": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "{{cookiecutter.project_slug}}",
    #     "USER": os.getenv("{{cookiecutter.project_slug.upper()}}_DB_USER"),
    #     "PASSWORD": os.getenv("{{cookiecutter.project_slug.upper()}}_DB_PASSWORD_FILE"),
    #     "HOST": os.getenv("{{cookiecutter.project_slug.upper()}}_DB_HOST"),
    #     "PORT": os.getenv("{{cookiecutter.project_slug.upper()}}_DB_PORT"),
    # },
}
# set oracle db
try:
    if "oracle" in DATABASES["default"]["ENGINE"]:
        if sys.platform.startswith("win"):
            oracledb.init_oracle_client(lib_dir=DATABASES["default"]["LIB_DIR"])
        else:
            oracledb.init_oracle_client()
except Exception as exc:
    raise DatabaseError(
        "Check Oracle Client library, please set:: LD_LIBRARY_PATH=/pathTo/instantclient"
    ) from exc

# DATABASE_ROUTERS = ["config.routers.DatabaseRouter", "config.routers.AuthRouter"]
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
if DEBUG:
    STATIC_ROOT = "/static"
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]
else:
    # For serving static files in PROD with Django
    STATIC_ROOT = BASE_DIR / "static"
    STATICFILES_DIRS = []

STATIC_URL = "/static/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework_datatables.renderers.DatatablesRenderer",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework_datatables.filters.DatatablesFilterBackend",
    ),
    # "DEFAULT_PAGINATION_CLASS": "rest_framework_datatables.pagination.DatatablesPageNumberPagination",
    # "PAGE_SIZE": 50,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 1000000,
}

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB

AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_LDAP_SERVER_URI = (
    os.getenv("AUTH_LDAP_SERVER_URI") or "ldap://ldaplocal.domain-name.com"
)
AUTH_LDAP_BIND_DN = (
    os.getenv("AUTH_LDAP_BIND_DN")
    or f"CN={os.getenv('LDAP_CN')},OU=Service Accounts,OU=Users,OU=AdminManagement,DC=domain-name,DC=com"
)  # dn for binding
AUTH_LDAP_BIND_PASSWORD = os.getenv("LDAP_PW")
AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
    LDAPSearch(
        "OU=LDAP_OU Users, OU=_LDAP_OU,DC=domain-name,DC=com",
        ldap.SCOPE_SUBTREE,
        "(sAMAccountName=%(user)s)",
    ),  # search for user in dn and all subtrees
    LDAPSearch(
        "OU=General Users,OU=LDAP_OU Users,OU=_LDAP_OU,DC=domain-name,DC=com",
        ldap.SCOPE_SUBTREE,
        "(sAMAccountName=%(user)s)",
    ),
    LDAPSearch(
        "OU=Information Systems,OU=AMT Users,OU=_LDAP_OU,DC=domain-name,DC=com",
        ldap.SCOPE_SUBTREE,
        "(sAMAccountName=%(user)s)",
    ),
    LDAPSearch(
        "OU=External,OU=LDAP_OU Users,OU=_LDAP_OU,DC=domain-name,DC=com",
        ldap.SCOPE_SUBTREE,
        "(sAMAccountName=%(user)s)",
    ),
    LDAPSearch(
        "OU=Remote-Mobile,OU=LDAP_OU Users,OU=_LDAP_OU,DC=domain-name,DC=com",
        ldap.SCOPE_SUBTREE,
        "(sAMAccountName=%(user)s)",
    ),
)
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0,
}
# seach group for user
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "OU=Groups,OU=_LDAP_OU,DC=domain-name,DC=com", ldap.SCOPE_SUBTREE, "(objectClass=*)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

# Set LDAP Authentacion Group
AUTH_LDAP_REQUIRE_GROUP = LDAPGroupQuery(
    "CN=LDAP_OU-DNIR-users,OU=IT-Apps,OU=Security,OU=Groups,OU=LDAP_OU Regional Objects,DC=domain-name,DC=com"
)
# make ldap binding for user only after 3600 s
AUTH_LDAP_CACHE_TIMEOUT = 3600

# find group perms and sync with perms in django admin add or change groupes in django admin for more perms
# AUTH_LDAP_MIRROR_GROUPS = True (mirrors all groups a user is member )
AUTH_LDAP_FIND_GROUP_PERMS = True

# To enable Swagger https api
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
