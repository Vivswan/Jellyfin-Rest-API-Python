from data_classes.device_info import DeviceInfo
from util.from_type import *


@dataclass
class DeviceInfoQueryResult:
    """Gets or sets the items."""
    items: Optional[List[DeviceInfo]] = None
    """The index of the first record in Items."""
    start_index: Optional[int] = None
    """The total number of records available."""
    total_record_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceInfoQueryResult':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(DeviceInfo.from_dict, x), from_none], obj.get("Items"))
        start_index = from_union([from_int, from_none], obj.get("StartIndex"))
        total_record_count = from_union([from_int, from_none], obj.get("TotalRecordCount"))
        return DeviceInfoQueryResult(items, start_index, total_record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Items"] = from_union([lambda x: from_list(lambda x: to_class(DeviceInfo, x), x), from_none], self.items)
        result["StartIndex"] = from_union([from_int, from_none], self.start_index)
        result["TotalRecordCount"] = from_union([from_int, from_none], self.total_record_count)
        return result


