from util.from_type import *
from data_classes.report_row import ReportRow


@dataclass
class ReportGroup:
    name: Optional[str] = None
    rows: Optional[List[ReportRow]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReportGroup':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        rows = from_union([lambda x: from_list(ReportRow.from_dict, x), from_none], obj.get("Rows"))
        return ReportGroup(name, rows)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Rows"] = from_union([lambda x: from_list(lambda x: to_class(ReportRow, x), x), from_none], self.rows)
        return result


