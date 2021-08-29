from util.from_type import *
from data_classes.condition import Condition
from data_classes.pro import Pro


@dataclass
class ProfileCondition:
    condition: Optional[Condition] = None
    is_required: Optional[bool] = None
    property: Optional[Pro] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileCondition':
        assert isinstance(obj, dict)
        condition = from_union([Condition, from_none], obj.get("Condition"))
        is_required = from_union([from_bool, from_none], obj.get("IsRequired"))
        property = from_union([Pro, from_none], obj.get("Property"))
        value = from_union([from_str, from_none], obj.get("Value"))
        return ProfileCondition(condition, is_required, property, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Condition"] = from_union([lambda x: to_enum(Condition, x), from_none], self.condition)
        result["IsRequired"] = from_union([from_bool, from_none], self.is_required)
        result["Property"] = from_union([lambda x: to_enum(Pro, x), from_none], self.property)
        result["Value"] = from_union([from_str, from_none], self.value)
        return result


