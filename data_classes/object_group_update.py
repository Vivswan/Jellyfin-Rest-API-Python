from util.from_type import *
from data_classes.group_update_type_enum import GroupUpdateTypeEnum


@dataclass
class ObjectGroupUpdate:
    """Class GroupUpdate."""
    """Gets the update data."""
    data: Any
    """Gets the group identifier."""
    group_id: Optional[UUID] = None
    """Gets the update type."""
    type: Optional[GroupUpdateTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ObjectGroupUpdate':
        assert isinstance(obj, dict)
        data = obj.get("Data")
        group_id = from_union([lambda x: UUID(x), from_none], obj.get("GroupId"))
        type = from_union([GroupUpdateTypeEnum, from_none], obj.get("Type"))
        return ObjectGroupUpdate(data, group_id, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Data"] = self.data
        result["GroupId"] = from_union([lambda x: str(x), from_none], self.group_id)
        result["Type"] = from_union([lambda x: to_enum(GroupUpdateTypeEnum, x), from_none], self.type)
        return result


