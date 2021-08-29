from util.from_type import *


@dataclass
class MediaUpdateInfoPathDto:
    """The media update info path."""
    """Gets or sets media path."""
    path: Optional[str] = None
    """Gets or sets media update type.
    Created, Modified, Deleted.
    """
    update_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaUpdateInfoPathDto':
        assert isinstance(obj, dict)
        path = from_union([from_str, from_none], obj.get("Path"))
        update_type = from_union([from_str, from_none], obj.get("UpdateType"))
        return MediaUpdateInfoPathDto(path, update_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Path"] = from_union([from_str, from_none], self.path)
        result["UpdateType"] = from_union([from_str, from_none], self.update_type)
        return result


