# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  2:37 下午
# @Author  : lidong@test.com
# @Site    : 
# @File    : models.py
from commons.model_type import ModelBase


class RedisInfoServer(ModelBase):
    description = "服务相关信息"


class RedisInfoClient(ModelBase):
    description = "客户端连接相关信息"


class RedisInfoMemory(ModelBase):
    description = "内存相关信息"


class RedisInfoPersistence(ModelBase):
    description = "持久化相关信息"


class RedisInfoStats(ModelBase):
    description = "网络状态相关信息"


class RedisInfoReplication(ModelBase):
    description = "主从集群相关信息"


class RedisInfoCPU(ModelBase):
    description = "CPU处理命令统计相关信息"


class RedisInfoCommandStats(ModelBase):
    description = "命令使用统计快照相关信息"


class RedisInfoCluster(ModelBase):
    description = "集群模式相关信息"


class RedisInfoKeySpace(ModelBase):
    description = "...相关信息"
