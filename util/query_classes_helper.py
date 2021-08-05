def query_class_arg_to_json(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    if isinstance(obj, list):
        return [query_class_arg_to_json(i) for i in obj]
    return obj


def parse_url_for_query_classes(url_path: str, request_args):
    new_request_args = {}
    for parameter_name in request_args:
        if "{" + url_path + "}" in url_path:
            url_path = url_path.replace("{" + url_path + "}", request_args[parameter_name])
        else:
            new_request_args[parameter_name] = request_args[parameter_name]
    return url_path, new_request_args
