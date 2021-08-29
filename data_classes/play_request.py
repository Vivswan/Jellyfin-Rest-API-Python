from util.from_type import *
from data_classes.play_command import PlayCommand


@dataclass
class PlayRequest:
    """Class PlayRequest."""
    audio_stream_index: Optional[int] = None
    """Gets or sets the controlling user identifier."""
    controlling_user_id: Optional[UUID] = None
    """Gets or sets the item ids."""
    item_ids: Optional[List[UUID]] = None
    media_source_id: Optional[str] = None
    """Gets or sets the play command."""
    play_command: Optional[PlayCommand] = None
    start_index: Optional[int] = None
    """Gets or sets the start position ticks that the first item should be played at."""
    start_position_ticks: Optional[int] = None
    subtitle_stream_index: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlayRequest':
        assert isinstance(obj, dict)
        audio_stream_index = from_union([from_int, from_none], obj.get("AudioStreamIndex"))
        controlling_user_id = from_union([lambda x: UUID(x), from_none], obj.get("ControllingUserId"))
        item_ids = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("ItemIds"))
        media_source_id = from_union([from_str, from_none], obj.get("MediaSourceId"))
        play_command = from_union([PlayCommand, from_none], obj.get("PlayCommand"))
        start_index = from_union([from_int, from_none], obj.get("StartIndex"))
        start_position_ticks = from_union([from_int, from_none], obj.get("StartPositionTicks"))
        subtitle_stream_index = from_union([from_int, from_none], obj.get("SubtitleStreamIndex"))
        return PlayRequest(audio_stream_index, controlling_user_id, item_ids, media_source_id, play_command, start_index, start_position_ticks, subtitle_stream_index)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioStreamIndex"] = from_union([from_int, from_none], self.audio_stream_index)
        result["ControllingUserId"] = from_union([lambda x: str(x), from_none], self.controlling_user_id)
        result["ItemIds"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.item_ids)
        result["MediaSourceId"] = from_union([from_str, from_none], self.media_source_id)
        result["PlayCommand"] = from_union([lambda x: to_enum(PlayCommand, x), from_none], self.play_command)
        result["StartIndex"] = from_union([from_int, from_none], self.start_index)
        result["StartPositionTicks"] = from_union([from_int, from_none], self.start_position_ticks)
        result["SubtitleStreamIndex"] = from_union([from_int, from_none], self.subtitle_stream_index)
        return result


