#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Lib.Config.config import Config
from Lib.Oauth.oauth import Oauth
from Lib.Protocol.rpc_client import RpcClient
from Lib.Api.yly_print import YlyPrint

config = Config('1036032809', '3b5812d9359dd06a99f3b7199ae7f37f')
oauth_client = Oauth(config)
token_data = oauth_client.get_token()
access_token = token_data['body']['access_token']
rpc_client = RpcClient(config, access_token)
print_service = YlyPrint(rpc_client)
print_service.index('4004517585', '测试', '12348798716564')