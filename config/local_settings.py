import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '(isdfwetyr4wdsawd35346w!lr%g^i7qxwdsa%sawdsad!rghe#g5ads3_m7ffawdsdawdsda567567frgf'

DEBUG = True

ALLOWED_HOSTS = ["*"]


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR,]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movie',
        'USER': 'vanich',
        'PASSWORD': 'treker123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}