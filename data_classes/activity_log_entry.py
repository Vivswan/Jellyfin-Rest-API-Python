from data_classes.severity import Severity
from util.from_type import *


@dataclass
class ActivityLogEntry:
    """Gets or sets the date."""
    date: Optional[datetime] = None
    """Gets or sets the identifier."""
    id: Optional[int] = None
    """Gets or sets the item identifier."""
    item_id: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the overview."""
    overview: Optional[str] = None
    """Gets or sets the log severity."""
    severity: Optional[Severity] = None
    """Gets or sets the short overview."""
    short_overview: Optional[str] = None
    """Gets or sets the type."""
    type: Optional[str] = None
    """Gets or sets the user identifier."""
    user_id: Optional[UUID] = None
    """Gets or sets the user primary image tag."""
    user_primary_image_tag: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActivityLogEntry':
        assert isinstance(obj, dict)
        date = from_union([from_datetime, from_none], obj.get("Date"))
        id = from_union([from_int, from_none], obj.get("Id"))
        item_id = from_union([from_str, from_none], obj.get("ItemId"))
        name = from_union([from_str, from_none], obj.get("Name"))
        overview = from_union([from_str, from_none], obj.get("Overview"))
        severity = from_union([Severity, from_none], obj.get("Severity"))
        short_overview = from_union([from_str, from_none], obj.get("ShortOverview"))
        type = from_union([from_str, from_none], obj.get("Type"))
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        user_primary_image_tag = from_union([from_str, from_none], obj.get("UserPrimaryImageTag"))
        return ActivityLogEntry(date, id, item_id, name, overview, severity, short_overview, type, user_id, user_primary_image_tag)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Date"] = from_union([lambda x: x.isoformat(), from_none], self.date)
        result["Id"] = from_union([from_int, from_none], self.id)
        result["ItemId"] = from_union([from_str, from_none], self.item_id)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Overview"] = from_union([from_str, from_none], self.overview)
        result["Severity"] = from_union([lambda x: to_enum(Severity, x), from_none], self.severity)
        result["ShortOverview"] = from_union([from_str, from_none], self.short_overview)
        result["Type"] = from_union([from_str, from_none], self.type)
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        result["UserPrimaryImageTag"] = from_union([from_str, from_none], self.user_primary_image_tag)
        return result


