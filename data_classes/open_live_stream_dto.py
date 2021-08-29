from util.from_type import *
from data_classes.protocol import Protocol
from data_classes.device_profile import DeviceProfile


@dataclass
class OpenLiveStreamDto:
    """Open live stream dto."""
    """Gets or sets the audio stream index."""
    audio_stream_index: Optional[int] = None
    """Gets or sets the device profile."""
    device_profile: Optional[DeviceProfile] = None
    """Gets or sets the device play protocols."""
    direct_play_protocols: Optional[List[Protocol]] = None
    """Gets or sets a value indicating whether to enable direct play."""
    enable_direct_play: Optional[bool] = None
    """Gets or sets a value indicating whether to enale direct stream."""
    enable_direct_stream: Optional[bool] = None
    """Gets or sets the item id."""
    item_id: Optional[UUID] = None
    """Gets or sets the max audio channels."""
    max_audio_channels: Optional[int] = None
    """Gets or sets the max streaming bitrate."""
    max_streaming_bitrate: Optional[int] = None
    """Gets or sets the open token."""
    open_token: Optional[str] = None
    """Gets or sets the play session id."""
    play_session_id: Optional[str] = None
    """Gets or sets the start time in ticks."""
    start_time_ticks: Optional[int] = None
    """Gets or sets the subtitle stream index."""
    subtitle_stream_index: Optional[int] = None
    """Gets or sets the user id."""
    user_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OpenLiveStreamDto':
        assert isinstance(obj, dict)
        audio_stream_index = from_union([from_int, from_none], obj.get("AudioStreamIndex"))
        device_profile = from_union([DeviceProfile.from_dict, from_none], obj.get("DeviceProfile"))
        direct_play_protocols = from_union([lambda x: from_list(Protocol, x), from_none], obj.get("DirectPlayProtocols"))
        enable_direct_play = from_union([from_bool, from_none], obj.get("EnableDirectPlay"))
        enable_direct_stream = from_union([from_bool, from_none], obj.get("EnableDirectStream"))
        item_id = from_union([lambda x: UUID(x), from_none], obj.get("ItemId"))
        max_audio_channels = from_union([from_int, from_none], obj.get("MaxAudioChannels"))
        max_streaming_bitrate = from_union([from_int, from_none], obj.get("MaxStreamingBitrate"))
        open_token = from_union([from_str, from_none], obj.get("OpenToken"))
        play_session_id = from_union([from_str, from_none], obj.get("PlaySessionId"))
        start_time_ticks = from_union([from_int, from_none], obj.get("StartTimeTicks"))
        subtitle_stream_index = from_union([from_int, from_none], obj.get("SubtitleStreamIndex"))
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        return OpenLiveStreamDto(audio_stream_index, device_profile, direct_play_protocols, enable_direct_play, enable_direct_stream, item_id, max_audio_channels, max_streaming_bitrate, open_token, play_session_id, start_time_ticks, subtitle_stream_index, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioStreamIndex"] = from_union([from_int, from_none], self.audio_stream_index)
        result["DeviceProfile"] = from_union([lambda x: to_class(DeviceProfile, x), from_none], self.device_profile)
        result["DirectPlayProtocols"] = from_union([lambda x: from_list(lambda x: to_enum(Protocol, x), x), from_none], self.direct_play_protocols)
        result["EnableDirectPlay"] = from_union([from_bool, from_none], self.enable_direct_play)
        result["EnableDirectStream"] = from_union([from_bool, from_none], self.enable_direct_stream)
        result["ItemId"] = from_union([lambda x: str(x), from_none], self.item_id)
        result["MaxAudioChannels"] = from_union([from_int, from_none], self.max_audio_channels)
        result["MaxStreamingBitrate"] = from_union([from_int, from_none], self.max_streaming_bitrate)
        result["OpenToken"] = from_union([from_str, from_none], self.open_token)
        result["PlaySessionId"] = from_union([from_str, from_none], self.play_session_id)
        result["StartTimeTicks"] = from_union([from_int, from_none], self.start_time_ticks)
        result["SubtitleStreamIndex"] = from_union([from_int, from_none], self.subtitle_stream_index)
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        return result


