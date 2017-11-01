from .settings import *  # noqa

import os

DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = '10102&qtnhp6_0f=7dl3&3g77@#7@ykw3thwbhvshf%!nnhg)vno*u='

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
