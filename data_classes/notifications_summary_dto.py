from util.from_type import *
from data_classes.level import Level


@dataclass
class NotificationsSummaryDto:
    """The notification summary DTO."""
    """Gets or sets the maximum unread notification level."""
    max_unread_notification_level: Optional[Level] = None
    """Gets or sets the number of unread notifications."""
    unread_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NotificationsSummaryDto':
        assert isinstance(obj, dict)
        max_unread_notification_level = from_union([Level, from_none], obj.get("MaxUnreadNotificationLevel"))
        unread_count = from_union([from_int, from_none], obj.get("UnreadCount"))
        return NotificationsSummaryDto(max_unread_notification_level, unread_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MaxUnreadNotificationLevel"] = from_union([lambda x: to_enum(Level, x), from_none], self.max_unread_notification_level)
        result["UnreadCount"] = from_union([from_int, from_none], self.unread_count)
        return result


