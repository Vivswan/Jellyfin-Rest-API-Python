from data_classes.match import Match
from util.from_type import *


@dataclass
class HTTPHeaderInfo:
    match: Optional[Match] = None
    name: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HTTPHeaderInfo':
        assert isinstance(obj, dict)
        match = from_union([Match, from_none], obj.get("Match"))
        name = from_union([from_str, from_none], obj.get("Name"))
        value = from_union([from_str, from_none], obj.get("Value"))
        return HTTPHeaderInfo(match, name, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Match"] = from_union([lambda x: to_enum(Match, x), from_none], self.match)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Value"] = from_union([from_str, from_none], self.value)
        return result


