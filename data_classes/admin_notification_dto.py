from data_classes.level import Level
from util.from_type import *


@dataclass
class AdminNotificationDto:
    """The admin notification dto."""
    """Gets or sets the notification description."""
    description: Optional[str] = None
    """Gets or sets the notification name."""
    name: Optional[str] = None
    """Gets or sets the notification level."""
    notification_level: Optional[Level] = None
    """Gets or sets the notification url."""
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminNotificationDto':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("Description"))
        name = from_union([from_str, from_none], obj.get("Name"))
        notification_level = from_union([Level, from_none], obj.get("NotificationLevel"))
        url = from_union([from_str, from_none], obj.get("Url"))
        return AdminNotificationDto(description, name, notification_level, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Description"] = from_union([from_str, from_none], self.description)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["NotificationLevel"] = from_union([lambda x: to_enum(Level, x), from_none], self.notification_level)
        result["Url"] = from_union([from_str, from_none], self.url)
        return result


