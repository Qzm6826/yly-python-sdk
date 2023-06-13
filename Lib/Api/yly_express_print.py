#!/usr/bin/python
# -*- coding: utf-8 -*-

class YlyExpressPrint:

    __client = None

    def __init__(self, client):
        self.__client = client

    def index(self, machine_code, content, origin_id, sandbox= 0):
        """
        面单打印接口
        不支持机型: 仅支持K5机型
        :param machine_code: 机器码
        :param content: 面单数据
        :param origin_id: 商户系统内部订单号，要求32个字符内，只能是数字、大小写字母
        :param sandbox: 沙箱环境1  正式环境0
        :return:
        """
        params = {
            'machine_code': machine_code,
            'content': content,
            'origin_id': origin_id,
        }
        if sandbox == 1:
            params['sandbox'] = sandbox


        return self.__client.call('expressprint/index', params)

    def cancel(self, machine_code, content):
        """
        面单取消接口
        :param machine_code: 机器码
        :param content: 面单数据
        :return:
        """

        params = {
            'machine_code': machine_code,
            'content': content,
        }
        return self.__client.call('expressprint/cancel', params)