from util.from_type import *


@dataclass
class DefaultDirectoryBrowserInfoDto:
    """Default directory browser info."""
    """Gets or sets the path."""
    path: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DefaultDirectoryBrowserInfoDto':
        assert isinstance(obj, dict)
        path = from_union([from_str, from_none], obj.get("Path"))
        return DefaultDirectoryBrowserInfoDto(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Path"] = from_union([from_str, from_none], self.path)
        return result


