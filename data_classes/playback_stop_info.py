from util.from_type import *
from data_classes.base_item_dto import BaseItemDto
from data_classes.queue_item import QueueItem


@dataclass
class PlaybackStopInfo:
    """Class PlaybackStopInfo."""
    """Gets or sets a value indicating whether this MediaBrowser.Model.Session.PlaybackStopInfo
    is failed.
    """
    failed: Optional[bool] = None
    """Gets or sets the item."""
    item: Optional[BaseItemDto] = None
    """Gets or sets the item identifier."""
    item_id: Optional[UUID] = None
    """Gets or sets the live stream identifier."""
    live_stream_id: Optional[str] = None
    """Gets or sets the media version identifier."""
    media_source_id: Optional[str] = None
    next_media_type: Optional[str] = None
    now_playing_queue: Optional[List[QueueItem]] = None
    playlist_item_id: Optional[str] = None
    """Gets or sets the play session identifier."""
    play_session_id: Optional[str] = None
    """Gets or sets the position ticks."""
    position_ticks: Optional[int] = None
    """Gets or sets the session id."""
    session_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlaybackStopInfo':
        assert isinstance(obj, dict)
        failed = from_union([from_bool, from_none], obj.get("Failed"))
        item = from_union([BaseItemDto.from_dict, from_none], obj.get("Item"))
        item_id = from_union([lambda x: UUID(x), from_none], obj.get("ItemId"))
        live_stream_id = from_union([from_str, from_none], obj.get("LiveStreamId"))
        media_source_id = from_union([from_str, from_none], obj.get("MediaSourceId"))
        next_media_type = from_union([from_str, from_none], obj.get("NextMediaType"))
        now_playing_queue = from_union([lambda x: from_list(QueueItem.from_dict, x), from_none], obj.get("NowPlayingQueue"))
        playlist_item_id = from_union([from_str, from_none], obj.get("PlaylistItemId"))
        play_session_id = from_union([from_str, from_none], obj.get("PlaySessionId"))
        position_ticks = from_union([from_int, from_none], obj.get("PositionTicks"))
        session_id = from_union([from_str, from_none], obj.get("SessionId"))
        return PlaybackStopInfo(failed, item, item_id, live_stream_id, media_source_id, next_media_type, now_playing_queue, playlist_item_id, play_session_id, position_ticks, session_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Failed"] = from_union([from_bool, from_none], self.failed)
        result["Item"] = from_union([lambda x: to_class(BaseItemDto, x), from_none], self.item)
        result["ItemId"] = from_union([lambda x: str(x), from_none], self.item_id)
        result["LiveStreamId"] = from_union([from_str, from_none], self.live_stream_id)
        result["MediaSourceId"] = from_union([from_str, from_none], self.media_source_id)
        result["NextMediaType"] = from_union([from_str, from_none], self.next_media_type)
        result["NowPlayingQueue"] = from_union([lambda x: from_list(lambda x: to_class(QueueItem, x), x), from_none], self.now_playing_queue)
        result["PlaylistItemId"] = from_union([from_str, from_none], self.playlist_item_id)
        result["PlaySessionId"] = from_union([from_str, from_none], self.play_session_id)
        result["PositionTicks"] = from_union([from_int, from_none], self.position_ticks)
        result["SessionId"] = from_union([from_str, from_none], self.session_id)
        return result


