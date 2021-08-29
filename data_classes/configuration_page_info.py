from data_classes.configuration_page_type import ConfigurationPageType
from util.from_type import *


@dataclass
class ConfigurationPageInfo:
    """The configuration page info."""
    """Gets or sets the type of the configuration page."""
    configuration_page_type: Optional[ConfigurationPageType] = None
    """Gets or sets the display name."""
    display_name: Optional[str] = None
    """Gets or sets a value indicating whether the configurations page is enabled in the main
    menu.
    """
    enable_in_main_menu: Optional[bool] = None
    """Gets or sets the menu icon."""
    menu_icon: Optional[str] = None
    """Gets or sets the menu section."""
    menu_section: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the plugin id."""
    plugin_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConfigurationPageInfo':
        assert isinstance(obj, dict)
        configuration_page_type = from_union([ConfigurationPageType, from_none], obj.get("ConfigurationPageType"))
        display_name = from_union([from_str, from_none], obj.get("DisplayName"))
        enable_in_main_menu = from_union([from_bool, from_none], obj.get("EnableInMainMenu"))
        menu_icon = from_union([from_str, from_none], obj.get("MenuIcon"))
        menu_section = from_union([from_str, from_none], obj.get("MenuSection"))
        name = from_union([from_str, from_none], obj.get("Name"))
        plugin_id = from_union([lambda x: UUID(x), from_none], obj.get("PluginId"))
        return ConfigurationPageInfo(configuration_page_type, display_name, enable_in_main_menu, menu_icon, menu_section, name, plugin_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ConfigurationPageType"] = from_union([lambda x: to_enum(ConfigurationPageType, x), from_none], self.configuration_page_type)
        result["DisplayName"] = from_union([from_str, from_none], self.display_name)
        result["EnableInMainMenu"] = from_union([from_bool, from_none], self.enable_in_main_menu)
        result["MenuIcon"] = from_union([from_str, from_none], self.menu_icon)
        result["MenuSection"] = from_union([from_str, from_none], self.menu_section)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["PluginId"] = from_union([lambda x: str(x), from_none], self.plugin_id)
        return result


