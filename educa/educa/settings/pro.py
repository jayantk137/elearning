
from .base import *

DEBUG =False

ADMINS = (
    ('Jayant kumar','jayantk137@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'jayantk137',

    }
}