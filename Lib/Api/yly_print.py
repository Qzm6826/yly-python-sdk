#!/usr/bin/python
# -*- coding: utf-8 -*-

class YlyPrint:

    __client = None

    def __init__(self, client):
        self.__client = client

    def index(self, machine_code, content, origin_id, idempotence= 0):
        """
        打印接口
        :param machine_code: 机器码
        :param content: 打印内容
        :param origin_id: 商户系统内部订单号，要求32个字符内，只能是数字、大小写字母
        :param idempotence 默认1，传入本参数，会根据origin_id进行幂等处理，2小时内相同origin_id会返回上一次的结果
        :return:
        """
        params = {
            'machine_code': machine_code,
            'content': content,
            'origin_id': origin_id
        }
        if idempotence == 1:
            params['idempotence'] = idempotence

        return self.__client.call('print/index', params)
