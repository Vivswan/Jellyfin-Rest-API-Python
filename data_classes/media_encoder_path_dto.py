from util.from_type import *


@dataclass
class MediaEncoderPathDto:
    """Media Encoder Path Dto."""
    """Gets or sets media encoder path."""
    path: Optional[str] = None
    """Gets or sets media encoder path type."""
    path_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaEncoderPathDto':
        assert isinstance(obj, dict)
        path = from_union([from_str, from_none], obj.get("Path"))
        path_type = from_union([from_str, from_none], obj.get("PathType"))
        return MediaEncoderPathDto(path, path_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Path"] = from_union([from_str, from_none], self.path)
        result["PathType"] = from_union([from_str, from_none], self.path_type)
        return result


