from data_classes.channel_media_type_element import ChannelMediaTypeElement
from data_classes.profile_condition import ProfileCondition
from util.from_type import *


@dataclass
class ContainerProfile:
    conditions: Optional[List[ProfileCondition]] = None
    container: Optional[str] = None
    type: Optional[ChannelMediaTypeElement] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ContainerProfile':
        assert isinstance(obj, dict)
        conditions = from_union([lambda x: from_list(ProfileCondition.from_dict, x), from_none], obj.get("Conditions"))
        container = from_union([from_str, from_none], obj.get("Container"))
        type = from_union([ChannelMediaTypeElement, from_none], obj.get("Type"))
        return ContainerProfile(conditions, container, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Conditions"] = from_union([lambda x: from_list(lambda x: to_class(ProfileCondition, x), x), from_none], self.conditions)
        result["Container"] = from_union([from_str, from_none], self.container)
        result["Type"] = from_union([lambda x: to_enum(ChannelMediaTypeElement, x), from_none], self.type)
        return result


