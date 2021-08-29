from util.from_type import *


@dataclass
class LogFile:
    """Gets or sets the date created."""
    date_created: Optional[datetime] = None
    """Gets or sets the date modified."""
    date_modified: Optional[datetime] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the size."""
    size: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LogFile':
        assert isinstance(obj, dict)
        date_created = from_union([from_datetime, from_none], obj.get("DateCreated"))
        date_modified = from_union([from_datetime, from_none], obj.get("DateModified"))
        name = from_union([from_str, from_none], obj.get("Name"))
        size = from_union([from_int, from_none], obj.get("Size"))
        return LogFile(date_created, date_modified, name, size)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DateCreated"] = from_union([lambda x: x.isoformat(), from_none], self.date_created)
        result["DateModified"] = from_union([lambda x: x.isoformat(), from_none], self.date_modified)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Size"] = from_union([from_int, from_none], self.size)
        return result


