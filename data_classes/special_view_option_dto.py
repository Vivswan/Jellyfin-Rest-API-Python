from util.from_type import *


@dataclass
class SpecialViewOptionDto:
    """Special view option dto."""
    """Gets or sets view option id."""
    id: Optional[str] = None
    """Gets or sets view option name."""
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SpecialViewOptionDto':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("Id"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return SpecialViewOptionDto(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_str, from_none], self.id)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


