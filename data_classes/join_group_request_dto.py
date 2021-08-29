from util.from_type import *


@dataclass
class JoinGroupRequestDto:
    """Class JoinGroupRequestDto."""
    """Gets or sets the group identifier."""
    group_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'JoinGroupRequestDto':
        assert isinstance(obj, dict)
        group_id = from_union([lambda x: UUID(x), from_none], obj.get("GroupId"))
        return JoinGroupRequestDto(group_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["GroupId"] = from_union([lambda x: str(x), from_none], self.group_id)
        return result


