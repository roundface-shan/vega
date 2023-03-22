# coding:utf-8

from db.mongo_db import client
from bson.objectid import ObjectId


class MongoNewDao:
    # 添加新闻正文记录
    def insert(self, title, content):
        try:
            client.vega.news.insert_one({"title": title, "content": content})
        except Exception as e:
            print(e)

    # 查找新闻正文的主键值
    def search_id(self, title):
        try:
            news = client.vega.news.find_one({"title": title})
            return str(news["_id"])
        except Exception as e:
            print(e)

    # 修改新闻正文
    def update(self, id, title, content):
        try:
            client.vega.news.update_one({"_id": ObjectId(id)}, {"$set": {"title": title, "content": content}})
        except Exception as e:
            print(e)

    # 根据id查找内容
    def search_content_by_id(self, id):
        try:
            news = client.vega.news.find_one({"_id": ObjectId(id)})
            return news["content"]
        except Exception as e:
            print(e)

    # 删除新闻
    def delete_by_id(self, id):
        try:
            client.vega.news.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            print(e)
