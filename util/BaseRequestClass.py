import requests


class BaseRequestClass:
    server_address: str
    api_key: str
    pre_path: str

    def __init__(self, server_address: str, api_key: str):
        self.api_key = api_key
        self.server_address = server_address

    def get(self, path, request_args=None, response_type=requests.Response):
        if request_args is None:
            request_args = {}

    def post(self, path, request_args=None, response_type=requests.Response):
        if request_args is None:
            request_args = {}

    def delete(self, path, request_args=None, response_type=requests.Response):
        if request_args is None:
            request_args = {}

    def head(self, path, request_args=None, response_type=requests.Response):
        if request_args is None:
            request_args = {}
