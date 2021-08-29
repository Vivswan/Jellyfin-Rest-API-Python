from data_classes.live_tv_service_info import LiveTvServiceInfo
from util.from_type import *


@dataclass
class LiveTvInfo:
    """Gets or sets the enabled users."""
    enabled_users: Optional[List[str]] = None
    """Gets or sets a value indicating whether this instance is enabled."""
    is_enabled: Optional[bool] = None
    """Gets or sets the services."""
    services: Optional[List[LiveTvServiceInfo]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LiveTvInfo':
        assert isinstance(obj, dict)
        enabled_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("EnabledUsers"))
        is_enabled = from_union([from_bool, from_none], obj.get("IsEnabled"))
        services = from_union([lambda x: from_list(LiveTvServiceInfo.from_dict, x), from_none], obj.get("Services"))
        return LiveTvInfo(enabled_users, is_enabled, services)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EnabledUsers"] = from_union([lambda x: from_list(from_str, x), from_none], self.enabled_users)
        result["IsEnabled"] = from_union([from_bool, from_none], self.is_enabled)
        result["Services"] = from_union([lambda x: from_list(lambda x: to_class(LiveTvServiceInfo, x), x), from_none], self.services)
        return result


