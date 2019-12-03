# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  3:18 下午
# @Author  : lidong@test.com
# @Site    : 
# @File    : exceptions.py
from sanic.handlers import ErrorHandler


class CustomErrorHandler(ErrorHandler):
    """
    # 不使用 Sanic 自带的 Error 处理方式; Sanic的 Error 会展示的在页面上, 效果不是很好, 需要的还是日志形式的 error log 的 存储
    # 文档看错了, 这个很好用
    """
    status_code = None
    message = None

    def default(self, request, exception):
        if isinstance(exception, CustomResponseException):
            res = {"status_code": exception.status_code, "message": exception.message}
            return res
        return super().default(request, exception)

    def response(self, request, exception):
        return self.default(request, exception)


class DefineCodeException(Exception):
    """
    编写过程中的错误 100X
    """
    status_code = 1000


class CustomResponseException(Exception):
    """
    返回前端的错误基类
    """
    status_code = None
    message = None


class FieldVerifyException(CustomResponseException):
    """
    字段校验的错误 200X
    """
    status_code = 2000


class RequestParamException(CustomResponseException):
    """
    用户请求的错误 40X
    """
    status_code = 400


class EmptyException(DefineCodeException):
    def __init__(self, status_code=1001, message="空值错误"):
        self.status_code = status_code
        self.message = message


class FieldNotDefineException(FieldVerifyException):
    def __init__(self, status_code=2001, error_msg="字段未定义"):
        self.status_code = status_code
        self.message = error_msg


class FieldTypeException(FieldVerifyException):
    def __init__(self, status_code=2002, error_msg="字段类型不匹配"):
        self.status_code = status_code
        self.message = error_msg
