DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emcad',
        'USER': 'emcaddbu',
        'PASSWORD': 'bUD7yfAdRr',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = 'http://media.emcad.ca/'
