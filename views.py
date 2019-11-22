# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:49
# @Author  : lidong@immusician.com
# @Site    :
# @File    : views.py

from sanic.response import html, json

from commons.common import app


@app.get("/")
async def index(request):
    template = request.app.template.get_template("/index.html")
    redis = request.app.redis
    ret = await redis.info("all")
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
    keys = await redis.keys("*")

    for key in keys:
        key_type = await redis.type(key)
        func = _type_dict[key_type]
        if key_type in (b"list", b"zset"):
            values = await func(key, 0, -1)
        else:
            values = await func(key)

        str_value = str(values)
        size = len(str_value)

        data.append({
            "key": key.decode("utf8"),
            "type": key_type.decode("utf8"),
            "details": str_value[0: 50],
            "size": size
        })
    template = request.app.template.get_template("/allKeys.html")
    return html(template.render(data=data))


@app.get("/version/info")
def version_info(request):
    return {}


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
