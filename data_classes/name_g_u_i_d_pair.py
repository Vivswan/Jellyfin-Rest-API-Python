from util.from_type import *


@dataclass
class NameGUIDPair:
    id: Optional[UUID] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NameGUIDPair':
        assert isinstance(obj, dict)
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return NameGUIDPair(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


