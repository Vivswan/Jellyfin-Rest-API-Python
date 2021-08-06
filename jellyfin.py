import json

import requests

from _config import SERVER_ADDRESS, API_KEY
from query_classes import Jellyfin


def print_json(parsed):
    print(json.dumps(parsed, indent=4, sort_keys=True))


if __name__ == '__main__':
    jf = Jellyfin(SERVER_ADDRESS, API_KEY)
    response = jf.system.post_ping_system()
    if isinstance(response, requests.Response):
        print(response.text)
    else:
        print(response)
