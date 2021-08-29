from util.from_type import *
from data_classes.transcode_reason import TranscodeReason


@dataclass
class TranscodingInfo:
    audio_channels: Optional[int] = None
    audio_codec: Optional[str] = None
    bitrate: Optional[int] = None
    completion_percentage: Optional[float] = None
    container: Optional[str] = None
    framerate: Optional[float] = None
    height: Optional[int] = None
    is_audio_direct: Optional[bool] = None
    is_video_direct: Optional[bool] = None
    transcode_reasons: Optional[List[TranscodeReason]] = None
    video_codec: Optional[str] = None
    width: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TranscodingInfo':
        assert isinstance(obj, dict)
        audio_channels = from_union([from_int, from_none], obj.get("AudioChannels"))
        audio_codec = from_union([from_str, from_none], obj.get("AudioCodec"))
        bitrate = from_union([from_int, from_none], obj.get("Bitrate"))
        completion_percentage = from_union([from_float, from_none], obj.get("CompletionPercentage"))
        container = from_union([from_str, from_none], obj.get("Container"))
        framerate = from_union([from_float, from_none], obj.get("Framerate"))
        height = from_union([from_int, from_none], obj.get("Height"))
        is_audio_direct = from_union([from_bool, from_none], obj.get("IsAudioDirect"))
        is_video_direct = from_union([from_bool, from_none], obj.get("IsVideoDirect"))
        transcode_reasons = from_union([lambda x: from_list(TranscodeReason, x), from_none], obj.get("TranscodeReasons"))
        video_codec = from_union([from_str, from_none], obj.get("VideoCodec"))
        width = from_union([from_int, from_none], obj.get("Width"))
        return TranscodingInfo(audio_channels, audio_codec, bitrate, completion_percentage, container, framerate, height, is_audio_direct, is_video_direct, transcode_reasons, video_codec, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioChannels"] = from_union([from_int, from_none], self.audio_channels)
        result["AudioCodec"] = from_union([from_str, from_none], self.audio_codec)
        result["Bitrate"] = from_union([from_int, from_none], self.bitrate)
        result["CompletionPercentage"] = from_union([to_float, from_none], self.completion_percentage)
        result["Container"] = from_union([from_str, from_none], self.container)
        result["Framerate"] = from_union([to_float, from_none], self.framerate)
        result["Height"] = from_union([from_int, from_none], self.height)
        result["IsAudioDirect"] = from_union([from_bool, from_none], self.is_audio_direct)
        result["IsVideoDirect"] = from_union([from_bool, from_none], self.is_video_direct)
        result["TranscodeReasons"] = from_union([lambda x: from_list(lambda x: to_enum(TranscodeReason, x), x), from_none], self.transcode_reasons)
        result["VideoCodec"] = from_union([from_str, from_none], self.video_codec)
        result["Width"] = from_union([from_int, from_none], self.width)
        return result


