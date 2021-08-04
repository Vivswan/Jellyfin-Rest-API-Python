from jellyfin.baseclass import BaseClass
from schema.classes._core import from_list
from schema.classes.base_item_dto_query_result import BaseItemDtoQueryResult
from schema.classes.file_organization_result_query_result import FileOrganizationResultQueryResult
from schema.classes.virtual_folder_info import VirtualFolderInfo


class Library(BaseClass):
    def __init__(self, server_address, api_key, pre_path):
        super().__init__(server_address, api_key, pre_path + f"/{self.__class__.__name__}")
        self.VirtualFolders = VirtualFolders(server_address, api_key, self.pre_path)
        self.FileOrganizations = FileOrganizations(server_address, api_key, self.pre_path)
        self.MediaFolders = MediaFolders(server_address, api_key, self.pre_path)


class VirtualFolders(BaseClass):
    def __init__(self, server_address, api_key, pre_path):
        super().__init__(server_address, api_key, pre_path + f"/{self.__class__.__name__}")

    def __call__(self, *args, **kwargs):
        return from_list(VirtualFolderInfo.from_dict, self.get_json())


class FileOrganizations(BaseClass):
    def __init__(self, server_address, api_key, pre_path):
        super().__init__(server_address, api_key, pre_path + f"/{self.__class__.__name__}")

    def __call__(self, *args, **kwargs):
        return FileOrganizationResultQueryResult.from_dict(self.get())


class MediaFolders(BaseClass):
    def __init__(self, server_address, api_key, pre_path):
        super().__init__(server_address, api_key, pre_path + f"/{self.__class__.__name__}")

    def __call__(self, *args, **kwargs):
        return BaseItemDtoQueryResult.from_dict(self.get())
