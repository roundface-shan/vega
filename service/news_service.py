# coding:utf-8

from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao
from db.mongo_news_dao import MongoNewDao


class NewsService:
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()
    __mongo_news_dao = MongoNewDao()

    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    # 查询待审批新闻列表的总页数
    def search_unreview_count_page(self):
        result = self.__news_dao.search_unreview_count_page()
        return result

    # 审批新闻
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    # 查询所有的新闻列表
    def search_all_list(self, page):
        result = self.__news_dao.search_all_list(page)
        return result

    # 查询全部新闻列表的总页数
    def search_all_count_page(self):
        result = self.__news_dao.search_all_count_page()
        return result

    # 删除新闻
    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)
        content_id = self.__news_dao.search_content_id(id)
        self.__mongo_news_dao.delete_by_id(content_id)

    # 添加新闻
    def insert(self, title, editor_id, type_id, content, is_top):
        self.__mongo_news_dao.insert(title, content)
        content_id = self.__mongo_news_dao.search_id(title)
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)

    # 查找用于缓存的记录
    def search_cache(self, id):
        result = self.__news_dao.search_cache(id)
        return result

    # 向Redis保存缓存数据
    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_news_dao.insert(id, title, username, type, content, is_top, create_time)

    # 删除缓存的新闻：
    def delete_cache(self, id):
        self.__redis_news_dao.delete_cache(id)

    # 根据id查找新闻：
    def seacher_by_id(self, id):
        result = self.__news_dao.seacher_by_id(id)
        return result

    # 更改新闻
    def update(self, id, title, type_id, content, is_top):
        content_id = self.__news_dao.search_content_id(id)
        self.__mongo_news_dao.update(content_id, title, content)
        self.__news_dao.update(id, title, type_id, content_id, is_top)
        self.__redis_news_dao.delete_cache(id)

    # 根据id查找内容
    def search_content_by_id(self, id):
        content = self.__mongo_news_dao.search_content_by_id(id)
        return content




# test = NewsService()
# test_2 = test.search_unreview_count_page()
# print(test_2)