#!/usr/bin/python
# -*- coding: utf-8 -*-

class YlyPrintMenu:

    __client = None

    def __init__(self, client):
        self.__client = client

    def add_print_menu(self, machine_code, content):
        """
        添加应用菜单接口
        :param machine_code: 机器码
        :param content: 菜单详情(json)
        :return:
        """
        params = {
            'machine_code': machine_code,
            'content': content
        }
        return self.__client.call('printmenu/addprintmenu', params)