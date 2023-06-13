#!/usr/bin/python
class Config:

    __client_id = None
    __client_secret = None
    __request_url = 'https://open-api.10ss.net'

    def __init__(self, id, secret):
        if (id == None or secret == None):
            raise Exception('ClientId and clientSecret cannot be empty')
        self.__client_id = id
        self.__client_secret = secret

    def get_client_id(self):
        return self.__client_id

    def get_client_secret(self):
        return self.__client_secret

    def get_request_url(self):
        return self.__request_url

    def set_request_url(self, request_url):
        self.__request_url = request_url