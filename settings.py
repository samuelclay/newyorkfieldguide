import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


# ===========
# = Globals =
# ===========

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Samuel CLay', 'samuel@ofbrooklyn.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/New_York' # Obviously
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
MEDIA_ROOT = here('media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
ROOT_URLCONF = 'urls'

if not DEBUG:
    PREPEND_WWW = True
    APPEND_SLASH = True
    
# ============
# = Database =
# ============

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'fieldguide'
DATABASE_USER = 'fieldguide'
DATABASE_PASSWORD = ''
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''


# ======================
# = Django Integration =
# ======================

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_DIRS = (
    here('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django_extensions',
    'tagging',
    'posts',
    'compress',
    'syncr.flickr',
)


# ================
# = Static Media =
# ================

COMPRESS_VERSION = True
COMPRESS_CSS_FILTERS = None

COMPRESS_CSS = {
    'global': {
        'source_filenames': (
            'css/reset.css',
            'css/type.css',
            'css/global.css',
        ),
        'output_filename': 'css/global.r?.css',
    },
}

COMPRESS_JS = {
    'common': {
        'source_filenames': (
            'js/jquery-1.4.2.js',
            'js/jquery.easing-1.3.js',
            'js/pngfix.js',
            'js/fieldguide_global.js',
        ),
        'output_filename': 'js/common.r?.js',
    },
}

# ==================
# = Configurations =
# ==================

from local_settings import *

COMPRESS = not DEBUG
