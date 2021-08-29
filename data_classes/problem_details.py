from util.from_type import *


@dataclass
class ProblemDetails:
    detail: Optional[str] = None
    instance: Optional[str] = None
    status: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProblemDetails':
        assert isinstance(obj, dict)
        detail = from_union([from_str, from_none], obj.get("detail"))
        instance = from_union([from_str, from_none], obj.get("instance"))
        status = from_union([from_int, from_none], obj.get("status"))
        title = from_union([from_str, from_none], obj.get("title"))
        type = from_union([from_str, from_none], obj.get("type"))
        return ProblemDetails(detail, instance, status, title, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["detail"] = from_union([from_str, from_none], self.detail)
        result["instance"] = from_union([from_str, from_none], self.instance)
        result["status"] = from_union([from_int, from_none], self.status)
        result["title"] = from_union([from_str, from_none], self.title)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


