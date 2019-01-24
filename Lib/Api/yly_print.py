#!/usr/bin/python
# -*- coding: utf-8 -*-

class YlyPrint:

    __client = None

    def __init__(self, client):
        self.__client = client

    def index(self, machine_code, content, origin_id):
        """
        打印接口
        :param machine_code: 机器码
        :param content: 打印内容
        :param origin_id: 商户系统内部订单号，要求32个字符内，只能是数字、大小写字母
        :return:
        """
        params = {
            'machine_code': machine_code,
            'content': content,
            'origin_id': origin_id
        }
        return self.__client.call('print/index', params)
