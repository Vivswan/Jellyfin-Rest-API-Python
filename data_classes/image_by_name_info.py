from util.from_type import *


@dataclass
class ImageByNameInfo:
    """Gets or sets the context."""
    context: Optional[str] = None
    """Gets or sets the length of the file."""
    file_length: Optional[int] = None
    """Gets or sets the format."""
    format: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the theme."""
    theme: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageByNameInfo':
        assert isinstance(obj, dict)
        context = from_union([from_str, from_none], obj.get("Context"))
        file_length = from_union([from_int, from_none], obj.get("FileLength"))
        format = from_union([from_str, from_none], obj.get("Format"))
        name = from_union([from_str, from_none], obj.get("Name"))
        theme = from_union([from_str, from_none], obj.get("Theme"))
        return ImageByNameInfo(context, file_length, format, name, theme)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Context"] = from_union([from_str, from_none], self.context)
        result["FileLength"] = from_union([from_int, from_none], self.file_length)
        result["Format"] = from_union([from_str, from_none], self.format)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Theme"] = from_union([from_str, from_none], self.theme)
        return result


