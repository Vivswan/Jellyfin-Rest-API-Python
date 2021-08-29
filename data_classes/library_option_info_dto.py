from util.from_type import *


@dataclass
class LibraryOptionInfoDto:
    """Library option info dto."""
    """Gets or sets a value indicating whether default enabled."""
    default_enabled: Optional[bool] = None
    """Gets or sets name."""
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LibraryOptionInfoDto':
        assert isinstance(obj, dict)
        default_enabled = from_union([from_bool, from_none], obj.get("DefaultEnabled"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return LibraryOptionInfoDto(default_enabled, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DefaultEnabled"] = from_union([from_bool, from_none], self.default_enabled)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


