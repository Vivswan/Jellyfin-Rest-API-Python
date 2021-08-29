from util.from_type import *


@dataclass
class LocalizationOption:
    name: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LocalizationOption':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        value = from_union([from_str, from_none], obj.get("Value"))
        return LocalizationOption(name, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Value"] = from_union([from_str, from_none], self.value)
        return result


