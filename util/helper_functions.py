import json


def del_none(d):
    """
    Delete keys with the value ``None`` in a dictionary, recursively.

    This alters the input so you may wish to ``copy`` the dict first.
    """
    # For Python 3, write `list(d.items())`; `d.items()` won’t work
    # For Python 2, write `d.items()`; `d.iteritems()` won’t work
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
        elif isinstance(value, list):
            if len(value) == 0:
                del d[key]
            else:
                [to_json_str(x) for x in value]
    return d  # For convenience


def to_json_str(arg):
    if hasattr(arg, "to_dict"):
        return to_json_str(arg.to_dict())

    if isinstance(arg, list):
        return to_json_str([to_json_str(x) for x in arg])

    if hasattr(arg, "keys"):
        return json.dumps(del_none(arg), indent=2)
    return arg
