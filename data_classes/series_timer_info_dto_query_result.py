from util.from_type import *
from data_classes.series_timer_info_dto import SeriesTimerInfoDto


@dataclass
class SeriesTimerInfoDtoQueryResult:
    """Gets or sets the items."""
    items: Optional[List[SeriesTimerInfoDto]] = None
    """The index of the first record in Items."""
    start_index: Optional[int] = None
    """The total number of records available."""
    total_record_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SeriesTimerInfoDtoQueryResult':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(SeriesTimerInfoDto.from_dict, x), from_none], obj.get("Items"))
        start_index = from_union([from_int, from_none], obj.get("StartIndex"))
        total_record_count = from_union([from_int, from_none], obj.get("TotalRecordCount"))
        return SeriesTimerInfoDtoQueryResult(items, start_index, total_record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Items"] = from_union([lambda x: from_list(lambda x: to_class(SeriesTimerInfoDto, x), x), from_none], self.items)
        result["StartIndex"] = from_union([from_int, from_none], self.start_index)
        result["TotalRecordCount"] = from_union([from_int, from_none], self.total_record_count)
        return result


