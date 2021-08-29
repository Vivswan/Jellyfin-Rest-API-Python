from util.from_type import *
from data_classes.search_hint import SearchHint


@dataclass
class SearchHintResult:
    """Class SearchHintResult."""
    """Gets or sets the search hints."""
    search_hints: Optional[List[SearchHint]] = None
    """Gets or sets the total record count."""
    total_record_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SearchHintResult':
        assert isinstance(obj, dict)
        search_hints = from_union([lambda x: from_list(SearchHint.from_dict, x), from_none], obj.get("SearchHints"))
        total_record_count = from_union([from_int, from_none], obj.get("TotalRecordCount"))
        return SearchHintResult(search_hints, total_record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SearchHints"] = from_union([lambda x: from_list(lambda x: to_class(SearchHint, x), x), from_none], self.search_hints)
        result["TotalRecordCount"] = from_union([from_int, from_none], self.total_record_count)
        return result


