# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:48
# @Author  : lidong@immusician.com
# @Site    :
# @File    : connections.py

import logging

import aioredis

logger = logging.getLogger('sanic')


class RedisConnectionPool(object):
    REDIS_HOST = None
    REDIS_PORT = None

    def __init__(self, loop=None):
        self.conn = None
        self._loop = loop
        self._pool = None

    async def init(self, config, conn=None):
        if conn:
            self.conn = conn
        self.REDIS_HOST = config["host"]
        self.REDIS_PORT = config["port"]
        self._pool = await aioredis.create_redis_pool('redis://{}:{}'.format(self.REDIS_HOST,
                                                                             self.REDIS_PORT),
                                                      minsize=1, maxsize=5, loop=self._loop)
        return self._pool
