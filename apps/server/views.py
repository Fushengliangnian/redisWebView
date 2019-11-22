# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  4:43 下午
# @Author  : lidong@test.com
# @Site    :
# @File    : views.py

from sanic.blueprints import Blueprint
from sanic.response import html, json


app = Blueprint("server")


@app.get("/")
async def index(request):
    template = request.app.template.get_template("/index.html")
    redis = request.app.redis
    ret = await redis.info("all")
    print(ret)
    return html(template.render())
