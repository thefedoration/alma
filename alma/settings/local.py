from __future__ import absolute_import

from alma.settings.base import *

DEBUG = True

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import dj_database_url
DATABASES['default'] =  {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
# DATABASES['default'] =  dj_database_url.config()