from util.from_type import *
from data_classes.base_item_dto import BaseItemDto
from data_classes.queue_item import QueueItem
from data_classes.play_method import PlayMethod
from data_classes.group_repeat_mode_enum import GroupRepeatModeEnum


@dataclass
class PlaybackProgressInfo:
    """Class PlaybackProgressInfo."""
    aspect_ratio: Optional[str] = None
    """Gets or sets the index of the audio stream."""
    audio_stream_index: Optional[int] = None
    brightness: Optional[int] = None
    """Gets or sets a value indicating whether this instance can seek."""
    can_seek: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is muted."""
    is_muted: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is paused."""
    is_paused: Optional[bool] = None
    """Gets or sets the item."""
    item: Optional[BaseItemDto] = None
    """Gets or sets the item identifier."""
    item_id: Optional[UUID] = None
    """Gets or sets the live stream identifier."""
    live_stream_id: Optional[str] = None
    """Gets or sets the media version identifier."""
    media_source_id: Optional[str] = None
    now_playing_queue: Optional[List[QueueItem]] = None
    playback_start_time_ticks: Optional[int] = None
    playlist_item_id: Optional[str] = None
    """Gets or sets the play method."""
    play_method: Optional[PlayMethod] = None
    """Gets or sets the play session identifier."""
    play_session_id: Optional[str] = None
    """Gets or sets the position ticks."""
    position_ticks: Optional[int] = None
    """Gets or sets the repeat mode."""
    repeat_mode: Optional[GroupRepeatModeEnum] = None
    """Gets or sets the session id."""
    session_id: Optional[str] = None
    """Gets or sets the index of the subtitle stream."""
    subtitle_stream_index: Optional[int] = None
    """Gets or sets the volume level."""
    volume_level: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlaybackProgressInfo':
        assert isinstance(obj, dict)
        aspect_ratio = from_union([from_str, from_none], obj.get("AspectRatio"))
        audio_stream_index = from_union([from_int, from_none], obj.get("AudioStreamIndex"))
        brightness = from_union([from_int, from_none], obj.get("Brightness"))
        can_seek = from_union([from_bool, from_none], obj.get("CanSeek"))
        is_muted = from_union([from_bool, from_none], obj.get("IsMuted"))
        is_paused = from_union([from_bool, from_none], obj.get("IsPaused"))
        item = from_union([BaseItemDto.from_dict, from_none], obj.get("Item"))
        item_id = from_union([lambda x: UUID(x), from_none], obj.get("ItemId"))
        live_stream_id = from_union([from_str, from_none], obj.get("LiveStreamId"))
        media_source_id = from_union([from_str, from_none], obj.get("MediaSourceId"))
        now_playing_queue = from_union([lambda x: from_list(QueueItem.from_dict, x), from_none], obj.get("NowPlayingQueue"))
        playback_start_time_ticks = from_union([from_int, from_none], obj.get("PlaybackStartTimeTicks"))
        playlist_item_id = from_union([from_str, from_none], obj.get("PlaylistItemId"))
        play_method = from_union([PlayMethod, from_none], obj.get("PlayMethod"))
        play_session_id = from_union([from_str, from_none], obj.get("PlaySessionId"))
        position_ticks = from_union([from_int, from_none], obj.get("PositionTicks"))
        repeat_mode = from_union([GroupRepeatModeEnum, from_none], obj.get("RepeatMode"))
        session_id = from_union([from_str, from_none], obj.get("SessionId"))
        subtitle_stream_index = from_union([from_int, from_none], obj.get("SubtitleStreamIndex"))
        volume_level = from_union([from_int, from_none], obj.get("VolumeLevel"))
        return PlaybackProgressInfo(aspect_ratio, audio_stream_index, brightness, can_seek, is_muted, is_paused, item, item_id, live_stream_id, media_source_id, now_playing_queue, playback_start_time_ticks, playlist_item_id, play_method, play_session_id, position_ticks, repeat_mode, session_id, subtitle_stream_index, volume_level)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AspectRatio"] = from_union([from_str, from_none], self.aspect_ratio)
        result["AudioStreamIndex"] = from_union([from_int, from_none], self.audio_stream_index)
        result["Brightness"] = from_union([from_int, from_none], self.brightness)
        result["CanSeek"] = from_union([from_bool, from_none], self.can_seek)
        result["IsMuted"] = from_union([from_bool, from_none], self.is_muted)
        result["IsPaused"] = from_union([from_bool, from_none], self.is_paused)
        result["Item"] = from_union([lambda x: to_class(BaseItemDto, x), from_none], self.item)
        result["ItemId"] = from_union([lambda x: str(x), from_none], self.item_id)
        result["LiveStreamId"] = from_union([from_str, from_none], self.live_stream_id)
        result["MediaSourceId"] = from_union([from_str, from_none], self.media_source_id)
        result["NowPlayingQueue"] = from_union([lambda x: from_list(lambda x: to_class(QueueItem, x), x), from_none], self.now_playing_queue)
        result["PlaybackStartTimeTicks"] = from_union([from_int, from_none], self.playback_start_time_ticks)
        result["PlaylistItemId"] = from_union([from_str, from_none], self.playlist_item_id)
        result["PlayMethod"] = from_union([lambda x: to_enum(PlayMethod, x), from_none], self.play_method)
        result["PlaySessionId"] = from_union([from_str, from_none], self.play_session_id)
        result["PositionTicks"] = from_union([from_int, from_none], self.position_ticks)
        result["RepeatMode"] = from_union([lambda x: to_enum(GroupRepeatModeEnum, x), from_none], self.repeat_mode)
        result["SessionId"] = from_union([from_str, from_none], self.session_id)
        result["SubtitleStreamIndex"] = from_union([from_int, from_none], self.subtitle_stream_index)
        result["VolumeLevel"] = from_union([from_int, from_none], self.volume_level)
        return result


