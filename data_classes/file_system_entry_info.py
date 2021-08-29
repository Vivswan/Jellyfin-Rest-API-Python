from data_classes.file_system_entry_type_enum import FileSystemEntryTypeEnum
from util.from_type import *


@dataclass
class FileSystemEntryInfo:
    """Class FileSystemEntryInfo."""
    """Gets the name."""
    name: Optional[str] = None
    """Gets the path."""
    path: Optional[str] = None
    """Gets the type."""
    type: Optional[FileSystemEntryTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FileSystemEntryInfo':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        path = from_union([from_str, from_none], obj.get("Path"))
        type = from_union([FileSystemEntryTypeEnum, from_none], obj.get("Type"))
        return FileSystemEntryInfo(name, path, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["Type"] = from_union([lambda x: to_enum(FileSystemEntryTypeEnum, x), from_none], self.type)
        return result


