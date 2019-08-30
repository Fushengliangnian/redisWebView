# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:50
# @Author  : lidong@immusician.com
# @Site    :
# @File    : common.py
from sanic import Sanic
from jinja2 import Environment, FileSystemLoader, select_autoescape
from settings import TEMPLATES_PATH

__all__ = ["app"]

app = Sanic(__name__)
app.template = Environment(
    loader=FileSystemLoader(TEMPLATES_PATH),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=False
)
app.static("/static", "./static")
app.static("/static/img/progress.gif", "./static/img/1.jpg")
