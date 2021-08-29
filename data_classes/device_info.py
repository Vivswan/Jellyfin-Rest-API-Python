from data_classes.capabilities import Capabilities
from util.from_type import *


@dataclass
class DeviceInfo:
    """Gets or sets the name of the application."""
    app_name: Optional[str] = None
    """Gets or sets the application version."""
    app_version: Optional[str] = None
    """Gets or sets the capabilities."""
    capabilities: Optional[Capabilities] = None
    """Gets or sets the date last modified."""
    date_last_activity: Optional[datetime] = None
    icon_url: Optional[str] = None
    """Gets or sets the identifier."""
    id: Optional[str] = None
    """Gets or sets the last user identifier."""
    last_user_id: Optional[UUID] = None
    """Gets or sets the last name of the user."""
    last_user_name: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceInfo':
        assert isinstance(obj, dict)
        app_name = from_union([from_str, from_none], obj.get("AppName"))
        app_version = from_union([from_str, from_none], obj.get("AppVersion"))
        capabilities = from_union([Capabilities.from_dict, from_none], obj.get("Capabilities"))
        date_last_activity = from_union([from_datetime, from_none], obj.get("DateLastActivity"))
        icon_url = from_union([from_str, from_none], obj.get("IconUrl"))
        id = from_union([from_str, from_none], obj.get("Id"))
        last_user_id = from_union([lambda x: UUID(x), from_none], obj.get("LastUserId"))
        last_user_name = from_union([from_str, from_none], obj.get("LastUserName"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return DeviceInfo(app_name, app_version, capabilities, date_last_activity, icon_url, id, last_user_id, last_user_name, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AppName"] = from_union([from_str, from_none], self.app_name)
        result["AppVersion"] = from_union([from_str, from_none], self.app_version)
        result["Capabilities"] = from_union([lambda x: to_class(Capabilities, x), from_none], self.capabilities)
        result["DateLastActivity"] = from_union([lambda x: x.isoformat(), from_none], self.date_last_activity)
        result["IconUrl"] = from_union([from_str, from_none], self.icon_url)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["LastUserId"] = from_union([lambda x: str(x), from_none], self.last_user_id)
        result["LastUserName"] = from_union([from_str, from_none], self.last_user_name)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


