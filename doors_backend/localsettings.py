# -*- coding: utf-8 -*-

import os
import json
import logging
from datetime import date

from .settings import *
from .social_auth import *




services = {
    'doors_goods_service': os.environ['DOORS_SERVICE_GOODS'],
    'doors_marketplace_service': os.environ['DOORS_SERVICE_MARKETPLACE']
}

try:
    DATABASES = json.load(open(os.environ['GOODS_DB_CONFIG']))
except Exception, e:
    logging.exception(e)


# Loggers
try:
    LOGGING = json.load(open(os.environ['DOORS_LOGGERS']))
except Exception, e:
    logging.exception(str(os.environ))


#Social auth

