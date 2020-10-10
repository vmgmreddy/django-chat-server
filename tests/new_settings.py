# Import socket to read host name
import socket

# If the host name starts with 'live', DJANGO_HOST = "production"
if socket.gethostname().startswith('live'):
    DJANGO_HOST = "production"
# Else if host name starts with 'test', set DJANGO_HOST = "test"
elif socket.gethostname().startswith('test'): 
    DJANGO_HOST = "testing"
else:
# If host doesn't match, assume it's a development server, set DJANGO_HOST = "development"
    DJANGO_HOST = "development"

# Define general behavior variables for DJANGO_HOST and all others
if DJANGO_HOST == "production":
    DEBUG = False
    STATIC_URL = 'http://static.coffeehouse.com/'
else:
    DEBUG = True
    STATIC_URL = '/static/'

# Define DATABASES variable for DJANGO_HOST and all others
if DJANGO_HOST == "production":
   # Use mysql for live host
   DATABASES = {
    'default': {
        'NAME': 'housecoffee',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'coffee',
        'PASSWORD': 'secretpass'
    }
  }
else: 
   # Use sqlite for non live host
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'coffee.sqlite3'),
    }
  }

# Define EMAIL_BACKEND variable for DJANGO_HOST
if DJANGO_HOST == "production":
    # Output to SMTP server on DJANGO_HOST production
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
elif DJANGO_HOST == "testing":
    # Nullify output on DJANGO_HOST test
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
else: 
    # Output to console for all others
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Define CACHES variable for DJANGO_HOST production and all other hosts 
if DJANGO_HOST == "production":
   # Set cache
   CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT':'1800',
            }
        }
   CACHE_MIDDLEWARE_SECONDS = 1800
else: 
   # No cache for all other hosts
   pass
