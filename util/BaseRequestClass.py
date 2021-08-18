import json
from typing import Union, Type, List, TypeVar, Dict
from urllib.error import HTTPError

import requests

T = TypeVar('T')
AddResponse = Union[requests.Response, T]


def arg_to_json(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    if isinstance(obj, list):
        return [arg_to_json(i) for i in obj]
    return obj


def parse_url_for_query_classes(url_path: str, request_args: Union[None, Dict] = None):
    if request_args is None:
        return url_path, {}

    new_request_args = {}
    for parameter_name in request_args:
        url_parameter_name = "{" + parameter_name + "}"
        if url_parameter_name in url_path:
            url_path = url_path.replace(url_parameter_name, str(request_args[parameter_name]))
        else:
            new_request_args[parameter_name] = arg_to_json(request_args[parameter_name])
    return url_path, new_request_args


def to_non_list_response_type(response: str, response_type: T) -> T:
    if hasattr(response_type, "from_dict"):
        return response_type.from_dict(json.loads(response))

    if response_type == str:
        try:
            if isinstance(json.loads(response), str):
                return json.loads(response)
        except:
            pass
        return response

    if response_type == float:
        return float(json.loads(response))

    if response_type == int:
        return int(json.loads(response))

    if response_type == bool:
        return bool(json.loads(response))

    if response_type == object:
        return json.loads(response)

    raise NotImplemented({f"response_type: {response_type}"})


def to_response_type(response: requests.Response, response_type: T) -> T:
    if str(response.status_code)[0] in ["4", "5"]:
        raise HTTPError(
            url=response.url,
            code=response.status_code,
            msg=f"<{response.reason}> :{response.text}",
            hdrs=response.headers,
            fp=None
        )

    if response.status_code != 200:
        return response

    if response_type == requests.Response:
        return response

    if hasattr(response_type, "__origin__") and response_type.__origin__ == list:
        return [to_non_list_response_type(json.dumps(x), response_type.__args__[0]) for x in response.json()]

    return to_non_list_response_type(response.text, response_type)


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

    def _send_request(
            self,
            http_method,
            path: str,
            request_args: Union[None, object] = None,
            response_type: type_response = requests.Response
    ) -> type_response:
        path, request_args = parse_url_for_query_classes(path, request_args)
        request_args["api_key"] = self._api_key

        url = f"{self._server_address}{path}"
        http_method_fn = getattr(requests, http_method)
        if "requestBody" in request_args:
            request_body = request_args["requestBody"]
            del request_args["requestBody"]
            response = http_method_fn(url, json=request_body, params=request_args)
        else:
            response = http_method_fn(url, params=request_args)

        return to_response_type(response, response_type)

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
