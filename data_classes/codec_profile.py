from data_classes.codec_type_enum import CodecTypeEnum
from data_classes.profile_condition import ProfileCondition
from util.from_type import *


@dataclass
class CodecProfile:
    apply_conditions: Optional[List[ProfileCondition]] = None
    codec: Optional[str] = None
    conditions: Optional[List[ProfileCondition]] = None
    container: Optional[str] = None
    type: Optional[CodecTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CodecProfile':
        assert isinstance(obj, dict)
        apply_conditions = from_union([lambda x: from_list(ProfileCondition.from_dict, x), from_none], obj.get("ApplyConditions"))
        codec = from_union([from_str, from_none], obj.get("Codec"))
        conditions = from_union([lambda x: from_list(ProfileCondition.from_dict, x), from_none], obj.get("Conditions"))
        container = from_union([from_str, from_none], obj.get("Container"))
        type = from_union([CodecTypeEnum, from_none], obj.get("Type"))
        return CodecProfile(apply_conditions, codec, conditions, container, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ApplyConditions"] = from_union([lambda x: from_list(lambda x: to_class(ProfileCondition, x), x), from_none], self.apply_conditions)
        result["Codec"] = from_union([from_str, from_none], self.codec)
        result["Conditions"] = from_union([lambda x: from_list(lambda x: to_class(ProfileCondition, x), x), from_none], self.conditions)
        result["Container"] = from_union([from_str, from_none], self.container)
        result["Type"] = from_union([lambda x: to_enum(CodecTypeEnum, x), from_none], self.type)
        return result


