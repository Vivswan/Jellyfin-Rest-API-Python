from util.from_type import *
from data_classes.profile_condition import ProfileCondition
from data_classes.channel_media_type_element import ChannelMediaTypeElement


@dataclass
class ResponseProfile:
    audio_codec: Optional[str] = None
    conditions: Optional[List[ProfileCondition]] = None
    container: Optional[str] = None
    mime_type: Optional[str] = None
    org_pn: Optional[str] = None
    type: Optional[ChannelMediaTypeElement] = None
    video_codec: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseProfile':
        assert isinstance(obj, dict)
        audio_codec = from_union([from_str, from_none], obj.get("AudioCodec"))
        conditions = from_union([lambda x: from_list(ProfileCondition.from_dict, x), from_none], obj.get("Conditions"))
        container = from_union([from_str, from_none], obj.get("Container"))
        mime_type = from_union([from_str, from_none], obj.get("MimeType"))
        org_pn = from_union([from_str, from_none], obj.get("OrgPn"))
        type = from_union([ChannelMediaTypeElement, from_none], obj.get("Type"))
        video_codec = from_union([from_str, from_none], obj.get("VideoCodec"))
        return ResponseProfile(audio_codec, conditions, container, mime_type, org_pn, type, video_codec)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioCodec"] = from_union([from_str, from_none], self.audio_codec)
        result["Conditions"] = from_union([lambda x: from_list(lambda x: to_class(ProfileCondition, x), x), from_none], self.conditions)
        result["Container"] = from_union([from_str, from_none], self.container)
        result["MimeType"] = from_union([from_str, from_none], self.mime_type)
        result["OrgPn"] = from_union([from_str, from_none], self.org_pn)
        result["Type"] = from_union([lambda x: to_enum(ChannelMediaTypeElement, x), from_none], self.type)
        result["VideoCodec"] = from_union([from_str, from_none], self.video_codec)
        return result


