# redisWebView
针对redis的Web版图形界面

# Quickstart
```
# 安装第三方包, 推荐使用虚拟环境 virtualenv 或者 venv
pip install -r requirements.txt

# 创建新的app
/bin/bash  /Users/lidong/opt/redisWebView/scripts/create_app.sh app_name
```

# Question:
- model 是否选用schematics

# Stack:
- python:3.6+
- bootstrap:4
- redis
- sanic
- docker

# Version:
**0.0.1**
- 支持页面配置进行连接redis
- 支持查看redis服务状态
- 支持查看每个db中存储的数据信息, 大小, 数据类型
- 支持每个db中根据关键字查询 key or value
- docker打包

# Expectation:
- 可配置的用户权限系统
- 对redis的增删改操作
- 定时轮寻redis的状态
- 监听redis中值的变化
- 存储redis中 value 的历史变化
- 页面的优化
- 项目整体的可配置化, 对其他框架也做兼容
- **逻辑尽量全部写在service里**, **view里只做数据的校验**, 先适用 F 后期在配置化的时候决定用 F or C

