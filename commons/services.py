# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  4:29 下午
# @Author  : lidong@test.com
# @Site    : 
# @File    : services.py


class BaseService:
    def __init__(self, request):
        self.redis = request.app.redis

    def exec(self):
        pass
