from data_classes.group_state_type_enum import GroupStateTypeEnum
from util.from_type import *


@dataclass
class GroupInfoDto:
    """Class GroupInfoDto."""
    """Gets the group identifier."""
    group_id: Optional[UUID] = None
    """Gets the group name."""
    group_name: Optional[str] = None
    """Gets the date when this DTO has been created."""
    last_updated_at: Optional[datetime] = None
    """Gets the participants."""
    participants: Optional[List[str]] = None
    """Gets the group state."""
    state: Optional[GroupStateTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GroupInfoDto':
        assert isinstance(obj, dict)
        group_id = from_union([lambda x: UUID(x), from_none], obj.get("GroupId"))
        group_name = from_union([from_str, from_none], obj.get("GroupName"))
        last_updated_at = from_union([from_datetime, from_none], obj.get("LastUpdatedAt"))
        participants = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Participants"))
        state = from_union([GroupStateTypeEnum, from_none], obj.get("State"))
        return GroupInfoDto(group_id, group_name, last_updated_at, participants, state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["GroupId"] = from_union([lambda x: str(x), from_none], self.group_id)
        result["GroupName"] = from_union([from_str, from_none], self.group_name)
        result["LastUpdatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.last_updated_at)
        result["Participants"] = from_union([lambda x: from_list(from_str, x), from_none], self.participants)
        result["State"] = from_union([lambda x: to_enum(GroupStateTypeEnum, x), from_none], self.state)
        return result


