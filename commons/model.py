# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  2:48 下午
# @Author  : lidong@test.com
# @Site    : 
# @File    : model_type.py
from commons.exceptions import EmptyException, FieldNotDefineException, FieldTypeException


class Field:
    field_type = None

    def __init__(
            self,
            description: str = None,
            required: bool = False,
            serialization_name: str = None,
            deserialization_name: str = None,
            *args,
            **kwargs):
        print("______")
        if description is None:
            raise EmptyException(error_msg="description 必须填写")
        self.description = description
        self.required = required
        self.serialization_name = serialization_name
        self.deserialization_name = deserialization_name

    # def __getattr__(self, item):
    #     if self.serialization_name:
    #         return

    def serialize(self):
        pass

    def deserialize(self):
        pass


class String(Field):
    field_type = str


MODEL_CLASS_DICT = {}


class ModelMeta(type):
    def __init__(cls, name: str, bases: tuple, attrs: dict):
        """

        :param cls: 该子类对象本身(非实例对象)
        :param name: 该子类本身的类的名字
        :param bases: 该子类的继承关系
        :param attrs: 该子类的自身的类对象属性
        """
        # print(cls._description, name, bases, attrs)
        # cls._process_serialization_name(attrs)
        # print(type(cls), type(name), type(bases), type(attrs))
        if name != "ModelBase":
            MODEL_CLASS_DICT[cls._description] = cls
            cls._process_serialization_name(attrs)

    # @staticmethod
    # def _process_serialization_name(attrs):
    #     for field, field_obj in attrs.items():
    #         if field[0] != "_":
    #             if isinstance(field_obj, Field):
    #                 if field_obj.serialization_name is not None:
    #                     attrs[field_obj.serialization_name] = field_obj
    #                     print(attrs)


class ModelBase(metaclass=ModelMeta):
    # class Meta:
    #     name = "a"
    _description = None
    _dict = None

    def __init__(self, params: dict):
        if not self._dict:
            self._dict = dict()
        self.params = params

    def _verify(self):
        for field, value in self.params:
            attrs = getattr(self, field)
            if not attrs:

                raise FieldNotDefineException()
            value_type = attrs.field_type
            if not isinstance(value, value_type):
                raise FieldTypeException()

    @classmethod
    def _process_serialization_name(cls, attrs):
        for field, field_obj in attrs.items():
            if field[0] != "_":
                if isinstance(field_obj, Field):
                    if field_obj.serialization_name is not None:
                        # attrs[field_obj.serialization_name] = field_obj
                        setattr(cls, field_obj.serialization_name, field_obj)
                        # TODO: 处理需要序列化的字段
                        print(attrs)


if __name__ == '__main__':
    pass
