from util.from_type import *


@dataclass
class SetPlaylistItemRequestDto:
    """Class SetPlaylistItemRequestDto."""
    """Gets or sets the playlist identifier of the playing item."""
    playlist_item_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SetPlaylistItemRequestDto':
        assert isinstance(obj, dict)
        playlist_item_id = from_union([lambda x: UUID(x), from_none], obj.get("PlaylistItemId"))
        return SetPlaylistItemRequestDto(playlist_item_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PlaylistItemId"] = from_union([lambda x: str(x), from_none], self.playlist_item_id)
        return result


