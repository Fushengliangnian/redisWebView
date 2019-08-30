# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:49
# @Author  : lidong@immusician.com
# @Site    :
# @File    : views.py
from sanic.response import html, json

from common import app


@app.get("/")
async def index(request):
    template = request.app.template.get_template("/index.html")
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
    template = request.app.template.get_template("/allKeys.html")
    return html(template.render(data=[{"key": "redis-key", "type": "hash", "size": 10, "details": "1"}]))


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
