# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:50
# @Author  : lidong@immusician.com
# @Site    :
# @File    : common.py
import asyncio

from sanic import Sanic
from jinja2 import Environment, FileSystemLoader, select_autoescape

from utils import load_setting
from connections import RedisConnectionPool

__all__ = ["app"]

app = Sanic(__name__)
app.config = load_setting()
app.template = Environment(
    loader=FileSystemLoader(app.config["TEMPLATES_PATH"]),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=False
)
app.static("/static", "./static")


@app.listener('before_server_start')
async def before_server_start(app, loop):
    queue = asyncio.Queue()
    app.queue = queue
    app.redis = await RedisConnectionPool(loop=loop).init(app.config['REDIS_CONFIG'])
