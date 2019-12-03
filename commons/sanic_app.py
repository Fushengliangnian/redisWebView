# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:50
# @Author  : lidong@immusician.com
# @Site    :
# @File    : common.py
import asyncio
import gzip

from sanic import Sanic
from sanic.response import html, json
from jinja2 import Environment, FileSystemLoader, select_autoescape

from commons.utils import load_setting
from commons.connections import RedisConnectionPool
from commons.exceptions import CustomErrorHandler

__all__ = ["app"]

app = Sanic(__name__)
app.config = load_setting()
app.template = Environment(
    loader=FileSystemLoader(app.config["TEMPLATES_PATH"]),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=False
)
app.static("/static", "./static")
app.error_handler = CustomErrorHandler()


@app.listener('before_server_start')
async def before_server_start(app, loop):
    queue = asyncio.Queue()
    app.queue = queue
    app.redis = await RedisConnectionPool(loop=loop).init(app.config['REDIS_CONFIG'])


@app.middleware("response")
async def gzip_response(request, response):
    if isinstance(response, dict):
        response = json(response)
        response.headers["Content-Type"] = "application/json"
    if isinstance(response, str):
        response = html(response)

    response.headers["Content-Encoding"] = "gzip"
    response.body = gzip.compress(response.body)
    return response
