# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:47
# @Author  : lidong@immusician.com
# @Site    :
# @File    : main.py

from commons.sanic_app import app
from apps.server.views import app as server_blueprint
from apps.redis_infos.views import app as info_blueprint


def main():
    app.blueprint(server_blueprint)
    app.blueprint(info_blueprint)
    app.run("0.0.0.0", debug=True)


if __name__ == '__main__':
    main()
