# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-29 17:47
# @Author  : lidong@immusician.com
# @Site    :
# @File    : main.py

from views import app


def main():
    app.run("0.0.0.0", debug=True)


if __name__ == '__main__':
    main()
