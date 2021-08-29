from data_classes.authentication_info import AuthenticationInfo
from util.from_type import *


@dataclass
class AuthenticationInfoQueryResult:
    """Gets or sets the items."""
    items: Optional[List[AuthenticationInfo]] = None
    """The index of the first record in Items."""
    start_index: Optional[int] = None
    """The total number of records available."""
    total_record_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticationInfoQueryResult':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(AuthenticationInfo.from_dict, x), from_none], obj.get("Items"))
        start_index = from_union([from_int, from_none], obj.get("StartIndex"))
        total_record_count = from_union([from_int, from_none], obj.get("TotalRecordCount"))
        return AuthenticationInfoQueryResult(items, start_index, total_record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Items"] = from_union([lambda x: from_list(lambda x: to_class(AuthenticationInfo, x), x), from_none], self.items)
        result["StartIndex"] = from_union([from_int, from_none], self.start_index)
        result["TotalRecordCount"] = from_union([from_int, from_none], self.total_record_count)
        return result


