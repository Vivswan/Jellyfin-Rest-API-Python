from util.from_type import *


@dataclass
class DeviceOptions:
    custom_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceOptions':
        assert isinstance(obj, dict)
        custom_name = from_union([from_str, from_none], obj.get("CustomName"))
        return DeviceOptions(custom_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CustomName"] = from_union([from_str, from_none], self.custom_name)
        return result


