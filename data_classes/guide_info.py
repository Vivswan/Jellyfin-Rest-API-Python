from util.from_type import *


@dataclass
class GuideInfo:
    """Gets or sets the end date."""
    end_date: Optional[datetime] = None
    """Gets or sets the start date."""
    start_date: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GuideInfo':
        assert isinstance(obj, dict)
        end_date = from_union([from_datetime, from_none], obj.get("EndDate"))
        start_date = from_union([from_datetime, from_none], obj.get("StartDate"))
        return GuideInfo(end_date, start_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EndDate"] = from_union([lambda x: x.isoformat(), from_none], self.end_date)
        result["StartDate"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        return result


