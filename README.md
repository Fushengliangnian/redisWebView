# redisWebView
针对redis的Web版图形界面

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
