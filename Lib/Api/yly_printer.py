#!/usr/bin/python
# -*- coding: utf-8 -*-

class YlyPrinter:

    __client = None

    def __init__(self, client):
        self.__client = client

    def add_printer(self, machine_code, msign, print_name= None, phone= None):
        """
        自有型应用授权终端接口
        :param machine_code: 机器码
        :param msign: 机器密钥
        :param print_name: 打印机昵称
        :param phone: gprs卡号
        :return:
        """
        params = {
            'machine_code': machine_code,
            'msign': msign,
            'print_name': print_name,
            'phone': phone
        }
        return self.__client.call('printer/addprinter', params)

    def set_voice(self, machine_code, contnet, isfile= False, aid= None):
        """
        设置内置语音接口 注意: 仅支持K4-WA、K4-GAD、K4-WGEAD型号
        :param machine_code: 机器码
        :param contnet: 在线语音地址链接 or 自定义语音内容
        :param isfile: true or false
        :param aid: 0~9 , 定义需设置的语音编号,若不提交,默认升序
        :return:
        """
        params = {
            'machine_code': machine_code,
            'content': contnet,
            'is_file': isfile,
        }
        if (aid != None):
            params['aid'] = aid
        return self.__client.call('printer/setvoice', params)

    def del_voice(self, machine_code, aid):
        """
        删除内置语音接口 注意: 仅支持K4-WA、K4-GAD、K4-WGEAD型号
        :param machine_code: 机器码
        :param aid: 0 ~ 9 编号
        :return:
        """
        params = {
            'machine_code': machine_code,
            'aid': aid
        }
        return  self.__client.call('printer/deletevoice', params)

    def del_printer(self, machine_code):
        """
        删除终端授权接口
        :param machine_code: 机器码
        :return:
        """
        params = {
            'machine_code': machine_code
        }
        return self.__client.call('printer/deleteprinter', params)

    def shutdown_restart(self, machine_code, type):
        """
        关机重启接口
        :param machine_code: 机器码
        :param type: restart or shutdown
        :return:
        """
        params = {
            'machine_code': machine_code,
            'response_type': type
        }
        return self.__client.call('printer/shutdownrestart', params)

    def set_sound(self, machine_code, voice, type):
        """
        声音调节接口
        :param machine_code: 机器码
        :param voice: 音量 0 or 1 or 2 or 3
        :param type: buzzer (蜂鸣器) or horn (喇叭)
        :return:
        """
        params = {
            'machine_code': machine_code,
            'voice': voice,
            'type': type
        }
        return self.__client.call('printer/setsound', params)

    def print_info(self, machine_code):
        """
        获取机型打印宽度接口
        :param machine_code: 机器码
        :return:
        """
        params = {
            'machine_code': machine_code
        }
        return self.__client.call('printer/printinfo', params)

    def get_version(self, machine_code):
        """
        获取机型软硬件版本接口
        :param machine_code: 机器码
        :return:
        """
        params = {
            'machine_code': machine_code
        }
        return self.__client.call('printer/getversion', params)

    def cancel_all(self, machine_code):
        """
        取消所有未打印订单接口
        :param machine_code: 机器码
        :return:
        """
        params = {
            'machine_code': machine_code
        }
        return self.__client.call('printer/cancelall', params)

    def cancel_one(self, machine_code, order_no):
        """
        取消单条未打印订单接口
        :param machine_code: 机器码
        :param order_no: 未打印的易联云id
        :return:
        """
        params = {
            'machine_code': machine_code,
            'order_id': order_no
        }
        return self.__client.call('printer/cancelone', params)

    def set_icon(self, machine_code, link):
        """
        设置logo接口
        :param machine_code: 机器码
        :param link: logo链接地址
        :return:
        """
        params = {
            'machine_code': machine_code,
            'img_url': link
        }
        return self.__client.call('printer/seticon', params)

    def del_icon(self, machine_code):
        """
        取消logo接口
        :param machine_code: 机器码
        :return:
        """
        params = {
            'machine_code': machine_code
        }
        return self.__client.call('printer/deleteicon', params)

    def btn_print(self, machine_code, type):
        """
        打印方式接口
        :param machine_code: 机器码
        :param type: btnopen or btnclose
        :return:
        """
        params = {
            'machine_code': machine_code,
            'response_type': type
        }
        return self.__client.call('printer/btnprint', params)

    def get_order(self, machine_code, type):
        """
        接单拒单设置接口
        :param machine_code: 机器码
        :param type: open or close
        :return:
        """
        params = {
            'machine_code': machine_code,
            'response_type': type
        }
        return self.__client.call('printer/getorder', params)

    def get_order_status(self, machine_code, order_no):
        """
        获取订单状态接口
        :param machine_code: 机器码
        :param order_no: 易联云订单id
        :return:
        """
        params = {
            'machine_code': machine_code,
            'order_id': order_no
        }
        return self.__client.call('printer/getorderstatus', params)

    def get_order_paging_list(self, machine_code, page_index= 1, page_size= 10):
        """
        获取订单列表接口
        :param machine_code: 机器码
        :param page_index: 第几页
        :param page_size: 查询条数
        :return:
        """
        params = {
            'machine_code': machine_code,
            'page_index': page_index,
            'page_size': page_size
        }
        return self.__client.call('printer/getorderpaginglist', params)

    def reprint(self, machine_code, order_no):
        """
        获取订单状态接口
        :param machine_code: 机器码
        :param order_no: 易联云订单id
        :return:
        """
        params = {
            'machine_code': machine_code,
            'order_id': order_no
        }
        return self.__client.call('printer/reprintorder', params)

    def get_print_status(self, machine_code):
        """
        获取终端状态接口
        :param machine_code: 机器码
        :return:
        """
        params = {
            'machine_code': machine_code
        }
        return self.__client.call('printer/getprintstatus', params)

    def push_switch(self, machine_code, status, mode= 1):
        """
        K8 推送开关设置接口
        :param machine_code:
        :param status:
        :param mode
        :return:
        """
        params = {
            'machine_code': machine_code,
            'status': status,
            'mode': mode
        }
        return self.__client.call('printer/pushswitch', params)


    def set_keywords(self, machine_code, keys, type, content):
        """
        K8关键词设置接口
        :param machine_code:
        :param keys:
        :param type:
        :param content:
        :return:
        """
        params = {
            'machine_code': machine_code,
            'keys': keys,
            'type': type,
            'content': content
        }
        return self.__client.call('printer/setkeywords', params)

    def setting(self, machine_code, usb_print_mode= None, usb_input_mode= None, camera_decode_tx_mode= None):
        """
        K8 高级设置接口
        :param machine_code:
        :param usb_print_mode:
        :param usb_input_mode:
        :param camera_decode_tx_mode:
        :return:
        """
        params = {'machine_code': machine_code}
        if (usb_print_mode == 0 or usb_print_mode == 1):
            params['usb_print_mode'] = usb_print_mode
        if (usb_input_mode == 0 or usb_input_mode == 1):
            params['usb_input_mode'] = usb_input_mode
        if (camera_decode_tx_mode == 0 or camera_decode_tx_mode == 1):
            params['camera_decode_tx_mode'] = camera_decode_tx_mode
        return self.__client.call('printer/setting', params)
