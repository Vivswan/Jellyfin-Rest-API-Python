from util.from_type import *


@dataclass
class ValidatePathDto:
    """Validate path object."""
    """Gets or sets is path file."""
    is_file: Optional[bool] = None
    """Gets or sets the path."""
    path: Optional[str] = None
    """Gets or sets a value indicating whether validate if path is writable."""
    validate_writable: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ValidatePathDto':
        assert isinstance(obj, dict)
        is_file = from_union([from_bool, from_none], obj.get("IsFile"))
        path = from_union([from_str, from_none], obj.get("Path"))
        validate_writable = from_union([from_bool, from_none], obj.get("ValidateWritable"))
        return ValidatePathDto(is_file, path, validate_writable)

    def to_dict(self) -> dict:
        result: dict = {}
        result["IsFile"] = from_union([from_bool, from_none], self.is_file)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["ValidateWritable"] = from_union([from_bool, from_none], self.validate_writable)
        return result


