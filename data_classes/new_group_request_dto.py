from util.from_type import *


@dataclass
class NewGroupRequestDto:
    """Class NewGroupRequestDto."""
    """Gets or sets the group name."""
    group_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NewGroupRequestDto':
        assert isinstance(obj, dict)
        group_name = from_union([from_str, from_none], obj.get("GroupName"))
        return NewGroupRequestDto(group_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["GroupName"] = from_union([from_str, from_none], self.group_name)
        return result


