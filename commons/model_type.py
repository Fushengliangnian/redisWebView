# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  2:48 下午
# @Author  : lidong@test.com
# @Site    : 
# @File    : model_type.py
from commons.exceptions import EmptyException

MODEL_CLASS_DICT = {}


class ModelMeta(type):
    def __init__(cls, name: str, bases: tuple, attrs: dict):
        """

        :param cls: 该子类对象本身(非实例对象)
        :param name: 该子类本身的类的名字
        :param bases: 该子类的继承关系
        :param attrs: 该子类的自身的类对象
        """
        # print(cls, name, bases, attrs)
        # print(type(cls), type(name), type(bases), type(attrs))
        if name != "ModelBase":
            MODEL_CLASS_DICT[attrs["description"]] = cls


class ModelBase(metaclass=ModelMeta):
    # class Meta:
    #     name = "a"
    description = None


class Field:
    def __init__(self, description: str = None, required: bool = False, *args, **kwargs):
        if description is None:
            raise EmptyException(error_msg="description 必须填写")
        self.description = description
        self.required = required


class String(Field):
    pass
