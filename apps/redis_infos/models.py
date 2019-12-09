# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    :  4:44 下午
# @Author  : lidong@test.com
# @Site    : 
# @File    : models.py
from commons.model import ModelBase, String


class RedisInfoServer(ModelBase):
    _description = "服务相关信息"

    redis_version = String(description="Redis 服务器版本")
    redis_git_sha1 = String(description="Git SHA1")
    redis_git_dirty = String(description="Git dirty flag")
    redis_build_id = String(description="Git dirty flag")
    redis_mode = String(description="运行模式，单机或者集群")
    # TODO: 原名 os, 为了避免冲突, 需要添加 序列化, 反序列化相关操作
    os_sys = String(description="服务器的宿主操作系统", serialization_name="os", deserialization_name="os")
    arch_bits = String(description="架构（32 或 64 位）")
    multiplexing_api = String(description="Redis 所使用的事件处理机制")
    atomicvar_api = String(description="原子处理api")
    gcc_version = String(description="编译 Redis 时所使用的 GCC 版本")
    process_id = String(description="服务器进程的 PID")
    run_id = String(description="Redis 服务器的随机标识符（用于 Sentinel 和集群）")
    tcp_port = String(description="TCP/IP 监听端口")
    uptime_in_seconds = String(description="自 Redis 服务器启动以来，经过的秒数")
    uptime_in_days = String(description="自 Redis 服务器启动以来，经过的天数")
    hz = String(description="edis内部调度（进行关闭timeout的客户端，删除过期key等等）频率，程序规定serverCron每秒运行10次")
    lru_clock = String(description="自增的时钟，用于LRU管理,该时钟100ms(hz=10,因此每1000ms/10=100ms执行一次定时任务)更新一次")
    executable = String(description="执行文件")
    config_file = String(description="配置文件路径")


class RedisInfoClient(ModelBase):
    _description = "客户端连接相关信息"

    connected_clients = String(description="已连接客户端的数量（不包括通过从属服务器连接的客户端）")
    client_longest_output_list = String(description="当前连接的客户端当中，最长的输出列表")
    client_biggest_input_buf = String(description="当前连接的客户端当中，最大输入缓存")
    blocked_clients = String(description="正在等待阻塞命令(BLPOP, BRPOP, BRPOPLPUSH)的客户端的数量")


class RedisInfoMemory(ModelBase):
    _description = "内存相关信息"


class RedisInfoPersistence(ModelBase):
    _description = "持久化相关信息"


class RedisInfoStats(ModelBase):
    _description = "网络状态相关信息"

    total_connections_received = String(description="新创建连接个数,如果新创建连接过多，过度地创建和销毁连接对性能有影响，说明短连接严重或连接池使用有问题，需调研代码的连接设置")
    total_commands_processed = String(description="redis处理的命令数")
    instantaneous_ops_per_sec = String(description="redis当前的qps，redis内部较实时的每秒执行的命令数")
    total_net_input_bytes = String(description="redis网络入口流量字节数")
    total_net_output_bytes = String(description="redis网络出口流量字节数")
    instantaneous_input_kbps = String(description="redis网络入口kps")
    instantaneous_output_kbps = String(description="redis网络出口kps")
    rejected_connections = String(description="拒绝的连接个数，redis连接个数达到maxclients限制，拒绝新连接的个数")
    sync_full = String(description="主从完全同步成功次数")
    sync_partial_ok = String(description="主从部分同步成功次数")
    sync_partial_err = String(description="主从部分同步失败次数")
    expired_keys = String(description="运行以来过期的key的数量")
    expired_stale_perc = String(description="过期的比率")
    expired_time_cap_reached_count = String(description="过期计数")
    evicted_keys = String(description="运行以来剔除(超过了maxmemory后)的key的数量")
    keyspace_hits = String(description="命中次数")
    keyspace_misses = String(description="没命中次数")
    pubsub_channels = String(description="当前使用中的频道数量")
    pubsub_patterns = String(description="当前使用的模式的数量")
    latest_fork_usec = String(description="最近一次fork操作阻塞redis进程的耗时数, 单位微秒")
    migrate_cached_sockets = String(description="是否已经缓存了到该地址的连接")
    slave_expires_tracked_keys = String(description="从实例到期key数量")
    active_defrag_hits = String(description="主动碎片整理命中次数")
    active_defrag_misses = String(description="主动碎片整理未命中次数")
    active_defrag_key_hits = String(description="主动碎片整理key命中次数")
    active_defrag_key_misses = String(description="主动碎片整理key未命中次数")


class RedisInfoReplication(ModelBase):
    _description = "主从集群相关信息"

    role = String(description="实例的角色")
    connected_slaves = String(description="连接的slave实例个数")
    master_replid = String(description="实例的角色")
    master_replid2 = String(description="实例的角色")
    master_repl_offset = String(description="实例的角色")
    second_repl_offset = String(description="实例的角色")
    repl_backlog_active = String(description="实例的角色")
    repl_backlog_size = String(description="实例的角色")
    repl_backlog_first_byte_offset = String(description="实例的角色")
    repl_backlog_histlen = String(description="实例的角色")


class RedisInfoCPU(ModelBase):
    _description = "CPU资源占用相关信息"

    used_cpu_sys = String(description="将所有redis主进程在核心态所占用的CPU时求和累计起来")
    used_cpu_user = String(description="将所有redis主进程在用户态所占用的CPU时求和累计起来")
    used_cpu_sys_children = String(description="将后台进程在核心态所占用的CPU时求和累计起来")
    used_cpu_user_children = String(description="将后台进程在用户态所占用的CPU时求和累计起来")


class RedisInfoCommandStats(ModelBase):
    _description = "命令使用统计快照相关信息"

    cmdstat_set = String(description="Set 命令统计")
    cmdstat_ping = String(description="Ping 命令统计")
    cmdstat_del = String(description="Del 命令统计")
    cmdstat_psync = String(description="Psync 命令统计")
    cmdstat_keys = String(description="Keys 命令统计")
    cmdstat_hmset = String(description="Hmset 命令统计")
    cmdstat_command = String(description="Command 命令统计")
    cmdstat_info = String(description="Info 命令统计")
    cmdstat_replconf = String(description="Replconf 命令统计")
    cmdstat_client = String(description="Client 命令统计")
    cmdstat_hgetall = String(description="Hgetall 命令统计")


class RedisInfoCluster(ModelBase):
    _description = "集群模式相关信息"

    cluster_enabled = String(description="是否启用集群模式")


class RedisInfoKeySpace(ModelBase):
    _description = "...相关信息"

    db0 = String(description="db0的key的数量")
