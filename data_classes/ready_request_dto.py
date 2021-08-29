from util.from_type import *


@dataclass
class ReadyRequestDto:
    """Class ReadyRequest."""
    """Gets or sets a value indicating whether the client playback is unpaused."""
    is_playing: Optional[bool] = None
    """Gets or sets the playlist item identifier of the playing item."""
    playlist_item_id: Optional[UUID] = None
    """Gets or sets the position ticks."""
    position_ticks: Optional[int] = None
    """Gets or sets when the request has been made by the client."""
    when: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReadyRequestDto':
        assert isinstance(obj, dict)
        is_playing = from_union([from_bool, from_none], obj.get("IsPlaying"))
        playlist_item_id = from_union([lambda x: UUID(x), from_none], obj.get("PlaylistItemId"))
        position_ticks = from_union([from_int, from_none], obj.get("PositionTicks"))
        when = from_union([from_datetime, from_none], obj.get("When"))
        return ReadyRequestDto(is_playing, playlist_item_id, position_ticks, when)

    def to_dict(self) -> dict:
        result: dict = {}
        result["IsPlaying"] = from_union([from_bool, from_none], self.is_playing)
        result["PlaylistItemId"] = from_union([lambda x: str(x), from_none], self.playlist_item_id)
        result["PositionTicks"] = from_union([from_int, from_none], self.position_ticks)
        result["When"] = from_union([lambda x: x.isoformat(), from_none], self.when)
        return result


