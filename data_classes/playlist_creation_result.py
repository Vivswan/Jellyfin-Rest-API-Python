from util.from_type import *


@dataclass
class PlaylistCreationResult:
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlaylistCreationResult':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("Id"))
        return PlaylistCreationResult(id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_str, from_none], self.id)
        return result


