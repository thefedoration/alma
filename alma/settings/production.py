from __future__ import absolute_import

from alma.settings.base import *

DEBUG = False



import dj_database_url
DATABASES['default'] =  {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'prod_db.sqlite3'),
}