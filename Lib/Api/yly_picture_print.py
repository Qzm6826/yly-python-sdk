#!/usr/bin/python
# -*- coding: utf-8 -*-

class YlyPicturePrint:

    __client = None

    def __init__(self, client):
        self.__client = client

    def index(self, machine_code, link, origin_id, idempotence= 0):
        """
        图形打印接口 不支持机型: k4-wh, k4-wa, m1
        :param machine_code: 机器码
        :param link: 图片链接地址
        :param origin_id: 商户系统内部订单号，要求32个字符内，只能是数字、大小写字母
        :return:
        """
        params = {
            'machine_code': machine_code,
            'picture_url': link,
            'origin_id': origin_id
        }
        if idempotence == 1:
            params['idempotence'] = idempotence

        return self.__client.call('pictureprint/index', params)