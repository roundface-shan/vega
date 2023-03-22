# coding:utf-8

import redis


try:
    pool = redis.ConnectionPool(
        host="localhost",
        port=6379,
        password="del159963",
        db=1,
        max_connections=50
    )
except Exception as e:
    print(e)