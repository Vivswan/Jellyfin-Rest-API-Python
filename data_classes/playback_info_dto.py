from util.from_type import *
from data_classes.device_profile import DeviceProfile


@dataclass
class PlaybackInfoDto:
    """Plabyback info dto."""
    """Gets or sets a value indicating whether to allow audio stream copy."""
    allow_audio_stream_copy: Optional[bool] = None
    """Gets or sets a value indicating whether to enable video stream copy."""
    allow_video_stream_copy: Optional[bool] = None
    """Gets or sets the audio stream index."""
    audio_stream_index: Optional[int] = None
    """Gets or sets a value indicating whether to auto open the live stream."""
    auto_open_live_stream: Optional[bool] = None
    """Gets or sets the device profile."""
    device_profile: Optional[DeviceProfile] = None
    """Gets or sets a value indicating whether to enable direct play."""
    enable_direct_play: Optional[bool] = None
    """Gets or sets a value indicating whether to enable direct stream."""
    enable_direct_stream: Optional[bool] = None
    """Gets or sets a value indicating whether to enable transcoding."""
    enable_transcoding: Optional[bool] = None
    """Gets or sets the live stream id."""
    live_stream_id: Optional[str] = None
    """Gets or sets the max audio channels."""
    max_audio_channels: Optional[int] = None
    """Gets or sets the max streaming bitrate."""
    max_streaming_bitrate: Optional[int] = None
    """Gets or sets the media source id."""
    media_source_id: Optional[str] = None
    """Gets or sets the start time in ticks."""
    start_time_ticks: Optional[int] = None
    """Gets or sets the subtitle stream index."""
    subtitle_stream_index: Optional[int] = None
    """Gets or sets the playback userId."""
    user_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlaybackInfoDto':
        assert isinstance(obj, dict)
        allow_audio_stream_copy = from_union([from_bool, from_none], obj.get("AllowAudioStreamCopy"))
        allow_video_stream_copy = from_union([from_bool, from_none], obj.get("AllowVideoStreamCopy"))
        audio_stream_index = from_union([from_int, from_none], obj.get("AudioStreamIndex"))
        auto_open_live_stream = from_union([from_bool, from_none], obj.get("AutoOpenLiveStream"))
        device_profile = from_union([DeviceProfile.from_dict, from_none], obj.get("DeviceProfile"))
        enable_direct_play = from_union([from_bool, from_none], obj.get("EnableDirectPlay"))
        enable_direct_stream = from_union([from_bool, from_none], obj.get("EnableDirectStream"))
        enable_transcoding = from_union([from_bool, from_none], obj.get("EnableTranscoding"))
        live_stream_id = from_union([from_str, from_none], obj.get("LiveStreamId"))
        max_audio_channels = from_union([from_int, from_none], obj.get("MaxAudioChannels"))
        max_streaming_bitrate = from_union([from_int, from_none], obj.get("MaxStreamingBitrate"))
        media_source_id = from_union([from_str, from_none], obj.get("MediaSourceId"))
        start_time_ticks = from_union([from_int, from_none], obj.get("StartTimeTicks"))
        subtitle_stream_index = from_union([from_int, from_none], obj.get("SubtitleStreamIndex"))
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        return PlaybackInfoDto(allow_audio_stream_copy, allow_video_stream_copy, audio_stream_index, auto_open_live_stream, device_profile, enable_direct_play, enable_direct_stream, enable_transcoding, live_stream_id, max_audio_channels, max_streaming_bitrate, media_source_id, start_time_ticks, subtitle_stream_index, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AllowAudioStreamCopy"] = from_union([from_bool, from_none], self.allow_audio_stream_copy)
        result["AllowVideoStreamCopy"] = from_union([from_bool, from_none], self.allow_video_stream_copy)
        result["AudioStreamIndex"] = from_union([from_int, from_none], self.audio_stream_index)
        result["AutoOpenLiveStream"] = from_union([from_bool, from_none], self.auto_open_live_stream)
        result["DeviceProfile"] = from_union([lambda x: to_class(DeviceProfile, x), from_none], self.device_profile)
        result["EnableDirectPlay"] = from_union([from_bool, from_none], self.enable_direct_play)
        result["EnableDirectStream"] = from_union([from_bool, from_none], self.enable_direct_stream)
        result["EnableTranscoding"] = from_union([from_bool, from_none], self.enable_transcoding)
        result["LiveStreamId"] = from_union([from_str, from_none], self.live_stream_id)
        result["MaxAudioChannels"] = from_union([from_int, from_none], self.max_audio_channels)
        result["MaxStreamingBitrate"] = from_union([from_int, from_none], self.max_streaming_bitrate)
        result["MediaSourceId"] = from_union([from_str, from_none], self.media_source_id)
        result["StartTimeTicks"] = from_union([from_int, from_none], self.start_time_ticks)
        result["SubtitleStreamIndex"] = from_union([from_int, from_none], self.subtitle_stream_index)
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        return result


