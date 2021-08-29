from data_classes.version_number import VersionNumber
from util.from_type import *


@dataclass
class IPlugin:
    """Defines the MediaBrowser.Common.Plugins.IPlugin."""
    """Gets the path to the assembly file."""
    assembly_file_path: Optional[str] = None
    """Gets a value indicating whether the plugin can be uninstalled."""
    can_uninstall: Optional[bool] = None
    """Gets the full path to the data folder, where the plugin can store any miscellaneous files
    needed.
    """
    data_folder_path: Optional[str] = None
    """Gets the Description."""
    description: Optional[str] = None
    """Gets the unique id."""
    id: Optional[UUID] = None
    """Gets the name of the plugin."""
    name: Optional[str] = None
    """Gets the plugin version."""
    version: Optional[VersionNumber] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IPlugin':
        assert isinstance(obj, dict)
        assembly_file_path = from_union([from_str, from_none], obj.get("AssemblyFilePath"))
        can_uninstall = from_union([from_bool, from_none], obj.get("CanUninstall"))
        data_folder_path = from_union([from_str, from_none], obj.get("DataFolderPath"))
        description = from_union([from_str, from_none], obj.get("Description"))
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        name = from_union([from_str, from_none], obj.get("Name"))
        version = from_union([VersionNumber.from_dict, from_none], obj.get("Version"))
        return IPlugin(assembly_file_path, can_uninstall, data_folder_path, description, id, name, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AssemblyFilePath"] = from_union([from_str, from_none], self.assembly_file_path)
        result["CanUninstall"] = from_union([from_bool, from_none], self.can_uninstall)
        result["DataFolderPath"] = from_union([from_str, from_none], self.data_folder_path)
        result["Description"] = from_union([from_str, from_none], self.description)
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Version"] = from_union([lambda x: to_class(VersionNumber, x), from_none], self.version)
        return result


