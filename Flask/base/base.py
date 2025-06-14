# -*- codeing = utf-8 -*-
# 

# 2/16 10:11
# 
# @File :base.py

from flask import request, current_app
from sqlalchemy import inspect

# 这个文件暂时没用到
class BaseParse(object):
    """
    识别要查询的字段
    """
    __model__ = None
    __request__ = request
    by = frozenset(['by'])
    query = frozenset(['gt', 'ge', 'lt', 'le', 'ne', 'eq', 'ic', 'ni', 'in'])

    def __init__(self):
        self._operator_funcs = {
            'gt': self.__gt_model,
            'ge': self.__ge.model,
            'lt': self.__lt_model,
            'le': self.__le_model,
            'ne': self.__ne_model,
            'eq': self.__eq_model,
            'ic': self.__ic_model,
            'ni': self.__ni_model,
            'by': self.__by_model,
            'in': self.__in_model,
        }

    def _parse_page_size(self):
        """
        获取页码和获取每页数据量
        :return: page 页码
             page_size 每页数据量
        """
        default_page = current_app.config['DEFAULT_PAGE_INDEX']
        default_size = current_app.config['DEFAULT_PAGE_SIZE']

        page = self.__request__.args.get("page", default_page)
        page_size = self.__request__.args.get("size", default_size)
        page = int(page) - 1
        page_size = int(page_size)
        return page, page_size

    def _parse_query_field(self):
        """
        解析查询字段
        :return: query_field 查询字段
                 by_field 排序字段
        """
        args = self.__request__.args
        query_field = list()
        by_field = list()
        for query_key, query_value in args.items():
            key_split = query_key.split('_', 1)
            if len(key_split) != 2:
                continue
            operator, key = key_split
            if not self._check_key(key=key):
                continue
            if operator in self.query:
                data = self._operator_funcs[operator](key=key, value=query_value)
                query_field.append(data)
            elif operator in self.by:
                data = self._operator_funcs[operator](key=key, value=query_value)
                by_field.append(data)
        return query_field, by_field

    def _parse_create_field(self):
        """
                检查字段是否为model的字段,并过滤无关字段.
                1.list(dict) => list(dict)
                2. dict => list(dict)
                :return:
                """
        obj = self.__request__.get_json(force=True)
        if isinstance(obj, list):
            create_field = list()
            for item in obj:
                if isinstance(item, dict):
                    base_dict = self._parse_field(obj=item)
                    create_field.append(base_dict)
            return create_field
        elif isinstance(obj, dict):
            return [self._parse_field(obj=obj)]
        else:
            return list()

    def _parse_field(self, obj=None):
        """
               检查字段模型中是否有，并删除主键值
               :param obj:
               :return:
               """
        obj = obj if obj is not None else self.__request__.get_json(force=True)
        field = dict()
        # 获取model主键字段
        primary_key = map(lambda x: x.name, inspect(self.__model__).primary_key)

        for key, value in obj.items():
            if key in primary_key:
                continue
            if self._check_key(key):
                field[key] = value
        return field

    def _check_key(self, key):
        """
               检查model是否存在key
               :param key:
               :return:
               """
        if hasattr(self.__model__, key):
            return True
        else:
            return False

    def __gt_model(self, key, value):
        """
        大于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) > value

    def __ge_model(self, key, value):
        """
        大于等于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) > value

    def __lt_model(self, key, value):
        """
        小于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) < value

    def __le_model(self, key, value):
        """
        小于等于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) <= value

    def __eq_model(self, key, value):
        """
        等于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) == value

    def __ne_model(self, key, value):
        """
        不等于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) != value

    def __ic_model(self, key, value):
        """
        包含
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key).like('%{}%'.format(value))

    def __ni_model(self, key, value):
        """
        不包含
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key).notlike('%{}%'.format(value))

    def __by_model(self, key, value):
        """
        :param key:
        :param value: 0:正序,1:倒序
        :return:
        """
        try:
            value = int(value)
        except ValueError as e:
            # logger.error(e)
            return getattr(self.__model__, key).asc()
        else:
            if value == 1:
                return getattr(self.__model__, key).asc()
            elif value == 0:
                return getattr(self.__model__, key).desc()
            else:
                return getattr(self.__model__, key).asc()

    def __in_model(self, key, value):
        """
        查询多个相同字段的值
        :param key:
        :param value:
        :return:
        """
        value = value.split('|')
        return getattr(self.__model__, key).in_(value)

