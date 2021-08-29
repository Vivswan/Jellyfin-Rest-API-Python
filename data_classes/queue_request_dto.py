from util.from_type import *
from data_classes.group_queue_mode_enum import GroupQueueModeEnum


@dataclass
class QueueRequestDto:
    """Class QueueRequestDto."""
    """Gets or sets the items to enqueue."""
    item_ids: Optional[List[UUID]] = None
    """Gets or sets the mode in which to add the new items."""
    mode: Optional[GroupQueueModeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QueueRequestDto':
        assert isinstance(obj, dict)
        item_ids = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("ItemIds"))
        mode = from_union([GroupQueueModeEnum, from_none], obj.get("Mode"))
        return QueueRequestDto(item_ids, mode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ItemIds"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.item_ids)
        result["Mode"] = from_union([lambda x: to_enum(GroupQueueModeEnum, x), from_none], self.mode)
        return result


