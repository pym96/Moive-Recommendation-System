# -*- codeing = utf-8 -*-
# 

# 2/15 15:31
# 
# @File :response.py
from base.code import ResponseCode

# 这个封装了返回信息的一个类
class ResMsg(object):
    """
    封装相应文本
    """

    def __init__(self, data=None, code=ResponseCode.SUCCESS,
                 msg=ResponseCode.SUCCESS):
        self._data = data
        self._msg = msg
        self._code = code

    # 使用这个方法来设置返回的状态码、数据和响应信息
    def update(self, code=None, data=None, msg=None):
        """
              更新默认响应文本
              :param code:响应状态码
              :param data: 响应数据
              :param msg: 响应消息
              :return:
              """
        if code is not None:
            self._code = code
        if data is not None:
            self._data = data
        if msg is not None:
            self._msg = msg

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name is not None and value is not None:
            self.__dict__[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        body["data"] = body.pop("_data")
        body["msg"] = body.pop("_msg")
        body["code"] = body.pop("_code")
        return body
