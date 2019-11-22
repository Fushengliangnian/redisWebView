# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:49
# @Author  : lidong@immusician.com
# @Site    :
# @File    : utils.py
import os

from sanic.config import Config


def load_setting():
    conf = Config()
    module = os.environ.get('SANIC_SETTINGS_MODULE', 'settings')
    path = '%s.py' % module.replace('.', '/')
    conf.from_pyfile(path)
    return conf


if __name__ == '__main__':
    print(load_setting())
