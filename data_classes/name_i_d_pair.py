from util.from_type import *


@dataclass
class NameIDPair:
    """Gets or sets the identifier."""
    id: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NameIDPair':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("Id"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return NameIDPair(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_str, from_none], self.id)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


