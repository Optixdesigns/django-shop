# Django project settings for localhost
import os, sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Webmaster', 'webmaster@localhost'),
)

MANAGERS = ADMINS

SITE_ID = 1
SITE_NAME = "Keith Haring"
SITE_DESCRIPTION = "Welcome to our"
SITE_KEYWORDS = ""
SITE_URL = 'http://localhost'
SITE_ROOT = os.path.abspath(os.path.dirname(__file__))
POWERED_BY = "Optixdesigns"
POWERED_BY_EMAIL = 'info@optixdesigns.com'

# Add our project app directory
sys.path.insert(0, os.path.join(SITE_ROOT, "apps"))

INTERNAL_IPS = ('127.0.0.1',)
HOSTNAME = 'localhost'

DEFAULT_FROM_EMAIL = '"Webmaster" <Webmaster@localhost>'
SERVER_EMAIL = '"Webmaster" <Webmaster@localhost>'

DATABASES = {
    'default': {
        # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'STORAGE_ENGINE': 'INNODB',
        'NAME': 'shop',
        'USER': 'shop',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3!sa61^q6jsvv-g1e!!@g$3js=qjdq)a4hizw0x-h)qnqg$-oq'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl_NL'

USE_I18N = True
USE_L10N = True

# Django timezone-aware datetimes.
USE_TZ = True

USE_ETAGS = True

MEDIA_ROOT = os.path.join(SITE_ROOT, '../media/')
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
  'hamlpy.template.loaders.HamlPyFilesystemLoader',
  'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'shop.cart.middleware.CartMiddleware',
    'shop.middleware.ShopMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  # default template context processors
  'django.core.context_processors.request',
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  # load system information for use in templates
  'context_processors.site_settings',
  #'shop.cart.context_processors.cart',
  'shop.context_processors.shop',
 )

#WSGI_APPLICATION = 'exampleshop.wsgi.application'

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates/'),
)

INSTALLED_APPS = (
    # Django specific
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.flatpages',
    
    # 3rd Party
    'sorl.thumbnail',
    'taggit',
    'south',
    'collector',
    'pagination',
    'mptt',
    #'rollyourown.seo',
    'tinymce',
    'djutils',
    'polymorphic', # We need polymorphic installed for the shop
    'share',
    #'nuggets',
    #'ajax_forms',
    'ajax_validation',
    'bootstrapform',

    'odin',
    'shop',
    'shop.product',
    'shop.order',
    'shop.cart',
    'shop.category',
    #'shop.attributes',
    
    #'exampleshop',

    # HUB apps
    'hub.core',
    #'hub.node',
    #'hub.categories',

    # Project Apps
    'core',
    'profiles',
    'articles',
    'products',
    'categories',
)

AUTH_PROFILE_MODULE = "profiles.Profile"

# Overide default shop moels
SHOP_PRODUCT_MODEL = 'products.models.Product'
SHOP_VARIANT_MODEL = 'products.models.Variant'
SHOP_CATEGORY_MODEL = 'categories.models.ProductCategory'
#SHOP_CART_MODIFIERS = ['shop_simplevariations.cart_modifier.ProductOptionsModifier',]

# TinyMCE
TINYMCE_JS_URL = os.path.join(MEDIA_URL + 'js/tiny_mce/tiny_mce.js')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'propagate': True,
        },
    }
}

if DEBUG == True:
  INSTALLED_APPS = INSTALLED_APPS + ('django.contrib.staticfiles',)
  
try:
    from settings_local import *
except ImportError:
    pass