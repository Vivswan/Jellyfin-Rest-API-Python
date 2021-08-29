from util.from_type import *
from data_classes.notification_dto import NotificationDto


@dataclass
class NotificationResultDto:
    """A list of notifications with the total record count for pagination."""
    """Gets or sets the current page of notifications."""
    notifications: Optional[List[NotificationDto]] = None
    """Gets or sets the total number of notifications."""
    total_record_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NotificationResultDto':
        assert isinstance(obj, dict)
        notifications = from_union([lambda x: from_list(NotificationDto.from_dict, x), from_none], obj.get("Notifications"))
        total_record_count = from_union([from_int, from_none], obj.get("TotalRecordCount"))
        return NotificationResultDto(notifications, total_record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Notifications"] = from_union([lambda x: from_list(lambda x: to_class(NotificationDto, x), x), from_none], self.notifications)
        result["TotalRecordCount"] = from_union([from_int, from_none], self.total_record_count)
        return result


