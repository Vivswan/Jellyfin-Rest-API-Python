from util.from_type import *
from data_classes.play_method import PlayMethod
from data_classes.group_repeat_mode_enum import GroupRepeatModeEnum


@dataclass
class Play:
    """Gets or sets the index of the now playing audio stream."""
    audio_stream_index: Optional[int] = None
    """Gets or sets a value indicating whether this instance can seek."""
    can_seek: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is muted."""
    is_muted: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is paused."""
    is_paused: Optional[bool] = None
    """Gets or sets the now playing media version identifier."""
    media_source_id: Optional[str] = None
    """Gets or sets the play method."""
    play_method: Optional[PlayMethod] = None
    """Gets or sets the now playing position ticks."""
    position_ticks: Optional[int] = None
    """Gets or sets the repeat mode."""
    repeat_mode: Optional[GroupRepeatModeEnum] = None
    """Gets or sets the index of the now playing subtitle stream."""
    subtitle_stream_index: Optional[int] = None
    """Gets or sets the volume level."""
    volume_level: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Play':
        assert isinstance(obj, dict)
        audio_stream_index = from_union([from_int, from_none], obj.get("AudioStreamIndex"))
        can_seek = from_union([from_bool, from_none], obj.get("CanSeek"))
        is_muted = from_union([from_bool, from_none], obj.get("IsMuted"))
        is_paused = from_union([from_bool, from_none], obj.get("IsPaused"))
        media_source_id = from_union([from_str, from_none], obj.get("MediaSourceId"))
        play_method = from_union([PlayMethod, from_none], obj.get("PlayMethod"))
        position_ticks = from_union([from_int, from_none], obj.get("PositionTicks"))
        repeat_mode = from_union([GroupRepeatModeEnum, from_none], obj.get("RepeatMode"))
        subtitle_stream_index = from_union([from_int, from_none], obj.get("SubtitleStreamIndex"))
        volume_level = from_union([from_int, from_none], obj.get("VolumeLevel"))
        return Play(audio_stream_index, can_seek, is_muted, is_paused, media_source_id, play_method, position_ticks, repeat_mode, subtitle_stream_index, volume_level)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioStreamIndex"] = from_union([from_int, from_none], self.audio_stream_index)
        result["CanSeek"] = from_union([from_bool, from_none], self.can_seek)
        result["IsMuted"] = from_union([from_bool, from_none], self.is_muted)
        result["IsPaused"] = from_union([from_bool, from_none], self.is_paused)
        result["MediaSourceId"] = from_union([from_str, from_none], self.media_source_id)
        result["PlayMethod"] = from_union([lambda x: to_enum(PlayMethod, x), from_none], self.play_method)
        result["PositionTicks"] = from_union([from_int, from_none], self.position_ticks)
        result["RepeatMode"] = from_union([lambda x: to_enum(GroupRepeatModeEnum, x), from_none], self.repeat_mode)
        result["SubtitleStreamIndex"] = from_union([from_int, from_none], self.subtitle_stream_index)
        result["VolumeLevel"] = from_union([from_int, from_none], self.volume_level)
        return result


