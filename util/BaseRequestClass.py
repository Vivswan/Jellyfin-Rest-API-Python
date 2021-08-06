from typing import Union, Type, List, TypeVar

import requests

from data_classes._core import from_list


def arg_to_json(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    if isinstance(obj, list):
        return [arg_to_json(i) for i in obj]
    return obj


def parse_url_for_query_classes(url_path: str, request_args):
    new_request_args = {}
    for parameter_name in request_args:
        if "{" + url_path + "}" in url_path:
            url_path = url_path.replace("{" + url_path + "}", request_args[parameter_name])
        else:
            new_request_args[parameter_name] = arg_to_json(request_args[parameter_name])
    return url_path, new_request_args


class BaseRequestClass:
    type_request = Union[None, object]
    type_response = TypeVar('type_response', bound=Union[
        str,
        int,
        float,
        bool,
        object,
        requests.Response,
        Type['BaseRequestClass'],
        List[Type['BaseRequestClass']]
    ])

    def __init__(self, server_address: str, api_key: str):
        self._api_key = api_key
        self._server_address = server_address

    @staticmethod
    def response_to_response_type(response, response_type: type_response) -> type_response:
        if hasattr(response_type, "__origin__") and response_type.__origin__ == list:
            if hasattr(response_type.__args__[0], 'from_dict'):
                return from_list(response_type.__args__[0].from_dict, response.json())

        if hasattr(response_type, "from_dict"):
            return response_type.from_dict(response.json())

        if response_type == str:
            try:
                if isinstance(response.json(), str):
                    return response.json()
            except:
                pass
            return response.text
        if response_type == float:
            return float(response.text)
        if response_type == int:
            return int(response.text)
        if response_type == bool:
            return bool(response.text)
        if response_type == object:
            return response.json()

        if response_type == requests.Response:
            return response
        else:
            raise NotImplemented({f"response_type: {response_type}"})

    def _send_request(
            self,
            http_method,
            path: str,
            request_args: Union[None, object] = None,
            response_type: type_response = requests.Response
    ) -> type_response:
        if request_args is None:
            request_args = {}

        path, request_args = parse_url_for_query_classes(path, request_args)
        request_args["api_key"] = self._api_key

        if "requestBody" in request_args:
            request_body = request_args["requestBody"]
            del request_args["requestBody"]
            response = getattr(requests, http_method)(f"{self._server_address}{path}", json=request_body,
                                                      params=request_args)
        else:
            response = getattr(requests, http_method)(f"{self._server_address}{path}", params=request_args)

        return self.response_to_response_type(response, response_type)

    def _get(
            self,
            path: str,
            request_args: type_request = None,
            response_type: type_response = requests.Response
    ) -> type_response:
        return self._send_request('get', path, request_args, response_type)

    def _post(
            self,
            path: str,
            request_args: Union[None, object] = None,
            response_type: type_response = requests.Response
    ) -> type_response:
        return self._send_request('post', path, request_args, response_type)

    def _delete(
            self,
            path: str,
            request_args: Union[None, object] = None,
            response_type: type_response = requests.Response
    ) -> type_response:
        return self._send_request('delete', path, request_args, response_type)

    def _head(
            self,
            path: str,
            request_args: Union[None, object] = None,
            response_type: type_response = requests.Response
    ) -> type_response:
        return self._send_request('head', path, request_args, response_type)
