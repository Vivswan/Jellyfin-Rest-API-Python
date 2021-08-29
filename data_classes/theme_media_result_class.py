from util.from_type import *
from data_classes.base_item_dto import BaseItemDto


@dataclass
class ThemeMediaResultClass:
    """Class ThemeMediaResult."""
    """Gets or sets the items."""
    items: Optional[List[BaseItemDto]] = None
    """Gets or sets the owner id."""
    owner_id: Optional[UUID] = None
    """The index of the first record in Items."""
    start_index: Optional[int] = None
    """The total number of records available."""
    total_record_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ThemeMediaResultClass':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(BaseItemDto.from_dict, x), from_none], obj.get("Items"))
        owner_id = from_union([lambda x: UUID(x), from_none], obj.get("OwnerId"))
        start_index = from_union([from_int, from_none], obj.get("StartIndex"))
        total_record_count = from_union([from_int, from_none], obj.get("TotalRecordCount"))
        return ThemeMediaResultClass(items, owner_id, start_index, total_record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Items"] = from_union([lambda x: from_list(lambda x: to_class(BaseItemDto, x), x), from_none], self.items)
        result["OwnerId"] = from_union([lambda x: str(x), from_none], self.owner_id)
        result["StartIndex"] = from_union([from_int, from_none], self.start_index)
        result["TotalRecordCount"] = from_union([from_int, from_none], self.total_record_count)
        return result


