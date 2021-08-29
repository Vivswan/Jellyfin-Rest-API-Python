from util.from_type import *
from data_classes.method import Method
from data_classes.media_stream_type_enum import MediaStreamTypeEnum


@dataclass
class MediaStream:
    """Class MediaStream."""
    """Gets or sets the aspect ratio."""
    aspect_ratio: Optional[str] = None
    """Gets or sets the average frame rate."""
    average_frame_rate: Optional[float] = None
    """Gets or sets the bit depth."""
    bit_depth: Optional[int] = None
    """Gets or sets the bit rate."""
    bit_rate: Optional[int] = None
    """Gets or sets the channel layout."""
    channel_layout: Optional[str] = None
    """Gets or sets the channels."""
    channels: Optional[int] = None
    """Gets or sets the codec."""
    codec: Optional[str] = None
    """Gets or sets the codec tag."""
    codec_tag: Optional[str] = None
    """Gets or sets the codec time base."""
    codec_time_base: Optional[str] = None
    """Gets or sets the color primaries."""
    color_primaries: Optional[str] = None
    """Gets or sets the color range."""
    color_range: Optional[str] = None
    """Gets or sets the color space."""
    color_space: Optional[str] = None
    """Gets or sets the color transfer."""
    color_transfer: Optional[str] = None
    """Gets or sets the comment."""
    comment: Optional[str] = None
    """Gets or sets the method."""
    delivery_method: Optional[Method] = None
    """Gets or sets the delivery URL."""
    delivery_url: Optional[str] = None
    display_title: Optional[str] = None
    """Gets or sets the height."""
    height: Optional[int] = None
    """Gets or sets the index."""
    index: Optional[int] = None
    """Gets a value indicating whether this instance is anamorphic."""
    is_anamorphic: Optional[bool] = None
    is_avc: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is default."""
    is_default: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is external."""
    is_external: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is external URL."""
    is_external_url: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is forced."""
    is_forced: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is interlaced."""
    is_interlaced: Optional[bool] = None
    is_text_subtitle_stream: Optional[bool] = None
    """Gets or sets the language."""
    language: Optional[str] = None
    """Gets or sets the level."""
    level: Optional[float] = None
    localized_default: Optional[str] = None
    localized_forced: Optional[str] = None
    localized_undefined: Optional[str] = None
    nal_length_size: Optional[str] = None
    """Gets or sets the length of the packet."""
    packet_length: Optional[int] = None
    """Gets or sets the filename."""
    path: Optional[str] = None
    """Gets or sets the pixel format."""
    pixel_format: Optional[str] = None
    """Gets or sets the profile."""
    profile: Optional[str] = None
    """Gets or sets the real frame rate."""
    real_frame_rate: Optional[float] = None
    """Gets or sets the reference frames."""
    ref_frames: Optional[int] = None
    """Gets or sets the sample rate."""
    sample_rate: Optional[int] = None
    """Gets or sets the score."""
    score: Optional[int] = None
    """Gets or sets a value indicating whether [supports external stream]."""
    supports_external_stream: Optional[bool] = None
    """Gets or sets the time base."""
    time_base: Optional[str] = None
    """Gets or sets the title."""
    title: Optional[str] = None
    """Gets or sets the type."""
    type: Optional[MediaStreamTypeEnum] = None
    """Gets or sets the video range."""
    video_range: Optional[str] = None
    """Gets or sets the width."""
    width: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaStream':
        assert isinstance(obj, dict)
        aspect_ratio = from_union([from_str, from_none], obj.get("AspectRatio"))
        average_frame_rate = from_union([from_float, from_none], obj.get("AverageFrameRate"))
        bit_depth = from_union([from_int, from_none], obj.get("BitDepth"))
        bit_rate = from_union([from_int, from_none], obj.get("BitRate"))
        channel_layout = from_union([from_str, from_none], obj.get("ChannelLayout"))
        channels = from_union([from_int, from_none], obj.get("Channels"))
        codec = from_union([from_str, from_none], obj.get("Codec"))
        codec_tag = from_union([from_str, from_none], obj.get("CodecTag"))
        codec_time_base = from_union([from_str, from_none], obj.get("CodecTimeBase"))
        color_primaries = from_union([from_str, from_none], obj.get("ColorPrimaries"))
        color_range = from_union([from_str, from_none], obj.get("ColorRange"))
        color_space = from_union([from_str, from_none], obj.get("ColorSpace"))
        color_transfer = from_union([from_str, from_none], obj.get("ColorTransfer"))
        comment = from_union([from_str, from_none], obj.get("Comment"))
        delivery_method = from_union([Method, from_none], obj.get("DeliveryMethod"))
        delivery_url = from_union([from_str, from_none], obj.get("DeliveryUrl"))
        display_title = from_union([from_str, from_none], obj.get("DisplayTitle"))
        height = from_union([from_int, from_none], obj.get("Height"))
        index = from_union([from_int, from_none], obj.get("Index"))
        is_anamorphic = from_union([from_bool, from_none], obj.get("IsAnamorphic"))
        is_avc = from_union([from_bool, from_none], obj.get("IsAVC"))
        is_default = from_union([from_bool, from_none], obj.get("IsDefault"))
        is_external = from_union([from_bool, from_none], obj.get("IsExternal"))
        is_external_url = from_union([from_bool, from_none], obj.get("IsExternalUrl"))
        is_forced = from_union([from_bool, from_none], obj.get("IsForced"))
        is_interlaced = from_union([from_bool, from_none], obj.get("IsInterlaced"))
        is_text_subtitle_stream = from_union([from_bool, from_none], obj.get("IsTextSubtitleStream"))
        language = from_union([from_str, from_none], obj.get("Language"))
        level = from_union([from_float, from_none], obj.get("Level"))
        localized_default = from_union([from_str, from_none], obj.get("localizedDefault"))
        localized_forced = from_union([from_str, from_none], obj.get("localizedForced"))
        localized_undefined = from_union([from_str, from_none], obj.get("localizedUndefined"))
        nal_length_size = from_union([from_str, from_none], obj.get("NalLengthSize"))
        packet_length = from_union([from_int, from_none], obj.get("PacketLength"))
        path = from_union([from_str, from_none], obj.get("Path"))
        pixel_format = from_union([from_str, from_none], obj.get("PixelFormat"))
        profile = from_union([from_str, from_none], obj.get("Profile"))
        real_frame_rate = from_union([from_float, from_none], obj.get("RealFrameRate"))
        ref_frames = from_union([from_int, from_none], obj.get("RefFrames"))
        sample_rate = from_union([from_int, from_none], obj.get("SampleRate"))
        score = from_union([from_int, from_none], obj.get("Score"))
        supports_external_stream = from_union([from_bool, from_none], obj.get("SupportsExternalStream"))
        time_base = from_union([from_str, from_none], obj.get("TimeBase"))
        title = from_union([from_str, from_none], obj.get("Title"))
        type = from_union([MediaStreamTypeEnum, from_none], obj.get("Type"))
        video_range = from_union([from_str, from_none], obj.get("VideoRange"))
        width = from_union([from_int, from_none], obj.get("Width"))
        return MediaStream(aspect_ratio, average_frame_rate, bit_depth, bit_rate, channel_layout, channels, codec, codec_tag, codec_time_base, color_primaries, color_range, color_space, color_transfer, comment, delivery_method, delivery_url, display_title, height, index, is_anamorphic, is_avc, is_default, is_external, is_external_url, is_forced, is_interlaced, is_text_subtitle_stream, language, level, localized_default, localized_forced, localized_undefined, nal_length_size, packet_length, path, pixel_format, profile, real_frame_rate, ref_frames, sample_rate, score, supports_external_stream, time_base, title, type, video_range, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AspectRatio"] = from_union([from_str, from_none], self.aspect_ratio)
        result["AverageFrameRate"] = from_union([to_float, from_none], self.average_frame_rate)
        result["BitDepth"] = from_union([from_int, from_none], self.bit_depth)
        result["BitRate"] = from_union([from_int, from_none], self.bit_rate)
        result["ChannelLayout"] = from_union([from_str, from_none], self.channel_layout)
        result["Channels"] = from_union([from_int, from_none], self.channels)
        result["Codec"] = from_union([from_str, from_none], self.codec)
        result["CodecTag"] = from_union([from_str, from_none], self.codec_tag)
        result["CodecTimeBase"] = from_union([from_str, from_none], self.codec_time_base)
        result["ColorPrimaries"] = from_union([from_str, from_none], self.color_primaries)
        result["ColorRange"] = from_union([from_str, from_none], self.color_range)
        result["ColorSpace"] = from_union([from_str, from_none], self.color_space)
        result["ColorTransfer"] = from_union([from_str, from_none], self.color_transfer)
        result["Comment"] = from_union([from_str, from_none], self.comment)
        result["DeliveryMethod"] = from_union([lambda x: to_enum(Method, x), from_none], self.delivery_method)
        result["DeliveryUrl"] = from_union([from_str, from_none], self.delivery_url)
        result["DisplayTitle"] = from_union([from_str, from_none], self.display_title)
        result["Height"] = from_union([from_int, from_none], self.height)
        result["Index"] = from_union([from_int, from_none], self.index)
        result["IsAnamorphic"] = from_union([from_bool, from_none], self.is_anamorphic)
        result["IsAVC"] = from_union([from_bool, from_none], self.is_avc)
        result["IsDefault"] = from_union([from_bool, from_none], self.is_default)
        result["IsExternal"] = from_union([from_bool, from_none], self.is_external)
        result["IsExternalUrl"] = from_union([from_bool, from_none], self.is_external_url)
        result["IsForced"] = from_union([from_bool, from_none], self.is_forced)
        result["IsInterlaced"] = from_union([from_bool, from_none], self.is_interlaced)
        result["IsTextSubtitleStream"] = from_union([from_bool, from_none], self.is_text_subtitle_stream)
        result["Language"] = from_union([from_str, from_none], self.language)
        result["Level"] = from_union([to_float, from_none], self.level)
        result["localizedDefault"] = from_union([from_str, from_none], self.localized_default)
        result["localizedForced"] = from_union([from_str, from_none], self.localized_forced)
        result["localizedUndefined"] = from_union([from_str, from_none], self.localized_undefined)
        result["NalLengthSize"] = from_union([from_str, from_none], self.nal_length_size)
        result["PacketLength"] = from_union([from_int, from_none], self.packet_length)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["PixelFormat"] = from_union([from_str, from_none], self.pixel_format)
        result["Profile"] = from_union([from_str, from_none], self.profile)
        result["RealFrameRate"] = from_union([to_float, from_none], self.real_frame_rate)
        result["RefFrames"] = from_union([from_int, from_none], self.ref_frames)
        result["SampleRate"] = from_union([from_int, from_none], self.sample_rate)
        result["Score"] = from_union([from_int, from_none], self.score)
        result["SupportsExternalStream"] = from_union([from_bool, from_none], self.supports_external_stream)
        result["TimeBase"] = from_union([from_str, from_none], self.time_base)
        result["Title"] = from_union([from_str, from_none], self.title)
        result["Type"] = from_union([lambda x: to_enum(MediaStreamTypeEnum, x), from_none], self.type)
        result["VideoRange"] = from_union([from_str, from_none], self.video_range)
        result["Width"] = from_union([from_int, from_none], self.width)
        return result


