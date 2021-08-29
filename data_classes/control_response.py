from util.from_type import *


@dataclass
class ControlResponse:
    headers: Optional[Dict[str, str]] = None
    is_successful: Optional[bool] = None
    xml: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ControlResponse':
        assert isinstance(obj, dict)
        headers = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Headers"))
        is_successful = from_union([from_bool, from_none], obj.get("IsSuccessful"))
        xml = from_union([from_str, from_none], obj.get("Xml"))
        return ControlResponse(headers, is_successful, xml)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Headers"] = from_union([lambda x: from_dict(from_str, x), from_none], self.headers)
        result["IsSuccessful"] = from_union([from_bool, from_none], self.is_successful)
        result["Xml"] = from_union([from_str, from_none], self.xml)
        return result


