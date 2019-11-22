# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  3:18 下午
# @Author  : lidong@test.com
# @Site    : 
# @File    : exceptions.py


class DefineCodeException(Exception):
    """
    编写过程中的错误 100X
    """
    status_code = 1000


class FieldVerifyException(Exception):
    """
    字段校验的错误 200X
    """
    status_code = 2000


class RequestParamException(Exception):
    """
    用户请求的错误 40X
    """
    status_code = 400


class EmptyException(DefineCodeException):
    def __init__(self, status_code=1001, error_msg="空值错误"):
        self.status_code = status_code
        self.error_msg = error_msg


class FieldNotDefineException(FieldVerifyException):
    def __init__(self, status_code=2001, error_msg="字段未定义"):
        self.status_code = status_code
        self.error_msg = error_msg


class FieldTypeException(FieldVerifyException):
    def __init__(self, status_code=2002, error_msg="字段类型不匹配"):
        self.status_code = status_code
        self.error_msg = error_msg
