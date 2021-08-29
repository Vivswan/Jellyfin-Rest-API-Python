from data_classes.library_options import LibraryOptions
from util.from_type import *


@dataclass
class AddVirtualFolderDto:
    """Add virtual folder dto."""
    """Gets or sets library options."""
    library_options: Optional[LibraryOptions] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AddVirtualFolderDto':
        assert isinstance(obj, dict)
        library_options = from_union([LibraryOptions.from_dict, from_none], obj.get("LibraryOptions"))
        return AddVirtualFolderDto(library_options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["LibraryOptions"] = from_union([lambda x: to_class(LibraryOptions, x), from_none], self.library_options)
        return result


