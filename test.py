#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Lib.Config.config import Config
from Lib.Oauth.oauth import Oauth
from Lib.Protocol.rpc_client import RpcClient
from Lib.Api.yly_print import YlyPrint

config = Config('1061036006', '22a8e517c8b1357f0419732d8d6c4c7d')
config.set_request_url('https://open-api.10ss.net/v2')
oauth_client = Oauth(config)
token_data = oauth_client.get_token()
access_token = token_data['body']['access_token']
rpc_client = RpcClient(config, access_token)
print_service = YlyPrint(rpc_client)
res = print_service.index('4004628158', '测试', '12348798716564')
print(res)