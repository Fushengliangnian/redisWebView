# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:49
# @Author  : lidong@immusician.com
# @Site    :
# @File    : views.py

import ujson
from sanic.response import html, json

from common import app


@app.get("/")
async def index(request):
    template = request.app.template.get_template("/index.html")
    redis = request.app.redis
    ret = await redis.info()
    print(ret)
    return html(template.render())


@app.route("/login", methods=["GET", "POST"])
async def login(request):
    print(request.form)
    if request.method == "GET":
        print(request.method)
        template = request.app.template.get_template("/login.html")
        return html(template.render())
    return json({})


@app.get("/all_keys/<db:int>")
async def all_keys(request, db):
    redis = request.app.redis

    _type_dict = {
        b"hash": redis.hgetall,
        b"zset": redis.zrange,
        b"list": redis.lrange,
        b"set": redis.smembers,
        b"string": redis.get,
    }
    data = []
    all_keys = await redis.keys("*")
    print(all_keys)
    # calls = [redis.type(key) for key in all_keys]
    # ret = await asyncio.gather(*calls)
    for key in all_keys:
        key_type = await redis.type(key)
        func = _type_dict[key_type]
        if key_type in (b"list", b"zset"):
            values = await func(key, 0, -1)
        else:
            values = await func(key)

        # json_value = ujson.dumps(values.decode("utf-8")) if key_type == b"string" else ujson.dumps(values)
        str_value = str(values)
        size = len(str_value)

        data.append({"key": key.decode("utf8"), "type": key_type.decode("utf8"), "details": str_value[0: 50], "size": size})
    print(data)
    template = request.app.template.get_template("/allKeys.html")
    # return html(template.render(data=[{"key": "redis-key", "type": "hash", "size": 10, "details": "1"}]))
    return html(template.render(data=data))


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
