from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'STORAGE_ENGINE': 'INNODB',
        'NAME': 'sarendsen_shop',                      # Or path to database file if using sqlite3.
        'USER': 'sarendsen_shop',                      # Not used with sqlite3.
        'PASSWORD': '127608fa',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS = settings.INSTALLED_APPS + ('debug_toolbar',)

WSGI_APPLICATION = 'exampleshop.wsgi.application'