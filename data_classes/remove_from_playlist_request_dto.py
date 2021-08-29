from util.from_type import *


@dataclass
class RemoveFromPlaylistRequestDto:
    """Class RemoveFromPlaylistRequestDto."""
    """Gets or sets the playlist identifiers ot the items."""
    playlist_item_ids: Optional[List[UUID]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemoveFromPlaylistRequestDto':
        assert isinstance(obj, dict)
        playlist_item_ids = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("PlaylistItemIds"))
        return RemoveFromPlaylistRequestDto(playlist_item_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PlaylistItemIds"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.playlist_item_ids)
        return result


