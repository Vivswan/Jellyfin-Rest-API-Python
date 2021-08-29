from data_classes.channel_media_type_element import ChannelMediaTypeElement
from util.from_type import *


@dataclass
class DirectPlayProfile:
    audio_codec: Optional[str] = None
    container: Optional[str] = None
    type: Optional[ChannelMediaTypeElement] = None
    video_codec: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DirectPlayProfile':
        assert isinstance(obj, dict)
        audio_codec = from_union([from_str, from_none], obj.get("AudioCodec"))
        container = from_union([from_str, from_none], obj.get("Container"))
        type = from_union([ChannelMediaTypeElement, from_none], obj.get("Type"))
        video_codec = from_union([from_str, from_none], obj.get("VideoCodec"))
        return DirectPlayProfile(audio_codec, container, type, video_codec)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioCodec"] = from_union([from_str, from_none], self.audio_codec)
        result["Container"] = from_union([from_str, from_none], self.container)
        result["Type"] = from_union([lambda x: to_enum(ChannelMediaTypeElement, x), from_none], self.type)
        result["VideoCodec"] = from_union([from_str, from_none], self.video_codec)
        return result


