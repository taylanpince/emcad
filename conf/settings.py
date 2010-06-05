DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emcad',
        'USER': 'emcaddbu',
        'PASSWORD': 'FicC0wa1Pv',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = 'http://media.emcad.ca/'

INTERNAL_IPS = (
    '127.0.0.1',
)
