from util.from_type import *


@dataclass
class NotificationTypeInfo:
    category: Optional[str] = None
    enabled: Optional[bool] = None
    is_based_on_user_event: Optional[bool] = None
    name: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NotificationTypeInfo':
        assert isinstance(obj, dict)
        category = from_union([from_str, from_none], obj.get("Category"))
        enabled = from_union([from_bool, from_none], obj.get("Enabled"))
        is_based_on_user_event = from_union([from_bool, from_none], obj.get("IsBasedOnUserEvent"))
        name = from_union([from_str, from_none], obj.get("Name"))
        type = from_union([from_str, from_none], obj.get("Type"))
        return NotificationTypeInfo(category, enabled, is_based_on_user_event, name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Category"] = from_union([from_str, from_none], self.category)
        result["Enabled"] = from_union([from_bool, from_none], self.enabled)
        result["IsBasedOnUserEvent"] = from_union([from_bool, from_none], self.is_based_on_user_event)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Type"] = from_union([from_str, from_none], self.type)
        return result


