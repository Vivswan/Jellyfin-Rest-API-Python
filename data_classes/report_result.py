from util.from_type import *
from data_classes.report_row import ReportRow
from data_classes.report_group import ReportGroup
from data_classes.report_header import ReportHeader


@dataclass
class ReportResult:
    groups: Optional[List[ReportGroup]] = None
    headers: Optional[List[ReportHeader]] = None
    is_grouped: Optional[bool] = None
    rows: Optional[List[ReportRow]] = None
    total_record_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReportResult':
        assert isinstance(obj, dict)
        groups = from_union([lambda x: from_list(ReportGroup.from_dict, x), from_none], obj.get("Groups"))
        headers = from_union([lambda x: from_list(ReportHeader.from_dict, x), from_none], obj.get("Headers"))
        is_grouped = from_union([from_bool, from_none], obj.get("IsGrouped"))
        rows = from_union([lambda x: from_list(ReportRow.from_dict, x), from_none], obj.get("Rows"))
        total_record_count = from_union([from_int, from_none], obj.get("TotalRecordCount"))
        return ReportResult(groups, headers, is_grouped, rows, total_record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Groups"] = from_union([lambda x: from_list(lambda x: to_class(ReportGroup, x), x), from_none], self.groups)
        result["Headers"] = from_union([lambda x: from_list(lambda x: to_class(ReportHeader, x), x), from_none], self.headers)
        result["IsGrouped"] = from_union([from_bool, from_none], self.is_grouped)
        result["Rows"] = from_union([lambda x: from_list(lambda x: to_class(ReportRow, x), x), from_none], self.rows)
        result["TotalRecordCount"] = from_union([from_int, from_none], self.total_record_count)
        return result


