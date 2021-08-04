import requests


class BaseClass:
    server_address: str
    api_key: str
    pre_path: str

    def __init__(self, server_address: str, api_key: str, pre_path: str):
        self.pre_path = pre_path
        self.api_key = api_key
        self.server_address = server_address

    def get(self, request=""):
        params = {
            "api_key": self.api_key
        }
        result = requests.get(f"{self.server_address}{self.pre_path}{request}", params=params)

        if result.status_code == 200:
            if len(result.text) > 0:
                return result
            else:
                return None
        else:
            raise Exception(f"{result.status_code}: {result.text}")

    def get_json(self, request=""):
        return self.get(request=request).json()
