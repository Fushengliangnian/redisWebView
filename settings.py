# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:48
# @Author  : lidong@immusician.com
# @Site    :
# @File    : settings.py
import os


TEMPLATES_PATH = "./templates/"


REDIS_CONFIG = {
    'host': os.environ.get('REDIS_SERVICE_HOST', '127.0.0.1'),
    'port': os.environ.get('REDIS_SERVICE_PORT', 6379)
}
