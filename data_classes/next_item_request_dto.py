from util.from_type import *


@dataclass
class NextItemRequestDto:
    """Class NextItemRequestDto."""
    """Gets or sets the playing item identifier."""
    playlist_item_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NextItemRequestDto':
        assert isinstance(obj, dict)
        playlist_item_id = from_union([lambda x: UUID(x), from_none], obj.get("PlaylistItemId"))
        return NextItemRequestDto(playlist_item_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PlaylistItemId"] = from_union([lambda x: str(x), from_none], self.playlist_item_id)
        return result


