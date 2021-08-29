from util.from_type import *


@dataclass
class MovePlaylistItemRequestDto:
    """Class MovePlaylistItemRequestDto."""
    """Gets or sets the new position."""
    new_index: Optional[int] = None
    """Gets or sets the playlist identifier of the item."""
    playlist_item_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MovePlaylistItemRequestDto':
        assert isinstance(obj, dict)
        new_index = from_union([from_int, from_none], obj.get("NewIndex"))
        playlist_item_id = from_union([lambda x: UUID(x), from_none], obj.get("PlaylistItemId"))
        return MovePlaylistItemRequestDto(new_index, playlist_item_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["NewIndex"] = from_union([from_int, from_none], self.new_index)
        result["PlaylistItemId"] = from_union([lambda x: str(x), from_none], self.playlist_item_id)
        return result


