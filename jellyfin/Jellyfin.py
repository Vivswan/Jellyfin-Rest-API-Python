from jellyfin.Library import Library
from jellyfin.baseclass import BaseClass


class Jellyfin(BaseClass):
    def __init__(self, server_address, api_key):
        super().__init__(server_address, api_key, "")
        self.Library = Library(self.server_address, self.api_key, self.pre_path)
