from util.from_type import *
from data_classes.channel_media_type_element import ChannelMediaTypeElement
from data_classes.context import Context
from data_classes.transcode_seek_info import TranscodeSeekInfo


@dataclass
class TranscodingProfile:
    audio_codec: Optional[str] = None
    break_on_non_key_frames: Optional[bool] = None
    container: Optional[str] = None
    context: Optional[Context] = None
    copy_timestamps: Optional[bool] = None
    enable_mpegts_m2_ts_mode: Optional[bool] = None
    enable_subtitles_in_manifest: Optional[bool] = None
    estimate_content_length: Optional[bool] = None
    max_audio_channels: Optional[str] = None
    min_segments: Optional[int] = None
    protocol: Optional[str] = None
    segment_length: Optional[int] = None
    transcode_seek_info: Optional[TranscodeSeekInfo] = None
    type: Optional[ChannelMediaTypeElement] = None
    video_codec: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TranscodingProfile':
        assert isinstance(obj, dict)
        audio_codec = from_union([from_str, from_none], obj.get("AudioCodec"))
        break_on_non_key_frames = from_union([from_bool, from_none], obj.get("BreakOnNonKeyFrames"))
        container = from_union([from_str, from_none], obj.get("Container"))
        context = from_union([Context, from_none], obj.get("Context"))
        copy_timestamps = from_union([from_bool, from_none], obj.get("CopyTimestamps"))
        enable_mpegts_m2_ts_mode = from_union([from_bool, from_none], obj.get("EnableMpegtsM2TsMode"))
        enable_subtitles_in_manifest = from_union([from_bool, from_none], obj.get("EnableSubtitlesInManifest"))
        estimate_content_length = from_union([from_bool, from_none], obj.get("EstimateContentLength"))
        max_audio_channels = from_union([from_str, from_none], obj.get("MaxAudioChannels"))
        min_segments = from_union([from_int, from_none], obj.get("MinSegments"))
        protocol = from_union([from_str, from_none], obj.get("Protocol"))
        segment_length = from_union([from_int, from_none], obj.get("SegmentLength"))
        transcode_seek_info = from_union([TranscodeSeekInfo, from_none], obj.get("TranscodeSeekInfo"))
        type = from_union([ChannelMediaTypeElement, from_none], obj.get("Type"))
        video_codec = from_union([from_str, from_none], obj.get("VideoCodec"))
        return TranscodingProfile(audio_codec, break_on_non_key_frames, container, context, copy_timestamps, enable_mpegts_m2_ts_mode, enable_subtitles_in_manifest, estimate_content_length, max_audio_channels, min_segments, protocol, segment_length, transcode_seek_info, type, video_codec)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioCodec"] = from_union([from_str, from_none], self.audio_codec)
        result["BreakOnNonKeyFrames"] = from_union([from_bool, from_none], self.break_on_non_key_frames)
        result["Container"] = from_union([from_str, from_none], self.container)
        result["Context"] = from_union([lambda x: to_enum(Context, x), from_none], self.context)
        result["CopyTimestamps"] = from_union([from_bool, from_none], self.copy_timestamps)
        result["EnableMpegtsM2TsMode"] = from_union([from_bool, from_none], self.enable_mpegts_m2_ts_mode)
        result["EnableSubtitlesInManifest"] = from_union([from_bool, from_none], self.enable_subtitles_in_manifest)
        result["EstimateContentLength"] = from_union([from_bool, from_none], self.estimate_content_length)
        result["MaxAudioChannels"] = from_union([from_str, from_none], self.max_audio_channels)
        result["MinSegments"] = from_union([from_int, from_none], self.min_segments)
        result["Protocol"] = from_union([from_str, from_none], self.protocol)
        result["SegmentLength"] = from_union([from_int, from_none], self.segment_length)
        result["TranscodeSeekInfo"] = from_union([lambda x: to_enum(TranscodeSeekInfo, x), from_none], self.transcode_seek_info)
        result["Type"] = from_union([lambda x: to_enum(ChannelMediaTypeElement, x), from_none], self.type)
        result["VideoCodec"] = from_union([from_str, from_none], self.video_codec)
        return result


