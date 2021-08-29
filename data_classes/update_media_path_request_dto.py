from util.from_type import *
from data_classes.path_info import PathInfo


@dataclass
class UpdateMediaPathRequestDto:
    """Update library options dto."""
    """Gets or sets the library name."""
    name: str
    """Gets or sets library folder path information."""
    path_info: PathInfo

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateMediaPathRequestDto':
        assert isinstance(obj, dict)
        name = from_str(obj.get("Name"))
        path_info = PathInfo.from_dict(obj.get("PathInfo"))
        return UpdateMediaPathRequestDto(name, path_info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_str(self.name)
        result["PathInfo"] = to_class(PathInfo, self.path_info)
        return result


