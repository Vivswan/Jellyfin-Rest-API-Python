from data_classes.live_tv_service_status_enum import LiveTvServiceStatusEnum
from util.from_type import *


@dataclass
class LiveTvServiceInfo:
    """Class ServiceInfo."""
    """Gets or sets a value indicating whether this instance has update available."""
    has_update_available: Optional[bool] = None
    """Gets or sets the home page URL."""
    home_page_url: Optional[str] = None
    """Gets or sets a value indicating whether this instance is visible."""
    is_visible: Optional[bool] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the status."""
    status: Optional[LiveTvServiceStatusEnum] = None
    """Gets or sets the status message."""
    status_message: Optional[str] = None
    tuners: Optional[List[str]] = None
    """Gets or sets the version."""
    version: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LiveTvServiceInfo':
        assert isinstance(obj, dict)
        has_update_available = from_union([from_bool, from_none], obj.get("HasUpdateAvailable"))
        home_page_url = from_union([from_str, from_none], obj.get("HomePageUrl"))
        is_visible = from_union([from_bool, from_none], obj.get("IsVisible"))
        name = from_union([from_str, from_none], obj.get("Name"))
        status = from_union([LiveTvServiceStatusEnum, from_none], obj.get("Status"))
        status_message = from_union([from_str, from_none], obj.get("StatusMessage"))
        tuners = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Tuners"))
        version = from_union([from_str, from_none], obj.get("Version"))
        return LiveTvServiceInfo(has_update_available, home_page_url, is_visible, name, status, status_message, tuners, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["HasUpdateAvailable"] = from_union([from_bool, from_none], self.has_update_available)
        result["HomePageUrl"] = from_union([from_str, from_none], self.home_page_url)
        result["IsVisible"] = from_union([from_bool, from_none], self.is_visible)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Status"] = from_union([lambda x: to_enum(LiveTvServiceStatusEnum, x), from_none], self.status)
        result["StatusMessage"] = from_union([from_str, from_none], self.status_message)
        result["Tuners"] = from_union([lambda x: from_list(from_str, x), from_none], self.tuners)
        result["Version"] = from_union([from_str, from_none], self.version)
        return result


