import requests

from _config import SERVER_ADDRESS, API_KEY


def get(request):
    return requests.get(f"{SERVER_ADDRESS}/{request}?api_key={API_KEY}").json()


def list_all_libraries():
    print(get("Persons")["StartIndex"])


if __name__ == '__main__':
    print(list_all_libraries())
