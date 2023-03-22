# coding:utf-8

from db.type_dao import TypeDao


class TypeService:
    __type_dao = TypeDao()
    # 查询新闻类型
    def search_type_list(self):
        result = self.__type_dao.search_type_list()
        return result
