# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  3:18 下午
# @Author  : lidong@test.com
# @Site    : 
# @File    : exceptions.py


class EmptyException(Exception):
    def __init__(self, status_code=1001, error_msg="空值错误"):
        self.status_code = status_code
        self.error_msg = error_msg
