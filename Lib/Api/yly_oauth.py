#!/usr/bin/python
# -*- coding: utf-8 -*-

class YlyOauth:

    __client = None

    def __init__(self, client):
        self.__client = client

    def set_push_url(self, cmd, link, status= 'open'):
        """
        设置推送URL接口
        :param cmd: 推送队列键
        :param link: 推送地址
        :param status: 推送开关
        :return:
        """
        params = {
            'cmd': cmd,
            'url': link,
            'status': status
        }
        return self.__client.call('oauth/setpushurl', params)
