# coding:utf-8

from db.role_dao import RoleDao


class RoleService:
    __role_dao = RoleDao()
    # 查询角色列表
    def search_role_list(self):
        result = self.__role_dao.search_role_list()
        return result
