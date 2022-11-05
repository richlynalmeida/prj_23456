"""
Django settings for prj23456 project.

Based on by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import moneyed
from decimal import ROUND_HALF_EVEN

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fa76dcc8-317f-48e2-8250-a1f3562d9d27'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'djmoney',
    'jazzmin',
    # 'admin_interface',
    # 'colorfield',
    # General use templates & template tags (should appear first)
    # 'adminlte3',
    # Optional: Django admin theme (must be before django.contrib.admin)
    # 'adminlte3_theme',
    # 'grappelli',
    # 'nested_admin',
    # 'viewtable',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 'django_hstore',
    # 'django.contrib.postgres',
    # CAMEOSE Solutions Ltd. Apps (Start)
    'csl',  # Home
    'a_hr',
    'b_wbs',
    'b_benchmarking',
    'c_project_calendar',
    'd_mm',
    'e_commodities',
    'f_contracts',
    'f_finance',
    'g_measures',
    'h_schedules',
    'i_eb',
    'j_cb',
    'k_quantum',
    'l_actuals',
    'm_claims',
    'n_knowledgebase',
    'r_risk',
    # 's_sandbox',
    'v_viewsdbo',
    # CAMEOSE Solutions Ltd. Apps (End)
    'phone_field',
    'phonenumber_field',
]

# only if django version >= 3.0 for django-admin-interface
# X_FRAME_OPTIONS = 'SAMEORIGIN'
# SILENCED_SYSTEM_CHECKS = ['security.W019']

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prj23456.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'prj23456.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': '-c search_path=dbo'
        },
        # 'NAME': 'prj_12345_pg',
        'NAME': 'prj_23456_pg',
        # 'NAME': 'postgres',
        'USER': 'cameose_superuser',
        'PASSWORD': 'cameose_superuser_2022$',
        # 'HOST': '34.83.227.208',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'OPTIONS': {
#             'options': '-c search_path=dbo'
#         },
#         'NAME': 'CSL_D_PG_22',
#         'USER': 'csl_developer',
#         'PASSWORD': 'AVNS_bWMfUfdCSIwsRF-',
#         'HOST': 'db-postgresql-sfo2-96017-do-user-11298491-0.b.db.ondigitalocean.com',
#         'PORT': '25060',
#     }
# }

# SQLServer
# Unable to migrate properly with Django v 3.1 and higher, need to Roll back to Django 3.0.14 or 2.2.28, migrate and
# then upgrade Django again
# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django_pyodbc',
#         # 'ENGINE': 'sql_server.pyodbc',
#         # 'ENGINE': 'django.db.backends.mssql',
#         'ENGINE': 'mssql',
#         'NAME': 'd_js1_a',
#         # 'NAME': 'bhp_n3sr',
#         # 'NAME': 'bhp_js1',
#         # 'NAME': 'CSL_D_SS_12345',
#         # 'NAME': 'CSL_D_SS_54321',
#         'USER': 'cameose_developer',
#         'PASSWORD': 'cameose_developer',
#         # 'HOST': 'localhost',
#         'HOST': 'JANL0084\SQLEXPRESS',
#         # 'HOST': '216.197.202.178',
#         # 'HOST': '172.28.192.1',
#         'PORT': '',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         },
#     },
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False
USE_THOUSAND_SEPARATOR = True

# djmoney
# CURRENCIES = ('USD', 'CAD')
# CURRENCY_CHOICES = [('USD', 'USD$'), ('CAD', 'CAD$')]
CURRENCIES = 'CAD'
CURRENCY_CHOICES = [('CAD', 'CA$')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIAFILES_DIRS = os.path.join(BASE_DIR, 'media')

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    'site_title': 'Project 12345',

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    'site_header': 'Project 12345',

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    'site_brand': 'Project 12345',

    # Logo to use for your site, must be present in static files, used for brand on top left
    'site_logo': 'CAMEOSE/Images/sigma.png',

    # CSS classes that are applied to the logo above
    'site_logo_classes': 'img-square',

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    'site_icon': 'CAMEOSE/Images/sigma.png',

    # Welcome text on the login screen
    'welcome_sign': 'Project 12345 in SQLServer',

    # Copyright on the footer
    'copyright': 'CAMEOSE Solutions Ltd',

    # The model admin to search from the search bar, search bar omitted if excluded
    'search_model': 'auth.User',

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    'user_avatar': None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        # {'name': 'Home', 'url': 'admin:index', 'permissions': ['auth.view_user']},
        # {'name': 'Home',  'url': 'csl:home', 'permissions': ['auth.view_user']},        

        {'name': 'Home Page', 'url': 'http://127.0.0.1:8000/', 'permissions': ['auth.view_user']},

        # external url that opens in a new window (Permissions can be added)
        {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},

        # model admin to link to (Permissions checked against model)
        {'model': 'auth.User'},

    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    'usermenu_links': [
        {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
        {'model': 'auth.user'}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': False,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # 'order_with_respect_to': ['a_hr', 'b_wbs', 'c_project_calendar', 'd_mm', 'e_commodities', 'f_contracts',
    #                           'g_measures', 'h_schedules', 'i_eb', 'j_cb', 'k_quantum', 'l_actuals', 'm_claims',
    #                           'r_risk', 'f_finance', ],

    # Custom links to append to app groups, keyed on app name
    'custom_links': {
        'books': [{
            'name': 'Make Messages',
            'url': 'make_messages',
            'icon': 'fas fa-comments',
            'permissions': ['books.view_book']
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },
    # Icons that are used when one is not manually specified
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    'related_modal_active': False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    'custom_css': None,
    'custom_js': None,
    # Whether to show the UI customizer on the sidebar
    'show_ui_builder': False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    'changeform_format': 'horizontal_tabs',
    # override change forms on a per modeladmin basis
    'changeform_format_overrides':
        {'auth.user': 'collapsible',
         'auth.group': 'vertical_tabs'
         },
    # Add a language dropdown into the admin
    'language_chooser': False,
}