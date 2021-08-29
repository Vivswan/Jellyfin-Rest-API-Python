from util.from_type import *
from data_classes.path_info import PathInfo


@dataclass
class MediaPathDto:
    """Media Path dto."""
    """Gets or sets the name of the library."""
    name: str
    """Gets or sets the path to add."""
    path: Optional[str] = None
    """Gets or sets the path info."""
    path_info: Optional[PathInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaPathDto':
        assert isinstance(obj, dict)
        name = from_str(obj.get("Name"))
        path = from_union([from_str, from_none], obj.get("Path"))
        path_info = from_union([PathInfo.from_dict, from_none], obj.get("PathInfo"))
        return MediaPathDto(name, path, path_info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_str(self.name)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["PathInfo"] = from_union([lambda x: to_class(PathInfo, x), from_none], self.path_info)
        return result


