from util.from_type import *


@dataclass
class CollectionCreationResult:
    id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CollectionCreationResult':
        assert isinstance(obj, dict)
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        return CollectionCreationResult(id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        return result


