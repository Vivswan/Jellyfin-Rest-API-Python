from jellyfin.baseclass import BaseClass


class Jellyfin(BaseClass):
    def __init__(self, server_address, api_key):
        super().__init__(server_address, api_key, "")
