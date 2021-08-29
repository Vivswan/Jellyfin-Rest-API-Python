from data_classes.device_profile_type_enum import DeviceProfileTypeEnum
from util.from_type import *


@dataclass
class DeviceProfileInfo:
    """Gets or sets the identifier."""
    id: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the type."""
    type: Optional[DeviceProfileTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceProfileInfo':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("Id"))
        name = from_union([from_str, from_none], obj.get("Name"))
        type = from_union([DeviceProfileTypeEnum, from_none], obj.get("Type"))
        return DeviceProfileInfo(id, name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_str, from_none], self.id)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Type"] = from_union([lambda x: to_enum(DeviceProfileTypeEnum, x), from_none], self.type)
        return result


