from util.from_type import *
from data_classes.level import Level


@dataclass
class NotificationDto:
    """The notification DTO."""
    """Gets or sets the notification date."""
    date: Optional[datetime] = None
    """Gets or sets the notification's description. Defaults to an empty string."""
    description: Optional[str] = None
    """Gets or sets the notification ID. Defaults to an empty string."""
    id: Optional[str] = None
    """Gets or sets a value indicating whether the notification has been read. Defaults to false."""
    is_read: Optional[bool] = None
    """Gets or sets the notification level."""
    level: Optional[Level] = None
    """Gets or sets the notification's name. Defaults to an empty string."""
    name: Optional[str] = None
    """Gets or sets the notification's URL. Defaults to an empty string."""
    url: Optional[str] = None
    """Gets or sets the notification's user ID. Defaults to an empty string."""
    user_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NotificationDto':
        assert isinstance(obj, dict)
        date = from_union([from_datetime, from_none], obj.get("Date"))
        description = from_union([from_str, from_none], obj.get("Description"))
        id = from_union([from_str, from_none], obj.get("Id"))
        is_read = from_union([from_bool, from_none], obj.get("IsRead"))
        level = from_union([Level, from_none], obj.get("Level"))
        name = from_union([from_str, from_none], obj.get("Name"))
        url = from_union([from_str, from_none], obj.get("Url"))
        user_id = from_union([from_str, from_none], obj.get("UserId"))
        return NotificationDto(date, description, id, is_read, level, name, url, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Date"] = from_union([lambda x: x.isoformat(), from_none], self.date)
        result["Description"] = from_union([from_str, from_none], self.description)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["IsRead"] = from_union([from_bool, from_none], self.is_read)
        result["Level"] = from_union([lambda x: to_enum(Level, x), from_none], self.level)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Url"] = from_union([from_str, from_none], self.url)
        result["UserId"] = from_union([from_str, from_none], self.user_id)
        return result


