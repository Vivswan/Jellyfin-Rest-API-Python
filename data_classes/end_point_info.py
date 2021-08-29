from util.from_type import *


@dataclass
class EndPointInfo:
    is_in_network: Optional[bool] = None
    is_local: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EndPointInfo':
        assert isinstance(obj, dict)
        is_in_network = from_union([from_bool, from_none], obj.get("IsInNetwork"))
        is_local = from_union([from_bool, from_none], obj.get("IsLocal"))
        return EndPointInfo(is_in_network, is_local)

    def to_dict(self) -> dict:
        result: dict = {}
        result["IsInNetwork"] = from_union([from_bool, from_none], self.is_in_network)
        result["IsLocal"] = from_union([from_bool, from_none], self.is_local)
        return result


