from util.from_type import *
from data_classes.version_number import VersionNumber
from data_classes.plugin_status_enum import PluginStatusEnum


@dataclass
class PluginInfo:
    """This is a serializable stub class that is used by the api to provide information about
    installed plugins.
    """
    """Gets or sets a value indicating whether the plugin can be uninstalled."""
    can_uninstall: Optional[bool] = None
    """Gets or sets the name of the configuration file."""
    configuration_file_name: Optional[str] = None
    """Gets or sets the description."""
    description: Optional[str] = None
    """Gets or sets a value indicating whether this plugin has a valid image."""
    has_image: Optional[bool] = None
    """Gets or sets the unique id."""
    id: Optional[UUID] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets a value indicating the status of the plugin."""
    status: Optional[PluginStatusEnum] = None
    """Gets or sets the version."""
    version: Optional[VersionNumber] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PluginInfo':
        assert isinstance(obj, dict)
        can_uninstall = from_union([from_bool, from_none], obj.get("CanUninstall"))
        configuration_file_name = from_union([from_str, from_none], obj.get("ConfigurationFileName"))
        description = from_union([from_str, from_none], obj.get("Description"))
        has_image = from_union([from_bool, from_none], obj.get("HasImage"))
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        name = from_union([from_str, from_none], obj.get("Name"))
        status = from_union([PluginStatusEnum, from_none], obj.get("Status"))
        version = from_union([VersionNumber.from_dict, from_none], obj.get("Version"))
        return PluginInfo(can_uninstall, configuration_file_name, description, has_image, id, name, status, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CanUninstall"] = from_union([from_bool, from_none], self.can_uninstall)
        result["ConfigurationFileName"] = from_union([from_str, from_none], self.configuration_file_name)
        result["Description"] = from_union([from_str, from_none], self.description)
        result["HasImage"] = from_union([from_bool, from_none], self.has_image)
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Status"] = from_union([lambda x: to_enum(PluginStatusEnum, x), from_none], self.status)
        result["Version"] = from_union([lambda x: to_class(VersionNumber, x), from_none], self.version)
        return result


