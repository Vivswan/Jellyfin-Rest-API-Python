from util.from_type import *
from data_classes.i_s_o_type import ISOType
from data_classes.protocol import Protocol
from data_classes.media_attachment import MediaAttachment
from data_classes.media_stream import MediaStream
from data_classes.timestamp import Timestamp
from data_classes.media_source_type_enum import MediaSourceTypeEnum
from data_classes.video3_d_format import Video3DFormat
from data_classes.video_type import VideoType


@dataclass
class MediaSource:
    analyze_duration_ms: Optional[int] = None
    bitrate: Optional[int] = None
    buffer_ms: Optional[int] = None
    container: Optional[str] = None
    default_audio_stream_index: Optional[int] = None
    default_subtitle_stream_index: Optional[int] = None
    encoder_path: Optional[str] = None
    encoder_protocol: Optional[Protocol] = None
    e_tag: Optional[str] = None
    formats: Optional[List[str]] = None
    gen_pts_input: Optional[bool] = None
    id: Optional[str] = None
    ignore_dts: Optional[bool] = None
    ignore_index: Optional[bool] = None
    is_infinite_stream: Optional[bool] = None
    iso_type: Optional[ISOType] = None
    """Differentiate internet url vs local network."""
    is_remote: Optional[bool] = None
    live_stream_id: Optional[str] = None
    media_attachments: Optional[List[MediaAttachment]] = None
    media_streams: Optional[List[MediaStream]] = None
    name: Optional[str] = None
    open_token: Optional[str] = None
    path: Optional[str] = None
    protocol: Optional[Protocol] = None
    read_at_native_framerate: Optional[bool] = None
    required_http_headers: Optional[Dict[str, str]] = None
    requires_closing: Optional[bool] = None
    requires_looping: Optional[bool] = None
    requires_opening: Optional[bool] = None
    run_time_ticks: Optional[int] = None
    size: Optional[int] = None
    supports_direct_play: Optional[bool] = None
    supports_direct_stream: Optional[bool] = None
    supports_probing: Optional[bool] = None
    supports_transcoding: Optional[bool] = None
    timestamp: Optional[Timestamp] = None
    transcoding_container: Optional[str] = None
    transcoding_sub_protocol: Optional[str] = None
    transcoding_url: Optional[str] = None
    type: Optional[MediaSourceTypeEnum] = None
    video3_d_format: Optional[Video3DFormat] = None
    video_type: Optional[VideoType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaSource':
        assert isinstance(obj, dict)
        analyze_duration_ms = from_union([from_int, from_none], obj.get("AnalyzeDurationMs"))
        bitrate = from_union([from_int, from_none], obj.get("Bitrate"))
        buffer_ms = from_union([from_int, from_none], obj.get("BufferMs"))
        container = from_union([from_str, from_none], obj.get("Container"))
        default_audio_stream_index = from_union([from_int, from_none], obj.get("DefaultAudioStreamIndex"))
        default_subtitle_stream_index = from_union([from_int, from_none], obj.get("DefaultSubtitleStreamIndex"))
        encoder_path = from_union([from_str, from_none], obj.get("EncoderPath"))
        encoder_protocol = from_union([Protocol, from_none], obj.get("EncoderProtocol"))
        e_tag = from_union([from_str, from_none], obj.get("ETag"))
        formats = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Formats"))
        gen_pts_input = from_union([from_bool, from_none], obj.get("GenPtsInput"))
        id = from_union([from_str, from_none], obj.get("Id"))
        ignore_dts = from_union([from_bool, from_none], obj.get("IgnoreDts"))
        ignore_index = from_union([from_bool, from_none], obj.get("IgnoreIndex"))
        is_infinite_stream = from_union([from_bool, from_none], obj.get("IsInfiniteStream"))
        iso_type = from_union([ISOType, from_none], obj.get("IsoType"))
        is_remote = from_union([from_bool, from_none], obj.get("IsRemote"))
        live_stream_id = from_union([from_str, from_none], obj.get("LiveStreamId"))
        media_attachments = from_union([lambda x: from_list(MediaAttachment.from_dict, x), from_none], obj.get("MediaAttachments"))
        media_streams = from_union([lambda x: from_list(MediaStream.from_dict, x), from_none], obj.get("MediaStreams"))
        name = from_union([from_str, from_none], obj.get("Name"))
        open_token = from_union([from_str, from_none], obj.get("OpenToken"))
        path = from_union([from_str, from_none], obj.get("Path"))
        protocol = from_union([Protocol, from_none], obj.get("Protocol"))
        read_at_native_framerate = from_union([from_bool, from_none], obj.get("ReadAtNativeFramerate"))
        required_http_headers = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("RequiredHttpHeaders"))
        requires_closing = from_union([from_bool, from_none], obj.get("RequiresClosing"))
        requires_looping = from_union([from_bool, from_none], obj.get("RequiresLooping"))
        requires_opening = from_union([from_bool, from_none], obj.get("RequiresOpening"))
        run_time_ticks = from_union([from_int, from_none], obj.get("RunTimeTicks"))
        size = from_union([from_int, from_none], obj.get("Size"))
        supports_direct_play = from_union([from_bool, from_none], obj.get("SupportsDirectPlay"))
        supports_direct_stream = from_union([from_bool, from_none], obj.get("SupportsDirectStream"))
        supports_probing = from_union([from_bool, from_none], obj.get("SupportsProbing"))
        supports_transcoding = from_union([from_bool, from_none], obj.get("SupportsTranscoding"))
        timestamp = from_union([Timestamp, from_none], obj.get("Timestamp"))
        transcoding_container = from_union([from_str, from_none], obj.get("TranscodingContainer"))
        transcoding_sub_protocol = from_union([from_str, from_none], obj.get("TranscodingSubProtocol"))
        transcoding_url = from_union([from_str, from_none], obj.get("TranscodingUrl"))
        type = from_union([MediaSourceTypeEnum, from_none], obj.get("Type"))
        video3_d_format = from_union([Video3DFormat, from_none], obj.get("Video3DFormat"))
        video_type = from_union([VideoType, from_none], obj.get("VideoType"))
        return MediaSource(analyze_duration_ms, bitrate, buffer_ms, container, default_audio_stream_index, default_subtitle_stream_index, encoder_path, encoder_protocol, e_tag, formats, gen_pts_input, id, ignore_dts, ignore_index, is_infinite_stream, iso_type, is_remote, live_stream_id, media_attachments, media_streams, name, open_token, path, protocol, read_at_native_framerate, required_http_headers, requires_closing, requires_looping, requires_opening, run_time_ticks, size, supports_direct_play, supports_direct_stream, supports_probing, supports_transcoding, timestamp, transcoding_container, transcoding_sub_protocol, transcoding_url, type, video3_d_format, video_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AnalyzeDurationMs"] = from_union([from_int, from_none], self.analyze_duration_ms)
        result["Bitrate"] = from_union([from_int, from_none], self.bitrate)
        result["BufferMs"] = from_union([from_int, from_none], self.buffer_ms)
        result["Container"] = from_union([from_str, from_none], self.container)
        result["DefaultAudioStreamIndex"] = from_union([from_int, from_none], self.default_audio_stream_index)
        result["DefaultSubtitleStreamIndex"] = from_union([from_int, from_none], self.default_subtitle_stream_index)
        result["EncoderPath"] = from_union([from_str, from_none], self.encoder_path)
        result["EncoderProtocol"] = from_union([lambda x: to_enum(Protocol, x), from_none], self.encoder_protocol)
        result["ETag"] = from_union([from_str, from_none], self.e_tag)
        result["Formats"] = from_union([lambda x: from_list(from_str, x), from_none], self.formats)
        result["GenPtsInput"] = from_union([from_bool, from_none], self.gen_pts_input)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["IgnoreDts"] = from_union([from_bool, from_none], self.ignore_dts)
        result["IgnoreIndex"] = from_union([from_bool, from_none], self.ignore_index)
        result["IsInfiniteStream"] = from_union([from_bool, from_none], self.is_infinite_stream)
        result["IsoType"] = from_union([lambda x: to_enum(ISOType, x), from_none], self.iso_type)
        result["IsRemote"] = from_union([from_bool, from_none], self.is_remote)
        result["LiveStreamId"] = from_union([from_str, from_none], self.live_stream_id)
        result["MediaAttachments"] = from_union([lambda x: from_list(lambda x: to_class(MediaAttachment, x), x), from_none], self.media_attachments)
        result["MediaStreams"] = from_union([lambda x: from_list(lambda x: to_class(MediaStream, x), x), from_none], self.media_streams)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["OpenToken"] = from_union([from_str, from_none], self.open_token)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["Protocol"] = from_union([lambda x: to_enum(Protocol, x), from_none], self.protocol)
        result["ReadAtNativeFramerate"] = from_union([from_bool, from_none], self.read_at_native_framerate)
        result["RequiredHttpHeaders"] = from_union([lambda x: from_dict(from_str, x), from_none], self.required_http_headers)
        result["RequiresClosing"] = from_union([from_bool, from_none], self.requires_closing)
        result["RequiresLooping"] = from_union([from_bool, from_none], self.requires_looping)
        result["RequiresOpening"] = from_union([from_bool, from_none], self.requires_opening)
        result["RunTimeTicks"] = from_union([from_int, from_none], self.run_time_ticks)
        result["Size"] = from_union([from_int, from_none], self.size)
        result["SupportsDirectPlay"] = from_union([from_bool, from_none], self.supports_direct_play)
        result["SupportsDirectStream"] = from_union([from_bool, from_none], self.supports_direct_stream)
        result["SupportsProbing"] = from_union([from_bool, from_none], self.supports_probing)
        result["SupportsTranscoding"] = from_union([from_bool, from_none], self.supports_transcoding)
        result["Timestamp"] = from_union([lambda x: to_enum(Timestamp, x), from_none], self.timestamp)
        result["TranscodingContainer"] = from_union([from_str, from_none], self.transcoding_container)
        result["TranscodingSubProtocol"] = from_union([from_str, from_none], self.transcoding_sub_protocol)
        result["TranscodingUrl"] = from_union([from_str, from_none], self.transcoding_url)
        result["Type"] = from_union([lambda x: to_enum(MediaSourceTypeEnum, x), from_none], self.type)
        result["Video3DFormat"] = from_union([lambda x: to_enum(Video3DFormat, x), from_none], self.video3_d_format)
        result["VideoType"] = from_union([lambda x: to_enum(VideoType, x), from_none], self.video_type)
        return result


