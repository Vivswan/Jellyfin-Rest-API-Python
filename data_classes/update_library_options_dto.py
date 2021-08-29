from util.from_type import *
from data_classes.library_options import LibraryOptions


@dataclass
class UpdateLibraryOptionsDto:
    """Update library options dto."""
    """Gets or sets the library item id."""
    id: Optional[UUID] = None
    """Gets or sets library options."""
    library_options: Optional[LibraryOptions] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateLibraryOptionsDto':
        assert isinstance(obj, dict)
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        library_options = from_union([LibraryOptions.from_dict, from_none], obj.get("LibraryOptions"))
        return UpdateLibraryOptionsDto(id, library_options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["LibraryOptions"] = from_union([lambda x: to_class(LibraryOptions, x), from_none], self.library_options)
        return result


