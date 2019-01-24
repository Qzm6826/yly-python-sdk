#!/usr/bin/python
import requests
import uuid
import time
import hashlib
import json
import urllib2
from urllib import urlencode

class RpcClient:

    def __init__(self, config, token):
        self.access_token = token
        self.client_id = config.get_client_id()
        self.client_secret = config.get_client_secret()
        self.url = config.get_request_url()
        self.md5 = hashlib.md5()

    def call(self, action, params):
        params['client_id'] = self.client_id
        params['access_token'] = self.access_token
        params['timestamp'] = time.time()
        params['id'] = uuid.uuid4()
        sign_str = str(self.client_id) + str(params['timestamp']) + self.client_secret
        self.md5.update(sign_str.encode('utf-8'))
        params['sign'] = self.md5.hexdigest()
        request_url = self.url + action
        request_data = urlencode(params)
        return self.post(request_url, request_data)

    def post(self, req_url, req_params):
        try:
            header = {
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
            }
            req = urllib2.Request(req_url, req_params, header)
            res = urllib2.urlopen(req)
            return json.loads(res.read())
        except Exception as e:
            raise Exception('yly api response:{}'.format(e))
