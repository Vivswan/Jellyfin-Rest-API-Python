import json

from _config import SERVER_ADDRESS, API_KEY
from data_classes.classes.virtual_folder_info import VirtualFolderInfo
from jellyfin.Jellyfin import Jellyfin


def print_json(parsed):
    print(json.dumps(parsed, indent=4, sort_keys=True))


if __name__ == '__main__':
    jf = Jellyfin(SERVER_ADDRESS, API_KEY)
    v = VirtualFolderInfo.from_dict(jf.get_json('/Library/VirtualFolders')[0])
