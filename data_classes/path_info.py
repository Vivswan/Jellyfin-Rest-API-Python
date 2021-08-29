from util.from_type import *


@dataclass
class PathInfo:
    """Gets or sets the path info.
    
    Gets or sets library folder path information.
    """
    network_path: Optional[str] = None
    path: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PathInfo':
        assert isinstance(obj, dict)
        network_path = from_union([from_str, from_none], obj.get("NetworkPath"))
        path = from_union([from_str, from_none], obj.get("Path"))
        return PathInfo(network_path, path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["NetworkPath"] = from_union([from_str, from_none], self.network_path)
        result["Path"] = from_union([from_str, from_none], self.path)
        return result


