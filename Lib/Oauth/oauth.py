#!/usr/bin/python
import uuid
import time
import hashlib
import json
import urllib2
from urllib import urlencode

class Oauth:

    def __init__(self, config):
        self.client_id = config.get_client_id()
        self.client_secret = config.get_client_secret()
        self.url = config.get_request_url()
        self.md5 = hashlib.md5()

    def get_token(self, code= None):
        params = {
            'client_id': self.client_id,
            'timestamp': int(time.time()),
            'id': uuid.uuid4(),
            'scope': 'all'
        }
        if (code == None):
            params['grant_type'] = 'client_credentials'
        else:
            params['grant_type'] = 'authorization_code'
            params['code'] = code
        sign_str = str(self.client_id) + str(params['timestamp']) + str(self.client_secret)
        self.md5.update(sign_str.encode('utf-8'))
        params['sign'] = self.md5.hexdigest()
        request_params = urlencode(params)
        return self.post(request_params)

    def refresh_token(self, refresh_token):
        params = {
            'client_id': self.client_id,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token',
            'scope': 'all',
            'timestamp': int(time.time()),
            'id': uuid.uuid4()
        }
        sign_str = str(self.client_id) + str(params['timestamp']) + str(self.client_secret)
        self.md5.update(sign_str.encode('utf-8'))
        params['sign'] = self.md5.hexdigest()
        request_params = urlencode(params)
        return self.post(request_params)

    def post(self, req_params):
        try:
            header = {
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
            }
            req_url = self.url + 'oauth/oauth'
            req = urllib2.Request(req_url, req_params, header)
            res = urllib2.urlopen(req)
            return json.loads(res.read())
        except Exception as e:
            raise Exception('yly api response:{}'.format(e))
