# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  4:43 下午
# @Author  : lidong@test.com
# @Site    :
# @File    : views.py

from sanic.blueprints import Blueprint
from commons.exceptions import FieldTypeException
from commons.utils import render


app = Blueprint("server")


@app.get("/")
async def index(request):
    redis = request.app.redis
    ret = await redis.info("all")
    # raise FieldTypeException()
    # raise Exception()
    return await render(request, "/index.html", ret=ret)
