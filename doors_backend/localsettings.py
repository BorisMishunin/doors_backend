# -*- coding: utf-8 -*-

import os
import json
import logging
from datetime import date

from .settings import *

try:
    DATABASES = json.load(open(os.environ['GOODS_DB_CONFIG']))
except Exception, e:
    logging.exception(e)


# Loggers
try:
    LOGGING = json.load(open(os.environ['DOORS_LOGGERS']))
except Exception, e:
    logging.exception(str(os.environ))